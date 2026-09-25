# 9.01 Software Design Principles

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695790. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles

9.01 Software Design Principles

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695790)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695790&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Software Principles at NASA](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Software Principles at NASA

This topic contains the Guiding Principles that have been built over the years at NASA. These Principles are designed to help projects be successful by reducing the likelihood of defects.

1. The software design principles presented here represent a consensus view of best practices in the design of mission-critical Class A and B software at NASA. They were selected with participation from several Centers, representing the major disciplines in embedded real-time software: launch systems, manned systems, and robotic missions.
2. The design principles focus on features and characteristics that are typically found in high-quality embedded software applications. They should be familiar to the experienced embedded software professional. However, they include only those principles that were deemed common across all Centers and disciplines. In the course of development, many good ideas were not selected for inclusion because they were specific to a particular mission or application type. However, application-specific approaches and interpretations are included in the discussion section accompanying each principle to convey the kinds of variations that might be introduced.
3. It is important to understand what the design principles are, and what they are not. They are a distillation of decades of experience in the kind of embedded software that has enabled NASA’s most spectacular achievements. They can be used as a source of design criteria both in development and at review time. Training materials for new developers can draw upon them. Individual projects and organizations can use them as a reference in the development and implementation of local standards and processes.
4. The design principles are not requirements. They do not supersede design principles already in place at NASA Centers. There is no requirement to justify using a different set of design standards, nor are waivers for deviation from the principles required. The design principles here are not a complete statement about what makes for good embedded software design. Organizations and projects that choose to adopt them are encouraged to tailor and elaborate these principles to their specific situation.

### 1.1 Structure of the Software Principle Topics

Principle statements are deliberately brief to avoid including the detail that might not be universally applicable. Each principle has a short rationale that expresses why it was considered important enough to include in the Agency-wide set of design principles.

Following this is a section entitled “Examples and Discussion” that elaborates on the principle. Depending on the topic, this section may provide life cycle guidance, discussion of techniques commonly used to implement the principle, and implementation considerations.

When applicable entries from the NASA Lessons Learned [439](#_tabs-<p>2</p>) database are available, links to these entries are also included in the Examples and Discussion section. Lessons Learned often highlight a subtle aspect of a design principle or identify an opportunity to consider how the application of a principle might have helped avoid an incident. In a handful of cases, there are positive lessons learned that support adoption of the related principle.

Each principle was derived from one or more source materials. Where this material is not included in the Examples and Discussion section, it is included in a concluding section entitled “Inputs”. Inputs may be from works in progress furnished to the team, or from official standards. The Center responsible for the input material is identified by a subheading preceding that Center’s material.

Each principle has the same basic structure:

1. Principle and Rationale - a simple statement of the principle together with a short explanation of why the principle is important.
2. Examples - detailed description and discussion of the principle from an engineering perspective. Includes an analysis of the supporting data.
3. Inputs - Additional material usually from one or more Centers. Includes Center specific application of the principle.
4. Resources - List of resources referenced in one or more tabs on the page, with links to the actual reference.
5. Lessons Learned - descriptions and links to the appropriate Lessons Learned referenced on the page.

|  |  |
| --- | --- |
| * [9.03 Coding Standards](/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards) | Implement a "secure" coding standard on all mission-critical software. |
| * [9.04 Command Receipt Acknowledgement](/spaces/SWEHBVD/pages/102695795/9.04+Command+Receipt+Acknowledgement) | Design software to send a positive acknowledgement of command receipt. |
| * [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) | Design software to verify the integrity of all inputs and outputs in the control system |
| * [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion) | Establish a policy for eliminating unreachable code or mitigating the risk of any unreachable code. |
| * [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) | In the software design, provide mechanisms to detect credible system faults and to react to these faults according to a pre-described plan. |
| * [9.08 Flight Software Modification](/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification) | Include in the software design the capability for commanding modification of the software, and for preventing unwanted modifications. |
| * [9.09 Incorrect Memory Use or Access](/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access) | Design software to protect against incorrect use of memory. |
| * [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode) | Design flight software to initialize software and hardware to a known, safe, and deliberate state |
| * [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) | Design software to handle invalid data appropriately. |
| * [9.12 Resource Margins](/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins) | Establish and maintain quantitative margins for all critical resources, allowing for maturation of usage estimates through the life cycle. |
| * [9.13 Resource Oversubscription](/spaces/SWEHBVD/pages/102695804/9.13+Resource+Oversubscription) | Include a robust and well thought out response to resource oversubscription situations in the software design. |
| * [9.14 Resource Usage Measurement](/spaces/SWEHBVD/pages/102695805/9.14+Resource+Usage+Measurement) | Incorporate timely visibility into the use of computing resources into the software design. |
| * [9.15 Safe Transitions](/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions) | Assert required preconditions and post-conditions at software transitions. |
| * [9.16 Thread Safety](/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety) | Design interaction between threads to prevent inappropriate interference. |
| * [9.17 Toggle Commands](/spaces/SWEHBVD/pages/102695808/9.17+Toggle+Commands) | Design both internal and external commanding to place the system into an explicitly specified state. |

### 1.2 Support for NASA Software Safety Standard

* The NASA software design principles provide considerable support for the implementation of the NASA software safety requirements found in the NASA Procedural Requirement for software engineering (NPR 7150.2, [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) ). It may be possible to demonstrate compliance for the design-related parts of the requirement through verified adherence to the design principles. See [9.02 Software Safety and Design Principles](/spaces/SWEHBVD/pages/102695792/9.02+Software+Safety+and+Design+Principles) for a compliance matrix and discussion.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-670)

  [Space Flight System Design and Environmental Test](https://www.nasa.gov/sites/default/files/atoms/files/std8070.1.pdf "Click to open in new window")

  ARC - APR 8070.1 This document defines engineering design and environmental test requirements and guidelines for Class C and D space flight systems.
* (SWEREF-671)

  [JPL-D-17868 (REV.1), JPL GUIDELINE: DESIGN, VERIFICATION/VALIDATION AND OPERATIONS PRINCIPLES FOR FLIGHT SYSTEMS (16 FEB 2001)](http://everyspec.com/NASA/NASA-JPL/JPL-D-178686362/ "Click to open in new window")

  JPL: DocID 43913, Rev. 1
* (SWEREF-672)

  [Rules for the Design, Development, Verification, and Operation of Flight Systems](https://nen.nasa.gov/documents/14202/1030520/GSFC+Gold+Rules+/de80ff63-aa7e-43a3-ab39-b2deafa37db1 "Click to open in new window")

  GSFC-STD-1000F, Approved: 02-08-2013 - With Administrative Changes , Expiration Date: 02-08-2018, Superseding GSFC-STD-1000E

Caveat on using JPL rules:   
  
Some of you may be interested in viewing standards recently made available to NASA civil servants. They are JPL Flight Project Practices; JPL Design, Verification/Validation & Ops Principles for Flight Systems (Design Principles); and JPL Systems Engineering Practices. Please keep in mind that these documents are labeled as confidential/proprietary and should be handled according to SBU procedures. JPL has lessons learned infusion process that cross-references lessons learned directly to JPL’s two mandatory core engineering standards – and you might be interested in reviewing the JPL process as guidance for your Centers lessons learned infusion.

## 2.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)        * [9.02 Software Safety and Design Principles](/spaces/SWEHBVD/pages/102695792/9.02+Software+Safety+and+Design+Principles) * [9.03 Coding Standards](/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards) * [9.04 Command Receipt Acknowledgement](/spaces/SWEHBVD/pages/102695795/9.04+Command+Receipt+Acknowledgement) * [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) * [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion) * [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) * [9.08 Flight Software Modification](/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification) * [9.09 Incorrect Memory Use or Access](/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access) * [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode) * [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) * [9.12 Resource Margins](/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins) * [9.13 Resource Oversubscription](/spaces/SWEHBVD/pages/102695804/9.13+Resource+Oversubscription) * [9.14 Resource Usage Measurement](/spaces/SWEHBVD/pages/102695805/9.14+Resource+Usage+Measurement) * [9.15 Safe Transitions](/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions) * [9.16 Thread Safety](/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety) * [9.17 Toggle Commands](/spaces/SWEHBVD/pages/102695808/9.17+Toggle+Commands) |

## 2.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 2.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |
