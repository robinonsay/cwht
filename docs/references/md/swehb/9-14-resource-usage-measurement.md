# 9.14 Resource Usage Measurement

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695805. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695805/9.14+Resource+Usage+Measurement

9.14 Resource Usage Measurement

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695805/9.14+Resource+Usage+Measurement#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695805)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695805&showCommentArea=true&showComments=true#addcomment)

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

Incorporate timely visibility into the use of computing resources into the software design.

### 1.1 Rationale

Measurement of resource usage enables determination and validation of operating margins throughout the life cycle of the project, which can be indicators of potential error and fault conditions. It also enables measurement of critical computing resources, thereby maximizing the prospects for safe and reliable operation of the software.

# 2. Examples and Discussion

Examples of computing resources to be measured include: real time tasks, background tasks, throughput, memory utilization, bus utilization, stack size and headroom, cycle slip statistics, and fragmentation. Each project needs to perform an assessment and determine which resources should be measured.

The Ames Research Center (ARC) standard describes this is as part of a self-test capability that is intentionally introduced into the software, and planned from day one. For example, functional requirements associated with the capability may be included at Preliminary Design Review (PDR). The requirements are implemented incrementally throughout the life cycle as needed to ensure maximum return on investment, with the full feature set being available to the test team during the Verification and Validation (V&V) phase.

The capability presents a challenge at deployment, because a decision must be made to either extract the feature just before deployment or to deploy the software with it. None of the Center standards offer a suggestion here, except to indicate that (1) the project must ensure that inadvertent activation of the feature during operations does not introduce harmful effects, and (2) thorough regression testing ought to be performed if the decision is to extract the feature. See the [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion) design principle for related discussion.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.2.5.3 Measurement of Constrained Resources** - Software shall be designed to provide easy and timely visibility into the use of computing resources during testing and operations.

*Note: Examples of resources to measure are: real time tasks, background tasks, throughput, memory, bus utilization, stack size and headroom, cycle slip statistics, fragmentation, memory leaks, and allocation latency. This makes it possible to validate margins and makes the flight software resource usage testable.*

### 3.2 GSFC

None

### 3.3 JPL

* **4.11.6.3 Measurement of constrained resources Software shall be designed to provide easy and timely visibility into the use of computing resources during testing and operations.**

*Note: Examples of resources to measure are: real time tasks, background tasks, throughput, memory, bus utilization, stack size and headroom, cycle slip statistics, fragmentation, memory leaks, and allocation latency. This makes it possible to validate margins and makes the flight software resource usage testable.*

### 3.4 MSFC

* **4.12.1.4 Software shall be designed to support performance measurement of defined constrained computing resource or function and provide visibility into whether real-time and background tasks are completed.**

*Note: Examples of resources to measure are: real time tasks, background tasks, throughput, memory, bus utilization, stack size and headroom, cycle slip statistics, fragmentation, memory leaks, and allocation latency.*  
  
*Rationale: These key metrics enable determination of operating margins, which can be indicators of potential error and fault conditions. This enables measurement of critical computing resources, thereby maximizing the prospects for safe and reliable operation of the software.*

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
* (SWEREF-674)

  [Manage Reaction Wheels as a Limited Spacecraft Resource (2002)](http://llis.nasa.gov/lesson/1598 "Click to open in new window")

  Lessons Learned Entry: 1598, Date: 2005-06-27, Submitting Organization: JPL, Submitted by: David J. Oberhettinger, Authored by: Allan Lee

  

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion) |

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

The NASA Lesson Learned [439](#_tabs-<p>4</p>)  database contains the following lessons learned related to resource usage measurement:

* **Science Data Downlink Process Must Address Constraints Stemming from Fixed Deep Space Network (DSN) Assets**.  **Lesson Learned 1483:** [557](#_tabs-<p>4</p>) "Given their minimal ability to mitigate DSN resource limitations, flight projects must consider mission design and mission operations improvements that may help to achieve Level 1 requirements, such as the 9 measures effectively employed by the Spitzer project."
* **Manage Reaction Wheels as a Limited Spacecraft Resource (2002)**. **Lesson Learned 1598:** [674](#_tabs-<p>4</p>) "After two and one-half years of operational use, a bearing cage instability trend developed in a bearing in one of three Cassini reaction wheels. JPL responded to the indication of life-limiting wear through steps to manage RWA use, including tracking reaction wheel assembly (RWA) performance, limiting RWA usage, using a software tool to manage reaction wheel biasing events, and providing a reaction wheel drag torque estimator to identify anomalous bearing drag conditions."
