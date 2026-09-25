# 9.11 Invalid Data Handling

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695802. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling

9.11 Invalid Data Handling

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695802)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695802&showCommentArea=true&showComments=true#addcomment)

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

Design software to handle invalid data appropriately. 

## 1.1 Rationale

The ability to continue operating in the presence of invalid data and react appropriately can prevent responses that lead to hazardous conditions.

## 2. Examples and Discussion

Invalid data can be the result of noisy signals, environmental conditions outside the expected range, malfunctions, software design errors (e.g., function calls outside of valid range) that result in faults, reuse of software in a system with different interface specifications, and other unforeseen situations. Although typically the optimum solution is to design the software to prevent acceptance of invalid input data, robust software often must be able to handle invalid input data without total loss of functionality (defensive programming). An analysis must be performed to determine how the software should respond to erroneous inputs. In some cases, the best response is to simply ignore the erroneous input (e.g., non-critical temperature sensor). In other cases, (e.g., navigation as mentioned in the documents listed below) the best response is for the software to estimate the value of the missing/erroneous inputs. In all cases, an analysis must also be performed to determine how long the software should continue to operate without valid data from each component, in light of safety concerns.

One specific case is data that is received that is not valid in the current state of the control system. A common example is a command being received that is not valid in the current state. The software must validate not only the formatting of commands but also the state of the system when a command is received to ensure validity. If possible, command validity for the current state of the target system is checked by both the sender (e.g., Ground Station) and the receiver. This double checking method forces the sender to check the state of the target and the receiver to protect itself against invalid commands.

In the same way that commands can be received that are not valid in the current state, data can be received that is within the range of valid outputs from a component but is not valid in the current state of the system. For instance, the software might receive a message from a component that includes a set of sensor data before power has been applied to the subsystem.

Some methods that have been used to mitigate the effects of invalid data include smoothing algorithms for noisy data, using a previous valid value, use of a redundant data item, and discarding invalid data. For discrete data, transient discretes can be suppressed by requiring a number of consecutive discretes to match before taking action.

Reporting the receipt of invalid data and any action taken in response can alert operators to a potential problem.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.2.4.8 Response to Off-Nominal Inputs**

Software should accommodate both nominal inputs (within specifications) and off-nominal inputs, from which recovery may be required. See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing). 

### 3.2 GSFC

None

### 3.3 JPL

* **4.11.4.2 Response to incorrect commands, loads, data, or memory**

     a. Flight software shall be designed to detect and respond safely to corrupted commands, data, or loads, and memory faults allocated to the software, such as stuck bits or single event effects (SEE).  
  
*Note: For example, flight computer designs have included Error Detection And Correction (EDAC) logic on EEPROMs, and the load process has been designed to detect and respond to failure if the EDAC detects an uncorrectable bit error. Software designs have included check sum logic and periodic verification of memory to detect command, data, or load, and memory faults.*  
  
     b. Flight software shall be designed to detect and respond safely to commands, data, or loads, that are incorrectly formatted, including invalid values, or out of range parameters.  
  
     c. Flight software shall be designed to detect and respond safely to commands, data, or loads that are invalid in the current context.  
  
*Note: For example, a command handler should check whether a received command is appropriate for the current system mode, and a software module should check whether a command is appropriate for its local state.*

### 3.4 MSFC

* **4.12.3.4 Software shall accommodate both nominal inputs (within specifications) and off-nominal inputs, from which recovery may be required.**  
    
  *Rationale: Inputs to algorithms outside of expected range are indicators of potential fault conditions and software must continue to function until the fault condition is detected and resolved.*
* **4.12.3.5 Software shall perform integrity checks on input and output across the computing system boundary.**  
    
  *Rationale: The software design should ensure that only valid inputs and outputs are incorporated into the control system state. An integrity check ensures the message is well-formed and not corrupted. Potential faults and the action taken must be defined and determined so that actions taken upon error detection do not set off a chain reaction leading to more serious fault conditions, e.g., issuance of questionable commands to actuators as a result of a fault condition that exacerbates the problem.*
* **4.12.3.7 Software shall be designed to detect and respond to incorrectly formatted commands, data, or loads, and memory faults allocated to the software.**  
    
  *Note: For example, flight computer designs have included Error Detection And Correction (EDAC) logic on EEPROMs, and the load process has been designed to detect and respond to failure if the EDAC detects an uncorrectable bit error. Software designs have included check sum logic and periodic verification of memory to detect command, data, or load, and memory faults.*  
    
  *Rationale: Inputs to the software outside of expected range are indicators of potential fault conditions and software must continue to function until the fault condition is detected and resolved. Incorrectly formatted inputs should be detected and handled by the software as a part of the Fault detection, isolation and recovery functionality.*

