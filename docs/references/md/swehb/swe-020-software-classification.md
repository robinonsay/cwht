# SWE-020 - Software Classification

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695405. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification

SWE-020 - Software Classification

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695405)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695405&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. The Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

3.5.1 The project manager shall classify each system and subsystem containing software in accordance with the highest applicable software classification definitions for Classes A, B, C, D, E, and F software in Appendix D. 

## 1.1 Notes

The expected applicability of requirements in this directive to specific systems and subsystems containing software is determined through the use of the NASA-wide definitions for software classes in Appendix D in conjunction with the Requirements Mapping Matrix in Appendix C. These definitions are based on (1) usage of the software with or within a NASA system, (2) criticality of the system to NASA’s major programs and projects, (3) extent to which humans depend upon the system, (4) developmental and operational complexity, and (5) extent of the Agency’s investment. Software assurance can perform an independent software classification, or software assurance can concur with engineering’s software classification decision. Software engineering and software assurance technical authorities need to agree on the classification of each system and subsystem containing software.

Software assurance may perform an independent software classification, or concur with engineering’s software classification decision. Software engineering and software assurance technical authorities need to agree on the classification of each system and subsystem containing software. If there is a disagreement between the technical authorities, then the dissenting opinion process for your center should be followed.

## 1.2 History

Click here to view the history of this requirement: SWE-020 History

SWE-020 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.8.1 The project shall classify each system and subsystem containing software in accordance with the software classification definitions for Classes A, B, C, D, E, F, G, and H software in Appendix E. |
| Difference between A and B | Clarified which Software Classification to chose by adding "highest applicable". |
| B | 3.5.1 The project manager shall classify each system and subsystem containing software in accordance with the highest applicable software classification definitions for Classes A, B, C, D, E, F, G, and H software in Appendix D. |
| Difference between B and C | Removed G and H software Classes |
| C | 3.5.1 The project manager shall classify each system and subsystem containing software in accordance with the highest applicable software classification definitions for Classes A, B, C, D, E, and F software in Appendix D. |
| Difference between C and D | No change |
| D | 3.5.1 The project manager shall classify each system and subsystem containing software in accordance with the highest applicable software classification definitions for Classes A, B, C, D, E, and F software in Appendix D. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

Classifying software provides essentially pre-tailoring of software engineering requirements, software safety requirements, software assurance requirements, and other software requirements for different types and levels of software. While every requirement may apply to the highest classification, not every requirement will apply to lower-level classifications.

Software classification is a cornerstone of NASA’s software engineering framework as it ensures that development rigor, safety measures, and assurance levels are appropriately aligned with the software's criticality, complexity, and mission significance. By classifying software correctly, the project can address safety risks, technical challenges, and the potential impact of software failure on the mission's success.

The rationale for this requirement is to provide a systematic approach to applying the appropriate level of engineering, assurance, and risk management to software systems and subsystems. Misclassification can result in underestimating the risks and applying inadequate controls, which could lead to failures or inefficiencies.

This requirement is essential to achieve an optimal and consistent balance between risk, resource allocation, and engineering rigor. By mandating a structured and collaborative classification process, NASA ensures that all software systems and subsystems are developed with appropriate levels of oversight, reliability, and compliance to maximize mission success.

## 2.1 Reasons for Software Classification

1. **Ensures the Correct Application of Requirements**

   * **NASA-STD-7150.2 Guidelines**: Software classes (A–F) are designed to define the level of engineering rigor and controls necessary for the scope and risks involved with each system or subsystem. By determining the software classification, projects can map the appropriate requirements using Appendix C to ensure compliance with NASA’s directives.
   * Without classification, there would be no structured approach to applying requirements, potentially leading to under-engineering or overburdening the project with unnecessary requirements.
2. **Matches Criticality with Rigor**

   * **Safety-Critical Systems**: For software deemed **safety-critical**, additional requirements and scrutiny are necessary because failures could result in loss of life, mission failure, or damage to property. Classification mandates stricter controls (e.g., Software Classes A or B) aligned with these risks.
   * **Lower Risk Systems**: Non-critical research or exploratory software may be classified as **Class C or D**, enabling the project to scale back unnecessary rigor while still maintaining accountability.
3. **Improves Risk Mitigation**

   * Correct classification ensures that software with significant risks to safety, mission objectives, or NASA’s reputation receives the highest level of oversight and testing. For example:
     + Mission-critical flight control systems (Class A) require rigorous validation and verification to minimize the risk of failure.
     + Software for internal research (Class D or E) may require lighter processes, reducing unnecessary burden.
4. **Optimizes Resources**

   * Classification enables projects to allocate resources—budget, personnel, and time—proportionally to the software’s importance and risk. Systems with higher classifications receive more intensive assurance and engineering focus, while less critical systems are developed using an efficient, streamlined process.
   * This avoids inefficient use of Agency resources while maintaining the necessary controls for high-risk systems.
5. **Supports Multi-Subsystem and Multi-Center Projects**

   * In projects with multiple subsystems or collaborations across Centers, classification ensures that each software product is developed with the necessary level of rigor. For example:
     + A rover’s autonomous navigation system may be classified as Class B or A, while its monitoring software may be Class C or D.
   * Classification allows teams to distinguish between critical and secondary components, enabling tailored requirements within large, complex projects.
6. **Provides Objective Documentation**

   * Software classification provides documented, traceable decisions that can be revisited and reevaluated as projects evolve. These decisions are essential during independent assessments, audits, and post-mission evaluations.
7. **Facilitates Relationship Between Engineering and Software Assurance**

   * The collaborative process of assigning classifications fosters communication and alignment between **Software Engineering (ETA)** and **Software Assurance (SMA TA)**. Mutual agreement on classifications ensures consistent application of NPR 7150.2 requirements.
8. **Supports Transition to Higher Classes**

   * Software classifications can evolve as project scope expands (e.g., transitioning from laboratory testing to operational deployment). The NPR includes guidance for reevaluating classifications during major project reviews to safeguard against underestimating project requirements.

