# 9.02 Software Safety and Design Principles

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695792. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695792/9.02+Software+Safety+and+Design+Principles

9.02 Software Safety and Design Principles

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695792/9.02+Software+Safety+and+Design+Principles#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695792)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695792&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Principle and Rational](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Software Design Principles and Software Safety

NASA software safety requirements are documented in NPR 7150.2 [083](#_tabs-<p>2</p>), and elaborated in the Software Assurance and Software Safety Standard, NASA-STD-8739.8A[278](#_tabs-<p>2</p>) .

Design features are a small but important part of an overall software safety implementation. The driving requirement in this area is NPR 7150.2C, requirement [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements). The design principles that support specific provisions of SWE-134 are shown in the table below. A verified application of the NASA software design principles can help form the basis for demonstrating compliance with SWE-134.

| **SWE-134 Sub-requirement** | **Applicable Design Principle** |
| --- | --- |
| a. The software is initialized, at first start and restarts, to a known safe state. | [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode) |
| b. The software safely transitions between all predefined known states. | [9.15 Safe Transitions](/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions) |
| c. Termination performed by the software functions is performed to a known safe state. | [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode)  [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) |
| d. Operator overrides of software functions require at least two independent actions by an operator. | [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) |
| e. The software rejects commands received out of sequence when the execution of those commands out of sequence can cause a hazard. | [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) |
| f. The software detects inadvertent memory modification and recovers to a known safe state. | [9.09 Incorrect Memory Use or Access](/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access) [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) |
| g. The software performs integrity checks on inputs and outputs to/from the software system. | [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) |
| h. The software performs prerequisite checks prior to the execution of safety-critical software commands. | [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) |
| i. No single software event or action is allowed to initiate an identified hazard. | [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) |
| j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. | [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) |
| k. The software provides error handling. | [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) |
| l. The software can place the system into a safe state. | [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) |

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

  

## 2.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)        * [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) * [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) * [9.09 Incorrect Memory Use or Access](/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access) * [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode) * [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) * [9.15 Safe Transitions](/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions) |

## 2.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 2.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |
