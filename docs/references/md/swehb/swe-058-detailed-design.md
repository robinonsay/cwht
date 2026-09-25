# SWE-058 - Detailed Design

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695443. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design

SWE-058 - Detailed Design

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695443)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695443&showCommentArea=true&showComments=true#addcomment)

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

4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-058 History

SWE-058 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.2.3 The project shall develop, record, and maintain a detailed design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. |
| Difference between A and B | Descoped from a detailed design to just a design;  otherwise, no change |
| B | 4.3.3 The project manager  shall develop, record, and maintain a design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. |
| Difference between B and C | Changed "design" to "software design". |
| C | 4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. |
| Difference between C and D | No change |
| D | 4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. |

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
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

# 2. Rationale

The detailed design, as an extension of the architectural design, provides detailed descriptions of the lowest level of software components. The detailed design provides enough information for someone to create code without significant interpretation. The design maintains consistency with design standards, programming language dependencies, and external interfaces. Any redesign or maintenance of the software work product anywhere in the life cycle must also conform to the detailed design to avoid software performance degradation or error issues. The documentation of the design and descriptions of the lower-level components enables other members of the team to base their activities on previous versions to assure successful coding, compiling, and testing.

Recording, which may be textual, visual, or a combination, allows for the design to be inspected to ensure that the design meets the project's requirements and architectural design. The design also needs to be maintained to assure updates are completed, and to assist in future modifications to the software.

This requirement ensures that the transition from high-level software architecture to lower-level implementable units is systematic, traceable, and adequately documented, enabling efficient coding, testing, and integration. It directly supports the successful implementation of software systems that align with mission requirements, safety standards, quality attributes, and operational goals. Below is the detailed rationale for this requirement.

---

### **1. Bridging the Gap Between Architecture and Implementation**

Software architecture describes the system's high-level structure and interactions between major components. However, to implement the system, architecture needs to be broken down into **detailed software design** that:

* Defines **lower-level units** (such as modules, classes, functions, and algorithms).
* Specifies **interfaces** between components and subsystems.
* Provides **detailed instructions** enabling coding, testing, and integration.

Without a detailed design derived from the architecture, developers may interpret the architecture inconsistently, leading to:

* **Misaligned implementations:** Developers may implement features incorrectly or deviate from architectural intent.
* **Integration problems:** Undefined or poorly designed interfaces can result in mismatched components or system-wide failures during integration.

Adopting a structured and detailed software design ensures that architectural specifications are translated consistently into implementable code.

---

### **2. Enabling Efficient and Accurate Development**

Detailed software design provides the necessary technical details for developers to proceed confidently with coding. These details include:

* **Logical structures:** Flowcharts, algorithms, and functional descriptions of how lower-level units behave.
* **Interface specifications:** Definitions for how components will communicate internally and externally (e.g., APIs, protocols, data formats).
* **Design constraints:** Considerations for performance, memory usage, real-time requirements, and hardware limitations.

By providing explicit guidance for coding, the risk of **ambiguities and misunderstandings** is minimized, resulting in:

* Faster and more accurate development.
* Reduced need for backtracking and rework during implementation.

---

### **3. Supporting Verification and Testing**

A testable design ensures that the lower-level units can be efficiently evaluated for correctness and compliance. Detailed software design enables:

1. **Unit Testing:**  
   Clear definitions of units at the design level (e.g., functions, modules, classes) allow corresponding tests to focus on verifying each unit for:

   * Correct functionality.
   * Interface compliance.
   * Alignment with requirements.
2. **Integration Testing:**  
   Defined interfaces ensure that software units can be integrated with minimal risks of incompatibility or communication errors between components.
3. **Traceability to Requirements:**  
   A well-maintained design links each code unit back to system-level and software-level requirements, enabling effective validation of both design and implementation. This reduces the risk of requirements drift or gaps.

---

### **4. Improving System Reliability**

System reliability depends on how well the software design anticipates risks and adheres to high-level architecture. A detailed design ensures that:

* **Fault tolerance mechanisms** defined at the architectural level (e.g., redundancy, error handling) are implemented consistently in individual units.
* **Critical paths** are addressed at the design level to ensure performance, scalability, and reliability.
* **Safety-critical functions** are correctly implemented and thoroughly tested, aligning with hazard mitigation strategies identified in safety analyses.

By maintaining detailed design documentation, reliability is preserved throughout development lifecycles, as corrective actions can be tracked and validated.

---

### **5. Supporting Software Maintenance and Evolution**

Software systems evolve over time due to changes in mission needs, hardware updates, or corrected defects. A detailed and well-documented design:

1. Provides **maintenance teams** with accessible information about system structure, dependencies, interfaces, and behavior, enabling:

   * Improved troubleshooting and defect correction.
   * Incremental updates with reduced risks of creating unintended issues.
2. Facilitates **system evolution** by clearly describing design decisions, allowing new functionality to be integrated without destabilizing the existing system.

A lack of detailed design documentation can result in **poor maintainability, increased costs, and higher risks of introducing errors during updates.**

---

### **6. Supporting Project Management and Accountability**

Recording and maintaining the software design serves as objective evidence that:

1. The software development process adheres to prescribed standards.
2. The project team has sufficiently analyzed system requirements and risks to arrive at a robust design.
3. Design decisions are traceable, providing stakeholders with transparency and accountability.
4. Future audits or evaluations have access to documentation that demonstrates compliance with NASA standards.

---

### **7. Addressing Complexity in NASA Missions**

Software for NASA missions often involves **high complexity**, including:

* Safety-critical functions requiring detailed attention to fault management and error isolation.
* Real-time performance requirements for spacecraft operations, navigation, and data processing.
* Tight integration with hardware (e.g., onboard sensors, actuators, telemetry systems).

Detailed design ensures that lower-level units are capable of addressing these complexities while adhering to architectural constraints and system requirements. For example:

* In safety-critical systems (like crewed spacecraft), design details ensure risk mitigation mechanisms (e.g., watchdog timers, redundancy) are correctly implemented.
* In scientific instruments (e.g., space telescopes), algorithms for data collection and preprocessing are carefully planned to avoid operational inefficiencies.

---

### **8. Supporting Traceability and NASA Standards**

Maintaining a detailed software design aligns with NASA's requirements for traceability, adherence to standards, and lifecycle documentation. The design document ensures compliance with:

* **NPR 7150.2:** Software Engineering Requirements, which requires structured progression from architecture to design to implementation.
* **SWE-058:** Requirements traceability to ensure all units and components are mapped back to their requirements and maintain alignment.
* **SWE-057:** Architecture documentation requirements, validating that lower-level software designs are consistent with the system architecture.

