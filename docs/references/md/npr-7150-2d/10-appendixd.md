# NPR 7150.2D — AppendixD

> Source: https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixD
> Page title: NPR 7150.2D - AppendixD
> Machine conversion; tables may be flattened. SWE-NNN identifiers are authoritative.

# Appendix D. Software Classifications

D.1 The applicability of requirements in this directive to specific systems and subsystems containing software is determined through the use of the NASA-wide software classification structure. These definitions are based on: (1) usage of the software with or within a NASA system, (2) criticality of the system to NASA’s major programs and projects, (3) extent to which humans depend upon the system, (4) developmental and operational complexity, and (5) extent of the Agency’s investment. Classes A through E cover engineering-related software. Class F cover Business and Information Technology Infrastructure Software. Using the Requirements Mapping Matrix, the number of applicable requirements and their associated rigor are scaled back for lower software classes. Situations in which a project contains separate systems and subsystems having different software classes are not uncommon.

D.2 For a given system or subsystem, software is expected to be uniquely defined within a single class. If more than one software class appears to apply, then assign the higher of the classes to the system/subsystem. Any potential discrepancies in classifying software within Classes A through-- E are to be resolved using the definitions and the five underlying factors listed in the previous paragraph. Engineering and SMA provide dual TA chains for resolving classification issues. The NASA Chief Engineer is the ultimate TA for software classification disputes concerning definitions in this NPR.

---

**Class A: Human Rated Space Software Systems**

**a. Definition:**

1. Human Space Flight Software Systems\*: Ground and flight software systems developed or operated by or for NASA needed to perform a primary mission objective of human space flight and directly interact with human space flight systems. Limited to software required to perform “vehicle, crew, or primary mission function,” as defined by software that is:

(a) Required to operate the vehicle or space asset (e.g., spacesuit, rover, or outpost), including commanding of the vehicle or asset.

(b) Required to sustain a safe, habitable1 environment for the crew.

(c) Required to achieve the primary mission objectives.

(d) Required to directly prepare resources (e.g., data, fuel, power) that are consumed by the above functions.

\*Includes software involving launch, on-orbit, in space, surface operations, entry, descent, and landing.

1 Current standards that address habitability and environmental health, including atmospheric composition and pressure, air, and water quality and monitoring, acceleration, acoustics, vibration, radiation, thermal environment, combined environmental effects, and human factors, are documented in NASA-Standard-3001 Volume 1, Space Flight Human-System Standard: Crew Health, NASA-Standard-3001 Volume 2, Space Flight Human-System Standard: Human Factors, Habitability, and Environmental Health, FAA HFDS - Human Factors Design Standard.

**b. Examples:**

Examples of Class A software (human-rated space flight) include, but are not limited to, the mission phases listed below.

1. During Launch:

Abort modes and selection; separation control; range safety; crew interface (display and controls); crew escape; critical systems monitoring and control; guidance, navigation, and control; and communication and tracking.

2. On-Orbit/In Space:

Extravehicular activity (EVA); control of electrical power; payload control (including suppression of hazardous satellite and device commands); critical systems monitoring and control; guidance, navigation, and control; life support systems; crew escape; rendezvous and docking; failure detection, isolation and recovery; communication and tracking; and mission operations.

3. On Ground:

Pre-launch and launch operations; Mission Control Center (and Launch Control Center) front-end processors; spacecraft commanding; vehicle processing operations; re-entry operations; flight dynamics simulators used for ascent abort calls; and launch and flight controller stations for human-crewed spaceflight.

4. Entry, Descent, and Landing (EDL):

Command and control; aero-surface control; power; thermal; fault protection; and communication and tracking.

5. Surface Operations:

Planet/lunar surface EVA and communication and tracking.

**c. Exclusions:**

Class A does not include:

1. Software that happens to fly in space but is superfluous to mission objectives (e.g., software contained in an iPod carried on board by an astronaut for personal use); or

2. Software that exclusively supports aeronautics, research and technology, and science conducted without space flight applications; or

3. Systems (e.g., simulators, emulators, facilities) used to test Class A systems containing software in a development environment.

---

**Class B: Non-Human Space Rated Software Systems or Large Scale Aeronautics Vehicles**

**a. Definitions:**

1. Space Systems involve flight and ground software that should perform reliably to accomplish primary mission objectives or major function(s) in non-human space rated systems. Included is software involving launch, on orbit, in space, surface operations, entry, descent, and landing. These systems are limited to software that is:

(a) Required to operate the vehicle or space asset (e.g., orbiter, lander, probe, flyby spacecraft, rover, launch vehicle, or primary instrument) such as commanding of the vehicle or asset;

(b) Required to achieve the primary mission objectives; or

(c) Required to directly prepare resources (data, fuel, power) that are consumed by the above functions.

2. Aeronautic Vehicles include large scale2 aeronautic software systems unique to NASA in which the software:

(a) Is integral to the control of an airborne vehicle;

(b) Monitors and controls the cabin environment; or

(c) Monitors and controls the vehicle’s emergency systems.

This definition includes software for vehicles classified as “test,” “experimental,” or “demonstration” that meets the above definition for Class B software. Also included are systems in a test or demonstration where the software’s known and scheduled intended use is to be part of a Class A or B software system.

2 Large-scale (life cycle cost exceeding $250M) fully integrated technology development system – see NPR 7120.8.

**b. Examples:**

Examples of Class B software include, but are not limited to:

1. Space, Launch, Ground, EDL, and Surface Systems:

Propulsion systems; power systems; guidance navigation and control; fault protection; thermal systems; command and control ground systems; planetary/lunar surface operations; hazard prevention; primary instruments; science sequencing engine; simulations that create operational EDL parameters; subsystems that could cause the loss of science return from multiple instruments; flight dynamics and related data; and launch and flight controller stations for non-human spaceflight.

2. Aeronautics Vehicles (Large Scale NASA Unique):

Guidance, navigation, and control; flight management systems; autopilot; propulsion systems; power systems; emergency systems (e.g., fire suppression systems, emergency egress systems, emergency oxygen supply systems, traffic/ground collision avoidance system); and cabin pressure and temperature control.

**c. Exclusions:**

Class B does not include:

1. Software that exclusively supports non-primary instruments on non-human space rated systems (e.g., low-cost, non-primary, university supplied instruments); or

2. Systems (e.g., simulators, emulators, facilities) used in testing Class B systems containing software in a development environment; or

3. Software for NASA Class D payloads, as defined in NPR 8705.4.

---

**Class C: Mission Support Software or Aeronautic Vehicles, or Major Engineering/Research Facility Software**

**a. Definitions:**

1. Space Systems include the following types of software:

(a) Flight or ground software necessary for the science return from a single (non-primary) instrument;

(b) Flight or ground software used to analyze or process mission data;

(c) Other software for which a defect could adversely impact the attainment of some secondary mission objectives or cause operational problems;

(d) Software used for the testing of space assets;

(e) Software used to verify system requirements of space assets by analysis; or

(f) Software for space flight operations not covered by Class A or B software.

2. Aeronautic Vehicles include systems for non-large scale aeronautic software systems in which the software:

(a) Is integral to the control of an airborne vehicle;

(b) Monitors and controls the cabin environment; or

(c) Monitors and controls the vehicle’s emergency system.

Also included are systems on an airborne vehicle (including large-scale vehicles) that acquire, store, or transmit the official record copy of flight or test data.

3. Major Engineering/Research Facility is systems that operate a major facility for research, development, test, or evaluation (e.g., facility controls and monitoring, systems that operate facility-owned instruments, apparatus, and data acquisition equipment).

4. Sounding Rockets and Sounding Rocket payloads.

5. Software for NASA Class D payloads, as defined in NPR 8705.4.

**b. Examples:**

Examples of Class C software include, but are not limited to:

1. Space Systems:

Software that supports prelaunch integration and test; mission data processing and analysis; analysis software used in trend analysis and calibration of flight engineering parameters; primary/major science data collection storage and distribution systems (e.g., Distributed Active Archive Centers); simulators, emulators, or facilities used to test Class A, B, or C software in development; integration and test environments; software used to verify system-level requirements associated with Class A, B, or C software by analysis (e.g., guidance, navigation, and control system performance verification by analysis); simulators used for mission training; software employed by network operations and control (which is redundant with systems used at tracking complexes); command and control of non-primary instruments; ground mission support software used for secondary mission objectives, real-time analysis, and planning (e.g., monitoring, consumables analysis, mission planning); CubeSat mission software; SmallSat mission software; sounding rocket software and sounding rocket experiments or payload software; and all software on NASA Class D payloads, as defined in NPR 8705.4 to examples of Class C software.

2. Aeronautics Vehicles:

Guidance, navigation, and control; flight management systems; autopilot; propulsion systems; power systems; emergency systems (e.g., fire suppression systems, emergency egress systems, emergency oxygen supply systems, traffic/ground collision avoidance system); cabin pressure and temperature control; in-flight telescope control software; aviation data integration systems; automated flight planning systems and primary/major science data collection storage and distribution systems (e.g., Distributed Active Archive Centers); sounding rockets and sounding rocket experiments or payload software; flight software for free-flying unmanned aerial vehicles (UAVs) in public airspace or over controlled ranges; Balloon Flight software and balloon flight experiment software, and all software on NASA Class D pay loads, as defined in NPR 8705.4.

3. Major Engineering/Research Facility:

Major Center facilities; data acquisition and control systems for wind tunnels, vacuum chambers, and rocket engine test stands; ground-based software used to operate a major facility telescope; and major aeronautic applications facilities (e.g., air traffic management systems; high fidelity motion based simulators).

**c. Exclusions:**

Class C does not include:

Systems unique to research, development, test, or evaluation activities in a major engineering/research facility or airborne vehicle in which the system is not part of the facility or vehicle and does not impact the operation of the facility or vehicle.

---

**Class D: Basic Science/Engineering Design and Research and Technology Software**

**a. Definitions:**

1. Basic Science/Engineering Design includes:

(a) Ground software that performs secondary science data analysis;

(b) Ground software tools that support engineering development;

(c) Ground software or software tools used for informal testing of software systems;

(d) Ground software tools that support mission planning or formulation;

(e) Ground software that operates a research, development, test, or evaluation laboratory (i.e., not a major engineering/research facility); or

(f) Ground software that provides decision support for non-mission critical situations.

2. Airborne Vehicle Systems include:

(a) Software whose anomalous behavior would cause or contribute to a failure of system function resulting in a minor failure condition for the airborne vehicle (e.g., DO-178C, Software Considerations in Airborne Systems and Equipment Certification, “Class D”);

(b) Software whose anomalous behavior would cause or contribute to a failure of system function with no effect on airborne vehicle operational capability or pilot workload (e.g., DO-178C, “Class E”); or

(c) Ground software tools that perform research associated with airborne vehicles or systems.

3. Major Engineering/Research Facility related software includes research software that executes in a major engineering/research facility but is independent of the operation of the facility.

**b. Examples:**

Examples of Class D software include, but are not limited to:

1. Basic Science and Engineering Design:

Engineering design and modeling tools (e.g., computer-aided design and computer-aided manufacturing (CAD/CAM), thermal/structural analysis tools); project assurance databases (e.g., problem reporting, analysis, and corrective action system, requirements management databases); propulsion integrated design tools; integrated build management systems; inventory management tools; probabilistic engineering analysis tools; test stand data analysis tools; test stand engineering support tools; experimental flight displays evaluated in a flight simulator; forecasts and assimilated data products; and tools used to develop design reference missions to support early mission planning.

2. Airborne Vehicles:

Software tools for designing advanced human-automation systems; experimental synthetic-vision display; and cloud-aerosol light detection and ranging installed on an aeronautics vehicle; flight software for physically constrained UAVs such as UAVs on tethers, within cages, or used in indoor labs; and experimental UAV payloads with minor consequences of failure.

**c. Exclusions:**

Class D does not include:

1. Software that can impact primary or secondary mission objectives or cause loss of data that is generated by space systems;

2. Software that operates a major engineering/research facility;

3. Software that operates an airborne vehicle; or

4. Flight software (i.e., software that meets the flight portions of Class A, B, or C Software Classifications).

---

**Class E: Design Concept, Research, Technology, and General Purpose Software**

**a. Definitions:**

1. Software developed to explore a design concept or hypothesis but not used to make decisions for an operational Class A, B, or C system or a to-be-built Class A, B, or C system.

2. Software used to perform minor analyses of science or experimental data.

3. A defect in Class E software may affect the productivity of a single user or small group of users but generally will not affect mission objectives or system safety. Class E software cannot be safety-critical software. If the software is classified as safety-critical software, then it has to be classified as Class D or higher.

4. Class E software runs in a general-purpose computing environment or a board top environment. Class E software does not support ground tests, flight tests, or operations.

**b. Examples:**

Examples of Class E software include, but are not limited to, parametric models to estimate performance or other attributes of design concepts; software to explore correlations between data sets; line of code counters; file format converters; and document template builders. Class E can include prototypes of flight and ground systems, developed at minimal cost, in the spirit of “exploring a design concept.” Once the design concept is demonstrated, and a program agrees to incorporate it for flight or ground operational use, or for an in-flight test of the technology, then the software should be upgraded to its appropriate classification, based on the operational (or in-flight test) use case. Class E software includes, but is not limited to, software such as word processing applications, spreadsheet applications, and presentation applications.

**c. Exclusions:**

Class E does not include:

1. Flight systems (i.e., software that meets the flight portions of Class A, B, C, or D Software Classifications);

2. Software developed by or for NASA to directly support an operational system (e.g., human-rated space system, robotics spacecraft, space instrument, airborne vehicle, major engineering/research facility, mission support facility, and primary/major science data collection storage and distribution systems);

3. Software developed by or for NASA to be flight qualified to support an operational system;

4. Software that directly affects primary or secondary mission objectives;

5. Software that can adversely affect the integrity of engineering/scientific artifacts;

6. Software used in technical decisions concerning operational systems, or systems being developed for operation;

7. Software that has an impact on operational vehicles; or

8. Software that is safety-critical.

Business and Information Technology Infrastructure Software

---

**Class F: General Purpose Computing, Business, and IT Software**

**a. Definition:**

General purpose computing Business and IT software used in support of the Agency, multiple Centers, multiple programs/projects, single Centers/projects, or locally deployed General Purpose Infrastructure To-Be Component of the NASA Enterprise Architecture. These software applications are generally used to support voice, wide-area network, local area network, video, data centers, cloud computing, information management, business and IT application services (e.g., Finance, Logistics, Human Capital, Procurement), messaging and collaboration, and public Web. A defect in Class F software is likely to affect the productivity of multiple users across a single geographic location or several geographic locations and may affect mission objectives or system safety. Mission objectives can be cost, schedule, or technical objectives for any work that the Agency or a Center performs.

**b. Examples:**

Examples of Class F software include, but are not limited to, Agency-wide enterprise applications (e.g., WebTADS, SAP, CONCURGov, ePayroll, Business Warehouse), Center-specific software, or specific Web applications, including mobile applications; Agency-wide educational outreach software; software in support of the NASA-wide area network; and the NASA Web portal.

  

|  |
| --- |
| | [TOC](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=main) | [Preface](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Preface) | [Chapter1](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter1) | [Chapter2](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter2) | [Chapter3](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter3) | [Chapter4](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4) | [Chapter5](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter5) | [Chapter6](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter6) | [AppendixA](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixA) | [AppendixB](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixB) | [AppendixC](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixC) | [AppendixD](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixD) | [AppendixE](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixE) | [ALL](displayAll.cfm?Internal_ID=N_PR_7150_002D_&page_name=ALL) | |
|  |
| | [NODIS Library](main_lib.html) | [Program Formulation(7000s)](lib_docs.cfm?range=7) | [Search](adv_search.cfm) | |
