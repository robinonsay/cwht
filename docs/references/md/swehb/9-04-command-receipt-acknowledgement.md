# 9.04 Command Receipt Acknowledgement

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695795. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695795/9.04+Command+Receipt+Acknowledgement

9.04 Command Receipt Acknowledgement

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695795/9.04+Command+Receipt+Acknowledgement#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695795)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695795&showCommentArea=true&showComments=true#addcomment)

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

Design software to send a positive acknowledgement of command receipt.

## 1.1 Rationale

Implementation of this rule gives assurance that the physical and virtual links between the sender and receiver are working properly.

# 2. Examples and Discussion

The basis of this principle is the need to have some positive confirmation that a command was received by the target. Historically, this rule has been captured in a software requirement and is sometimes paired with a related requirement to acknowledge that the resulting action has been initiated. An example where this principle is useful is when a command is sent to open a valve but that valve does not open. The problem could be in the command link, or the valve failure itself, or the valve driver, or somewhere else in the system. Positive acknowledgement of command receipt by the target computer facilitates troubleshooting of the problem. Implementations that provide a reason code with a negative acknowledgement further support troubleshooting and autonomous fault protection at little additional cost. Implementation of this principle would also help identify a dropped command in a sequence of commands that might otherwise go undetected. Note that the acknowledgement discussed in this principle is in addition to command acknowledgement implemented by the transmission protocol (e.g., MIL-STD 1553B [668](#_tabs-<p>4</p>), Consultative Committee for Space Data Systems (CCSDS) [667](#_tabs-<p>4</p>). The additional acknowledgement will help detect command errors at the application software level.

In some cases, like the transfer of data from a non-critical component, the designer may make the determination that a command acknowledgement is not necessary (unless there is an approved requirement to do so). But these decisions need to be carefully considered with respect to required troubleshooting capabilities.

The Ames Research Center (ARC) document excerpted in the Inputs section below does not specifically address commands generated internal to the flight software. The notes in the Marshall Space flight Center (MSFC) document (excerpted below) do indicate that the design principle applies to commands generated internally in the flight software. However, the wording in the MSFC document allows the designer some latitude, since it seems excessive to place an item in telemetry for every internally generated command that is placed on every bus for every cycle. The designer may interpret the command acknowledgement to be an acknowledgement to the sender, even if the sender is an on-board computer.

The reference documents do address responding to invalid commands (e.g., nack response) and the discussion is included in the [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) and [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) Design Principles.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.6.2.2 Command Logging**  
    
  The flight software generated data products available for downlink shall include a log of all received, executed and rejected commands that indicates:  
        time of receipt  
        time of execution
* **3.6.2.3 Critical Command Locking**  
    
  Critical commands that may adversely affect system operation or safety shall be controlled so that they cannot be inadvertently executed without operator acknowledgement.

* **3.7.2.4.1 Command Validation and Acknowledgement**  
    
        a) Flight software shall be designed to verify uplinked commands, data, or loads.  
        b) Flight software shall ignore, and log incorrectly formatted commands, data, or loads and provide notification that they were incorrectly formatted.  
        c) Flight software shall be designed to send acknowledgement of command receipt to the source with indication of acceptance or rejection of command. For rejected commands, the acknowledgement message shall include a reason for rejection in the transmitted message.   
    
  *Note: For example, flight computer designs have included Error Detection And Correction (EDAC) logic on EEPROMs, and the load process has been designed to detect and respond to failure if the EDAC detects an uncorrectable bit error. Software designs have included check sum logic and periodic verification of memory to detect command, data, or load, and memory faults.*  
    
  *Note: For example, a command handler should check whether a received command is appropriate for the current system mode, and a software module should check whether a command is appropriate for its local state.*  
    
  *Note: For example, flight computer designs have included Error Detection And Correction (EDAC) logic on EEPROMs, and the load process has been designed to detect and respond to failure if the EDAC detects an uncorrectable bit error. Software designs have included check sum logic and periodic verification of memory to detect command, data, or load, and memory faults. For example, a command handler should check whether a received command is appropriate for the current system mode, and a software module should check whether a command is appropriate for its local state.*

### 3.2 GSFC

None

### 3.3 JPL

None

### 3.4 MSFC

* **4.12.1.8 Software shall be designed to send acknowledgement of command receipt.**   
    
  *Note: Critical command information needs to be captured in both the downlink in real-time and on any kind of onboard recording device, including internally generated commands.*   
    
  *Rationale: To verify successful command transmission and to evaluate command disposition.*

# 4. Resources

### 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-667)

  [Consultative Committee for Space Data Systems](https://public.ccsds.org/default.aspx "Click to open in new window")

  Multi-national forum for the development of communications and data systems standards for spaceflight
* (SWEREF-668)

  [MIL-STD-1553 - Mechanical, electrical, and functional characteristics of a serial data bus](http://www.everyspec.com/MIL-STD/MIL-STD-1500-1599/download.php?spec=MIL-STD-1553B.002938.pdf "Click to open in new window")

  MIL-STD-1553B, published in 1978,

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) * [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) |

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

No lessons learned [439](#_tabs-<p>4</p>) have currently been identified for this principle.
