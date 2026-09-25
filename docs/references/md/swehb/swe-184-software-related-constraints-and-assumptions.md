# SWE-184 - Software-related Constraints and Assumptions

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695520. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions

SWE-184 - Software-related Constraints and Assumptions

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695520)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695520&showCommentArea=true&showComments=true#addcomment)

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

4.1.4 The project manager shall include software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software in the software requirements documentation.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-184 History

SWE-184 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.1.4 The project manager shall include software related safety constraints, controls, mitigations and assumptions between the hardware, operator, and software in the software requirements documentation. |
| Difference between C and D | No change |
| D | 4.1.4 The project manager shall include software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software in the software requirements documentation. |

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
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Rationale

To show how the software requirements and software-related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software integration implement the system requirements and system operation. The software and hardware work together to perform a safety-critical function, their roles, precedence, and failure modes need to be documented and understood.

### **1. Mitigating Safety Risks in Complex Systems**

Modern NASA missions involve tightly integrated systems comprising hardware, software, and human operators. Software often plays a critical role in managing safety functions, decision-making processes, and fail-safes. Explicitly documenting *safety constraints, controls, mitigations, and assumptions* ensures that:

* Safety risks stemming from software, hardware, and operator interactions are identified early.
* Preventative measures and mitigation strategies are built into system designs.
* Software requirements address possible hazards before they propagate downstream, reducing the likelihood of system failure or accidents during operation.
* **Why it matters:**

  + The software may be responsible for controlling hardware mechanisms (e.g., actuators, sensors, propulsion systems), and any issue in software logic could lead to hardware failures or unsafe conditions.
  + Explicit documentation of assumptions ensures that safety-critical dependencies are clearly identified and reviewed.

#### **Example:**

In the Mars Orbiter loss, insufficient integration of software guidance algorithms with hardware performance metrics caused miscommunication between systems, leading to a mission failure.

---

### **2. Enhancing Hardware-Software Safety Alignment**

Software interacts directly with hardware components, such as sensors, actuators, and controllers, to implement safety-critical functions. For instance:

* **Constraints:** Define operational ranges (e.g., temperature or pressure thresholds) that the software will monitor and enforce to avoid hardware damage or unsafe conditions.
* **Controls:** Specify software mechanisms (e.g., error checking, automated shutdown) that act as safeguards to prevent hardware malfunction or physical damage.
* **Mitigations:** Identify fallback actions (e.g., switching to redundant systems) in case of hardware or software failures.
* **Why it matters:**

  + Without explicitly defined constraints, controls, and mitigations, software requirements cannot effectively prevent hardware-related hazards.
  + Proper alignment ensures that hardware limitations are accounted for in software logic, preventing unsafe interactions.

#### **Example:**

Propulsion systems rely on software to maintain proper pressure and temperature within the thrusters. Without explicitly defining constraints such as "software must monitor pressure between X and Y psi," there is a risk of thruster damage or explosion.

---

### **3. Incorporating Human Operators into the Safety Model**

Human operators play an essential role in the safety of NASA missions, especially during high-risk procedures (e.g., spacecraft docking, critical system overrides). Software requirements must include assumptions about operator interactions to ensure safety in scenarios requiring manual inputs or overrides. This involves:

* **Constraints:** Specify the conditions under which human intervention is allowed (e.g., "operator must confirm action if system enters fault mode").
* **Controls:** Define how software communicates critical system conditions to the operator (e.g., alarm thresholds, visual alerts).
* **Mitigations:** Document fallback actions for cases where operator behavior conflicts with software expectations (e.g., automated override if human error is detected).
* **Why it matters:**

  + Ambiguity in assumptions about operator behavior can lead to unsafe outcomes, such as actions taken by operators in contradictory or hazardous conditions without software safeguards.

#### **Example:**

The crash of Air France Flight 447 highlighted the dangers of poor alignment between human operators and software automation. Ambiguous software assumptions about pilot actions during stall conditions led to a tragic loss of control.

---

### **4. Preventing Cascading Failures Across System Components**

In tightly connected systems, failures in hardware, software, or operator interactions can create cascading failures. For example:

* A hardware failure due to environmental stress (e.g., extreme heat) could result in untested software behavior that misinterprets sensor data and incorrectly alerts the operator, leading to unsafe actions.

By explicitly documenting safety constraints, controls, mitigations, and assumptions, the requirements provide guidance to manage these interdependencies and ensure that:

* Software includes fault-tolerant mechanisms.
* Hardware-software interfaces are designed to support error detection and proper recovery.
* Operators are provided with clear decision-making tools to prevent unsafe escalation.
* **Why it matters:**

  + Cascading failures can cause unexpected chain reactions that are both expensive and dangerous to resolve during testing, operations, or mission execution.

#### **Example:**

In the loss of the Mars Polar Lander, software was assumed to detect touchdown via hardware sensor signals. Misaligned assumptions between hardware and software regarding transient signals led to premature engine shutdown, resulting in the spacecraft’s crash.

---

### **5. Supporting Certification and Regulatory Compliance**

Safety-critical systems developed by NASA must comply with aerospace standards for safety and reliability. Industry standards such as **DO-178C** (Software Considerations in Airborne Systems and Equipment Certification), **ISO 26262** (Functional Safety for Transportation Systems), and **NASA-STD-8719.17** emphasize the explicit identification and documentation of safety controls, constraints, and assumptions across system components.

* Explicit inclusion of these elements in software requirements documentation ensures project compliance and provides auditable evidence during system certification.
* **Why it matters:**

  + Failure to comply with safety standards or produce evidence of integrated safety measures can lead to delays, increased costs, or even rejection of the system during review.

#### **Example:**

NASA missions involving crewed spacecraft, such as the Space Shuttle and Artemis, require detailed documentation of software-driven safety measures for certification by regulatory bodies.

---

### **6. Enabling Verification and Validation (V&V)**

Software requirements that include clearly defined safety constraints, controls, mitigations, and assumptions between hardware, operator, and software lay the foundation for effective **Verification and Validation (V&V)** activities. This enables:

* **Testing of constraints:** Validating that software implements proper checks and limits to keep systems safe (e.g., testing maximum temperature thresholds for software alerts).
* **Testing of controls:** Verifying that safety mechanisms operate as intended (e.g., automatically shutting down a subsystem during fault conditions).
* **Validation of assumptions:** Ensuring requirements align with actual system behavior (e.g., how operators interact with safety-critical systems during simulations).
* **Why it matters:**

  + V&V processes help confirm that the implemented software safety measures effectively reduce risks during real-world operation.

