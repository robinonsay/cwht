# 5.02 - IDD - Interface Design Description

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695656. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description

5.02 - IDD - Interface Design Description

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695656)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695656&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Minimum Recommended Content](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

Return to 7[.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)

# 1. Minimum Recommended Content

Minimum recommended content for the Interface Design Description. 

1. 1. Priority assigned to the interface by the interfacing entity(ies).
   2. Type of interface (e.g., real-time data transfer, storage-and-retrieval of data) to be implemented.
   3. Specification of individual data elements (e.g., format and data content, including bit-level descriptions of data interface) that the interfacing entity(ies) will provide, store, send, access, and receive.
   4. Specification of individual data element assemblies (e.g., records, arrays, files, reports) that the interfacing entity(ies) will provide, store, send, access, and receive.
   5. Specification of communication methods that the interfacing entity(ies) will use for the interface.
   6. Specification of protocols the interfacing entity(ies) will use for the interface.
   7. Other specifications, such as physical compatibility of the interfacing entity(ies).
   8. Traceability from each interfacing entity to the system or CSCI requirements addressed by the entity's interface design, and traceability from each system or CSCI requirement to the interfacing entities that address it.
   9. Interface compatibility.
   10. Safety-related interface specifications and design features.

# 2. Rationale

The Interface Design Description (IDD) describes the interface characteristics of one or more systems, subsystems, Hardware Configuration Items (HWCIs), Computer Software Configuration Items (CSCIs), manual operations, or other system components. Typical NASA development projects are complex, multi-disciplined activities that consist of systems and systems of systems. These projects usually require integrated product teams working together to achieve the goals and objectives in a timely and cost-efficient manner. The execution of the software development life cycle and its activities by the team requires multiple tasks and work products to be developed and accomplished in parallel. To assure that the assembled systems and integrated systems function as intended, the interfaces for the software work products (components) and systems must be accurately defined, designed, controlled, and communicated. A high-quality IDD document fulfills these needs for the software development team.

# 3. Guidance

The software IDD document may be a stand-alone entity or part of the Software Design Description document ([5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)) or part of an electronic data system. Center policies and procedures are expected to be followed when determining which documentation approach is suitable for a particular project. It is important that the interface design information be identified and tracked as the software system is being developed, tested, and operated. Software interface designs and requirements tend to drive software designs and can lead to a potential source of anomalies during the development and operational life cycle. The key to implementing this requirement is to have a good description of all software, hardware, operations, and system interfaces and interactions during the design and operational phases of a development cycle. The content of the IDD is defined by PDR (Preliminary Design Review). The preliminary IDDs are expected to be approximately 30 percent completed at PDR. All interface components are to be defined by PDR. The IDDs are completed by CDR (Critical Design Review) and updated as needed after CDR. The final as-built IDD is documented as a part of the as-built design documentation for operational use, software modification, and potential software reuse applications. See also [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design). See also Topic [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures), [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification),

The software development team is responsible for preparing an IDD that describes the interface entity characteristics for all defined systems, subsystems, domains, hardware items, software items, manual operations, and other system components.

The descriptions contain the interface characteristics for systems or configuration items that participate in the interface (including human-system and human-human interfaces), standards and protocols, responsible parties, interface operational schedules, and any error handling routines. The software team also defines those interface characteristics that are existing or permanent, as well as those that are being developed or modified. The applicability of this requirement is highly dependent on the classification level for the software work product(s). Appendix C, Requirements Mapping Matrix, of NPR 7150.2 shows the requirements for each classification level (see [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)).

An excellent way to begin the descriptions of the interfaces is with a context or state diagram. A suitably detailed diagram (showing the relationship of the interface with the overall activity) with legends and callouts will easily show the dependencies that must be controlled and satisfied in the software detailed design. Either a single diagram or an interrelated set of diagrams, depending on the complexity of the software work product(s), may be the most appropriate choice.

As shown in the text above, the software IDD document is recommended to contain specific information.  NASA-specific interface design description information and resources are available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.

Below are suggestions for the type of information to consider for the named content.

## 3.1 Document content

The following paragraphs are based on Department of Defense (DoD) DI-IPSC-81436A, Data Item Description Interface Design Description (IDD) [025](#_tabs-<p></p>), along with supporting material from GRC (Glenn Research Center) GRC-SW-TPLT-IDD, Interface Design Description (IDD) Template.

* Assigned priority.   
  This is the priority assigned to the interface by the interfacing entity(ies).The level of the priority allows the software to service higher priority queues ahead of lower priority queues. Complex priority values may allow timeouts and software interrupts to avoid the starving of lower priority interfaces.
* Type of interface.   
  The IDD document includes characteristics about interface types, such as real-time data transfer, storage-and-retrieval of data, remote programming interface, etc., that will be implemented.

Factors like functionality, performance speed, the time needed to use the program, user satisfaction, and the rate of user errors are some criteria for the software development team to consider when designing an interface. The software interface tests are specified in the [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan).

The two most common ways of expressing interface information are (1) alphabetically by parameter and (2) for data-oriented interfaces, by layers with reference to a level-of-abstraction model such as the Open Systems Interconnection (OSI)-7 Layer model. [303](#_tabs-<p></p>) In the latter case, individual information items (e.g., requirements or characteristics) are framed consistent with the layer definitions and then specified by layer, "physical" up to "application" in that order of the OSI-7 Layer model. Within a layer, control flow sequence is used where applicable to express information; otherwise it is expressed alphabetically by parameter.

* **Specifications of individual data elements**   
  The IDD document includes characteristics about the individual data elements that the interfacing entity(ies) will provide, store, send, access, receive, etc., such as:

* Names/identifiers.

1. 1. 1. 1. Project-unique identifier.
         2. Nontechnical (natural language) name.
         3. Standard data element name.
         4. Technical name, e.g., variable or field name in code or database.
         5. Abbreviation or synonymous names.

* Data type (alphanumeric, integer, etc.), indicating data types that are not defined until implementation, such as C++ type overloading (templates) and dynamic typecasting.
* Size and format, i.e., length and punctuation of a character string or bit-level descriptions.
* Units of measurement, i.e., meters, dollars, or nanoseconds.
* Range or enumeration of possible values, i.e., 0 to 99.
* Accuracy (how correct) and precision (number of significant digits).
* Priority, timing, frequency, volume, sequencing, and other constraints, such as whether the data element may be updated and whether business rules apply.
* Security and privacy constraints.
* Sources (setting or sending entities) and recipients (using or receiving entities).
* Safety-criticality.

* **Specifications of data element assemblies**  
  The IDD document includes characteristics about data element assemblies, such as records, messages, files, arrays, displays, reports, etc., that the interfacing entity(ies) will provide, store, send, access, receive, etc., such as:

+ Names/identifiers.

1. 1. Project-unique identifier.
   2. Nontechnical (natural language) name.
   3. Technical name, e.g., record or data structure name in code or database. Abbreviations or synonymous names.

* Data elements in the assembly and their structure (number, order, grouping, and bit-level descriptions).
* Medium, i.e., disk, and structure of data elements or assemblies on the medium.
* Visual and auditory characteristics of displays and other outputs, i.e., colors, layouts, fonts, icons, and other display elements, beeps, and lights.
* Relationships among assemblies, such as sorting or access characteristics.
* Priority, timing, frequency, volume, sequencing, and other constraints, such as whether the assembly may be updated and whether business rules apply.
* Security and privacy constraints.
* Sources (setting or sending entities) and recipients (using or receiving entities).
* Safety-criticality.

* **Specifications of communication methods**   
  The IDD document includes characteristics about communication methods that the interfacing entity(ies) will use for the interface, such as:
  + Project-unique identifier(s).
  + Communication links, bands, frequencies, media, and their characteristics.
  + Message formatting.
  + Flow control, i.e., sequence numbering and buffer allocation.
  + Data transfer rate, whether periodic or aperiodic, and interval between transfers.
  + Routing, addressing, and naming conventions.
  + Transmission services, including priority and grade.
  + Security and privacy considerations, such as encryption, user authentication, compartmentalization, and auditing.
  + Safety-criticality.

* **Specifications for communications protocol**   
  The IDD document includes characteristics about digital message formats and the rules for exchanging those messages. A protocol defines the syntax, semantics, and synchronization of communication, and the specified behavior is typically independent of how it is to be implemented. A protocol can therefore be implemented as hardware or software or both. Characteristics of protocols the interfacing entity(ies) will use for the interface include:
  + Project-unique identifier(s).
  + Priority or layer of the protocol.
  + Packeting, including fragmentation and reassembly, routing, and addressing.
  + Legality checks, error control, and recovery procedures.
  + Synchronization, including connection establishment, maintenance, and termination.
  + Status, identification, and any other reporting features.

* **Other characteristics**, such as   
  Physical compatibility of the interfacing entity(ies) (dimensions, tolerances, loads, voltages, plug compatibility, etc.).
* **Traceability**   
  Show the path from each interfacing entity to the system or CSCI (Computer Software Configuration Item) requirement addressed by the design. To complete the bidirectional tracing of the requirements, show from each system or CSCI requirement to the interfacing entity that addresses it.
* **Interface Compatibility**   
  The IDD document contains information about the intended compatibility between or among the interfaces being developed. Specifically, will there be uniform or optional approaches to developing weak versus strong compatibility? Will the compatibility of the software components' interaction with their environment be characterized as optimistic or pessimistic in nature?
* **Safety-related interface specifications and design features**   
  Safety-critical off-the-shelf (OTS) and reused software must undergo safety analysis that considers:  
  + Its ability to meet required safety functions.
  + Extra functionality that may be present, even if not planned for use.
  + The impact on safety.
  + Interfaces to developed code.

Additional analysis, testing, or a combination thereof can be performed to verify safety-critical OTS or reused software to the same level required of in-house developed software to the extent possible via black box testing.

The Contract Data Requirements List specifies whether deliverable data are to be delivered on paper or electronic media; may be delivered in developer format rather than in the format specified herein; and may reside in a computer-aided software engineering or other automated tool rather than in the form of a traditional document.

See also Topic [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis). [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews), [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis)

## 3.2 Best practices

The software development team solicits relevant stakeholder involvement to evaluate applicable system interface(s).

Whenever possible, the software development team considers using an industry recognized standard for system interfaces.

## 3.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

The proper execution of interfaces among entities in software design activities is no less important for small projects than for large projects. Improper interface development, evaluation, and testing will cause any software work product to fail to function, regardless of the size of the project.

Smaller projects may benefit by using standard interface designs or Interface Design Description (IDD) templates previously developed and cataloged in software reuse repositories or by using personnel with previous experience on identical or similar interfaces. Where applicable, information may be duplicated from IDDs written for previously developed software interfaces. Extreme care is used whenever deciding to reuse software. (See [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) for information that may be applicable.) (See the Center's repository of best practices for additional guidance in this area.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-025)

  ["IDD-DID SW Interface Design Description,"](http://www.everyspec.com/DATA+ITEM+DESC+%28DIDs%29/DI-IPSC/download.php?spec=DI-IPSC-81436A.003748.pdf "Click to open in new window")

  DI-IPSC-81436A, Department of Defense, 1999.
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-303)

  [What are Interface Requirements Specifications, Interface Design Descriptions, Interface Control Documents, and how do they relate?,](https://www.ppi-int.com/resources/systems-engineering-faq/interface-requirements-specifications-interface-design-descriptions-interface-control-documents-relate/ "Click to open in new window")

  Robert Halligan, Project Performance International. (Expressing and Organizing Interface Information). Accessed November 3, 2014 from http://ppi-int.com/systems-engineering/irs-idd-icd-relationship.php.
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-508)

  [Interface Control and Verification](https://llis.nasa.gov/lesson/569 "Click to open in new window")

  Public Lessons Learned Entry: 569.
* (SWEREF-513)

  [Mars Climate Orbiter Mishap Investigation Board - Phase I Report](https://llis.nasa.gov/lesson/641 "Click to open in new window")

  Public Lessons Learned Entry: 641.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)        * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) |

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

* **Interface Control and Verification. Lesson Number 0569[508](#_tabs-<p></p>):** Problems occurred during the Mars Pathfinder spacecraft integration and test due to out-of-date or incomplete interface documentation. (While this lesson involves a hardware-related problem, it illustrates the need for accuracy in interface documentation.) Investigation showed that the main wiring harness was built in accordance with documentation that had not been updated after design changes were made. In part, this was due to independently prepared Mechanical Interface Control Drawings by the Government and the contractor. The MICD s should have had periodic verification for accuracy and compatibility.
* **Mars Climate Orbiter Mishap Investigation Board - Phase I Report. Lesson Number 0641[513](#_tabs-<p></p>)**: "The MCO Mishap Investigation Board (MIB)...determined that the root cause for the loss of the MCO spacecraft was the failure to use metric units in the coding of a ground software file." The data in the ... file was required to be in metric units per existing software interface documentation, and the trajectory modelers assumed the data was provided in metric units per the requirements. In fact, the angular momentum (impulse) data was in English units rather than metric units. The failure to properly communicate what was in the interface documentation is a warning that the effective implementation of the IDD requirement includes adequate communication of its contents, not just the writing and recording.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
