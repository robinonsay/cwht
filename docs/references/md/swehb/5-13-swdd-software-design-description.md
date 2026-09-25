# 5.13 - SwDD - Software Design Description

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695674. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description

5.13 - SwDD - Software Design Description

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695674)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695674&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Minimum Recommended Content](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

Return to [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)

# 1. Minimum Recommended Content

Minimum recommended content for a Software Design Description. 

a. CSCI -wide design decisions/trade decisions.

b. CSCI architectural design.

c. CSCI decomposition and interrelationship between components:

1. CSCI components:  
   1. Description of how the software item satisfies the software requirements, including algorithms, data structures, and functional decomposition.
   2. Software item I/O description.
   3. Static/architectural relationship of the software units.
   4. Concept of execution, including data flow, control flow, and timing.
   5. Requirements, design and code traceability.
   6. CSCI's planned utilization of computer hardware resources.
2. Rationale for software item design decisions/trade decisions including assumptions, limitations, safety and reliability related items/concerns or constraints in design documentation.
3. Interface design.

The documentation of the architectural design of a software system identifies and describes the architectural elements of the software, the external interfaces, and the interfaces between elements. The description includes element responsibilities (constraints on inputs and guarantees on outputs), and constraints on how the elements interact (such as message and data sharing protocols). The architectural design documentation includes multiple views of the architecture and identifies and supports the evaluation of the key quality attributes of the planned software product. The key quality attributes of the software will depend on the mission in which the software is to be used and the manner in which it is to be developed and deployed. They will usually include: performance, availability, maintainability, modifiability, security, testability and usability (operability.)

# 2. Rationale

The Software Design Description describes the design of a computer software configuration item (CSCI). It describes the CSCI-wide design decisions, the CSCI architectural design, and the detailed design needed to implement the software. The software design process transforms the software requirements into a structured, organized set of information appropriate for implementing in code. This design is captured in the software design description (SwDD), making the SwDD a critical document in the software development process.

# 3. Guidance

When creating the software design description (SwDD), the following minimum content is included. If the content is included in another document or tool, such as separate trade study documents, interface design documents, modeling or simulation tools, or data dictionaries, those documents or tools may be referenced in the SwDD. See also [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) and [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design).

## 3.1 CSCI-wide design decisions/trade decisions

It is important to document decisions made during the design process, as well as the reasons those decisions were made. (See *Rationale for software item design* (Item 2 under *CSCI decomposition and interrelationship between components*) guidance below.) This information is useful for the implementation phase, as well as future software maintenance activities. CSCI-wide design decisions are “decisions about the CSCI's behavioral design (how it will behave, from a user's point of view, in meeting its requirements, ignoring internal implementation) and other decisions affecting the selection and design of the software units that make up the CSCI.” [490](#_tabs-<p></p>) Glenn Research Center's (GRC's) GRC-SW-TPLT-SDD, Software Design Description Template, suggests considering the following when capturing "decisions about the CSCI's behavioral design (how it will behave from a user's point of view, in meeting its requirements, and ignoring internal implementation) and other decisions affecting the selection and design of the software units that make up the CSCI":

* Capture design decision dependencies on system states or modes. [096](#_tabs-<p></p>)
* Capture design decisions "regarding inputs the CSCI will accept and outputs it will produce, including interfaces with other systems, hardware configuration items (HWCIs), CSCIs, and users." [096](#_tabs-<p></p>)
* Capture design decisions "on CSCI behavior in response to each input or condition, including actions the CSCI will perform, response times, and other performance characteristics, description of physical systems modeled, selected equations, algorithms, or rules, and handling of invalid inputs or conditions." [096](#_tabs-<p></p>)
* Capture design decisions "on how databases and data files will appear to the user." [096](#_tabs-<p></p>)
* Capture the "selected approach to meeting safety, security, and privacy requirements." [096](#_tabs-<p></p>)
* Capture design decisions "made in response to requirements, such as selected approach to providing required flexibility, availability, and maintainability." [096](#_tabs-<p></p>)
* If a design decision depends upon system states or modes, indicate this dependency. [490](#_tabs-<p></p>)
* Make Decisions based on trade studies, including the options considered or a reference to the document(s) that capture the trade study information.
* Capture decisions to use open source components along with a description of the components and their planned use.
* Capture decisions to reuse software components along with a description of those components and their planned use.

Capture decisions to use commercial off the shelf (COTS) components along with a description of those components and their planned use.

## 3.2 CSCI architectural design

Goddard Space Flight Center's (GSFC's) 580-STD-077-01, Requirements for Minimum Contents of Software Documents, notes that "The architectural design documentation includes multiple views of the architecture and identifies and supports the evaluation of key quality attributes of the planned software product. The key quality attributes of the software will depend on the mission in which the software is to be used and the manner in which it is to be developed and deployed. They will usually include performance, availability, maintainability, modifiability, security, testability and usability (operability)."

The architectural design may be captured in a variety of ways but is typically captured in one or more diagrams. Consider including diagram conventions, as appropriate, so readers can better understand the architectural design captured in those diagrams. When capturing the architectural design, consider including:

* A subsystem/component context diagram.
* A system design diagram (such as a top-level data flow diagram or UML (Unified Modeling Language) diagram).
* "A list of [software] subsystems, tasks, or major components – e.g., user interface, database, task management." [073](#_tabs-<p></p>)
* A map or list of software units that make up each CSCI.

## 3.3 CSCI decomposition and interrelationship between components

“Identify the software units that make up the CSCI [the purpose and the CSCI requirements and CSCI-wide design decisions allocated to it].  ...A software unit is an element in the design of a CSCI; for example, a major subdivision of a CSCI, a component of that subdivision, a class, object, module, function, routine, or database.  Software units may occur at different levels of a hierarchy and may consist of other software units.  Software units in the design may or may not have a one-to-one relationship with the code and data entities (routines, procedures, databases, data files, etc.) that implement them or with the computer files containing those entities.  A database may be treated as a CSCI or as a software unit.  The SwDD may refer to software units by any name(s) consistent with the design methodology being used.” [490](#_tabs-<p></p>)

1. **CSCI components**
   * Description of functionality and operational modes, data storage concepts, and structures. [072](#_tabs-<p></p>)
   * Derived requirements.[073](#_tabs-<p></p>)
   * Functional allocations among the software subsystems.
   * Databases, data files, and shared data with safety-critical data marked. [276](#_tabs-<p></p>)
   * "Identify, state the purpose, and describe in detail the algorithms to be incorporated into the execution of the CSU. The algorithms shall be described in terms of the manipulation of input and local data elements and the generation of output data elements." [176](#_tabs-<p></p>)
   * Fault management approach and algorithm implementation.
   * Identification and formats of input and output data. [072](#_tabs-<p></p>)
   * Purpose, source and destination, data type, data representation, size, units of measure, limit/range, accuracy, precision/resolution.
   * Identification of safety-critical input and output data used in interfaces. [276](#_tabs-<p></p>)
   * I/O data rates.
   * A subsystem/component context diagram. [072](#_tabs-<p></p>)
   * A system design diagram (such as a top-level data flow diagram or UML diagram). [072](#_tabs-<p></p>)
   * Design diagrams for the task [072](#_tabs-<p></p>)and descriptions of major modules. [073](#_tabs-<p></p>)
   * Identification of non-safety-critical units that can interact with safety-critical ones. [276](#_tabs-<p></p>)
   * Documentation of the positions and functions of safety-critical components in the design hierarchy. [276](#_tabs-<p></p>)
   * Relationship of this software to other software components in the system.
   * Interrupts and/or exception handling, including event, failure detection and correction (FDC), and error messages. [072](#_tabs-<p></p>)
   * End-to-end data flow description and/or diagrams.[073](#_tabs-<p></p>)
   * "Execution control, interrupt characteristics, initialization, synchronization, and control of the components...include finite state machines." [276](#_tabs-<p></p>)
   * Timing and sequencing diagrams.
   * States and modes of software operation, including the software units that execute in each state and mode, as well as the execution control and data flow between components in the different states and modes.
   * Control and signal flow, interrupt priorities and interrupt handling, error detection and handling.
   * "Dynamically controlled sequencing, state transition diagrams..., priorities among units..., concurrent execution, dynamic allocation and de-allocation, dynamic creation and deletion of objects, processes, tasks, and other aspects of dynamic behavior." [096](#_tabs-<p></p>)
   * Thread interactions.
   * "Requirements trace or flow down of system-level requirements to the subsystem, with any safety-critical requirements highlighted."[073](#_tabs-<p></p>)
   * Trace of each safety-critical component back to original safety requirements and how the requirement is implemented. [276](#_tabs-<p></p>)
   * Traceability between the architectural design and software components.

1. **Description of how the software item satisfies the software requirements, including algorithms, data structures,** data configuration loads, **and functional decomposition**, including software and hardware fault management and how software requirements are allocated to processors and tasks**.**   
   Consider including the following when describing how each software item satisfies the associated set of software requirements:
2. **Software item input/output (I/O) description.**   
   When capturing the I/O description, consider including the following information, as appropriate:
3. **Static/architectural relationship of the software units.**   
   Like the CSCI architectural design, the static/architectural relationship of software units is typically captured in one or more diagrams. Consider the following when capturing this information:
4. **Concept of execution, including data flow, control flow, and timing.**   
   The concept of execution may be captured in "diagrams and descriptions showing the dynamic relationship of the software units, that is, how they will interact during CSCI operation." [096](#_tabs-<p></p>) Consider including the following information when capturing the concept of execution:
5. **Requirements, design, and code traceability.**   
   Traceability is another type of information that is important for development and maintenance of the software because it allows development personnel to identify affected software products when a change or update is made. Consider the following when capturing the traceability information for the design. (See also the traceability guidance in this Handbook for [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability).)

**f. CSCI's planned utilization of computer hardware resources.**   
Consider the following when capturing the planned utilization of computer hardware resources for each CSCI:

* Resource limitations, the strategy for managing each resource and its limitations, the margins, and the method for measuring those margins, for example, timing, fault messages, memory.
* "Utilization constraints (e.g., CPU, memory); how the software will adapt to changing margin constraints; performance estimates." [072](#_tabs-<p></p>)
* "Estimates of computer hardware resources usage ... to ensure that the design is within the total hardware resource capacity."  [001](#_tabs-<p></p>)
* Storage and memory resource allocations across the software architecture.
* Memory, bus, throughput estimates, and margins.
* Planned CSCI usage of processor capacity, I/O device capacity, auxiliary storage capacity, communication or network capacity. [096](#_tabs-<p></p>)
* “The CSCI requirements or system-level resource allocations being satisfied.
* The assumptions and conditions on which the utilization data are based (for example, typical usage, worst-case usage, assumption of certain events).
* Any special considerations affecting the utilization (such as use of virtual memory, overlays, or multiprocessors or the impacts of operating system overhead, library software, or other implementation overhead).
* The units of measure used (such as percentage of processor capacity, cycles per second, bytes of memory, kilobytes per second).
* The level(s) at which the estimates or measures will be made (such as software unit, CSCI, or executable program).”  [490](#_tabs-<p></p>)

g. Whether components are new or previously developed, and, if previously developed, reference to the baseline from which they were taken.  This should include a detailed description of the operating system, device drivers and board support package software.

**2. Rationale for software item design decisions/trade decisions, including assumptions, limitations, safety and reliability-related items/concerns or constraints in design documentation.**

It is important to document the reasons for design decisions for the implementation phase, as well as future software maintenance activities. Design decisions need to be traceable to relevant trade studies and the associated reasoning behind those decisions. Consider the following when capturing the rationale for design decisions:

* Alternatives that were part of the design process but that were excluded, along with the reasons for those exclusions, e.g., did not meet requirements, low probability of success, and exceeded cost and/or schedule constraints. [001](#_tabs-<p></p>)
* Assumptions made during discussions of design options.
* Limitations of various design options that affected the design choice, e.g., technical, cost, schedule limitations.
* Safety and reliability considerations in the design elements and interfaces for each software subsystem, task, or component.[073](#_tabs-<p></p>)
* Design constraints, e.g., feasibility, coupling, extensibility, maintainability.
* Design drivers, e.g., performance, reliability, usability, hardware considerations, established for the project that affected the software design.
* "Design alternatives, including reuse of heritage software and/or COTS tradeoffs."[073](#_tabs-<p></p>)
* Performance parameters that were part of the rationale, e.g., reliability, safety, affordability, schedule, risk. [001](#_tabs-<p></p>)
* "Selection criteria (e.g., adherence to design standards, verifiability, ease of construction, reuse, use of COTS, safety)." [001](#_tabs-<p></p>)
* "Assumptions about the environment including operating system, user interface, component, data management, data interchange, graphics, and network services, especially assumptions on which safety functions and computer security needs may be based."
* "Assumptions and conditions on which the utilization data are based (e.g., typical usage, worst-case usage, and assumption of certain events)." [096](#_tabs-<p></p>)
* Architectural element responsibilities (constraints on inputs and guarantees on outputs) and constraints on how the elements interact (such as message and data sharing protocols).

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality), [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations),

**3. Interface design**

Consider the following when capturing the interface characteristics of the software units which can be described as “interfaces among the software units and their interfaces with external entities such as systems, configuration items, and users.“ [490](#_tabs-<p></p>) (See also the guidance in this topic for the interface design description document.) If all or part of this information is captured in one or more interface documents, those documents may be referenced here.

* Internal interfaces between all components.
* Operator interfaces.
* Device interfaces.
* Allocation of the software's external interface requirements to components.
* "Identify the safety-critical ... interfaces throughout the design. Identify non-critical units that can interact with safety-critical ones." [276](#_tabs-<p></p>)
* "Design of each interface in terms of:

* Information description;
* Initiation criteria;
* Expected response;
* Protocol and conventions;
* Error identification, handling and recovery;
* Queuing;
* Implementation constraints;
* Requirements relative to safety and computer security."

* Interface type and purpose.
* Interface description, including data transmitted, messages transmitted, priority of interfaces, and messages transmitted across them.
* All direct hardware interfaces like the flight computer interface or application program interface or operation system interface.

See also Topic [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description),

## 3.4 CSCI detailed design

The detailed design describes “each software unit of the CSCI.  ...  If design information falls into more than one paragraph, it may be presented once (in the design document) and referenced from the other paragraphs.”  When capturing the detailed design, consider the following:

* Software unit identification and descriptions.  
  + Unit design decisions, such as algorithms used.
  + Constraints, limitations, or unusual features in the design of the software unit.
  + Programming language to be used and rationale.
  + Procedural commands (such as menu selections in a database management system (DBMS) for defining forms and reports, on-line DBMS queries for database access and manipulation, input to a graphical user interface (GUI) builder for automated code generation, commands to the operating system, or shell scripts), and reference to user manuals or other documents that explain them.
  + Description of inputs, outputs, and other data elements and data element assemblies, as applicable.  Data local to the software unit shall be described separately from data input to or output from the software unit.
  + Logic to be used by the software unit, including, as applicable:  
    - Conditions in effect within the software unit when its execution is initiated
    - Conditions under which control is passed to other software units
    - Response and response time to each input, including data conversion, renaming, and data transfer operations
    - Sequence of operations and dynamically controlled sequencing during the software unit's operation, including:  
      * The method for sequence control.
      * The logic and input conditions of that method, such as timing variations, priority assignments.
      * Data transfer in and out of memory.
      * The sensing of discrete input signals and timing relationships between interrupt operations within the software unit.
    - Exception and error handling.[490](#_tabs-<p></p>)
* Bidirectional requirements traceability between the software units and requirements allocated to them.[490](#_tabs-<p></p>)

Other candidate information for the software design description includes:

* Scope, including system identification, system overview, document overview, and referenced documents.[490](#_tabs-<p></p>)
* Software operational metrics.
* Design methods and details for their implementation, for example, software updates, user-modifiable software or software parameters, redundancy management approach for the software design or multiple-version dissimilar software.
* If the software contains deactivated code or test code, a description of the means to ensure that the code cannot be enabled in the target computer.
* Security design features.
* Safety considerations addressed in the design, show traceable to all software hazards and software hazard migration steps.

The Software Architecture Review Board, a software engineering sub-community of practice accessible on the NASA Engineering Network, is a good resource of software design information, including sample documents, reference documents, and expert contacts.

Additional guidance related to software design may be found in Topic [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description), and [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews).

See also Topic [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures),

## 3.5 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

Projects with limited personnel or budgets need to consider the guidance and use of software design document templates from the local Center PAL. Center Engineering Technical Authorities also have been empowered to provide specific relief when the software classification specifies required design description items, i.e., "X" in Requirements Mapping Matrix in NPR 7150.2.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-072) Checklist for the Contents of Software Critical Design Review (CDR),
   580-CK-008-02, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2010.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-073) Checklist for the Contents of Software Preliminary Design Review (PDR),  580-CK-007-02, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2010.  This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-096) Software Design Description Template,  GRC-SW-TPLT-SDD, NASA Glenn Research Center (GRC), 2011.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-176)

  [Software Design Document Data Item Description,](https://sce.uhcl.edu/helm/ms_2167/over_2167.html "Click to open in new window")

  Department of Defense, DI-MCCR-80012A, 1988.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-490)

  [History of NASA’s Academy of Program/Project & Engineering Leadership.](http://appel.nasa.gov/about-us/history/ "Click to open in new window")

  Academy of Program/Project and Engineering Leadership (APPEL). Retrieved on September 14, 2015 from http://appel.nasa.gov/about-us/history/.
* (SWEREF-501)

  [Mars Observer Inertial Reference Loss](https://llis.nasa.gov/lesson/310 "Click to open in new window")

  Public Lessons Learned Entry: 310.
* (SWEREF-514)

  [Preliminary Design Review](https://llis.nasa.gov/lesson/655 "Click to open in new window")

  Public Lessons Learned Entry: 655.
* (SWEREF-515)

  [Critical Design Review for Unmanned Missions](http://llis.nasa.gov/lesson/657 "Click to open in new window")

  Public Lessons Learned Entry 657.
* (SWEREF-517)

  [Fault Tolerant Design](https://llis.nasa.gov/lesson/707 "Click to open in new window")

  Public Lessons Learned Entry: 707.
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-550)

  [ADEOS-II NASA Ground Network (NGN) Development and Early Operations -- Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned](https://llis.nasa.gov/lesson/1346 "Click to open in new window")

  Public Lessons Learned Entry: 1346.
* (SWEREF-551)

  [Lessons Learned From Flights of ?Off the Shelf? Aviation Navigation Units on the Space Shuttle, GPS](https://llis.nasa.gov/lesson/1370 "Click to open in new window")

  Public Lessons Learned Entry: 1370.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
* (SWEREF-571)

  [NASA Study of Flight Software Complexity](https://llis.nasa.gov/lesson/2050 "Click to open in new window")

  Public Lessons Learned Entry: 2050.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No specific Lessons Learned have currently been identified for this topic. However, included below are lessons learned related to software design that can also be found in the related requirements named in the guidance section.

* **Preliminary Design Review. Lesson Learned 0655[514](#_tabs-<p></p>):**  By not holding a PDR "one or a number of potential problems which could result in an adverse impact on the system, subsystem, and/or project might not be identified in a timely manner. This oversight might later result in a condition having a significant effect on quality, reliability, capability, schedule, and/or cost...Conduct a formal Preliminary Design Review (PDR) at the system and subsystem levels prior to the start of subsystem detail design, to assure that the proposed design and associated implementation approach will satisfy the system and subsystem functional requirements."
* **Critical Design Review for Unmanned Missions. Lesson Learned 0657[515](#_tabs-<p></p>):**  "In the absence of a CDR, potential problems with adverse impacts on the subsystem, system, or project may not be identified in a timely manner. This oversight may later result in a condition having a significant effect on quality, reliability, capability, schedule, or cost."
* **Lessons Learned From Flights of "Off the Shelf" Aviation Navigation Units on the Space Shuttle, GPS (Importance of Accurate Interface Control Document.) Lesson Learned 1370[551](#_tabs-<p></p>):**  "If the integrator and user do not have access to firmware and firmware requirements, the ICD may be the only written source of information on unit parameters. Developers of software that will interface with the unit must examine the ICD closely. .... An inaccurate ICD will lead to software and procedural issues that will have to be addressed before a system can be certified as operational. An accurate ICD is also needed for instrumentation port data that is critical during the test and verification phase of a project...Short development schedules may result in changes to the ICD while host vehicle software requirements are being defined and software is in development and test. A disciplined process of checks must be in place to ensure that the ICD and software requirements for units that interface with the [hardware and instruments] are consistent. Individuals who have knowledge of both [hardware] requirements and requirements for other interfacing units must be able to communicate and be involved in any changes made to the ICD."
* **MER Spirit Flash Memory Anomaly (2004). Lesson Learned 1483[557](#_tabs-<p></p>):**  "Shortly after the commencement of science activities on Mars, an MER rover lost the ability to execute any task that requested memory from the flight computer. The cause was incorrect configuration parameters in two operating system software modules that control the storage of files in system memory and flash memory. Seven recommendations cover enforcing design guidelines for COTS software, verifying assumptions about software behavior, maintaining a list of lower priority action items, testing flight software internal functions, creating a comprehensive suite of tests and automated analysis tools, providing downlinked data on system resources, and avoiding the problematic file system and complex directory structure."
* **NASA Study of Flight Software Complexity. Lesson Learned 2050[571](#_tabs-<p></p>):**  "Flight software development problems led NASA to study the factors that have led to the accelerating growth in flight software size and complexity. The March 2009 report on the NASA Study on Flight Software Complexity contains recommendations in the areas of systems engineering, software architecture, testing, and project management."
* **Software Design for Maintainability. Lesson Number 0838[526](#_tabs-<p></p>)**: Impact of Non-Practice: "Because of increases in the size and complexity of software products, software maintenance tasks have become increasingly more difficult. Software maintenance should not be a design afterthought; it should be possible for software maintainers to enhance the product without tearing down and rebuilding the majority of code."
* **Mars Observer Inertial Reference Loss. Lesson Number 0310[501](#_tabs-<p></p>)**: Design for Maintenance, Lesson Learned No. 4: "Design flexibility of the flight computer and software is critical to the ability to uplink software patches for the correction of unexpected in-flight spacecraft anomalies."
* **ADEOS-II NASA Ground Network (NGN) Development and Early Operations – Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned. Lesson Number 1346[550](#_tabs-<p></p>)**: Use of commercial off the shelf (COTS) products: "Match COTS tools to project requirements. Deciding to use a COTS product as the basis of system software design is potentially risky, but the potential benefits include quicker delivery, less cost, and more reliability in the final product. The following lessons were learned in the definition phase of the [software] development.  
  + "Use COTS products and re-use previously developed internal products.
  + "Create a prioritized list of desired COTS features.
  + "Talk with local experts having experience in similar areas.
  + "Conduct frequent peer and design reviews.
  + "Obtain demonstration versions of COTS products.
  + "Obtain customer references from vendors.
  + "Select a product appropriately sized for your application.
  + "Choose a product closely aligned with your project's requirements.
  + "Select a vendor whose size will permit a working relationship.
  + "Use vendor tutorials, documentation, and vendor contacts during COTS evaluation period."
* **Fault Tolerant Design. Lesson Number 0707[517](#_tabs-<p></p>)**: "Systems which do not incorporate fault tolerant design (FTD) as a part of their development process will experience a higher risk of a severely degraded or prematurely terminated mission, or it may result in excessively large weight volume, or high cost to achieve an acceptable level of performance by using non-optimized redundancy or overdesign...Incorporate hardware and software features in the design of spacecraft equipment which tolerate the effects of minor failures and minimize switching from the primary to the secondary string. This increases the potential availability and reliability of the primary string."

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
