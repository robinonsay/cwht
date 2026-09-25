# 9.13 Resource Oversubscription

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695804. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695804/9.13+Resource+Oversubscription

9.13 Resource Oversubscription

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695804/9.13+Resource+Oversubscription#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695804)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695804&showCommentArea=true&showComments=true#addcomment)

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

Include a robust and well thought out response to resource oversubscription situations in the software design.

## 1.1 Rationale

Resource oversubscription is a severe fault condition that can lead to unpredictable behavior of the software system and render it inoperable. Timely detection and planned response to oversubscriptions can preserve critical system capabilities.

## 2. Examples and Discussion

Many resources can become oversubscribed during system operation. Examples include: buffers overflowing, exceeding a rate group time boundary, and excessive inputs or interrupts. The usual response consists of reducing the demand presented on the system by non-essential items, especially if they are the cause of the oversubscription. The system can also generate error messages, being careful not to overload the system further, and attempt to throttle the demand presented to it by external entities. In severe cases interrupts may be locked out. Additionally, the system may be reconfigured to reduce/eliminate non-essential functionality, or to allow use of less-demanding (even if less-accurate) algorithms. In severe cases processes and even the computer may have to be shut down.

An example of a graceful response to an overload is the Apollo Lunar Module onboard software, which correctly handled an unplanned scenario in which the LM's ascent stage rendezvous radar was incorrectly switched on, overloading the Apollo Guidance Computer with input data. In this case the use of task prioritization (the Guidance, Navigation and Control (GNC) had higher priority than the radar), prevented the critical GNC functions from being starved of processor time, saving the mission and crew.

It is recommended that the system design include the monitoring of resource usage with appropriate thresholds set to trigger carefully designed escalation responses, and that the method for detection and response protocol be explicitly documented and verified in the requirements.

This design principle is closely related to the [9.12 Resource Margins](/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins) principle. Implementing run time measurements enables monitoring of margins during development as well as protecting against oversubscription once the software has been deployed operationally.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.2.4.5 Response to Resource Over-Subscription** - The software design should accommodate unintended situations where resource usage is oversubscribed. The action to be taken in such situations should be specified as part of the requirements on the design.

*Note: Examples of these situations include buffers overflowing, exceeding a rate group time boundary, and excessive inputs or interrupts. There are several common methods for tolerating these situations, most of which relate to reducing demand from non-essential items, especially if they are the source of over subscription:*  
  
     a. Generate warning messages when appropriate.  
     b. Instruct external systems to reduce their demands.  
     c. Lock out interrupts.  
     d. Change operational behavior to handle the load. For example, the software may use faster but less accurate algorithms to keep up with the load.  
     e. Reduce the functionality of the software, or even halt or suspend a process or shutdown a computer.

### 3.2 GSFC

None

### 3.3 JPL

* **4.11.4.5 Response to resource over-subscription** - The software design shall contain a robust response to situations where computer resources are oversubscribed. The action to be taken in such situations shall be specified as part of the requirements on the design.

*Note: Examples of these situations include buffers overflowing, exceeding a rate group time boundary, and excessive inputs or interrupts. There are several common methods for tolerating these situations, most of which relate to reducing demand from non-essential items, especially if they are the source of over subscription:*  
  
     a. Generate warning messages when appropriate.  
     b. Instruct external systems to reduce their demands.  
     c. Lock out interrupts.  
     d. Change operational behavior to handle the load. For example, the software may use faster but less accurate algorithms to keep up with the load.  
     e. Reduce the functionality of the software, or even halt or suspend a process or shutdown a computer.

### 3.4 MSFC

None

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-675)

  [Science Data Downlink Process Must Address Constraints Stemming from Fixed DSN Assets](http://llis.nasa.gov/lesson/1843 "Click to open in new window")

  Public Lessons Learned Entry: 1843, Date: 2008-02-19, Submitting Organization: JPL, Submitted by: David Oberhettinger

  

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [9.12 Resource Margins](/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins) |

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

The NASA Lesson Learned [439](#_tabs-<p>4</p>) database contains the following lessons learned related to resource oversubscription:

* **Science Data Downlink Process Must Address Constraints Stemming from Fixed Deep Space Network (DSN) Assets**.  **Lesson Learned 1843: [675](#_tabs-<p>4</p>)**  "Given their minimal ability to mitigate DSN resource limitations, flight projects must consider mission design and mission operations improvements that may help to achieve Level 1 requirements, such as the 9 measures effectively employed by the Spitzer project."