## 2.2 Key Classification Drivers

Classification decisions are based on several critical factors, as defined in the NPR:

1. **Purpose of the Software**: What is the intended function of the software, and what objectives does it support?
2. **Safety-Critical Designation**: Is the software directly or indirectly linked to systems upon which personnel safety depends?
3. **Operational Complexity**: Does the software integrate with other systems in complex ways, requiring additional controls?
4. **Developmental Complexity**: Are there challenges or risks related to developing the software, such as high levels of innovation or unproven technologies?
5. **NASA Investment**: Does the project represent a significant monetary or reputational investment for NASA, dictating additional scrutiny and assurance requirements?

## 2.3 Benefits of Implementing the Requirement

1. **Improved Mission Safety and Reliability**  
   Correctly classified software ensures that safety-critical systems are subject to the rigor required to identify and mitigate risks, improving the reliability of NASA programs and protecting human life.
2. **Efficient Use of Resources**  
   Resources are applied where they are most needed—higher-risk systems are developed with full assurance measures, while lower-risk systems use more streamlined approaches.
3. **Flexibility Across Project Types**  
   The classification system allows for tailored application of requirements across a wide range of software, from research software and onboard spacecraft systems to administrative tools.
4. **Scalability for Multi-System Projects**  
   By assigning classifications at the system or subsystem level, the guidance ensures effective requirements management even for complex, multi-component projects.
5. **Accountability and Traceability**  
   Classification records provide objective evidence of decisions made, fostering accountability and simplifying assessment and audit processes.
6. **Compliance with Standards**  
   Ensures all software aligns with **NASA-STD-7150.2**, **NASA-STD-8739.8**, and other applicable agency standards, fostering consistent practices across Centers and projects.

## 2.4 Risks Addressed by This Requirement

1. **Failure in Safety-Critical Systems**: Misclassification of critical systems can lead to inappropriate application of verification and validation processes, increasing the likelihood of catastrophic failures.
2. **Over-Engineering Low-Risk Components**: Without tailored classifications, systems with minimal risk could be subjected to excessive processes, leading to inefficiency and unnecessary expenditure.
3. **Miscommunication Between Teams**: Clear classification encourages communication across software engineering, software assurance, and project management, reducing the likelihood of conflicting interpretations.
4. **Evolving Project Scope Without Reclassification**: Revisiting classifications ensures that project or mission changes are reflected in the requirements applied to software systems.

# 3. Guidance

Adherence to accurate software classification ensures that the appropriate requirements are applied to systems and subsystems based on their criticality, purpose, and risks. For small projects, classification must balance efficiency with compliance, while for larger projects, it provides a foundation for robust assurance and risk mitigation practices throughout the software lifecycle. Regular review and documentation are essential for maintaining classification accuracy as project scope and goals evolve.

## 3.1 Applicability of Requirements

### 3.1.1 Overview

In projects containing multiple systems and subsystems with varying software classifications, the applicability of **NPR 7150.2 requirements** is determined based on the combination of software classification (Appendix D) and safety-critical designation, as outlined in the **Requirements Mapping and Compliance Matrix (Appendix C)**. This mapping process ensures the appropriate application of engineering, safety, and assurance practices that reflect the software’s criticality, operational complexity, and role within its system.

### 3.1.2 Key Considerations for Applicability

When classifying software and determining the applicability of requirements:

1. **Usage Context**: Evaluate the software's purpose and its interaction within a **NASA system**.
2. **Criticality of System**: Assess the impact of the software on major NASA programs, focusing on mission reliability.
3. **Human Dependency**: Consider the extent to which humans directly depend on the software (e.g., safety-critical flight systems).
4. **Developmental and Operational Complexity**: Complexity drives rigor and requirements—analyze integration challenges and operational constraints.
5. **Agency Investment**: Ensure robust classification for high-investment systems that require stringent assurance to protect resources.

### 3.1.3 Actionable Guidance

* **Timing**: **Perform software classification as soon as a project includes software**. Early classification ensures requirements are applied in alignment with project scope and risks.
* **Technical Authority Agreement**: Classification decisions must be agreed upon by **Software Engineering Technical Authority (ETA)** and **Software Assurance Technical Authority (SMA TA)**. Disagreements follow the Center’s dissenting opinion process.
* **Default Compliance Matrix**: Use **Appendix C** as the foundation to map requirements based on the assigned software class and safety-criticality designation.

### 3.1.4 Resources

1. **Topic 7.04**: Flow Down of NPR Requirements on Contracts and Multi-Center Projects.
2. **Topic 7.16**: Appendix C - Requirements Mapping and Compliance Matrix.
3. **SWE-176**: Guidelines for Software Records Documentation.

## 3.2 Classification Considerations

### 3.2.1 Critical Factors for Classification

When classifying systems or subsystems containing software, consider the following:

1. **Scope of Classification**:

   * Conduct classification assessments for all software components within the system or subsystem.
   * Some subsystems may merit unique classifications if their usage or risks differ from the broader system.
2. **Purpose of Software**:

   * Classify based on the intended function of the software: control functions, data processing, or interaction with hardware.
3. **Usage Context**:

   * Evaluate how the software will be employed within operational environments or systems (e.g., flight or ground operations).
4. **Program and Project Relevance**:

   * Determine how the software contributes to major NASA programs or the mission’s critical objectives.
5. **Hardware Controls**:

   * Assess interaction with hardware, as systems that control critical hardware (e.g., propulsion systems) may require higher classification.
6. **Human Interaction**:

   * Identify systems with direct human interaction, as these often require enhanced safety and usability assurance.
7. **Complexity**:

   * Consider both **developmental complexity** (e.g., integration with external systems) and **operational complexity** (e.g., adapting to dynamic environments).
8. **Risks**:

   * Address risks to the project, the sponsoring Center, and the Agency, factoring in potential failures.
9. **Investment**:

   * Higher levels of Agency investment in a software product warrant thorough classification and applicable requirements.

### 3.2.2 Special Considerations for Safety-Critical Components