#### **Example:**

Mission-critical systems like life support systems on crewed spacecraft rely on robust V&V to ensure that software correctly monitors and controls environmental conditions (e.g., oxygen levels, CO₂ scrubbers) under varying operator inputs.

---

### **7. Preventing Overlooked Safety Dependencies**

Safety constraints, controls, mitigations, and assumptions serve as the bridge between hardware, software, and human operators. Documenting these explicitly ensures that no critical dependencies are overlooked, such as:

* Sensor data assumptions for software logic.
* Environmental conditions affecting hardware-software performance.
* Operator workflows contradicting software automation.

This documentation enables teams across disciplines (e.g., software engineers, systems engineers, safety analysts, operators) to collaboratively address potential gaps and ensure seamless integration.

* **Why it matters:**
  + Software failures are often traced to overlooked dependencies during requirements analysis, leading to costly redesigns or mission failures.

#### **Example:**

Without assumptions about hardware latency, software delays in interpreting sensor data can lead to false-positive diagnostics, triggering unnecessary operator overrides or system shutdowns.

---

### **8. Guiding Design and Development Decisions**

Safety considerations documented during the requirements phase serve as the foundation for decision-making throughout the software development lifecycle. Explicitly captured constraints, controls, mitigations, and assumptions guide:

* Architectural decisions (e.g., redundancy, fault-tolerance mechanisms).
* Design choices (e.g., prioritizing safety-critical functional paths over non-critical functionalities).
* Testing priorities (e.g., identifying high-risk scenarios for early testing).
* **Why it matters:**

  + Early integration of safety measures into software design prevents costly rework and ensures consistent alignment with system-level safety objectives.

#### **Example:**

The introduction of redundant fail-safe systems in the Apollo program was guided by software requirements emphasizing fault tolerance and operator safety during critical mission phases.

---

### **9. Facilitating Cross-Disciplinary Understanding**

Detailed safety documentation ensures that hardware engineers, software developers, operators, testers, and safety personnel share a common understanding of system safety objectives. This fosters collaboration and reduces miscommunications that may lead to unsafe designs or gaps in implementation.

* **Why it matters:**
  + Misalignment between disciplines, particularly hardware-software integration, has historically resulted in project delays and failures.

#### **Example:**

Proper alignment across disciplines helped ensure the success of the Curiosity rover by explicitly defining constraints, controls, and mitigation strategies for software-hardware interactions during critical landing phases.

---

### **Conclusion**

This requirement ensures that software-related safety aspects are explicitly captured in requirements documentation to address risks stemming from the interaction between hardware, human operators, and software systems. By mitigating safety risks, aligning hardware-software safety measures, enabling cross-disciplinary collaboration, supporting certification, and guiding effective V&V, this requirement safeguards NASA missions against failures while ensuring operational excellence and mission success.

# 3. Guidance

This requirement emphasizes the integration of safety-related considerations within software requirements to ensure the safe operation of complex systems involving software, hardware, and human operators. Below is detailed engineering guidance to help fulfill this requirement effectively.

The software-related safety constraints, controls, mitigations, and assumptions specified in software requirements documentation serve as the foundation for designing safe systems that integrate software, hardware, and human operators. By rigorously addressing these facets during requirements definition, project managers establish a clear path for identifying and mitigating risks, aligning multidisciplinary teams, and ensuring system success—all critical for NASA missions where safety is paramount.

---

### **1. Clearly Define Software Safety Constraints**

Ensure software requirements explicitly state constraints that prevent unsafe conditions resulting from software interaction with hardware or operators. Constraints provide operational boundaries that software must enforce to guarantee safety in all scenarios.

#### **Key Actions:**

* **Identify boundaries:** Examples include temperature, pressure, velocity, or timing thresholds monitored by sensors and enforced by software logic. Ensure constraints align with hardware and system limitations.
  + Example: "Software shall prevent engine initiation if the temperature sensor reads below 10°C or above 120°C."
* **Define acceptable operator behavior:** Specify constraints around manual inputs, overrides, or unanticipated human actions that could affect software and hardware safety.
  + Example: "Software shall require operator confirmation at all critical stages before overriding safety protocols."
* **Integrate environmental constraints:** Specify environmental conditions (e.g., heat, vibration, radiation) that could affect system performance and ensure safety under these conditions.

---

### **2. Develop Safety Controls**

Safety controls are mechanisms embedded in software to detect, alert, and mitigate unsafe behavior or conditions. These controls are critical to protecting hardware, operators, and the success of the mission.

#### **Key Actions:**

* **Implement fault detection and diagnostics:** Ensure software can detect hardware anomalies, sensor failures, or invalid operator inputs in real time.
  + Example: "Software shall detect a pressure sensor fault within 500ms and transition to safe mode."
* **Introduce automated safety actions:** Define software controls to take corrective action in the event of unsafe conditions or failures.
  + Example: "Software shall initiate an emergency shutdown sequence if pressure exceeds 300 psi."
* **Develop safety logic for human interaction:** Include controls that limit unsafe operator actions or provide proper guidance during critical situations.
  + Example: "Software shall issue an audible and visual alarm when the operator attempts to issue commands that conflict with active safety protocols."

#### **Tools/Standards for Controls Development:**

* NASA-STD-8719.13 (*Software Safety*)
* Fault detection algorithms (e.g., for redundancy management, transient detection).

---

### **3. Define Mitigation Strategies**

Software requirements must include mitigation strategies to address failures or hazards that cannot be entirely avoided. These strategies provide fallback mechanisms to maintain system safety under adverse conditions.

#### **Key Actions:**

* **Design fallbacks and redundancy:** Define alternative actions or mechanisms software can switch to in the event of primary system failure.
  + Example: "Software shall switch to redundant hardware sensors if the primary sensor fails validation."
* **Include degraded mode operations:** Specify safe operational modes activated by the software when nominal functionality is compromised.
  + Example: "Software shall enter degraded mode if power input levels drop below operational thresholds."
* **Use failure isolation techniques:** Incorporate requirements for fault isolation to prevent cascading failures across system components.
  + Example: "Software shall isolate subsystem errors to prevent propagation to mission-critical functions."

#### Supplemental Considerations:

* Mitigation strategies should be verified through hazard analysis (e.g., FMECA - Failure Modes and Effects Criticality Analysis).
* Validate fallback mechanisms through testing under failure conditions.

---

### **4. Document Assumptions Explicitly**

Include all assumptions related to safety in software requirements documentation. Assumptions about hardware behavior, operator inputs, environmental conditions, or mission-critical scenarios provide context for safety requirements and allow for validation during system design and testing.

