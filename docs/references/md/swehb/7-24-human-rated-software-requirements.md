# 7.24 - Human Rated Software Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 167805194. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements

7.24 - Human Rated Software Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=167805194)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=167805194&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Requirements](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Resources](#tabs-4)

# 1. Introduction

What requirements do you need to follow when you are developing or acquiring human-rated software?  The answer is NPR 7150.2 Class A requirements and some of the NASA-STD-8719.29 software requirements. NASA-STD-8719.29 [458](#_tabs-<p>4</p>)  defines technical requirements necessary to produce human-rated space systems that protect the safety of the crew and passengers on NASA space missions. This NASA technical standard provides uniform engineering and technical requirements for processes, procedures, practices, and methods that have been endorsed as standards for NASA programs and projects, including requirements for the selection, application, and design criteria of an item. For software, NPR 7150.2, NASA-STD-8739.8,  and this NASA technical standard, NASA-STD-8719.29, together with the Human Rating Certification Process and associated requirements addressed in NPR 8705.2C [024](#_tabs-<p>4</p>), provides a complete picture of human-rating of applicable space flight systems.

This standard establishes technical requirements necessary to produce human-rated space systems that protect the safety of the crew and passengers on NASA space missions. A human-rated system accommodates human needs, effectively utilizes human capabilities, controls hazards with sufficient certainty to be considered safe for human operations, and provides, to the maximum extent practical, the capability to safely recover the crew from hazardous situations.

The standard is applicable to crewed space systems developed or operated by NASA and to crewed space systems used to conduct NASA human spaceflight missions as specified by NPR 8705.2. This standard is applicable to NASA Headquarters and NASA Centers, including Component Facilities and Technical and Service Support Centers.

These requirements form a high-level compliance framework for human-rating but are not all-inclusive for every specific space system. Additional requirements or unique considerations may be levied at other system or sub-system levels by applicable Technical Authorities in order to ensure the system fully meets safety considerations for human missions into space. Full compliance for human rating occurs when all levied requirements or considerations at each level have been appropriately addressed.

## 1.1 Human Rated Systems

A human-rated system accommodates human needs, effectively utilizes human capabilities, controls hazards with sufficient certainty to be considered safe for human operations, and provides, to the maximum extent practical, the capability to safely recover the crew from hazardous situations within the framework of the chosen risk posture.

See also [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) for additional guidance on Safety-Critical Software.

## 1.2 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Requirements

The requirements (shall statements) in NASA-STD-8719.29 are listed in the table below. If the requirement is related to Software, it has been given a SWE number and the SHALL statement is included. For those requirements that are not Software-related, the SHALL statement is stated and the rationale describes why the requirement is not software-related.

14 requirements in NASA-STD-8719.29 are specifically related to Human Rated Software.

| SWE Title | Requirement | Rationale |
| --- | --- | --- |
|  | 4.2.1 The space system shall provide a safe environment for crew habitation. | Environmental |
|  | 4.2.2 The space system shall meet probabilistic safety criteria derived from the Agency-level safety goals and safety thresholds with a specified degree of certainty. | Environmental |
| [HR-31 - Single Failure Tolerance](/spaces/SWEHBVD/pages/167805124/HR-31+-+Single+Failure+Tolerance) | 4.3.1 The space system shall provide at least single failure tolerance to catastrophic events, with specific levels of failure tolerance and implementation (similar or dissimilar redundancy) derived via an integration of the design and safety analysis (required by NPR 8705.2). | Software Related |
|  | 4.3.2 The space system shall provide the failure tolerance capability without the use of emergency equipment and systems. | Excludes emergency equipment and systems. |
| [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action) | 4.3.3 The space system shall be designed to tolerate inadvertent operator action (minimum of one inadvertent action), as verified by a human error analysis, without causing a catastrophic event. | Software Related |
| [HR-34 - Operator Action With Single System Failure](/spaces/SWEHBVD/pages/171508198/HR-34+-+Operator+Action+With+Single+System+Failure) | 4.3.4 The space system shall tolerate inadvertent operator action, as described in Section 4.3.3, in the presence of any single system failure. | Software Related |
| [HR-35 - Mitigate Hazardous Behavior Of Critical Software](/spaces/SWEHBVD/pages/167805151/HR-35+-+Mitigate+Hazardous+Behavior+Of+Critical+Software) | 4.3.5 The space system shall provide the capability to mitigate the hazardous behavior of critical software where the hazardous behavior would result in a catastrophic event. | Software Related |
| [HR-36 - Detect And Annunciate Faults](/spaces/SWEHBVD/pages/171508203/HR-36+-+Detect+And+Annunciate+Faults) | 4.3.6 The space system shall provide the capability to detect and annunciate faults that affect critical systems, subsystems, or crew health. | Software Related |
| [HR-37 - Fault Recovery](/spaces/SWEHBVD/pages/171508207/HR-37+-+Fault+Recovery) | 4.3.7 The space system shall provide the capability to isolate and recover from faults identified during system development or mission operations that would result in a catastrophic event. | Software Related |
| [HR-38 - Data Analysis](/spaces/SWEHBVD/pages/171508210/HR-38+-+Data+Analysis) | 4.3.8 The space system shall provide the capability to utilize health and status data (including system performance data) of critical systems and subsystems to facilitate anomaly resolution during and after the mission. | Software Related |
| [HR-39 - Autonomous Operation](/spaces/SWEHBVD/pages/171508213/HR-39+-+Autonomous+Operation) | 4.3.9 The crewed space system shall provide the capability for autonomous operation of system and subsystem functions which, if lost, would result in a catastrophic event. | Software Related |
|  | 4.3.10 The space system shall provide the capability for the crew to readily access equipment involved in the response to emergency situations and the capability to gain access to equipment needed for follow-up and recovery operations. | Related to non-software equipment. |
| [HR-41 - Crew Operations](/spaces/SWEHBVD/pages/171508215/HR-41+-+Crew+Operations) | 4.4.1 The crewed space system shall provide the capability for the crew to monitor, operate, and control the crewed space system and subsystems, where:  1. 1. The capability is necessary to execute the mission; or    2. The capability would prevent a catastrophic event; or    3. The capability would prevent an abort. | Software Related |
| [HR-42 - Crew Override](/spaces/SWEHBVD/pages/171508217/HR-42+-+Crew+Override) | 4.4.2 The crewed space system shall provide the capability for the crew to manually override higher level software control and automation (such as automated abort initiation, configuration change, and mode change) when the transition to manual control of the system will not cause a catastrophic event. | Software Related |
| [HR-43 - Crew Control](/spaces/SWEHBVD/pages/171508219/HR-43+-+Crew+Control) | 4.4.3 The space system shall provide the capability for humans to remotely monitor, operate, and control the crewed system elements and subsystems, where:  1. 1. The remote capability is necessary to execute the mission; or    2. The remote capability would prevent a catastrophic event; or    3. The remote capability would prevent an abort. | Software Related |
| [HR-51 - Crew Flight Control](/spaces/SWEHBVD/pages/167805155/HR-51+-+Crew+Flight+Control) | 4.5.1 The crewed space system shall provide the capability for the crew to manually control the flight path and attitude of their spacecraft, with the following exception: during the atmospheric portion of Earth ascent when structural and thermal margins have been determined to negate the benefits of manual control. | Software Related |
|  | 4.5.2 The crewed spacecraft shall exhibit Level 1 handling qualities (Handling Qualities Rating (HQR) 1, 2, and 3), as defined by the Cooper-Harper Rating Scale, during manual control of the spacecraft's flight path and attitude for crew manual control events when the vehicle has not had failures which result in degraded flight control. | Manual control events |
|  | 4.6.1 The space system shall provide the capability for the crew to monitor, operate, and control an uncrewed spacecraft during proximity operations, where: a. The capability is necessary to execute the mission; or b. The capability would prevent a catastrophic event; or c. The capability would prevent an abort. | Monitor, operate, and control an uncrewed |
|  | 4.6.2 The crewed space system shall provide the capability for direct voice communication, ship-to-ship without relay through another system, between crewed spacecraft (two or more) during proximity operations. | Voice communication |
|  | 4.7.1.1 The space system shall provide the capability for unassisted crew emergency egress to a safe haven during Earth prelaunch activities. | Crew Egress |
|  | 4.7.1.2 The space system shall provide abort capability from the launch pad until Earth orbit insertion to protect for the following ascent failure scenarios: a. Complete loss of ascent thrust/propulsion. b. Loss of attitude or flight path control. | Abort capability |
|  | 4.7.1.3 The crewed space system shall monitor the Earth ascent launch vehicle performance and automatically initiate an abort when an impending catastrophic failure is detected. | Abort capability |
|  | 4.7.1.4.1 The space system shall provide the capability for the crew to initiate the Earth ascent abort sequence. | Abort capability |
| [HR-7142 - Ground Initiate Ascent Abort Sequence](/spaces/SWEHBVD/pages/171508229/HR-7142+-+Ground+Initiate+Ascent+Abort+Sequence) | 4.7.1.4.2 The space system shall provide the capability for the ground control to initiate the Earth ascent abort sequence. | Software Related |
| [HR-715 - Interface With Range Safety Destruct System](/spaces/SWEHBVD/pages/171508231/HR-715+-+Interface+With+Range+Safety+Destruct+System) | 4.7.1.5 If a range safety destruct system is incorporated into the design, the space system shall automatically initiate the Earth ascent abort sequence when range safety destruct commands are received onboard, with an adequate time delay prior to destruction of the launch vehicle to allow a successful abort. | Software Related |
|  | 4.7.2 The crewed space system shall provide the capability to autonomously abort the mission from Earth orbit by targeting and performing a deorbit to a safe landing on Earth. | Abort capability |
|  | 4.7.3.1 The crewed space system shall provide the capability to autonomously abort the mission during lunar transit and from lunar orbit by executing a safe return to Earth. | Abort capability |
|  | 4.7.4.1 The crewed space system shall provide the capability to autonomously abort the lunar descent and execute all operations required for a safe return to Earth. | Abort capability |
|  | 4.7.5.1 The space system shall provide the capability for the crew on the lunar surface to monitor the descent and landing trajectory of an uncrewed spacecraft and send commands necessary to prevent a catastrophic event. | Descent and landing |
|  | 4.7.6.1 The crewed space system shall provide the capability for unassisted crew emergency egress after Earth landing. | Emergency egress |
|  | 4.7.7.1 The crewed space system shall maintain a safe and habitable environment for the crew inside the spacecraft after Earth landing until the arrival of the landing recovery team or rescue forces. | Safe and habitable environment |
|  | 4.7.7.2 The crewed space system shall maintain a safe and habitable environment for the crew inside the spacecraft after Earth landing until the arrival of the landing recovery team or rescue forces. | Safe and habitable environment |
|  | 4.7.7.3 The space system shall provide recovery forces with the location of the spacecraft after return to Earth. | Recovery |

# 3. Guidance

Guidance from the NASA-STD-8719.29 that applies to SWEs is included in the appropriate SWE page. Another guidance from NASA-STD-8719.29 that applies to a requirement that is not a SWE is left in NASA-STD-8719.29.

If requirements are reclassified as SWEs, a SWE page will be built and added to the SWEHB.

## 3.1 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [HR-31 - Single Failure Tolerance](/spaces/SWEHBVD/pages/167805124/HR-31+-+Single+Failure+Tolerance) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action) * [HR-34 - Operator Action With Single System Failure](/spaces/SWEHBVD/pages/171508198/HR-34+-+Operator+Action+With+Single+System+Failure) * [HR-35 - Mitigate Hazardous Behavior Of Critical Software](/spaces/SWEHBVD/pages/167805151/HR-35+-+Mitigate+Hazardous+Behavior+Of+Critical+Software) * [HR-36 - Detect And Annunciate Faults](/spaces/SWEHBVD/pages/171508203/HR-36+-+Detect+And+Annunciate+Faults) * [HR-37 - Fault Recovery](/spaces/SWEHBVD/pages/171508207/HR-37+-+Fault+Recovery) * [HR-38 - Data Analysis](/spaces/SWEHBVD/pages/171508210/HR-38+-+Data+Analysis) * [HR-39 - Autonomous Operation](/spaces/SWEHBVD/pages/171508213/HR-39+-+Autonomous+Operation) * [HR-41 - Crew Operations](/spaces/SWEHBVD/pages/171508215/HR-41+-+Crew+Operations) * [HR-42 - Crew Override](/spaces/SWEHBVD/pages/171508217/HR-42+-+Crew+Override) * [HR-43 - Crew Control](/spaces/SWEHBVD/pages/171508219/HR-43+-+Crew+Control) * [HR-51 - Crew Flight Control](/spaces/SWEHBVD/pages/167805155/HR-51+-+Crew+Flight+Control) * [HR-7142 - Ground Initiate Ascent Abort Sequence](/spaces/SWEHBVD/pages/171508229/HR-7142+-+Ground+Initiate+Ascent+Abort+Sequence) * [HR-715 - Interface With Range Safety Destruct System](/spaces/SWEHBVD/pages/171508231/HR-715+-+Interface+With+Range+Safety+Destruct+System)        * [PAT-035 - Checklist for Safety-Critical or Mission-Critical Software](/spaces/SITE/pages/180584532/PAT-035+-+Checklist+for+Safety-Critical+or+Mission-Critical+Software) |

## 3.2 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Resources

### 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-024)

  [Human-Rating Requirements for Space Systems (Updated w/Change 2)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=2C "Click to open in new window")

  NPR 8705.2C, NASA Office of Safety and Mission Assurance, 2008.,
  Effective Date: July 10, 2017, Expiration Date: July 10, 2025
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-458)

  [NASA Technical Requirements for Human-Rating](https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/NASA-STD-871929-Baseline-draft.pdf "Click to open in new window")

  NASA-STD-8719.29, National Aeronautics and Space Administration, Approved:2023-12-11 Baseline,  This standard establishes technical requirements necessary to produce human-rated space
  systems that protect the safety of the crew and passengers on NASA space missions

### 4.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.