* Any software component deemed **safety-critical**, per the process defined in **NASA-STD-8739.8**, must be classified as **Class D or higher**. This ensures rigor appropriate for systems where failures could result in loss of life, mission, or system integrity.

### 3.2.3 Resources

1. **Topic 7.02**: Classification and Safety-Criticality Overview.
2. **NASA-STD-8739.8**: Safety-Critical Software Designation Process.

## 3.3 Commercial, Government, Legacy, Heritage, and MOTS Software

### 3.3.1 Verification and Validation Standards

COTS (Commercial Off-the-Shelf), MOTS (Modified Off-the-Shelf), GOTS (Government Off-the-Shelf), reused, legacy, heritage, or auto-generated software components must be verified and validated to **meet the same standards** as newly developed software to ensure fitness for their intended use.

Projects must ensure compliance by:

1. **Matching with Class Requirements**: These software components must meet the applicable requirements based on their assigned classification from **Appendix C**.
2. **Consistency in Testing**: Conduct verification and validation activities equivalent to those required for developed software, including:
   * Functional testing.
   * Performance testing.
   * Integration testing with system hardware.
3. **Documenting Compliance**: Record results in project documentation to demonstrate compliance.

### 3.3.2 Resources and Special Considerations

1. **Topic** [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations)
2. **Topic** [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code)

## 3.4 Final Classification

### 3.4.1 Resolving Classification Conflicts

The **final classification** of systems and subsystems containing software is achieved through agreement between the project office, Software Development organization, and Software Assurance (SA).

* **Conflict Resolution:** In cases of disagreement, the **Software Engineering Technical Authority (ETA)** facilitates resolution with the **Safety and Mission Assurance Organization (SMA)**.

### 3.4.2 Prevent Misclassification

Software classifications must reflect the true criticality and risk associated with the component—**misclassification to reduce requirements is prohibited**. If certain requirements cannot be met for a high-risk or small mission, initiate a waiver process through the Engineering Technical Authority.

## 3.5 Classification Revisited

### 3.5.1 Periodic Review

Software classification is not static and may evolve as the project progresses. Revisit and validate the classification during **major project reviews (e.g., PDR, CDR)** or whenever there are significant changes in:

1. **Software Design**: New architectural or functional decisions may alter risks and classification.
2. **Operational Usage**: Moving software from research/development environments into operational use may require transitioning to a higher classification level.
3. **Project Scope**: Scope changes impacting criticality or investment may warrant re-evaluation.

### 3.5.2 Example Case

A research software system initially classified as **Class C** for laboratory use may be transitioned to **Class B** if it becomes essential for operations in real-world environments.

### 3.5.3 Transition Considerations

* Use **SWE-021** and **Topic 7.13** for guidelines on transitioning software classification to a higher class.
* Update **SWE-125 Requirements Compliance Matrix** to reflect new classifications and ensure all revised requirements are addressed.

## 3.6 NASA Software Classifications

Definitions and examples for each software classification taken from NPR 7150.2D, Appendix D:

**Figure 1. NASA software classification structure**

#### **NASA-Wide Software Classifications**

#### **Class AHuman-Rated Space Software Systems**

#### **Class B      Non-Human Space-Rated Software Systems or Large-Scale Aeronautics Vehicles**

#### **Class C      Mission Support Software or Aeronautic Vehicles, or Major Engineering/Research Facility Software**

#### **Class D****Basic Science/Engineering Design and Research and Technology Software**

#### **Class E       Design Concept, Research, Technology, and General Purpose Software**

#### **Class F       General Purpose Computing, Business, and IT Software**

#### ***Notes: It is not uncommon for a project to contain multiple systems and subsystems having different software classes.***

The balance of this appendix has been reorganized into a table format to make it easier to read.

