# 7.02 - Classification and Safety-Criticality

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695612. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality

7.02 - Classification and Safety-Criticality

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695612)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695612&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Classification Descriptions](#tabs-2)
* [3. Classification Examples](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Lessons Learned](#tabs-5)

# 1. Introduction

NASA has two significant independent classification schemas for software:

1. a software engineering classification as described in NPR 7150.2 [083](#_tabs-<p>4</p>), NASA Software Engineering Requirements, Appendix D, and
2. the software can be determined to be safety-critical software as described in NASA-STD-8739.8 [278](#_tabs-<p>4</p>), Software Assurance and Software Safety Standard.

[SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) describes the relationship between these classifications. For a given system or subsystem, the software is expected to be uniquely defined within a single classification pair (software engineering classification X software safety definition). Knowing this pair determines the minimal set of software requirements from NPR 7150.2 needing to be addressed (via Appendix C of NPR 7150.2) by the project's software team. See also Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix).

## 1.1 Software Classifications

The classifications table below comes directly from NPR 7150.2D, paragraph P.2 APPLICABILITY:

**Figure 1. NASA software classification structure**

#### **NASA-Wide Software Classifications**

#### **Class AHuman-Rated Space Software Systems**

#### **Class B      Non-Human Space-Rated Software Systems or Large-Scale Aeronautics Vehicles**

#### **Class C      Mission Support Software or Aeronautic Vehicles, or Major Engineering/Research Facility Software**

#### **Class D****Basic Science/Engineering Design and Research and Technology Software**

#### **Class E       Design Concept, Research, Technology, and General Purpose Software**

#### **Class F       General Purpose Computing, Business, and IT Software**

#### ***Notes: It is not uncommon for a project to contain multiple systems and subsystems having different software classes.***

# 1.2 Software Safety Criticality

The description of Safety-Critical Software comes directly from NASA-STD-8739.8B:

**8739.8B para 3.2 Definitions: Safety-Critical Software**

**Safety-Critical Software**.  Software is classified as safety-critical if the software is determined by and traceable to a hazard analysis. Software is classified as safety-critical if it meets at least one of the following criteria:

a. Causes or contributes to a system hazardous condition/event,  
b. Controls functions identified in a system hazard,  
c. Provides mitigation for a system hazardous condition/event,  
d. Mitigates damage if a hazardous condition/event occurs,  
e. Detects, reports, and takes corrective action if the system reaches a potentially hazardous state.

Software is classified as safety-critical if the software is determined by and traceable to hazard analysis. See Appendix A for guidelines associated with addressing software in hazard definitions. See [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software). Other independent means of protection (software, hardware, barriers, or administrative) should be considered as part of the system hazard definition process.

Defining software safety criticality involves the determination of whether the software is performing a safety-critical function, including verification of safety-critical software, hardware, or operations component, subsystem, or system.

### **All Safety-critical software has to be classified as Class D or higher.**

## 1.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 2. Classification Descriptions

Software classification determines NPR 7150.2 [083](#_tabs-<p>4</p>) requirement applicability for a specific system or sub-system. As stated in NPR 7150.2: "These definitions are based on 1) usage of the software with or within a NASA system, 2) criticality of the system to NASA's major programs and projects, 3) extent to which humans depend upon the system, 4) developmental and operational complexity, and 5) the extent of the Agency's investment." Classes A through E cover engineering-related software. Class F covers Business and Information Technology Infrastructure Software. Using the Requirements Mapping Matrix, the number of applicable requirements and their associated rigor are scaled back for lower software classes. Situations in which a project contains separate systems and subsystems having different software classes are not uncommon.

For a given system or subsystem, software is expected to be uniquely defined within a single class. If more than one software class appears to apply, then assign the higher of the classes to the system/subsystem. Any potential discrepancies in classifying software within Classes A through-- E are to be resolved using the definitions and the five underlying factors listed in the previous paragraph. Engineering and SMA provide dual TA chains for resolving classification issues. The NASA Chief Engineer is the ultimate TA for software classification disputes concerning definitions in this NPR.

The material in this table is from Appendix D of NPR 7150.2.

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

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Classification Examples

The following chart lists projects by software classification as examples of how software has been classified for Class A-E software. The project can use these examples to help inform their classification activities.

|  |  |
| --- | --- |
| **Projects** | **Software Classification** |
| CCP (Commercial Crew Program) | A |
| Exploration Ground Systems | A |
| Extravehicular Activity and Human Surface Mobility Program | A |
| Flight Software on the Commercial Crew Programs | A |
| Free Flyer Project | A |
| Gateway | A |
| Ground Systems Development and Operations (GSDO) Program - End-to-End Command and Control | A |
| Human Landing System (HLS) | A |
| International Space Station (ISS) Avionics & Software Critical Flight Software | A |
| Multi-Purpose Crew Vehicle (EFT-1) Flight Software | A |
| Multi-Purpose Crew Vehicle (EM-1) Flight Software | A |
| Multi-Purpose Crew Vehicle (EM-2) Flight Software | A |
| Orion Flight Software | A |
| PPE (power and propulsion element) | A |
| Space Launch System Flight Software | A |
| Space Shuttle Flight Software | A |
| ACCESS (Advanced Communications Capabilities for Exploration and Science Systems) | B |
| Chandra Space Telescope Flight Software | B |
| Climate Absolute Radiance and Refractivity Observatory (CLARREO) | B |
| CloudSat and the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Flight Software | B |
| Copernicus Polar Ice and Snow Topography Altimeter CRISTAL (ESA Mission) | B |
| core Flight System (cFS) | B |
| Cyclone Global Navigation Satellite System (CYGNSS) Flight Software | B |
| DAVINCI (Deep Atmosphere Venus Investigation of Noble gases, Chemistry, and Imaging (DAVINCI) mission) | B |
| Dragonfly | B |
| Europa Clipper | B |
| Flight Software on Various Small Satellite Missions (e.g., EDSN, BioSentinel, EuCROPIS) | B |
| GDC (Geospace Dynamics Constellation) | B |
| Geostationary Operational Environmental Satellites (GOES-R) Flight Software | B |
| GeoXO Geostationary Extended Observations (NOAA mission) | B |
| GLIDE (Global Lyman-alpha Imagers of the Dynamic Exosphere) | B |
| Global Hawk Aircraft | B |
| GMSEC (Goddard Mission Services Evolution Center) | B |
| Gravity Recovery and Climate Experiment (GRACE) Flight Software | B |
| HelioSwarm | B |
| HST | B |
| Ice, Cloud, and Land Elevation Satellite (ICESat II) Flight Software | B |
| IMAP (APL- Interstellar Mapping and Acceleration Probe) | B |
| InSight (Interior Exploration using Seismic Investigations, Geodesy and Heat Transport) Flight Software | B |
| Investigation of Convective Updrafts (INCUS) | B |
| Ionospheric Connection (ICON) Explorer Flight Software | B |
| James Webb Space Telescope (JWST) Flight Software | B |
| Joby S4 Aircraft | B |
| Joint Polar Satellite System (JPSS (Ground)) | B |
| Joint Polar Satellite System (JPSS) Flight Software | B |
| Kepler: Flight Software | B |
| Kepler: Science Pipeline Software | B |
| Landsat Next | B |
| Laser Communication Rely Demo | B |
| Low Boom Flight Demonstrator X-59 | B |
| Magnetospheric Multiscale (MMS) | B |
| Mars Sample Return | B |
| Mars Surface Mission/Mars 2020 | B |
| MSL | B |
| NAVIGATION TECHNOLOGY SATELLITE – 3 (NTS-3) Air Force Research Lab Project | B |
| Neo Surveyor (space-based infrared telescope) | B |
| Origins, Spectral Interpretation, Resource Identification, Security, Regolith Explorer (OSIRIS-REx) | B |
| PACE (Plankton, Aerosol, Cloud, ocean Ecosystem) | B |
| PSYCHE | B |
| Quicksounder (NOAA) | B |
| Roman Space Telescope | B |
| Solar Probe Plus (SPP) | B |
| Space Network Ground Segment Sustainment (SGSS) | B |
| SphereX | B |
| Starling (A Multi-CubeSat Mission to Demonstrate Autonomous Swarm Technologies) | B |
| Stratospheric Aerosol and Gas Experiment (SAGE III) Flight Software, Experiment on ISS | B |
| SunRise (CubeSat/SmallSat) | B |
| Sustainable Flight Demonstrator X-66 | B |
| SWFO (Space Weather Follow On) | B |
| Transiting Exoplanet Survey Satellite (TESS) | B |
| Tropospheric Emissions: Monitoring of Pollution (TEMPO) Flight Software | B |
| 14x22-Foot Subsonic Wind Tunnel | C |
| 20-foot Vertical Spin Tunnel Rotary Balance Control System, Fan Control System | C |
| 8 foot High Temperature Tunnel | C |
| A-1 Control System | C |
| Advanced Microgravity Combustion Experiment (ACME) | C |
| Air traffic management systems | C |
| Airborne Collision Avoidance System For Unmanned Aircraft (ACAS Xu) | C |
| Airborne Synthetic Aperture Radar | C |
| AirSTAR (Flight Software) | C |
| AOS Deployable Optical Receiver Aperture (DORA) | C |
| Archive Next Generation software (ANGe) | C |
| ARCSTONE | C |
| Astrobee Flight and Ground Software | C |
| Atmosphere Observing System (AOS) | C |
| Autonomous Satellite Technology for Resilient Applications (ASTRA) | C |
| B1221 Research Complex | C |
| B1230 Data Acquisition Systems Laboratory | C |
| Balloon Flight software and balloon flight experiment software | C |
| CADRE (Cooperative Autonomous Distributed Robotic Exploration) | C |
| CAPE (Cubesat Application for Planetary Entry Missions) | C |
| Clouds and the Earth's Radiant Energy System (CERES FM5 on NPP) | C |
| Clouds and the Earth's Radiant Energy System (CERES FM6 FVTS Simulator) | C |
| Clouds and the Earth's Radiant Energy System (CERES FM6 on NPOESS) | C |
| CloudSat and the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Science Level 1, 2  and 3 Code | C |
| Cockpit Motion Facility | C |
| Combined Loads Test System | C |
| Compressor Station Automation Project | C |
| CubeSat mission software | C |
| Data acquisition and control systems for wind tunnels | C |
| E-1 Control System | C |
| E-3 Control System | C |
| Flow Boiling Condensation Experiment (FBCE) | C |
| Free-flying unmanned aerial vehicles | C |
| General Aviation Main (GAMain) | C |
| Geosynchronous Littoral Imaging and Monitoring Radiometer (GLIMR) | C |
| Geosynchronous Littoral Imaging and Monitoring Radiometer (GLIMR) | C |
| Ground-based software used to operate a major facility telescope | C |
| HDTN (High-Rate Delay Tolerant Networking) | C |
| HGS | C |
| High-Pressure Gas Facility Supervisory Control System | C |
| High-Pressure Industrial Water Plant (HPIW) Control System | C |
| High-energy Ion Telescope (HIT) | C |
| High-fidelity motion-based simulators | C |
| HNSCSS | C |
| HPGF Air Compressor | C |
| Lang+B56:B80ley Standard Real-Time Simulation and Core Vehicle Models (LaSRS Core) | C |
| Langley Data Center Atmospheric Flight and Entry Systems Cluster | C |
| LaRC Transonic Dynamics Tunnel ABDAS Upgrade | C |
| LaRC Transonic Dynamics Tunnel FAS Upgrade | C |
| Laser Interferometer Space Antenna (LISA) (ESA Mission) | C |
| LCRNS (Lunar Communications Relay and Navigation Systems) | C |
| LEIA (Lunar Explorer Instrument for Space Biology Applications) | C |
| LIBERA (LASP instrument) | C |
| Lunar Experiment Survival System and Handling (LESSH) | C |
| Multi-Mission Ground Systems & Services (MGSS) | C |
| NASA Class D payloads | C |
| NASA Data Acquisition System (NDAS) - High Speed and Low-Speed Data Acquisition (SSC, WSTF, MSFC, and GRC) | C |
| NASA Data Acquisition System (NDAS) Redline System at WSTF | C |
| NASA Data Acquisitions System (Ndas) | C |
| National Transonic Facility | C |
| Near Earth Magnetometer Instrument in a Small Integrated System (NEMESIS) | C |
| NSN (Near Space Network) | C |
| Olympus (multi-purpose construction system primarily using local Lunar and Martian resources) | C |
| Primary/major science data collection storage and distribution systems | C |
| Radiation Budget Instrument (RBI) | C |
| Radiation Dosimetry Experiment (RAD-X) | C |
| Radio Frequency Mass Gauge (RF Mass Gauge) | C |
| Rocket engine test stands | C |
| Rodent Research (ISS payload) | C |
| Roman CGI | C |
| SAFFIRE (Spacecraft Fire Safety Demonstration Project) | C |
| SmallSat mission software | C |
| SMBA (NOAA's Sounder for Microwave-Based Applications) | C |
| SOFIA Science Pipeline | C |
| Sounding rocket experiments or payload software | C |
| Sounding Rockets | C |
| Space Communications and Navigation (SCaN) Testbed | C |
| Space Launch System System Integration Lab (SIL) Ground Software | C |
| Spacecraft Fire Safety (Saffire) | C |
| Spacecraft Fire Safety Demonstration | C |
| Steam Distribution System (Steam Plant) | C |
| Stratospheric Aerosol and Gas Experiment (SAGE III) Ground Software, Experiment on ISS | C |
| Stratospheric Aerosol and Gas Experiment (SAGE) III on ISS | C |
| Stratton Road Substation | C |
| Structures Laboratory | C |
| Synthetic aperture radar VenSAR | C |
| System Power Analysis for Capability Evaluation | C |
| Test Stand Control System for EUS | C |
| Total and Spectral Solar Irradiance Sensor TSIS-2 | C |
| Transiting Exoplanet Survey Satellite (TESS) Science Processing Operations Center (SPOC) Software | C |
| Transonic Dynamics Tunnel (TDT) Facility Automation System Upgrade | C |
| UAS projects | C |
| UAVs in public airspace or over-controlled ranges; | C |
| Vacuum chambers | C |
| Vacuum Facility #5 (VF-5) Control Software | C |
| Various Health and Human Countermeasures Projects | C |
| ZBOT-NC, IVGEN Mini, PBRE-WRS, and MAMS | C |
| 20W/20K Cryo | D |
| Advanced Spacecraft Integration and System Test (ASIST) | D |
| Advanced Stirling Radio-Isotope Generator | D |
| Aeronautics Research Mission Directorate Test Data Portal | D |
| Aerosol Wind Profiler (AWP) | D |
| Airborne Instrumentation for Real-world Video of Urban Environments | D |
| Airborne Location Integrating Geospatial Navigation Systems | D |
| Airspace and Traffic Operations Simulations (ATOS) | D |
| AirSTAR (Phase V Ground Facility Software) | D |
| Arc Jet Modernization | D |
| COBRA Data Acquisition System | D |
| Cognitive Comm (may contain a further portfolio of projects) | D |
| Consultative Committee for Space Data Systems (CCSDS) | D |
| Deterministic and Statistical Link Budget Simulator (DSLB) | D |
| DTN (Delay/Disruption Tolerant Networking) | D |
| EMTG (Evolutionary Mission Trajectory Generator (EMTG)) | D |
| Environmental Control System for Exploration Upper Stage (EUS) | D |
| Flutter and Strength Optimization Program for Lifting-Surface (FASTOP) | D |
| Glenn Extreme Environment Rig Control System | D |
| GlennICE (ICE models) | D |
| Goddard Enhanced Onboard Navigation System (GEONS) | D |
| GRC Facility Software Safety | D |
| Ground Recorder Systems | D |
| IMPACT (overseeing the lifecycle of Earth science data to maximize the scientific return) | D |
| Integrated Test and Operations System (ITOS) | D |
| INvestigation of Convective Updrafts (INCUS) | D |
| LaRC Facilities projects | D |
| LaRC Science and Research projects | D |
| Mosaic (Multidisciplinary drifting Observatory for the Study of Arctic Climate) | D |
| Multiple Axis Space Test Inertia Facility (MASTIF) | D |
| NDAS Video (NVID) in the E-Complex | D |
| NGRTG (Next-Generation Radioisotope Thermoelectric Generator) | D |
| Optimal Trajectories by Implicit Simulation (OTIS) | D |
| Pathfinding for Autonomous Airspace and Vehicles | D |
| Regenerative Fuel Cells | D |
| RFMG (Radio Frequency Mass Gauge (RFMG)) | D |
| Safeguard Software Managed Autonomously Restricted Terrain (SMART) | D |
| Stereo CAmeras for Lunar Plume-Surface Studies (SCALPSS) | D |
| Suite of computational | D |
| Various Facility Data Acquisition Systems | D |
| Various Facility Industrial Control System Software | D |
| Various Models and Simulation Software | D |
| Various Research Software Projects | D |
| Various SCAN Program Tools | D |
| Vertical Motion Simulator | D |
| Earth Independent Operations (EIO) | E |
| Global Integrated Design Environment (GLIDE) | E |
| Unmanned Aircraft Systems Integration in the National Airspace System project, or UAS in the NAS, ADS-B | E |
| Various Research Software Projects | E |

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-070)

  [Volume 5, NASA Enterprise Architecture: NASA To-Be Architecture, Approach to Design and Implementation,](https://prod.nais.nasa.gov/eps/eps_data/117920-OTHER-003-005.pdf "Click to open in new window")

  Version 3.0, NASA Office of the Chief Technology Officer, 2004. No Longer Available
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-246)

  [Man-Systems Integration Standards,](https://msis.jsc.nasa.gov/ "Click to open in new window")

  NASA-STD-3000, Volume I, Revision B, NASA, 1995. See also Man-Systems Integration Standards, NASA-STD-3000, Volume II
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-498)

  [NASA Space Flight Human-System Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-3001-vol-2 "Click to open in new window")

  NASA-STD\_3001, Volume 2: Human Factors, Habitability, and Environmental Health, Revision A, 2015.

  

## 4.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 4.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) |

## 4.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Center Libraries](https://nen.nasa.gov/web/software/wiki)      * [Classification](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Classification) |

## 4.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 5. Lessons Learned

### 5.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 5.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