#### **Key Actions:**

* **Hardware assumptions:** Clearly state expectations around hardware (e.g., sensor accuracy, actuation speed, latency), ensuring software requirements account for system limitations.
  + Example: "It is assumed that temperature sensors will provide accurate readings within ±2°C."
* **Operator assumptions:** Define assumptions about operator behavior, skills, training levels, and familiarity with safety systems.
  + Example: "It is assumed that operators are trained to manually override automated controls in critical situations."
* **Environmental assumptions:** Reflect assumptions on environmental conditions (e.g., radiation levels, gravitational forces) within software requirements documentation.
  + Example: "Software is developed under the assumption of nominal solar radiation levels during operation."

#### Helpful Tip:

Validate assumptions during system-level testing and safety workshops involving cross-disciplinary teams (hardware, software, operations).

---

### **5. Implement Bi-Directional Traceability**

Ensure that all safety-related constraints, controls, mitigations, and assumptions in software requirements directly map to system-level requirements and higher-level safety analyses. Bi-directional traceability ensures comprehensive safety coverage.

#### **Key Actions:**

* **Trace system-level to software-level requirements:** Link software requirements to parent system requirements (e.g., performance, safety, reliability) to avoid gaps in critical functionality.
  + Example: "Safety-critical software functions shall trace to system-level fail-safe modes defined in the mission safety plan."
* **Trace software requirements to test cases:** Build test coverage that explicitly validates constraints, controls, mitigations, and assumptions.
  + Example: "Test Case #001 – Verify software enforces a maximum temperature threshold of 120°C under sensor input fluctuation."

#### Tools/Standards for Traceability:

* Requirements management tools like IBM DOORS or Jama Connect.
* NASA-STD-8719.8 - Software Safety Standard Technical Procedures.

---

### **6. Collaborate Across Disciplines**

Effective integration of software safety measures requires collaboration among software engineers, hardware engineers, operators, and safety analysts. These teams ensure all interactive dependencies are clearly defined and validated.

#### **Key Actions:**

* **Hold safety workshops:** Bring together cross-disciplinary teams to align software requirements with hardware, operator, and safety expectations. These meetings help define constraints and incompatibilities early.
* **Early involvement of safety personnel:** Identify safety hazards during requirements definition with input from safety analysts.
* **Conduct joint reviews:** Involve hardware teams to ensure software requirements meet constraints imposed by physical systems, and operations teams to validate assumptions about operator interaction.

---

### **7. Use Formal Safety Analysis Techniques**

Leverage formal safety analysis techniques to ensure all relevant hazards between hardware, operators, and software are identified, documented, and mitigated through software requirements.

#### **Key Actions:**

* **Hazard analysis:** Perform systematic hazard analysis to identify risks arising from hardware/software/operator interactions (e.g., generate hazard logs for safety-critical functions).
* **Failure modes analysis:** Use methods such as FMECA (Failure Modes, Effects, and Criticality Analysis) or fault tree analysis to identify system vulnerabilities and document mitigation requirements.
* **Risk assessment:** Quantify risks for all identified hazards and validate that software safety measures reduce risks to acceptable levels.

---

### **8. Perform Rigorous Testing and Verification**

Ensure all safety-related constraints, controls, mitigations, and assumptions are testable and include validation criteria in the software requirements documentation.

#### **Key Actions:**

* **Safety-specific test cases:** Write test cases that explicitly validate all safety-related requirements.
  + Example: "Test Case #023 – Validate that software automatically shuts down thrusters if temperature thresholds exceed operational limits."
* **Develop fault injection testing:** Simulate hardware failures or invalid operator inputs to verify that safety mitigations operate as intended.
  + Example: Simulate faulty sensor inputs to verify fallback to redundant sensors.
* **Perform end-to-end validation:** Ensure safety-related requirements are tested under realistic mission conditions.

---

### **9. Follow Relevant Standards and Guidelines**

Adhere to both NASA-specific and industry standards for software-related safety requirements.

#### Key Standards to Reference:

* **NASA-STD-8719.13** - Software Safety Standard.
* **NASA-STD-8719.8** - Safety and Mission Assurance.
* **DO-178C** - Software Considerations in Airborne Systems Certification (if applicable).
* **ISO 26262** - Functional Safety for Automotive Systems (for robotics or autonomous operations).

Using these standards ensures comprehensive coverage and certifiability of safety requirements.

---

## 3.1 Safety Constraints And Constraints

All software-related safety constraints and constraints between the hardware, operator, and software are documented in the software requirements documentation.  When the software, hardware, or operator performs a safety-critical function, document the hardware, software, and operator (1) roles in that function, (2) the precedence, and (3) the failure modes as well as any known constraints, controls,  mitigations, conditions, timing constraints, limits, and wear-out factors that impact how software needs to respond. [271](#_tabs-<p></p>)

Also, it is strongly recommended that software requirements developers seek out inputs from the operators and hardware engineers, asking about constraints and operating conditions the software may need to account for.

Software-related safety constraints, controls, mitigations, and assumptions between the hardware, operator and the software should be defined in the software requirements documentation, including all software-related safety constraints on a Class D software project.  Software-related safety constraints, controls, mitigations, and assumptions between the hardware, operator and the software should always be done on all safety-critical software components.

## 3.2 Safety Requirements

Software related safety requirements which include constraints and assumptions between the hardware, operator, and software will be documented in the software requirements documentation.  While the Software Requirement Specification ([5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)) is not required to have a specific section that addresses the safety requirements, safety requirements are to be included in the SRS and designated (marked) as safety requirements. See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements).

