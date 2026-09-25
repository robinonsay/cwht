# 8.02 - Software Quality

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695703. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality

8.02 - Software Quality

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695703)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695703&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Planning](#tabs-2)
* [3. Workmanship](#tabs-3)
* [4. Software Failure Analysis](#tabs-4)
* [5. Design](#tabs-5)
* [6. Resources](#tabs-6)

# 1. Introduction

The **Software Assurance and Software Safety Standard** establishes requirements for implementing a structured and systematic approach to software assurance, software safety, and Independent Verification and Validation (IV&V). This applies to software that is created, acquired, provided, used, or maintained by or for NASA. The standard is designed to enable consistency and rigor in software assurance and safety activities across all stages of the software life cycle, promoting high-quality and reliable outcomes.

Software assurance activities may be performed by personnel from various domains, including program, project, engineering, facility, or Safety and Mission Assurance (SMA) organizations. By clearly defining such requirements, the standard ensures that these professionals apply a uniform approach across all forms of software—be it systems software, embedded applications, or other critical mission software.

In alignment with NPR 7150.2, **NASA Software Engineering Requirements**, the Software Assurance and Software Safety Standard (278) supports the implementation of key practices and sub-disciplines in workforce activities. Given the diversity in NASA programs and missions, the specific implementation of this standard may vary to suit the requirements and context of the system and software products being developed or maintained.

---

### 1.1 Objectives of the Software Assurance and Software Safety Standard

The primary objectives of the Software Assurance and Software Safety Standard are to:

1. Ensure that **processes, procedures, and products used to create, maintain, and support software** conform to applicable quality, safety, and performance requirements.
2. Provide a framework for assessing adherence to development standards and evaluating the adequacy of software processes to meet mission goals.
3. Establish confidence that the defined software processes are sufficient to produce software of the required quality, reliability, and safety.
4. Measure and verify software product quality and ensure risks are mitigated across the software life cycle.
5. Ensure that safety-critical software requirements are rigorously implemented to maintain system and operational safety.
6. Enhance system security by addressing risks from potential vulnerabilities and ensuring secure software behavior.
7. Employ evidence-based methodologies, such as thorough analysis and testing, to conduct independent assessments of critical software products and processes.

---

### 1.2 Overview of Key Software Quality Steps

To guarantee mission-critical software reliability and safety, software development and assurance must aim to deliver software that operates as intended under all conditions, including adverse scenarios. Additionally, maintainability must allow for efficient and effective updates, addressing changes without introducing faults. Reliable software should not only perform under nominal conditions but also maintain a safe state during failures or off-nominal events, ensuring that issues are detected, mitigated, and proactively resolved.

Achieving software quality requires early planning and sustained focus throughout each development phase. This systems-level approach integrates assurance activities that are well-aligned with design, development, and maintenance milestones.

Key assurance steps involve:

* **Workmanship (process audits)** to ensure disciplined process adherence.
* **Software requirements analysis** to capture and validate all functional, safety, and system-level requirements.
* **Software design analysis** to assess safe and efficient design solutions.
* **Software safety analysis (SSA)** to identify and mitigate risks related to safety-critical components.
* **Source code analysis** to ensure adherence to critical coding practices and mitigate potential errors.
* **Software testing analysis** for robust validation of functional and performance characteristics.
* **Static code analysis** to preemptively identify issues within the codebase.

Seamlessly integrating these activities ensures the software is resilient, maintainable, and ready for deployment in complex environments.

### 1.3 Introduction to Key Activity Areas

#### 1.3.1 Workmanship (Process Audits)

High-quality software begins with robust development processes. Process audits focus on verifying adherence to established standards and preventing fault introduction. Quality metrics, including defect counts, are collected and monitored to identify trends and maintain consistent quality. This ensures the integrity of the development lifecycle. See [8.59 - Audit Reports] for further guidance.

#### 1.3.2 Software Requirements Analysis

Requirements analysis ensures that all software functions align with system needs—including performance, interfaces, safety, and security. In NASA projects, logical decomposition is used to generate detailed software requirements, validated against acceptance criteria. For more detail, see [8.54 - Software Requirements Analysis] and [SWE-034 - Acceptance Criteria].

#### 1.3.3 Software Design Analysis

Design analysis transforms software requirements into dependable architectures and detailed components. This process is critical for verifying that system designs address both nominal and off-nominal conditions while reducing risks and enabling future modifications. For additional details, see [8.55 - Software Design Analysis] and [8.01 - Off-Nominal Testing].

#### 1.3.4 Software Safety Analysis (SSA)

SSA evaluates whether software components meet safety-critical requirements and align with system hazard analyses. It focuses on ensuring that risk claims in hazard reports hold true and adopts requirements from NASA-STD-8739.8 and NPR 7150.2 SWE-205. See [8.09 - Software Safety Analysis] for further information.

#### 1.3.5 Source Code Analysis

This activity analyzes source code quality to detect and eliminate issues that may affect software integrity. It confirms conformance to coding standards, safety, and functional requirements. Refer to [8.56 - Source Code Quality Analysis].

#### 1.3.6 Software Testing Analysis

Testing ensures that software meets functional, performance, and safety expectations. The review of test plans, procedures, and results is part of this process. Refer to [8.57 - Testing Analysis] for guidance.

#### 1.3.7 Static Code Analysis

Static code analysis is a proactive technique to identify and address issues within the software before execution. It plays a significant role in achieving fault-free implementation.

### 1.4 Software Life Cycles

The Software Assurance and Software Safety Standard is built to support all types of software development life cycles. Projects are not limited to a specific model (e.g., waterfall, agile) and can adopt the standard according to the specific development framework being used.

### 1.5 Additional Guidance

Additional resources and links are available to provide further details on implementing the Software Assurance and Software Safety Standard. Refer to the **Resources tab** for access to the relevant guidance materials.

### Key Takeaways

By committing to structured planning, adherence to standards, and rigorous assurance principles, NASA can ensure software reliability and safety for mission-critical systems. The Software Assurance and Software Safety Standard prioritizes a lifecycle approach to building dependable software while minimizing risks to personnel, assets, and mission success.

# 2. Plan for High-Quality Software

Planning for high-quality software is a foundational step in ensuring mission success, reliability, and safety. Effective planning begins with a comprehensive understanding of the system's objectives, operational requirements, and the critical role software plays in achieving them. This requires active collaboration between software engineers, system analysts, and designers throughout the development process to ensure seamless integration of functional and performance requirements across hardware and software domains. Recognizing the distribution of functionality—between hardware and software—early in the process enables teams to identify key software requirements that support both system-level objectives and operational concepts.

Moreover, software must be designed with robust features that proactively monitor and respond to hardware faults, system failures, and other adverse factors that could jeopardize mission objectives. These features must be integrated seamlessly to mitigate risks and maintain reliability under nominal and off-nominal conditions. Measuring software quality effectively requires identifying appropriate metrics, developing detailed plans for their measurement, and conducting systematic collection and analysis to guide improvements throughout the software lifecycle.

## 2.1 Key Analyses to Support Quality Planning

Key analyses, such as **Fault Tree Analysis (FTA)** and **Failure Modes and Effects Analysis (FMEA)**, are indispensable in planning for software quality. These tools provide complementary perspectives:

* **FTA**, a top-down analysis, identifies critical paths to system failures by examining high-level failure modes.
* **FMEA**, a bottom-up analysis, leverages findings from FTA to focus on specific failure modes, examining how individual components contribute to system risks.

Integrating these techniques with system-level hazard analyses—such as software hazard analyses and system reliability analyses—helps prioritize efforts by narrowing the scope of software assessments to areas with the highest potential impact on safety and reliability.

Additionally, the **System Critical Items List (CIL)** should be reviewed to identify any software-related impacts. If new critical areas or hazards are uncovered during software-specific analyses, they must be escalated to system-level hazard reports. Supporting documentation should include detailed information about the associated risks, their criticality, and corresponding mitigations. This collaborative process ensures that software is tightly aligned with system-wide safety and reliability goals, avoiding gaps between subsystem analyses and overall mission assessments.

For further guidance on methodologies, see [8.07 - Software Fault Tree Analysis] and [8.05 - Software Failure Modes and Effects Analysis]. These resources provide deeper insights into implementing FTA and FMEA techniques effectively.

## 2.2 Determining Necessary Software Quality

Determining the level of software quality required for a given project varies based on the mission’s objectives, constraints, and risk profile. A tailored approach ensures resources are appropriately focused on areas that demand higher reliability while avoiding overengineering in less critical domains.

Software quality planning should begin with inheriting requirements from the broader system’s objectives, with special consideration given to how hardware mitigates software-specific risks. For example, systems with highly reliable hardware may reduce the criticality of some software components, while other systems may place greater dependency on software to ensure safe operation during hardware faults or failures.

In general, highly critical systems—such as life-support systems, spacecraft navigation, and mission-critical operations—should default to the assumption that highly reliable software is essential. Unless proven otherwise through risk assessments or mitigations, such software should meet the highest reliability standards, including rigorous fault detection, recovery mechanisms, and redundancy to maintain a safe state at all times.

Conversely, proof-of-concept systems, experimental prototypes, or research software not intended for flight or operational use may prioritize speed and flexibility over reliability. In these cases, reliability levels need only meet the requirements to support the experiment, demonstration, or study rather than long-term operational robustness. Careful scoping of software quality for prototypes ensures resources are allocated effectively while maintaining feasibility in early-stage technologies.

By maintaining focus on mission-driven constraints and objectives, the planning process ensures that software quality aligns with the needs of the system, facilitating both operational success and reliability without incurring unnecessary overhead.

## 2.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 3. Development: Ensuring Workmanship in Software

High-quality software workmanship is critical to minimizing defects and ensuring reliability throughout the software development process. By adhering to structured, consistent, and adaptive software development practices, teams can proactively detect and eliminate errors. Moreover, these practices should evolve over time, as lessons learned from defect analysis inform process refinements that reduce the likelihood of future defect insertion.

---

## 3.1 Key Steps to Ensure Workmanship

#### **Defect Tracking and Analysis**

Effective defect tracking and management form the backbone of high-quality software workmanship. Software assurance (SA) personnel play a vital role in monitoring defects throughout the software development lifecycle. Their responsibilities include classifying defects, identifying systemic issues, and analyzing trends to uncover root causes of errors. Based on these insights, SA personnel work closely with software engineering teams to implement targeted solutions, such as:

* Revising development processes
* Introducing additional peer reviews or inspections
* Utilizing enhanced testing procedures
* Deploying automated quality analysis tools

The systematic tracking of all defects—whether encountered during development, maintenance, or testing—ensures that issues are categorized, recorded, and analyzed to inform actionable improvements. This process not only addresses immediate defects but also drives iterative refinements to engineering practices for long-term reliability gains.

#### **Addressing Defect Sources**

Software defects may originate from several areas, such as:

1. **Legacy Code**: Code inherited from earlier systems or projects, which might contain undetected weaknesses or outdated approaches.
2. **Development and Maintenance Activities**: Defects introduced due to process inefficiencies, human error, or insufficient testing during software life cycle phases.

To combat these defect sources, teams must adopt a robust multi-layered approach that encompasses:

* Disciplined engineering processes
* Rigorous peer reviews and inspections
* Code analysis tools for static and dynamic validation
* Comprehensive integration and system testing

Software assurance activities mandated by relevant NASA standards (e.g., defect tasking and metrics tracking) are designed to enhance the reliability of both developed and acquired software products. These measures create a framework for early identification and proactive resolution of issues.

---

## 3.2 Early and Continuous Defect Analysis

Defect analysis is most effective when initiated early—during the requirements phase—and consistently applied throughout development. By tracking and analyzing metrics such as error frequency, defect severity, and system impact, teams can measure progress and adjust processes as needed to reduce defect rates.

#### **Metrics and Agile Development Practices**

In iterative methodologies such as Agile development, defect analysis plays a key role in identifying and managing technical debt. For example:

* Defects and issues uncovered after each sprint should be systematically captured, categorized, and reviewed.
* Trend analysis of defect metrics across sprints can reveal underlying causes, highlighting areas needing targeted improvements.
* If defect rates rise persistently across sprints, corrective actions—such as reevaluating development processes, increasing testing rigor, or refining user stories—should be addressed proactively during sprint retrospectives and planning sessions.

Continuous analysis ensures teams remain agile and responsive while maintaining high standards of reliability. Metrics such as defect resolution rates, error impact assessments, or defect reintroduction frequencies provide clear visibility into progress and signal when corrective actions are required.

For related processes on tracking and addressing defects, see:

* **SWE-054:** Corrective Action for Inconsistencies
* **SWE-057:** Software Architecture
* **SWE-068:** Evaluate Test Results
* **SWE-071:** Update Test Plans and Procedures
* **SWE-192:** Software Hazardous Requirements

---

## 3.3 Software Assurance Role

The role of **Software Assurance (SA)** personnel extends beyond defect monitoring to evaluating the effectiveness of their own processes and ensuring they drive meaningful improvements in software quality. SA personnel should:

* **Validate metrics**: Confirm the reliability of quality metrics used by engineering teams, supplementing these metrics with independent analyses and observations.
* **Assess robustness**: Analyze how well the software withstands operating environments and responds to errors, ensuring reliability in critical scenarios.
* **Enhance reliability**: Provide actionable feedback to improve reliability processes, particularly when trends suggest areas of concern.

By bridging quality metrics with their own assessments, SA personnel offer a holistic view of software robustness and reliability, ensuring insights are grounded in objective evidence.

For SA tracking and reporting requirements, consult:

* **SWE-024:** Plan Tracking
* **SWE-039:** Software Supplier Insight
* **SWE-201:** Software Non-Conformances

---

## 3.4 Continuous Improvement

Continuous improvement is the cornerstone of high-quality software workmanship. Through systematic collection, tracking, and analysis of defects and reliability metrics, SA personnel can provide an accurate and transparent status of project reliability. However, the goal is not simply to react to defects—it is to use them as a source of insight to refine processes and drive proactive improvements over time.

Key strategies for continuous improvement include:

* Regularly evaluating defect trends and root causes to identify opportunities for process optimization.
* Leveraging lessons learned to improve peer reviews, testing methodologies, and code quality analysis.
* Encouraging feedback loops between SA personnel and development teams, fostering collaboration and shared goals for quality enhancement.

By focusing on proactive refinement alongside reactive management, software assurance ensures that quality and reliability are not static requirements but evolving practices that adapt to challenges across the entire development lifecycle.

---

Ensuring workmanship in software is not just about resolving defects; it is about building a culture of reliability, collaboration, and continuous improvement—one where every artifact and process contributes to delivering the safest and most dependable software possible for NASA’s critical missions.

## 3.5 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 4. Software Failure Analysis

Failure analysis evaluates the software’s response to faults and its capability to maintain operational integrity throughout the design and development lifecycle. This involves identifying potential weaknesses and vulnerabilities that could affect system functionality and mission success. A thorough failure analysis process includes reviewing error checklists for known safety or security vulnerabilities and leveraging tools like **Failure Modes and Effects Analysis (FMEA)** and **Fault Tree Analysis (FTA)** to pinpoint areas needing enhanced fault tolerance or design modifications.

For further guidance, refer to:

* **8.02** - Software Quality
* **8.04** - Additional Requirements Considerations for Use with Safety-Critical Software
* **8.05** - SW Failure Modes and Effects Analysis
* **8.07** - Software Fault Tree Analysis

---

### 4.1 Key Steps in a Software Failure Analysis

Failure analysis involves collaboration between system reliability experts, software engineers, and systems engineers to identify high-risk areas and implement changes to enhance fault tolerance.

* **Initial Failure Analysis**: Focuses on broad software functionality and the system’s ability to handle faults during early design phases.
* **Follow-Up Failure Analysis**: Concentrates on critical or weak areas of the design, ensuring that previously identified faults and concerns are addressed and do not reappear during later stages of development.

---

#### 4.1.1 **Top-Down Software Failure Analysis**

Top-down failure analysis examines the system from a high-level perspective, ensuring that software contributes to the system's ability to meet its operational requirements by appropriately managing faults. Software often supports the system's fault tolerance by detecting, isolating, logging, and enabling recovery from failures.

**Key Activities:**

* Develop or reference a **software functional criticality list** to prioritize fault management for critical functions.
* Monitor requirements, design, implementation, and testing activities to ensure that fault-critical components are rigorously assessed.
* Use tools like system models and fault tree analysis to evaluate software’s role in detecting and recovering from critical failures.

**Specific Objectives:**

* Confirm that system analyses include software’s contributions to failure management and ensure alignment with overall hardware and software reliability goals.
* Ensure that results from failure analysis are appropriately translated into actionable software requirements or design features.
* Validate that software categorized as **mission-critical** or **safety-critical** is equipped with robust requirements, fault management designs, and rigorous testing.
* Assess the potential impact of software changes, trade studies, and unresolved defects on system fault tolerance, and communicate findings to software and project management to guide decisions.

**Relevant Guidance:**

* **SWE-023** - Software Safety-Critical Requirements
* **SWE-051** - Software Requirements Analysis
* **5.09** - Software Requirements Specification (SRS)
* **8.01** - Off-Nominal Testing
* **8.17** - Software Safety Audit Checklists
* **8.20** - Safety-Specific Activities in Each Phase
* **8.58** - Software Safety and Hazard Analysis

---

#### 4.1.2 **Bottom-Up Software Failure Analysis**

Bottom-up failure analysis focuses on identifying and resolving potential failure points at the software specification, design, and implementation levels. This method ensures that lower-level issues are addressed before they can contribute to broader system failures.

**Key Activities:**

* Analyze critical software components to identify failure modes, using predefined lists of **generic software failure types** as a baseline.
* Review ongoing software failure analyses to ensure gaps are identified and resolved.
* Verify that mitigation steps, such as process improvements and design changes, are implemented to reduce the likelihood of reoccurring software failures.

---

### 4.2 Continuous Collaboration for Software Failure Analysis

Failure analysis is an iterative and collaborative effort that integrates system-level insights with software-level observations to ensure a complete fault management framework. By combining top-down and bottom-up approaches, teams can address faults comprehensively, ensuring that both system-wide and granular risks are effectively mitigated.

---

## 4.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

---

Failure analysis ensures that potential faults, whether system-level or software-specific, are identified and addressed early in the development process. Through the application of rigorous tools, systematic methodologies, and cross-functional collaboration, teams can design and deliver robust software that meets the highest standards of system integrity and mission safety.

# 5. Designing for Software Failure Management

Designing for software failure management requires embedding fault detection, isolation, and recovery mechanisms directly into the software and system architecture. While initial steps focus on identifying vulnerabilities or weak points, proactive design strategies are critical to managing known and anticipated failure scenarios. The **Failure Detection, Isolation, and Recovery (FDIR)** framework is a key methodology used in this process. FDIR equips systems with tools to monitor, detect, isolate, and address failures dynamically, ensuring that the system can operate safely even in the presence of faults.

---

### 5.1 Key Considerations for Software Failure Management

#### **5.1.1 Fault and Failure Management**

Failure management begins with identifying potential hardware and software faults, followed by designing mechanisms to mitigate their effects. The system should include:

* **Fault monitoring mechanisms**: Ensure the system can detect recoverable failures without disruption.
* **Adaptive monitoring levels**: Tailor monitoring depth based on the system’s operational state and available recovery options.
* **Prioritized recovery actions**: Define actions such as isolating faults, rebooting processes, or tolerating partial failures for non-critical functions.

---

#### **5.1.2 FDIR Design Challenges**

FDIR design is a critical aspect of managing failures because it directly impacts system resilience and overall cost-effectiveness. Key challenges include:

* **Customized FDIR processes**: Avoid generic designs that fail to fit specific project needs; instead, tailor fault monitoring and responses for particular risks (e.g., memory corruption, missed communications, sensor failures).
* **Integration with hardware systems**: Collaborate with hardware engineers to optimize sensor configurations, implement appropriate voting schemes, and manage fault detection/recovery timings.
* **Complex response systems**: Consider advanced algorithms that interpret multifaceted fault indicators and provide nuanced response options to prevent cascading failures.

---

#### **5.1.3 Isolation and Recovery**

Isolation and recovery designs ensure that faults do not propagate across the system and that failures can be managed effectively. Key strategies include:

* **Failure isolation**: Identify where faults occur, enabling quicker and more precise recovery.
* **Recovery mechanisms**: Implement robust corrective actions, such as:
  + Switching to redundant systems.
  + Resetting software processes through reboots.
  + Logging non-critical errors to prevent interruptions while informing future maintenance.

---

#### **5.1.4 Robust Design Features**

Key features for failure management in software include:

* **Data integrity checks**: Ensure all communications undergo validation (e.g., checksums, CRC).
* **Input validation**: Prevent faults by validating input parameters for size, type, and range.
* **Memory safeguards**: Use techniques to detect and prevent memory corruption or leaks.
* **Timeout mechanisms**: Employ watchdog timers to ensure processes do not stall indefinitely.

For a detailed list of fault mitigation strategies, refer to **Appendix D** of **NASA-STD-8739.8**.

---

### 5.2 Role of Software Assurance (SA) in Software Failure Management

Software Assurance (SA) plays a key role in integrating failure analysis results into system design and verifying effectiveness.

* **Integration of Analysis Results**: Ensure that findings from failure analyses (e.g., FMEA, FTA) are accurately incorporated as software requirements or design updates.
* **Verification of Controls**: Test and validate fault detection, isolation, and recovery mechanisms, ensuring they respond appropriately under simulated fault conditions.

---

Designing for failure management enables systems to function reliably under adverse scenarios while providing robust mechanisms for fault detection, isolation, and recovery. Collaborative design practices paired with thorough testing ensure that software is resilient, adaptable, and mission-ready.

## 5.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 6. Resources

## 6.1 Resources

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 6.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 6.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 6.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>6</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design)      * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements)      * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration)      * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety)      * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 6.5 Associated Activities

This topic is associated with the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |
