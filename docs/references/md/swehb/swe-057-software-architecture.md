# SWE-057 - Software Architecture

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695442. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture

SWE-057 - Software Architecture

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695442)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695442&showCommentArea=true&showComments=true#addcomment)

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

4.2.3 The project manager shall transform the requirements for the software into a recorded software architecture.

## 1.1 Notes

A documented software architecture that describes: the software’s structure; identifies the software qualities (i.e., performance, modifiability, and security); identifies the known interfaces between the software components and the components external to the software (both software and hardware); identifies the interfaces between the software components and identifies the software components. Reference NASA’s Software Architecture Review Board (SARB) paper NTRS ID 20160005787, “Quality Attributes for Mission Flight Software: A Reference for Architects.”

## 1.2 History

Click here to view the history of this requirement: SWE-057 History

SWE-057 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.2.2 The project shall transform the allocated and derived requirements into a documented software architectural design. |
| Difference between A and B | Descoped the requirement to transform the allocated and derived requirements into an architectural design to just develop the SW architecture. |
| B | 4.2.3 The project manager shall develop and record the software architecture. |
| Difference between B and C | Changed "develop" to "transform the requirements". |
| C | 4.2.3 The project manager shall transform the requirements for the software into a recorded software architecture. |
| Difference between C and D | No change |
| D | 4.2.3 The project manager shall transform the requirements for the software into a recorded software architecture. |

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

Experience confirms that the quality and longevity of a software-reliant system are largely determined by its architecture. (See lessons learned *NASA Study of Flight Software Complexity*. [571](#_tabs-<p></p>)) The software architecture underpins a system's software design and code; it represents the earliest design decisions, ones that are difficult and costly to change later. [131](#_tabs-<p></p>)  The transformation of the derived and allocated requirements into the software architecture results in the basis for all software development work.

Software architecture:

* Formalizes precise subsystem decompositions.
* Defines and formalizes the dependencies among software work products within the integrated system.
* Serves as the basis for evaluating the impacts of proposed changes.
* Maintains rules for use by subsequent software engineers that assure a consistent software system as the work products evolve.
* It provides a stable structure for use by future groups through the documenting of the architecture, its views and patterns, and its rules.

**Requirement 4.2.3** ensures that software requirements are systematically transformed into a documented software architecture. This is a critical step in the software development life cycle (SDLC) because the architecture serves as the foundational blueprint for the system, providing structure, clarity, and traceability from requirements to implementation. The creation of a recorded software architecture ensures that the software fulfills its requirements and operates effectively within the project’s constraints and environment.

---

### **Key Reasons for this Requirement**

#### **1. Supports Traceability from Requirements to Implementation**

* Transforming requirements into a recorded software architecture ensures that all high-level functional and non-functional requirements are explicitly addressed and linked to specific architectural components.
* A recorded architecture provides **bidirectional traceability**:
  + From **requirements to architecture**, to verify that all requirements are addressed in the system design.
  + From **architecture back to requirements**, to confirm that no architectural component is unnecessary or unaligned with project and stakeholder goals.

**Example:** Safety-critical requirements for a spacecraft system can be traced to redundant architectural components designed to meet fault tolerance objectives.

---

#### **2. Establishes a Structured Foundation for Design and Implementation**

* Software architecture defines the **high-level structure** of the system, decomposing functional and non-functional requirements into manageable components, subsystems, and their interactions.
* By recording this architecture, the project team ensures clarity and alignment during detailed design and implementation phases, minimizing ambiguity and reducing the risk of misinterpretation by developers.
* A well-defined architecture allows for reusable, modular, and scalable solutions that are easier to implement and evolve.

**Example:** For a mission-critical satellite communication system, a layered architecture (e.g., protocol, service, and application layers) ensures separation of concerns, enabling focused implementation of communication protocols independently of application requirements.

---

#### **3. Facilitates Early Problem Detection and Risk Management**

* Developing a software architecture helps identify potential risks or issues early in the project lifecycle, including:
  + Misalignment between requirements and development goals.
  + Feasibility issues such as resource constraints, timing conflicts, or integration limitations.
  + Conflicts between non-functional requirements (e.g., performance vs. maintainability).
* Early identification of conflicts or gaps prevents costly downstream rework and delays.

**Example:** Developing an architectural prototype or high-level model can uncover computational bottlenecks in embedded systems before coding begins.

---

#### **4. Ensures Consistency and Compliance with Project Constraints**

* Documenting the architecture enables systematic alignment with project constraints, including:
  + Hardware limitations.
  + Operational environment specifications.
  + Industry standards and NASA-specific requirements (e.g., safety-critical software).
* Architecture captures decisions regarding design trade-offs (e.g., performance vs. fault tolerance) and ensures these are consistent with stakeholder priorities.

**Example:** A flight software system may adopt a federated architecture to comply with redundancy requirements for fault tolerance while also managing constraints on onboard processing power and memory.

---

#### **5. Supports Non-Functional Requirements (NFRs)**

* While functional requirements typically address what the software does, non-functional requirements describe how the system operates. A recorded software architecture ensures non-functional requirements are integrated into the system from the beginning, avoiding ad-hoc or poorly documented design compromises later.
* **Key NFRs supported through architecture include:**
  + **Scalability:** Architecture documents enable planning for future scaling by defining extensible components and interfaces.
  + **Reliability & Fault Tolerance:** Defines redundant architectures (e.g., double-redundant data buses for spacecraft).
  + **Security & Safety:** Incorporates secure component interactions, data encryption, and fault-tolerant subsystems at the architectural level.
  + **Performance:** Ensures architecture optimizes response times and resource usage.

**Example:** For a planetary rover, real-time control systems may be validated architecturally to ensure latency requirements are met.

---

#### **6. Enables Collaboration Across Multidisciplinary Teams**

* A recorded architecture provides a common point of reference for stakeholders, system engineers, developers, testers, and external partners, ensuring consistency in understanding across the project.
* It serves as the **communication bridge** between high-level requirements and low-level technical details, facilitating collaboration in complex, multi-stakeholder environments.

**Example:** In large projects like Mars missions, the software architecture enables consistent collaboration between the flight software team, ground system developers, and mission scientists.

---

#### **7. Supports Reuse and Maintainability**

* A properly recorded architecture can serve as a reusable asset for similar projects or subsystems, allowing NASA to leverage proven architectures.
* Architectures promote maintainability by separating concerns, documenting dependencies, and providing a modular structure to support future changes.

**Example:** The architecture for a science data processing pipeline can be reused or adapted for other missions with similar data processing requirements, saving time and ensuring reliability.

---

#### **8. Aids in Verification and Validation**

* Recorded architecture provides a documented foundation to verify and validate the system design:
  + Verifies that architectural components align with functional requirements through review.
  + Validates that non-functional requirements, such as performance and security, are addressed through analysis and modeling.
* Clear architectural documentation simplifies testing because it provides a reference for integrating and testing individual subsystems.

**Example:** Verifying and validating that the architecture of a CubeSat mission meets its thermal and power regulation requirements ensures compliance before moving into detailed design and hardware integration.

---

#### **9. Provides a Baseline for Change Management**

* A recorded architecture serves as a baseline for evaluating the impact of requested changes.
* Architectural documentation provides insight into how changes to requirements might affect downstream components and systems.

**Example:** If a late requirement change introduces a new external interface, the architecture helps developers and stakeholders evaluate the ripple effects on performance, security, and subsystem interactions.

---

#### **10. Addresses Programmatic and Regulatory Compliance**

* Architecture documentation is necessary for meeting programmatic or regulatory compliance requirements, such as those stipulated by:
  + NASA Procedural Requirements (e.g., **NPR 7150.2**).
  + Project standards for quality assurance and safety-critical systems.
  + Internal configuration management goals (e.g., accessibility, traceability, and auditable decision-making).

**Example:** A NASA safety-critical project ensures its architecture adheres to software assurance and IV&V policies by providing auditable records of all architectural decisions.

---

### **Consequences of Skipping or Insufficient Architecture Documentation**

* **Unmanaged Complexity:** Without a documented architecture, software design becomes ad hoc, causing misunderstandings, misaligned components, and integration issues.
* **Missed Requirements:** Lack of documentation can result in overlooked requirements, especially for safety-critical and non-functional needs.
* **Increased Costs:** Inadequate architecture can lead to costly rework during the later stages of development, affecting schedule and resources.
* **Operational Failures:** Failure to validate the alignment of architecture with the customer environment can lead to mission failures (e.g., the Mars Climate Orbiter mishap highlighted the need for ensuring architecture accounts for unit consistency and compatibility).

---

### **Conclusion**

The rationale behind Requirement 4.2.3 is to ensure that every requirement is methodically transformed into a robust, well-documented software architecture. This recorded architecture provides the necessary foundation for detailed design, implementation, validation, and successful operation in the customer’s environment. By establishing traceability, managing risks, addressing constraints, and supporting system-wide collaboration, the recorded software architecture ensures the delivery of high-quality, mission-critical software for NASA’s projects.

# 3. Guidance

## 3.1 What is Software Architecture?

Software architecture is the fundamental organization of a software system, defined by its components, their relationships, and the principles guiding its design, evolution, interactions, and operational behavior. According to **“Software Architecture in Practice” by Len Bass et al.,** software architecture is "the process of defining a collection of hardware and software components and their interfaces to establish the framework for the development of a computer system.” IEEE Std 1471-2000 expands this definition to "the fundamental organization of a system, embodied in its components, their relationships to each other and the environment, and the principles governing its design and evolution."

### **Key Features of Software Architecture:**

1. **Structural Elements:**

   * Includes software components, their properties, and their relationships to other components and to environmental factors.
2. **Interactions:**

   * Defines how components interact to realize system behaviors, fulfilling both functional and non-functional requirements.
3. **Documentation (Critical Importance):**

   * Explicitly recording the software architecture facilitates communication between stakeholders, supports critical early design decisions, and provides the basis for reusable design patterns.
4. **Relationship Between Software and System Structures:**

   * The software architecture maps the software's structure and behaviors to the system's structure and behaviors. This includes its interaction with the operating environment.

---

### **Core Goals of Documenting Software Architecture**

* Establish a **shared understanding** of the software's high-level design among stakeholders.
* Enable **reuse** of components and design patterns across projects.
* Provide **design rules and patterns** for cross-cutting concerns (e.g., fault detection and recovery, telemetry processing, startup protocols).
* Present **quality attributes** (e.g., reusability, safety, security, testability, reliability) that the software needs to achieve.

Additionally, architecture documentation identifies architecture patterns—abstract models that generate technical solutions consistently—and expresses rules ensuring uniform implementation of capabilities shared across components.

**See also:** *Topic 8.02 – Software Quality.*

---

## 3.2 How Do Software Architecture and Software Detailed Design Differ?

Architecture serves as the **blueprint of the system**, focusing on how the software’s structural elements and interactions enable system behaviors and meet quality attributes, while **detailed design** refines architectural decisions into technical entities required for implementation.

### **Key Differentiators:**

#### **Software Architecture:**

* **Scope:**  
  Focuses on high-level structure, abstraction, and relationships between software components and their environment.
* **Purpose:**  
  Defines **how the system works** and ensures alignment with system-wide requirements and constraints.
* **Characteristics:**

  1. Allocated system requirements trace to architecture elements (e.g., modules, components, subsystems).
  2. Abstracts common features or patterns (e.g., messaging protocols, safety mechanisms) without instantiating specific implementations.
* **Artifacts:**  
  Captures only the conceptual content of data (e.g., interaction formats, functional processes) without detailing data types or signatures.

---

#### **Detailed Design:**

* **Scope:**  
  Decomposes architectural components into concrete units, classes, functions, interfaces, and associated data structures.
* **Purpose:**  
  Provides **implementation-ready technical solutions** for derived software requirements.
* **Characteristics:**

  1. Defines the specific instantiations of architecture abstractions.
  2. Includes detailed information on user-defined data types, functional signatures, and interface protocols.
  3. Traceable directly to code and derived requirements.
* **Artifacts:**  
  Defines data types, instances, memory management strategies, algorithm implementations, and control pathways.

---

#### **Overlap:**

In some cases, detailed design activities may begin alongside architecture development to address high-severity technical risks. These instances blur the line between architecture and detailed design—but both are critical for guiding development and ensuring quality.

---

## 3.3 When and How Does One Define Software Architecture?

Software architecture is defined early in the software lifecycle, refined throughout development, and validated at significant milestones. It is drafted during requirements scoping and operational concept development and baselined at the **Preliminary Design Review (PDR)** (see also *7.08: Maturity of Life Cycle Products at Milestone Reviews*).

#### **Key Steps in Defining Software Architecture:**

1. **Requirements Gathering and Assessment:**

   * Software architecture begins with understanding **top-level system requirements** and structuring them.
   * Operational concepts document (ConOps) captures user workflows and maps requirements to software functions.
2. **Decomposition and Sub-Allocation:**

   * Requirements are decomposed or sub-allocated into focused activities, forming the hierarchical structure of the software.
   * Derived requirements emerge logically, representing extensions of allocated system requirements.
   * (Refer to *SWE-050 - Software Requirements* and *SWE-051 - Software Requirements Analysis*.)
3. **Transformation to Architecture:**

   * Through **architectural design** processes, decomposed requirements are transformed into a cohesive framework supporting the system's software solutions.
4. **Quality Attributes, Constraints, and Assumptions:**

   * Quality attributes (e.g., scalability, performance, fault tolerance) are defined alongside constraints from environmental factors (hardware, stakeholder inputs, NASA policies).
   * Collaborative development between hardware and software teams is critical to avoid hardware-imposed constraints dominating the architecture.
5. **Reuse and Heritage:**

   * Assess existing software architectures, frameworks, middleware, and technologies to reduce cost, schedule, and risk.
   * Explore *buy-vs-build* decisions while preserving flexibility in architectural design.

---

### **Best Practices:**

* Use **views** and **patterns** to express architecture:

  + **Views** represent how the system components relate (e.g., developer view, operations view, tester view).
  + **Patterns** provide proven reusable designs to solve recurring problems.
* Continuously evaluate and refine the architecture throughout development and testing.
* Conduct architecture reviews (e.g., *Software Architecture Review Board*).

---

## 3.4 Recording the Software Architecture

Per *SWE-057*, software architecture must be thoroughly documented in the **Software Design Description (SwDD)**. While the format may vary by project, the documentation must contain the following critical elements:

#### **Essential Content for Recording:**

1. **Driving Requirements** - Allocated system requirements and quality attributes.
2. **Stakeholders and Concerns** - Identified parties and their architectural expectations.
3. **Assumptions and Constraints** - Environmental and organizational limits.
4. **Alternatives Assessment** - Analysis of various architectures and rationale for selection.
5. **Subsystem Decomposition and Dependencies** - Software components and their interactions.
6. **Verification Methods** - Metrics and strategies for assessing architectural conformance.
7. **Risks and Rationale:**
   * Identified risks inherent to the selected architecture.
   * Recorded rationale for changes or re-design decisions.

#### **Domain-Specific Architectural Representations:**

* Patterns (e.g., abstractions, concurrent threads).
* Data and resource management (e.g., memory, inter-process communication).
* Real-time execution attributes (e.g., throughput, synchronization).
* Dependency structure models (compact lists of subsystem dependencies).

---

## 3.5 Continuous Importance of Architecture

Software architecture must remain active throughout the software lifecycle, influencing development, implementation, testing, and refinement. Projects should emphasize architecture as a response to complexity:

#### **Risks of Weak Architecture:**

* Difficult to validate for correct behaviors beyond case-by-case analyses.
* Difficult to manage or modify with confidence.
* Operates unpredictably outside thoroughly tested conditions.
* Cannot easily be reused or inherited for new development.

#### **Avoid Weak Architecture by:**

* Conducting periodic **architecture reviews**.
* Maintaining architecture **traceability and relevance**.
* Using dependency models for successively refining architecture during later lifecycle phases.

---

### **Resources**

Software architecture review resources (e.g., NASA Engineering Network [NEN] documentation templates, reference designs, toolkits) facilitate robust architectural design and documentation. Recommended tools include **UML (v2.0)** for modeling and decomposition strategies that tame complexity.

By embracing a structured approach to software architecture, projects ensure scalable, reliable, reusable solutions, improving mission outcomes and enabling long-term innovation even in the face of evolving systems complexity.

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality)

See [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) and [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) for more discussion on derived requirements.

The required content for the [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) document includes the software architectural design.

See topic [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description) for additional information on the recommended kinds of content that usually appear in software architecture descriptions and for examples from several sources of outlines for documenting software architecture descriptions.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)        * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

# 4. Small Projects

Software architecture is a critical non-coding activity that enhances the quality, maintainability, and long-term viability of the software. While smaller projects often require less-formal approaches to keep costs and complexity manageable, they must still address architectural concerns proportional to the project's risk, novelty, and scope. Below is improved guidance tailored to small projects that balances resource constraints with the importance of effective architecture.

---

#### **Key Principles for Small Project Software Architecture**

1. **Understand Project Risk and Complexity:**

   * For **low-risk, highly precedented systems**, small projects may leverage lightweight architectural practices with a focus on usability and affordability.
   * For **high-risk, novel systems**, small projects must dedicate more attention to architecture, as failure to address risks early can lead to costly issues during development or operations.
2. **Adopt a “Risk-Driven” Approach:**

   * Small projects don’t need exhaustive architecture upfront. Instead, focus on identifying the **most pressing risks**—such as safety risks, security concerns, or mission feasibility—and apply targeted architecture and design techniques to mitigate those risks.
   * Examples of risk-driven techniques include:
     + Simplifying system modularity for easier debugging or iteration.
     + Ensuring interface compatibility to avoid integration risks.
     + Prioritizing fault tolerance in critical functions for high-impact systems.
3. **Adequate Documentation (Regardless of Project Size):**

   * Even for smaller projects, the software architecture must be **adequately documented** to support communication among team members, traceability across requirements, and maintainability over the software lifecycle.
   * Documentation doesn’t need to be formal or exhaustive, but it must:
     + Define major components and their interactions.
     + Identify constraints, assumptions, and limitations.
     + Capture design decisions made to address project-specific challenges.

---

#### **Small Project Architectural Practices**

Smaller projects can adopt streamlined methods to define and document architecture without burdening resources unnecessarily:

1. **Use Simplified Modeling Tools:**

   * Instead of engaging in complex formal processes, small projects can use lightweight tools like flowcharts, diagrams, or simplified Unified Modeling Language (UML) models to describe architecture elements and system interactions.
   * Example: A basic block diagram representing the major subsystems and their relationships may suffice for a small utility software project.
2. **Define Core Components and Interfaces:**

   * Focus on identifying the project's **primary functional components**, their relationships, and external interfaces. For example:
     + Components: Input module, processing module, data storage.
     + Interfaces: File-format compatibility, API specifications, or hardware device protocols.
3. **Reusing Proven Architectures:**

   * Where possible, leverage existing architectures from heritage systems or off-the-shelf solutions. Proven architectural practices from past projects can reduce development time and mitigate risk while ensuring reliability.
4. **Collaborate with Stakeholders on Documentation:**

   * Use informal collaborative methods (e.g., group discussions, brainstorming sessions) to capture architectural understanding and validate early design decisions. Stakeholders can confirm:
     + Whether the architecture meets operational needs.
     + Whether constraints have been incorporated appropriately.
     + Any anticipated risks or concerns based on project experience.
5. **Real-World Alignment:**

   * Ensure the architecture addresses the system’s real-world context, including constraints imposed by the operating environment, hardware, or customer requirements.

---

#### **Risks of Skipping Architecture or Insufficient Effort**