| Definition | Examples and Exclusions |
| --- | --- |
| Class A Human Rated Space Software Systems | |
| **Human Space Flight Software Systems\*:**  Ground and flight software systems developed or operated by or for NASA needed to perform a primary mission objective of human space flight and directly interact with human space flight systems. Limited to software required to perform "vehicle, crew, or primary mission function," as defined by software that is:  (a) Required to operate the vehicle or space asset (e.g., spacesuit, rover, or outpost), including commanding of the vehicle or asset.  (b) Required to sustain a safe, habitable1 environment for the crew.  (c) Required to achieve the primary mission objectives, or  (d) Required to directly prepare resources (e.g., data, fuel, power) that are consumed by the above functions.  \*Includes software involving launch, on-orbit, in space, surface operations, entry, descent, and landing.  1 Current standards that address habitability and environmental health, including atmospheric composition and pressure, air, and water quality and monitoring, acceleration, acoustics, vibration, radiation, thermal environment, combined environmental effects, and human factors, are documented in NASA-Standard-3001 Volume 1, Space Flight Human-System Standard: Crew Health, NASA-Standard-3001 Volume 2, Space Flight Human-System Standard: Human Factors, Habitability, and Environmental Health, FAA HFDS - Human Factors Design Standard. | **Examples of Class A software (human-rated space flight) include but are not limited to the mission phases listed below:**  Examples of Class A software (human-rated space flight) include, but are not limited to, the mission phases listed below.  1. During Launch:  Abort modes and selection; separation control; range safety; crew interface (display and controls); crew escape; critical systems monitoring and control; guidance, navigation, and control; and communication and tracking.  2. On-Orbit/In Space:  Extravehicular activity (EVA); control of electrical power; payload control (including suppression of hazardous satellite and device commands); critical systems monitoring and control; guidance, navigation, and control; life support systems; crew escape; rendezvous and docking; failure detection; isolation and recovery; communication and tracking; and mission operations.  3. On Ground:  Pre-launch and launch operations; Mission Control Center (and Launch Control Center) front-end processors; spacecraft commanding; vehicle processing operations; re-entry operations; flight dynamics simulators used for ascent abort calls; and launch and flight controller stations for human-crewed spaceflight.  4. Entry, Descent, and Landing (EDL):  Command and control; aero-surface control; power; thermal; fault protection; and communication and tracking.  5. Surface Operations:  Planet/lunar surface EVA and communication and tracking.    **Exclusions:**  **Class A does not include:**  1. Software that happens to fly in space but is superfluous to mission objectives (e.g., software contained in an iPod carried onboard by an astronaut for personal use); or  2. Software that exclusively supports aeronautics, research and technology, and science conducted without space flight applications; or  3. Systems (e.g., simulators, emulators, stimulators, facilities) used to test Class A systems containing software in a development environment. |
| Class B Non - Human Space Rated Software Systems or Large Scale Aeronautics Vehicles | |
| 1. Space Systems involve flight and ground software that should perform reliably to accomplish primary mission objectives or major function(s) in non-human space rated systems. Included is software involving launch, on-orbit, in space, surface operations, entry, descent, and landing. These systems are limited to software that is:  (a) Required to operate the vehicle or space asset (e.g., orbiter, lander, probe, flyby spacecraft, rover, launch vehicle, or primary instrument) such as commanding of the vehicle or asset;  (b) Required to achieve the primary mission objectives; or  (c) Required to directly prepare resources (data, fuel, power) that are consumed by the above functions.  2. Airborne Vehicles include large scale1 aeronautic vehicles unique to NASA in which the software:  (a) Is integral to the control of an airborne vehicle;  (b) Monitors and controls the cabin environment; or  (c) Monitors and controls the vehicle’s emergency systems.  This definition includes software for vehicles classified as “test,” “experimental,” or “demonstration” that meets the above definition for Class B software. Also included are systems in a test or demonstration where the software’s known and scheduled intended use is to be part of a Class A or B software system.  1 Large-scale (life cycle cost exceeding $250M) fully integrated technology development system – see NPR 7120.8. | Examples of Class B software include, but are not limited to:  1. Space, Launch, Ground, EDL, and Surface Systems:  Propulsion systems; power systems; guidance navigation and control; fault protection; thermal systems; command and control ground systems; planetary/lunar surface operations; hazard prevention; primary instruments; science sequencing engine; simulations that create operational EDL parameters; subsystems that could cause the loss of science return from multiple instruments; flight dynamics and related data; and launch and flight controller stations for non-human spaceflight.  2. Aeronautics Vehicles (Large Scale NASA Unique):  Guidance, navigation, and control; flight management systems; autopilot; propulsion systems; power systems; emergency systems (e.g., fire suppression systems, emergency egress systems, emergency oxygen supply systems, traffic/ground collision avoidance system); and cabin pressure and temperature control.  **c. Exclusions:**  Class B does not include:  1. Software that exclusively supports non-primary instruments on non-human space rated systems (e.g., low-cost non-primary university supplied instruments); or  2. Systems (e.g., simulators emulators, stimulators, facilities) used in testing Class B systems containing software in a development environment; or  3. Software for NASA Class D payloads, as defined in NPR 8705.4. |
| Class C Mission Support Software or Aeronautic Vehicles, or Major Engineering/ Research Facility Software | |
| **1. Space Systems include the following types of software:**  (a) Flight or ground software necessary for the science return from a single (non-primary) instrument;  (b) Flight or ground software used to analyze or process mission data;  (c) Other software for which a defect could adversely impact the attainment of some secondary mission objectives or cause operational problems;  (d) Software used for the testing of space assets;  (e) Software used to verify system requirements of space assets by analysis; or  (f) Software for space flight operations not covered by Class A or B software.  **2. Airborne Vehicles include systems for non-large scale aeronautic vehicles in which the software:**  (a) Is integral to the control of an airborne vehicle;  (b) Monitors and controls the cabin environment; or  (c) Monitors and controls the vehicle’s emergency system.  Also included are systems on an airborne vehicle (including large-scale vehicles) that acquire, store, or transmit the official record copy of flight or test data.  **3. Major Engineering/Research Facility is systems that operate a major facility for research, development, test, or evaluation (e.g., facility controls and monitoring, systems that operate facility-owned instruments, apparatus, and data acquisition equipment).**  **4. Sounding Rockets and Sounding Rocket payloads.**  **5. Software for NASA Class D payloads, as defined in NPR 8705.4.** | **Examples of Class C software include, but are not limited to:**  **1. Space Systems:**  Software that supports prelaunch integration and test; mission data processing and analysis; analysis software used in trend analysis and calibration of flight engineering parameters; primary/major science data collection storage and distribution systems (e.g., Distributed Active Archive Centers); simulators, emulators, stimulators, or facilities used to test Class A, B, or C software in development; integration and test environments; software used to verify system-level requirements associated with Class A, B, or C software by analysis (e.g., guidance, navigation, and control system performance verification by analysis); simulators used for mission training; software employed by network operations and control (which is redundant with systems used at tracking complexes); command and control of non-primary instruments; ground mission support software used for secondary mission objectives, real-time analysis, and planning (e.g., monitoring, consumables analysis, mission planning); CubeSat mission software; SmallSat mission software; sounding rocket software and sounding rocket experiments or payload software; and all software on NASA Class D payloads, as defined in NPR 8705.4 to examples of Class C software.  **2. Aeronautics Vehicles:**  Guidance, navigation, and control; flight management systems; autopilot; propulsion systems; power systems; emergency systems (e.g., fire suppression systems, emergency egress systems, emergency oxygen supply systems, traffic/ground collision avoidance system); cabin pressure and temperature control; in-flight telescope control software; aviation data integration systems; automated flight planning systems and primary/major science data collection storage and distribution systems (e.g., Distributed Active Archive Centers); sounding rockets and sounding rocket experiments or payload software; flight software for free-flying unmanned aerial vehicles (UAVs) in public airspace or over-controlled ranges; Balloon Flight software and balloon flight experiment software, and all software on NASA Class D payloads, as defined in NPR 8705.4.  **3. Major Engineering/Research Facility:**  Major Center facilities; data acquisition and control systems for wind tunnels, vacuum chambers, and rocket engine test stands; ground-based software used to operate a major facility telescope; and major aeronautic applications facilities (e.g., air traffic management systems; high fidelity motion-based simulators).  **c.** **Exclusions:**  **Class C does not include:**  Systems unique to research, development, test, or evaluation activities in a major engineering/research facility or airborne vehicle in which the system is not part of the facility or vehicle and does not impact the operation of the facility or vehicle. |
| Class D Basic Science/Engineering Design and Research and Technology Software | |
| **1. Basic Science/Engineering Design includes:**  (a) Ground software that performs secondary science data analysis;  (b) Ground software tools that support engineering development;  (c) Ground software or software tools used for informal testing of software systems;  (d) Ground software tools that support mission planning or formulation;  (e) Ground software that operates a research, development, test, or evaluation laboratory (i.e., not a major engineering/research facility); or  (f) Ground software that provides decision support for non-mission critical situations.  **2. Airborne Vehicle Systems include:**  (a) Software whose anomalous behavior would cause or contribute to a failure of system function resulting in a minor failure condition for the airborne vehicle (e.g., DO-178B, “Class D”);  (b) Software whose anomalous behavior would cause or contribute to a failure of system function with no effect on airborne vehicle operational capability or pilot workload (e.g., DO-178B, “Class E”); or  (c) Ground software tools that perform research associated with airborne vehicles or systems.  **3. Major Engineering/Research Facility related software includes research software that executes in a major engineering/research facility but is independent of the operation of the facility.** | **Examples of Class D software include, but are not limited to:**  **1. Basic Science and Engineering Design:**  Engineering design and modeling tools (e.g., computer-aided design and computer-aided manufacturing (CAD/CAM), thermal/structural analysis tools); project assurance databases (e.g., problem reporting, analysis, and corrective action system, requirements management databases); propulsion integrated design tools; integrated build management systems; inventory management tools; probabilistic engineering analysis tools; test stand data analysis tools; test stand engineering support tools; experimental flight displays evaluated in a flight simulator; forecasts and assimilated data products; and tools used to develop design reference missions to support early mission planning.  **2. Airborne Vehicles:**  Software tools for designing advanced human-automation systems; experimental synthetic-vision display; and cloud-aerosol light detection and ranging installed on an aeronautics vehicle; flight software for physically constrained UAVs such as UAVs on tethers, within cages, or used in indoor labs; and experimental UAV payloads with minor consequences of failure.  **c. Exclusions:**  **Class D does not include:**  1. Software that can impact primary or secondary mission objectives or cause loss of data that is generated by space systems;  2. Software that operates a major engineering/research facility;  3. Software that operates an airborne vehicle; or  4. Flight software (i.e., software that meets the flight portions of Class A, B, or C Software Classifications). |
| Class E Design Concept and Research and Technology Software | |
| **Definition:**  1. Software developed to explore a design concept or hypothesis but not used to make decisions for an operational Class A, B, or C system or to-be-built Class A, B, or C system.  2. Software used to perform minor analyses of science or experimental data. Class E software cannot be safety-critical software. If the software is classified as safety-critical software, then it has to be classified as Class D or higher.  3. A defect in Class E software may affect the productivity of a single user or small group of users but generally will not affect mission objectives or system safety.  4. Class E software runs in a general-purpose computing environment or a board top environment. Class E software does not support ground tests, flight tests, or operations. | **Examples of Class E software include, but are not limited to:**  Examples of Class E software include, but are not limited to, parametric models to estimate performance or other attributes of design concepts; software to explore correlations between data sets; line of code counters; file format converters; and document template builders. Class E can include prototypes of flight and ground systems, developed at minimal cost, in the spirit of “exploring a design concept.” Once the design concept is demonstrated, and a program agrees to incorporate it for flight or ground operational use, or for an in-flight test of the technology, then the software should be upgraded to its appropriate classification, based on the operational (or in-flight test) use case. Class E software includes, but is not limited to, software such as word processing applications, spreadsheet applications, and presentation applications.  **Exclusions**  Class E does **not** include:'  1. Flight systems (i.e., software that meets the flight portions of Class A, B, C, or D Software Classifications);  2. Software developed by or for NASA to directly support an operational system (e.g., human-rated space system, robotics spacecraft, space instrument, airborne vehicle, major engineering/research facility, mission support facility, and primary/major science data collection storage and distribution systems);  3. Software developed by or for NASA to be flight-qualified to support an operational system;  4. Software that directly affects primary or secondary mission objectives;  5. Software that can adversely affect the integrity of engineering/scientific artifacts;  6. Software used in technical decisions concerning operational systems, or systems being developed for operation;  7. Software that has an impact on operational vehicles; or  8. Software that is safety-critical. |
| **Business and Information Technology Infrastructure Software** | |
| **Class F General Purpose Computing, Business, and IT Software** | |
| **Definition:**  General-purpose computing Business and IT software used in support of the Agency, multiple Centers, multiple programs/projects, single Centers/projects, or locally deployed General Purpose Infrastructure To-Be Component of the NASA Enterprise Architecture. These software applications are generally used to support voice, wide-area network, local area network, video, data Centers, business and IT application services (e.g., Finance, Logistics, Human Capital, Procurement), messaging and collaboration, and public Web. A defect in Class F software is likely to affect the productivity of multiple users across a single geographic location or several geographic locations and may affect mission objectives or system safety. Mission objectives can be cost, schedule, or technical objectives for any work that the Agency or a Center performs. | Examples of Class F software include but are not limited to: Examples of Class F software include, but are not limited to, Agency-wide enterprise applications (e.g., WebTADS, SAP, eTravel, ePayroll, Business Warehouse), Center-specific software, or specific Web applications, including mobile applications; Agency-wide educational outreach software; software in support of the NASA-wide area network; and the NASA Web portal. |

