# 9.10 Initialization - Safe Mode

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695801. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode

9.10 Initialization - Safe Mode

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695801)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695801&showCommentArea=true&showComments=true#addcomment)

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

Design flight software to initialize software and hardware to a known, safe, and deliberate state

## 1.1 Rationale

Upon startup, flight systems need to autonomously enter a state that requires no immediate ground intervention to ensure its health and safety, and that preserves vital system resources, even in the presence of faults.

# 2. Examples and Discussion

Flight software initialization spans three typical scenarios: nominal, multiple restart, and minimal boot. The minimal boot scenario results in a stable, commandable state, where downlinks are possible, and that maximizes preservation of system resources---a safe state. Multiple restart is a type of fault response where the software attempts a start after a prior failed attempt. Multiple restarts require the software system to preserve knowledge of a prior failed attempt so it can invoke degraded performance restart modes all the way down to minimal boot. Nominal boot is a safe state where certain capabilities are inactive by design. The definition of safe state is dependent on mission phase.

Initialization-Safe Mode may require incorporation of the following software design elements:

1. Software designed to initialize itself and any associated hardware, including any back-up hardware or software system, to a safe and known state upon startup---nominal boot.
2. Software designed to record and transmit its progress through each attempt at initialization.
3. Software designed to detect off-nominal restarts and to successively reinitialize with less and less dependency on preserved state (e.g., inertial, temporal, device capability or configuration, file allocation tables, boot code in RAM, etc.) from before the most recent reset, until a fully known and tested initial configuration is obtained, and until stable operation has been restored. See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).
4. Flight software designed to accommodate restarts during mission-critical events in situations that allow time for restarts. For example during mission critical events, a single string-system may choose to reboot during mission-critical events (a worst case scenario), whereas a multi-string system may choose to ignore a downed computer and rely on its redundant set.
5. Fault protection response designed, at a minimum, to autonomously configure the system to a safe, sustainable, ground-commandable state that preserves vital resources and provides for at least a communication link to the ground following fault conditions that may impact health, safety, or consumables. The safe mode may be a single state or more than one state. The communication link to the ground need not be continuous, but must be predictable in its timing.
6. Fault protection response designed to autonomously re-establish the needed system functionality to permit safe, reliable and timely completion of the mission critical activity.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.3.4 Multiple Restart Flight Software Initialization** - The software shall be designed to detect off-nominal restarts and to successively reinitialize with less and less dependency on preserved state (e.g., inertial, temporal, device capability or configuration, file allocation tables, boot code in RAM, etc.) from before the most recent reset, until a fully known and tested initial configuration is obtained, and until stable operation has been restored.  
    
  *Note: Reset is commonly used as a means of autonomous recovery from serious software problems caused by errors or single event upsets. Reset is not effective unless the problematic software state is cleared during re-initialization. Ultimately, all software states must be presumed suspect and expendable, if prior re-initializations have failed to resolve a problem. A complete accounting of preserved state is essential, if effective measures are to be taken against it.*
* **3.7.2.3 Start-Up Response** - Software shall be designed to initialize itself and any associated hardware, including any back-up hardware or software system, to a safe and known state upon startup.
* **3.7.4.2 Fault Protection Response During Time-Critical Mission Activities** - The fault protection response shall be designed to autonomously re-establish the needed spacecraft functionality to permit safe, reliable and timely completion of the mission critical activity.
* **3.7.4.3 Fault Protection Response During Non-Time-Critical Mission Activities** - The fault protection response shall be designed to, at a minimum, autonomously configure the spacecraft to a safe, quiescent, ground command-able state, transmitting periodically, at least a radio frequency (RF) carrier downlink signal during non mission-critical cruise periods following a fault condition.  
    
  *Note: A safe state is a state in which the spacecraft thermal condition and inertial orientation are stable, the spacecraft is commandable and is transmitting a downlink signal, and requires no immediate commanding to ensure spacecraft health and safety that preserves vital spacecraft resources. The safe state shall be power-positive.*

### 3.2 GSFC

None

### 3.3 JPL

* **4.9.2.2 Flight system safing** - Following fault conditions that may impact spacecraft health, safety, or consumables, fault protection shall, at a minimum, autonomously configure the spacecraft to a safe, sustainable, ground commandable mode that preserves vital spacecraft resources and provides for at least an RF carrier downlink signal to the Earth.  
    
  *Note: The safing mode may be a single state or more than one state. The  downlink signal need not be continuous, but must be predictable in its timing.*  
    
  *Rationale: The spacecraft must autonomously recover from a detected fault when the function(s) affected by the fault threaten spacecraft/instrument survival (e.g., functions necessary to maintain Safe mode). Ensure spacecraft survivability and viability by preserving vital spacecraft resources (e.g., thermal, power), while enabling ground interaction (e.g., command and downlink) for recovery operations. It is not enough merely to diagnose and isolate faults, or to restore lost functionality, if the resulting system state still threatens the rest of the mission (e.g., through stress, loss of consumables, or unresponsiveness to operator control).*
* **4.9.2.2.1 Sustainable duration** - The safe state(s) established by the safing response shall be sustainable for a duration consistent with frequency of planned communications contacts and timing of operational activities.  
    
  *Note: A missed tracking pass should not be reason to declare a spacecraft emergency, thus requiring rescheduling of tracking resources.*  
    
  *Note: 14 days is a typical duration based on the interval between ground contacts, but can be project and mission phase dependent.*
* **4.9.2.2.2 Fault protection during safing** - The spacecraft shall be able to detect and respond to faults while in a safe configuration including the safe state(s) established by the safing response.  
    
  *Rationale: Transition to safing may be due to an operational mistake, and the system should still be single fault tolerant while awaiting ground recovery.*
* **4.9.2.3 Autonomous completion** - For events or activities that are required for mission success and must be performed without the possibility of ground intervention, fault protection shall endeavor to ensure the autonomous, timely completion of that event or activity.  
    
  *Note: Autonomous completion implies restoring the functionality needed to complete the mission-critical event. See 4.9.1.2 and 4.9.1.3 in the**JPL Rules**on Protection for Credible Single Faults and Protection for Multiple Faults, respectively.*  
    
  *Rationale: For certain mission critical events, ground response may not be possible and the autonomous fault protection design must ensure completion in the event of a single fault.*
* **4.9.2.3.1 Accommodation of processor resets** - The design shall accommodate processor resets during mission-critical events.
* **4.11.2 Initialization**
* **4.11.2.1 Nominal flight software initialization** - Flight software shall be designed to initialize software and hardware to a known, safe, and deliberate state.  
    
  *Note: Elements to consider when establishing state include inertial, temporal, device capability or configuration, file allocation tables, and boot code in RAM.*
* **4.11.2.2 Multiple restart flight software initialization** - The software shall be designed to detect off-nominal restarts and to successively reinitialize with less and less dependency on preserved state (e.g., inertial, temporal, device capability or configuration, file allocation tables, boot code in RAM…) from before the most recent reset, until a fully known and tested initial configuration is obtained, and until stable operation has been restored.  
    
  *Note: Reset is commonly used as a means of autonomous recovery from serious software problems caused by errors or single event upsets. Reset is not effective unless the problematic software state is cleared during re-initialization. Ultimately, all software states must be presumed suspect and expendable, if prior re-initializations have failed to resolve a problem. A complete accounting of preserved state is essential, if effective measures are to be taken against it.*
* **4.11.2.3 Minimalist boot** - The boot implementation of the flight computer(s) software shall include a "minimalist" configuration that requires a minimum of on-board resources for vehicle safety and ground intervention.  
    
  *Note: This would include the ability to boot without resources that are of higher risk, or are not strictly required for safing. For example, some missions have included a separate flight software version that was capable of minimal operations without the file system.*
* **4.11.2.4 System initialization trace telemetry** - The flight software shall be designed to record and transmit its progress through each attempt at initialization.

### 3.4 MSFC

* **4.12.3.6 In situations that allow time for reboots, Flight software shall be designed to accommodate processor resets during mission-critical events.**  
    
  *Rationale: For certain mission critical events, ground response may not be possible and the autonomous fault protection design must ensure completion in the event of a single fault.*
* **4.12.3.12 The software shall be designed to record its progress through each attempt at initialization.**  
    
  *Rationale: Diagnostic code is to be designed and incorporated into the software early, and be accessible through flight interfaces, so that problem resolution can be done rapidly and easily at element and flight system level in development and during flight operations. Mission critical event data and visibility of mission-critical errors should be available via real time telemetry for diagnostic use on the ground or during testing.*

# 4. Resources

### 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-512)

  [Lewis Spacecraft Mission Failure Investigation Board](https://llis.nasa.gov/lesson/625 "Click to open in new window")

  Public Lessons Learned Entry: 625.
* (SWEREF-683)

  [Anomalous Flight Conditions May Trigger Common-Mode Failures in Highly Redundant Systems](http://llis.nasa.gov/lesson/1778 "Click to open in new window")

  Public Lessons Learned Entry: 1778, Date: 2007-03-6. Submitting Organization: JPL, Submitted by: Martin Ratliff

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) |

## 4.3  Center Process Asset Libraries

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

* **Anomalous Flight Conditions May Trigger Common-Mode Failures in Highly Redundant Systems**. **Lesson Learned 1778:** [683](#_tabs-<p>4</p>) "After launch, MRO was found to be susceptible to a solar flare event during the critical aerobraking phase of the mission that could corrupt the multiply redundant identical file systems in the Command & Data Handling subsystem. This could have caused a mission failure during aerobraking if the files had been needed for entry into safe mode or to perform an SEU-induced reboot of the flight computer. Assure that fault tolerant designs reflect full consideration of anomalous conditions that could trigger common-mode failures."
* **Lewis Spacecraft Mission Failure Investigation Board**. **Lesson Learned 0625:** [512](#_tabs-<p>4</p>) "The Board found that the loss of the Lewis Spacecraft was the direct result of an implementation of a technically flawed Safe Mode in the Attitude Control System. This error was made fatal to the spacecraft by the reliance on that unproven Safe Mode by the on orbit operations team and by the failure to adequately monitor spacecraft health and safety during the critical initial mission phase."
