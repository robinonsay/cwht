# 8.21 - Software Hazard Causes

> NASA Software Engineering Handbook (SWEHB Ver D), page id 109969546. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/109969546/8.21+-+Software+Hazard+Causes

8.21 - Software Hazard Causes

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/109969546/8.21+-+Software+Hazard+Causes#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=109969546)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=109969546&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Introduction

## 1.1 Software Hazard Causes

When a device or system can lead to injury, death, the destruction or loss of vital equipment, or damage to the environment, system safety is paramount.  The system safety discipline focuses on  “hazards” and the prevention of hazardous situations.

A hazard is the presence of a potential risk situation that can result in or contribute to a mishap. To ensure the system being developed is as safe as possible, it is important to begin identifying potential hazards as early as possible in the development. Thus, the software and system safety personnel generally look at the hazardous events that could happen and what could potentially cause them.

Every hazard has at least one cause, which in turn can lead to several effects (e.g., damage, illness, failure). A hazard cause may be a defect in hardware or software, a human operator error, or an unexpected input or event which results in a hazard. The table below provides several potential software causes to consider in the project when developing the list of hazards and their potential causes.

Hazard control is a method for preventing the hazard, reducing the likelihood of the hazard occurring, or the reduction of the impact of that hazard.  Hazard controls use software (e.g. detection of the stuck valve and automatic response to open secondary valve), hardware (e.g. pressure relief valve), operator procedures, or a combination of methods to avert the hazard.  For every hazard cause, there must be at least one control method, usually a design feature (hardware and/or software) or a procedural step.

## 1.2 Table of Software Causes

**Potential Software Causes to Consider When Identifying Software Causes in Hazard Analysis**

**(Table taken directly from NASA-STD-8739.8B Appendix A GUIDELINES FOR THE HAZARD DEVELOPMENT INVOLVING SOFTWARE)**