For small projects, skipping or underestimating software architecture can result in:

* **Unmanaged Complexity:** Issues scaling the project or adapting to changes.
* **Integration Failures:** Misdirected interfaces leading to runtime errors or incompatibility with subsystems.
* **Reduced Maintainability:** Difficulties modifying, debugging, or reusing the software due to lack of clarity in architectural design.
* **Costly Rework:** High downstream costs to fix foundational problems that could have been avoided during early architecture definition.

---

#### **What "Just Enough" Architecture Looks Like**

Small, low-risk projects can practice **lightweight architecture** by targeting specific areas that are most critical to success:

1. **Identify and Mitigate Pressing Risks:**

   * Example: If the project requires interaction with external hardware devices, the architecture should prioritize the definition of interfaces and protocols to prevent integration issues.
2. **Document Key Architectural Decisions:**

   * Keep records of:
     + Component definitions and responsibilities.
     + Interaction models and communication mechanisms (e.g., API calls or message-passing).
     + Constraints like memory, processing power, or operational environment limitations.
3. **Focus on Modular Scalability:**

   * Even for smaller software, adopting a modular structure simplifies future updates, debugging, and maintenance.
4. **Evaluate Reuse Opportunities:**

   * Where possible, avoid novel solutions for low-risk projects. Use heritage software architecture, standard libraries, or existing frameworks to reduce effort.

---

#### **Best Practices for Small Projects**

* **Start Small but Adapt as Needed:**

  + Begin with a minimally viable architecture tailored to project goals, and scale it as the complexity or risk rises during the software lifecycle.
* **Incorporate Quality Attributes Early:**

  + Focus on quality attributes most relevant to the project:
    - High-risk projects may emphasize **fault tolerance** and **security.**
    - Low-risk projects may prioritize **reusability** or **performance optimization.**
* **Engage in Stakeholder Collaboration:**

  + Use informal but structured stakeholder input sessions to validate architectural choices.

---

#### **Focusing on Documentation for Small Projects**

Even for lightweight or informal architectures, documentation should at least include:

1. **System Overview:**

   * A simple description of the major functional components and their roles in the system.
2. **Interfaces:**

   * Define dependencies, communication pathways, and external interaction mechanisms (e.g., hardware, APIs).
3. **Constraints:**

   * Identify assumptions, limitations, and requirements relevant to the architecture.
4. **Risk Mitigation Strategies:**

   * List architectural decisions that address potential risks (e.g., fault tolerance in data processing components).
5. **Changes and Rationale:**

   * Document any changes made to the architecture and the reasons behind those changes.

---

### **Conclusion**

