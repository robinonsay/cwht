# SWE-052 - Bidirectional Traceability

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695427. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability

SWE-052 - Bidirectional Traceability

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695427)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695427&showCommentArea=true&showComments=true#addcomment)

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

3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between the following software elements:

|  |  |  |  |
| --- | --- | --- | --- |
| Bi-directional Traceability | Class A, B, and C | Class D | Class F |
| Higher-level requirements to the software requirements | X |  | X |
| Software requirements to the system hazards | X | X |  |
| Software requirements to the software design components | X |  |  |
| Software design components to the software code | X |  |  |
| Software requirements to the software verification(s) | X | X | X |
| Software requirements to the software non-conformances | X | X | X |

## 1.1 Notes

The project manager will maintain bi-directional traceability between the software requirements and software-related system hazards, including hazardous controls, hazardous mitigations, hazardous conditions, and hazardous events.

## 1.2 History

Click here to view the history of this requirement: SWE-052 History

SWE-052 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.1.1.4 The project shall perform, document, and maintain bidirectional traceability between the software requirement and the higher-level requirement. |
| Difference between A and B | No change |
| B | 4.1.2.3 The project manager shall perform, record, and maintain bidirectional traceability between the software requirement and the higher-level requirement. |
| Difference between B and C | Specified traceability based on SW Classification by adding Table 1 in NPR-7150.2C.;  Added trace from requirements to system hazards for classes A,B,C and D;  Added trace from requirement to non-conformances;  SWE-059, SWE-064, and SWE-72 were merged into this requirement. |
| C | 3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between the following software elements:   |  |  |  |  | | --- | --- | --- | --- | | Bi-directional Traceability | Class A, B, and C | Class D | Class F | | Higher-level requirements to the software requirements | X |  | X | | Software requirements to the system hazards | X | X |  | | Software requirements to the software design components | X |  |  | | Software design components to the software code | X |  |  | | Software requirements to the software test procedures | X | X | X | | Software requirements to the software non-conformances | X | X | X | |
| Difference between C and D | Updated table to change 'test procedures' to 'verification(s)' |
| D | 3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between the following software elements:   |  |  |  |  | | --- | --- | --- | --- | | Bi-directional Traceability | Class A, B, and C | Class D | Class F | | Higher-level requirements to the software requirements | X |  | X | | Software requirements to the system hazards | X | X |  | | Software requirements to the software design components | X |  |  | | Software design components to the software code | X |  |  | | Software requirements to the software verification(s) | X | X | X | | Software requirements to the software non-conformances | X | X | X | |

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
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Rationale

Bidirectional traceability matrices help ensure that all the required software requirements (only what is required is developed) are addressed in software design and tested in the software testing activities. Bidirectional traceability matrices also make it less likely that requirements are misinterpreted as they are refined.

Bi-directional traceability serves as a critical mechanism for ensuring that all software-related elements (requirements, design, implementation, verification, and validation) are properly linked and aligned throughout the software development lifecycle. It addresses the need for accountability, completeness, consistency, and verification of system functionality while managing changes or risks. This is particularly relevant in NASA projects where software often plays a central role in ensuring mission safety, reliability, and performance.

---

### **Rationale**

1. **Ensures Complete Implementation**

   * Bi-directional traceability ensures that **each requirement** is accounted for in the system design, implementation, and testing.
   * Upward traceability from **design/code/testing back to the requirement** guarantees that no functionality is included without justification or supporting requirements ("avoids over-engineering").
   * Downward traceability from **requirements to design/code/testing** ensures that no requirement is overlooked or left unimplemented, preventing gaps in system functionality.
2. **Supports Verification and Validation (V&V)**

   * Traceability provides a systematic way to verify implementation and validate functionality:
     + By tracing requirements to test cases, it ensures that each requirement has been verified for correctness during testing.
     + By tracing test failures back to requirements, traceability helps identify areas where corrective action is needed (e.g., design adjustments or requirement modifications).
3. **Enables Impact Analysis During Change Management**

   * NASA systems frequently undergo changes during development due to evolving mission goals, advanced technical understanding, or unforeseen risks. Traceability enables **impact analysis** to determine how a change to one element (e.g., a requirement modification) impacts other elements (e.g., design, code, or testing).
   * Example: If a new adversarial detection requirement is added, traceability ensures updates in relevant design components, code modules, and test cases are linked and implemented properly.
4. **Improves Communication Across Teams**

   * NASA projects involve multi-disciplinary teams (software engineers, safety engineers, system architects, mission planners, etc.). Traceability creates clear maps of relationships between software elements, reducing misunderstandings and providing a **single source of truth** for collaborative development. For example:
     + Requirements engineers can confirm implementation progress by tracing downward to design elements or test results.
     + Test engineers can trace upward from test failures to determine if a defect arose from an incomplete or unclear requirement.
5. **Facilitates Risk Management**

   * Ensures that critical elements (requirements, designs, tests, etc.) associated with safety, security, or mission-critical goals are consistently traced and implemented.
   * Rapid identification of missing, conflicting, or misunderstood requirements reduces risks of system failure, adversarial vulnerability, or noncompliance with mission objectives.
6. **Enables Compliance with Standards**

   * NASA software projects must adhere to rigorous engineering policies, safety-critical standards (e.g., SWE-102, SWE-104, SWE-201), and cybersecurity regulations. Traceability provides objective evidence demonstrating compliance. For example:
     + Projects can use a traceability matrix to show how each safety-critical software requirement has been implemented and verified.
     + Traceability ensures all requirements from governing bodies (e.g., NASA-STD-8739.8A) are implemented and associated with concrete design/test elements.
7. **Reduces Errors Found Late in the Lifecycle**

   * Errors discovered late in development (e.g., a misinterpreted requirement, missing feature, or untested functionality) are costly and time-consuming to fix. With early traceability, projects reduce these risks by ensuring software aligns with requirements from the beginning and verifying end-to-end functionality throughout the lifecycle.
8. **Aids Post-Deployment Maintenance**

   * During operations and future upgrades, traceability simplifies understanding of how components relate to mission requirements. For example:
     + If changes to a deployed system are needed due to updated mission goals, traceability helps pinpoint the affected elements and ensures modifications do not introduce gaps or vulnerabilities.

---

### **Examples of Where Traceability is Essential**

1. **Mission-Critical Software**:

   * Traceability ensures that software meets strict operational demands, such as telemetry processing, guidance, navigation, or safety-critical systems.
   * Example: A requirement for safe autonomous landing could link traceability through design algorithms (sensor integration), code modules (landing logic), and test cases (simulated landing scenarios).
2. **Safety-Critical Considerations**:

   * Traceability is vital for ensuring safety requirements are properly addressed, designed, implemented, and validated without exception.
   * Example: A requirement to prevent erroneous commands to spacecraft thrusters could link downward into software control logic and test cases simulating failure scenarios.
3. **Cybersecurity-Sensitive Software**:

   * Traceability ensures adversarial detection mechanisms (requirements) are incorporated into system design, implemented in code, and validated to detect unauthorized activity or tampering.
   * Example: Traceability for logging unauthorized access attempts ensures the requirement is fully implemented and verified through automated test scenarios.

---

### **Key Bi-Directional Traceability Relationships**

NASA systems require traceability between software elements at multiple levels:

1. **Requirements ↔ Design**:

   * Ensures all requirements are incorporated into the system architecture and design.
2. **Design ↔ Implementation**:

   * Ensures designs accurately translate into code modules, algorithms, and software functions.
3. **Implementation ↔ Testing**:

   * Ensures that software implementations are fully tested for correctness, functionality, and compliance.
4. **Requirements ↔ Verification & Validation (V&V)**:

   * Provides evidence that all requirements are tested and validated.

---

### **Why This Matters in NASA Context**

NASA projects often operate within environments of high complexity and risk. A failure to maintain bi-directional traceability could lead to critical gaps, including:

* **Unverified Requirements**: Useful functionality might be omitted from the design or testing phases, resulting in incomplete software capabilities.
* **Over-Engineering**: Risk of implementing unnecessary features unrelated to mission requirements, adding cost and complexity.
* **Missed Safety-Critical Connections**: Gaps in translating safety-critical requirements into functional code or tests could jeopardize operational safety.
* **Inconsistent Change Management**: Poor traceability increases the risk of changes causing unintended consequences, such as introducing design flaws or new vulnerabilities.

---

### **Artifacts Supporting Bi-Directional Traceability**

1. **Requirements Traceability Matrix (RTM)**:

   * A structured table or database providing links between requirements, designs, implementations, and test cases.
   * Demonstrates how changes in any element propagate throughout others.
