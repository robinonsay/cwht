# 9.09 Incorrect Memory Use or Access

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695800. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access

9.09 Incorrect Memory Use or Access

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695800)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695800&showCommentArea=true&showComments=true#addcomment)

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

Design software to protect against incorrect use of memory.

## 1.1 Rationale

Incorrect use of memory can lead to catastrophic failure.

## 2. Examples and Discussion

Memory access errors generically fall into two types: inappropriate reads and writes.

Spacecraft have several types of memory, with different characteristics, residing in different devices. All spacecraft will have memory on the processor board, and a form of non-volatile memory for boot code. There are often other devices that provide storage for extra copies of the flight software, system data, telemetry, and science data. While there are many types of memory technology in use, they can roughly be grouped into three categories:

* Programmable Read-Only Memory that cannot be modified (e.g., PROM);
* Persistent (non-volatile) memory that can be modified (e.g., EEPROM), and
* Volatile memory that can be modified freely, but which does not guarantee content on reset or power cycle (e.g., DRAM , SDRAM , etc.).

Which technology is chosen depends on the persistence requirements of the data that needs to be stored.

Processor memory is typically organized with areas reserved for code storage, compiled-in data storage, stack space, and dynamic (heap) storage. Depending on processor architecture, these areas may be known by different terms, and be organized in physical memory in different ways, but regardless of architecture, each area in memory has a specific purpose, and the boundaries between each must be strictly observed.

The specific techniques employed to prevent inappropriate memory use vary according to the underlying technology, frequency of access, criticality of the contents, and other application-specific considerations. The choice of techniques should balance the need for reliability against the cost, complexity, and risk of proposed solutions. For example, data replication with a simple checksum may be sufficient to guarantee an acceptable level of data integrity. In other situations, data replication might need to be combined with error detection and correction (either hardware or software-based), and possibly write protection mechanisms to achieve the desired reliability. See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality).

Additional techniques that might be considered, either alone or in conjunction with other techniques include:

* Read-after-write verification,
* Operating system or hardware-based memory partitioning,
* The ability to roll back a failed change operation,
* Use of multiple memory technologies to prevent common-mode failures,
* Software checks on computed addresses or pointers to ensure they refer to valid memory locations,
* Use of memory write protection,
* Initializing unused memory to illegal instructions that cause interrupts when executed, and
* Initializing unused memory to values other than zero.

Memory contents in both code and data segments may become corrupted due the effects of the space environment. This as a special case of incorrect write access. The techniques employed to detect and correct memory corruption include many of the techniques described above as well as systematic processes such as:

* Hardware or software error detection and correction (EDAC) and memory scrubbing
* Use of check-sums on important memory segments
* Read-after-write to ensure that critical data have been correctly transferred to memory
* Tracking of bad bits and/or memory blocks, with associated memory management to prevent us of physical areas of memory with known problems.

Whatever techniques are used, when safeguard measures are invoked to prevent an undesirable action, or correct a detected fault, reporting the event in telemetry alerts ground operators to the situation and allows them to take appropriate action.

See also the [9.08 Flight Software Modification](/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification) and [9.16 Thread Safety](/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety) design principles for related discussion.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.2.5 Protection Against Incorrect Memory Use** - Software shall be designed to protect against incorrect use of memory with the following considerations:  
    
       a. Execution in data areas, unused areas, and areas not intended for execution.  
       b. Unintended over-writing of code areas.  
       c. The updating of code/software be limited to a single target memory device under user ground control and monitoring at a time. If dual memory units are incorporated in the design, under no circumstances are the prime and redundant memories to be modified concurrently, or before the operational performance of the change is properly assured in a single unit.
* **3.7.2.4.3 Protection from Unintended Software Modification** -The flight software architecture should be designed to protect flight software that is intended to be modifiable during flight from unintended modifications.
* **3.7.2.4.1 Command Validation and Acknowledgement**  
       a. Flight software shall be designed to verify uplinked commands, data, or loads.  
       b. Flight software shall ignore, and log incorrectly formatted commands, data, or loads and provide notification that they were incorrectly formatted.  
       c. Flight software shall be designed to send acknowledgement of command receipt to the source with indication of acceptance or rejection of command. For rejected commands, the acknowledgement message shall include a reason for rejection in the transmitted message.  
    
  *Note: For example, flight computer designs have included Error Detection And Correction (EDAC) logic on EEPROMs, and the load process has been designed to detect and respond to failure if the EDAC detects an uncorrectable bit error. Software designs have included check sum logic and periodic verification of memory to detect command, data, or load, and memory faults. For example, a command handler should check whether a received command is appropriate for the current system mode, and a software module should check whether a command is appropriate for its local state.*

### 3.2 GSFC

None

### 3.3 JPL

* **4.11.4.2 Response to incorrect commands, loads, data, or memory**  
  a. Flight software shall be designed to detect and respond safely to corrupted commands, data, or loads, and memory faults allocated to the software, such as stuck bits or single event effects (SEE).  
    
  *Note:**For example, flight computer designs have included Error Detection And Correction (EDAC) logic on EEPROMs, and the load process has been designed to detect and respond to failure if the EDAC detects an uncorrectable bit error. Software designs have included check sum logic and periodic verification of memory to detect command, data, or load, and memory faults.*
