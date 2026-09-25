# 9.12 Resource Margins

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695803. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins

9.12 Resource Margins

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695803)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695803&showCommentArea=true&showComments=true#addcomment)

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

Establish and maintain quantitative margins for all critical resources, allowing for maturation of usage estimates through the life cycle. 

## 1.1 Rationale

Computing resources tend to become problematic late in the development process. Design margins help identify problems earlier, and provide a means of managing them.

## 2. Examples and Discussion

Resource margins are commonly used throughout the aerospace industry. Commercial organizations usually have established standards, which may be different than those at NASA Centers. Due to the proprietary nature of these standards, only NASA standards will be discussed here.

The Goddard Space Flight Center (GSFC) “Golden Rules” [672](#_tabs-<p>4</p>)  establish detailed margins for a variety of resources. In addition to setting margins at different stages in the life cycle, their approach includes the method used to calculate the margin (i.e., estimation, analysis, measurement, or combination). This approach has the advantage of providing explicit guidance on the level of confidence to be placed in the measurement. For example, a project with a high degree of heritage may qualify for a Critical Design Review (CDR)-level margin at the Systems Requirements Review (SRR) if it can be shown that the anticipated changes required will not significantly affect the estimated resource usage. Conversely, it may be appropriate to apply SRR-level margins at CDR for a project with little or no heritage and many uncertainties remaining.

**GSFC Table 3.07-1 FSW Margins**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mission Phase** | **FSW SRR** | **FSW PDR** | **FSW CDR** | **Ship/Flight** |
| Method | Estimate | Analysis | Analysis/Measured | Measured |
| Average CPU Usage | 50% | 50% | 40% | 30% |
| CPU Deadlines | 50% | 50% | 40% | 30% |
| PROM | 50% | 30% | 20% | 0% |
| EEPROM | 50% | 50% | 40% | 30% |
| RAM | 50% | 50% | 40% | 30% |
| PCI Bus | 75% | 70% | 60% | 50% |
| 1553 Bus | 30% | 25% | 20% | 10% |
| Spacewire (1355) | TBD | TBD | TBD | TBD |
| UART/Serial I/F | 50% | 50% | 40% | 30% |

While the GSFC approach provides very detailed guidance, there may be project-specific resources that do not appear on the list. If that is the case, the project must establish its own margins. The existing margins provide guidelines for items that were not specified. Other Centers (Ames Research Center (ARC) and JPL) have taken an approach that relies on projects identifying and establishing resource margins within a general set of guidelines. Examples from JPL, and ARC are shown below.

**JPL Table 6.3.5-1**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Mission Phase** | **CPU Selection** | **PDR** | **CDR** | TRR | **Launch** |
| Margin | 75% | 60% | - | - | 20% |

**ARC Section 3.1.6.2**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Mission Phase** | **CPU Selection** | **PDR** | **CDR** | **TRR** | **Launch** |
| Margin | 75% | 60% | 50% | - | 20% |

Both Centers adopt a more aggressive stance in terms of required margins early in the life cycle, while being more lenient at launch. In the JPL case, the high margin requirements in the early phases is driven by experience with unprecedented systems that frequently experience substantial growth in required functionality during product development. Both Centers have chosen to start margin management at Central Processing Unit (CPU) selection rather than SRR. With this approach the required compute margins may drive selection of a processor. At JPL this was an intentional. The flight software resource margins at JPL fit into a larger process of identifying and managing critical resources across the project. These are usually documented at project start by the project system engineer, who continues to manage resources throughout the life cycle.

Marshall Space Flight Center (MSFC) has adopted a margin policy that is midway between the GSFC standard and the JPL/ARC standard. Marshall’s margins provide more detail than do JPL or ARC, but less than GSFC. Their margins also commence later in the life cycle than the other Centers. Like GSFC, the MSFC standard sets different margin levels for different resource types. This is an important feature, as requirements growth tends to impact different resources unevenly.

**MSFC Section 4.12.5.2**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Mission Phase** | **CPU Selection** | **PDR** | **CDR** | **TRR** | **Launch** |
| Random Access Memory | - | - | 50% | 40% | 30% |
| EEPROM Memory | - | - | 50% | 20% | 10% |
| CPU Utilization | - | - | - | 35% | 25% |
| Data Bus Throughput | - | - | 35% | 25% | 20% |

Margins are set based on past experience. But that experience may be heavily influenced by the types of projects typically undertaken by an organization. The typical method used to calculate resource margins is via the equation:

% margin = (available resource-estimated usage of resource)/available resource

However, this may not always be the case. When looking at different sources for margin guidance it is critical that the formula used be clearly understood. Likewise, it is critical to understand what is meant by a particular resource, and how an organization typically uses that resource. For example, the “Data Bus Throughput” entry in the MSFC table may reflect traffic on the CPU backplane only, the bus connecting the CPU to a suite of instruments, or both. How the margins are set will depend on which case is intended.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

Included in Examples section.

### 3.2 GSFC

Included in Examples section.

### 3.3 JPL

Included in Examples section.

### 3.4 MSFC

Included in Examples section.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-672)

  [Rules for the Design, Development, Verification, and Operation of Flight Systems](https://nen.nasa.gov/documents/14202/1030520/GSFC+Gold+Rules+/de80ff63-aa7e-43a3-ab39-b2deafa37db1 "Click to open in new window")

  GSFC-STD-1000F, Approved: 02-08-2013 - With Administrative Changes , Expiration Date: 02-08-2018, Superseding GSFC-STD-1000E

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

No Lessons Learned [439](#_tabs-<p>4</p>) have currently been identified for this principle.