| Software Cause Areas to Consider | Potential Software Causes |
| --- | --- |
| Data errors | 1. Asynchronous communications 2. Single or double event upset/bit flip or hardware induced error 3. Communication to/from an unexpected system on the network 4. An out-of-range input value, a value above or below the range 5. Start-up or hardware initiation data errors 6. Data from an antenna gets corrupted 7. Failure of software interface to memory 8. Failure of flight software to suppress outputs from a failed component 9. Failure of software to monitor bus controller rates to ensure communication with all remote terminals on the bus schedule's avionics buses 10. Ground or onboard database error 11. Interface error 12. Latent data 13. Communication bus overload 14. Missing or failed integrity checks on inputs, failure to check the validity of input/output data 15. Excessive network traffic/babbling node - keeps the network so busy it inhibits communication from other nodes 16. Sensors or actuators stuck at some value 17. Wrong software state for the input |
| Commanding errors | 1. Command buffer error or overflow 2. Corrupted software load 3. Error in real-time command build or sequence build 4. Failure to command during hazardous operations 5. Failure to perform prerequisite checks before the execution of safety-critical software commands 6. Ground or onboard database error for the command structure 7. Error in command data introduced by command server error 8. Incorrect operator input commands 9. Wrong command or a miscalculated command sent 10. Sequencing error, failure to issue commands in the correct sequence 11. Command sent in wrong software state or software in an incorrect or unanticipated state 12. An incorrect timestamp on the command 13. Missing software error handling on incorrect commands 14. Status messages on command execution not provided 15. Memory corruption, critical data variables overwritten in memory 16. Inconsistent syntax 17. Inconsistent command options 18. Similarly named commands 19. Inconsistent error handling rules 20. Incorrect automated command sequence built into script containing single commands that can remove multiple inhibits to a hazard |
| Flight computer errors | 1. Board support package software error 2. Boot load software error 3. Boot Programmable Read-Only Memory (PROM) corruption preventing reset 4. Buffer overrun 5. CPU overload 6. Cycle jitter 7. Cycle over-run 8. Deadlock 9. Livelock 10. Reset during program upload (PROM corruption) 11. Reset with no restart 12. Single or double event upset/bit flip or hardware induced error 13. Time to reset greater than time to failure 14. Unintended persistent data/configuration on reset 15. Watchdog active during reboot causing infinite boot loop 16. Watchdog failure 17. Failure to detect and transition to redundant or backup computer 18. Incorrect or stale data in redundant or backup computer |
| Operating systems errors | 1. Application software incompatibility with upgrades/patches to an operating system 2. Defects in Real-Time Operating System (RTOS) Board Support software 3. Missing or incorrect software error handling 4. Partitioning errors 5. Shared resource errors 6. Single or double event upset/bit flip 7. Unexpected operating system software response to user input 8. Excessive functionality 9. Missing function 10. Wrong function 11. Inadequate protection against operating system bugs 12. Unexpected and aberrant software behavior |
| Programmable logic device errors | 1. High cyclomatic complexity levels (above 15) 2. Errors in programming and simulation tools used for Programmable Logic Controller (PLC) development 3. Errors in the programmable logic device interfaces 4. Errors in the logic design 5. Missing software error handling in the logic design 6. PLC logic/sequence error 7. Single or double event upset/bit flip or hardware induced error 8. Timing errors 9. Unexpected operating system software response to user input 10. Excessive functionality 11. Missing function 12. Wrong function 13. Unexpected and aberrant software behavior |
| Flight system time management errors | 1. Incorrect data latency/sampling rates 2. Failure to terminate/complete process in a given time 3. Incorrect time sync 4. Latent data (Data delayed or not provided in required time) 5. Mission elapsed time timing issues and distribution 6. Incorrect function execution, performing a function at the wrong time, out of sequence, or when the program is in the wrong state 7. Race conditions 8. The software cannot respond to an off-nominal condition within the time needed to prevent a hazardous event 9. Time function runs fast/slow 10. Time skips (e.g., Global Positioning System time correction) 11. Loss or incorrect time sync across flight system components 12. Loss or incorrect time Synchronization between ground and spacecraft Interfaces 13. Unclear software timing requirements 14. Asynchronous systems or components 15. Deadlock conditions 16. Livelocks conditions |
| Coding, logic, and algorithm failures, algorithm specification errors | 1. Auto-coding errors as a cause 2. Bad configuration data/no checks on external input files and data 3. Division by zero 4. Wrong sign 5. Syntax errors 6. Error coding software algorithm 7. Error in positioning algorithm 8. Case/type/conversion error/unit mismatch 9. Buffer overflows 10. High cyclomatic complexity levels (above 15) 11. Dead code or unused code 12. Endless do loops 13. Erroneous outputs 14. Failure of flight computer software to transition to or operate in a correct mode or state 15. Failure to check safety-critical outputs for reasonableness and hazardous values and correct timing 16. Failure to generate a process error upon detection of arithmetic error (such as divide-by-zero) 17. Failure to create a software error log report when an unexpected event occurs 18. Inadvertent memory modification 19. Incorrect "if-then" and incorrect "else" 20. Missing default case in a switch statement 21. Incorrect implementation of a software change, software defect, or software non-conformance 22. Incorrect number of functions or mathematical iteration 23. Incorrect software operation if no commands are received or if a loss of commanding capability exists (inability to issue commands) 24. Insufficient or poor coding reviews, inadequate software peer reviews 25. Insufficient use of coding standards 26. Interface errors 27. Missing or inadequate static analysis checks on code 28. Missing or incorrect parameter range and boundary checking 29. Non-functional loops 30. Overflow or underflow in the calculation 31. Precision mismatch 32. Resource contention (e.g., thrashing: two or more processes accessing a shared resource) 33. Rounding or truncation fault 34. Sequencing error (e.g., failure to issue commands in the correct sequence) 35. Software is initialized to an unknown state; failure to properly initialize all system and local variables are upon startup, including clocks 36. Too many or too few parameters for the called function 37. Undefined or non-initialized data 38. Untested COTS, MOTS, or reused code 39. Incomplete end-to-end testing 40. Incomplete or missing software stress test 41. Errors in the data dictionary or data dictionary processes 42. Confusing feature names 43. More than one name for the same feature 44. Repeated code modules 45. Failure to initialize a loop-control 46. Failure to initialize (or reinitialize) pointers 47. Failure to initialize (or reinitialize) registers 48. Failure to clear a flag 49. Scalability errors 50. Unexpected new behavior or defects introduced in newer or updated COTS modules 51. Not addressing pointer closure |
| Fault tolerance and fault management errors | 1. Missing software error handling 2. Missing or incorrect fault detection logic 3. Missing or incorrect fault recovery logic 4. Problems with the execution of emergency safing operations 5. Failure to halt all hazard functions after an interlock failure 6. The software cannot respond to an off-nominal condition within the time needed to prevent a hazardous event 7. Common mode software faults 8. A hazard causal factor occurrence isn't detected 9. False positives in fault detection algorithms 10. Failure to perform prerequisite checks before the execution of safety-critical software commands 11. Failure to terminate/complete process in a given time 12. Memory corruption, critical data variables overwritten in memory 13. Single or double event upset/bit flip or hardware induced error 14. Incorrect interfaces, errors in interfaces 15. Missing self-test capabilities 16. Failing to consider stress on the hardware 17. Incomplete end-to-end testing 18. Incomplete or missing software stress test 19. Errors in the data dictionary or data dictionary processes 20. Failure to provide or ensure secure access for input data, commanding, and software modifications |
| Software process errors | 1. Failure to implement software development processes or implementing inadequate processes 2. Inadequate software assurance support and reviews 3. Missing or inadequate software assurance audits 4. Failure to follow the documented software development processes 5. Missing, tailored, or incomplete implementation of the safety-critical software requirements in NPR 7150.2 6. Missing, tailored, or incomplete implementation of the safety-critical software requirements in Space Station Program 50038, Computer-Based Control System Safety Requirements 7. Incorrect or incomplete testing 8. Inadequate testing of reused or heritage software 9. Failure to open a software problem report when an unexpected event occurs 10. Failure to include hardware personnel in reviews of software changes, software implementation, peer reviews, and software testing 11. Failure to perform a safety review on all software changes and software defects 12. Defects in COTS, MOTS, or OSS Software, 13. Failure to perform assessments of available bug fixes and updates available in COTS software 14. Insufficient use of coding standards 15. Missing or inadequate static analysis checks on code 16. Incorrect version loaded 17. Incorrect configuration values or data 18. No checks on external input files and data 19. Errors in configuration data changes being uploaded to spacecraft 20. Software/avionics simulator/emulator errors and defects 21. Unverified software 22. High cyclomatic complexity levels (over 15) 23. Incomplete or inadequate software requirements analysis 24. Compound software requirements 25. Incomplete or inadequate software hazard analysis 26. Incomplete or inadequate software safety analysis 27. Incomplete or inadequate software test data analysis 28. Unrecorded software defects found during informal and formal software testing 29. Auto-coding tool faults and defects 30. Errors in design models 31. Software errors in hardware simulators due to a lack of understanding of hardware requirements 32. Incomplete or inadequate software test data analysis 33. Inadequate built-in-test coverage 34. Inadequate regression testing and unit test coverage of flight software application-level source code 35. Failure to test all nominal and planned contingency scenarios (breakout and re-rendezvous, launch abort) and complete mission duration (launch to docking to splashdown) in the hardware in the loop environment 36. Incomplete testing of unexpected conditions, boundary conditions, and software/interface inputs 37. Use of persistence of test data, files, or config files in an operational scenario 38. Failure to provide multiple paths or triggers from safe states to hazardous states 39. Interface control documents and interface requirements documents errors 40. System requirements errors 41. Misunderstanding of hardware configuration and operation 42. Hardware requirements and interface errors, Incorrect description of the software/hardware functions and how they are to perform 43. Missing or incorrect software requirements or specifications 44. Missing software error handling 45. Requirements/design errors not fully defined, detected, and corrected) 46. Failure to identify the safety-critical software items 47. Failure to perform a function, performing the wrong function, performing the function incompletely 48. An inadvertent/unauthorized event, an unexpected, unwanted event, an out-of-sequence event, the failure of a planned event to occur 49. The magnitude or direction of an event is wrong 50. Out-of-sequence event protection 51. Multiple events/actions trigger simultaneously (when not expected) 52. Error or exception handling missing or incomplete 53. Inadvertent or incorrect mode transition for required vehicle functional operation; undefined or incorrect mode transition criteria; unauthorized mode transition 54. Failure of flight software to correctly initiate proper transition mode 55. Software state transition error 56. Software termination is an unknown state 57. Errors in the software data dictionary values |
| Human-machine interface errors | 1. Incorrect data (unit conversion, incorrect variable type) 2. Stale data 3. Poor design of human machine interface 4. Too much, too little, incorrect data displayed 5. Ambiguous or incorrect messages 6. User display locks up/fails 7. Missing software error handling 8. Unsolicited command (command issued inadvertently, cybersecurity issue, or without cause) 9. Wrong command or a miscalculated command sent 10. Failure to display information or messages to a user 11. Display refresh rate leads to an incorrect operator response 12. Lack of ordering scheme for hazardous event queues (such as alerts) in the human-computer interface (i.e., priority versus time of arrival, for example, when an abort must go to the top of the queue) 13. Incorrect labeling of operator controls in the human interface software 14. Failure to check for constraints in algorithms/specifications and valid boundaries 15. Failure of human interface software to check operator inputs 16. Failure to pass along information or messages 17. No onscreen instructions 18. Undocumented features 19. States that appear impossible to exit 20. No cursor 21. Failure to acknowledge an input 22. Failure to advise when a change takes effect 23. Wrong, misleading, or confusing information 24. Poor aesthetics in the screen layout 25. Menu layout errors 26. Dialog box layout errors 27. Obscured instructions 28. Misuse of color 29. Failure to allow tabbing navigation to edit fields (mouse only input) |
| Security and virus errors | 1. Denial or interruption of service 2. Spoofed or jammed inputs 3. Missing capabilities to detect insider threat activities 4. Inadvertent or intentional memory modification 5. Inadvertent or unplanned mode transition 6. Missing software error handling or detect handling 7. Unsolicited command 8. Stack-based buffer overflows 9. Heap-based attacks 10. Cybersecurity vulnerability or computer virus 11. Inadvertent access to ground system software 12. Destruct commands incorrectly allowed in a hands-off zone 13. Communication to/from an unexpected system on the network |
| Unknown Unknowns errors | 1. Undetected software defects 2. Unknown limitations for COTS (operational, environmental, stress) 3. COTS extra capabilities 4. Incomplete or inadequate software safety analysis for COTS components 5. Compiler behavior errors or undefined compiler behavior 6. Software defects and investigations that are unresolved before the flight |

See also Topic [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software),

**Note**:  Software is classified as safety-critical if the software is determined by and traceable to hazard analysis. See appendix A for guidelines associated with addressing software in hazard definitions. See [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software). Consideration for other independent means of protection (software, hardware, barriers, or administrative) should be a part of the system hazard definition process.

**Note**:  Fault tolerant systems are built to handle most probable, and some less probable but hazardous, faults. Taking care of the faults will usually help prevent the software, or the system, from going into failure.  The down-side to fault tolerance is that it requires multiple checks and monitoring at very low levels.  If a system is failure tolerant, it will ignore most faults and only respond to higher-level failures. A presumption is that it requires less work and is simpler to detect, isolate, stop, or recover from the failures. A project must weigh the costs and benefits of each approach and determine what will provide the most safety for the least cost and effort.

## 1.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-337)

  [Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf "Click to open in new window")

  Souppaya, Murugiah, Scarfone, Karen, NIST Special Publication NIST SP 800-40r4, April, 2022

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