---

### **9. Lessons Learned Supporting This Requirement**

NASA's Lessons Learned database highlights examples that underscore the importance of detailed design derived from architecture:

#### **Mars Climate Orbiter Failure (1999)**:

Failure due to inconsistent unit systems (imperial vs. metric) between subsystems was rooted in poor design traceability and insufficient documentation between lower-level components.  
**Recommendation:** Ensure detailed design documentation specifies all dependencies, interfaces, and conventions to prevent misalignment or miscommunication during coding and compilation.

#### **MER Spirit Flash Memory Anomaly (2004)**:

Faulty storage allocation from poorly designed COTS parameters highlights the risk of undetailed lower-level design elements.  
**Recommendation:** Ensure design details account for resource allocation and memory use assumptions.

---

### **Conclusion**

Requirement 4.3.2 is vital to ensuring the success of NASA software projects. A software design derived from software architecture and documented in detail is essential for:

1. Transitioning seamlessly from architecture to implementation.
2. Enabling efficient development, verification, and testing.
3. Addressing complexity, maintaining reliability, and ensuring traceability.
4. Supporting maintenance and future evolution of software systems.

Adherence to this requirement reduces risk and ensures the software system meets its performance, safety, and functionality goals, a necessity in the high-stakes environment of NASA missions.

# 3. Guidance

**NPR 7150.2** mandates the detailed software design phase as an essential transition between the architectural design phase and development (coding) activities. The purpose of this phase is to systematically develop a lower-level software design that elaborates on the software architectural design. The detailed design configures software modules, components, interfaces, and data flows to a level sufficient for coding, compiling, and testing.

* **Preliminary Detailed Design:** Addressed during and validated by the **Preliminary Design Review (PDR)**, ensuring readiness to proceed.
* **Baselined Design:** Finalized during the **Critical Design Review (CDR)** to serve as the foundation for implementation.

The design process ensures traceability to requirements, clarity for developers, and builds a framework for maintainable, verifiable, and operational software solutions.

---

## 3.1 Design Readiness

#### **Preliminary Design Readiness (Before Starting Detailed Design Activities)**

Evaluating readiness to proceed to the detailed design phase ensures that teams and processes are adequately prepared. The following processes and artifacts are essential for achieving design readiness:

1. **Establish Design Inputs:**

   * A **documented software architecture definition** (see SWE-057) providing high-level structure, components, and dependencies.
   * A **systems requirements specification (SRS)** (see SWE-049) with defined and traceable software requirements.
2. **Define the Design Process:**

   * A **Software Development Plan (SDP)** and **Software Management Plan (SMP)** (see SWE-013) to outline design phases, outputs, and validation checkpoints.
   * Familiarity with tools, methodologies, coding standards (SWE-061), and applicable guidelines.
3. **Evaluate Team Readiness:**

   * Ensure team members possess training, expertise, and familiarity with development methods and tools (see SWE-017).
   * Confirm that team resources and software reuse options, such as pre-approved commercial off-the-shelf (COTS) software, have been analyzed (SWE-027).
4. **Analyze and Prioritize Alternatives:**

   * Perform an **alternatives analysis** of system architectural options to validate the selected design approach against operational goals.

#### Example Checklist for Readiness:

* Do you have documented milestones for the design process (e.g., entry/exit criteria at PDR, CDR)?
* Have interface definitions between components been finalized?
* Have quality attributes (e.g., performance, security, safety) driving the architecture been evaluated and incorporated into the design approach?
* Are the design methods consistent with operational constraints and mission goals?

---

## 3.2 Detailed Design Process

#### **Detailed Design Activities**

The detailed design process expands on the architectural definitions by focusing on lower-level components, aligning them with the allocated requirements, and ensuring testability at all levels.

1. **Key Design Outputs:**

   * **Lower-Level Component Definitions:** Each module, class, or function is defined with specific interfaces, processing logic, dependencies, and constraints.
   * **Interface Design:** Define all external/internal software interfaces, their input/output characteristics, and their compatibility (see IDD, SWE-112).
   * **Data Design:** Include all data structures, formats, types, units, ranges, and usage characteristics (see SDD, SWE-058).
2. **Recommended Practices:**

   * **Modularity:** Use well-abstracted, reusable components with high internal **cohesion** (tight scope within functions) and low external **coupling** (minimal dependency between components).
   * **Scalability:** Design with a view toward potential system growth or reuse in future missions.
   * **Documentation:** Maintain clarity with diagrams, pseudocode, or standardized design languages like UML to improve understandability and facilitate reviews.

#### **Component-Specific Considerations**

* **Pre-Existing Components:** In projects using fixed or existing modules (e.g., COTS or reusable components), focus design activities on seamless integration, configuration customization, and addressing constraints of the prebuilt elements.
* **Custom Components:** Precisely define processing logic, inputs/outputs, constraints, and verification strategies tailored to project-specific requirements.

---

## 3.3 Coding Standards and Processes

The coding phase is directly impacted by the practices and standards established during the detailed design phase, including decomposition into smaller modules, specification of logic flows, and consistent implementation practices. To ensure coding readiness:

1. **Establish Coding Practices:**

   * **Maintain Standards (SWE-061):** Clearly define coding standards (e.g., programming languages, comment conventions, style rules) and ensure the design is aligned with these practices. Secure coding practices (SWE-207, SWE-185) must be incorporated.
   * **Portability:** Design interfaces to be adaptable across platforms. Use wrappers or adapters where necessary to ensure reusable components conform to standards.
2. **Reuse Strategies:**

   * Assess existing libraries such as mathematical utilities, database systems, or GUI libraries to determine how they can reduce design complexity while optimizing resources.
3. **Transition to Coding:**

   * Use detailed design documentation (UML diagrams, pseudocode) to establish a seamless progression from design to implementation.
   * Regularly revisit architectural decompositions to ensure design choices continue to meet mission objectives, particularly regarding cohesion and coupling.

---

## 3.4 Progress Reviews and Validation

Regular progress reviews ensure designs are on track, mature, and aligned with project requirements. Design validation includes peer reviews, inspections, and scenario-based evaluations.

#### **Validation Activities:**

* **Design Inspections:** Trace logical workflows in modules to identify weaknesses.
* **Scenario-Based Analysis:** Evaluate how components respond to different stimuli or edge-case conditions.
* **Requirements Traceability:** Verify that every requirement is accounted for in design and every design element maps back to a requirement (see SWE-052).

#### **Review Progress Documentation:**

* Key documentation and templates include:
  + **Software Design Description (SwDD):** Primary reference for architecture and logic definitions.
  + **Interface Design Description (IDD):** Detailed specifications for all data and component interfacing.
  + **Data Dictionary (SDD):** Description of key data elements, structures, and constraints.

---

## 3.5 Maintenance and Iteration

Software detailed design is not static; it evolves in response to changes in requirements, unforeseen constraints, and lessons learned during coding or testing phases.

1. **Adaptive Design Management:**

   * Maintain up-to-date documentation reflecting approved changes in requirements, functionality, or constraints (see SWE-080).
   * Update related test plans, procedures, and reports to align with design changes (see SWE-071).
2. **Configuration Control (SWE-082):**

   * Use established configuration management practices to track changes to design elements, minimizing the risk of introducing errors due to uncoordinated updates.
3. **Long-Term Maintenance:**

   * Document rationale for all major design decisions to simplify future updates, debugging, and reusability of software in subsequent missions.

---

## 3.6 Design Best Practices

* **Emphasize Modularity and Reuse:** Well-abstracted modules improve long-term maintainability and reduce costs for future missions. Components should be reusable wherever feasible.
* **Balance Simplicity and Performance:** Avoid overcomplicated designs that hinder maintainability, while ensuring that design meets mission-critical performance constraints.
* **Documentation as a Key Asset:** Design documentation supports communication between architects, developers, and mission planners and should be clear, concise, and regularly updated.

---

### **Conclusion**

The detailed design process serves as a critical foundation for NASA's software development lifecycle, enabling traceable, testable, and maintainable implementations. By ensuring upfront readiness, validating designs against system requirements, and maintaining strong documentation and configuration control, projects can reduce risks, ensure system reliability, and achieve mission success. Properly implemented software design supports both immediate project needs and long-term objectives, ensuring that NASA's software systems remain robust, scalable, and mission-ready.

A review of the success criteria for Preliminary Design Reviews (PDRs) (see [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)) by the software development team will assure the readiness to proceed to the detailed design phase. The software development team then decides which criteria are necessary for the project.

Consider the following before starting the detailed design:

* Do you have a well-documented software development process (see [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination))?
* Do you understand what is to be performed and produced in each phase of the design process (see [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan))?
* Do you have a software architecture definition document (see [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description))?
* Do you have a systems requirements specification (see [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification))?
* Are you familiar with the methods, tools, standards, and guidelines for your project (see [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards))?
* Are applicable and efficient design methods being implemented on your project?
* Are the developers trained and experienced in the chosen development process and methods (see [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training))?
* Is software reuse being considered throughout the development effort (see [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software))?
* Is off-the-shelf software being considered for use on the project (see [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software))?
* Has an analysis of alternatives been completed?
* Is the selection of architecture and design methods based on system operational characteristics?

Consider the following during detailed design:

* Are CASE tools being used to assist and document the design effort (see [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation))?
* Does your design process include a robust configuration control process (see [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan))?
* Is the design effort being properly documented? (see [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)) Is it adequate but not burdensome?
* Is your team committed to following the design process?
* Are all requirements traceable to design elements (see [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability))?
* Are all design elements traceable to specific requirements?
* Have all software work products (components, units, systems) been identified (see [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan))?
* Are the characteristics of all data elements identified (type, format, size, units, and others important to the project) (see [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary))?

See also [PAT-014 - Architecture Design Checklist](/spaces/SITE/pages/114328318/PAT-014+-+Architecture+Design+Checklist), [PAT-015 - Detailed Design Checklist](/spaces/SITE/pages/114328341/PAT-015+-+Detailed+Design+Checklist), [PAT-031 - Critical Design Analysis Checklist](/spaces/SITE/pages/123600967/PAT-031+-+Critical+Design+Analysis+Checklist),

See also [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices),

See also [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access), [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification),

3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)       * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [PAT-006 - Design Practices for Safety](/spaces/SITE/pages/114327707/PAT-006+-+Design+Practices+for+Safety) * [PAT-015 - Detailed Design Checklist](/spaces/SITE/pages/114328341/PAT-015+-+Detailed+Design+Checklist) * [PAT-016 - Functional Design Checklist](/spaces/SITE/pages/114328352/PAT-016+-+Functional+Design+Checklist) * [PAT-021 - SADESIGN Checklist](/spaces/SITE/pages/115933188/PAT-021+-+SADESIGN+Checklist) * [PAT-031 - Critical Design Analysis Checklist](/spaces/SITE/pages/123600967/PAT-031+-+Critical+Design+Analysis+Checklist) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

# 4. Small Projects

For smaller projects, the detailed design process should leverage existing tools, standards, and practices to minimize complexity, waste, and risk while ensuring the design supports coding, testing, and system integration. The guidance below helps small projects optimize their efforts, reduce overhead, and meet requirements efficiently by utilizing proven resources and reusable assets.

---

### **1. Streamlining Detailed Design for Small Projects**

#### **1.1 Minimize Complexity**

Smaller projects may benefit from simplifying the detailed design phase by:

* Reducing the need for **original designs** where applicable components or reusable libraries already exist.
* Focusing on straightforward modular decomposition that avoids overly complex dependencies (e.g., minimize coupling and maximize cohesion).
* For processes that do not introduce significant risks, consider **limiting toolchains** to lightweight development environments that are well-supported and easy to integrate.

#### **1.2 Incorporate Pre-Existing Standards and Assets**

Where applicable, smaller projects should:

* Use **existing coding standards** (see SWE-061) from the Center's **Process Asset Library (PAL)** or industry-standard coding guidelines.
  + Example: Avoid the time-consuming development of unique coding conventions unless required by project-specific constraints.
* Adopt **document templates** for software design descriptions (SwDDs) and interface design descriptions (IDDs). Established templates streamline documentation efforts and ensure alignment with lifecycle standards.
* Leverage **software process models** already developed in the PAL of the Center or other Centers, designed for smaller projects.

#### **1.3 Avoid Over-Engineering**

Small projects should avoid excessive customization or the development of unique tools and environments that:

* Increase time and resource requirements unnecessarily.
* Complicate future maintenance or reuse due to the lack of standardization.
* Risk technical challenges in adapting untested tools.

---

### **2. Benefits of PAL Usage for Smaller Projects**

#### **2.1 Practical Resource Optimization**

Accessing the Center's Process Asset Library (PAL) or PALs from other Centers enables small projects to benefit from:

* **Reusable Design Assets:**
  + Components, algorithms, libraries, and code snippets designed for similar requirements.
  + Standardized workflows, tools, or documentation that align with NASA’s software lifecycle processes.