# 4. Resources

### 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-501)

  [Mars Observer Inertial Reference Loss](https://llis.nasa.gov/lesson/310 "Click to open in new window")

  Public Lessons Learned Entry: 310.
* (SWEREF-507)

  [Thrusters Fired on Launch Pad (1975)](https://llis.nasa.gov/lesson/403 "Click to open in new window")

  Public Lessons Learned Entry: 403.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-676)

  [Provide Software Checks On All Spacecraft Command Constraints (1997)](http://llis.nasa.gov/lesson/567 "Click to open in new window")

  Public Lessons Learned Entry: 0567, Date: 1998-04-09, Submitting Organization: JPL, Submitted by: C. Guernsey/D. Oberhettinger
* (SWEREF-677)

  [Orbiter Software Upgrades](http://llis.nasa.gov/lesson/195 "Click to open in new window")

  Public Lessons Learned Entry: 0195, Date: 1992-11-04, Submitting Organization: KSC, Submitted by: David Pennington
* (SWEREF-684)

  [Flight Software Deadly Embrace](http://llis.nasa.gov/lesson/369 "Click to open in new window")

  Public Lessons Learned Entry: 0369, Date: 1995-01-24, Submitting Organization: JPL, Submitted by: B. Larman

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

The NASA Lesson Learned [439](#_tabs-<p>4</p>)  database contains the following lessons learned related to invalid data handling:

* **Mars Observer Inertial Reference Loss**. **Lesson Learned 0310: [501](#_tabs-<p>4</p>)**  "Mars Observer experienced inertial reference loss on several occasions during its cruise to Mars. These incidents were due to the lack of a detailed code walk-through, and to use of gyro noise values, obtained from in-house test, that were more optimistic than the manufacturer's specifications. Do not depend on hardware performance being better than the manufacturer's specification. Perform detailed code walk-through of critical software modules. Pay special attention to inherited critical software. Design the flight computer and software to permit necessary changes in flight."
* **Probable Scenario for Mars Polar Lander Mission Loss (1998)**. **Lesson Learned 0938:** **[529](#_tabs-<p>4</p>)** "Neither the MPL software requirements specification nor the software, subsystem or system test plans required verification of immunity to transient signals. MPL touchdown sensors generated known transient signals at leg deployment. Full leg deployment test was not repeated after wiring corrections. Tests should be re-run after test deficiencies are corrected or hardware or software is revised unless clear rationale exists for not doing so. Hardware operational characteristics, including transients and spurious signals must be reflected in software requirements and verified by test."
* **Flight Software Deadly Embrace**. **Lesson Learned 0369:**[684](#_tabs-<p>4</p>)****  "During a walk-through of the Galileo Spacecraft System fault protection implementation a possible "deadly embrace" in the flight software was uncovered. A deadly embrace is a continuous software looping operation that may preclude the achievement of an acceptable spacecraft state."
* **Orbiter Software Upgrades**. **Lesson Learned 0195:** **[677](#_tabs-<p>4</p>)** "The movement of some requests for software upgrades to crew procedures is a matter of serious concern. The crew already has a very large number of procedures with which to be familiar. Adding to that load, particularly with items that could be handled easily with greater reliability and safety by software, does not seem wise. Procedures such as "do not touch the keyboard for X seconds after the occurrence of event Y" can be handled easily by software. If such procedures are contingencies that are employed infrequently, the chance of error when they are needed rises." A review of all computer-related procedures to ascertain whether or not there is significant potential for design-induced human errors should be mounted. This review should include crew representatives, experts on human factors, and members of safety and mission quality organization."
* **Provide Software Checks On All Spacecraft Command Constraints (1997)**. **Lesson Learned 0567:**[676](#_tabs-<p>4</p>)****  "The Command and Control Subsystem for a commercial satellite lacked software command constraint checks. A gyro sensitivity setting that was incompatible with on-orbit testing of the thrusters resulted in a severe spin. Recommendations involve allowable command parameters, walk-throughs of critical mission command sequences, and use of a system testbed facility."
* **Thrusters Fired on Launch Pad (1975)**. **Lesson Learned 0403:**[507](#_tabs-<p>4</p>)****  "Inadvertent commanding of the safing sequence while the Viking (VO-2) spacecraft was still on the launch pad enabled the RCS thrusters. The thrusters fired in an attempt to compensate for the Earth's rotation, resulting in a significant loss of attitude control gas. When command sequences intended to be exercised only in the event of abnormal spacecraft activity are stored onboard, consider the consequences of their activation during system test or the pre-launch phases."
