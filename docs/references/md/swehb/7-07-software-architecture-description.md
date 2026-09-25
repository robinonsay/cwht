# 7.07 - Software Architecture Description

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695632. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description

7.07 - Software Architecture Description

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695632)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695632&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. General Guidance](#tabs-2)
* [3. Structure of this Topic](#tabs-3)
* [4. Recommended Contents](#tabs-4)
* [5. Common Weaknesses](#tabs-5)
* [6. Example Outlines](#tabs-6)
* [7. Quality Attribute Table](#tabs-7)
* [8. Resources](#tabs-8)
* [9. Lessons Learned](#tabs-9)

# 1. Purpose

The purpose of this document is to recommend content for software architecture descriptions for NASA projects in order to make the architecture description *informative* and *complete* providing a good basis for understanding and assessments of the architecture.  The recommendations here apply equally to flight software, ground software, and other types of less critical software. They are intended to promote understanding of software architecture among stakeholders, to enable effective architecture reviews, and to facilitate future reuse. These recommendations are *informal* in the sense that they provide a number of details beyond NASA's top-level requirements associated with software architecture and design preparation (see the requirements in NPR 7150.2 section 4.2).

IEEE Standard 1471-2000, Recommended Practice for Architectural Description for Software-Intensive Systems, defines architecture as "the fundamental organization of a system, embodied in its components, their relationships to each other and the environment, and the principles governing its design and evolution." [210](#_tabs-<p>8</p>)

In preparing an architecture description, one must decide how much detail is appropriate. According to Bass, Clements, and Kazman, "An architecture is a description of system structures, of which there are several (module decomposition, process, deployment, layered, etc.). Architecture is the first artifact that can be analyzed to determine how well its quality attributes are being achieved, and it also serves as the manifestation of the earliest design decisions, and is a re-usable abstraction that can be transferred to new systems." [239](#_tabs-<p>8</p>)

It is important to note that the *description* of software architecture is not the same as the architecture itself. A system can have great software architecture with a weak description, or weak software architecture with a great description.

# 2.  General Guidance

In preparation for a NASA software architecture review, the NASA Software Architecture Review Board (SARB) recommends a set of resources (located on the NEN [here](https://nen.nasa.gov/web/sarb/home?p_p_id=gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_cur=1&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_delta=20&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_orderByCol=modifiedDate&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_orderByType=desc&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_selectedResourceRecordTypeIds=137) and from external organizations) to guide both the architecting process as well as documentation of the resulting architecture. Utilizing these guidelines will help prepare software architects for the review, making sure the documentation and presentation of the architecture are complete according to best practices and addresses concerns that are unique to the domain of flight software engineering.

The Software Engineering Institute (SEI) at Carnegie Mellon University has arguably the largest collection of software-architecture-related material. Faculty, professors, and researchers from this organization spearheaded many of the current approaches and practices in this domain. Therefore, the SARB recommends the use of the SEI website as a starting place for learning about and guiding the process of software architecture documentation and review. The link is [327](#_tabs-<p>8</p>) in the Resources tab for this guidance topic.

This website contains software-architecture-related background information that may be useful to the software architect in preparation for the development of the architecture, and in setting the stage for architecture documentation and formal review. See [499](#_tabs-<p>8</p>) in the Resources tab for a direct link.

For the purposes of preparing a software architecture description document, this website provides the key tools necessary for getting started. The bottom of the page referenced above has an “Availability” section with three strong sources for guiding documentation efforts: a template [296](#_tabs-<p>8</p>), a pointer to what is widely considered the definitive book on software architecture documentation (read this for more detail on a particular documentation aspect), and finally a link to consulting services that can be used for on-site help and guidance with creating the documentation based on the approach described on this page, in the template, and in the book.

Finally, this guidance should be used in conjunction with the SEI materials referenced above to help ensure that the concerns and characteristics specific to the NASA spacecraft flight software domain are clearly addressed in the architecture description document.

Projects are not required to produce a document separate from a software architecture model (e.g., Unified Modeling Language [UMl] model) or cover the software architecture description in a single electronic file.  Rather than transcribe a software architecture model to a document or presentation, projects can use a model as the architecture description, in whole or in part. However, this often necessitates that the project a) creates additional views to communicate the architecture to various stakeholders and b) organizes and links the model to provide a structured and logical navigation of the model. Likewise, a project can use a combination of documents, presentations, and/or architecture models to cover different portions of the recommended content. The project simply needs to provide a document, like a hypertext document, that guides readers to the recommended order and manner of reviewing the files.

# 3. Structure of this Topic

This guidance is organized as a list of recommended contents with the rationale for each recommendation. This guidance focuses on the SEI template [296](#_tabs-<p>8</p>), but does offer additional examples in tab 6. Example Outlines .

# 4. Recommended Contents

The Software Architecture Review Board (SARB) has identified several aspects of software architecture description of particular importance in flight software for NASA’s space missions. Although these same aspects can be found in the SEI template for a software architecture document [010](#_tabs-<p>8</p>) , they are not necessarily given the same prominence due to their location within the SEI template’s five levels of headings. The purpose of this guidance, then, is to draw special attention to specific aspects of architecture description that the SARB recommends be addressed in NASA architecture description documents.

## 4.1 Architecture Terminology

Several sections of the SEI template make it clear that software architects are expected to follow the terminology defined in ANSI/IEEE-1471-2000, IEEE Recommended Practice for Architectural Description of Software-Intensive Systems [210](#_tabs-<p>8</p>).  However, where appropriate, architects are encouraged to use terminology from the newer international standard ISO/IEC/IEEE 42010, Systems and software engineering — Architecture description. Important terms include *system, environment, stakeholder, concern, view, viewpoint, and rationale*. The figure below shows a partial concept map of how different terms relate to each other. For example, every system has one or more stakeholders, and every stakeholder has one or more concerns, and an architecture description selects viewpoints that are addressed to those concerns.

## 4.2 Mission Overview

A system is intended to fulfill a mission, and software is largely responsible for the behavior of the system (flight and ground systems). As such, it is helpful to readers to provide context for the architectural drivers that follow. Most readers won't be scientists, and external reviewers might come from outside of the aerospace industry, so it's not necessary to go deep into the science objectives. However, it's very helpful to highlight aspects of the mission that give rise to the driving requirements. When using the SEI template, this overview is captured in Section 2.1 (Problem Background) and possibly Section 2.1.1 (System Overview).

## 4.3 Context Diagram, Context Description

An architecture description is about a system, and that system always exists in a larger context. Clements et al describe this very well:

* "A top-level context diagram (TLCD) establishes the scope for the system whose architecture is being documented, defining the boundaries around the system that shows what's in and what's out. A TLCD shows how the system under consideration interacts with the outside world. Entities in that outside world may be humans, other computer systems, or physical objects, such as sensors or controlled devices. A TLCD identifies sources of data to be processed by the system, destinations of data produced by the systems, and other systems with which it must interact." [295](#_tabs-<p>8</p>)

A context diagram helps readers avoid confusion about what is in scope and what is not. Also, a context description allows the architect to describe the internal boundaries between the system and the software, and discuss the system architecture as well as the software architecture, and the degree to which the system in which the software resides is a part of the architecture description. When using the SEI template, context diagrams are called for in the View Packet subsection of Section 4.1.

*Example:*

When documenting context, it is also important to describe the computing hardware on which the software will run. The computing hardware can shoulder some system functions and quality attributes. Computing hardware can also be the source of constraints and limitations that influence architecture decisions, some of which may influence architecture complexity. A more specific view of the hardware as a set of assigned critical resources with margins is discussed more fully in section 4.5.

## 4.4 Architectural Drivers

One of the most important aspects of architecture description is to identify the major architectural challenges. These challenges may appear in the form of *functional requirements, quality attribute requirements* (sometimes called non-functional requirements), *critical resources*, and *constraints.* These challenges are identified as architectural drivers when they have a major influence on design. Explanation of architectural drivers is an opportunity to educate non-software stakeholders about software challenges.

When discussing requirements, it's useful to make a distinction between *key requirements* (important to the customer) and *driving requirements* (challenging to meet; will drive cost, schedule, or some other aspect of the system). Some requirements are both, but the distinction is important since the latter shapes the architecture.

The SEI template calls for this information in Section 2.1 (Problem Background), which asks for an explanation of “the constraints that provided significant influence over the architecture”, and Section 2.1.3 (Significant Driving Requirements) which asks for “behavioral and quality attribute requirements (original or derived) that shaped the software architecture.”

*Example drivers:*

* EDL (Entry, Descent, and Landing) requires completely autonomous control and exact timing of pyrotechnic events.
* Space Shuttle's primary avionics system had to allow astronauts to make the most critical decisions, including failover to the backup flight system.
* Fault tolerance design almost always impacts software architecture.
* Security risks of the software system.

## 4.5 Critical Resources and Margins

Flight system software often must deal with resources that are severely limited. Such critical resources may include power or energy, nonvolatile storage, bus data rate or latency, uplink or downlink rate, and processor memory or speed. A critical resource is often what makes a requirement "driving". It's important to identify critical resources for the benefit of stakeholders who might not otherwise understand the difficulties that software must face and the tradeoffs to be made.

Critical resources usually have associated margins, and development organizations usually have required margins at each phase to accommodate unforeseen growth. An architecture description shows, for each critical resource, the current best estimate of usage along with the required margin for the current phase.

Curiously, the SEI template makes no mention of resource margins, but it may be that they have lumped that in with “constraints”. Constraints are required in Section 1.5.1 (Viewpoint Definition) and in the view and view packet subsections of Section 3.

*Example Critical Resources:*

* Non-volatile memory. The development team for Mars Exploration Rover (MER) had to do a lot of work to manage what was stored in a relatively small non-volatile memory.
* Power/energy. Lack of power and energy on MER required careful operational planning with overnight sleep periods and recharge periods.

## 4.6 Stakeholders and Concerns

Every system has many stakeholders. Among these are customer, owner, operator, architect, systems engineer, designer, developer, tester, installer, maintainer, vendor, the service provider (e.g., telecommunications), and subcontractor. Failure to identify all stakeholders and their concerns (i.e., “care about”) can lead to unplanned events, rework, and schedule delays.

Section 1.4 (Stakeholder Representation) of the SEI template addresses this important aspect, and it’s important to engage with the stakeholders, draw out their various concerns, and address those concerns through appropriate views in the architecture description.

*Examples:*

|  |  |
| --- | --- |
| **Stakeholder** | **Concerns** |
| Project Manager | Amount of risk due to new technology |
| Project Systems Engineer | Interactions between flight computer and payload |
| Tester | Want the ability to run various tests from tester-defined starting states |
| Operators | Want telemetry data organized in ways that facilitate state determination |

## 4.7 Quality Attribute Analysis

Quality attributes that are important in mission software often include availability, modifiability, performance, safety, security, testability, and usability. As Bass et al describe:

"Business considerations determine qualities that must be accommodated in a system's architecture. These qualities are over and above that of functionality -  Systems are frequently redesigned *not* because they are functionally deficient — the replacements are often functionally identical — but because they are difficult to maintain, port, or scale, or are too slow, or have been compromised by network hackers."  [239](#_tabs-<p>8</p>)

The quality attributes that have the greatest influence on one mission are not necessarily the same on other missions. An architecture description will say several things about quality attributes. For each quality attribute, it will define what the attribute means and describe how the attribute will be measured, often in terms of a usage scenario. The attributes are often ranked in importance and difficulty, and the architecture description will explain how the architecture satisfactorily achieves each desired quality.

To help architects be precise about quality attribute claims, NASA’s Software Architecture Review Board generated a quality attribute table ( tab 7 ) that lists fourteen key quality attributes, identifies different important aspects of each quality attribute and considers each aspect in terms of requirements, rationale, evidence, and tactics to achieve the aspect. This quality attribute table is intended to serve as a guide to software architects, software developers, and software architecture reviewers in the domain of mission-critical real-time embedded systems, such as space mission flight software.

Section 2.1.3 (Significant Driving Requirements) of the SEI template calls for a description of quality attribute requirements and quality attribute goals, but that treatment is limited to driving requirements. Section 2.2 (Solution Background) of the SEI template calls for “a convincing argument that the architecture is the right one to satisfy the behavioral and quality attribute goals levied on it.”

*Examples:*

* Quality attribute: *Availability/Failure Recovery.*

+ Scenario: "A user reports an issue with accessing mission data. The ground team determines that there has been a disk failure. The faulty disk is replaced and mission data restored from backup within 24 hours of the problem report."

* Quality attribute: *Replicability.*

+ Description: When the Hubble Space Telescope upgraded a flight processor, the software had to be coded in C, and its behavior had to replicate the previous software behavior — potentially with the same anomalies — so that operations would not be affected and not require new training.

## 4.8 Measures of Performance

NPR 7123.1, NASA Systems Engineering Processes and Requirements[041](#_tabs-<p>8</p>), recommends that projects establish Measures of Performance (MOPs), a selected set of which is extended to Technical Performance Measures (TPMs). MOPs are quantitative measures of the system's fitness to satisfy stakeholder expectations. TPMs have the additional characteristic of monitoring performance by comparing a TPM's actual value against time or event-based model of expected values (which are usually derived from histories of previous projects). The architecture description identifies MOPs and TPMs (if any) that relate to the architecture and identify those elements or attributes of the architecture that address these MOPs and TPMs.

The SEI template makes passing reference to “performance characteristics” and to “measure” but does not call for its description in any section. However, that SEI may use the term “behavior” as a general term that encompasses performance. Perhaps the Behavior and Constraints subsections of Section 3.1.5 in the SEI Template collectively address this issue.

*Examples:*

* The system must be able to sustain a downlink data rate of 300 Kbps.
* The system must initiate the execution of a real-time command within 1 second of receipt.

## 4.9 Architectural Decisions and Rationale

Architecting is a process of understanding the problem, evaluating possible solutions, and making decisions about design. A good approach to developing a software architecture does not present it as a *fait accompli*, a fact. An architecture description will identify the big decisions and *substantiate* them. The rationale is hugely important to those who come aboard a project later and is hugely important to future architects who may consider reusing an architecture. Software architecture decisions can be driven by the hardware (or avionics) designs. The project should design an architecture that may have to handle late changes including hardware problems that need to be fixed in software.

The SEI template calls for architecture rationale in two places: Section 2.2.1 (Architectural Approaches), and Section 3.i.5.j.5 (Architecture background).

*Examples:*

* Architects for the Core Flight Executive (CFE) software framework decided to provide a publish/subscribe software bus and to clearly distinguish its application program interface (API) from possible implementations. It's important that an architecture description identifies and explains major decisions such as this, including limitations as well as benefits.
* One flight project designed a component-based software architecture in order to make software subsystems more testable and maintainable by virtue of architecturally-prescribed interfaces. The decision facilitated on-orbit FSW updates by reducing the amount of data to uplink.

## 4.10 Architectural Alternatives (Trade Studies)

While it’s good to state the big architectural decisions, it’s even better to describe what alternatives were considered. This may occur naturally in providing the rationale, especially if a decision is the result of a careful trade study. Descriptions of alternatives don’t have to be elaborate; often, readers simply want to know what plausible alternatives were considered and why they were found to be less suitable. This provides evidence that all solutions have been considered.

Sometimes an alternative is so appealing—but so radical—that a prototype must be built and demonstrated in order to get serious consideration from stakeholders. In those cases, the architectural description describes the prototype and its results, as an objective comparison between the old way and new way.

Trade studies and their results are called for in Section 2.2.1 (Architectural Approaches) and Section 2.2.2 (Analysis Results) of the SEI template.

*Examples:*

* The choice between centralized and distributed processing often has wide-ranging effects on quality attributes and is therefore often subject to a trade study.
* The Radiation Belt Storm Probe (RBSP) project conducted a flight software trade study to compare a software bus architecture (using cFE) to a more “traditional” architecture having tightly coupled inter-task communication.
* Some missions have conducted trade studies concerning the software-based portion of fault protection. Does fault protection go in the “main” processor, or does part of it reside in a separate, simpler processor (or even in a field-programmable gate array (FPGA))?

## 4.11 Multiple Views

An architecture description must address the diverse concerns of its stakeholders. An architecture description must address how the design satisfies functional requirements, but there are *many* other concerns such as cost, schedule, assembly, integration, verifiability, operability, and maintainability. Different concerns require different views of the architecture — views such as structure, behavior, deployment, and operation. The key is to create views that not only address stakeholder concerns but also clearly convey the ideas to the stakeholders. Some views can be well described in the diagrams of unified modeling language (UML), object management groups (OMG), systems modeling language (SysML), and architecture analysis & design language (AADL), but architecture descriptions need not be restricted to such diagrams. There is no singular solution, use what is best for the message being conveyed.

The SEI template is inherently organized for multiple views in Section 3 (Views) and Section 4 (Relations Among Views).

*Examples of useful views*:

* Run-time: Components with Data Flows.
* Compile-time: module structure (source code tree), layers.
* Fault containment regions.
* Bus traffic is shown in terms of average and peak message rate and data volume.
* Deployment: diagrams to document the deployment of software components onto the hardware and/or OS of the target system. This would include an indication of processes utilized, threading, and partitions (if applicable). It would cover process and thread creation and scheduling to document how the software will be deployed on the target system and meet any timing, availability, or other system requirements.

See *4.13* *Architecture Frameworks (Views and Viewpoints)* for additional ideas.

## 4.12 Diagrams and Legends

The purpose of every diagram is to visually convey important information with a minimum amount of associated explanation. To that end, a diagram will contain a legend that explains what the boxes and lines and other symbols mean. When standard diagrams are used, such as UML or SysML diagrams, it is still helpful to include a notation summary (perhaps as a reference page) for readers and reviewers who are not as familiar with the notations. Also, when a diagram contains acronyms, it’s helpful to include acronym definitions in the legend, even if they are repeated in the glossary. Do not assume that everyone uses the same symbols.

The SEI template makes no mention of diagram legends.

## 4.13 Architecture Frameworks (Views and Viewpoints)

As noted earlier, an architecture description addresses numerous stakeholder concerns. Many architecture thought leaders have organized their thoughts —and architecture descriptions—from different viewpoints, and have developed many architecture frameworks for architects to draw upon. Examples include the Department of Defense Architecture Framework (DoDAF), The British Ministry of Defense Architecture Framework (MoDAF), The Open Group Architecture Framework (TOGAF), Reference Architecture for Space Data Systems (RASDS), Reference Model of Open Distributed Processing (RM-ODP), and Zachman [183](#_tabs-<p>8</p>), [354](#_tabs-<p>8</p>) . Our purpose in mentioning architecture frameworks is not to recommend adherence to a particular framework but simply to point to them as aids in developing views and viewpoints that clearly communicate to stakeholders. In reality, most of this document’s recommendations can be mapped into existing viewpoints.

*Examples:*

Krutchen’s “4+1” view model calls for a logical architecture (what the system provides in terms of services), a process architecture (a set of processes distributed across a set of hardware resources), a development architecture (software module organization on the software development environment), a physical architecture (different physical configurations for development, testing, and deployment), and scenarios (instances of use cases that show the four views working together seamlessly).

The DoDAF 2. 0 [177](#_tabs-<p>8</p>) , organizes architecture descriptions into eight viewpoints named: *Project, Capability, Operational, Services, Systems, Standards, Data and Information,* and *All*, as shown in the following figure.

## 4.14 Heritage Analysis

Most software built for today's missions involve significant "heritage" or "legacy" from an earlier mission, whether in architecture, design, code or reuse of product line software. Such inheritance can be a smart move for projects, but it is critical to understand the differences between the new mission and the earlier mission and the costs and risks of reuse.

The well-known story of Ariane 5 Flight 501 [156](#_tabs-<p>8</p>) offers a cautionary tale. Ariane 5 reused code from Ariane 4 that contained a limitation on the forces it was designed to process, and the greater forces in Ariane 5 caused an arithmetic overflow that resulted in the loss of four spacecraft. The lesson here is that architects must carefully examine any heritage with respect to differences between prior usage and planned usage, and document that analysis in the architecture description. This can be especially challenging since designs are often shaped by unstated assumptions.

Fortunately, NASA’s Earth Science Data Systems Software Reuse Working Group has formalized such evaluations in a document “Reuse Readiness Levels (RRLs)” [Marshall 2010] [016](#_tabs-<p>8</p>) . That document identifies nine topic areas to consider in evaluating a software asset for reuse:

1. Documentation: Information that describes the software asset and how to use it.
2. Extensibility: The ability of the asset to be grown beyond its current context.
3. Intellectual Property: The legal rights for obtaining, using, modifying and distributing the asset.
4. Modularity: The degree of segregation and containment of an asset or component of an asset.
5. Packaging: The methodology and technology for assembling and encapsulating the components of a software asset.
6. Portability: The independence of an asset from platform-specific technologies.
7. Standards Compliance: The adherence of an asset to accepted technology definitions.
8. Support: The amount and type of assistance available to users of the asset.
9. Verification and Testing: The degree to which the functionality and applicability of the asset have been demonstrated.

Surprisingly, the SEI template makes no mention of “heritage software” or “legacy software”. Although the word “reuse” appears in the title of Section 2.3 (Product Line Reuse Considerations), that section is not about reusing existing software, but about making software reusable to support a product line version. The decision to reuse software should be documented in Section 2.2.1 (Architectural Approaches) and the analysis substantiating that decision should be documented in Section 2.2.2 (Analysis Results).

Some questions to address in a heritage analysis:

* If there is major re-use in flight software, to what extent is the avionics hardware being re-used?
* Are the same operations concepts being re-used?
* What is the organizational experience with re-use? Has it produced the claimed benefits in the past? Has re-use in the past required re-use of people?
* What's different from what was done previously?
* Does the area of re-use make sense, given differences between the new mission and the old mission?

See [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) for a broader discussion on heritage or reused software and additional items to consider.

## 4.15 Assumptions and Limitations

Architects recognize that the systems they are architecting might well provide heritage for a future project. As such, it is valuable to document any assumptions underlying architecture and any inherent limitations. Admittedly, this can be difficult because many assumptions are unconsciously made based on mission specifics, resulting in hidden limitations of the system's suitability for future missions.

The SEI template makes passing reference to “assumptions” as externally visible properties, so the rather clear concept of “assumption” gets lost in the common meaning of “properties”. Some treatment of “assumptions” should appear in Section 2.2 (Solution Background) so that known assumptions will get passed along to future architects who need to extend the architecture or apply it in a new context.

*Examples*:

Assumption: Disturbances that the attitude control system must correct for will not exceed 1.5 Newton.

Assumption: The triple-redundant network interface card (NIC) handles qualification and consolidation of raw packets. The software can assume that the raw packets received from the NIC is free of transmission errors; the probability of this assumption being violated (1E-9) is an acceptable risk.

## 4.16 Architectural Principles, Patterns, Invariants, and Rules

Although a system to be built may be large, its architecture can often be described compactly, and more readily understood, in terms of principles that shape the design and architectural patterns that are applied consistently. An architectural pattern, applied uniformly, greatly aids understanding by software designers, developers, and reviewers.

While it is extremely useful to document architecture in terms of principles and patterns, there's no guarantee that downstream designers and developers will consistently adhere to them, meaning that the built system may not possess all the characteristics promised by the architect. As such, it's often important to provide some means for checking adherence to the principles and patterns.

In flight software, architecture patterns are useful to ensure consistent design and interoperable implementation of system functions that cut across subsystems.  These include but are not limited to command & data handling, telemetry, fault management, displays & controls, security, cross-channel exchange, checkpoint & restore, and in-flight updates,

Section 2.2.1 (Architectural Approaches) of the SEI template includes the use of architectural styles or design patterns, and Section 3.1.3 includes patterns.

## 4.17 Fault Management

Fault management has *often* been a source of problems in the integration and testing phase of flight systems, so it should be given suitable attention in architecture descriptions. Fault management encompasses topics that often appear under a variety of names such as fault protection; failure modes and effects analysis (FMEA); fault detection, isolation, and recovery (FDIR); fault detection, diagnostics and response (FDDR); fault detection, notification and response (FDNR), integrated vehicle health management (IVHM); integrated systems health management (ISHM); caution & warning; and aborts. At a minimum, fault management is to be examined in terms of its interactions with the nominal control system and its behavior in the face of concurrent faults and responses. For more information, see the Fault Management Community of Practice on NASA Engineering Network (NEN) [260](#_tabs-<p>8</p>).

See also Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis).

The SEI template makes passing mention of “fault handling” in a general paragraph on software architecture and, once again, lumps an important issue under “externally visible properties”. Architects should make sure that fault management is appropriately addressed (and emphasized) in views of behavior.

## 4.18 Non-Concerns

Systems often have some easy-to-meet requirements, and often build upon mature heritage designs and software. For example, consider a mission that has modest uplink and downlink data rates relative to the proven capabilities of a heritage design that they are reusing and adapting. In that context, downlink data handling might be considered a "non-concern." It is reasonable, and even desirable, to treat these areas of non-concern lightly in the architecture description. However, good practice indicates that such areas first be *identified* as non-concerns, with good explanations as to *why* they are non-concerns. (See *4.14 Heritage Analysis*.)

Non-concerns can be addressed in Section 1.5.1.2 (Stakeholders and Their Concerns Addressed).

## 4.19 Glossary and Acronyms

Architecture descriptions will often be reviewed by people outside the project, or even by people outside NASA. These people won’t necessarily understand all the numerous technical terms and acronyms in use, so a glossary and list of acronyms can be very helpful to readers.

## 4.20 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 5. Common Weaknesses

This section lists common weaknesses seen in architecture descriptions.

## 5.1 Ambiguous Context Diagram

Most architecture descriptions provide a top-level diagram that aims to provide readers with “the big picture”, and while such a diagram is always useful, it is sometimes unclear about the boundaries of the system being described.

## 5.2 Driving Requirements Missing

Every system has driving requirements, but when they are not clearly identified, readers have to infer what they are from other statements.

## 5.3 Architectural Decisions and Rationale Not Identified

The architecture is presented as a *fait accompli*, a fact, with no mention of the decisions that were made and their rationale.

## 5.4 Inappropriate Detail

Avoid description details that are inappropriate to the system, as defined in the context diagram. Such details might be about entities *outside* of the system, or might be details about subsystem internals that, while interesting, are not relevant to the system’s architecture.

## 5.5 Unequal Coverage of Software Functionality

Setting aside non-concerns, the document doesn't give equal coverage to its subsystems.

## 5.6 Too Lengthy

Some architecture descriptions are so huge (hundreds of pages) that it’s hard to see the essential architectural concepts amidst all the details. A system may be big, but the architectural concepts governing it should be describable more succinctly.

## 5.7 Important Information Buried

Anything that strongly influences architectural decisions should be clearly identified upfront, whether as a driving requirement or constraint or concern of an influential stakeholder. It’s annoying to readers when any such material is buried in subsection and has to be “discovered”. One document, for example, had a statement in a fifth-level subsection about how their program office regarded a particular approach as crucial to success.

## 5.8 Diagram Lacks Legend

Diagrams that lack legends can be confusing to and/or misinterpreted by readers. Often, authors erroneously assume that the meanings of their boxes and lines are obvious, or that color distinction and solid-versus-dashed lines are obvious. Diagrams that adhere to a standard such as UML or SysML or AADL do not need a legend on each diagram, but it is very useful to provide a notation summary as a reminder for reviewers who are less familiar with the standard.

## 5.9 Software Security Considerations

Software security can be helped by the architecture of the software system, but it can also be hindered.  Considering how the software needs to be patched for vulnerabilities or providing methods for encryption, verification, availability, authentication, and other security concepts may seem daunting, but they are required to be considered in a digital world.

## 5.10 Real-Time Considerations

Real-time reactive software often appears in NASA systems classified as Class A, B, or C.  Qualities of real-time and determinism may not be identified directly as driving requirements but may take the form of deadlines or bounds on latency. Therefore, architectures may neglect including views that describe how the software manages real-time execution, real-time communications, and deterministic operation. These views often describe clock management, decomposition into processes (tasks), process scheduling, inter-process communication, and interfaces with sources or sinks of real-time data.

## 5.11 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 6. Example Outlines

Although the purpose of this document is to recommend *content* in architecture descriptions, some readers have asked for an example outline. Accordingly, this section shows three outlines from different sources. It is not our intent to endorse these outlines, but rather to show some thoughtful examples.

## 6.1 Example Outline (SEI Template)

The outline below is based on the SEI’s “Views and Beyond” method for documenting software architectures, as described in Clements, et al. [295](#_tabs-<p>8</p>). The Software Engineering Institute’s architecture web site provides a template, available as a free download [296](#_tabs-<p>8</p>), that describes in detail what each section typically contains. Even if using a different outline, the SEI template is worth reading.

**1   Documentation Roadmap**

**1.1     Document Management and Configuration Control Information**

**1.2     Purpose and Scope of the SAD**

**1.3     How the SAD is Organized**

**1.4     Stakeholder Representation**

**1.5     Viewpoint Definitions**

1.5.1     <Insert name of viewpoint> Viewpoint Definition

1.5.1.1      Abstract

1.5.1.2      Stakeholders and Their Concerns Addressed

1.5.1.3      Elements, Relations, Properties, and Constraints

1.5.1.4      Language(s) to Model/Represent Conforming Views

1.5.1.5      Applicable Evaluation/Analysis Techniques and Consistency/Completeness Criteria

1.5.1.6      Viewpoint Source

**1.6      How a View is Documented**

**1.7      Relationship to Other SADs**

**1.8      Process of Updating this SAD**

**2   Architecture Background**

**2.1     Problem Background**

2.1.1      System Overview

2.1.2      Goals and Context

2.1.3      Significant Driving Requirements

**2.2     Solution Background**

2.2.1      Architectural Approaches

2.2.2      Analysis Results

2.2.3      Requirements Coverage

2.2.4      Summary of Background Changes Reflected in Current Version

**2.3     Product Line Reuse Considerations**

**3   Views**

**3.1     <Insert View Name> View**

3.1.1      View Description

3.1.2      View Packet Overview

3.1.3      Architecture Background

3.1.4      Variability Mechanisms

3.1.5      View Packets

3.1.5.1      View packet # j

3.1.5.1.1      Primary Presentation

3.1.5.1.2      Element Catalog

3.1.5.1.3      Context Diagram

3.1.5.1.4      Variability Mechanisms

3.1.5.1.5      Architecture Background

3.1.5.1.6      Related View Packets

**4   Relations Among Views**

**4.1     General Relations Among Views**

**4.2     View-to-View Relations**

**5   Referenced Materials**

**6   Directory**

**6.1     Index**

**6.2     Glossary**

**6.3     Acronym List**

**7   Sample Figures & Tables**

## 6.2 Example Outline: TestGen

Students in a software architecture class taught by Prof. David Garlan (Carnegie Mellon University) prepared the architecture description document whose outline is shown below. The document describes “TestGen”, a tool to help a test engineer create test suites conforming to ISO/IEC Standard 9646-3: 1998 regarding open systems in information technology [455](#_tabs-<p>8</p>).

1 Introduction

    1.1 TestGen System  
    1.2 Business Context

2 Architectural Drivers  
    2.1 Functional Requirements  
    2.2 Constraints  
    2.3 Quality Attributes

3 Architectural Decisions  
    3.1 To Use the Traditional Structure of a Compiler  
    3.2 To include all BNF Grammar in the Parser  
...  
    3.7 To Use a Visitor Pattern  
    3.8 To Divide the Generation Part and Formatting Part

4 Component & Connector Architectural View  
    4.1 Component & Connector view-type and its style(s)  
    4.2 C & C View: Data-shared Style and Call-return Style

5 Module Architectural View  
    5.1 Module View-type and its style(s)  
    5.2 Module View: Decomposition Style

6 Allocation Architectural View  
    6.1 Allocation View-type and its Style(s)  
    6.2 Allocation View: Implementation Style

7 Mapping Between Architectural Views

8 Architectural Alternatives  
    8.1 Code Generation: Static vs. Dynamic  
    8.2 C Code Formatting: COTS formatter vs. internal formatter  
    8.3 Rule Description: Translation Rule File vs. Rule Engine

9 Architectural Approach Analysis  
    9.1 Scenario 1: To generate C code understandable for a test engineer  
    9.2 Scenario 2: To find a reason for failure for a test engineer  
    9.3 Scenario 6: To include additional functions  
    9.4 Tradeoff Summary

10 Future Extension

11 ATAM Process Evaluation

12 Appendix  
    12.1 Glossary  
    12.2 References  
    12.3 Quality Scenarios  
    12.4 Acme Textual Description  
    12.5 FSP Source

## 6.3 Example Outline: SMAP

The Soil Moisture Active Passive (SMAP ) mission is an Earth-orbiting science mission with the objective of providing three years of measurements of soil moisture and soil freeze/thaw state over the entire globe. The outline shown below was used in the SMAP architecture description document, authored by Alex Murray (JPL), which was formally reviewed by the NASA Software Architecture Review Board [323](#_tabs-<p>8</p>).

|  |  |
| --- | --- |
|  | |
| **Introduction** |  |
| Mission Overview | Mention heritage |
| Document Overview | Describes the structure of the document.  Also tips for using it, like "right-click to keep a window with this diagram up for later reference" |
| Architectural Approach | Describe the architectural method, e.g., Krutchen 4+1, etc. |
| **Architectural Drivers** |  |
| Stakeholders | Identify and describe concerns and also the method of inputs.   Concerns are operational (e.g. FSW reliability) as well as programmatic (low schedule risk) |
| Key Decisions | MSAP heritage, (implies CPU and its limitations, hardware, and their limitations) |
| Driving Requirements | This section should show the key requirements, and also explain how the architecture supports them. |
| Trade Studies | C vs. C++, Component Architecture, Real Time Processes |
| **Quality Analysis** |  |
| Attributes | What are they, how is each defined, what are the "Figures of Merit" - measures of evaluating how well the QA is achieved |
| Prioritizations | Ranking of QAs based on Stakeholder concerns |
| Realization | How does our architecture (in the largest sense) achieve the QAs in the FSW product? |
| **Environment** | IEEE1471 uses "environment" |
| Context | Logical and physical context diagrams  Enumerate and characterize data flows  Crude whack at volumes/rates across external interfaces |
| Interactions | Show interaction with the environment, in the context of executing Key Requirements in behavior diagrams |
| **FSW Architecture** | This is the FSW Architecture model (parts of it), showing the top-level design and key patterns. |
| Principles | Guiding principles for software architecture and design |
| Constraints | Design constraints (modeling constraints, coding standards),  includes checklists in modeling (including test models) and development |
| Patterns | Key patterns: Init, Components and connectors, IPC, Threads, Layering |
| Design Trades | This package will describe some of the key design trades that we have done. |
| **Views** |  |
| Run Time | Run-time structure (components with data flows) |
| MSAP Views | Run-time structure of MSAP (components with data flows) |
| Compile Time | Module structure (source code tree)  Layers expressed in terms of dependencies |
| Deployment | Show object libraries on the NVM, the SUROM, etc. |
| Components | This gives a little high-level look at a few key components |
| ACS Component | This is a key component in that it is responsible for implementing requirements included in the Key requirements section. |
| Fp Component | This is a key component in that it is responsible for implementing requirements included in the Key requirements section. |
| **Development Process** | We need this section to show how our process supports realizing the QAs |
| Artifacts | Outputs and internal products.  Outputs related to stakeholders' concerns. |
| Config Management | This contributes to the lessening of schedule risk, as well as reliability and maintainability |
| Standards | This section talks about the kinds of standards and constraints we use, and how we check them (show coding standards, design constraints as an artifact.  Talk about standard enforcement (represent as activities) |
| Task Control | Contributes to the monitoring of schedule risk |
| Verification | Need to get a system-level test pattern done for this.  Also, show an example of mapping L4s to a test. |
| Methodology | Describes our approach to verifying the system level requirements (Level 4) |
| Test Scenarios | Just the beginning of a list of scenarios needed to verify the requirements |
| Analyses | A package containing analysis scenarios that verify requirements that are not amenable to test verification. |

## 6.4 Additional Guidance

See also [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture), and topic [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description).

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 7. Quality Attribute Table

Linked below for download is the Quality Attribute Table developed by NASA’s Software Architecture Review Board. The table lists fourteen key quality attributes, identifies different important aspects of each quality attribute and considers each aspect in terms of requirements, rationale, evidence, and tactics to achieve the aspect. It is intended to serve as a guide to software architects, software developers, and software architecture reviewers in the domain of mission-critical real-time embedded systems, such as space mission flight software. **Download this spreadsheet to obtain a usable copy**.

[Quality Attribute Spreadsheet 2016.xlsx](#)

## 7.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 8. Resources

## 8.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-010)

  [Software Architecture Document (template).](http://www.sei.cmu.edu/downloads/sad/SAD_template_05Feb2006.dot "Click to open in new window")

  Software Engineering Institute, CMU, Feb. 2006.
* (SWEREF-016)

  [Reuse Readiness Levels (RRLs).](https://earthdata.nasa.gov/files/RRLs_v1.0.pdf "Click to open in new window")

  James J. Marshall, editor, 2010. Prepared by NASA Earth Science Data Systems – Software Reuse Working Group. Marshall 2011 Retrieved July, 2016 from https://earthdata.nasa.gov/files/RRLs\_v1.0.pdf.
* (SWEREF-021)

  [The 4+1 View Model of Architecture.](https://en.wikipedia.org/wiki/4%2B1_architectural_view_model "Click to open in new window")

  Philippe B. Kruchten. 1995
* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-156)

  [Cluster (spacecraft),](http://en.wikipedia.org/w/index.php?title=Cluster_%28spacecraft%29&oldid=481296441 "Click to open in new window")

  2012, March 11. In Wikipedia, The Free Encyclopedia. Retrieved 18:29, March 19, 2012, from http://en.wikipedia.org/w/index.php?title=Cluster\_(spacecraft)&oldid=481296441 Note: Wikipedia disambiguous link rerout from topic: Ariane\_5\_Flight\_501
* (SWEREF-177)

  [The DoDAF Architecture Framework Version 2.02](http://dodcio.defense.gov/Library/DoD-Architecture-Framework/ "Click to open in new window")
* (SWEREF-183)

  [Enterprise architecture framework.](https://en.wikipedia.org/wiki/Enterprise_architecture_framework "Click to open in new window")

   In Wikipedia, The Free Encyclopedia (6 April 2019).
* (SWEREF-210)

  [IEEE Computer Society, "Systems and Software Engineering--Recommended Practice for Architectural Description of Software-Intensive Systems,](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4278472 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1471-2000 ( ISO/IEC 42010:2007), 2007. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-239)

  [Software Architecture in Practice,](https://jegadeesansite.files.wordpress.com/2018/01/sei-series-in-software-engineering-len-bass-paul-clements-rick-kazman-software-architecture-in-practice-addison-wesley-professional-2012.pdf "Click to open in new window")

  Len Bass, Paul Clements, and Rick Kazman, 2003. Second Edition. Addison-Wesley.
* (SWEREF-260)

  [NASA Fault Management Community of Practice](https://nen.nasa.gov/web/faultmanagement "Click to open in new window")

  This NASA-only resource is available to NASA-users at https://nen.nasa.gov/web/faultmanagement.
* (SWEREF-295)

  [Documenting Software Architectures: Views and Beyond, Second Edition,](http://www.sei.cmu.edu/library/abstracts/books/0321552687.cfm "Click to open in new window")

  Clements, P., et al. Addison-Wesley, 2011. Available for purchase at various locations.
* (SWEREF-296)

  ["Views and Beyond: The SEI Approach to Architecture Documentation"](http://www.sei.cmu.edu/architecture/tools/document/viewsandbeyond.cfm "Click to open in new window")

  (2012). Software Engineering Institute (SEI). Carnegie-Mellon University. Retrieved April 13, 2012 from link listed here.
* (SWEREF-323)

  [Software Architecture Review Board sub-community of practice.](https://nen.nasa.gov/web/sarb "Click to open in new window")

  The objectives of SARB are to manage and/or reduce flight software complexity through better software architecture and help improve mission software reliability and save costs.
* (SWEREF-327)

  [Published Appraisal Results (PAR).](https://cmmiinstitute.com/pars/ "Click to open in new window")

  Software Engineering Institute (SEI), architecture web site.
* (SWEREF-354)

  [View Model,](http://en.wikipedia.org/w/index.php?title=View_model&oldid=473612428 "Click to open in new window")

  In Wikipedia, The Free Encyclopedia. (2012, January 28).  Retrieved 18:33, March 19, 2012, from http://en.wikipedia.org/w/index.php?title=View\_model&oldid=473612428
* (SWEREF-455)

  [Information technology -- Open Systems Interconnection -- Conformance testing methodology and framework -- Part 3: The Tree and Tabular Combined Notation (TTCN).](http://www.iso.org/iso/home/store/catalogue_ics/catalogue_detail_ics.htm?ics1=35&ics2=100&ics3=01&csnumber=30621 "Click to open in new window")

  ISO/IEC 9646-3:1998. Must be purchased from the International Organization for Standardization (ISO); no free copy or access via NASA Technical Standards site available.
* (SWEREF-499)

  [Views and Beyond: The SEI Approach to Architecture Documentation.](http://www.sei.cmu.edu/architecture/tools/document/viewsandbeyond.cfm "Click to open in new window")

  Software Engineering Institute website. Carnegie-Mellon University. Retrieved July, 2016 from http://www.sei.cmu.edu/architecture/tools/document/viewsandbeyond.cfm.
* (SWEREF-571)

  [NASA Study of Flight Software Complexity](https://llis.nasa.gov/lesson/2050 "Click to open in new window")

  Public Lessons Learned Entry: 2050.

  

## 8.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 8.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture)        * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) |

## 8.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>8</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 8.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

# 9. Lessons Learned

### 9.1 NASA Lessons Learned

A documented lesson from the NASA Lessons Learned database notes the following:

* **NASA Study of Flight Software Complexity: Lesson Learned 2050[571](#_tabs-<p>8</p>)**.  "Flight software development problems led NASA to study the factors that have led to the accelerating growth in flight software size and complexity. The March 2009 report on the NASA Study on Flight Software Complexity contains recommendations in the areas of systems engineering, software architecture, testing, and project management."

### 9.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
