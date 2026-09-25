# 9.07 Fault Detection and Response

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695798. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response

9.07 Fault Detection and Response

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695798)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695798&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Principle and Rational](#tabs-1)
* [2. Examples](#tabs-2)
* [3. Inputs](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Lessons Learned](#tabs-5)

# 1. Principle

[9.01 Software Design Principles](/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles)

* [9.03 Coding Standards](/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards)
* [9.04 Command Receipt Acknowledgement](/spaces/SWEHBVD/pages/102695795/9.04+Command+Receipt+Acknowledgement)
* [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity)
* [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion)
* [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response)
* [9.08 Flight Software Modification](/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification)
* [9.09 Incorrect Memory Use or Access](/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access)
* [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode)
* [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling)
* [9.12 Resource Margins](/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins)
* [9.13 Resource Oversubscription](/spaces/SWEHBVD/pages/102695804/9.13+Resource+Oversubscription)
* [9.14 Resource Usage Measurement](/spaces/SWEHBVD/pages/102695805/9.14+Resource+Usage+Measurement)
* [9.15 Safe Transitions](/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions)
* [9.16 Thread Safety](/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety)
* [9.17 Toggle Commands](/spaces/SWEHBVD/pages/102695808/9.17+Toggle+Commands)

In the software design, provide mechanisms to detect credible system faults and to react to these faults according to a pre-described plan.

## 1.1 Rationale

Without the capability to safely recover from certain credible faults the system could lose data, harm an instrument or, in the worst case, cause loss of life or the end-of-mission.

## 2. Examples and Discussion

Control systems incorporate fault detection and response mechanisms in order to properly respond to off-nominal conditions.  Although some low criticality systems incorporate a generic fault response to any detected error, this is not generally sufficient for control systems. See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

Identifying potential causes of anomalies typically requires specialized knowledge of the system components, material properties, wear mechanics, environmental effects, and other factors. Understanding how each potential local anomaly will affect the rest of the system, and developing appropriate and effective responses is typically the domain of systems engineering. Thus, a complete specification of fault detection and responses for a system is usually the result of a collaboration between lower-level domain experts, designers, and system engineers. Although the software team does not develop the overall fault protection system, they are usually charged with implementing the higher level behaviors, and play an important role in shaping the approach based on what they have found effective in the past. Some of the design features and considerations that have proven useful on NASA missions are discussed in the paragraphs to follow.

Because fault detection and correction approaches will change depending upon the mission phase and system state, the capability to enable/disable scenarios as well as completely update them is an important feature of the software architecture. Fault management architectures usually include some type of escalating response to persistent failures. (For example, the software might notify upon the first failure, take some precautionary action upon a continuing failure, and shutdown equipment if the failure continues to persist.) Fault definitions and responses may be implemented in software as ground-modifiable data tables. Typically, the operator needs to have control of the specific fault responses and be able to modify them. Capabilities can include enabling and disabling fault detections and/or responses and modifying a table of potential faults and planned responses.

Detection methods that have been used include checking the entire input data set against expected ranges. Values are typically checked against the range that is expected based on the current state of the system. Other fault detection mechanisms that have been used include:

* Comparing redundant or associated values for agreement,
* Comparing data values to a low fidelity model of the system executing in real time synchronized with the control system,
* Incorporating periodic heartbeat signals in the components of the control system, and
* Comparing and the value of an indicator to the expected state based on commanded state (i.e. after a valve has been commanded to open, checking the valve position indicator to verify the valve is open).

One failure response implementation that has been widely used includes reporting the fault and maintaining a count of the number of specific failures that have occurred. When a predefined, but modifiable, maximum number of specific failures is exceeded, a more severe response is initiated. More severe responses that have been used include resetting components, shutting down faulty components, switching to backup systems, or a complete system restart.

A software architecture choice that must be considered is whether to design a centralized error checking system, a distributed system, or a combination of the two. As examples, a centralized implementation might limit-check all system measurements in one compact set of looping code, whereas a distributed implementation would limit-check individual (or small sets of) measurements as they are read. Previous experience has shown that a centralized system simplifies maintenance of the error checking code and produces reusable code. However, some environments would require multiple data moves across software interfaces to gather measure data for limit checking (e.g., a partitioned operating system with measurement data in several partitions), impacting the performance of the system. Or in extreme cases, the measurement may need to be limit-checked as soon as possible after it is read to identify faults. The software architects need to make the optimal decision based on careful consideration of the requirements and system constraints.

Building in capabilities to continue operating in the presence of (possibly permanent) faults is an important software system design aspect. While the fault detection and response design specifies how the system will respond to faults as they are discovered, long term solutions may be required that extend beyond ensuring the immediate safety of the system. For example, the permanent failure of an inertial measurement unit (IMU) on a robotic spacecraft might be compensated by implementing a portion of its capabilities in software using a star tracker. In this example the immediate response to the IMU failure would probably involve using a sun sensor to ensure there was enough sun on the solar arrays to keep the spacecraft alive, while the alternate functionality would be the long-term solution.

### **Table 1. Sample Faults Types**

|  |  |
| --- | --- |
| **Sample Types** | **Definition** |
| Over heating | Certain thermal conditions could feasibly occur that could be corrected autonomously by turning off a subsystem or part of a subsystem. |
| Pointing violation | Certain instruments may be harmed if pointed erroneously. This should be detected by the Fault Management System and commands to the attitude control system (ACS) should be sent. |
| Memory Failures | Certain memory areas could be failing and work-arounds could be put in place assuring that those memory locations not be used. |
| Power loss | A loss of power can be detected and the system can autonomously be put in safehold by the software. |

### **Table 2. Example life cycle phased implementation of fault detection and response**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Phase | A | B | C | D |
| Activities: | 1. Document a flight software (FSW) Fault Detection and Correction Plan | 1. An analysis of the entire system must be performed to indentify all potential faults and the proper response to each fault.   2. With the system engineering team and instrument managers, agree on the FSW Detection and Correction Plan | 1. Implement the FSW Detection and Correction Plan.   2. Test all defined scenarios | 1. Update and analyze the documentation.   2. Refine the scenarios as necessary |
| Verification: | Verify at Mission Definition Review (MDR). | 1. Verify at FSW Software Requirements Review (SRR) & FSW Preliminary Design Review (PDR)    2. Verify at System Design Review (SDR) & PDR | 1. Verify at Critical Design Review (CDR)    2. Verify at FSW CDR | 1. Verify at FSW Acceptance Test Review   2. Verify at Pre-Ship Review (PSR) and Flight Readiness Review (FRR). |

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.4 Fault Protection**
  + **3.7.4.1 Protection for Credible Single Faults** - Fault protection software shall include all flight system single-fault scenarios deemed credible by system-level hazard analysis.
  + **3.7.4.2 Fault Protection Response During Time-Critical Mission Activities** - The fault protection response shall be designed to autonomously re-establish the needed spacecraft functionality to permit safe, reliable and timely completion of the mission critical activity.
  + **3.7.4.3 Fault Protection Response During Non-Time-Critical Mission Activities** - The fault protection response shall be designed to, at a minimum, autonomously configure the spacecraft to a safe, quiescent, ground command-able state, transmitting periodically, at least an RF carrier downlink signal during non mission-critical cruise periods following a fault condition.   
      
    *Note: A safe state is a state in which the spacecraft thermal condition and inertial orientation are stable, the spacecraft is commandable and is transmitting a downlink signal, and requires no immediate commanding to ensure spacecraft health and safety that preserves vital spacecraft resources. The safe state shall be power-positive.*
  + **3.7.4.4 In-Flight Commandability and Parameter Visibility** - The fault protection system shall be designed as in-flight-command-able to permit changing the state of enable/disable parameters and other pertinent parameters, e.g., threshold and persistence values. The status of these parameters should be telemetered and made available for timely flight team use.
  + **3.7.4.5 Fault Indication Filtering** - The design should select the enable/disable, trigger, and persistence values for fault indication filtering to ensure safety but not "hair triggered" to cause inadvertent Fault Protection entry/execution.

### 3.2 GSFC

None

### 3.3 JPL

* **4.9 System Fault Protection Design**
  + **4.9.1 General**
    - **4.9.1.1 Fault protection definitions**- Definitions used in the Fault Protection section are as follows:   
        
      a. Anomaly- any unexpected occurrence.   
        
      *Note: Applied to indicate any of faults, failures, and their observable symptoms*   
        
      b. Error- an observable symptom of a fault   
        
      *Note: In not all cases will faults give rise to observable symptoms.*   
        
      c. Failure- the inability of a system or component to perform its required function.   
        
      d. Fault- a physical defect or occurrence which causes the loss of required functionality
    - **4.9.1.2 Protection for credible single faults** - Fault Protection shall handle all credible single faults or losses of functionality within all expected environmental conditions.   
        
      *Note: Fault protection is not intended as a remedy for faults that result from design error and/or designs that are inadequate for the specified environment.*   
        
      *Rationale: Designs should not be required to handle unrealistic scenarios, yet based on our operational experience, we know they must handle 'unknown-unknowns'. Fault protection scope must include function preservation (loss of functionality) as well as identified fault scenarios. This notion of a 'safety-net' would include (but not be limited to) uplink command loss, attitude control loss, attitude knowledge loss, ephemeris errors, excess system momentum, system power/energy deficiency, and system over/under temperature.*
    - **4.9.1.3 Protection for multiple faults** - Fault protection shall handle multiple, non-coincident faults, provided that they occur in functionally independent system elements.   
        
      *Rationale: Having dealt with prior faults, it is nonetheless important to preserve remaining options for mission success. The likelihood of faults in functionally independent system elements is undiminished. Coincident faults, however, are generally of sufficiently low likelihood to justify making no overt provisions for them in the design.*   
        
      *Note: A newly discovered latent fault (e.g., one exposed by a recovery action for a recent fault) should not be considered a concurrent fault. Only the error detection is concurrent in this case. Operational mitigations to reveal latent faults in a timely manner may obviate the need to deal with such concurrent errors.*
    - **4.9.1.4 Smallest level of FP concern** - Fault protection shall be able to diagnose and isolate faults at the level of the defined fault containment regions, and need not attempt recovery below this level.   
        
      *Note: Fault containment regions represent the smallest level of concern to fault protection. See 4.12.1.6.*   
        
      *Rationale: Redundancy schemes can be seriously compromised in the absence of fault containment. Also, failure to contain faults can complicate recovery by confusing diagnosis, and requiring more complex response actions.*
    - **4.9.1.5 Tolerance to false alarms** - At all times throughout the mission, the spacecraft shall tolerate execution of fault protection in response to false alarms.   
        
      *Rationale: False alarms are inevitable, so the system shouldn’t be vulnerable to them.*   
        
      *Example: Incorrectly set monitor threshold may cause an unexpected response, and this should not severely degrade the mission, or create an operational hardship.*
    - **4.9.1.6 Variation in FP behavior** - Variations in fault protection behavior shall be based directly upon the system mode or activity, rather than indirectly on individual manipulation of enables, thresholds, etc.   
        
      *Example: Fault protection objectives or behavior may vary depending on mission phase. This variation should be based upon system modes or circumstances, rather than changed via a separate set of commands that alter fault protection enables/disables, thresholds, etc. System-wide behavioral changes should be made in a more atomic, integrated fashion- making the overall design less susceptible to operator error, or timing vulnerabilities.*
  + **4.9.2 Fault Protection Response**   
      
    - **4.9.2.1 Fault protection priorities** - Fault protection shall preserve flight system health, safety, and consumables throughout all mission phases, except when the completion of time critical events or activities takes priority.   
        
      *Rationale If fault protection response actions must choose between completing a time critical event or losing the mission, it is better to attempt to complete the event (risking health and/or safety) and risk saving the mission vs. not completing the event and losing the mission.*   
        
      *Note: Mission-critical events are those that if not executed properly and in a timely manner could result in failure to achieve mission success (e.g., orbit insertion, EDL). A TCM is not mission-critical unless it must execute properly in the time scheduled for it, i.e. cannot be delayed.*
    - **4.9.2.2 Flight system safing** - Following fault conditions that may impact spacecraft health, safety, or consumables, fault protection shall, at a minimum, autonomously configure the spacecraft to a safe, sustainable, ground commandable mode that preserves vital spacecraft resources and provides for at least an RF carrier downlink signal to the Earth.   
        
      *Note: The safing mode may be a single state or more than one state. The RF downlink signal need not be continuous, but must be predictable in its timing.*   
        
      *Rationale: The spacecraft must autonomously recover from a detected fault when the function(s) affected by the fault threaten spacecraft/instrument survival (e.g., functions necessary to maintain Safe mode). Ensure spacecraft survivability and viability by preserving vital spacecraft resources (e.g., thermal, power), while enabling ground interaction (e.g., command and downlink) for recovery operations It is not enough merely to diagnose and isolate faults, or to restore lost functionality, if the resulting system state still threatens the rest of the mission (e.g., through stress, loss of consumables, or unresponsiveness to operator control).*   
        
      * **4.9.2.2.1 Sustainable duration** - The safe state(s) established by the safing response shall be sustainable for a duration consistent with the frequency of planned communications contacts and timing of operational activities.   
          
        *Note: A missed tracking pass should not be reason to declare a s/c emergency, thus requiring rescheduling of tracking resources.*   
          
        *Note: 14 days is a typical duration based on the interval between ground contacts, but can be project and mission phase dependent.*
      * **4.9.2.2.2 Fault protection during safing** - The spacecraft shall be able to detect and respond to faults while in a safe configuration including the safe state(s) established by the safing response.   
          
        *Rationale: Transition to safing may be due to an operational mistake, and the system should still be single fault tolerant while awaiting ground recovery.*
    - **4.9.2.3 Autonomous completion** - For events or activities that are required for mission success and must be performed without the possibility of ground intervention, fault protection shall endeavor to ensure the autonomous, timely completion of that event or activity.   
        
      *Note: Autonomous completion implies restoring the functionality needed to complete the mission-critical event. See 4.9.1.2 and 4.9.1.3.*   
        
      *Rationale: For certain mission critical events, ground response may not be possible and the autonomous fault protection design must ensure completion in the event of a single fault.*   
        
      * **4.9.2.3.1 Accommodation of processor resets** - The design shall accommodate processor resets during mission-critical events.

### 3.4 MSFC

* **4.12.1.12 The software shall detect and annunciate, if applicable, cautions and warnings that affect critical systems, subsystems, and/or crew health.**  
    
  *Rationale: The determination of caution and warning is performed by the processing of logic utilizing a defined subset of health and status measurements. This includes the logic for the determination of abort conditions. Sensor latency is not included because it is application dependent and can vary widely.*
* **4.12.3.1 Software shall provide fault containment mechanisms to protect against error propagation.**  
    
  *Rationale: Potential faults and the action taken must be defined and determined so that actions taken upon error detection do not set off a chain reaction leading to more serious fault conditions, e.g., issuance of questionable commands to actuators as a result of a fault condition that exacerbates the problem.*
* **4.12.3.2 Software shall record and provide notification of errors and the corresponding time of occurrence.**  
    
  *Rationale: All error conditions must be logged in a manner that ground and crew are aware of the vehicle performance, whether real-time or during post-flight analysis.*
* **4.12.3.14 The software fault protection design shall permit ground operators to modify the fault protection control settings (e.g., enables, thresholds, persistence values).**  
    
  *Rationale: This requirement ensures that the operators participate in the decision to activate sequences involving hazardous commands. Operator inhibits or enables can be considered one of the functionally independent parameters*

# 4. Resources

### 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-501)

  [Mars Observer Inertial Reference Loss](https://llis.nasa.gov/lesson/310 "Click to open in new window")

  Public Lessons Learned Entry: 310.
* (SWEREF-504)

  [Mars Observer Inappropriate Fault Protection Response Following Contingency Mode Entry due to a Postulated Propulsion Subsystem Breach](https://llis.nasa.gov/lesson/343 "Click to open in new window")

  Public Lessons Learned Entry: 343.
* (SWEREF-505)

  [Mars Observer Attitude Control Fault Protection](https://llis.nasa.gov/lesson/345 "Click to open in new window")

  Public Lessons Learned Entry: 345.
* (SWEREF-512)

  [Lewis Spacecraft Mission Failure Investigation Board](https://llis.nasa.gov/lesson/625 "Click to open in new window")

  Public Lessons Learned Entry: 625.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
* (SWEREF-562)

  [MRO Articulation Keep-Out Zone Anomaly](https://llis.nasa.gov/lesson/2044 "Click to open in new window")

  Public Lessons Learned Entry:2044. In NASA Engineering Network. Retrieved March 31, 2015 from http://llis.nasa.gov/lesson/2044.
* (SWEREF-568)

  [Erroneous Onboard Status Reporting Disabled IMAGE's Radio](https://llis.nasa.gov/lesson/1799 "Click to open in new window")

  Public Lessons Learned Entry: 1799.
* (SWEREF-569)

  [Mars Global Surveyor (MGS) Spacecraft Loss of Contact](https://llis.nasa.gov/lesson/1805 "Click to open in new window")

  Public Lessons Learned Entry:1805. In NASA Engineering Network. Retrieved March 31, 2015 from http://llis.nasa.gov/lesson/1805.
* (SWEREF-586)

  [Redundant Verification of Critical Command Timing (1995) Public Lesson Learned Entry: 559.](https://llis.nasa.gov/lesson/559 "Click to open in new window")

  Public Lessons Learned Entry: 559.
* (SWEREF-680)

  [Verify Configuration of Flight Hardware Prior to Test (1998)](https://llis.nasa.gov/lesson/885 "Click to open in new window")

  Public Lessons Learned Entry: 0885, Date: 2000-06-8,Submitting Organization: JPL, Submitted by: R. Menke, R. Welch, D. Oberhettinger
* (SWEREF-681)

  [MRO Spaceflight Computer Side Swap Anomalies -Export Version](http://llis.nasa.gov/lesson/2041 "Click to open in new window")

  Public Lessons Learned Entry: 2041, Date: 2008-12-16, Submitting Organization: JPL, Submitted by: David Oberhettinger
* (SWEREF-682)

  [Galileo Spacecraft Safing During Star Scanner Calibration](http://llis.nasa.gov/lesson/288 "Click to open in new window")

  Public Lessons Learned Entry: 0288, Date: 1993-07-13, Submitting Organization: JPL, Submitted by: J. O. Blosiu
* (SWEREF-683)

  [Anomalous Flight Conditions May Trigger Common-Mode Failures in Highly Redundant Systems](http://llis.nasa.gov/lesson/1778 "Click to open in new window")

  Public Lessons Learned Entry: 1778, Date: 2007-03-6. Submitting Organization: JPL, Submitted by: Martin Ratliff

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) |

## 4.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 4.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

## 5. Lessons Learned

### 5.1 NASA Lessons Learned

Lessons that appear in the NASA LLIS [439](#_tabs-<p>4</p>) or Center Lessons Learned Databases.

* + **MER Spirit Flash Memory Anomaly (2004)**. **Lesson Learned 1483:** [557](#_tabs-<p>4</p>) "Shortly after the commencement of science activities on Mars, an MER rover lost the ability to execute any task that requested memory from the flight computer. The cause was incorrect configuration parameters in two operating system software modules that control the storage of files in system memory and flash memory. Seven recommendations cover enforcing design guidelines for COTS software, verifying assumptions about software behavior, maintaining a list of lower priority action items, testing flight software internal functions, creating a comprehensive suite of tests and automated analysis tools, providing downlinked data on system resources, and avoiding the problematic file system and complex directory structure."
  + **Mars Global Surveyor (MGS) Mars Global Surveyor (MGS) Spacecraft Loss of Contact**. **Lesson Learned 1805: [569](#_tabs-<p>4</p>)**  
    Contact was lost with the Mars Global Surveyor (MGS) spacecraft in November 2006 during its 4th extended mission. A routine memory load command sent to an incorrect address 5 months earlier corrupted positioning parameters, and their subsequent activation placed MGS in an attitude that fatally overheated a battery and depleted spacecraft power. The report by the independent MGS Operations Review Board listed 10 key recommendations to strengthen operational procedures and processes, correct spacecraft design weaknesses, and assure that economies implemented late in the course of long-lived missions do not impose excessive risks.
  + **Anomalous Flight Conditions May Trigger Common-Mode Failures in Highly Redundant Systems**. **Lesson Learned 1778:** [683](#_tabs-<p>4</p>) "After launch, MRO was found to be susceptible to a solar flare event during the critical aerobraking phase of the mission that could corrupt the multiply redundant identical file systems in the Command & Data Handling subsystem. This could have caused a mission failure during aerobraking if the files had been needed for entry into safe mode or to perform an SEU-induced reboot of the flight computer. Assure that fault tolerant designs reflect full consideration of anomalous conditions that could trigger common-mode failures."
  + **Lewis Spacecraft Mission Failure Investigation Board**. **Lesson Learned 0625:** [512](#_tabs-<p>4</p>) "The Board found that the loss of the Lewis Spacecraft was the direct result of an implementation of a technically flawed Safe Mode in the Attitude Control System. This error was made fatal to the spacecraft by the reliance on that unproven Safe Mode by the on orbit operations team and by the failure to adequately monitor spacecraft health and safety during the critical initial mission phase."
  + **Mars Observer Inertial Reference Loss**. **Lesson Learned 0310:** [501](#_tabs-<p>4</p>) "Mars Observer experienced inertial reference loss on several occasions during its cruise to Mars. These incidents were due to the lack of a detailed code walk-through, and to use of gyro noise values, obtained from in-house test, that were more optimistic than the manufacturer's specifications. Do not depend on hardware performance being better than the manufacturer's specification. Perform detailed code walk-through of critical software modules. Pay special attention to inherited critical software. Design the flight computer and software to permit necessary changes in flight."
  + **Redundant Verification of Critical Command Timing (1995)**. **Lesson Learned 0559:** [586](#_tabs-<p>4</p>) "When a new mission software release was uploaded to the spacecraft, the inflight upload failed to include a software patch that had been written to fix a defective countdown timer. Because an independent “watchdog timer” was planned, but never implemented due to constrained project resources, the thrusters continued to fire after the desired shutdown time and the mission was terminated. Recommendations Centered on the need for rigorous software configuration management, a watchdog timer to terminate operations, and testbed verification of in-flight software updates."
  + **Erroneous Onboard Status Reporting Disabled IMAGE's Radio**. **Lesson Learned 1799: [568](#_tabs-<p>4</p>)** "The loss of the IMAGE satellite was attributed to a Single Event Upset-induced "instant trip" of the Solid State Power Controller (SSPC) that supplies power to the single-string Transponder. The circuit breaker was not reset because this hybrid device incorrectly reported the circuit breaker as closed, and ground could not command a reset because the satellite's single telemetry receiver had been disabled by the SSPC. The SSPC's problematic state reporting characteristic was an intentional design feature that was not reflected in any part documentation, and three similar "instant trips" on other NASA satellites had not been reported in the GIDEP system. Consider hardwiring receiver power to the power bus, or build redundancy into the power switching or into the operational status sensing. Ensure that GIDEP reports or NASA Alerts are written and routed to mission operations (as well as to hardware developers), and that flight software responds to command loss with a set of timed spacecraft-level fault responses."
  + **Mars Observer Attitude Control Fault Protection**. **Lesson Learned 0345:** [505](#_tabs-<p>4</p>) "From the analyses performed after the Mars Observer mission failure, it became apparent that the MO fault protection suffered from a lack of top-down system engineering design approach. Most fault protection was in the category of low-level redundancy management. It was also determined that the MO fault protection software was never tested on the flight spacecraft before launch. Design fault protection to detect and respond to excessive attitude control errors, use RCS Thrusters to control excessive attitude control errors, and always test fault protection software on the flight spacecraft before launch."
  + **Mars Observer Inappropriate Fault Protection Response Following Contingency Mode Entry due to a Postulated Propulsion Subsystem Breach**. **Lesson Learned 0343:** [504](#_tabs-<p>4</p>) "Following the loss of the Mars Observer spacecraft, simulations showed that a postulated propellant breach would have caused angular accelerations that could have inhibited downlink and caused multi-axis gyro saturation. In this case, fault protection features of flight software would have inhibited all momentum unloading and prevented the stabilization of the spacecraft. Ensure that fault protection takes proper action regardless of spacecraft state. Fault responses should not be allowed to interrupt critical activities."
  + **Galileo Spacecraft Safing During Star Scanner Calibration**. **Lesson Learned 0288:** [682](#_tabs-<p>4</p>) "An unintended in-flight mode change impacted a planned Galileo sequence only because of a hardware failure during the sequence. The spacecraft entered safing, necessitating a difficult recovery process that could have impacted science return had it happened during encounter. When simulating and testing command sequences, assure that the software and hardware states exactly match the expected in-flight states. Any anomaly that changes a fundamental spacecraft state must be scrutinized for potential impacts."
  + **MRO Articulation Keep-Out Zone Anomaly**. **Lesson Learned 2044: [562](#_tabs-<p>4</p>)**  "An articulating solar array collided with the MRO spacecraft due to inadequate definition and verification/validation of system-level design requirements for implementing the appendage's keep-out zone in flight software. Construct models to ensure requirements discovery is complete, provide a robust appendage motion backstop capability, ensure precision in requirements language, and never ask control laws to exceed your control authority."
  + **MRO Spaceflight Computer Side Swap Anomalies [Export Version]** **Lesson Learned 2041: [681](#_tabs-<p>4</p>)**  "A few months into its mission, MRO began experiencing unexpected side swaps to the redundant flight computer that placed the spacecraft into safe mode. The problem was traced to subtle inconsistencies between the MRO design implementation of an ASIC device and a known limitation of that device. Users of the RAD750 spaceflight computer should assure that the "PPCI Erratum 24" ASIC defect cannot cause excessive accumulation of uncorrectable SDRAM memory errors, and that the system architecture has robust error recovery capabilities."
  + **Verify Configuration of Flight Hardware Prior to Test (1998)** **Lesson Learned 0885:** [680](#_tabs-<p>4</p>) "During a system-level ambient functional test of the MPL spacecraft, the software test sequence commanded the gimbaled medium gain antenna through its full range of motion, striking one of the undeployed solar panels. Confirm that developmental and flight hardware is in a configuration that has been reviewed for hardware and personnel safety prior to beginning any test sequence and that the appropriate procedure for powering down flight hardware in all test configurations under any potential emergency condition has been determined. Hold a thorough Test Readiness Review using the most current checklist that addresses personnel safety, software and hardware safety, test operations and constraints, fault protection actions, kinematics and interference analysis, commandability, emergency shutdown, and restart procedures."
