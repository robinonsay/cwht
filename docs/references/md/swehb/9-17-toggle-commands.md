# 9.17 Toggle Commands

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695808. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695808/9.17+Toggle+Commands

9.17 Toggle Commands

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695808/9.17+Toggle+Commands#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695808)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695808&showCommentArea=true&showComments=true#addcomment)

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

Design both internal and external commanding to place the system into an explicitly specified state.

## 1.1 Rationale

Making assumptions about the system state can lead to malfunctions.

## 2. Examples and Discussion

This principle is often formulated in terms of a prohibition against “toggle” commands pertaining to the spacecraft. Both the JPL and Marshall Space Flight Center (MSFC) standards are written in that manner. The underlying problem is maintaining knowledge of the spacecraft’s state. If the command to turn a component on or off, for example, is simply defined as a command to switch state from the current state to the opposite state, ground controllers must keep track of how many times the command has been used to ensure that the correct state is commanded. Use of toggle commands also complicates the development of command sequences that may be invoked in parallel. This may occur as either part of planned commanding, as with the use of so-called “background” sequences and their supporting utility sequences, or asynchronously with planned commanding, as in the case of a sequence that is invoked to implement a recovery procedure. In these cases a race condition is created, with the behavior of the command sequences being dependent on relative timing of execution. Command sequences that execute in parallel are still vulnerable to interference, but prohibiting toggle commands eliminates a particularly difficult source of commanding bugs.

Both JPL and MSFC standards allow the use of toggle commands if information exists to determine the current state of the spacecraft. The Ames Research Center (ARC) formulation of this principle does not grant this allowance, and requires the desired state to be explicitly specified as part of the command. The ARC formulation was preferred in the development of these design principles.

However, none of the Center standards explicitly take into account the practice of generating commands internal to flight software. The design principle as presented here extends the prohibition of toggle commands to internally generated commands.

As used here, the term “command” should be interpreted to include any function or mechanism used to alter the state of any spacecraft component.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.6.2.1 Explicit Commanding of States** - Commands that are intended to place spacecraft in a specific known state, shall explicitly specify the target state.  
    
  *Note: This requirement precludes the use of toggle commands, which have a target state implicitly defined by the current state.*  
    
  *Note: Elements to consider when establishing state include inertial, temporal, device capability or configuration, file allocation tables, and boot code in RAM.*

### 3.2 GSFC

None

### 3.3 JPL

* **4.4.4.1 Use of toggle and step commands** - Toggle commands and step commands shall be permitted only if absolute position commands and telemetry also exist for the same function(s).

*Rationale: To avoid needing to predict the s/c state that will exist at the time of command execution.*

### 3.4 MSFC

* **4.12.1.10 Toggle commands and step commands shall be permitted if the capability exists to determine absolute position for the commanded function.**

*Rationale: To avoid needing to predict the vehicle state that will exist at the time of command execution.*

# 4. Resources

### 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-673)

  [Stepping Commands Cause Positioning Problems (1970/76)](http://llis.nasa.gov/lesson/405 "Click to open in new window")

  Public Lessons Learned Entry: 0405, Date: 1996-04-26, Submitting Organization: JPL, Submitted by: J.A. Roberts

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
|  |

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

The NASA Lesson Learned [439](#_tabs-<p>4</p>)  database contains the following lessons learned related to toggle commands:

* **Stepping Commands Cause Positioning Problems (1970/76)**.  **Lesson Learned 0405:** [673](#_tabs-<p>4</p>) "Unlike explicit commands, stepping or incremental commands, however, simply cause the device to move by the commanded increment from its current position to the new position. If the current position is incorrect, the next position and all subsequent positions will be incorrect. The use of explicit commands is recommended whenever no significant operational advantage exists using incremental commands. Should an incremental command capability be desired for other reasons, the system design should consider also implementing the explicit command capability to ensure fault tolerance."