* Any safety-related constraints between the hardware and software are included in the software requirements documentation. That is, when the software and hardware work together to perform a safety-critical function, their roles, precedence, and failure modes are documented and understood.[271](#_tabs-<p></p>)
* Software safety requirements are derived from the system safety requirements, environmental requirements, standards, program specifications, vehicle or facility requirements, interface requirements, system hazard reports, and system hazard analyses. [271](#_tabs-<p></p>) See also Topic [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations).
* System safety analyses, including the PHA [Preliminary Hazard Analysis], subsequent system hazard analyses, and software safety analyses are used to create new or identify existing, software requirements necessary to mitigate or resolve any hazards where software is a potential cause or contributor or enable the software to be used as a hazard control. Such requirements are designated as software safety requirements. [271](#_tabs-<p></p>)
* Software safety requirements include the modes or states of operation under which they are valid and any modes or states in which they are not applicable. [271](#_tabs-<p></p>)

* Software safety personnel, system safety personnel, and the Center Safety and Mission Assurance (SMA) organization work together to develop and identify or provide assistance in identifying software safety requirements. [271](#_tabs-<p></p>)

See also [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements), Topic [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVD/pages/102695554/6.2+-+Checklist+for+General+Software+Safety+Requirements),

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVD/pages/102695554/6.2+-+Checklist+for+General+Software+Safety+Requirements) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

# 4. Small Projects

For a smaller project with limited resources and scope, this guidance focuses on structured yet streamlined approaches to ensure compliance with this safety-critical requirement. The goal is to strike a balance between satisfying the requirement and avoiding unnecessary overhead while maintaining project safety and quality.

---

### **1. Keep It Concise and Context-Specific**

Focus only on the essential safety-related interactions relevant to the small project. Evaluate the size, complexity, and level of safety impact to prioritize efforts.

#### **Steps:**

1. **Define Boundaries:**

   * Start with a high-level assessment of the hardware, software, and operator roles in the system. Clearly define the scope of their interdependencies and focus only on safety-related elements applicable to the project.
     + Example: If the software is for a temperature monitoring subsystem, only document safety constraints, mitigations, and assumptions related to temperature thresholds, hardware sensors, and operator actions.
2. **Identify Safety-Critical Requirements First:**

   * Use functional decomposition to isolate system needs tied to safety.
   * Example for a robotic system: "Software shall monitor light sensor data and enforce an automated stop if obstacle distance is less than 5cm."

#### Output:

* A short "Safety Requirements Section" or a checklist in the Software Requirements Documentation that addresses only the essential constraints, controls, mitigations, and assumptions.

---

### **2. Use Simple Templates or Checklists**

Small projects can avoid large documentation overhead by using simplified templates or checklists to capture safety-related information instead of overly detailed technical reports.

#### **Steps:**

1. **Safety Constraints:**
   * Define operating limits imposed on hardware or other system aspects.
     + Example: "Temperature must remain between 0–100°C; no commands shall be executed outside this range."
2. **Safety Controls:**
   * Document software responses to detected unsafe conditions.
     + Example: "If temperature exceeds 100°C, software shall trigger a system shutdown and generate an operator alert with a failure code."
3. **Safety Mitigations:**
   * Outline fallback mechanisms to reduce risks when something unsafe happens.
     + Example: "If the primary hardware sensor fails, software shall switch to the redundant backup sensor."
4. **Assumptions:**
   * Include key assumptions about external factors (hardware reliability, operator competence, environment).
     + Example: "It is assumed that operators will understand alert codes and follow shutdown procedures properly."

#### Output:

Use a simple 1-2 page table, like this example:

| **Safety Category** | **Details** |
| --- | --- |
| Safety Constraint | Software must maintain actuator speed below 2 m/s under normal conditions. |
| Safety Control | Software shall stop actuator motion if speed exceeds 2.5 m/s and notify the operator using an audible alert. |
| Safety Mitigation | If the actuator sensor fails, software shall enter "safe mode" and notify the operator within 1 second. |
| Assumption | Operator is trained to perform manual override within 30 seconds of alert activation. |

---

### **3. Perform a Simplified Safety Analysis**

In small projects, do a lightweight safety analysis to identify risks and integrate safety measures into the requirements documentation.

#### **Steps:**

1. **Identify Hazards:**

   * Use brainstorming, a hazard checklist, or ask simple questions:
     + What could go wrong with hardware that software needs to handle (e.g., sensor failures, actuator malfunctions)?
     + What unsafe operator actions could occur?
     + What is the worst-case scenario if the software fails?
   * Example: For a power control system, identify "over-voltage" as a hazard.
2. **Define Requirements for Each Hazard:**

   * Example Hazard: "Over-voltage could damage circuit hardware."
   * Safety Requirements:
     + "Software shall monitor voltage levels from the hardware sensor every 1 second."
     + "If voltage exceeds 10% above operating range, software shall disable the circuit breaker."

#### Output:

Generate a simple Hazard Log table:

| **Hazard** | **Mitigation Strategy** | **Software Requirement** |
| --- | --- | --- |
| Sensor failure | Use fallback to redundant backup sensor. | "Software shall detect sensor failures and switch to the redundant sensor within 500ms." |
| Operator error | Add an automated fail-safe stop feature for unanticipated manual inputs. | "Software shall reject conflicting commands and provide error feedback to the operator." |
| Over-voltage fault | Shut down systems during unsafe voltage levels. | "Software shall disable the breaker if voltage exceeds 10% of predefined thresholds." |

---

### **4. Focus on Practical Testing and Validation**

Ensure that safety-related requirements are straightforward to validate via testing. Small projects can use manual reviews, basic automated tests, or simulations to confirm compliance with safety constraints, controls, and mitigations.

#### **Steps:**

1. **Define Test Scenarios for Safety-Related Requirements:**

   * Relate safety-critical requirements to specific test scenarios.
   * Example: For a robotic arm, a test scenario could involve simulating an "emergency stop" triggered by a detected obstacle.
2. **Perform Basic Fault Injection Testing (if feasible):**

   * Simulate simple failures (e.g., sensor disconnects, incorrect operator inputs) and verify software behavior.
     + Example: Remove the power input to a sensor during a test to observe if the software switches to the redundant backup sensor.
3. **Operator Validation:**

   * Test operator assumptions in the field or via simulation to ensure documented expectations (e.g., responses to alerts) are realistic.

#### Outputs:

* Validation Checklist: Summarize test results for each safety-related requirement.
  + **Example:**
    - Requirement: “Software shall enter safe mode if temperature rises above 100°C.”
    - Test Result: Successfully triggered safe mode in 3/3 test cases.

---

### **5. Prioritize Communication and Documentation**

In small projects, effective communication between the project team is crucial. Focus on keeping documentation concise, but ensure clarity, especially for stakeholders (e.g., developers, testers, operators).

#### **Key Actions:**

1. **Engage Stakeholders Early:**

   * Even in small projects, make sure safety-critical requirements account for input from:
     + Hardware engineers: Ensure hardware limits are well-understood.
     + Operators: Validate workflows and assumptions.
     + Software developers: Assess implementation feasibility.
2. **Use Diagrams for Clarity:**

   * Include simple system interaction diagrams to visualize safety interactions between hardware, software, and operators.

**Example:**  
Create a safety model using inputs/outputs:

* **Inputs:** Sensors, operator commands.
* **Outputs:** Actuator controls, operator alerts, fail-safes.

---

### **6. Adopt Lightweight Tools and Standards**

Leverage tools and practices suited for small projects to manage effort and simplify workflows.

#### **Tools and Practices:**

* **Requirements Tools:** Use lightweight tools for requirements and traceability (e.g., Excel, Confluence, Jira). Avoid heavyweight requirements management systems unless absolutely necessary.
* **Standards:** Follow simplified interpretations of NASA-STD-8719.13 (Software Safety) and NASA-STD-8739.8 (Software Assurance). Focus on core concepts (e.g., hazard tracking, requirement traceability).

---

### **Summary Checklist for Small Projects**

To fulfill Requirement 4.1.4, ensure the following are in place:

1. **Safety Constraints:** Defined operating limits for software interactions with hardware and operators.
2. **Safety Controls:** Automated or manual mechanisms to prevent unsafe outcomes.
3. **Safety Mitigations:** Fallback mechanisms for failures (e.g., switching to redundant hardware).
4. **Assumptions:** Clearly stated expectations about hardware performance, operators, and environmental conditions.
5. **Testing Plan:** Validation of safety measures under both nominal and failure scenarios.
6. **Documentation:** Concise safety requirements and hazard logs included in project documentation.

By following this streamlined approach, small projects can effectively integrate safety measures into software requirements without overwhelming the team or resources. Proper implementation will ensure safety, reliability, and mission success.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Here are several **NASA Lessons Learned** that are relevant to Requirement 4.1.4, emphasizing the importance of including software-related safety constraints, controls, mitigations, and assumptions between hardware, operators, and software in the software requirements documentation. These lessons are extracted from NASA's publicly available resources and documented failures, as well as successful mitigation strategies.

---

### **Lesson 1: Mars Polar Lander (1999)**

**Incident:**  
The Mars Polar Lander failure was caused by premature shutdown of the descent engines due to software misinterpreting vibrations from deployed landing legs as a touchdown signal. This critical misunderstanding between hardware and software interactions was traced back to gaps in the requirements documentation.

**Key Takeaways:**

* **Importance of Assumptions**: Assumptions about how hardware signals (e.g., vibrations) would be handled by software were not well-documented. This resulted in the software incorrectly processing transient data from hardware sensors.
* **What Went Wrong:**

  + Lack of clearly defined safety mitigations for handling transient signals led to the failure of the descent system.
  + The absence of fallback strategies for validating landing conditions caused a cascading failure during critical mission phases.

**Guidance for Requirement 4.1.4:**

* Include explicit software assumptions when interpreting hardware sensor data, especially in mission-critical phases.
* Implement safety controls to validate sensor inputs against redundant systems before taking irreversible actions.

---

### **Lesson 2: Mars Climate Orbiter (1999)**

**Incident:**  
The Mars Climate Orbiter was lost due to a mismatch between metric (N-m) and imperial (lbf-s) units in software and hardware calculations for trajectory corrections. This resulted in improper thrust commands, causing the spacecraft to enter the Martian atmosphere at an unsafe angle.

**Key Takeaways:**

* **Importance of Constraints:**  
  Failure to define unit consistency constraints in software requirements regarding trajectory calculations led to hardware-software misalignment.
* **What Went Wrong:**

  + Software-to-hardware interface requirements did not explicitly specify unit conversions between systems.
  + Critical controls to verify thrust commands before execution (such as range validation or unit compatibility checks) were absent.

**Guidance for Requirement 4.1.4:**

* Define constraints that ensure consistent interfaces, especially for calculations involving units, timing, and operational thresholds.
* Incorporate validation controls in software to detect and correct discrepancies between hardware and software inputs.

---

### **Lesson 3: Space Shuttle Challenger Disaster (1986)**

**Incident:**  
The Challenger disaster was largely caused by the failure of O-ring seals in the rocket boosters due to freezing temperatures. While the root cause was hardware-related, the software’s inability to process temperature as part of the launch constraints exacerbated the problem.

**Key Takeaways:**

* **Importance of Environmental Factors:**  
  The software requirements did not adequately account for environmental constraints (such as minimum operating temperatures affecting hardware components).
* **What Went Wrong:**

  + Software assumptions about hardware operating within nominal temperature ranges were invalid during launch conditions.
  + Absence of mitigations to verify environmental suitability before initiating launch likely contributed to the inability to detect unsafe conditions.

**Guidance for Requirement 4.1.4:**

* Explicitly document environmental safety constraints in software requirements, including operational temperature ranges, pressure limits, or radiation thresholds for hardware.
* Include controls and mitigations for handling environmental violations (e.g., halting operations, issuing alerts).

---

### **Lesson 4: NASA Helios Prototype Loss (2003)**

**Incident:**  
The Helios solar-powered aircraft disintegrated at high altitude due to dynamic instability caused by improper handling of flight control logic during turbulent conditions. This failure revealed gaps between software assumptions about hardware performance and real-world aerodynamic factors.

**Key Takeaways:**

* **Importance of Robust Safety Mitigations:**  
  Safety mitigations for handling severe aerodynamic instability were either insufficient or not defined in software requirements documentation.
* **What Went Wrong:**

  + Software assumptions relied on nominal aerodynamic performance data without accounting for hardware limitations during turbulent conditions.
  + Controls to detect and respond to abnormal airflow dynamics were absent.

**Guidance for Requirement 4.1.4:**

* Include explicit assumptions about hardware performance and environmental conditions in software requirements.
* Implement real-time safety controls that detect and react to instability or abnormal system behavior (e.g., turbulence, irregular sensor data).

---

### **Lesson 5: Apollo 11—Success Through Redundancy (1969)**

**Incident:**  
On the Apollo 11 lunar landing mission, the onboard computer issued a series of "1202 Program Alarms" caused by task overload during descent. Despite this anomaly, proper mitigations and safety design allowed the mission to succeed.

**Key Takeaways:**

* **Importance of Fallback Strategies:**  
  Redundant safety controls and mitigations prevented mission failure despite unexpected software behavior caused by hardware overload.
* **What Went Right:**

  + Software failovers were designed to prioritize critical tasks over non-essential operations during task overload conditions.
  + Clear documentation of hardware-software interactions enabled rapid diagnosis and resolution by engineers and astronauts.

**Guidance for Requirement 4.1.4:**

* Include fallback strategies in software requirements to prioritize safety-critical operations during task overload or system faults.
* Ensure that key assumptions about hardware capacity and software task prioritization are explicitly documented.

---

### **Lesson 6: Genesis Spacecraft Failure (2004)**

**Incident:**  
The Genesis spacecraft experienced a crash due to the deployment of its parachutes failing to initiate. This was caused by unresolved software issues related to sensor data-handling logic.

**Key Takeaways:**

* **Importance of Interaction Constraints and Controls:**  
  Software requirements lacked precise constraints and controls for validating sensor data before triggering safety mechanisms such as parachute deployment.
* **What Went Wrong:**

  + Assumptions about sensor behavior were incorrect, leading the software to misinterpret critical inputs.
  + A lack of mitigations (e.g., redundant checks or alternative deployment mechanisms) caused the failure.

**Guidance for Requirement 4.1.4:**

* Document sensor constraints in software requirements, including operational ranges and error-handling strategies.
* Implement mitigations such as redundant hardware/software checks for safety-critical actions triggered by sensor data.

---

### **Lesson 7: James Webb Space Telescope (JWST)—Success Through Rigorous Testing**

**Incident:**  
The JWST faced challenges during its development, especially in integrating its complex software systems with hardware controls for the precise positioning of mirrors. Early identification of safety concerns between hardware and software reduced risk during operations.

**Key Takeaways:**

* **Importance of Testing Safety Mitigations:**  
  Comprehensive testing of safety controls and mitigations during development prevented significant failures during deployment.
* **What Went Right:**

  + Rigorous requirements documentation explicitly outlined hardware constraints, software safety controls, and fallback mitigations.
  + Thorough validation processes incorporated fault injection testing for sensor failures and operator errors.

**Guidance for Requirement 4.1.4:**

* Include robust testing protocols for safety-related software requirements, especially for fallback mechanisms tied to hardware or operator interactions.
* Validate safety assumptions during development using realistic mission conditions.

---

### **Summary of Lessons Learned**

These historical examples highlight key aspects of safety-related failures and successes in NASA projects:

#### **What to Include in Software Requirements Documentation:**

1. **Constraints:** Clearly define limits (e.g., operational ranges for temperature, pressure, velocity) to avoid hardware or software-induced failures.
2. **Controls:** Implement mechanisms to handle detected unsafe conditions (e.g., automated shutdowns, alarms).
3. **Mitigations:** Provide fallback strategies for sensor failures, operator errors, or environmental violations.
4. **Assumptions:** Explicitly state expectations about hardware behavior, operator inputs, and environmental conditions.
5. **Testing:** Validate safety-related requirements under realistic mission conditions, including fault injection testing.

By applying these lessons learned, projects can avoid repeating past mistakes and ensure safer integration of hardware, software, and operator interactions to meet mission objectives successfully.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Project's hardware designers to include a debug register that is both readable and writable](https://software.gsfc.nasa.gov/lesson-details/160/). **Lesson Number 160**: The recommendation states: "Advise the project's hardware designers to include a debug register that is both readable and writable, to enable software developers to test read and write accesses to the hardware."
* [Document behavior of legacy systems beyond what is captured in ICDs](https://software.gsfc.nasa.gov/lesson-details/164/). **Lesson Number 164**: The recommendation states: "Avoid schedule delays by documenting behavior of legacy systems (if not already documented) beyond what is captured in ICDs."
* [Engage system test leads in flight software (FSW) requirements](https://software.gsfc.nasa.gov/lesson-details/299/). **Lesson Number 299**: The recommendation states: "Before the System Requirements Review (SRR), reach out to your system test lead (or someone with experience with testing similar systems) to review your electrical and flight software (FSW) architecture, requirements, and use cases. Specifically, ask them to identify any changes that would simplify the system testing."

# 7. Software Assurance

**SWE-184 - Software-related Constraints and Assumptions**

4.1.4 The project manager shall include software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software in the software requirements documentation.

**Background Context**:  
Requirement 4.1.4 mandates that software safety constraints, controls, mitigations, and assumptions between hardware, operator, and software be explicitly included during the creation and analysis of software requirements documentation. Software assurance (SA) plays a critical role in ensuring that these safety elements are properly analyzed, validated, and integrated into the system as a whole. The following updated and expanded guidance refines the original content for clarity, actionability, and alignment with best practices.

This improved software assurance guidance provides clear, actionable steps for satisfying Requirement 4.1.4. It focuses on proactive analysis, validation, and documentation of safety-critical elements in the software requirements. By ensuring early integration of safety considerations, the project minimizes lifecycle risks, avoids costly redesign, and ensures mission success. Close collaboration between engineering and assurance teams is emphasized to balance safety, reliability, and development efficiency.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Analyze and confirm that the software requirements documentation contains the software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and the software.

## 7.2 Software Assurance Products

---

**Objective:** To ensure thorough analysis and assurance of safety-related software requirements throughout the project lifecycle, including their alignment with system safety objectives.

#### 1. **System Hazard Analyses Including Software**

* Maintain a copy of **system hazard analyses** (e.g., Preliminary Hazard Analysis (PHA), Fault Tree Analysis (FTA), Failure Mode and Effect Analysis (FMEA)) that explicitly include software components as potential hazard contributors or controllers. These analyses must be reviewed to:
  + Identify and document software-induced hazards or hazard mitigations.
  + Trace these hazards to corresponding software requirements and test cases for validation.

#### 2. **Software Safety Analysis of Requirements**

* Conduct independent **software safety analyses** to ensure that safety-related requirements:
  + Mitigate software-induced hazards identified during PHA, FTA, or FMEA.
  + Account for worst-case scenarios, including off-nominal operating conditions.
  + Clearly define the conditions under which the requirements apply (e.g., system modes, operator interactions).
* Confirm that safety constraints do not conflict with other system requirements and that software does not compromise hazard inhibit independence or hardware redundancy.

#### 3. **Problem Tracking for Safety-Related Issues**

* Maintain a **list of safety-related non-conformances** in a problem tracking system, documenting:
  + Identified issues categorized as safety-critical, major, or minor.
  + Resolutions, corrective actions, and their verification status.
  + Trends over time (e.g., recurring types of issues) to identify systemic risks.

#### 4. **Software Requirements Documentation**

* Ensure that software requirements clearly reflect all relevant safety constraints, controls, mitigations, and assumptions. Key elements in the documentation include:
  + Hazard-derived software safety requirements.
  + Interface definitions between hardware/software and operators.
  + Constraints to ensure independence of hazard controls and hardware redundancy.

#### 5. **Software Requirements Analysis Report**

* SA should review and deliver a **software requirements analysis report**, showing:
  + Results of traceability and consistency checks for safety-related requirements.
  + Identified gaps or ambiguities in the requirements, along with recommended actions.
  + Documentation of resolved and unresolved safety requirements issues.

---

## 7.3 Metrics

**Objective:** To measure the health and effectiveness of software assurance activities related to safety requirements, providing actionable insights for addressing risks.

#### Suggested Metrics:

1. **Non-Conformance Metrics:**

   * Number of software work product non-conformances identified, categorized by lifecycle phase and severity over time.
   * Number of **safety-related non-conformances** identified by lifecycle phase over the project lifecycle.
2. **Safety-Related Requirements Metrics:**

   * Number of safety-related requirements issues (e.g., ambiguities, gaps) identified during analysis, split by status:
     + Opened issues.
     + Resolved/Closed issues.
   * Analysis of unresolved safety issues to assess criticality and monitor resolution timelines.
3. **Hazard Mitigation Metrics:**

   * Percentage of software-induced hazards mitigated or resolved by safety-related requirements at each lifecycle phase.
   * Level of coverage for safety-critical software requirements in testing activities (e.g., validation tests for fault handling).

#### Reference:

For additional metrics recommendations, refer to **SA Topic 8.18 - SA Suggested Metrics**, which offers metrics tailored to small and large projects.

---

## 7.4 Guidance

#### **Step 1: Analyze the Software Requirements**

1. **Verify Inclusion of Safety-Related Elements:**
   * Assess that **software-related safety constraints, controls, mitigations, and assumptions** between hardware, operator, and software are explicitly documented in the Software Requirements Specification (SRS).
   * Confirm that safety constraints address the interactions required to execute safety-critical functions, including roles, precedence, and failure modes.
   * Ensure safety-related requirements trace to specific **system safety analyses, such as PHA, SHA (System Hazard Analysis), and FTA**, and align with the overall system safety design.

#### **Step 2: Independence and Redundancy Analysis**

* Perform **software assurance analysis** to ensure:
  + The software does not violate hazard inhibit independence across multiple processors (e.g., redundant or independent hazard inhibits are functionally isolated from each other).
  + Hardware redundancy is preserved in failure conditions, and fault-tolerant mechanisms are verifiable.
  + Single points of failure in software or hardware controllers are eliminated or mitigated, especially for safety-critical paths.

#### **Step 3: Hazard Control Validation**

* Use outputs from system safety analyses (PHA, SHA) to define or refine **software safety requirements** that:
  + Address software as a hazard contributor or hazard controller.
  + Highlight required **software modes or states** for safety-critical operations (e.g., fail-safe or degraded modes).
  + Identify necessary **error-handling mechanisms** for fault detection and recovery.

#### **Step 4: Collaborate with Safety Personnel**

* Work collaboratively with stakeholders:
  + Software safety engineers and system safety engineers to align hazard analysis with software design.
  + Mission assurance experts to anticipate safety risks and resolve early-phase issues.

---

### **Specific Clarifications for Notes and Sub-Requirements**

1. **Item a - Known Safe State:**

   * When a hazard is detected, the "safe state" should address hardware/software conditions (e.g., actuators/states to be frozen), system phase, and configurations. This must account for device capability, memory content, and other critical operational factors.
   * Example: Include requirements for reverting hardware/software to "safe mode" when an unexpected power flux is detected.
2. **Item d - Operator Inputs:**

   * Multiple independent commands for critical actions (like manual overrides) reduce operator errors. For example:
     + "Software shall require two independent confirmatory inputs from the operator before overriding automatic safety measures."
3. **Item f - Memory Protection:**

   * Address how to handle memory corruption, such as radiation-induced faults. Incorporate requirements for memory integrity mechanisms like:
     + Error Detection and Correction (EDAC).
     + Periodic memory scrubbing.
     + Authentication for data loads.
4. **Item h - Safety-Critical Command Sequencing:**

   * Prevent execution of operator commands in inappropriate system states. Safety-critical commands should enforce logic gates like:
     + Mode-specific validation before command execution.
     + "Must-work" or "must-not-work" conditions.
5. **Item j - Fault Handling:**

   * Define specific timeframes for hazard mitigation following **off-nominal** conditions, such as fault isolation and transition to a safe state.
   * Ensure that time-critical software events can complete before system failure.
6. **Item k - Error Handling:**

   * Include software features to detect and isolate both internal (logic errors, invalid inputs) and external faults (sensor failures, hardware faults).
7. **Item l - Instrumentation and Self-Monitoring:**

   * Specify requirements for adequate sensors and effectors to enable software hazard detection and mitigation.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

From [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations)

**SWE-134 - Safety-Critical Software Design Requirements**

3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:

a. The software is initialized, at first start and restarts, to a known safe state.  
b. The software safely transitions between all predefined known states.  
c. Termination performed by software functions is performed to a known safe state.  
d. Operator overrides of software functions require at least two independent actions by an operator.  
e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard.  
f. The software detects inadvertent memory modification and recovers to a known safe state.  
g. The software performs integrity checks on inputs and outputs to/from the software system.  
h. The software performs prerequisite checks prior to the execution of safety-critical software commands.  
i. No single software event or action is allowed to initiate an identified hazard.  
j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event.  
k. The software provides error handling.  
l. The software can place the system into a safe state.

See **Software Contributions to Hazards, **Software in system hazard analysis in [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) .****

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVD/pages/102695554/6.2+-+Checklist+for+General+Software+Safety+Requirements) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements) |

# 8. Objective Evidence

Providing **objective evidence** for Requirement 4.1.4 involves documenting and reporting artifacts, analyses, and verification results that demonstrate compliance with this requirement. The objective evidence must show that **software-related safety constraints, controls, mitigations, and assumptions** between hardware, software, and operators have been identified, documented, analyzed, implemented, and verified.

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

Here’s how you can provide **objective evidence** for Requirement 4.1.4 at each stage of the lifecycle:

---

## **Objective Evidence Categories:**

### 1. **Requirements Documentation**

Evidence that software safety constraints, controls, mitigations, and assumptions were properly defined and documented in the **Software Requirements Specification (SRS)** and related documents.

#### Key Artifacts:

* **Software Requirements Specification (SRS):**

  + Contains a section or tagged requirements for safety-related constraints (e.g., operational thresholds, redundancy).
  + Includes all system-derived safety requirements mapped to software.
  + Example Requirement: *“Software shall immediately transition to Safe Mode if hardware temperature exceeds 120°C ± 2°C.”*
* **System Hazard Reports (SHRs) or System Safety Requirements:**

  + Show alignment between system hazard analysis results (e.g., Preliminary Hazard Analysis (PHA)) and software-level safety requirements.
  + Trace documented hazards to specific software requirements (e.g., hazard X mitigated by Software Safety Requirement Y).

#### Examples of Evidence:

* Annotated SRS with safety-critical requirements highlighted and mapped to system safety artifacts.
* A summary of all safety-related software constraints, mitigations, and assumptions, including modes of operation and fallback states.
* Change logs showing updates made to safety requirements following hazard reviews.

---

### 2. **Safety Analyses**

Evidence that safety analyses were performed to identify and mitigate hazards, validate safety requirements, and verify compliance.

#### Key Activities:

* **Software Contribution Analysis:**

  + Show how software contributes to or controls hazards identified at the system level.
  + Example: Software interactions with hardware inhibit mechanisms or fault-tolerant processes.
* **Fault Tree Analysis (FTA) or Failure Modes and Effects Analysis (FMEA):**

  + Include sections that identify software-related faults, their likelihood, and mitigations.
  + Example: Evidence that redundant software paths or diagnostic checks mitigate single-point failures.
* **System Hazard Analysis (SHA):**

  + Demonstrates that system-level hazards involving hardware, software, and operators were identified and controlled.

#### Examples of Evidence:

* Completed FMEA/FTA reports with software hazards identified and mitigated.
* Updated System Hazard Analysis including software contributions to risk.
* Software safety analysis report showing traceability from hazards to software requirements.

---

### 3. **Traceability Matrices**

Evidence that all safety constraints, controls, mitigations, and assumptions were traced to their respective system hazards and test cases.

#### Key Artifacts:

* **Requirements Traceability Matrix (RTM):**

  + Links software safety requirements to:
    - System safety requirements.
    - Hazards from PHA, FMEA, or SHA.
    - Verification and validation test cases.
  + Example RTM Entry:

    | **Requirement ID** | **Hazard ID** | **Safety Mitigation** | **Test Case ID** |
    | --- | --- | --- | --- |
    | SW-SAF-001 | HZ-123 | Temperature failsafe | TC-001 |
* **Interface Requirements Trace Matrix (for software-hardware and software-operator coordination):**

  + Ensures that software safety requirements align with hardware constraints and human-system interactions.
  + Example: *“Actuator Stop Command (SW-SAF-003) maps to hardware verification test HW-TC-01 for response delay.”*

#### Examples of Evidence:

* RTMs or bidirectional traceability reports demonstrating links between hazards, requirements, and tests.
* Traceability between system design documents and software safety requirements.
* Assessment or review reports ensuring traceability coverage.

---

### 4. **Testing and Validation Evidence**

Evidence that all safety-related software requirements were validated through testing.

#### Key Artifacts:

* **Test Plans:**

  + Safety-specific software test plans detailing scenarios that validate constraints, mitigations, and assumptions.
  + Example Test Scenario: Simulating a failed primary sensor and verifying fallback to the redundant sensor.
* **Test Reports:**

  + Results of testing safety-related software features, such as:
    - Fault detection and recovery.
    - Validating hardware and operator interactions.
    - Environmental constraints (e.g., temperature thresholds under extreme conditions).
* **Fault Injection Testing Results:**

  + Evidence of tests showing the system’s ability to handle off-nominal conditions (e.g., hardware sensor failure or corrupted input from the operator).

#### Examples of Evidence:

* Execution logs from safety-critical test cases demonstrating pass/fail outcomes.
* Fault injection reports showing successful recovery from identified faults.
* Validation reports showing system behavior under both nominal and extreme conditions.

---

### 5. **Configuration Management**

Evidence that safety-related software artifacts were properly managed and independently reviewed.

#### Key Artifacts:

* **Problem Tracking Logs:**

  + List of all safety-related non-conformances found during the project, categorized by:
    - Phase in the lifecycle (e.g., requirements, design, test).
    - Criticality (e.g., High, Medium, Low).
  + Resolution status (e.g., open, under review, closed).
* **Configuration Audit Reports:**

  + Show that safety-related software requirements and associated deliverables were tracked for changes and adequately reviewed.

#### Examples of Evidence:

* Closed issue logs for safety-related defects.
* Configuration status accounting reports showing safety requirements and test coverage.
* Review comments/resolutions for safety-critical documents.

---

### 6. **Collaboration Evidence**

Evidence of coordination between software assurance, system safety, and other stakeholders in developing and validating safety requirements.

#### Key Activities:

* **Collaboration Logs or Meeting Minutes:**

  + Records of discussions between software engineers, safety analysts, hardware engineers, and operators regarding safety-critical requirements.
* **Review Evidence:**

  + Proof that safety requirements underwent independent software assurance reviews.
  + Example: Formal review sign-off for safety constraints in the SRS or test plan.

#### Examples of Evidence:

* Meeting notes showing how software safety constraints (related to hazard control or hardware interaction) were developed.
* Minutes of joint safety working group discussions.
* Review checklists and approval signatures for hazard reports.

---

### 7. **Independent Verification and Validation (IV&V) Reports**

Evidence that an independent verification team assessed the compliance of safety-critical software requirements.

* These reports confirm:
  + Adequacy of safety constraints, controls, mitigations, and assumptions in the SRS.
  + Correct implementation of safety-related requirements.
  + System conformity between software, operator, and hardware.

#### Examples of Evidence:

* IV&V report highlighting the completeness of software safety constraints and assumptions.
* Findings and resolutions of any identified gaps in safety-related requirements or tests.
* Evidence of independent validation testing for safety-critical functions.

---

### **Evidence Submission Summary Checklist**

For streamlined reporting, ensure the following deliverables are included as objective evidence:

1. **Documented Software Safety Requirements:**
   * Clearly highlighted constraints, controls, mitigations, and assumptions in the main SRS.
2. **System Hazard Analyses:**
   * Hazard logs showing software’s role in mitigation or contribution.
3. **Traceability Matrices:**
   * RTMs linking hazards, safety requirements, and tests.
4. **Test Reports:**
   * Evidence of safety constraints validated through appropriate test cases or simulation (e.g., off-nominal testing, fault injection).
5. **Defect Logs:**
   * A categorized list of safety-related issues and resolutions.
6. **IV&V Reports:**
   * Review reports demonstrating independent validation of safety-critical software.
7. **Collaboration Records:**
   * Minutes or logs of safety-related decisions between software, hardware, and operator teams.

---

### Conclusion

By collecting and presenting these pieces of objective evidence, you can confirm compliance with Requirement 4.1.4. Solid objective evidence ensures that safety considerations for software, hardware, and operators were not only identified but also successfully implemented, tested, and independently validated within the project lifecycle. This approach minimizes risks and increases confidence in the safety and reliability of the system.