When questions arise regarding software classification, consult with the Engineering and SMA Technical Authorities (TAs).

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-021 - Transition to a Higher Class](/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

Records of classification are maintained by the project. See also [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans), and Topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan), [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan),

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Classification](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Classification)      * [Process Selection](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Process+Selection) |

# 4. Small Projects

Small projects often have less complexity and fewer resources compared to large-scale missions. However, classification remains a critical step for ensuring appropriate rigor is applied to software systems and subsystems. To address the needs of small projects efficiently, the guidance below focuses on streamlining the classification process while ensuring compliance with **NPR 7150.2** [083](#_tabs-<p></p>).

Small projects can successfully meet classification requirements by tailoring the process for their scale, leveraging pre-existing classifications, efficiently collaborating, and documenting decisions concisely. This approach balances compliance with resource constraints to enable small projects to achieve high-quality outcomes without unnecessary administrative overhead.

## 4.1 Leverage Pre-Existing Classification Frameworks

Small projects can reduce effort by reusing or referencing classification decisions from similar previous projects, particularly those using similar technologies, methodologies, and risk profiles.

* **Analyze Similar Projects:** Identify previous projects that share similarities in system goals, software tools, or subsystems.
* **Reuse Established Class Definitions:** If the classification process for similar projects is well-documented, adapt it for the current project, ensuring the rationale still applies.
* **Confirm Applicability:** Verify that conditions such as new risks, safety-criticality, or added complexity are accounted for—adjust classifications if necessary.

## 4.2 Create a Simplified Classification Workflow

For small projects, the classification process can be optimized based on fewer systems and subsystems. Establish a straightforward workflow:

1. **List Subsystems and Their Software Components**: Identify all software integrated into the project’s systems and subsystems.
2. **Evaluate Safety-Criticality**: Identify whether any component qualifies as **safety-critical** per **NASA-STD-8739.8**, requiring a minimum classification of Software Class D.
3. **Review Appendix D Definitions**: Align the classification of each system and subsystem with NPR 7150.2 Appendix D definitions based on:
   * How the software is intended to be used.
   * Interaction with humans.
   * Developmental and operational complexity.
   * Risks and Agency investment.
4. **Assign Classifications:** Apply the **highest applicable classification level** across related systems and subsystems (e.g., if a safety-critical subsystem is Class D, the system may need to match this classification).

## 4.3 Collaborate Effectively

Although small projects may have a leaner team, collaboration between **Software Engineering** and **Software Assurance (SA)** remains critical:

* **Shared Responsibility**: Software Engineering performs the initial classification, while SA reviews and provides concurrence.
* **Streamlined Communication**: Use regular team meetings or joint reviews to agree on classifications early in the project timeline.
* **Dispute Resolution**: Escalate disagreements through the Technical Authority chains only when local collaboration cannot resolve the discrepancy.

## 4.4 Focus on Key Known Risks

Small projects typically have limited scope, so risk assessment is often focused on a few critical factors:

* **Safety-Critical Designation:** Determine whether the software supports hardware or functions that could compromise safety or operational integrity (e.g., software controlling flight systems or hazardous operations).
* **Interaction Complexity:** Assess systems that interact extensively with users or external systems for higher classification.
* **Investment Protection:** Ensure rigorous classification for software systems tied to significant Agency investments (e.g., research software or mission control software).

## 4.5 Minimize Documentation Overhead

Small projects often have lighter documentation requirements. Scale classification records to reflect the project size:

* **Simplified Classification Report:** Consolidate the classification results for all systems and subsystems into a single brief document that includes:
  + List of systems/subsystems and their classifications.
  + Justifications for classification decisions.
  + Evidence of SA concurrence (e.g., meeting notes, signed documents).
* **Use Existing Templates:** NASA or Center-provided templates for classification reports can be adapted for small projects.

## 4.6 Schedule Classifications Early

Small projects often need to move quickly through the initial stages. Early classification ensures applied requirements correspond with the risk and complexity of the system.

* **Classify During Formulation Phase**: Begin classification as soon as it is determined that the project includes software.
* **Efficiency Tip:** For software reusing heritage code or tools, classifications can often be inherited (with reassessments as needed).

## 4.7 Tools and Resources for Small Projects

Leverage lightweight tools and resources to streamline classifications for small projects. Useful resources include:

* **Software Classification Appendix D**: Review the definitions provided by NPR 7150.2.
* **NASA-STD-8739.8**: Define and confirm safety-critical software designations.
* **Center Tools**: Many Centers have tools or databases that include previously documented classification decisions for reference.
* **SATERN Training**: Provide concise training to project personnel on classification requirements if gaps exist in team expertise.

## 4.8 Handling Multiple Classifications

Some small projects may contain systems and subsystems with varying software classifications:

* **Aggregate by Highest Classification**: Ensure that subsystems with the highest classification drive overarching requirements for the system.
* **Apply Minimal Differentiation Where Possible**: Whenever feasible, minimize complexity by combining subsystems under a single classification to streamline processes.
* **Customize Individual Subsystems Only If Needed**: Adapt requirements specifically for subsystems with lower classifications, but avoid excessive partitioning that undermines efficiency.

## 4.9 Addressing Discrepancies

For small projects where classification disagreements arise:

* **Resolve Locally**: Schedule focused discussions between SA and software engineering to reconcile views.
* **Escalate Only If Necessary**: Small projects should avoid Technical Authority escalation unless disagreements pose significant risks to system development or compliance.
* **Use Precedent**: Reference classifications from older projects to support resolution of disputes.

## 4.10 Example Use Case

**Small Project Scenario**: A small project is developing a scientific autonomous software system controlling a rover for environmental monitoring.

* **Initial Indicators**:
  + The rover’s software interacts minimally with humans but is central to mission functionality.
  + Some subsystems are designed for high-complexity sequences (e.g., autonomous decision-making).
  + The project investment is moderate.
  + The software does not support hardware impacting safety directly.
* **Classification Result**:
  + Safety review determines software is not safety-critical.
  + Classification aligns closely with **Class C**, based on relevance to NASA programs and operational complexity.
  + Software engineering proposes Class C classification, and SA concurs after review.

## 4.11 Benefits of This Approach

1. **Efficiency**: Reduces unnecessary steps by leveraging pre-existing resources and streamlining the process.
2. **Compliance**: Ensures proper classifications are applied, adhering to NPR requirements without overburdening small projects.
3. **Consistency**: Establishes a repeatable framework for small projects, enabling predictability across future classification workflows.
4. **Cost-Effectiveness**: Minimizes documentation and effort while maintaining oversight.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-332) Software Project Planning,  GRC-SW-7150.3, Revision C, Software Engineering Process Group, NASA Glenn Research Center, 2011. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook. Note: Revision Mark-up visible on this version.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