2. **Design Review Records**:

   * Evidence demonstrating traceability during the transition from requirements to design (e.g., design maps for adversarial detection).
3. **Verification Test Reports**:

   * Shows that test cases explicitly verify requirements and implementation and include traces back to the original requirement.
4. **Configuration Management Records**:

   * Provides logging of traceability updates during system changes or versions.

---

### **Conclusion**

Bi-directional traceability supports software assurance by ensuring requirements are fully implemented, validated, and aligned with system needs, reducing risks, enabling efficient changes, and ensuring compliance with NASA's stringent engineering and security standards. This requirement is indispensable for projects operating in complex environments, where the cost of oversight or failure is extremely high.

# 3. Guidance

## 3.1 Bidirectional Traceability

*Bidirectional* traceability is defined as an “association among two or more logical entities that are discernible in either direction (to and from an entity)” (ISO/IEC/IEEE 24765:2010 Systems and software engineering—Vocabulary [230](#_tabs-<p></p>)).

Software requirements come from various sources, including system requirements specifications, safety standards, security standards, hazard and risk analyses, system constraints, customer input, software safety "best practices," etc. [276](#_tabs-<p></p>) Bidirectional traceability matrices help ensure that all the requirements included in the [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)  trace back to a higher-level requirement that is the source or reason for having that requirement in the SRS. Bidirectional traceability also helps ensure that all requirements are addressed and that only what is required is developed. Bidirectional traceability matrices also make it less likely that requirements are misinterpreted as they are refined.

Bidirectional traceability is a traceability chain that can be traced in both the forward and backward directions, as illustrated below (Bidirectional Requirements Traceability, Westfall, 2006 [356](#_tabs-<p></p>)). It is important because it can point out software design elements that are not fulfilled in the code (i.e., missing or incomplete functionality) and source code that does not have a parent design element (i.e., extra functionality). Ideally, the trace does not identify any elements that have no source, such as a design element with no parent requirement. Still, if such "orphan" elements are discovered in the trace, they need to be discussed by the project team and assurance personnel to determine if the "orphan" elements are necessary. If they are determined to be necessary, any missing source elements, such as requirements, are added to the project.

See also [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis), [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics)

Figure 2 illustrates possible sources of higher-level requirements that are to be traced to the software requirements.

Figure 3 shows Bidirectional traceability is defined as a traceability chain that can be traced in both the forward and backward directions.

Figure 3

Using a matrix such as the one shown below (Bidirectional Requirements Traceability, Westfall, 2006 [356](#_tabs-<p></p>)) allows a single exercise to show traceability both forwards and backward. The matrix is completed left to right early in the appropriate phase in the project life cycle. As each column is completed, the forward trace is extended to the next set of products. Simply starting with a column such as the LLD (low-level design) Section and looking at the data in the columns to the left shows the backward traceability from an LLD element to its parent HLD (high-level design) element and back to the parent requirements.

Missing requirements are an indication that the resulting software product may not fully meet the goals and objectives for which the software is being designed. Extra requirements mean the end product may include unnecessary features and functionality, which add complexity and allow additional areas where problems could occur with the software.

## 3.2 Tracing Software Requirements To Higher-level Requirements

This requirement, SWE-052, is specific to tracing software requirements to higher-level requirements.  Software requirements come from different sources and can also be derived if needed.  Sources of requirements include, but are not limited, to the following items:

* Hardware specifications.
* Computer\processor\programmable logic device specifications.
* Hardware interfaces.
* Operating system requirements and board support package requirements.
* Data\File definitions and interfaces.
* Communication interfaces, including bus communication and fault interfaces.
* Software interfaces.
* Derived from domain analyses.
* Fault detection, isolation, and recovery actions and requirements.
* Models.
* Commercial software interfaces and functional requirements.
* Software security requirements.
* User interface requirements.
* Algorithms.
* Legacy or reuse software requirements.
* Derived from operational analyses.
* Prototyping activities.
* Interviews.
* Surveys.
* Questionnaires.
* Brainstorming.
* Observation.
* Software test requirements.
* Software fault management requirements.
* Hazard analyses.
* COTS, GOTS, MOTS, OSS, or reused software components.

Per the NASA Software Safety Guidebook [276](#_tabs-<p></p>) , the key benefits of tracing requirements include the following:

* Verification that all user needs are implemented and adequately tested. Full requirements test coverage is virtually impossible without some form of requirements traceability.
* Verification that there are no "extra" system behaviors cannot be traced to a user requirement.
* Improved understanding of the impact of changing requirements.

## 3.3 Bidirectional Traceability Matrix

When creating a bidirectional traceability matrix, consider the following actions:

* Create a matrix at the beginning of the project. [147](#_tabs-<p></p>)
* Uniquely identify each requirement using a number system that helps convey information about the requirement hierarchy and lineage. [147](#_tabs-<p></p>)
* Capture the source of the requirement, such as the document or standard identifier for the highest-level requirements or the unique identifier for the higher-level (parent) requirement.
* List a requirement once and show all of its higher-level requirement relationships using the appropriate identifiers; *do not duplicate requirements in the traceability matrix.*
* Consider including the required text in the matrix (rather than just the identifier).
* Keep the matrix maintained throughout the life of the project.
* Assign responsibility for creating and maintaining the matrix to a project team member since managing the links/references can be a labor-intensive process that needs to be tracked and monitored. [142](#_tabs-<p></p>)
* Maintain the matrix as an electronic document to make maintenance and reporting easier.
* Create the matrix such that it may be easily sorted to achieve/convey bi-directional traceability. [233](#_tabs-<p></p>)
* Justify requirements that are not directly traceable to higher-level requirements to show that they are included for a purpose.  
  + For example, a system architectural design that creates multiple computer software configuration items (CSCI) may result in requirements about how the CSCIs will interface, even though these interfaces are not covered in system requirements. Such requirements may be traced to a general requirement such as "system implementation" or to the system design decisions that resulted in their generation.
* Has the matrix been reviewed at major phases/key reviews of the project?

## 3.4 Software Design

Software design is created based on the software requirements.  Some assurance is needed to show that the design fulfills the software requirements and that no requirements are lost or left out of the design. One method of providing this "check and balance" is to create a traceability matrix between the software requirements and the resulting design.

Traceability links between individual requirements and other system elements, including but not limited to design, are helpful tools when evaluating the impact of changing or deleting a requirement. When a requirement is changed, traceability can help identify the affected products, including design, documentation, source code, tests, etc. (NASA-GB-8719.13, NASA Software Safety Guidebook [276](#_tabs-<p></p>))

Traceability is important because it can point out software design elements that are not fulfilled in the code (i.e., missing or incomplete functionality) and source code that does not have a parent design element (i.e., extra functionality). Ideally, the trace does not identify any design elements that have no source requirement. Still, if such "orphan" design elements are discovered in the trace, they need to be discussed by the project team and assurance personnel to determine if the "orphan" elements are necessary. If they are determined to be necessary, any missing source requirements are added to the project.

Keep in mind that a single requirement could trace to multiple architectural elements, design elements, etc. The reverse is also true. Design elements could trace back to multiple source requirements, so the relationships identified in the matrix are not required to be one-to-one.

 

As decisions are made during the development of the software design, the team may generate new requirements. When that happens, and the requirements are confirmed as being within the project's scope (not expanding the scope or “gold plating” the system by including unnecessary functionality), the traceability matrix is revised to include the new requirements and the mapped design elements.  Keep in mind that the requirements document(s) will also need to be revised when this occurs.

If the software design team is not the same as the requirements development team, collaboration may be needed to ensure proper bidirectional traceability between design and requirements.  Likewise, when tracing detailed design to high-level design, a collaboration between the different groups may be needed to ensure proper understanding and proper traceability documentation.

According to “Software Development Life Cycles: Outline for Developing a Traceability Matrix,” an article from *The Regulatory Forum* [127](#_tabs-<p></p>), key aspects of tracing design elements include:

* Trace high-level design specifications to software requirements.
* Trace detailed design specifications to high-level design.
* Trace design interfaces to hardware, user, operator, and software interface requirements.
* Trace the design back to hazard analysis if the design introduces hazards.

See also [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design),  [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes),  Topic [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description),

## 3.5 Software Test Procedures

Software test procedures are created to verify the software requirements for a project. To ensure that all requirements are verified via the test procedure set, the requirements need to be linked to the test procedures which verify them.

Traceability matrices help ensure that test procedures verify one or more software requirements by mapping those procedures back to one or more software requirements. Traceability is also used to ensure that the necessary level of test coverage is achieved, i.e., that there are sufficient tests to verify the requirements have been correctly implemented in the software.

Traceability links between individual requirements and other system elements, including but not limited to test procedures, are helpful tools when evaluating the impact of changing or deleting a requirement. When a requirement is changed, traceability can help identify the affected products, including design, documentation, source code, tests, etc. (NASA-GB-8719.13, NASA Software Safety Guidebook [276](#_tabs-<p></p>).)

Traceability is important because it can point out software requirements that are not tested (i.e., missing tests) and tests that do not serve to test requirements (i.e., extra tests).

Keep in mind that a single requirement could trace to multiple test procedures. The reverse is also true. Test procedures could trace back to multiple requirements, so the relationships identified in the matrix are not required to be one-to-one. The matrix needs to contain no missing relationships, i.e., empty cells in the matrix. Those indicate a problem with the set of test procedures that need to be designed such that every requirement is verified.

New requirements may be generated during design and implementation.  When that happens, and the requirements are confirmed as being within the scope of the project (not expanding the scope or “gold plating” the system by including unnecessary functionality), the traceability matrix needs to be revised to include the new requirements and the mapped design elements, implementation (source code), and test procedures.

If the software verification team is not the same as the requirements development team, collaboration may be needed to ensure proper bidirectional traceability between test procedures and requirements.

To ensure full traceability between requirements and tests, it is important to trace test cases, test scripts, test data, and other supporting test information not already found in the test procedures to the relevant test procedures.  This level of trace information may or may not appear in a traceability matrix.  The test procedures, test cases, test scripts, and test data can include the proper links and references to ensure full traceability among all the elements of the tests.

Key aspects of tracing test procedures include:

* Ensure that tests for safety-critical functions are identified either through the traceability matrix or through test procedure documentation.

* Trace each requirement and functional specification to one or more test cases (Manager's Handbook for Software Development [031](#_tabs-<p></p>)). If not already done, trace unit tests to source code and design specifications.
* Trace integration tests to high-level design specifications.
* Trace system tests to software requirement specifications (SRS). [127](#_tabs-<p></p>)

A project must define processes that trace requirements to validation and verification, test procedures, and evidence, in accordance with this requirement. This traceability enables the project to demonstrate that its validation and verification of each requirement is sufficient. A Project should connect the computing system requirements to the analytical and test evidence that demonstrates their implementation in a manner suited to its development process. The connections should be verifiable and human-readable, and the connections for safety requirements should be included in the application materials. NASA does not prescribe the technical methods for making these traceability connections but will evaluate the selected method for possibilities of error.

See also [SWE-066 - Perform Testing](/spaces/7150/pages/16450267/SWE-066+-+Perform+Testing), [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures), 

## 3.6 Software requirements to the system hazards

Bi-directional traceability with hazard analyses that include software allows a project to develop and maintain a list of all software safety-critical components that have been identified by the system hazard analysis.  The bi-directional traceability with the hazard analyses allows the engineers and safety personnel to see which software components are software safety-critical components and allows the project to ensure that the software safety-critical requirements are implied to those software components that trace to hazard analyses. See also Topic [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis),

The key to determining if the software is safety-critical software is the hazard analysis process.

Hazard Analysis must consider the software’s potential to cause or control a given hazard. It is a best practice to integrate the software within the system hazard analysis whenever possible. The general hazard analysis must consider software common-mode failures that can occur in redundant flight computers running the same software.

Software Safety Analysis supplements the system hazard analysis by assessing the software performing critical functions serving as a hazard cause or control. The review assures compliance with the levied functional software requirements, including [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), the software doesn’t violate the independence of hazard inhibits, and the software doesn’t violate the independence of hardware redundancy. The Software Safety Analysis should follow the phased hazard analysis process. A typical Software Safety Analysis process begins by identifying the must-work and must not work functions in Phase 1 hazard reports. The system hazard analysis and software safety analysis process should assess each function, between Phase 1 and 2 hazard analysis, for compliance with the levied functional software requirements, including SWE-134. For example, Solar Array deployment (must work function) software should place deployment effectors in the powered-off state when it boots up and requires initializing and executing commands in the correct order within 4 CPU cycles before removing a deployment inhibit. The analysis also assesses the channelization of the communication paths between the inputs/sensors and the effectors to ensure no violation of fault tolerance by routing a redundant communication path through a single component. The system hazard analysis and software safety analysis also assures the redundancy management performed by the software supports fault tolerance requirements. For example, software can’t trigger a critical sequence in a single fault-tolerant manner using single sensor input. Considering how software can trigger a critical sequence is true for triggering events such as payload separation, tripping FDIR responses that turn off critical subsystems, failover to redundant components, and providing closed-loop control critical functions such as propellant tank pressurization. See also [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements),

The project should have bi-directional traceability between the software requirements and software-related system hazards, including hazardous controls, hazardous mitigations, hazardous conditions, and hazardous events.

Traceability between the software requirements and software-related system hazards, including hazardous controls, hazardous mitigations, hazardous conditions, and hazardous events, allows us to determine which software components are software safety-critical and ensure that the required software safety-critical requirements are included in the software requirements and software activities.

Bidirectional traceability is a traceability chain that can be traced in both the forward and backward directions, as illustrated below (Bidirectional Requirements Traceability, Westfall, 2006 [356](#_tabs-<p></p>)). It is important because it can point out software design elements that are not fulfilled in the code (i.e., missing or incomplete functionality) and source code that does not have a parent design element (i.e., extra functionality). Ideally, the trace does not identify any elements that have no source, such as a design element with no parent requirement. Still, if such "orphan" elements are discovered in the trace, they need to be discussed by the project team and assurance personnel to determine if the "orphan" elements are necessary. If they are determined to be necessary, any missing source elements, such as requirements, are added to the project.

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics)        * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

# 4. Small Projects

Small projects often operate under constraints of time, budget, and resources, making it challenging to adopt advanced requirement tracing tools. However, effective traceability is critical to ensure project success, especially when safety-critical or mission-essential requirements are involved. The guidance below improves the original advice by providing practical, structured options for handling requirement traceability in small projects while staying effective and lightweight.

---

### **Traceability Options for Small Projects**

#### **1. Lightweight Tools for Requirement Traceability**

For small projects without access to specialized requirements tools with tracing features:

* Use **lightweight tools** such as spreadsheets, simple databases, or textual documents.
  + **Spreadsheets** (e.g., Microsoft Excel, Google Sheets):
    - Create clear columns for requirements, design elements, implementation artifacts, and test cases.
    - Use color coding, filters, or grouping to quickly identify traceability gaps and manage changes.
  + **Simple Databases** (e.g., Microsoft Access, Google Sheets with database-like formatting):
    - Create tables linking requirements to their associated software elements, with options to export and share structured reports.
  + **Textual Documents** (e.g., Word documents):
    - Use hierarchical numbering or unique identifiers to establish manual links between requirements, design, code files, and test results.

#### **Advantages**:

* Low-cost and quick setup.
* Easy to manage by non-specialists.
* Flexible for small-scale traceability needs.

#### **Challenges**:

* Limited scalability for large or dynamic requirements.
* Requires **manual updates** when software or requirements change, increasing overhead.

---

#### **2. Diligence in Maintaining Traceability**

Without automated tools to manage changes, **manual diligence** is essential in keeping traceability up to date:

* Assign a dedicated **traceability champion** or team member responsible for maintaining traceability work products.
* Establish **update policies**:
  + After any requirement, design, implementation, or test change, ensure the traceability matrix (or chosen traceability format) is manually updated.
  + Conduct periodic reviews (e.g., weekly or milestone-based) to confirm alignment between all traced elements.
* Use version control (e.g., Git or shared cloud platforms) for traceability documents to avoid losing historical or updated versions.

---

#### **3. Value-Based Requirement Traceability**

Value-based requirement traceability prioritizes traceability activities based on the **importance of each requirement** to mission success. This strategy enables small projects to focus their limited resources effectively by tracing only the **higher-priority requirements** (e.g., safety-critical, mission-critical, or customer-mandated requirements).

##### **Implementation Steps**:

1. **Prioritize Requirements**:

   * Engage the team during the requirements analysis phase to prioritize system requirements by their importance to mission success, safety, or customer demands. Classify requirements into categories such as:
     + **High priority**: Safety-critical, mission-critical requirements (these get full traceability).
     + **Medium priority**: Secondary requirements that support the operation of high-priority requirements (trace partially—e.g., only design artifacts may be linked).
     + **Low priority**: Non-essential, optional, or “nice-to-have” requirements (trace lightly or omit altogether).
2. **Focus Resources**:

   * Allocate time and effort disproportionately toward establishing traceability for **high-priority requirements**. For example:
     + Fully trace a high-priority requirement from its specification to design artifacts, implementation code, test cases, and validation results.
     + Use simpler methods (e.g., high-level links) for medium-priority requirements.
3. **Periodic Validation of Prioritization**:

   * Ensure the prioritization of requirements remains accurate throughout the project. Reassess priorities periodically when new risks or system dependencies arise.

##### **Advantages**:

* Saves effort by avoiding excessive traceability for low-value requirements.
* Improves alignment between team resources and system value.

##### **Challenges**:

* Requires careful **prioritization discussions**—misclassification of a critical requirement as low priority can result in gaps that jeopardize mission success.
* May not be feasible if **full traceability** is mandated by customer standards, NASA policies, or regulatory requirements.

---

#### **4. Structured Traceability Practices**

Even with simple tools, small projects can adopt structured approaches to maintain efficient traceability while minimizing overhead:

##### **Traceability Setup**:

* Create a **Requirements Traceability Matrix (RTM)** in the chosen format (Excel, database, or document). Include:
  + Requirement ID, description, and priority level (e.g., high, medium, or low).
  + Linked design elements.
  + Linked implementation artifacts (e.g., code modules/files).
  + Linked test cases.
  + Verification status (e.g., passed, failed, not yet tested).
* Maximize clarity:
  + Include unique IDs for all elements to avoid ambiguity (e.g., "REQ-101" for requirements, "DES-303" for design links).
  + Incorporate filters, conditional formatting, or reports in spreadsheets/databases.

##### **Periodic Reviews and Communication**:

* Conduct regular **traceability reviews** during milestone meetings:
  + Use checklists to confirm all high-priority requirements are completely traced to relevant design/code/testing artifacts.
  + Identify and resolve traceability gaps.
* Incorporate traceability discussion into **change control boards** to ensure all impacted requirements are linked correctly during changes.

---

#### **5. Consider Future Scalability**

For small projects anticipating **growth** or systems that may later require **full traceability** (e.g., due to customer demand or standards compliance), consider strategies to prepare for future scaling without significant rework:

* Maintain **structured records** in portable formats (e.g., CSV for spreadsheets, or standard database backups) that are easily imported into formal tools when available.
* Use **consistent naming conventions** and unique IDs for requirements, design, implementation, and tests to make migration to automated tools seamless.
* Document traceability decisions (e.g., rationale for value-based prioritization) for customer transparency or expanding traceability scope later.

---

### **Scenario-Specific Guidance**

#### **1. For Projects with Safety-Critical Requirements**:

* Prioritize **full traceability** for all safety-critical requirements per NASA standards (e.g., linking requirements to detailed safety analyses, failure modes, mitigation strategies, and verification testing).
* Create a **separate log** for safety-critical requirements within the RTM to make them easy to track and review explicitly.
* Use redundancy in traceability (e.g., linking safety-critical requirements to multiple supporting tests).

#### **2. For Low-Risk Projects with Minimal Customer Traceability Expectations**:

* Use value-based traceability to minimize unnecessary tracing for low-priority requirements.
* Focus documentation efforts on high-priority customer goals.

#### **3. For Projects Anticipating Future Adoption of Formal Tools**:

* Maintain structured and traceable artifacts (e.g., spreadsheets) with compatibility in mind (e.g., field mapping for easy transition).
* Track lessons learned during manual traceability processes to inform future tool selection and training.

---

### **Summary of Improvements**

1. **Lightweight Tools**: Utilize simple tools like spreadsheets, databases, or textual documents with defined structures for traceability.
2. **Diligence**: Assign responsibilities and implement periodic reviews to keep manual traceability accurate despite budget/tool limitations.
3. **Prioritization**: Use value-based tracing for small budgets, focusing on high-priority requirements, especially safety-critical ones.
4. **Structured Records**: Implement standardized naming conventions, traceability matrices, and periodic checks for maintaining traceability consistency.
5. **Scalability**: Prepare for potential migration to formal tools by maintaining portable and well-organized traceability artifacts.

By tailoring these approaches to the scale and scope of the project, small teams can maintain compliance with traceability requirements effectively, even under resource constraints.

[237](#_tabs-<p></p>)

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-031)

  [Manager's Handbook for Software Development,](http://www.everyspec.com/NASA/NASA-General/SEL-84-101_REV-1_1990_30283/ "Click to open in new window")

  SEL-84-101, Revision 1, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1990.
* (SWEREF-047)

  ["Recommended Approach to Software Development,"](http://everyspec.com/NASA/NASA-GSFC/GSFC-General/SEL-81-305_REV-3_2419/ "Click to open in new window")

  SEL-81-305, Revision 3, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1992.
* (SWEREF-061)

  [Software Requirements Engineering: Practices and Techniques,](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=875d04783add30ea3ed1381f682207a992169ebc "Click to open in new window")

  JPL Document D-24994, NASA Jet Propulsion Laboratory, 2003.
   See Page 20.
  Approved for U.S. and foreign release.
* (SWEREF-127)

  [Baldwin, Diana, AccuReg, Inc. (2001). "Software Development Life Cycles: Outline for Developing a Traceability Matrix." In The Regulatory Forum. Retrieved February 29, 2012 from http://www.regulatory.com/forum/article/tracedoc.html.](http://www.regulatory.com/forum/article/tracedoc.html "Click to open in new window")
* (SWEREF-142) The Importance of Requirements Traceability Brown, Craig (2008). The Project Management Hut. No longer available Formerly accessed June 2011 from http://www.pmhut.com/the-importance-of-requirements-traceability. Other articles are available based on a search on the title.
* (SWEREF-147)

  [Requirements Traceability Matrix - RTM.](https://project-management.com/requirements-traceability-matrix-rtm/ "Click to open in new window")

  Carlos, Tom (October, 2008).
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-201)

  [Doing Requirements Right the First Time,](http://www.crosstalkonline.org/storage/issue-archives/1998/199812/199812-Hammer.pdf "Click to open in new window")

  Hammer, Huffman, Rosenberg (1998). CrossTalk Online,
* (SWEREF-230)

  [ISO/IEC/IEEE 24765:2017 Systems and software engineering -- Vocabulary.](https://www.iso.org/standard/71952.html "Click to open in new window")

  ISO/IEC/IEEE 24765:2017  It was prepared to collect and standardize terminology. Copy attached.
* (SWEREF-233)

  [Traceability,](http://www.pmhut.com/traceability "Click to open in new window")

  Jenkins, Nick (April, 2008). In The Project Management Hut. Retrieved February 29, 2012 from http://www.pmhut.com/traceability.
* (SWEREF-237)

  [Why Software Requirements Traceability Remains a Challenge,](http://www.crosstalkonline.org/storage/issue-archives/2009/200907/200907-Kannenberg.pdf "Click to open in new window")

  Kannenberg, CrossTalkOnline, July/August 2009.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-356)

  [Bidirectional Requirements Traceability,](http://www.westfallteam.com/Papers/Bidirectional_Requirements_Traceability.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2006),
* (SWEREF-560)

  [Orbital Space Plane - Technical Rigor & Integrity](https://llis.nasa.gov/lesson/1504 "Click to open in new window")

  Public Lessons Learned Entry: 1504.
* (SWEREF-576)

  [Software Requirements Management](https://llis.nasa.gov/lesson/3377 "Click to open in new window")

  Public Lessons Learned Entry: 3377.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

Effective bidirectional traceability is pivotal to the success of software projects, particularly in NASA's complex and mission-critical environments. Traceability issues can negatively impact milestone reviews, cost, schedule, and overall mission assurance. Lessons learned from NASA projects provide valuable insights into best practices and pitfalls for managing requirements traceability and its integration into the software lifecycle.

---

### **NASA Lessons Learned Relevant to Bidirectional Traceability**

#### **1. Orbital Space Plane - Technical Rigor & Integrity**

**Lesson Number 1504:**  
Poor requirement traceability can compromise technical products and disrupt **milestone reviews** such as System Requirements Review (SRR) and System Design Review (SDR).

* **Key Issues Identified**:

  + Contractor requirements traceability matrices lacked clarity, failing to address **requirement rationale and allocation**, leaving reviewers unable to understand the work performed.
  + Deliverables were disorganized, making it difficult to trace requirements through the system lifecycle, which hindered communication during critical reviews.
* **Impact**:

  + Poor traceability hampered effective validation and increased ambiguity during milestone reviews, reducing the reviewers' ability to assess technical work performed or trace issues accurately.
* **Lessons to Apply**:

  + **Establish Clear Structure for Traceability Matrices**: Ensure matrices clearly define:
    - Requirement rationale (why each requirement was established).
    - Allocation of requirements to specific system components, interfaces, or tests.
  + **Organize Deliverables for Review**: Create concise and hierarchical documentation that allows reviewers to trace requirements efficiently.
  + **Focus on Bidirectional Traceability**: Ensure traceability links requirements, design, implementation, and testing both upward (to ensure rationale and alignment to broader goals) and downward (to verify completeness in implementation).

---

#### **2. Software Requirements Management**

**Lesson Number 3377:**  
The ability to manage and trace software requirements is **critical for project success**, enabling reliable, high-quality, and cost-effective software products to meet mission needs.

* **Key Issues Identified**:

  + Manual methods for managing software requirements are **inefficient and prone to errors**, contributing to excessive costs and schedule delays.
  + Incomplete, incorrect, or undefined requirements lead to **major cost and schedule impacts later in the lifecycle**, as retroactive fixes often require significant rework.
* **Challenges Highlighted**:

  + Lack of clear, unambiguous, testable, and prioritized requirements results in implementation challenges and misalignment with end-user needs.
  + Shifting or misunderstood requirements complicate traceability and increase the risk of incomplete or inconsistent implementation.
* **Lessons to Apply**:

  + **Automated Tools Are Essential for Efficient Management**: Replace manual methods with requirements management tools like IBM Rational DOORS, RequisitePro, or Cradle, which offer **innovative automated traceability features**.
  + **Collaborative Relationships Improve Communication**: Foster strong collaboration between developers and users/customers to ensure defined requirements are stated clearly, unambiguously, and realistically tied to mission needs.
  + **Early and Continuous Traceability Assessments**: Perform lifecycle traceability assessments during key stages (e.g., requirements specification, design updates, implementation changes) to ensure traceability remains intact throughout development.
  + **Set Standards for Requirements Clarity**: Requirements must be concise, complete, autonomous, implementable, and testable.

---

### **Additional NASA Lessons Learned Relevant to Traceability**

#### **3. Mars Climate Orbiter - Requirements Management Failure**

**Lesson Number 0740:**  
Inconsistent requirements verification and traceability led to catastrophic mission failure during the Mars Climate Orbiter project.

* **Key Issue Identified**:

  + Traceability breakdown arose from insufficient verification of engineering and software requirements, which caused discrepancies between subsystems (e.g., mismatched unit systems between imperial and metric).
* **Impact**:

  + The lack of tight coupling between traced technical requirements, design, and verification resulted in a failure to detect and address critical errors during software development.
* **Lessons to Apply**:

  + **Ensure Comprehensive Verification Links**: Link all requirements to test plans and validation procedures early in the lifecycle.
  + **Cross-Disciplinary Validation**: Traceability must include links between multidisciplinary teams (e.g., software, systems engineering, hardware) to detect mismatched requirements.
  + **Prioritize Traceability for Mission-Critical Elements**: Systems involving high-risk operational requirements, such as navigation or propulsion, need enhanced traceability and verification diligence.

---

#### **4. International Space Station - Change Management Traceability**

**Lesson Number 1622:**  
Incomplete traceability mechanisms led to gaps in requirement updates during subsystem modifications, resulting in integration delays and increased rework costs.

* **Key Issues Identified**:

  + Requirements updates often failed to propagate across affected subsystems, leading to **disconnected designs and implementations**.
  + Change impacts were underestimated due to incomplete understanding of how requirements, design components, and tests were interlinked.
* **Lessons to Apply**:

  + **Use Bidirectional Traceability for Change Impact Analysis:** Ensure that when any requirement is modified, traceability provides impact links from the changed requirement to design artifacts, implementation code, and testing procedures.
  + **Automate Alert Mechanisms**: Tools with automated traceability features should be used to flag downstream dependencies when upstream requirements are changed.
  + **Conduct Regular Traceability Audits**: Periodic audits should confirm completeness and synchronization across all traced software elements after changes.

---

#### **5. Lunar Module Software - Integration Challenges**

**Lesson Number 0021:**  
Traceability failures between requirements and testing caused critical integration challenges in lunar module software, delaying the timeline for testing and validation.

* **Key Issues Identified**:

  + Requirements inadequately traced to unit tests and integration tests, leading to incomplete validation of software modules.
  + Lack of clarity in a traceable hierarchy between software elements caused disconnects during integration activities.
* **Lessons to Apply**:

  + **Close the Traceability Loop**: Ensure robust links directly connect requirements to unit tests, integration tests, and system validation tests to avoid gaps.
  + **Use Hierarchical Traceability**: Define a layered traceability approach with clear mapping between high-level requirements, subsystem/component requirements, and specific implementation tests.
  + **Early Testing of Traceability Links**: Verify traceability links during testing phases, ensuring all critical requirements flow accurately through the integration process.

**6. LLSW03,**

* **Context/Background:** It took ~6 months to obtain limited artifact “access,” insufficient for tool‑based analysis; effectiveness dropped sharply.
* **Lesson Learned:** Contracts must explicitly define **access** (portal read) vs. **delivery** (files for tooling), with rationale and intended use (traceability, FDIR analysis).
* **Evidence/Observation:** Tool‑driven analysis needs full artifacts to compute relationships across thousands of requirements; delays impede phase‑aligned feedback.
* **Cause(s):** Ambiguous contractual language; unclear IV&V needs.
* **Recommendation/Corrective Action:** Specify artifact delivery cadence, formats, and completeness (requirements snapshots, designs, code, tests) and repository permissions.
* **Implementation Guidance:** Tie to **SWE050** (requirements captured/maintained), **SWE052/072** (traceability), **SWE131/141** (IV&V planning/execution).
* **Success Criteria/Verification:** IV&V receives complete, tool‑readable baselines at defined intervals; measurable reduction in analysis latency.
* **Applicability/Scope:** All mission/safety‑critical developments.
* **Related Standards/Requirements:** SWE013, SWE050, SWE052, SWE072, SWE131, SWE141.

**7. LLSW05,**

* **Context/Background:** IV&V analyzed deleted requirements due to delta‑only updates and unsynchronized extractions.
* **Lesson Learned:** Provide **complete, periodic baselines** (not deltas) from the authoritative repository to keep analyses aligned and traceability intact.
* **Evidence/Observation:** Confusion when parent requirements disappeared while traced children remained.
* **Cause(s):** Unclear CM plans; tool extraction difficulties.
* **Recommendation/Corrective Action:** Contract for monthly snapshots; define canonical source; include change logs.
* **Implementation Guidance:** **SWE050/052/072** for traceability across levels/tests.
* **Success Criteria/Verification:** No IV&V findings tied to stale/missing requirements; traceability reports pass audits.
* **Applicability/Scope:** All software classes with formal requirements.
* **Related:** SWE050, SWE052, SWE072.

**8. LL‑SW‑07 — Share Requirement Implementation Status with IV&V**

* **Source LL ID(s):** IVV‑06
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** IV&V needs to know whether a requirement is implemented/in progress/to‑do to avoid premature findings and missed analyses.
* **Lesson Learned:** Provide IV&V **live implementation status** via JIRA/Jama (or equivalent) aligned to features/sprints.
* **Evidence/Observation:** Improved precision when IV&V had requirement‑level visibility.
* **Cause(s):** Limited visibility into development progress.
* **Recommendation/Corrective Action:** Grant read access to status dashboards; map requirement IDs to code/test tickets.
* **Implementation Guidance:** Maintain **SWE‑052/072** traceability across requirements and tests; capture status in plans (**SWE‑013**).
* **Success Criteria/Verification:** Fewer “false‑positive” IV&V issues; synchronized analyses; timely defect resolution.
* **Applicability/Scope:** All software with tracked requirements.
* **Related Standards/Requirements:** **SWE‑013, SWE‑050, SWE‑052, SWE‑072, SWE‑131, SWE‑141**.

**9. LL‑SW‑12 — Consistent Allocation of CBCS Requirements**

* **Source LL ID(s):** GW‑SMA‑LL‑081 (CBCS)
* **Discipline(s):** CBCS, SE&I, Software
* **Context/Background:** Inconsistent CBCS requirement allocation created design/safety issues and contractual resistance to corrections.
* **Lesson Learned:** Apply **consistent** CBCS requirements across all providers to avoid design discrepancies and integration gaps.
* **Evidence/Observation:** Partial applicability led to resistance and unresolved safety concerns.
* **Cause(s):** Uneven contract language; fragmented requirement ownership.
* **Recommendation/Corrective Action:** Centralize CBCS requirements, clarify ownership, and enforce uniform flow‑down (see LL‑SW‑13).
* **Implementation Guidance:** **SWE‑050** (requirement management), **SWE‑052** (traceability), **SWE‑013** (plans).
* **Success Criteria/Verification:** All contracts reflect identical CBCS requirements; traceability shows complete coverage across providers.
* **Applicability/Scope:** Multi‑provider CBCS developments.
* **Related Standards/Requirements:** **SWE‑050, SWE‑052, SWE‑013**.

**10. LL‑SW‑13 — Centralize Safety Requirements and Clarify Verification Closeout**

* **Source LL ID(s):** GW‑SMA‑LL‑007, GW‑SMA‑LL‑033 (SE&I)
* **Discipline(s):** SE&I, Software, CBCS
* **Context/Background:** Safety requirements scattered across subsystem specs; unclear verification responsibilities/closure at L3 caused confusion.
* **Lesson Learned:** Maintain a **single S&MA requirements document** with clear verification strategies, roles, and cross‑level closure definitions.
* **Evidence/Observation:** L3 compliance and verification closure not understood; differences for hardware delivery vs. integrated configuration.
* **Cause(s):** Distributed ownership; late/immature TVV tools/processes.
* **Recommendation/Corrective Action:** Decompose L2→L3 requirements; define verification terminology and responsibilities early; maintain numbering/titles/types.
* **Implementation Guidance:** **SWE‑050** (requirements captured/maintained), **SWE‑052/072** (traceability), **SWE‑018** (reviews).
* **Success Criteria/Verification:** Auditable verification closure at provider and integrated levels; consistent numbering and traceability reports.
* **Applicability/Scope:** All elements and interfaces.
* **Related Standards/Requirements:** **SWE‑050, SWE‑052, SWE‑072, SWE‑018**.

**11. LL‑SW‑19 — Security of Interfaces that Are Hazard Controls**

* **Source LL ID(s):** GW‑SMA‑LL‑046 (flag interface req/verification tied to hazard control)
* **Discipline(s):** SE&I, IHA, Software Requirements
* **Context/Background:** DNG lacked attribute to flag when interface requirement/verification implements a hazard control; gaps and IHCRs increased.
* **Lesson Learned:** Add explicit **tool attributes/flags** to mark interface requirements/verifications that serve as hazard controls; set early in lifecycle.
* **Evidence/Observation:** Beneficial to reduce IHCRs and clarify cross‑element dependencies.
* **Cause(s):** Attribute never implemented; ICD/IDD artifacts were outside DNG.
* **Recommendation/Corrective Action:** Implement DNG attribute; define process to set flags prior to hazard Phase II.
* **Implementation Guidance:** **SWE‑052/072** (traceability) and **SWE‑050** (requirements) for consistent cross‑artifact linking and reporting.
* **Success Criteria/Verification:** Interface hazard controls are discoverable via reports; fewer transfer requests; clearer verification ownership.
* **Applicability/Scope:** All interface‑heavy systems.
* **Related Standards/Requirements:** **SWE‑050, SWE‑052, SWE‑072**.

**12. LL‑SW‑20 — Apply Software Assurance to Ground Segment Architecture**

* **Source LL ID(s):** Ops/Ground Segment Architecture Gap (#OS‑GWLL‑01)
* **Discipline(s):** Ground Software, Ops Safety, Software Assurance
* **Context/Background:** The integrated ground segment (control centers, networks, stations) wasn’t defined early; delayed hazard reports, unclear responsibilities.
* **Lesson Learned:** Define **ground segment architecture early**, including hazard report ownership, requirements, ICDs, and integrated test plans.
* **Evidence/Observation:** MCC hazard report delivery delayed due to undefined overall architecture.
* **Cause(s):** Program‑level planning gap.
* **Recommendation/Corrective Action:** Fund an integrator; include simulations/test facilities; align with software assurance and IV&V processes.
* **Implementation Guidance:** **SWE‑013** (planning), **SWE‑018** (reviews), **SWE‑050** (requirements/ICDs).
* **Success Criteria/Verification:** Architecture documents baselined; hazard reports on schedule; integrated test coverage achieved.
* **Applicability/Scope:** All programs with multi‑center ground segments.
* **Related Standards/Requirements:** **SWE‑013, SWE‑018, SWE‑050**.

### **Key Themes from NASA Lessons Learned**

From the above lessons learned, several recurring themes and actionable practices emerge:

#### **1. Impacts of Poor Requirement Traceability**

* **Disrupted Milestone Reviews**: Poor traceability confuses reviewers and jeopardizes the approval of technical deliverables (Lesson Number 1504).
* **Increased Lifecycle Costs and Delays**: Incorrect or incomplete requirements significantly increase costs and schedules when issues arise later in development (Lesson Number 3377).
* **Critical Failure Risks**: Lack of traceability has directly contributed to mission failures, such as the Mars Climate Orbiter (Lesson Number 0740).

#### **2. Recommendations for Effective Bidirectional Traceability**

* **Automate Where Possible**: Reduce inefficiencies of manual methods through tools that track changes and link elements automatically (Lesson Number 3377).
* **Prioritize High-Impact Requirements**: Focus traceability efforts on safety-critical, mission-critical, and high-risk requirements first to save resources while ensuring priority coverage (Lesson Number 1504, 0740).
* **Collaborate Between Teams**: Ensure end-users, customers, and developers work closely to define clear, actionable requirements, improving traceability across disciplines (Lesson Number 3377, 1622).
* **Audit and Validate Early**: Perform regular reviews of traceability matrices, hierarchy completeness, and testing results to identify gaps before they impact integration (Lesson Number 0021).

---

### **Conclusion**

The lessons learned reinforce the importance of bidirectional traceability to prevent project disruption, minimize costs, reduce risks, and deliver high-quality software products. NASA projects must treat traceability as a mission-critical activity, employing structured processes, automated tools, and team collaboration to achieve traceability that supports both technical rigor and operational success. By applying these lessons, teams can address common pitfalls and improve performance across the software lifecycle.

### 6.2 Other Lessons Learned

**Interface Control Documents (ICDs)**

* ICDs must document data behaviors for critical parameters.
* Include human factor considerations in ICD documentation (e.g., capturing notes that identify inconsistencies or other potential pitfalls).
* It is essential to have unambiguous traceability between ICD parameters and downstream software artifacts such as requirements, code, tests, and models.

# 7. Software Assurance

**SWE-052 - Bidirectional Traceability**

3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between the following software elements:

|  |  |  |  |
| --- | --- | --- | --- |
| Bi-directional Traceability | Class A, B, and C | Class D | Class F |
| Higher-level requirements to the software requirements | X |  | X |
| Software requirements to the system hazards | X | X |  |
| Software requirements to the software design components | X |  |  |
| Software design components to the software code | X |  |  |
| Software requirements to the software verification(s) | X | X | X |
| Software requirements to the software non-conformances | X | X | X |

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that bi-directional traceability has been completed, recorded, and maintained.

2. Confirm that the software traceability includes traceability to any hazard that includes software.

## 7.2 Products

Objective: Provide comprehensive assurance products that analyze traceability across the software lifecycle and pinpoint areas requiring corrective action, particularly for hazards involving software.

#### **Products to be Delivered by SA**

##### **1. Analysis of Bidirectional Requirements Traceability**

SA must perform an analysis of bidirectional traceability, ensuring all requirements flow logically and completely between lifecycle artifacts. This analysis should:

* **Verify completeness**:
  + Ensure all system-level requirements are mapped to lower-level software requirements.
  + Trace software requirements bi-directionally to design elements, implementation artifacts (e.g., code modules), and test procedures.
* **Identify and resolve gaps**:
  + Highlight missing links, circular traces, or disconnected (orphan) elements in the traceability matrix.
  + Ensure no high-priority safety-critical requirement or hazard is left untraced or poorly linked.
* **Audit rationale**:
  + Confirm traceability links include clear justifications for decisions made during allocation (e.g., reasoning behind software requirements derived from system risks).

##### **2. Hazard Analysis Traceability**

SA must analyze traceability between hazards (documented in hazard analysis or risk management artifacts) and software requirements.

* **Ensure hazards that include software are fully mapped**:
  + All hazards posing risks to mission assurance, human safety, or critical assets must have related software requirements clearly identified, traced, and verified.
  + Validate links from software-related hazards to test cases designed specifically to mitigate or monitor these hazards.
* **Corrective actions for traceability gaps**:
  + Highlight any software requirements, designs, or tests missing links to hazards that could compromise risk mitigation.
  + Recommend and document corrective actions to close these gaps before key project milestones.

##### **3. Bidirectional Traceability Results**

SA shall provide comprehensive results that summarize bidirectional traceability completion rates, gaps, and resolutions. These results should include:

* **Traceability matrices** showcasing completed trace links:
  + System-level requirements ↔ Software requirements ↔ Design components ↔ Code modules ↔ Test procedures.
  + Software-related hazards ↔ Software requirements ↔ Test cases targeting hazard mitigation.
* **Trend analysis**:
  + Document trace completeness trends and progress over time.
  + Track areas requiring repeated corrective actions to identify persistent issues or inefficiencies.
* **Corrective actions** taken:
  + List all traceability gaps identified and resolved during the lifecycle, emphasizing safety-critical or hazard-related gaps.

##### **4. Integration with Hazard Analysis Documentation**

SA must ensure bidirectional traceability results are **integrated with hazard analysis artifacts**, including:

* Hazard Analysis Reports (HARs).
* Fault Trees (if applicable).
* Failure Modes and Effects Analysis (FMEA). This integration enables seamless alignment between risks and their associated software components.

---

## 7.3 Metrics

Objective: Provide quantitative metrics that measure the completeness, quality, and impact of traceability efforts throughout the software lifecycle, with a particular focus on safety and hazard-related traceability.

#### **Recommended Metrics**

##### **1. Coverage Metrics**

Coverage metrics measure the **extent of traceability completion** across different lifecycle areas:

* **Number of Software Requirements**:
  + Total count of requirements at various levels of granularity (Project-level, Application-level, Subsystem-level, System-level).
* **Percentage of Traceability Completed**:
  + Breakdown across lifecycle artifacts:
    - System-level requirements to software requirements.
    - Software requirements to design.
    - Design to code.
    - Software requirements to test procedures.
* **Percentage of Hazard Traceability Completed**:
  + Fraction of identified hazards (documented in FMEA or HAR) traced to software requirements and verified by test procedures.

##### **2. Trace Quality Metrics**

Trace quality metrics assess the **accuracy and efficiency of traceability** links, revealing common defects and trends:

* **Defect Trends for Trace Quality**:
  + Number of trace defects such as:
    - **Circular traces**: Requirements traced back to themselves or their indirect sources.
    - **Orphans**: Requirements, design elements, or tests without incoming or outgoing trace links.
    - **Widows**: Elements traced only partially, with discrete gaps in the lifecycle (e.g., test procedures missing links to software requirements).
* **Traceability Gaps**:
  + Percentage of requirements, design elements, or hazards left untraced at any given lifecycle phase.

##### **3. Safety-Critical and Hazard-Related Metrics**

These metrics focus on traceability for **safety-related requirements** and software-related hazards:

* **Number of Safety-Related Requirement Issues**:
  + Count of safety-related requirement issues (open and closed) tracked over time.
  + Breakdown by type (e.g., traceability gaps, incomplete tests, design flaws).
* **Number of Safety-Related Non-Conformances Identified by Lifecycle Phase**:
  + Number of safety-related non-conformances detected at each lifecycle phase (Requirements, Design, Implementation, Testing).
  + Helps identify lifecycle phases where quality assurance activities need strengthening.
* **Percentage of Test Procedures Addressing Software-Related Hazards**:
  + Fraction of hazards involving software successfully mitigated by verified test cases.

##### **4. Traceability Progress Metrics**

Metrics to track progress over the lifecycle in achieving bidirectional traceability:

* **Number of Software Requirements Verified Over Time**:
  + Track progress in completing test procedures linked to software requirements at key milestones (SRR, SDR, TRR, and post-deployment).
* **Open/Closed Safety-Related Trace Issues Over Time**:
  + Count of trace issues flagged and resolved as the project progresses.
* **Time-to-Close Safety Traceability Gaps**:
  + Measure the average duration required to identify, resolve, and validate traceability gaps for safety-related requirements or hazards.

##### **5. Efficiency Metrics**

Efficiency metrics reflect how traceability improves over time and impacts project goals:

* **Cost of Traceability Defects**:
  + Total time, effort, and cost associated with resolving traceability gaps, particularly in safety-critical scenarios.
* **Percentage of Automated Traceability Utilized**:
  + For projects with tools offering automatic traceability, track the percentage of trace links leveraged by automation versus manual methods.

---

### **Action Plan for Software Assurance**

1. **Proactive Analysis**:

   * Conduct proactive and regular assessments of bi-directional traceability across lifecycle artifacts.
   * Flag areas of concern, particularly where hazards or safety-critical requirements are insufficiently traced, and implement corrective actions.
2. **Integration with Risk/ Hazard Documentation**:

   * Ensure traceability metrics align with broader risk assessment artifacts like FMEA and HAR.
   * Verify that all software-related hazards are linked to test cases and mitigation procedures.
3. **Continuous Improvement**:

   * Use defect trends and metrics to refine traceability processes, resolving recurring gaps or inefficiencies.
   * Leverage lessons learned from previous projects to improve trace completion rates for high-impact (safety-critical, hazard-related) requirements.
4. **Prioritization**:

   * Focus on safety-critical and mission-critical traceability as a primary objective for assurance activities.
   * For smaller projects or constrained programs, implement *value-based traceability* to prioritize high-risk requirements.
5. **Automated and Manual Methods**:

   * Encourage adoption of automated tools where feasible (e.g., IBM DOORS, RequisitePro, Cradle) for high-efficiency traceability, while maintaining rigorous foundational methods for manual traceability when tools are unavailable.

---

### **Conclusion**

This enhanced guidance ensures Software Assurance activities fully account for traceability gaps and continuously assess progress using actionable metrics. By analyzing both bidirectional traceability and hazard-related trace results, SA provides critical oversight to ensure safety, mission success, and lifecycle compliance. Through the effective use of metrics, teams can identify areas of improvement, balance priorities, and optimize traceability over time without compromising project quality or cost-effectiveness.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

Confirm that bi-directional traceability has been completed, recorded, and maintained for the software elements in NPR 7150.2D - Table 1 in section 3.12.1 appropriate to software classification. Review the software results of their bi-directional traceability (usually performed in a tool) and check that all the traces have been listed below have been done, using the software classification to determine which traces are required. If there are issues found in the initial trace matrices, track to see that these are addressed. When changes are made to the system, confirm that any corresponding changes to the traceability have been documented.

3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between the following software elements: 

|  |  |  |  |
| --- | --- | --- | --- |
| Bi-directional Traceability | Class A, B, and C | Class D | Class F |
| Higher-level requirements to the software requirements | X |  | X |
| Software requirements to the system hazards | X | X |  |
| Software requirements to the software design components | X |  |  |
| Software design components to the software code | X |  |  |
| Software requirements to the software verification(s) | X | X | X |
| Software requirements to the software non-conformances | X | X | X |

Confirm that the bi-directional software traceability includes traceability to the hazard analysis

The project should have bi-directional traceability between the software requirements and software-related system hazards, including hazardous controls, hazardous mitigations, hazardous conditions, and hazardous events.

Traceability between the software requirements and software-related system hazards, including hazardous controls, hazardous mitigations, hazardous conditions, and hazardous events, allows us to determine which software components are software safety-critical and ensure that the required software is safety-critical requirements are included in the software requirements and software activities.

## 7.4.1 Software Safety Requirements

Software safety requirements contained in NASA-STD-8739.8 [278](#_tabs-<p></p>)

The software safety requirements contained in NASA-STD-8739.8 for safety-critical software are:

1. Confirm that the identified safety-critical software components have implemented the safety-critical software assurance requirements listed in this standard.

2. Analyze the software design to ensure that partitioning or isolation methods are used to logically isolate the safety-critical design elements from those that are non-safety-critical.

3. Analyze the design and work with the project to implement NPR 7150.2 [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) requirement items "a" through "l."

4. Assess that the source code satisfies the conditions in the NPR 7150.2 [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) requirement "a" through "l" for safety-critical software at each code inspection, test review, safety review, and project review milestone.

5. Confirm 100% code test coverage has been achieved or addressed for all identified software safety-critical components or provide a risk assessment explaining why the test coverage is not possible for the safety-critical code component.

6. Assess each safety-critical software component to determine the software component’s cyclomatic complexity value.

7. Confirm that all identified software safety-critical components have a cyclomatic complexity value of 10 or lower. If not, provide a risk assessment showing why the cyclomatic complexity value needs to be higher than ten and why the software component cannot be structured to be lower than 10.  

Figure 3 shows bidirectional traceability as a traceability chain that can be traced in both the forward and backward directions.

Figure 3

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics)        * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

# 8. Objective Evidence

Objective evidence refers to tangible, verifiable artifacts or outputs that demonstrate compliance with this requirement. For Requirement 3.12.1, the evidence must prove that bidirectional traceability has been implemented, maintained, and verified throughout the software development lifecycle.

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

### **Objective Evidence Categories for Requirement 3.12.1**

#### **1. Requirements Traceability Matrix (RTM)**

The **Requirements Traceability Matrix (RTM)** is the primary evidence for bidirectional traceability between software elements. It directly links system-level requirements, software-level requirements, design components, implementation code, test cases, and hazards.

##### **Must Include**:

* Links between **System-Level Requirements ↔ Software Requirements** to ensure all high-level system needs are cascaded into software needs.
* Traceability from **Software Requirements ↔ Design Artifacts** (e.g., architecture diagrams, detailed designs).
* Traceability from **Design Artifacts ↔ Code Implementation**, confirming the design is fully realized.
* Traceability from **Software Requirements ↔ Test Procedures/Test Cases** to verify all requirements are testable and validated during verification and validation (V&V).
* Traceability from **Hazards ↔ Software Requirements ↔ Tests**, ensuring all hazards posing a risk to safety or mission success are correctly mitigated.
* Link identification across all mapped items, such as unique identifiers (e.g., REQ-101, TEST-305, HAZ-14).

##### **Examples of RTM Evidence**:

* Export of a **fully populated RTM** with all lifecycle links:
  + Example: A table or tool-generated matrix showing that:
    - Requirement REQ-001 is traced to architecture design DES-101, code component CODE-150, and test procedure TEST-001.
    - Hazard HAZ-072 is linked to requirement REQ-015 and the corresponding test case TEST-078.
* **Tool Output**:
  + Automated RTMs generated by tools such as IBM DOORS, RequisitePro, or Jira.

---

#### **2. Design Review Artifacts**

Design reviews throughout the lifecycle (e.g., System Requirements Review [SRR], Software Design Review [SDR], Preliminary Design Review [PDR], Critical Design Review [CDR]) must include evidence that traceability was assessed.

##### **Must Include**:

* **Bidirectional traceability checked during reviews**:
  + Traceability completeness (e.g., are all system requirements mapped downward to software requirements? Are requirements traced forward to test plans, validation, implementations?).
* **Review findings**:
  + Documentation of traceability gaps discovered, if any, and corrective actions planned or implemented prior to milestone sign-off.
* **Presentation Materials**:
  + Slidedecks or charts with visual representations, such as:
    - Traceability graphs showing relationships between requirements, design, and test cases.
    - Coverage maps: Percentage of traced vs. untraced elements during the review stage.

##### **Examples of Evidence**:

* Design Review Checklist:
  + A completed checklist confirming bidirectional traceability was reviewed for each system-level requirement, hazard-linked requirement, and software requirement.
* Signed Review Documentation:
  + Meeting minutes or evaluation forms confirming stakeholders verified and accepted traceability results.

---

#### **3. Test Plan, Reports, and Procedures**

Testing is a critical activity to demonstrate bidirectional traceability. Test-related artifacts must show traces from software requirements to test cases and the results of test execution.

##### **Must Include**:

* **Test Plans**:
  + Documentation mapping software requirements to planned test procedures.
  + Evidence that all software requirements are covered with corresponding test cases.
* **Test Procedures**:
  + Detailed scripts or procedural instructions showing how each test verifies a software requirement.
* **Test Results/Reports**:
  + Reports showing successful execution of test procedures and demonstration of traceability completeness.
  + Link issues or test failures to specific traced requirements with clear resolutions or defect trends.

##### **Examples of Evidence**:

* **Test Case Trace Reports**:
  + A matrix or report from a testing system (e.g., TestRail, HP ALM, or similar) showing requirement-to-test links and tracking verification status.
  + Example entry: "Requirement REQ-035 linked to Test Case TEST-205 (Passed)."
* **Test Execution Results**:
  + Evidence showing pass/fail status for requirements verification and validation, with clear backward links to the originating requirement.

---

#### **4. Version-Controlled Traceability Documents**

Documentation of traceability must be maintained under configuration control to ensure consistency and continuity over the project lifecycle.

##### **Must Include**:

* **Configuration Management System (e.g., Git, SVN, or similar)**:
  + Version-controlled traceability documents like RTMs, test matrices, and associated deliverables.
  + Logs demonstrating updates to traceability documents as requirements, designs, or tests evolve.
* **Change Logs**:
  + Evidence that traceability impacts were analyzed and updated after system requirement changes.

##### **Examples of Evidence**:

* **Version-Controlled RTM Updates**:
  + History of updates to the traceability matrix linked to requirement or design changes (e.g., requirement REQ-015 was revised in version 2.4, and associated test case links in TEST-042 were updated accordingly).
* **Baseline Traceability Audit Reports**:
  + Configuration audit checklists documenting traceability accuracy for key project baselines (e.g., system design baseline, test baseline).

---

#### **5. Hazard Analysis Traceability and Safety Assurance**

Hazards and safety-critical requirements must be fully documented and traced through design and testing to show mitigation of risks.

##### **Must Include**:

* **Hazard Analysis Reports (HAR)**:
  + Evidence that all hazards involving software components are traced to software requirements.
* **Safety Requirement Links**:
  + Links from hazards to:
    - Software requirements designed for hazard mitigation.
    - Validation test cases demonstrating mitigation effectiveness.
* **Verification Audit Reports**:
  + Evidence that hazard-to-test traceability is complete and passes lifecycle review.

##### **Examples of Evidence**:

* Unique identifiers linking HAR entries (e.g., HAZ-112) to:
  + Software requirements (REQ-052 and REQ-106).
  + Test cases (TEST-300 validating mitigation of HAZ-112).
* Reports summarizing traceability of all hazards to test procedures.

---

#### **6. Lessons Learned or Traceability Evaluations**

If traceability issues arise during the lifecycle, lessons learned and remediation efforts must be documented.

##### **Must Include**:

* **Lessons Learned Reports**:
  + Documentation of traceability gaps identified during reviews and actions taken to resolve them.
  + Examples:
    - "Requirement REQ-040 initially lacked a design implementation. This was corrected by linking CODE-073."
    - "Test cases for HAZ-015 were missing and were added after PDR."
* **Post-Milestone Evaluation Reports**:
  + Traceability evaluation results post-SRR, SDR, or CDR showing improvements over time.

##### **Examples of Evidence**:

* Final Traceability Gap Analysis Report:
  + Report documenting open/closed issues related to trace quality and improvement efforts by the end of the lifecycle.
* Corrective Actions Document:
  + Summary of steps taken to ensure traceability compliance, such as workflow refinements or team training.

---

### **Examples of Tools That Generate Objective Evidence**

1. **Requirements Management Tools**:
   * IBM DOORS, Cradle, Jama Connect, Rational RequisitePro.
   * Objective evidence output: Traceability matrices, visual trace graphs, change impact analysis logs.
2. **Testing Tools**:
   * TestRail, HP ALM, Tosca, or JIRA with test case plugins.
   * Objective evidence output: Test procedures linked to requirements, test completion reports, defect trace reports.
3. **Configuration Management Tools**:
   * Git, SVN, Perforce.
   * Objective evidence output: Change logs, version-controlled RTMs/history of trace artifacts.

---

### **Summary of Objective Evidence for 3.12.1**

| **Category** | **Examples of Evidence** |
| --- | --- |
| Requirements Traceability Matrix (RTM) | Populated RTMs showing links across lifecycle: system requirements ↔ software requirements ↔ design ↔ code ↔ tests ↔ hazards. |
| Design Review Artifacts | Milestone review checklists, meeting minutes, traceability charts, gap analysis summaries, corrective actions. |
| Test Plans, Reports, and Procedures | Test procedures and results directly linked to requirements, hazard trace validations, and automated test reports from tools. |
| Version-Controlled Documents | Configuration logs of RTM changes, links to requirements/design/test updates in version-controlled systems (e.g., Git logs, document revisions). |
| Hazard Analysis Traceability | Hazard Analysis Reports (HAR), fault tree links, and evidence of mitigation testing for hazards involving software. |
| Lessons Learned | Post-milestone evaluations, corrective action plans for traceability improvements, and documentation of known issues resolved during the lifecycle. |

This objective evidence ensures compliance with Requirement 3.12.1 and demonstrates that bidirectional traceability processes are complete, documented, and verifiable throughout the software's lifecycle.