* **Established Process Frameworks:**
  + Coding standards, design guidance, testing protocols, and review procedures tailored to projects with limited budgets and resources.

#### **2.2 Reduced Cost and Time**

By utilizing pre-existing standards, small projects can reduce:

* Time spent developing coding standards from scratch.
* Costs related to developing tools, systems, or workflows that may require significant validation effort.

#### **2.3 Consistency and Compliance**

Using shared assets reinforces alignment with NASA software engineering policies (e.g., NPR 7150.2) and ensures that even small projects conform to organizational standards for quality, reliability, and safety.

---

### **3. Practical Recommendations for Small Projects**

Smaller projects conducting detailed design activities should prioritize the following approaches:

#### **3.1 Leverage Pre-Existing Coding and Design Standards**

* Use coding standards, programming guidelines, or testing practices that were previously established for similar project types or missions.
  + Example: Center-specific coding standards addressing common safety, performance, and security concerns.

#### **3.2 Simplify Documentation**

Adopt standardized documentation processes to avoid the burden of custom documentation creation:

* Documentation templates for SwDD, IDD, and SDD (Software Data Dictionary).
* Utilize automated documentation tools when available to reduce manual effort.

#### **3.3 Reuse Tools and Libraries**

* Where possible, use **commercial tools** or NASA-accredited tools/core libraries (see SWE-136 - Software Tool Accreditation) that are already approved and tested.
* Identify reusable components from PALs or previous projects that meet current project needs, reducing the need for extensive design and coding efforts.

#### **3.4 Focus on Minimal Viable Design**

In resource-limited environments, small projects can adopt simplified design processes that focus on:

* **Essential Design Outputs:** Modules, interfaces, logic flows, and data structures adequate for coding and testing without excessive details.
* **Iterative Refinement:** Conduct periodic reviews during the design phase rather than finalizing designs upfront, allowing flexibility to adapt based on testing results in later phases.

---

### **4. Example Checklist for Small Projects**

#### **Before Starting the Detailed Design Phase:**

1. Have pre-existing coding standards and design templates been identified and approved for reuse?
2. Are reusable tools, environments, or libraries available in PALs or from previous projects?
3. Are applicable coding and design guidelines clear to the development team?
4. Has team training incorporated knowledge about reuse of COTS, legacy software, and process assets?
5. Will the reduced documentation workload (from standardized templates) meet project requirements?

#### **During the Detailed Design Phase:**

1. Are tools and environments appropriate for small-scale design needs?
2. Are modules and interfaces kept simple, reducing overhead and risks of high complexity?
3. Are reused components adequately integrated into the detailed design documentation?
4. Are traceability matrices between design elements and requirements clear and maintained?
5. Are the chosen tools aligned with PAL standards for documentation and coding?

---

### **5. Key Concepts for Small Projects**

#### **5.1 Lightweight Modularity and Cohesion**

Focusing on modular design ensures components are reusable, maintainable, and scalable. For small projects:

* Avoid oversized modules with excessive logic; aim for smaller, **single-purpose modules** with well-defined boundaries.
* Keep interactions between modules simple to reduce debugging and integration effort.

#### **5.2 Reuse as a Best Practice**

Reuse is a critical strategy for smaller projects with limited resources. Take advantage of:

* **Reusable libraries** for calculations, data processing, or graphical outputs.
* **Legacy modules** that were validated in prior missions with similar objectives.

#### **5.3 Simplified Tools and Process Management**

Small projects can benefit from lightweight and simple tools. Ensure project tools:

* Are easy to set up and operate.
* Provide sufficient support for coding, testing, and documentation while avoiding unnecessary overhead.
* Minimize learning curves for developers who may be working under short timelines.

---

### **6. Maintenance and Evolution for Small Projects**

Small projects must also plan maintenance efforts for the detailed design phase to ensure:

* **Updated Documentation:** Keep design documents accurate and updated with any changes during testing, coding, or requirement updates.
* **Configuration Control:** Update reusable components in PALs for future projects, creating a feedback cycle that benefits future development teams.
* **Focus on Long-Term Simplicity:** Avoid introducing excessive complexity during iteration; instead, stick to manageable, scalable solutions that align with the long-term use of software.

---

### **Summary**

