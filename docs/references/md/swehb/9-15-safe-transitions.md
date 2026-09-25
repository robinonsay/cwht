# 9.15 Safe Transitions

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695806. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions

9.15 Safe Transitions

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695806)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695806&showCommentArea=true&showComments=true#addcomment)

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

Assert required preconditions and post-conditions at software transitions.

## 1.1 Rationale

Assuming preconditions and post-conditions are met can lead to hazardous situations and system malfunction.

## 2. Examples and Discussion

When a system transitions from one state to another, the hardware configuration may change, software controls may be enabled or disabled, or both. For example, a transition from test mode to launch mode may enable the system to execute commands to power on transmitters, fire pyrotechnic devices, deploy mechanisms, and other potentially hazardous operations. When the system transitions back to test mode, commands to execute them can be inadvertently processed, and harm to personnel and equipment can ensue if these operations are not completely disabled. Unverified assumptions about system state can threaten mission success.

Useful development practice is to itemize the desired/required state of all aspects of the system at each state transition, and then ensure that all items on the list are implemented and verified. Desired/required states can be asserted by explicit command, or where this is not safe or practical, by verifying via other telemetry (e.g., a valve position might be verified by downstream pressure). Where additional safeguards are required or desired, another design option to consider would be to enforce a man-in-the-loop checkpoint that requires manual operator intervention before a system can transition to a potentially hazardous state.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

None

### 3.2 GSFC

None

### 3.3 JPL

None

### 3.4 MSFC

None

# 4. Resources

### 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-530)

  [MPL Uplink Loss Timer Software/Test Errors (1998)](https://llis.nasa.gov/lesson/939 "Click to open in new window")

  Public Lessons Learned Entry: 939.

  

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
|  |

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

The NASA Lesson Learned [439](#_tabs-<p>4</p>)  database contains the following lessons learned related to safe transitions:

* **MPL Uplink Loss Timer Software****/****Test Errors (1998)** **Lesson Learned 0939:** [530](#_tabs-<p>4</p>) "Prelaunch tests and verification of software and hardware used to switch to a redundant string should include assumed failures in either string during all mission phases. MPL did not verify the ability of the Lander to switch to the redundant uplink string after landing assuming a failure in the primary string had occurred during earlier entry, descent, and landing phases. Recognize that transitions to another mission phase are high-risk sequences and that database changes that impact logic decisions should be retested."