* **4.11.4.3 Protection from unintended software modification** - Flight software that is modifiable during flight shall be protected from unintended modifications including those caused by operations errors, single event effects, and hardware problems.  
    
  *Note: Protection is typically provided by intentionally enabling a write operation before modifying the software; at all other times, write operations are disabled to protect the software from unintended modifications. Unintended modifications can be introduced through configuration management, design, and operations flaws as well as physics.*
* **4.11.4.11 Protection against incorrect memory use** - Software shall be designed to protect against incorrect use of memory:  
  a. Execution in data areas, unused areas, and other areas not intended for execution caused by branching into non-code areas.  
  b. Using code as data.  
  c. Unintended, harmful over-writing of code areas.  
    
  *Note: Wherever possible, features of the processor and/or operating system should be utilized to protect against incorrect memory use. For example, disabling the “write enable” switch such that writing to protected memory areas causes interrupts. Software techniques may also be used such as initializing unused memory to illegal instructions that cause interrupts when executed.*

### 3.4 MSFC

* **4.12.1.3 Flight software loads, updates and sequence memory loads shall be capable of verification after upload.**  
  *Rationale: To ensure the integrity of the process, all updates to the program of reprogrammable devices, e.g., flight software loads/updates and sequence memory loads, must be verified by a memory readout or checksum readout. Depending on the application and mission/system consequence, single or multiple readouts may be considered. Program here refers to both loading software and configuration files.*
* **4.12.1.5 Software shall be designed to protect against incorrect use of memory.**  
  *Note: Incorrect use of memory such as execution in data areas, unused areas, and other areas not intended for execution, unintended over-writing of code areas. Wherever possible, features of the processor and/or operating system should be utilized to protect against incorrect memory use. For example, disabling the “write enable” switch such that writing to protected memory areas causes interrupts. Software techniques may also be used such as initializing unused memory to illegal instructions that cause interrupts when executed.*  
    
  *Rationale: Techniques such as partitioning of code and data help minimize the potential for unintended modification. It is a technique for providing isolation between functionally independent software elements and may even reduce the verification effort and increase its fidelity.*
* **4.12.3.9 Flight software shall detect inadvertent memory modification and recover to a known safe state.**  
  *Rationale: Memory modifications may occur due to radiation-induced errors, uplink errors, configuration errors, or other causes, so the computing system must be able to detect the problem and recover to a safe state. For example, there have been cases aboard the International Space Station in which the computing system’s memory check sum function detected incorrect data loads and enabled isolation and safe recovery. Memory correction features may be used to enable such a recovery. As an example, computing systems may implement error detection and correction, software executable and data load authentication, periodic memory scrub and space partitioning to provide protection against inadvertent memory modification.*

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
* (SWEREF-569)

  [Mars Global Surveyor (MGS) Spacecraft Loss of Contact](https://llis.nasa.gov/lesson/1805 "Click to open in new window")

  Public Lessons Learned Entry:1805. In NASA Engineering Network. Retrieved March 31, 2015 from http://llis.nasa.gov/lesson/1805.
* (SWEREF-678)

  [The NEAR Rendezvous Burn Anomaly of December 1998](https://spacese.spacegrant.org/Failure%20Reports/NEAR_Rendezvous_BurnMIB.pdf "Click to open in new window")

  Final Report of the NEAR (Near Earth Asteroid Rendezvous Anomaly Review Board, November 1999

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [9.08 Flight Software Modification](/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification) * [9.16 Thread Safety](/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety) |

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

The NASA Lesson Learned [439](#_tabs-<p>4</p>) database contains the following lessons learned related to incorrect memory use or access:

* **MER Spirit Flash Memory Anomaly (2004)**. **Lesson Learned 1483:** [557](#_tabs-<p>4</p>)"Shortly after the commencement of science activities on Mars, an MER rover lost the ability to execute any task that requested memory from the flight computer. The cause was incorrect configuration parameters in two operating system software modules that control the storage of files in system memory and flash memory. Seven recommendations cover enforcing design guidelines for COTS software, verifying assumptions about software behavior, maintaining a list of lower priority action items, testing flight software internal functions, creating a comprehensive suite of tests and automated analysis tools, providing downlinked data on system resources, and avoiding the problematic file system and complex directory structure."
* **Mars Global Surveyor (MGS) Mars Global Surveyor (MGS) Spacecraft Loss of Contact**. **Lesson Learned 1805: [569](#_tabs-<p>4</p>)**  
  Contact was lost with the Mars Global Surveyor (MGS) spacecraft in November 2006 during its 4th extended mission. A routine memory load command sent to an incorrect address 5 months earlier corrupted positioning parameters, and their subsequent activation placed MGS in an attitude that fatally overheated a battery and depleted spacecraft power. The report by the independent MGS Operations Review Board listed 10 key recommendations to strengthen operational procedures and processes, correct spacecraft design weaknesses, and assure that economies implemented late in the course of long-lived missions do not impose excessive risks.

In addition, a report prepared by the Near Earth Asteroid Rendezvous (NEAR) Anomaly Review Board contains information related to incorrect memory use or access. The report is entitled "The NEAR Rendezvous Burn Anomaly of December 1998" [678](#_tabs-<p>4</p>)
