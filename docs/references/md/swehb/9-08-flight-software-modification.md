# 9.08 Flight Software Modification

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695799. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification

9.08 Flight Software Modification

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695799)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695799&showCommentArea=true&showComments=true#addcomment)

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

Include in the software design the capability for commanding modification of the software, and for preventing unwanted modifications.

## 1.1 Rationale

There is often a need for modification of the software or data components after delivery to correct faults, improve performance, maintain hardware functionality or other attributes, or adapt to a changed environment. The capability is needed in-flight via the uplink command function and prior to launch via the umbilical link. Additionally, software that is modifiable during operation should be protected from unintended modifications including those caused by single event effects, and hardware problems.

## 2. Examples and Discussion

This design principle includes the following four aspects:

1. *The capability to command an upload of code (portions or in total), and the data, ought to be limited to a single target memory device under user/ground control and monitoring at a time.*  
   If dual memory units are incorporated in the design, under no circumstances are the prime and redundant memories to be modified concurrently, or before the operational performance of the change is properly assured in a single unit. Care must be taken during the operation to ensure that the code being replaced is not executing at the time of its replacement.
2. *The capability to verify that an uploaded code or data portion is correct before placing it into service.*  
   Typically this is done via direct memory compares of the software version ID and checksum during the upload process and during power on self-test/built in test.
3. *The design should avoid use of self-modifying code.*  
   Self-modifying code is error-prone as well as difficult to read, test, and maintain.
4. *The capability to detect inadvertent modification of a memory segment.*  
   Inadvertent modification of memory can be caused by unintended over-writing of code areas, execution in data areas, unused areas, and other areas not intended for execution. Wherever possible, features of the processor and/or operating system should be used to protect against incorrect memory use (for example, disabling the “write enable” switch such that writing to protected memory areas causes interrupts). Initializing unused memory to illegal instructions that cause interrupts when executed is a software technique that may also be used. Techniques such as partitioning of code and data help minimize the potential for unintended modification. Such techniques provide isolation between functionally independent software elements and may even reduce the verification effort and increase its fidelity.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.2.4.3 Protection from Unintended Software Modification**  
  The flight software architecture should be designed to protect flight software that is intended to be modifiable during flight from unintended modifications.
* **3.7.2.1 Software Modifiability**  
  The flight software design shall provide the capability to upload new software and replace old modules during the mission.
* **3.7.2.5 Protection Against Incorrect Memory Use**  
  Software shall be designed to protect against incorrect use of memory with the following considerations:  
    
       a. Execution in data areas, unused areas, and areas not intended for execution.  
       b. Unintended over-writing of code areas.  
       c. The updating of code/software be limited to a single target memory device under user ground control and monitoring at a time. If dual memory units are incorporated in the design, under no circumstances are the prime and redundant memories to be modified concurrently, or before the operational performance of the change is properly assured in a single unit.

### 3.2 GSFC

None

### 3.3 JPL

* **4.11.4.3 Protection from unintended software modification** - Flight software that is modifiable during flight shall be protected from unintended modifications including those caused by operations errors, single event effects, and hardware problems.  
  *Note: Protection is typically provided by intentionally enabling a write operation before modifying the software; at all other times, write operations are disabled to protect the software from unintended modifications. Unintended modifications can be introduced through configuration management, design, and operations flaws as well as physics.*
* **4.1.7.3 Capability to re-load flight software** - The design shall include the capability to re-load flight software in-flight via the uplink command function, and prior to launch via the umbilical link.

### 3.4 MSFC

* **4.12.1.3 Flight software loads, updates and sequence memory loads shall be capable of verification after upload.**  
  *Rationale: To ensure the integrity of the process, all updates to the program of reprogrammable devices, e.g., flight software loads/updates and sequence memory loads, must be verified by a memory readout or checksum readout. Depending on the application and mission/system consequence, single or multiple readouts may be considered. Program here refers to both loading software and configuration files.*
* **4.12.1.5 Software shall be designed to protect against incorrect use of memory.**  
  *Note: Incorrect use of memory such as execution in data areas, unused areas, and other areas not intended for execution, unintended over-writing of code areas. Wherever possible, features of the processor and/or operating system should be utilized to protect against incorrect memory use. For example, disabling the “write enable” switch such that writing to protected memory areas causes interrupts. Software techniques may also be used such as initializing unused memory to illegal instructions that cause interrupts when executed.*  
    
  *Rationale: Techniques such as partitioning of code and data help minimize the potential for unintended modification. It is a technique for providing isolation between functionally independent software elements and may even reduce the verification effort and increase its fidelity.*
* **4.12.1.7 The software design shall provide the capability to upload software.**  
  *Rationale: Software design should include the functionality and capability to allow modification of the software or data components after delivery to correct faults, improve performance, maintain hardware functionality or other attributes, or adapt to a changed environment.*
* **4.12.1.9 Flight software shall report the software version ID and checksum value as part of the power on self test and/or built in test status.**  
  *Rationale: Validate that the correct software version is loaded into the electronic component*  
    
       a. No self-modifying code to be used in flight software.  
    
  *Rationale: Self-modifying code is error-prone as well as difficult to read, test, and maintain.*
* **4.12.3.9 Flight software shall detect inadvertent memory modification and recover to a known safe state.**  
  *Rationale: Memory modifications may occur due to radiation-induced errors, uplink errors, configuration errors, or other causes, so the computing system must be able to detect the problem and recover to a safe state. For example, there have been cases aboard the International Space Station in which the computing system’s memory check sum function detected incorrect data loads and enabled isolation and safe recovery. Memory correction features may be used to enable such a recovery. As an example, computing systems may implement error detection and correction, software executable and data load authentication, periodic memory scrub and space partitioning to provide protection against inadvertent memory modification.*

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-679)

  [Provide In-flight Capability to Modify Mission Plans During All Operations (2004)](http://llis.nasa.gov/lesson/1480 "Click to open in new window")

  Public Lessons Learned Entry: 1480, Date: 2004-06-21, Submitting Organization: JPL, Submitted by: Mark Boyles/David Oberhettinger

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

Lessons that appear in the NASA LLIS [439](#_tabs-<p>4</p>) or Center Lessons Learned Databases.

* **Provide In-flight Capability to Modify Mission Plans During All Operations (2004)**. **Lesson Learned 1480: [679](#_tabs-<p>4</p>)** "The Mars Exploration Rover (MER) flight system had the ability to update EDL parameters during Approach, and the mission design furnished an operational plan, process, and tools for performing the updates. These capabilities permitted JPL to respond to new data on the Mars atmospheric density by modifying the timing of the MER parachute release, assuring mission success. Maintain an operational capability to code critical parameters in flight software and to update them during the latter stages of encounter/EDL."
