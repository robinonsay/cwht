# 8.09 - Software Safety Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695725. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis

8.09 - Software Safety Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695725)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695725&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Relationship with Hazard Analysis](#tabs-2)
* [3. Performing Software Safety Analysis](#tabs-3)
* [4. Other Notes](#tabs-4)
* [5. Resources](#tabs-5)

# 1. Introduction

Software Safety Analysis (SSA) is a term that is used to describe a wide range of analyses.  This article provides guidance on performing an SSA to satisfy the NASA-STD-8739.8 [278](#_tabs-<p>5</p>) requirement associated with NPR 7150.2 [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software).  This requirement intends to assess the software causes and controls of a system hazard analysis to ensure the software and firmware meets the needs of the hazard and align with the risk claims within the hazard report.  There are several other forms of analysis that support the safety aspects of software development such as requirements and test analysis.  These analyses are out of scope for this article but the ties to the SSA supporting hazard analysis will be covered.

## 1.1 Purpose

This article will provide guidance on performing an SSA on a NASA project or program to assure the software supports the claims and risk profile documented by supported system hazard analysis.

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 2. Relationship with Hazard Analysis

As previously mentioned, the SSA supports system hazard analysis.  The final acceptance or approval of the SSA comes with the approval of the supported hazard analyses.  The software functions which appear as hazard causes or controls require an SSA.  It is acceptable to extend the SSA approach to mission-critical software functions.  It is also noted that a very detailed hazard report and some hazard verification activities may cover some of the goals of the SSA which is perfectly acceptable.  It is rare; however, that standard system hazard analysis will adequately analyze the details of the software and avionics design and implementation to avoid the need for an SSA. See also Topic [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis),

The SSA traces to the hazard analysis through the identification of Must Work Functions (MWF) and Must Not Work Functions (MNWF) within a hazard report.  Typically, a hazard cause describing software failing to perform a function will be a Must Work Function.  For example, a hazard cause describing flight software failing to initiate a solar array deployment is describing a software Must Work Function.  A hazard caused by describing flight software inadvertently deploying a solar array is describing a software Must Not Work Function.  In this example, the solar array deployment function is both a MWF and a MNWF (this is not uncommon).  These functions are the target of the supporting SSA and have clear traceability between a hazard report cause/control to analysis within an SSA.

Defining the MWF and MNWF can be difficult. The functions must be defined at the right level of detail to have an efficient and thorough SSA.  Consider the Fault Tree Analysis (FTA) in Figure 1 that is identifying causes for the *Loss of Attitude Control* hazard.  Defining the function at too high a level would complicate the SSA.  Declaring the MWF of *Maintain Attitude Control* would require analysis of Guidance, Navigation and Control (GNC), and thruster control and tank pressure control with very diverse sets of inputs, Fault Detection Isolation and Recovery (FDIR), commands, etc.  It would be very difficult to organize the material.  Defining the function at too low a level will result in a very large number of functions to analyze.  For medium and large projects, this will become unwieldy.  Defining a MNWF of *Operating the Pressure Relief Valve* would require several other functions such as MWF *Operating the Pressure Relief Valve*, MWF *Injecting Tank Pressure*, MNWF *Injecting Tank Pressure*, etc., which are all using the same sensors and effectors.  This approach will cause a lot of repeated information, unnecessary documentation overhead, and be a configuration management challenge.  In this example, defining a MWF of *Maintain Tank Pressure* is the right balance.  A rule of thumb is to define the function as high as possible without causing a large increase in the sensors and effectors that are in scope.

***Figure 1: Software Function Definition Example***

The preceding information assumes a system hazard analysis exists.  If a project has safety-critical software but does not have system hazard analysis available, a top-down analysis (such as a Fault Tree Analysis) is recommended to identify critical software capabilities and functions to enable the SSA. See also [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis).

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 3. Performing Software Safety Analysis

There are several methods to perform an SSA.  The method should be selected based on the class and criticality of the software.  The Assurance Topics: [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) in this Handbook offer guidance for various types of analysis and the Computer-Based Control System Safety Requirements (SSP 50038) provides requirements that drive a rigorous SSA called a Computer-Based Controls Systems (CBCS) analysis by the International Space Station (ISS) Program.  Software Fault Tree Analysis and Software Failure Modes and Effects Analysis can be valid methods but must meet the SSA goals and typically are paired with supplemental analysis and verifications depending on the complexity and criticality of the software under analysis.  The recommended method is a collection of analyses that are documented in a framework that is organized by the SSA Goals in [*Table 1: Goals of an SSA*].

The SSA is ideally a system-level assessment with strong avionics and subsystem input assisting the software safety analyst.  For example, assessing the communication path between redundant sensors to redundant flight computers to redundant effectors is very difficult without an avionics expert to detail the communication bus routing in the hardware and a software expert to detail any virtual Local Area Networks (LANs) and proxies.  The SSA often serves as a point of integration to engage subsystem leads to ensure they understand the software behavior.

The actual SSA product can be an attachment to the supported hazard reports, several small analysis documents, or one large analysis document.  The SSA follows the phased safety analysis and gets updated for the Phase 0/1 (~Preliminary Design Review (PDR)), Phase 2 (~Critical Design Review (CDR)), and Phase 3 (before Flight Readiness Review (FRR)) reviews.  Guidance for meeting each goal through the development cycle is captured in the following sections. See also [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews), [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria),

Planning and performing a software assurance analysis should consider the class and criticality of the software functions.  The approach and rigor should be tailored appropriately.  For example, a MWF controlling a hazard that also has two mechanical controls will not need a rigorous analysis (unless it is a particularly risky hazard cause).  On the other extreme, software that is controlling multiple legs of a given hazard’s inhibits should receive a more rigorous examination. 

**Table 1: Goals of an SSA**

|  |  |
| --- | --- |
|  | **Goals of a Software Safety Assessment** |
| 1 | Confirm external software safety requirements are met |
| 2 | Ensure hazard inhibit independence is not violated |
| 3 | Ensure hardware redundancy independence is not violated |
| 4 | Assess Fault Detection Isolation and Recovery (FDIR) |
| 5 | Assess hazardous commands and critical telemetry |
| 6 | Support other Software Assurance tasks |

## 3.1 Confirm external software safety requirements are met

There are many sources of software safety requirements.  The prime example is NPR-7150.2 [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), which includes several functional requirements for safety-critical software.  The SSA can serve as a framework to identify the MWF and MNWF that must meet these requirements and assess the functions for compliance.  As previously mentioned, SSP 50038 has an excellent list of detailed software safety functional requirements that can serve as a reference for what requirements a SSA could analyze.

#### Example

|  |  |
| --- | --- |
| **Safety Phase** | **SSA** |
| P0/P1   (PDR) | Review Hazard Reports:  Identifies Solar Array Deployment as a MWF |
| P2   (CDR) | SWE-134   requires safe initialization.  The SSA defines the safe initialization state of the solar array deployment motor controllers to be powered off during the ascent phase while the fairings are still attached. |
| P3   (<FRR) | The SSA is used to inform test planning to simulate a flight computer reboot during ascent.  An analysis of the test log shows that when the flight software boots up, the solar array deployment motor controllers are initially unpowered. |

See also Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews),

## 3.2 Ensure hazard inhibit independence is not violated

One of the prime hazard control strategies is electro-mechanical inhibits.  These inhibits support meeting failure tolerance requirements and are often controlled by software.  The software has the unique ability to bundle multiple commands into a single stored command sequence (script) and can easily remove all hazard inhibits with a single action.  The software must be very careful not to violate the independence of hazard inhibits.

It is possible to define stored command sequences never to remove more than one inhibit for a given hazard, but this is often not practical.  On the other hand, using a stored command sequence allows a ground operator to recover from an off-nominal scenario quickly.  Using a stored command sequence can reduce the number of commands that must be sent (risk of human error) and can reduce the time it takes to issue a set of commands (time to effect).  A common approach is to protect inadvertent removal of inhibits through the use of pre-requisite logic, interlocks, and the use of independent trigger parameters.  The SSA should assess the stored command sequences, the triggers that automatically initiate the sequences, and the pre-requisite logic to ensure the risk of inadvertently removing multiple inhibits in a given hazard report is acceptable.  It is imperative to search all forms of stored command sequences including FDIR, on-board autonomous sequences, ground software scripts, console operator scripts, testing scripts, and safing sequences.  Be sure to include vehicle state and mode transitions which can kickoff stored command sequences. See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing)

#### Example

|  |  |
| --- | --- |
| **Safety Phase** | **SSA** |
| P0/P1   (PDR) | Review Hazard Reports: Identifies Solar Array Deployment as a MNWF |
| P2   (CDR) | Review Hazard Reports to identify the FETs on the high and low side of the solar array deployment motor controller power feed as the inhibits to inadvertent solar array deployment.    The following commands close these FETs (which removes the hazard inhibit)   * slr\_dply\_mc\_low\_close * slr\_dply\_mc\_hi\_close * slr\_dply\_mc\_pwr\_test     The following stored command sequences issue these commands and are triggers, and pre-requisite logic that initiates these sequences are assessed.    |  |  |  | | --- | --- | --- | | Initiator | Name/Description | Analysis | | Automated sequence     (Flight Software (FSW)) | Solar\_array\_deploy | *Solar\_array\_deploy* is called by the flight software 30 seconds after the vehicle detects fairing separation.  The stored command sequence closes the high and low deployment motor controller power Field-Effect Transistors (FETs) to initiate solar array deployment.   Independent Parameter check:  This fairing separation is detected by two of three break wires.  Each of the three break wires is fed to the flight computers by three independent communication paths.  In this logic, all three parameters are independent, and it requires two independent parameters to fail to initiate this sequence.       Pre-requisite Logic check:  The power unit which receives the FET closure commands checks that the vehicle is in the *Solar Array Deploy Prep* state before executing the commands.  If the commands are received outside of this state, the FETs will not be closed, and a command rejects counter is incremented. | | Test script | SA\_E2E\_checkout | The solar array end to end checkout performed at the launch site requires the solar array motor controllers to be powered.  This test script is manually issued by the test conductor and closes both FETs by sending the *slr\_dply\_mc\_pwr\_test* command.       This test command does not exist in any onboard stored command sequence and is excluded from the ground software command database so there is the little risk this command poses during the mission.       There are strict test procedures which include exclusion zones and restraint pins that protect ground     personnel from an inadvertent deployment, so there is little risk of harm due to inadvertent solar array deployment during testing | |
| P3   (<FRR) | The   SSA was updated to include two new hazardous commands that were added (*pwr\_ch1a\_on,* *pwr\_ch2a\_on*) and then confirmed no new stored command sequences call these commands.  After sequence testing was completed, the SSA referenced the appropriate test cases which confirm that solar array deployment motor controllers were not inadvertently powered |

## 3.3 Ensure hardware redundancy independence is not violated

Software is in control of most of the hardware, and in space systems, it often has to manage redundant hardware.  Poorly designed software logic or incorrectly channelized communication and power can violate the independence of redundant hardware.  The SSA must assess each critical software function to ensure the redundancy management is performed correctly.

It is important to assess how software combines redundant sensors.  For example, performing selecting the median (mid-value selection) from three sensors is a great way to be single failure tolerant to a sensor failure.  What if two fault tolerance is required?  Sometimes there are validation criteria and health checks that can be added to the mid-value selection that approach risk levels near two fault tolerance.  Merging redundant inputs becomes more difficult if the inputs are not the same type.  For example, consider three-position indicator sensors: two limit switches and one potentiometer-based position sensor.  The software must find a way to normalize the sensor inputs to combine them and retain fault tolerance.

For open-loop software control, the trigger logic must be failure tolerant.  A hazard analysis will sometimes cover the trigger logic but if not, the SSA must assess the Boolean logic and persistency to ensure fault tolerance is retained.  An FDIR trigger that uses several OR checks poses a risk to MNWFs.  A vehicle state transition that uses several AND checks poses a risk to MWFs.

For open and closed-loop software control functions that utilize redundant sensors and effectors, the SSA must assess the communication path and the power supply to each leg of redundancy. For open and closed-loop software control functions that utilize redundant sensors and effectors is a situation where the software safety engineer will benefit from having support from the avionics and power subsystem teams.  Having three pyro controllers with Ethernet communication buses passing through the same network switch is vulnerable to a single failure at the switch.  The power subsystem team often performs power channelization, but it is less common to have a detailed communication channelization analysis for a given safety-critical software function.

#### Example

|  |  |
| --- | --- |
| **Safety Phase** | **SSA** |
| P0/P1   (PDR) | Reviews Hazard Reports and identifies *Solar Array Deployment* as a MWF |
| P2   (CDR) | The following sensors are involved with the *Solar Array Deployment* along with their communication and power channelization analysis:   * Fairing Breakwire 1a   + Comm: sensor -> ADC I/O 1a ->   Ethernet LV switch 1a -> LV Flight Computers A and B -> triplicated   LV/SC umbilical -> Spacecraft Flight Computers A and B   + Power: N/A (passive sensor) * Fairing Breakwire 1b   + Comm: sensor -> ADC I/O 1b ->   Ethernet LV switch 2a -> LV Flight Computers A and B -> triplicated   LV/SC umbilical -> Spacecraft Flight Computers A and B   + Power: N/A (passive sensor) * Fairing Breakwire 2a   + Comm: sensor -> ADC I/O 2b ->   Ethernet LV switch 2b -> LV Flight Computers A and B -> triplicated   LV/SC umbilical -> Spacecraft Flight Computers A and B   + Power: N/A (passive sensor)     Fairing break wires 1a and 1b **do not**  have independent communication paths:  Fairing break wires 1a and 1b share Analog to Digital Converter 1.  They are wired to different sides but ADC 1 is not internally fault-tolerant to ground faults.  The hazard report claims three independent break wire sensors but has been proven to be incorrect.  ***The design must be changed or the hazard report must be updated.***    Note:  Breakwires 1b and 2a communicate to the Launch Vehicle flight computers through LV switch 2, which is fully internally redundant and poses no independence issues. |
| P3   (<FRR) | Review of the final master wiring list and final configuration files confirm the data in the SSA is still accurate.  A review of the software qualification tests has confirmed that injected communication errors at LV Ethernet switch 2a did not impact Spacecraft’s flight computers from sensing Fairing Breakwire 2a. |

## 3.4 Assess Fault Detection Isolation and Recovery

Fault management and FDIR is a critical function that often shows up as a hazard control.  These FDIR controls could be identified as a MWF, but, more commonly, MWFs are defined at a higher level as shown in Figure 1.  Regardless of how the MWF/MNWFs are defined, FDIR must be analyzed within the SSA when it can disable a MWF and initiate a MNWF.

The fault detection trigger logic must be fault-tolerant when it can disable a MWF or initiate a MNWF.  The fault detection trigger logic is often straight forward by assessing the trigger Boolean logic.  Be suspicious of ORs as they represent several conditions that could initiate the response.

FDIR is often in place to detect faults that require very fast responses to avoid a hazard.  The FDIR means that there is a risk trade for the amount of persistence required before action is taken and how broad the response will be.  For example, if a fire is detected in a crew cabin, O2 injection will be halted.  This state probably means this FDIR will disable all of the redundant O2 feeds.  Oxygen injection is a must work function but the time to effect of not having O2 injection is on the order of minutes for most designs and the time to effect of the fire is very fast.  In this situation, a small persistency or a “hair trigger” logic for fire detection may be acceptable despite the possibility of a false positive (which disables a MWF) because an operational response to restore oxygen flow can easily occur before the crew runs out of air.

The most complex aspect of analyzing FDIR is interactions with other FDIR or other automated functions.  It is recommended that FDIR only be enabled when the hazard/fault is possible to reduce the unintended consequences.  There is no need to have FDIR that will deploy parachutes in a contingency scenario active during ascent.  The SSA should ensure the FDIR is enabled and disabled at correct times.  Also, the SSA should inspect the FDIR for its ability to interfere with other MWF and MNWF or other FDIR.  For example, FDIR that closes an isolation valve if pressure drops in a tank may cause a pressure spike and trip other upstream high-pressure FDIR causing another FDIR to take action.  This example is yet another example of the system perspective that is important in an SSA.

#### Example

|  |  |
| --- | --- |
| **Safety Phase** | **SSA** |
| P0/P1   (PDR) | Review Hazard Reports and identify Oxygen Injection as a Must Work Function and Fire Detection as a Must Work Function |
| P2   (CDR) | Fire   FDIR:  Fire is detected when two of three smoke detectors indicate the presence of fire for five consecutive cycles.  When the FDIR response is enabled, all O2 injection will be stopped.    Analysis:  Inadvertent activation of this fault is one fault-tolerant due to sensor failure and is tolerant of sensor noise due to the persistence of the trigger.  Turning off O2 injection is disabling a Must Work function that can cause a hazard (Toxic Environment).  The time to effect of incurring injury or death of the crew by inadequate O2 is 1.5 hrs.  There is adequate time for the ground or crew to acknowledge the fire alarm, don suits, and manually initiate the flow of O2 to the suits allowing for a longer-term solution to be executed. |
| P3   (<FRR) | A  review of the final FDIR configurations confirms the P2 analysis to be still correct.  A review of the FDIR software test verifications has confirmed that no unexpected system behavior or unintended system interactions following this FDIR response occurred. |

## 3.5 Assess hazardous commands and critical telemetry

One of the significant risks that software poses is from an inadvertent command.  Hazardous commands must be identified and have adequate protections in place to protect from human error (e.g., operator mistake) and from flaws in the automated internal software commanding (e.g., stored commanding sequences).  Hazardous commands are commands which disable Must Work Functions, enable Must Not Work Functions, and remove hazard inhibits.

It is typical to use graphical interface features such as requiring multiple steps to send hazardous commands to protect against inadvertent hazardous commanding by a human.  For example, when a console operator issues a command tagged as hazardous in the command database, the software will prompt the user asking if they are sure they want to issue the command. The Cancel button is highlighted by default, and the OK button is in a different location than the initial send command button.  This situation means that if the user accidentally double clicks or hits the enter key twice, it will not send the command.  Human Factors specialists often provide valuable input when designing the system to protect against these types of errors.

Protections are built into the mission software to protect against any inadvertent hazardous command (manual and automatically initiated). This case is usually through pre-requisite logic, interlocks, and multiple unique commands.

* Pre-requisite logic allows developers to define what internal software states and modes are safe to execute a given command.  For example, the payload separation command, which initiates detonation of all the separation bolts should not be executed if the vehicle is in a pre-launch mode.
* Interlocks allow a safe or unsafe condition to be defined so that software will assess before executing a command.  For example, the command to turn on a wind tunnel turbine is not allowed if the access door is not secured and locked.
* Multiple unique commands are similar to multiple-step commands in that they require several steps before an action is taken. Still, this strategy requires multiple commands to be defined within the software before a hazardous event is initiated.  For example, deploying parachutes requires the arm command to be received before the fire command and the fire command must follow the arm command by no more than 5 seconds.  In this example, the arm command closes the low side of the firing circuit and the fire command closes the high side of the firing circuit and the commands are two unique and diverse bit patterns.

In addition to protections for hazardous commands, telemetry is also important to monitor the safety of the system.  For many projects, the operations team must maintain situational awareness of the system’s configuration.  Telemetry must be provided that reports on the state of hazard inhibit and the health of the system.  An SSA can be used to assure adequate telemetry has been defined to monitor the MW and MNW functions.

#### Example

|  |  |
| --- | --- |
| **Safety Phase** | **SSA** |
| P0/P1   (PDR) | Review Hazard Reports and identify Parachute Deployment as a Must Not Work Function |
| P2   (CDR) | Analysis   Summary:  The drogue and main parachute deployment has three inhibits (pyro power bank,   firing circuit FET hi, firing circuit FET lo).  Commands which remove any of these inhibits are considered hazardous commands.  Drogue and main chute deployment use similar avionics and software commands.  The total number of steps to manually command a pyro firing is four but assumes the first inhibit is in place.  When the first inhibit is nominally removed in preparation for a pyro event, it only requires two commands to fire a pyro.  The design intends only to remove the first inhibit no more than 30 seconds before a pyro event.  It is acceptable for the limited vehicle modes and exposure window to only have 2 erroneous commands between an inadvertent chute deploy.  All other times have a two fault tolerance to erroneous manual commanding.    Note:   See Commanding software safety analysis section for general command protections    Analysis Details:  1st   inhibit (pyro bank power):  The pyro bank power inhibit is removed any time a pyro check is being performed (prelaunch) or in preparation for a pyro event.    Manual commanding of this inhibit from the ground console controlling this inhibit requires two steps to issue the command.    The flight software will only act on this command if the vehicle is in the Prelaunch checkout, Ascent, or EDL modes (the command is rejected if received in any other mode).    2nd   inhibit (fire circuit FET hi):  The hi side of the firing circuit is closed when the respective \_arm command is received.  The command begins charging the firing circuit but does not result in firing the pyro until the lo side is closed.  This command does not exist in the ground software command database and can only be manually issued by entering the raw command in a protected window in the ground software.    3rd   inhibit (fire circuit FET lo):  The lo side of the firing circuit is closed when the respective \_fire command is received.  The command dumps the firing circuit energy to the pyro initiator, which causes the pyro charge to fire.  This command is only accepted if it follows the arm command by no more than 5 seconds.  This command does not exist in the ground software command database and can only be manually issued by entering the raw command in a protected window in the ground software. |
| P3   (<FRR) | The final hazardous command list has been generated      |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Inhibit | Command | Mnemonic | Hazardous | Two-Step | Mission Phase | | 1 | pwrbnkpyro | Pyro Power Bank Enable | Yes | Yes | Prelaunch\_checkout, Ascent,  EDL | | 2 (drogue) | dchutearm | Drogue Chute     Deploy\_arm (hi side) | Yes | No | EDL | | 3 (drogue) | dchutefire | Drogue Chute Deploy\_fire (lo side) | Yes | No | EDL | | 2 (main) | mchutearm | Main Chute Deploy\_arm (hi side) | Yes | No | EDL | | 3 (main) | mchutefire | Main Chute Deploy\_fire (lo side) | Yes | No | EDL | |

## 3.6 Support other Software Assurance tasks

The value an SSA can provide is not limited to supporting hazard analysis.  A timely SSA can be used to inform requirements, design, implementation, verification, and operations:

* Requirements:
  + SSA can inform requirements development by providing a lower level trace surface than what a systems hazard analysis provides.  It is important to trace hazard controls to requirements to perform a gap analysis to assure hazard controls are fully specified.  An SSA can be used for this trace to have a complete gap analysis.
* Design:
  + During Phase 2 SSA, the analysis can identify safety improvements to inform the design just as a hazard analysis can and should inform design.
* Implementation:
  + The SSA can be used to ensure software commands are correctly classified and architected to be safe (e.g., multiple unique commands) and that stored command sequences have the appropriate pre-requisite logic, trigger logic, persistency, etc.
* Verification
  + The SSA can inform test plan development by identifying the off-nominal scenarios, fault injections, and define the test passing criteria (SSA can define the safe state through time).
* Operations
  + SSA can inform Ops and Flight Notes, procedures, etc. when manual responses and actions are identified to cover design/implementation issues through the analysis.  It also identifies the inhibits, hazardous commands, and telemetry, which are valuable information to reference when an issue arises during operation.

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) , [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality), [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists), [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists)

See also [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description), [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews), [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria),

## 3.7 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Other Notes

## 4.1 Platform Critical Services

The bulk of the guidance provided in the above sections focuses on software functions controlling specific effectors and subsystems.  There will be several critical functions identified as MWF and MNWF in hazard analysis that are general software services such as:

* Memory management and scrubbing
* Timekeeping
* Error handling and fault management
* Command validation
* Interrupt handling
* Sensor validation
* Redundancy management

These critical platform services also need to be analyzed and can be treated as a MWF, but the analysis approach will be different than a subsystem analysis.  For example, there will still be hazardous commands that can disable, reboot, and mask these critical functions. Still, it is unlikely to have electro-mechanical hazard inhibits in place for commanding.  The software safety analyst will need to use engineering judgment to define the analysis detail and approach for these critical services.

#### Example

|  |  |
| --- | --- |
| **Safety Phase** | **SSA** |
| P0/P1   (PDR) | Reviews Hazard Reports and identifies *Software Patching* as a MWF |
| P2   (CDR) | (Assessing Goal 4: Fault Detection Isolation and Recovery)    …  Throughout the software patching process, a watchdog is active that will ensure the flight computers remain active.  If the watchdog is not serviced for five consecutive cycles, it will reboot the flight computers.  Since the watchdog is active in all flight computer modes, there is a risk that the watchdog will cause an infinite boot loop, specifically if rebooting during the boot sequence, and it may be unrecoverable given the non-deterministic nature of how ground communication is established during the boot sequence.  **Risk Ticket 314159 has been entered to address this concern**  … |
| P3   (<FRR) | Risk   Ticket 314159 has been resolved by Change Ticket 6022, which disables the watchdog during the boot sequence to permit a ground command and software update to be uploaded to resolve the issue. |

## 4.2 Complex Electronics

Complex electronics such as FPGAs commonly serve critical roles within modern safety-critical NASA projects.  The logic onboard complex electronics is a candidate for MWF and MNWF and should be analyzed within the SSA.

## 4.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-337)

  [Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf "Click to open in new window")

  Souppaya, Murugiah, Scarfone, Karen, NIST Special Publication NIST SP 800-40r4, April, 2022

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