**LLSW15 — Early Safety Applicability to “Uncrewed” Systems that Interface with Crew**

* ***Context/Background: PPE initially excluded from human‑rating; later interfaces demanded safety compliance, causing costly remedies.***
* ***Lesson Learned: Apply safety requirements early to any system that interfaces with crewed systems.***
* ***Evidence/Observation: Delays/confusion in HR scope; expensive fixes to improve.***
* ***Cause(s): Procurement/requirements processes lacked SMA inputs.***
* ***Recommendation/Corrective Action: Engage SMA in procurement; include safety clauses in contracts; classify software appropriately (SWE020/160/133).***
* ***Implementation Guidance: SWE020, SWE133/134, SWE013.***
* ***Success Criteria/Verification: No late adds of safety requirements; HR scope correct at start; reduced variance requests.***
* ***Applicability/Scope: All interfacing systems, crew‑adjacent.***
* ***Related Standards/Requirements: SWE020, SWE133, SWE134, SWE013.***

**LLSW14 — Strengthen Fault Tolerance Requirements**

* **Context/Background: Wording emphasized single‑fault tolerance; permanent crew goals argue for dual‑fault tolerance in many cases.**
* **Lesson Learned: Encourage dual+ fault tolerance for systems supporting crewed missions.**
* **Evidence/Observation: Gateway’s short crewed periods vs Moon Base permanence; ISS practices emphasize dual FT.**
* **Cause(s): Ambiguous FT wording; provider minimal compliance.**
* **Recommendation/Corrective Action: Update safety requirement language; define explicit FT targets and verification.**
* **Implementation Guidance: SWE133/134, SWE050.**
* **Success Criteria/Verification: Documented FT analyses; verification across nominal/off‑nominal.**
* **Applicability/Scope: Safety‑critical software and interfaces.**
* **Related: SWE133, SWE134, SWE050.**

