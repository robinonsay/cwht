# 9.05 Data Interface Integrity

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695796. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity

9.05 Data Interface Integrity

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695796)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695796&showCommentArea=true&showComments=true#addcomment)

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

Design software to verify the integrity of all inputs and outputs in the control system

## 1.1 Rationale

Systems must use accurate data to maintain state information and produce correct output messages.

## 2. Examples and Discussion

For the purpose of this discussion, the term data integrity will be used to describe messages that are correctly formatted, not corrupted in transmission, and complete. A robust control system must test the integrity of input data and incorporate features to allow testing the integrity of its output data.

Methods that have been used to test the integrity of input data include validating the expected length of the message, verifying error detection codes incorporated in the data messages (e.g., parity bits, checksums, cyclical redundancy checks (CRC)), and ensuring the correct value of fixed bits within the message. In some cases, measurements within a message are validated to be within the operational range of the hardware device (e.g., sensor). These validity checks are used to ensure that the hardware was read properly and are performed before typical limit monitoring.

Interface integrity checks are especially important where safety is a concern. Safety-critical commands whose inadvertent execution could pose a hazard to personnel or equipment are required to be implemented as two-step procedures (NPR 7150.2, [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) (d) & (i)). Integrity checking must ensure that both parts of a two-step command are present and properly formed, as well as implementing associated constraints such as timeouts, parameter value checks, and system mode requirements.

The same methods that apply to testing the integrity of input data are used to test the integrity of output data. However, the tests are performed by the receiving device to ensure the integrity of the system (e.g., flight computer) and the transmission. The system must incorporate features (e.g., appending the error codes to output commands) to allow the receiver to perform output data validity checks.

A special case to consider is an architecture with redundant computers voting outputs and ensuring consistent inputs. Consistent inputs can be validated to be bit-for-bit identical or within an expected tolerance. Outputs are typically voted to ensure that identical commands are transmitted on redundant interfaces.

The systems fault detection and response requirements ought to specify the appropriate response to receipt of input data with integrity errors by the control system and receipt of output data with integrity errors at the end item devices. Typical responses include discarding a predefined number of incorrect messages, using a previous valid message, and substituting messages from redundant devices. Logging and reporting errors aids in troubleshooting faults.

Related design principles include [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) and [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response).

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

None

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

* **4.12.3.5 Software shall perform integrity checks on input and output across the computing system boundary.**  
    
  *Rationale: The software design should ensure that only valid inputs and outputs are incorporated into the control system state. An integrity check ensures the message is well-formed and not corrupted. Potential faults and the action taken must be defined and determined so that actions taken upon error detection do not set off a chain reaction leading to more serious fault conditions, e.g., issuance of questionable commands to actuators as a result of a fault condition that exacerbates the problem.*

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)        * [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) * [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) |

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