For small projects, software architecture remains a critical element to ensuring quality and reducing risk. While formal, exhaustive architectures may not be necessary for low-risk projects, teams should adopt **risk-driven lightweight approaches** to capture essential architectural information. Regardless of the project's size or method, architecture documentation is a non-negotiable artifact that empowers maintainability, integration, and scalability throughout the software lifecycle. By balancing effort against risk and complexity, small projects can achieve well-structured software efficiently without compromising quality.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-131)

  [Software Architecture in Practice, (2nd Ed.).](http://www.amazon.com/Software-Architecture-Practice-Len-Bass/dp/0201199300 "Click to open in new window")

  Len Bass, Paul Clements, and Rick Kazman. Boston: Addison-Wesley, 2003.
* (SWEREF-139)

  [The Unified Modeling Language User Guide,](http://www.amazon.com/Unified-Modeling-Language-User-Guide/dp/0321267974 "Click to open in new window")

  Booch, G., Rumbaugh, J., and Jacobson, L., Addison Wesley, 2nd Edition, 2005.
* (SWEREF-174)

  [Systems Engineering Fundamentals,](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-885j-aircraft-systems-engineering-fall-2005/readings/sefguide_01_01.pdf "Click to open in new window")

  Department of Defence Systems Management College, Supplementary text prepared by the Defense Acquisition University Press, Fort Belvoir, VA, 2001.
* (SWEREF-191)

  [Pattern-Oriented Software Architecture, Volume 1, A System of Patterns.](http://www.amazon.com/Pattern-Oriented-Software-Architecture-System-Patterns/dp/0471958697 "Click to open in new window")

  Frank Buschman, Regine Meunier, Hans Rohnert, Peter Sommertad, and Michael Stal. Wiley, 1996.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-210)

  [IEEE Computer Society, "Systems and Software Engineering--Recommended Practice for Architectural Description of Software-Intensive Systems,](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4278472 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1471-2000 ( ISO/IEC 42010:2007), 2007. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-295)

  [Documenting Software Architectures: Views and Beyond, Second Edition,](http://www.sei.cmu.edu/library/abstracts/books/0321552687.cfm "Click to open in new window")

  Clements, P., et al. Addison-Wesley, 2011. Available for purchase at various locations.
* (SWEREF-313)

  [Dependency Models to Manage Software Architecture,](http://www.crosstalkonline.org/storage/issue-archives/2005/200511/200511-Sangal.pdf "Click to open in new window")

  Sangal, N., Waldman, F., Crosstalk Magazine, November, 2005
* (SWEREF-345)

  [Software Architecture; Theory and Practice,](http://static1.1.sqspcdn.com/static/f/702523/15002943/1320631378633/201111-Tarullo.pdf?token=FXjqIL3 "Click to open in new window")

  Tarullo, Michael, L3 Communications, Crosstalk Magazine, Nov/Dec, 2011.
* (SWEREF-363)

  [Quality Attributes for Mission Flight Software: A Reference for Architects](https://ntrs.nasa.gov/citations/20160005787 "Click to open in new window")

  Wilmot, Jonathan, Fesq, Lorraine, Dvorak, Dan, Conference Paper, Publication Date
  March 5, 2016, GSFC-E-DAA-TN30323,
* (SWEREF-387)

  [Quality Attribute Spreadsheet,](https://nen.nasa.gov/web/sarb/home/-/list/view/6551?_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_returnUrl=https%3A%2F%2Fnen.nasa.gov%3A443%2Fweb%2Fsarb%2Fhome%2F-%2Flist%2Ftype%2F137%3F_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_cur%3D1%26_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_delta%3D20%26_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_orderByCol%3DmodifiedDate%26_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_orderByType%3Ddesc%26_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_selectedResourceRecordTypeIds%3D137 "Click to open in new window")

  NASA Software Architecture Review Board, 4/16/2016,  Download spreadsheet. A set of software architecture quality attributes that can be used within the domain of mission-critical, real-time, embedded systems.
* (SWEREF-571)

  [NASA Study of Flight Software Complexity](https://llis.nasa.gov/lesson/2050 "Click to open in new window")

  Public Lessons Learned Entry: 2050.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database provides valuable insights into challenges and mitigation strategies from past software development efforts. These lessons highlight the importance of good software architecture in managing complexity, ensuring system reliability, and avoiding downstream development issues. Below is an improved and expanded version referencing documented lessons:

---

### **Lessons Learned: In Class D, Fault Protection Becomes the Safety Net—So It Must Be Excellent**

**Problem/Observation:**  
Class D missions accept higher hardware and redundancy risk, which places greater reliance on software‑based fault protection (FP). The Anomaly Review Board (ARB) emphasized that FP must be robust enough to compensate for these elevated risks. For LTB, several FP weaknesses emerged that limited the system’s ability to autonomously protect itself.

**ARB Context:**  
The ARB explicitly stated:  
“On a Class D mission that assumes risk, ensure that the safety net of fault protection can adequately mitigate some of the risks.”

**Contributing Factors:**  
• Incorrect or insufficiently validated FP thresholds.  
• Fault protection logic split across multiple authorities and implementation paths.  
• Sequence‑based safing behaviors and FSW‑based safing behaviors were never tested together end‑to‑end.  
• Missing telemetry limited situational awareness and inhibited on‑orbit diagnosis.  
• Reset behavior and recovery paths were not fully characterized or validated.

**Resulting Impacts:**  
The spacecraft’s ability to safely respond to anomalies was compromised. Fragmented FP design, incomplete testing, and unclear behavior under reset conditions reduced system resilience during off‑nominal events.

**Relevant SWEHB Guidance:**  
Core SWEHB requirements remain applicable even when tailored for Class D:  
• SWE‑057 (Software Architecture) requires the design and documentation of fault management behavior.  
• SWE‑050, SWE‑051, and SWE‑055 require verifiable, traceable FP‑related requirements and logic.  
• SWE‑070 and SWE‑073 require modeling, simulation, and end‑to‑end testing to validate FP behavior under nominal and off‑nominal conditions.

**Lesson Learned:**  
Class D missions rely disproportionately on software fault protection because hardware redundancy is limited. For this reason, FP must be designed, validated, and tested with exceptional rigor. Software fault protection is a mission‑critical system—not an optional enhancement—and must be treated as such from architecture through ATLO and operations.

### **Lesson Learned (Starliner CFT):** **Telemetry design, reset behavior, and fault protection architecture must be explicit and validated.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Telemetry sample rates were inadequate; reset behavior and configuration persistence were not fully defined; fault protection was fragmented across sequences and FSW.

**Contributing Factors:**

* Missing telemetry channels/precision to diagnose anomalies.
* Unclear ownership of FP logic (sequencer vs. FSW) and cross‑path validation.
* Insufficient definition and testing of reset and recovery pathways.

**Impacts:**

* Reduced observability, slower diagnosis, and inconsistent safing outcomes.
* Late discovery of threshold/logic issues and interactions.

**Recommended Practices (Aligned to SWE‑057):**

* Architect **health monitoring** with sufficient fidelity (rates, timestamps, states) and explicit telemetry requirements.
* Consolidate FP **design authority**; document interactions across implementation paths and validate end‑to‑end.
* Define **reset/recovery architecture** (states, persistence rules, timing) and verify under mission‑representative conditions.

**Actionable Checks:**

* Architecture documents include telemetry specifications and FP state diagrams.
* End‑to‑end FP/safing tests demonstrate combined sequence + FSW behavior.
* Reset behavior test reports cover cold/warm starts, fault injections, and configuration persistence.

### **NASA Study of Flight Software Complexity**

**Lesson Number: 2050**  
**Date:** March 2009

NASA conducted a comprehensive study in March 2009 to investigate the root causes of flight software size and complexity growth, which had led to significant development problems across multiple projects. The study identified factors contributing to **accelerating growth in software complexity**, including the addition of new capabilities, intricate interfaces, and poor architectural practices. Among the key takeaways, the study emphasized:

**"Good software architecture is the most important defense against incidental complexity in software designs."**

#### **What is Incidental Complexity?**

Incidental complexity refers to unnecessary or unintended complications that arise during the design and development of software—not from the inherent requirements of the system but due to suboptimal decisions, inadequate planning, or flawed architectural practices. Examples include:

* Overly intricate or non-standard software interfaces.
* Poor modularization that leads to tightly coupled components and difficulty in modifying or scaling the software.
* Misalignment between requirements, design, and implementation, causing integration challenges.

#### **Contributing Factors Identified in the NASA Study:**

1. **Growth of Requirements without Scaled Architecture:**

   * Projects underestimated the need for robust architecture as requirements expanded or evolved late in the development lifecycle, leading to patchworked solutions and complexity buildup.
2. **Lack of Focus on Reusability and Modularity:**

   * Tight coupling of software components resulted in systems that were harder to modify, extend, and debug. Modular architectures were identified as critical for scalability and maintainability.
3. **Underestimation of Interfaces:**

   * Inadequate architectural foresight in managing system interfaces—both internal (between subsystems) and external (with hardware or other systems)—resulted in integration failures and excessive rework.
4. **Late Architectural Adjustments:**

   * Changes in architecture late in a project’s lifecycle were significantly more costly, exacerbating development delays and introducing risk. This reinforced the need for early, well-documented architectural planning.

#### **Lesson Learned Recommendations:**

To address the challenges identified, the study recommended the following practices for mitigating complexity:

* **Adopt Robust Architectural Planning:**  
  Invest time upfront to create a scalable software architecture that anticipates potential growth in requirements, interfaces, and operational constraints.
* **Modular and Standardized Design:**

  + Prioritize modular designs to separate functionality into isolated, reusable, and scalable components.
  + Use standard and well-documented patterns to ensure consistency across subsystems.
* **Interface Management:**  
  Explicitly define and document both internal and external interfaces to prevent integration issues and improve system interoperability.
* **Proactive Risk Identification:**  
  Recognize architectural risks early and mitigate them through simulation, prototyping, and architectural reviews.

---

### **Lessons Learned: Class D Budget and Schedule Pressure Leading to Reduced Software Maturity at ATLO**

**Problem/Observation:**  
A combination of Class D mission constraints and schedule compression resulted in flight software (FSW) entering Assembly, Test, and Launch Operations (ATLO) with insufficient maturity. The Anomaly Review Board (ARB) highlighted several systemic contributors to this reduced readiness.

**Contributing Factors:**  
• Cancellation of the Janus mission reduced opportunities for heritage software reuse.  
• The IM‑2 rideshare shift forced accelerated delivery timelines.  
• Class D budget constraints limited staffing, depth, and robustness of software development and assurance activities.

**Resulting Impacts:**  
• FSW command sequences were still undergoing validation up to the eve of launch.  
• Key elements of the fault protection architecture entered ATLO in an immature state.  
• COTS software behaviors were not fully characterized before integration.  
• Critical end‑to‑end tests—such as SA phasing and GNC phasing—were never executed.

**Relevant SWEHB Guidance:**  
While Class D missions are allowed to tailor processes, the SWEHB still requires adherence to core engineering and assurance expectations, including:  
• SWE‑028, SWE‑065, SWE‑066: Verification planning and execution.  
• SWE‑057: Ensuring the software architecture is complete and validated.  
• SWE‑071, SWE‑073: Integrated testing, simulation, and end‑to‑end verification.

**Lesson Learned:**  
Regardless of mission class, flight software must reach sufficient maturity before entering ATLO. Tailoring does not remove the need for complete architectures, characterized behaviors, and integrated test evidence. The LTB demonstrates the risks introduced when these fundamentals are compressed or deferred, particularly in resource‑limited Class D environments.

### **Additional NASA Lessons Learned Cases on Software Architecture**

#### **Case Study: Mars Climate Orbiter Failure**

**Lesson Number: 0641**  
**Date:** November 10, 1999

The Mars Climate Orbiter mission failed due to a software error caused by a mismatch between metric and imperial units in ground and spacecraft systems. This issue could have been prevented by creating a robust architecture that enforced **unit consistency** across systems.

**Lesson Learned:**

* Software architecture must define system-wide standards for unit use, data representation, and the interactions between ground systems and onboard software to prevent systemic errors.
* Design reviews should stress consistency between requirements, design, and implementation elements specifically for cross-domain communication.

---

#### **Case Study: Orbital Maneuvering System Software**

**Lesson Number: 0070**  
**Date:** April 14, 1981

A critical software error in the Shuttle’s Orbital Maneuvering System was identified during testing but had not been accounted for during architectural design. The issue arose due to inadequate **fault tolerance** mechanisms in the software architecture.

**Lesson Learned:**

* Software architectures for safety-critical systems must incorporate **redundancy**, **failure detection**, and **fault recovery mechanisms** early in the lifecycle to prevent mission-critical errors.

---

#### **Case Study: International Space Station Software Integration**

**Lesson Number: 1586**  
**Date:** October 7, 2008

The complexity of integrating the International Space Station’s software caused significant delays due to insufficient architectural planning for **multi-party software interfaces** developed by different international teams.

**Lesson Learned:**

* Software architecture should explicitly address interoperability and integration requirements when multiple development teams are involved. Independent components should align with the overarching architecture and undergo frequent integration testing.

---

### **Immature Testbeds and Simulation Environments**

**Incident:**  
Major incompatibilities between JPL and Maxar testbeds delayed verification activities and prevented execution of essential closed‑loop GNC testing. Early assumptions about vendor simulation capabilities proved incorrect.

**Lesson Learned:**

* **Interface Verification:** Simulation environments must be verified early with contractual clarity on capabilities, interfaces, and data integration.
* **End‑to‑End Fidelity:** High‑fidelity closed‑loop simulation must be operational well before system‑level V&V.

**Implication:**  
Faulty assumptions about vendor simulation capacity or testbed interoperability can cripple software testing and threaten mission readiness.

### **Key Takeaways Across NASA Lessons Learned**

NASA's experiences highlight the critical role of software architecture in addressing challenges across diverse projects. Common recommendations from lessons learned include:

1. **Invest in Architectural Planning Early:**  
   Overlooking architecture can lead to compounding issues, including complexity, integration failures, and costly rework.
2. **Prioritize Modularity and Scalability:**  
   Design architectures that are modular, maintainable, and capable of accommodating future system growth without breaking existing functionality.
3. **Document Architecture Thoroughly:**  
   Clear and concise architecture documentation ensures traceability, stakeholder alignment, and effective communication across teams.
4. **Standardize Practices Across Domains:**  
   Projects should establish consistent standards for data representation, system interfaces, quality attributes, and operating constraints within architectural guidelines.
5. **Continuous Validation Through Reviews:**  
   Architecture reviews should occur regularly across the development lifecycle to identify emergent complexities and refine architectural decisions.

---

### **Conclusion**

Lessons learned from NASA underscore the necessity of software architecture in addressing incidental complexity, managing interfaces, supporting scalability, and maintaining quality. By incorporating architectural best practices early on and applying insights from past experiences, projects can avoid costly mistakes, enhance system reliability, and improve the chances of mission success. Whether addressing complexity on a high-risk flight software project or ensuring compatibility across international collaborations, software architecture remains one of NASA's most critical defenses against development challenges.

---

This expanded guidance integrates critical examples from NASA’s history while linking lessons learned to actionable practices for future projects. It highlights architecture's significance as both a proactive and defensive tool in software development.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Intra-operations center ICDs](https://software.gsfc.nasa.gov/lesson-details/85/). **Lesson Number 85**: The recommendation states: "Consider implementing intra-operations center ICDs as a standard practice."
* [Incorporate an FPU into Spacecraft Processor Architectures](https://software.gsfc.nasa.gov/lesson-details/104/). **Lesson Number 104**: The recommendation states: "Incorporate an Floating Point Unit (FPU) into Spacecraft Processor Architectures."
* [Primary Instruments should have a Programmable Processor](https://software.gsfc.nasa.gov/lesson-details/105/). **Lesson Number 105**: The recommendation states: "Primary Instruments should have a Programmable Processor."
* [Take advantage of the Space Physics Data Facility](https://software.gsfc.nasa.gov/lesson-details/117/). **Lesson Number 117**: The recommendation states: "Take advantage of the Space Physics Data Facility (SPDF). Engage with the SPDF early in the project and sustain that engagement throughout development."
* [Missions with a constellation of spacecraft should strongly consider separate Telemetry & Command (T&C) strings](https://software.gsfc.nasa.gov/lesson-details/128/). **Lesson Number 128**: The recommendation states: "Missions with a constellation of spacecraft should strongly consider separate Telemetry & Command (T&C) strings for each spacecraft."
* [Project's hardware designers to include a debug register that is both readable and writable](https://software.gsfc.nasa.gov/lesson-details/160/). **Lesson Number 160**: The recommendation states: "Advise the project's hardware designers to include a debug register that is both readable and writable, to enable software developers to test read and write accesses to the hardware."

# 7. Software Assurance

The page could not be found.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess that the software architecture addresses or contains the software structure, qualities, interfaces, and external/internal components.

2. Analyze the software architecture to assess whether software safety and mission assurance requirements are met.

## 7.2 Software Assurance Products

#### **Software Design Analysis Results:**

Software assurance activities should produce detailed analyses of the architecture to ensure that it:

1. Meets the allocated and derived requirements.
2. Mitigates risks related to safety and mission assurance.
3. Identifies architectural issues related to performance, reliability, scalability, and maintainability.

This analysis involves assessing:

* The structure and organization of architectural components.
* Internal and external interfaces.
* Patterns or abstractions used to address cross-cutting concerns.
* Quality attributes and constraints that drive architectural decisions.

Deliverables include:

* **Results of Architecture Analysis:**

  + Document findings confirming whether the software architecture addresses essential qualities (e.g., security, fault tolerance, performance) and satisfies system requirements.
  + Highlight any identified risks, weaknesses, or architectural issues that require corrective action.
  + Summary of the connection between derived requirements and architectural components.
* **Software Assurance Risk Analysis:**

  + A list of risks associated with architectural patterns, design decisions, or implementation constraints.
  + Include an assessment of any architecture-specific risks tied to safety and assurance, such as fault management and data management integrity.
* **Software Safety and Mission Assurance Impact:**

  + Explicit identification of software architecture features that impact safety and mission assurance, such as:
    - Partitioning to ensure functional safety between mission-critical and non-critical components.
    - Redundancy mechanisms for fault tolerance.
    - Interface handling to prevent external system dependency risks.
    - Resource and memory management for real-time constraints.

#### **Additional Supporting Products:**

* **Software Architecture Review Board Report and Findings:**  
  For projects that utilize a **Software Architecture Review Board (SARB)**, use the findings to:

  + Validate architectural conformance to requirements and quality attributes.
  + Identify unresolved architectural issues, proposed solutions, and measures taken to address deviations.
* **Summary of Non-Conformances & Resolutions:**  
  A summary of any identified non-conformances (e.g., gaps in requirements compliance, safety issues) and the actions taken to close them.

---

## 7.3 Metrics for Software Assurance Activities

Utilize metrics to track the effectiveness, quality, and progress of software architecture. Metrics inform project decision-making, risk management, and assurance activities.

1. **Non-Conformances Over Time:**  
   Track the number of non-conformances in software work products (including architectural artifacts) identified per lifecycle phase:

   * Requirements analysis.
   * Preliminary design.
   * Detailed design and implementation.
   * Integration and testing.
2. **Architectural Issues Closure Rate:**

   * Measure the number of issues identified during architecture evaluations versus those resolved over time. This provides insight into:
     + Responsiveness to findings.
     + Architectural soundness leading into implementation.
3. **Safety-Related Non-Conformances:**

   * Specifically track safety-related architectural issues, including any elements that impact safety requirements. Categorize these by lifecycle phase to ensure early identification and resolution.

**Related Reference:**  
See *Topic 8.18 - SA Suggested Metrics* for additional metrics that can be applied to software architecture.

---

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance for Software Assurance Activities

#### **Confirm Comprehensive Documentation:**

Ensure the software architecture is fully documented and addresses the following key attributes:

* Drafted early in the lifecycle and baselined at the **Preliminary Design Review (PDR)** (refer to *Topic 7.08 - Maturity of Life Cycle Products at Milestone Reviews*).
* Derived from top-level system requirements and operational concepts.
* Reflects functional/physical decomposition of system components and performance characteristics.
* Clearly identifies derived requirements that extend allocated system specifications (*See SWE-050 and SWE-051*).

---

#### **Verify Key Architectural Content:**

**Check that the software architecture includes the following elements:**

1. **Structure and Components:**

   * Definition of the software's structure, including subsystems, components, and their relationships.
   * Subsystem decomposition sufficient to manage complexity.
2. **Driving Requirements:**

   * Documentation of the requirements, quality attributes, constraints, and derived requirements that influence architectural decisions.
3. **Stakeholder Concerns:**

   * Clear connection to stakeholder expectations, including operational needs, safety, and mission assurance expectations.
4. **Interfaces:**

   * Definitions of interfaces (both internal and external) that include data flow diagrams and clearly specified dependencies.
5. **Alternatives Assessment:**

   * Assessment of alternative architectural approaches, including analyses of trade-offs and risks.
6. **Rationale for Chosen Design:**

   * Explanation of architectural patterns, abstractions, and algorithms selected to meet requirements.
   * Justifications for significant architectural changes during development.
7. **Verification and Validation Methods:**

   * Strategies for measuring conformance to the architecture.
   * Identification of methods to validate that the architecture meets both functional and quality requirements.
8. **Risk Analysis and Management:**

   * Documentation of architectural risks, such as resource constraints, security vulnerabilities, and fault tolerance concerns.

---

#### **Address Safety and Mission Assurance Impact:**

Evaluate the software architecture specifically for its implications on **safety** and **mission assurance:**

1. **Hazard Analysis:**

   * Trace software safety hazards to architectural components:
     + Do architecture elements (e.g., resource partitions, real-time subsystems, or data handling workflows) contribute to or mitigate hazards?
2. **Safety-Critical Features:**

   * Identify components that must meet safety and assurance requirements:
     + Fault tolerance mechanisms (e.g., health monitoring, redundancy).
     + Data integrity and consistency across subsystems.
     + Time-sensitive controls or real-time execution performance.
3. **Review Partitioning and Isolation:**

   * Evaluate whether partitioning approaches (e.g., physical or software-based) effectively isolate safety-critical components from non-critical ones.
   * Assess the impact of shared resources (e.g., memory, threads) on fault propagation.
4. **Mission Resilience:**

   * Examine architectural choices that impact mission assurance:
     + Scalability for long-term operations.
     + Recovery mechanisms for degraded states.
     + Ability to handle external dependencies, such as ground systems or hardware interfaces.

---

#### **Perform Software Architecture Analysis:**

Conduct an architecture review to ensure the architecture’s adequacy to meet system, safety, and mission requirements. Confirm that each of the following questions is addressed:

1. **Alignment with Safety and Quality Attributes:**

   * Does the architecture address system constraints and characteristics (e.g., reliability, reusability, scalability)?
   * Are attributes such as fault tolerance, operational security, and failure recovery designed into the architecture?
2. **Compliance with NASA Standards:**

   * Does the architecture conform to applicable standards, such as NASA software assurance policies, SWE requirements, and other project-specific guidelines?
3. **Change Impact Analysis:**

   * Can the architecture handle anticipated changes with minimal risk?
   * Are dependencies and risks clearly modeled to minimize ripple effects during future updates?
4. **Integration and Interfaces:**

   * Are data flows, message-passing mechanisms, and external/internal interfaces clearly defined and validated?

---

### **Conclusion: Ensuring Architecture Excellence**

Software assurance activities for architecture are pivotal to enhancing safety, reliability, and mission success. By applying rigorous analysis, utilizing metrics for insight, and confirming thorough architectural documentation, assurance activities serve as a critical safeguard against poorly designed systems. Additionally, the identification of risks and mission assurance impacts early in the lifecycle enables small but impactful corrections that enhance long-term project success. This proactive approach ensures the architecture is scalable, maintainable, and resilient under operational conditions—key elements for successful NASA missions.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)        * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence refers to verifiable artifacts, documentation, analyses, or other tangible outputs that confirm compliance with a requirement. For Requirement 4.2.3, objective evidence demonstrates that software requirements have been methodically transformed into a documented software architecture.

Below is a list of common types of objective evidence for compliance with this requirement, categorized by lifecycle phase and activity.

---

#### **1. Software Requirements Documentation**

* **Purpose:** Ensures the project has a clear foundation for developing the software architecture.
* **Artifacts:**
  + A requirements specification (e.g., *Software Requirements Specification - SWE-050*) listing all functional and non-functional requirements (performance, scalability, safety, etc.).
  + **Derived requirements** traceable to allocated system requirements, showing logical extensions based on operational scenarios.
  + Stakeholder requirements that validate user needs and constraints for software architecture.
  + Interface requirements detailing how the software interacts with other system components or external systems.

---

#### **2. Architectural Design Documentation**

* **Purpose:** Validates the transformation of requirements into a documented architecture and highlights the decisions leading to the software's structure and interactions.
* **Artifacts:**
  + **Software Architecture Description (SWE-057):**
    - Defines the architecture structure, components, subsystems, and their relationships.
    - Documents quality attributes (e.g., reliability, security, scalability) that are influenced by requirements.
    - Includes architecture patterns, abstractions, or algorithms that directly address project requirements.
  + **Subsystem Decomposition:** A breakdown of high-level components into subsystems and modules aligned with requirements.
  + **Interface Design Documents:**
    - Description of internal and external interfaces, data flows, interaction protocols, and boundary conditions.

---

#### **3. Requirements to Architecture Traceability Matrix**

* **Purpose:** Provides bidirectional traceability between software requirements and architectural components, verifying that all requirements are appropriately addressed in the architecture.
* **Artifacts:**
  + A **traceability matrix** mapping each requirement to the corresponding architectural component responsible for its realization.
  + Evidence that non-functional requirements (e.g., fault tolerance, performance constraints) are traced to specific architectural design decisions.

---

#### **4. Risk and Alternatives Analysis**

* **Purpose:** Ensures risks related to architecture decisions are identified and mitigated, and alternatives are evaluated before finalizing the architecture.
* **Artifacts:**
  + Risk analysis reports documenting potential architectural risks (e.g., safety, scalability, integration issues) and their mitigation strategies.
  + Architectural alternatives analysis report describing the tradeoffs and rationale for the adopted architectural approach.
  + Review Board findings validating that architecture decisions considered risks and constraints.

---

#### **5. Architecture Modeling and Diagrams**

* **Purpose:** Serves as a visual representation of the software's layout, component interactions, and system behaviors.
* **Artifacts:**
  + **Models:** High-level design models (e.g., UML diagrams such as component diagrams, sequence diagrams, activity diagrams, flowcharts) that represent the architecture and address major requirements.
  + **Data Flow Diagrams (DFDs):** Represent how data is propagated through the architecture and between system components.
  + **Execution Flow and Thread Architecture:** Shows processes, threads, and concurrency mechanisms in relation to real-time execution requirements.

---

#### **6. Interface Definition and Documentation**

* **Purpose:** Verifies that internal/external interfaces are documented and satisfy interface-related requirements.
* **Artifacts:**
  + Interface Control Documents (ICDs) specifying message formats, protocols, and data management strategies.
  + Communication protocol documentation for data transfer between architectural components.
  + Integration needs analysis for external system compatibility.

---

#### **7. Architecture Validation Results**

* **Purpose:** Validates architectural decisions and ensures conformance with requirements.
* **Artifacts:**
  + Results from architecture simulation or prototyping for high-risk areas.
  + Verification reports showing that architecture meets performance, safety, and fault tolerance requirements.
  + Test reports of early prototypes confirming architectural validity under expected operating conditions.

---

#### **8. Software Architecture Reviews**

* **Purpose:** Independent evaluation of the software architecture to ensure it meets system and software requirements.
* **Artifacts:**
  + **Software Architecture Review Board (SARB) Reports:** Findings and recommendations from architecture reviews, including identified risks, adherence to requirements, alternatives evaluation, and action items.
  + Formal review meeting minutes outlining feedback from stakeholders and subject matter experts.

---

#### **9. Safety and Mission Assurance Analysis**

* **Purpose:** Ensures safety and mission-critical features are accounted for in the architecture.
* **Artifacts:**
  + Safety hazard analyses showing how critical requirements (e.g., fault tolerance, resource isolation) translate into architectural components.
  + Documentation of architectural mechanisms supporting partitioning, redundancy, or other safety features.
  + Mission assurance reports evaluating architecture robustness for long-term operations.

---

#### **10. Software Design Description Document (SwDD)**

* **Purpose:** Provides comprehensive documentation of the software architecture and design, supporting requirements traceability, implementation, and verification.
* **Artifacts:**
  + SwDD sections explicitly addressing architectural design, system structure, and component relationships (refer to *SWE-057* for required content).

---

#### **11. Configuration Management Evidence**

* **Purpose:** Confirms that the software architecture has been baselined, versioned, and updated as necessary.
* **Artifacts:**
  + Baselined architectural documents stored in a configuration management system.
  + Change request records linked to architectural modifications based on evolving software requirements or risks.

---

#### **12. Metrics and Outcomes**

* **Purpose:** Demonstrates continuous improvement and tracking of architectural issues.
* **Artifacts:**
  + Metrics reports tracking:
    - Number of architectural issues identified and resolved.
    - Number of traced requirements covered by architectural components.
    - Non-conformances related to architecture by lifecycle phase.

---

### **Summary of Typical Objective Evidence**

Objective evidence for Requirement 4.2.3 may include:

* Requirements documentation (SRS, traceability matrix).
* Software Architecture Description (SWE-057).
* UML diagrams, data flow diagrams, and interface control documents.
* Validation and verification results.
* Risk analysis reports and alternatives evaluation.
* Safety and mission assurance analyses.
* SwDD baseline documents and SARB review findings.
* Metrics reports and change management records.

When compiled and reviewed, these artifacts ensure compliance with the requirement and provide stakeholders and auditors with confidence that the software architecture aligns with project goals, requirements, and constraints.

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