Small projects benefit from limiting customization and maximizing reuse of tools, standards, and libraries. Leveraging existing resources through PALs, reducing documentation complexity, and adopting modular designs are key strategies for meeting detailed design requirements efficiently. These approaches allow smaller teams to focus on producing high-quality software work products while minimizing risks, costs, and time investments.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-077)

  ["Guide to the software detailed design and production phase",](http://www.esa.int/TEC/Software_engineering_and_standardisation/TECBUCUXBQE_0.html "Click to open in new window")

  ESA PSS-05-05, Issue 1, Revision 1, ESA Board for Software Standardisation and Control, 1995.  The PSS family of standards was the ESA internal set of standards which was replaced by ECSS. It inluded a software engineering standard and a set of guides. This page contains the cited resource as well as others in the collection.
* (SWEREF-173)

  [The SYNTHESIS Environment for Component-Based Software Development,](http://ccs.mit.edu/dell/papers/step97.pdf "Click to open in new window")

  Dellarocas, Chrysanthos, Sloan School of Management, Massachusetts Institute of Technology, MA, 1997.
* (SWEREF-174)

  [Systems Engineering Fundamentals,](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-885j-aircraft-systems-engineering-fall-2005/readings/sefguide_01_01.pdf "Click to open in new window")

  Department of Defence Systems Management College, Supplementary text prepared by the Defense Acquisition University Press, Fort Belvoir, VA, 2001.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-323)

  [Software Architecture Review Board sub-community of practice.](https://nen.nasa.gov/web/sarb "Click to open in new window")

  The objectives of SARB are to manage and/or reduce flight software complexity through better software architecture and help improve mission software reliability and save costs.
* (SWEREF-417)

  ["The Power of 10: Rules for Developing Safety-Critical Code"](http://spinroot.com/gerard/pdf/Power_of_Ten.pdf "Click to open in new window")

  Holzmann, G.J., NASA Jet Propulsion Laboratory (JPL), 2006.
* (SWEREF-418)

  ["Certifying Auto-generated Flight Code"](https://slideplayer.com/slide/1457415/ "Click to open in new window")

  Denney, E., NASA Ames, 2008. Related: https://ti.arc.nasa.gov/m/profile/edenney/papers/Denney-BigSky-08.pdf
* (SWEREF-501)

  [Mars Observer Inertial Reference Loss](https://llis.nasa.gov/lesson/310 "Click to open in new window")

  Public Lessons Learned Entry: 310.
* (SWEREF-517)

  [Fault Tolerant Design](https://llis.nasa.gov/lesson/707 "Click to open in new window")

  Public Lessons Learned Entry: 707.
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-550)

  [ADEOS-II NASA Ground Network (NGN) Development and Early Operations -- Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned](https://llis.nasa.gov/lesson/1346 "Click to open in new window")

  Public Lessons Learned Entry: 1346.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
* (SWEREF-643)

  [Software Architecture & Design](https://www.tutorialspoint.com/software_architecture_design/key_principles.htm "Click to open in new window")

  Tutorials Point, Simply Easy Learning web site
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Process Asset Templates

**SWE-058 Process Asset Templates**

Click on a link to download a usable copy of the template.

* (PAT-006 - )

  [PAT-006 - Design Practices for Safety](https://swehb.nasa.gov/download/attachments/114327707/Design%20Practices%20for%20Safety.docx?api=v2 "Click to open in new window")

  Topic 6.1, Topic Group: Programming Checklists
* (PAT-008 - )

  [PAT-008 - Safety Considerations for Design Peer Reviews Checklist](https://swehb.nasa.gov/download/attachments/114328132/Safety%20Considerations%20for%20Design%20Peer%20Reviews%20Checklist%20.docx?api=v2 "Click to open in new window")

  Software Design Analysis, tab 3.2,
* (PAT-015 - )

  [PAT-015 - Detailed Design Checklist](https://swehb.nasa.gov/download/attachments/114328341/Detailed%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.4, Also found in Peer Review and Design Analysis categories.
* (PAT-016 - )

  [PAT-016 - Functional Design Checklist](https://swehb.nasa.gov/download/attachments/114328352/Functional%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.5, Also found in Peer Review and Design Analysis categories.
* (PAT-020 - )

  [PAT-020 - Examples of Interface Problems](https://swehb.nasa.gov/download/attachments/115179572/Examples%20of%20Interface%20Problems.docx?api=v2 "Click to open in new window")

  Topic 8.16, Software Design Analysis, tab 3.3, Item 6, Also found in Design Analysis category.
* (PAT-021 - )

  [PAT-021 - SADESIGN Checklist](https://swehb.nasa.gov/download/attachments/115933188/SADESIGN%20%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.16 - Software Design Analysis, tab 2, Also in SWE-058, tab 7.4.1
* (PAT-031 - )

  [PAT-031 - Critical Design Analysis Checklist](https://swehb.nasa.gov/download/attachments/123600967/Critical%20Design%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  Software Design Analysis, tab 2.4.3
* (PAT-036 - )

  [PAT-036 Software Architecture and Design Process Audit](https://swehb.nasa.gov/download/attachments/198770701/PAT-036%20-%20Architecture%20and%20Design%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Architecture and Design.
* (PAT-047 - )

  [PAT-047 - Architecture and Detailed Design Assessment](https://swehb.nasa.gov/download/attachments/198770765/PAT-047%20-%20Architecture%20and%20Detailed%20Design%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Architecture and Detailed Design in the Software Design Description document. Based on the minimum recommended content for a Software Design Description.
* (PAT-048 - )

  [PAT-048 - Interface Design Description Assessment](https://swehb.nasa.gov/download/attachments/198770866/PAT-048%20-%20Interface%20Design%20Description%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Interface Design Description document. Based on the minimum recommended content for an Interface Design Description.
* (PAT-055 - )

  [PAT-055 - Software Data Dictionary Assessment](https://swehb.nasa.gov/download/attachments/198770882/PAT-055%20-%20Software%20Data%20Dictionary%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Data Dictionary. Based on the minimum recommended content for a Software Data Dictionary.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA's **Lessons Learned Database** provides invaluable insights derived from historical projects, offering actionable recommendations to improve future software design efforts. These lessons underscore the importance of robust design practices, maintainability, fault tolerance, and strategic use of commercial off-the-shelf (COTS) tools. Below is an improved format for this section with clear takeaways for each lesson learned and how to apply them effectively in the context of NASA's software design processes.

---

### **1. MER Spirit Flash Memory Anomaly (2004)**

**Lesson Number:** 1483  
**Key Issue:** Memory management problems were deprioritized during an overly compressed flight software development schedule, leading to unexpected software performance issues.

#### **Lesson Learned:**

**Enforce Design Guidelines:** To minimize risks, project-specific design guidelines should be enforced for both COTS software and NASA-developed software. Ensure the flight software development team reviews logic and functional behavior of COTS software and includes vendor participation.

#### **Takeaways for Future Projects:**

* **Design Priority Management:** Avoid reprioritizing design tasks mid-project without reevaluating risks. Ensure critical areas like memory management and resource allocation are addressed systematically.
* **COTS Software Considerations:**
  + Work closely with vendors to ensure full understanding of COTS functionalities.
  + Include vendors in peer reviews and briefings to mitigate compatibility or integration risks.
* **Allocate Time for Fundamental Reviews:** Even in compressed schedules, allocate sufficient time for the team to assess basic logic and functions of COTS software.

---

### **2. Software Design for Maintainability**

**Lesson Number:** 0838  
**Key Issue:** As software becomes increasingly complex, poor maintainability can significantly hinder future updates, enhancements, and extensions of the codebase.

#### **Lesson Learned:**

**Design for Maintenance:** Software maintainability must not be an afterthought. Design software with maintainers in mind, ensuring they can enhance or update the product without needing to rebuild the majority of the codebase.

#### **Takeaways for Future Projects:**

* **Modular Design:** Emphasize modularity during design. Components should be standalone, thereby allowing updates without impacting unrelated modules.
* **Documentation:** Produce comprehensive yet concise documentation for maintainers, including clear interfaces, dependencies, and architectural decision rationales.
* **Tool Selection:** Provide maintainers with tools that enable efficient evaluation and updates, integrating version control and automated diagnostics.

---

### **3. Mars Observer Inertial Reference Loss**

**Lesson Number:** 0310  
**Key Issue:** Unexpected spacecraft anomalies highlighted the need for flexibility in software and hardware design to permit mid-mission corrections via patches or updates.

#### **Lesson Learned:**

**Design Flexibility:** Flight computers and software should be flexible to allow uplinking and implementing software patches to address anomalies during operations.

#### **Takeaways for Future Projects:**

* **Patchable Software Design:** Ensure designs remain adaptable, enabling patching without operational disruption.
* **Compatible Architectures:** Flight computer architectures should support efficient software patch delivery and execution, even in remote and challenging environments.
* **Testing:** Simulate patching procedures during development and testing phases to validate robustness, traceability, and reaction to unexpected anomalies.

---

### **4. ADEOS-II NASA Ground Network (NGN) Development – Use of COTS Products**

**Lesson Number:** 1346  
**Key Issue:** COTS products offer potential benefits (quicker delivery, lower costs, etc.), but require careful evaluation to mitigate risks and ensure alignment with project requirements.

#### **Lesson Learned:**

**COTS Selection Best Practices:** Deciding to use COTS products inherently carries risks but offers significant advantages when properly matched to project requirements.

#### **Takeaways for Future Projects:**

* **Evaluate COTS Candidates:**
  + Create a prioritized list of desired COTS features that align with project requirements.
  + Obtain demonstration versions and test extensively in the project's environment.
* **Leverage Vendor Expertise:**
  + Conduct tutorials, reference checks, and engage vendor contacts to ensure the product meets reliability and operational needs.
  + Choose vendors with proven relationships and scalability.
* **Optimize System Design:** Match the product to the application's size and complexity, favoring alignment with specific project requirements over generalized flexibility.
* **Conduct Peer Reviews:** Conduct frequent reviews to detect integration challenges early and mitigate risks tied to COTS adoption.

---

### **5. Fault-Tolerant Design**

**Lesson Number:** 0707  
**Key Issue:** Projects that neglect fault-tolerant design experience higher risks of degraded mission performance, premature termination, or excessive resource waste due to redundant overdesign.

#### **Lesson Learned:**

**Incorporate Fault Tolerance:** Build hardware and software features in spacecraft systems to tolerate minor failures and reduce dependency on switching to secondary systems.

#### **Takeaways for Future Projects:**

* **Proactive Fault Management:** Clearly define fault tolerance mechanisms during the design phase to detect and compensate for failures dynamically.
* **Optimize Redundancy:** Balance redundancy with spacecraft resource constraints. Avoid excessive backups and instead use optimized recovery methods (e.g., graceful degradation).
* **Cross-System Reliability:** Design interdependent subsystems with reliability principles to minimize cascading failures across spacecraft components.
* **Fault Simulation:** Test fault-tolerance features under simulated mission conditions to validate system durability and recovery functionality.

---

### **6. Summary of Lessons Applied**

NASA's software design lessons highlight critical areas essential for successful missions. By learning from previous challenges, future projects can take proactive steps to ensure high-quality, maintainable software designs:

#### **Key Lessons Integrated:**

1. Enforce design guidelines, particularly when using COTS software.
2. Design for maintainability to reduce long-term costs and effort.
3. Ensure software flexibility for mid-mission corrections.
4. Evaluate and align COTS tools carefully with project requirements.
5. Incorporate fault tolerance proactively to ensure system reliability.

---

### **Implementation Recommendations**

* **Integrate Lessons into Training:** Provide teams with training about NASA's lessons learned database, ensuring past mistakes are proactively addressed in new projects.
* **Develop Checklist-Based Processes:** Use these lessons to create robust checklists for design validation, maintainability, fault tolerance, and COTS evaluation.
* **Share Lessons Across Teams:** Actively circulate lessons within NASA Centers via documentation and process libraries (PALs) to reduce knowledge gaps between project teams.

By incorporating these lessons learned, software design activities can align with historical recommendations and prevent repeat issues that could compromise mission success or increase costs.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Incorporate an FPU into Spacecraft Processor Architectures](https://software.gsfc.nasa.gov/lesson-details/104/). **Lesson Number 104**: The recommendation states: "Incorporate an Floating Point Unit (FPU) into Spacecraft Processor Architectures."
* [Include a requirement for spacecraft FSW to provide the capability to update the flight code without mission interruption](https://software.gsfc.nasa.gov/lesson-details/156/).**Lesson Number 156**: The recommendation states: "When developing or acquiring spacecraft flight software, the design should provide the capability to update the flight software (in RAM and EEPROM) without impacting current mission data collection or pointing (i.e., without interrupting the mission due to entering safe hold)."

# 7. Software Assurance

**SWE-058 - Detailed Design**

4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess the software design against the hardware and software requirements and identify any gaps.

2. Assess the software design to verify that the design is consistent with the software architectural design concepts and that the software design describes the lower-level units to be coded, compiled, and tested. 

3. Assess that the design does not introduce undesirable behaviors or unnecessary capabilities.

4. Confirm that the software design implements all of the required safety-critical functions and requirements. 

5. Perform a software assurance design analysis.

## 7.2 Software Assurance Products

#### **1. Design Analysis Deliverables**

Software assurance activities must produce well-documented, actionable deliverables to ensure the software design meets requirements, minimizes risks, and adheres to safety standards. Key products include:

1. **Software Design Analysis Results:**

   * Comprehensive assessment of the software design, including evaluations of architectural and detailed design phases.
   * Verification that safety-critical functions and requirements are implemented correctly and traceable throughout the lifecycle (from requirements to implementation).
2. **Identified Risks and Issues:**

   * A consolidated list of design risks and issues, including their impact, probability, and recommended mitigation strategies. These risks should be tracked for timely resolution.
3. **Safety-Critical Design Implementation:**

   * Assessments confirming that all identified safety-critical functions align with system hazard analyses (see SWE-205) and are adequately implemented within the design.

---

#### **2. Additional Assurance Outputs**

* **Design Coverage Traceability Matrix:**  
  A traceability matrix linking architectural elements, detailed design components, safety-critical requirements, and hazard mitigations ensures comprehensive design coverage.
* **Peer Review Feedback Documentation:**  
  Summarized feedback from design peer reviews, capturing gaps, design improvements, hazards, or operational risks identified during the assurance process.

---

## 7.3 Metrics

Software assurance metrics are essential for measuring the progress and effectiveness of the design assurance process and identifying trends in risks and non-conformances across lifecycle phases. Suggested metrics include:

#### **Key Metrics for Software Design Assurance:**

1. **Architectural Issues Identified vs. Closed:**  
   Tracks architectural defects that propagate into the detailed design phase.
2. **Design Issues Identified vs. Resolved:**  
   Measures the effectiveness of issue resolution during the design process.
3. **Safety-Related Requirement Issues (Open vs. Closed):**  
   Monitors safety issues throughout development, focusing on timely resolutions.
4. **Safety Non-Conformance Trends by Lifecycle Phase:**  
   Evaluates safety-critical non-conformance occurrences over time, helping to identify recurring risks during specific lifecycle phases.
5. **Software Product Non-Conformance Trends by Phase:**  
   Highlights mismatches between product requirements and design implementations, enabling quick corrective actions.

#### **Additional Metrics:**

* **Peer Review Findings:** Quantify unresolved peer review findings that must be addressed before subsequent lifecycle phases.
* **Design Rework Effort:** Measure time and resources spent correcting design errors to improve upfront design accuracy.

---

## 7.4 Software Assurance Guidance

#### **Task 1: Requirements Traceability Assessment**

* **Objective:** Ensure requirements trace through the architectural design into the detailed design.
  + Review evolving design documents to confirm all requirements have corresponding design elements.
  + **Actions:**
    - Attend design peer reviews to monitor alignment of requirements and design evolution.
    - Identify missing or ambiguous traces and bring them to the design team’s attention.
    - Track gaps to resolution using project-specific traceability management tools.
  + **Outcome:** Ensure all software functionality requirements, operational requirements, and safety-critical requirements can trace end-to-end through the design lifecycle.

---

#### **Tasks 2 & 3: Design Review and Scenario Evaluation**

* **Objective:** Verify that detailed design flows down from architectural design and meets operational needs.
  + **Actions:**

    - Review the integrity and maturity of the design as it evolves from architectural definitions.
    - Mentally "step through" design scenarios to evaluate how operational and off-nominal behaviors are addressed. Focus on:
      * Missing design elements.
      * Pitfalls such as overly complex logic.
      * Superfluous or conflicting features that might introduce risks.
    - Attend design peer reviews to collaborate on closing issues.
  + **Scenario-Based Testing:**

    - Simulate operational workflows for various design scenarios (nominal vs. off-nominal conditions).
    - Identify pitfalls or misaligned behavior and recommend corrections before coding begins.
  + **Outcome:** Ensure that design decisions enable operational behaviors, mitigate risks, and provide clarity for implementers.

---

#### **Task 4: Safety-Critical Design Verification**

* **Objective:** Confirm that all safety-critical functions and requirements are effectively implemented in the detailed design.
  + **Actions:**

    - Cross-verify safety-critical requirements traced from system hazard analysis (SWE-205) to detailed design components.
    - Ensure safety-critical functions appear in the detailed design at a sufficient level to enable implementation.
    - Review hazard analysis documents periodically to capture updates and apply them to the design reviews.
  + **Safety Assessment Deliverables:**

    - **Safety Requirement Verification Matrix:** Links hazard mitigation strategies and detailed design components explicitly.
    - **Inspection Reports:** Results of safety assurance reviews conducted during design peer reviews.
  + **Outcome:** Guarantee that safety mitigations are adequately implemented and traceable back to requirements.

---

#### **Task 5: Develop the Software Assurance Design Analysis**

* **Objective:** Document an assurance-driven analysis of the detailed design to verify requirement satisfaction, risk mitigation, and suitability for coding activities.
  + Refer to **Topic 7.18: SADESIGN** analysis guidance for detailed procedures.

#### **Key Actions for Design Analysis:**

* **Evaluate Design Transformation:**  
  Confirm that requirements were correctly and completely transformed into architectural and detailed design elements during refinement phases.
* **Assess Risk:**  
  Ensure no design choices result in unacceptable operational risks or unintended behaviors. Address risk mitigation gaps proactively.
* **Evaluate Future Modifiability:**  
  Review design for maintainability and modifiability, ensuring that future updates do not require extensive rework.

---

## 7.4.1 Software Assurance Design Analysis Best Practices

Software assurance design analysis is critical for ensuring designs are correct, accurate, complete, and maintainable. Key best practices include:

1. **Focus on Nominal and Off-Nominal Needs:**

   * Assess if the design adequately addresses nominal operational scenarios and predicts behavior under off-nominal conditions (failures, degraded mode performance, etc.).
2. **Prevent Unintended Features:**

   * Ensure design logic avoids unintended features or behaviors that could jeopardize operation, introduce risks, or conflict with requirements.
3. **Identify Design Gaps:**

   * Validate traceability matrices to find missing design elements or incomplete coverage.
4. **Review Modifiability:**

   * Confirm modularity, reusability, and design flexibility to facilitate easy maintenance and updates during the lifecycle.

---

### **Additional References**

* **Topic 8.55:** Software Design Analysis.
* **Topic 7.18:** Documentation Guidance under SADESIGN.
* **Topic 8.18:** SA Suggested Metrics.
* **SWE-205:** Safety-Critical Software Determination.
* **SWE-058:** Software Development Design Guidelines.
* **SWE-087:** Peer Review and Inspection Guidance.

---

### **Conclusion**

Software assurance activities are critical to ensuring that NASA's detailed software design phase results in safe, reliable, traceable, and maintainable software products. Through traceability assessments, design reviews, scenario simulations, safety-critical function verifications, and risk evaluations, assurance teams can proactively identify and resolve issues before implementation begins. By maintaining focus on metrics, leveraging peer reviews, and applying lessons learned from NASA's extensive history, software assurance can minimize risk and ensure mission success.

Software Design Analysis (see Topic [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis))\

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing), [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis).

```

```

Consider the SADESIGN Checklist [PAT-021](#_tabs-<p></p>)  below when evaluating the software design, :

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-021 - SADESIGN Checklist**

See also [PAT-031 - Critical Design Analysis Checklist](/spaces/SITE/pages/123600967/PAT-031+-+Critical+Design+Analysis+Checklist), [PAT-006 - Design Practices for Safety](/spaces/SITE/pages/114327707/PAT-006+-+Design+Practices+for+Safety),

Some design principles to think about during design reviews:

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)       * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [PAT-006 - Design Practices for Safety](/spaces/SITE/pages/114327707/PAT-006+-+Design+Practices+for+Safety) * [PAT-015 - Detailed Design Checklist](/spaces/SITE/pages/114328341/PAT-015+-+Detailed+Design+Checklist) * [PAT-016 - Functional Design Checklist](/spaces/SITE/pages/114328352/PAT-016+-+Functional+Design+Checklist) * [PAT-021 - SADESIGN Checklist](/spaces/SITE/pages/115933188/PAT-021+-+SADESIGN+Checklist) * [PAT-031 - Critical Design Analysis Checklist](/spaces/SITE/pages/123600967/PAT-031+-+Critical+Design+Analysis+Checklist) |

# 8. Objective Evidence

Objective Evidence

Requirement 4.3.2 establishes that the project manager shall develop, record, and maintain a detailed software design based on the software architectural design, describing lower-level components to enable coding, compiling, and testing. Objective evidence is meant to demonstrate that the requirement is met and that the software design process is traceable, complete, and aligned with requirements.

Below is a comprehensive list of **objective evidence** that can be used to assess compliance with this requirement:

---

### **1. Software Design Documents**

#### **a. Software Design Description (SwDD)**

* The SwDD is the primary document that captures the detailed software design. The SwDD must include:
  + **Lower-Level Component Designs:** Definitions of all software modules, classes, functions, and components.
  + **Interfaces:** Clear documentation of how components interact, including input/output data formats, protocols, APIs, and external/system interfaces.
  + **Data Design:** Comprehensive information on data structures, variables, and relationships.
  + **Performance Details:** Constraints, timing, resource usage, and scalability considerations.
* **Purpose:** This document links the architectural design to the detailed design and explains how lower-level components will fulfill software requirements.

#### **b. Interface Design Description (IDD)**

* Details external and internal interfaces, including formats, protocols, and control flows.
* Shows the integration of software components with other system elements such as hardware or external software.

#### **c. Traceability Matrices**

1. **Requirements-to-Design Traceability Matrix:**
   * Maps system/software requirements to architectural and detailed design components to ensure:
     + Full design coverage for all requirements.
     + Safety-critical requirements are implemented in the design.
2. **Design-to-Code Traceability Matrix:**
   * Maps detailed design elements to the implementation and coding deliverables.

---

### **2. Design Review Artifacts**

#### **a. Design Peer Reviews:**

* Peer review records, findings, and resolutions for both architectural and detailed designs.
* Evidence of the design review process addressing:
  + Suitability of design elements for implementation.
  + Alignment with requirements (including safety-critical requirements).
  + Design risks and mitigations.

#### **b. Preliminary Design Review (PDR) Artifacts:**

* Evidence that the design transitioned from high-level architecture to preliminary components, modules, and interfaces.
* Validation of the architectural design's traceability to requirements.

#### **c. Critical Design Review (CDR) Artifacts:**

* Approval of the detailed design and evidence that it is complete and ready for implementation.
* Closure of design-related action items identified during PDR or earlier stages.
* Assessment of design maturity, including the ability to meet coding and testing needs.

---

### **3. Software Development and Management Plans**

#### **a. SDP/SMP Alignment:**

* Evidence that the Software Development Plan (SDP) or Software Management Plan (SMP) includes processes for transitioning from architectural to detailed design.

#### **b. Configuration Management Evidence:**

* Design baselines from PDR and CDR phases showing preserved and version-controlled design artifacts.
* Logs or traceability records reflecting updates to the design in response to requirements changes, risk findings, or testing results.

---

### **4. Design Traceability and Compliance to Safety Requirements**

#### **a. Safety Requirements Implementation:**

* Documentation verifying that all safety-critical requirements identified in system hazard analyses (see SWE-205) have been implemented in detailed design components.
* Evidence of linkage between safety requirements, design components, and testing procedures in the hazard analysis documentation.
* Safety analysis reports showing that the design decisions mitigate identified risks.

#### **b. Use of Fault Tolerance Mechanisms:**

* Evidence that design supports fault tolerance, especially for safety-critical software components, including redundancy, error-handling, and recovery strategies.

#### **c. Hazard Tracking and Closure Logs:**

* Logs demonstrating the capture of safety-related issues during design reviews and their resolution prior to detailed design acceptance.

---

### **5. Coding Preparation Evidence**

#### **a. Design Implementability:**

* Evidence that the detailed design contains sufficient detail to begin coding, compiling, and testing, including:
  + Component decompositions down to classes, functions, or equivalent units.
  + Pseudocode, flowcharts, or UML diagrams for complex parts of the design.
  + Logic descriptions and explanation of algorithms.
* **Purpose:** Demonstrate the readiness of the design to transition to implementation.

#### **b. Design Documentation for Coding Standards:**

* Evidence that the design aligns with project coding standards (SWE-061), including:
  + Adherence to variable naming conventions, coding structures, and API usage.
  + Secure coding practices for safety-critical and operational software.

---

### **6. Design Reviews and Risks**

#### **a. Identified Design Risks:**

* Design review findings or Software Assurance analysis documentation showing:
  + Identified risks in the design process (e.g., excessive coupling, low cohesion, or unimplemented safety objectives).
  + Plans for mitigating or addressing design risks.

#### **b. Risk Closure Documentation:**

* Trackable logs showing the resolution of risks identified during design reviews.
* **Purpose:** Ensure all risks to operability, safety, or requirement satisfaction are addressed before design implementation.

#### **c. Lessons Learned Integration:**

* Evidence that relevant design-related lessons learned from previous projects were incorporated during the design development process.
* Examples:
  + Addressing maintainability from the start of design (e.g., Lesson Number 0838).
  + Applying fault-tolerant strategies (Lesson Number 0707).
  + Reviewing and verifying COTS software integration (see MER Spirit Flash Memory Anomaly).

---

### **7. Software Assurance Evidence**

#### **a. Software Assurance Design Analysis:**

* Software assurance team’s independent evaluation of the design, covering:
  + Alignment with requirements and traceability.
  + Testability and correctness of the design at the module level.
  + Verification of safety-critical functions and failure management strategies.

#### **b. Configuration Control Evidence:**

* Records proving that design changes triggered by software assurance findings were controlled and implemented through formal change management processes.

#### **c. Safety Testing Readiness:**

* Evidence that the design includes specific provisions or hooks for safety-critical function testing during unit, integration, and system-level phases.

---

### **8. Metrics Reports**

* Metrics demonstrating the quality and effectiveness of the design process, such as:
  + Number of design issues identified vs. closed.
  + Number of safety-related design issues resolved over time.
  + Ratio of resolved vs. unresolved design-derived non-conformances during development.
  + Traceability matrix coverage metrics.

---

### Example Checklist of Objective Evidence:

1. **Design Documentation:**
   * SwDD, IDD, Traceability Matrices.
2. **Review Artifacts:**
   * PDR/CDR Reports, Action Item Logs.
3. **Safety Evidence:**
   * Safety Hazard Logs, Safety-Critical Requirements Verification.
4. **Metrics:**
   * Design issue resolution rates, safety compliance trends.
5. **Transition Evidence:**
   * Coding-readiness reviews, adherence to coding standards.
6. **Software Assurance Products:**
   * Risk Assessment Reports, Peer Review Findings.
7. **Configuration Logs:**
   * Baseline design snapshots, version control records.

---

### Conclusion:

Objective evidence ensures that Requirement 4.3.2 is not only met, but also traceable and verifiable throughout the lifecycle. By producing clear documentation, traceability matrices, metrics, and assurance deliverables at each phase of the design cycle, NASA teams can confidently transition from detailed design to implementation while addressing risks and aligning with mission goals.

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