**LLSW11 — COTS Classification Issues for CBCS**

* ***Context/Background: Teams struggled to apply NPRs to COTS/reuse; safety controls missing in COTS; insight difficult.***
* ***Lesson Learned: Create program‑specific COTS/reuse policy clarifying applicability of NPR******2/standards to CBCS, including safety control expectations.***
* ***Evidence/Observation: Reliability/availability/upgrade issues with COTS critical items; provider resistance to design insights.***
* ***Cause(s): Undefined requirements/expectations; lack of upfront safety control provisions.***
* ***Recommendation/Corrective Action: Update Agency NPRs/standards (or tailor) for COTS in human‑rated contexts; perform early feasibility against safety controls.***
* ***Implementation Guidance: SWE027, SWE133/134, SWE158.***
* ***Success Criteria/Verification: Documented COTS policies; hazard controls traceable to requirements; successful verification closeouts.***
* ***Applicability/Scope: Safety‑critical CBCS, avionics, integrated systems.***
* ***Related: SWE027, SWE133, SWE134, SWE158.***

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-020 - Software Classification**

3.5.1 The project manager shall classify each system and subsystem containing software in accordance with the highest applicable software classification definitions for Classes A, B, C, D, E, and F software in Appendix D.

Accurate software classification is critical to ensuring appropriate application of NASA’s software engineering requirements as defined in **NPR 7150.2**. Software classifications influence the rigor applied to development, assurance, and verification processes. Software Assurance (SA) plays a critical role in independently reviewing the classification process and providing concurrence (or identifying disagreements that require escalation). Ensuring alignment with the correct classification minimizes risks by applying the appropriate controls proportional to the software’s criticality, complexity, and importance to NASA missions.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Perform a software classification or concur with the engineering software classification of software per the descriptions in NPR 7150.2.

## 7.2 Software Assurance Products

### 7.2.1 Software Classification Assessment Report

**Purpose**: Documents SA’s evaluation and concurrence (or disagreement) with the classifications assigned to the project's systems and subsystems containing software.  
**Contents**:

* List of all systems and subsystems containing software, along with their assigned classifications (Class A, B, C, D, E, F).
* Justification for the classifications assigned by software engineering, including:
  + Software purpose and relevance to NASA programs and projects.
  + Hardware controls and software's role in the system.
  + Operational and developmental complexity.
  + Interaction with humans and other subsystems.
  + Risks to the project or Agency.
  + Agency investment in the software.
* Results of the SA review, including:
  + Concurrence with classifications or identification of inconsistencies.
  + Recommendations or alternatives for reclassification (if applicable).
* Record of communication between SA and software engineering regarding classification agreement or disagreements.

### 7.2.2 Evidence of Software Assurance Concurrence

**Purpose**: Tracks formal Software Assurance concurrence (or non-concurrence) on the project’s software classification decisions.  
**Contents**:

* Signed concurrence document or verification notes where SA agrees with the assigned software classifications.
* Records of SA participation in discussions or meetings where software classification assignments were reviewed.
* Documentation of reclassification processes (if reclassification was required based on SA input).

### 7.2.3 Software Classification Discrepancy Report (if applicable)

**Purpose**: Formalizes cases where SA identifies discrepancies in the software classifications assigned by software engineering.  
**Contents**:

* Specific areas of disagreement with the assigned software classifications, including detailed rationale and references to **NPR 7150.2 Appendix D** and **NASA-STD-8739.8**.
* Recommended resolutions or actions to escalate the discrepancy via the Engineering Technical Authority (ETA) and Safety and Mission Assurance Technical Authority (SMA TA) chains.
* Status and resolution details of discrepancies, including outcomes of discussions between SA and software engineering.

## 7.3 Metrics

Metrics provide insight into the completeness, accuracy, and distribution of software classifications across the project portfolio.

### Key Metrics

### 7.3.1 Distribution of Software Classifications Across the Project:

* **% of Total Source Code at Each Software Classification (organizational measure):**
  + Indicates the proportional breakdown of the project's software code across classifications (e.g., Class A, B, C, etc.).
  + Supports resource planning and ensures appropriate levels of rigor are applied to software products based on their assigned classes.

### 7.3.2 Software Classification Agreement Metrics:

* **% of Projects with SA Concurrence for Software Classifications:**
  + Tracks the rate of agreement between SA and software engineering on classification assignments.
* **% of Classification Discrepancies Resolved Before Major Reviews (e.g., PDR, CDR):**
  + Measures the resolution effectiveness of classification disagreements to ensure timely compliance.

see also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

### 7.4.1 Reaching Agreement on Software Classifications

* **Collaboration Between SA and Software Engineering**: Classification is a joint responsibility between Software Engineering and Software Assurance. Both parties must agree on the assigned classifications for systems and subsystems.
* **Independent SA Assessment (Optional):** Although an independent reclassification effort by SA is not required by default, NASA Centers may mandate an independent review of classifications based on local processes. If no independent review is required, SA should perform an evaluation of the proposed classifications and confirm their concurrence.

### 7.4.2 Classification Considerations

Ensure all factors are considered when classifying software:

1. **Software Role in the System or Subsystem**: Assess the software’s purpose, usage, and relevance to program or system objectives.
2. **Safety-Critical Status**: If software is determined to be safety-critical (per **NASA-STD-8739.8**), it must be assigned Class D or higher.
3. **Interaction with Humans**: Systems with significant interaction with humans may require higher classification levels based on inherent risks.
4. **Operational and Developmental Complexity**: Complex systems with high integration demands may require stricter classification.
5. **Risk to the Mission or Agency**: Consider risks associated with software failure to NASA’s reputation, mission success, and financial investment.

### 7.4.3 Best Practices for Timely Classification

* Classify **as soon as it is determined that a project includes software.** Early classification ensures that requirements (e.g., SWE-071, SWE-190 for safety-critical software) are applied promptly.
* Use **Appendix D of NPR 7150.2** as the primary reference for classification definitions and apply the Requirements Mapping and Compliance Matrix in **Appendix C** to guide requirements applicability.

### 7.4.4 Resolving Classification Disagreements

When SA and software engineering do not agree on classification assignments:

1. **Document Disagreement**: SA should record the specific issues in a **Software Classification Discrepancy Report**.
2. **Engage the Technical Authority Chains**: Escalate unresolved discrepancies through the **Engineering Technical Authority (ETA)** and **SMA Technical Authority (SMA TA)** to ensure resolution.
3. **Determine Correct Classification**: Use authority chain decisions to finalize classification assignments, ensuring compliance with NPR 7150.2 requirements.

By rigorously verifying and concurring on software classifications, Software Assurance ensures that appropriate development rigor, risk management, and NASA standards are applied to each software product in the project. Accurate and timely classifications reduce risks and improve the quality, safety, and reliability of software for NASA’s critical systems and missions.

When classifying software be sure to consider:

* All software for the system or subsystem (classification may need to be assessed separately). [278](#_tabs-<p></p>)
* The purpose of the software.
* How the software is intended to be used.
* Relevance to major programs and projects.
* Hardware controls.
* Operations.
* Interaction with humans.
* Complexity (developmental and operational complexity is woven into the class definitions).
* The risk to the project, Center, and Agency
* Investment.

If a software component is determined to be safety-critical software, per the software safety-critical determination process defined in NASA-STD-8739.8 [278](#_tabs-<p></p>), then the software component classification must be Software Class D or higher.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-021 - Transition to a Higher Class](/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

# 8. Objective Evidence

Objective evidence ensures traceability and accountability for the software classification process as it applies to systems and subsystems.

Definition of objective evidence

Objective evidence is an unbiased, documented fact showing that an activity was confirmed or performed by the software assurance/safety person(s). The evidence for confirmation of the activity can take any number of different forms, depending on the activity in the task. Examples are:

* Observations, findings, issues, risks found by the SA/safety person and may be expressed in an audit or checklist record, email, memo or entry into a tracking system (e.g. Risk Log).
* Meeting minutes with attendance lists or SA meeting notes or assessments of the activities and recorded in the project repository.
* Status report, email or memo containing statements that confirmation has been performed with date (a checklist of confirmations could be used to record when each confirmation has been done!).
* Signatures on SA reviewed or witnessed products or activities, or
* Status report, email or memo containing a short summary of information gained by performing the activity. Some examples of using a “short summary” as objective evidence of a confirmation are:
  + To confirm that: “IV&V Program Execution exists”, the summary might be: IV&V Plan is in draft state. It is expected to be complete by (some date).
  + To confirm that: “Traceability between software requirements and hazards with SW contributions exists”, the summary might be x% of the hazards with software contributions are traced to the requirements.
* The specific products listed in the Introduction of 8.16 are also objective evidence as well as the examples listed above.

## 8.1 Objective Evidence to Be Collected

### 8.1.1 Classification Documentation:

* Classification assignments for all software systems and subsystems, including:
  + Assigned classifications (e.g., Class A, B, C, D, E, F).
  + Classification rationale (aligned with NPR 7150.2 Appendix D definitions).
  + Safety-critical software designations per **NASA-STD-8739.8**.

### 8.1.2 Evidence of SA Involvement in Classification:

* Records of SA concurrence with the project’s software classifications, such as:
  + Signed documentation of classification agreement between SA and software engineering.
  + Meeting minutes or communications showing collaborative discussions on software classification.

### 8.1.3 Evidence of Escalation (if applicable):

* If disagreements arose, evidence of escalation through ETA and SMA TA chains:
  + Discrepancy reports or formal notifications to the appropriate authorities.
  + Resolutions and artifacts showing resulting classification adjustments.
