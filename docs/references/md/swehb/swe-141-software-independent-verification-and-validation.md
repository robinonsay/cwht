# SWE-141 - Software Independent Verification and Validation

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695499. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation

SWE-141 - Software Independent Verification and Validation

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695499)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695499&showCommentArea=true&showComments=true#addcomment)

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

3.6.2 For projects reaching Key Decision Point A, the program manager shall ensure that software IV&V is performed on the following categories of projects: 

a. Category 1 projects as defined in NPR 7120.5.  
b. Category 2 projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4, Risk Classification for NASA Payloads.  
c. Projects selected explicitly by the Mission Directorate Associate Administrator (MDAA) to have software IV&V.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-141 History

SWE-141 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | New |
| B | 3.6.2 For projects reaching KDP (Key Decision Point)  A after the effective date of this directive’s revision, the program manager shall ensure that software IV&V (Independent Verification and Validation) is performed on the following categories of projects:   1. 1. Category 1 Projects as defined in NPR 7120.5.    2. Category 2 Projects as defined in NPR 7120.5 that have Class A or Class B payload risk classification per NPR 8705.4.    3. Projects specifically selected by the NASA CSMA to have software IV&V. |
| Difference between B and C | Removed KDP acronym;  removed the caveat "after the effective date of this directive's revision"; In item c, removed "specifically" and added "explicitly",;  Spelled out the "CSMA" acronym by removing and replacing with "Chief of the Office of Safety and Mission Assurance". |
| C | 3.6.2 For projects reaching Key Decision Point A the program manager shall ensure that software IV&V is performed on the following categories of projects:   1. 1. Category 1 projects as defined in NPR 7120.5.    2. Category 2 projects as defined in NPR 7120.5 that have Class A or Class B payload risk classification per NPR 8705.4.    3. Projects selected explicitly by the NASA Chief of the Office of Safety and Mission Assurance to have software IV&V. |
| Difference between C and D | Item c. was updated to show change to MDAA for selection. |
| D | 3.6.2 For projects reaching Key Decision Point A, the program manager shall ensure that software IV&V is performed on the following categories of projects:   a. Category 1 projects as defined in NPR 7120.5. b. Category 2 projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4, Risk Classification for NASA Payloads. c. Projects selected explicitly by the Mission Directorate Associate Administrator (MDAA) to have software IV&V. |

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
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |

# 2. Rationale

Independent Verification and Validation (IV&V) is a specialized discipline within software assurance that leverages rigorous and systematic analysis, inspection, and testing methodologies to evaluate software products and processes. The primary objective of IV&V is to provide an autonomous, evidence-based assessment to ensure that software systems fulfill their intended functionality and satisfy mission objectives in a reliable, safe, and dependable manner. By conducting IV&V activities throughout the software development life cycle (from requirements through design, implementation, testing, deployment, and maintenance), critical issues can be identified and analyzed early, minimizing risks to project success.

IV&V evaluates both nominal operations—ensuring that the software meets functional, performance, safety, and dependability requirements under expected conditions—and off-nominal conditions, such as the software's behaviors in the presence of faults, hazardous situations, or other anomalous events. This comprehensive assessment provides insights into whether the software is robust enough to handle mission-critical scenarios and helps mitigate risks associated with technical, safety, or performance failures.

The ultimate goal of IV&V is to generate independent assurance conclusions that are informed by objective evidence found in key software development artifacts, project-specific risks, and the software's intended behavior. These conclusions and insights are communicated to the project team and stakeholders, facilitating data-driven decision-making and risk management. Through its independent and rigorous approach, IV&V contributes to the success of projects by enhancing confidence in the quality, safety, and mission readiness of software systems.

This requirement ensures **Independent Verification and Validation (IV&V)** is applied systematically to software development efforts on high-priority, high-risk projects to mitigate software-related risks and ensure mission success. Software is a critical and increasingly complex component of NASA’s projects, and software failures have the potential to jeopardize entire missions. By requiring IV&V for these specific categories of projects, NASA ensures a standardized process of independent assessment that reduces risk, promotes safety and reliability, and validates the delivery of mission-critical capabilities.

Key Takeaways of This Requirement:

* **Category 1 Projects:** High-visibility, high-complexity missions with the greatest stakes for NASA’s success require IV&V to align software with mission-critical needs.
* **Category 2 Projects with Class A/B Payloads:** High-priority science or exploration missions benefit from IV&V analysis to address the complexities and risks of their payloads and operational environments.
* **MDAA Selections:** Allows program managers to address project-specific risks or high-priority objectives not captured by standard classifications.

This requirement represents a proactive strategy to ensure mission success by addressing software-related risks early, leveraging independent oversight, and prioritizing NASA’s most critical and high-profile projects. The use of IV&V bolsters confidence that software systems are robust, reliable, and ready to meet the demands of NASA’s high-stakes missions.

# Why This Requirement Is Necessary

## 2.1 Software Complexity and Criticality

NASA missions increasingly rely on complex software systems that control spacecraft, instruments, and mission operations. These systems must operate flawlessly in unpredictable and often hostile environments. Errors in software, even small ones, can result in catastrophic mission failures, particularly for safety-critical and mission-critical systems.

* **Category 1 Projects (NPR 7120.5):** These projects are typically **flagship missions** with the highest national or international visibility, significance, and complexity. Examples include human spaceflight missions (e.g., Artemis), flagship astrophysics missions (e.g., James Webb Space Telescope), and Mars exploration. Failures in such projects risk significant funding losses, scientific setbacks, and reputational harm.
* **Category 2 Projects with Class A or Class B Payloads:** These projects include high-priority science missions or exploration efforts (e.g., Mars rovers, planetary probes, or Earth observation satellites). Class A and B payloads represent **critical assets** requiring high levels of assurance, as their failure has broad implications for mission objectives and scientific outcomes.

**Why This Matters:**

* Software systems in such projects often have unique, complex designs, making them more prone to undetected errors.
* Earlier mission failures, such as the **Mars Climate Orbiter** (1999), largely resulted from software-related issues and a lack of comprehensive independent validation.
* Requiring IV&V ensures an unbiased, meticulous review of software at all lifecycle stages, reducing the risk of undetected discrepancies that might threaten mission success.

## 2.2 Addressing Risk at Key Decision Point (KDP) A

KDP A is when preliminary project baselines are established, and project feasibility is assessed for continued funding and development. At this critical point, it's essential to identify and address risks early, particularly for high-priority or high-risk software systems.

**Why Early IV&V Matters:**

* Software deficiencies become increasingly costly and time-consuming to fix if caught late in development.
* IV&V at KDP A assesses how well software plans and processes address mission needs and constraints, ensuring that:
  + Requirements are complete, feasible, and testable.
  + High-risk areas (e.g., interfaces, safety-critical systems) are adequately defined and resourced.
  + Effective mitigation strategies are in place for critical risks.

Early intervention by IV&V ensures that significant errors or omissions in planning, design, or implementation are identified and addressed before they can impact later project phases.

## 2.3 Independent Assessment is Essential for High-Risk Systems

Safety-critical and mission-critical systems, such as those controlling human spaceflight or autonomous spacecraft landing, require an extra level of scrutiny. These systems face low tolerance for failure due to their high stakes, making an **independent check** of software design and implementation critical.

* **Independence in IV&V:**  
  Allows unbiased assessments of software, free from development pressures. IV&V analysts:
  + Examine requirements validity, correctness, and traceability independently.
  + Validate that safety measures are correctly implemented.
  + Confirm system behavior will meet mission goals for both nominal and off-nominal scenarios.

**Why Independence is Necessary:**

* Developers may have conflicts of interest or unintentional biases in assessing their own work.
* Independent reviewers (IV&V) provide an objective perspective, often identifying risks or issues overlooked by development teams.
* Independence ensures robust validation against safety and mission-critical requirements.

## 2.4 Risk Management Specific to Class A and Class B Payloads

Projects with **Class A or Class B payloads** per NPR 8705.4 inherently involve higher mission risks due to their priority, complexity, or operational environments. Class A payloads are life-critical missions, where failure leads to unacceptable outcomes (e.g., human safety risks or the loss of flagship missions). Class B payloads remain high-priority, requiring stringent measures to ensure long-term mission success.

**Why IV&V Is Important for Class A and Class B Payloads:**

* These payloads directly impact human life, high-value resources, or globally significant science.
* Safety-critical software used in launch, navigation, hazard avoidance, or fail-safe systems must work precisely as intended—failure is not an option.
* IV&V activities verify and validate:
  + Functional compliance with mission-critical requirements.
  + Hazard controls and proper mitigation of failure scenarios.
  + Integration of hardware-software systems to avoid unexpected interactions or unintended outcomes.

## 2.5 Flexibility for Mission Directorate Associate Administrator (MDAA) Selection

Some projects may not fit into the strict definitions of Category 1 or Category 2 with Class A/B payloads but may still carry **unique risks** or **strategic importance**. The MDAA's ability to explicitly select these projects for IV&V provides flexibility to address specific circumstances.

Examples include:

* Highly innovative missions with uncharacterized risks (e.g., use of new software architectures or experimental designs).
* Small missions with limited resources but a disproportionately high national or scientific profile.
* Collaborative missions involving international agencies or commercial partners, where independent assessments provide additional quality assurance.

**Why MDAA Selection is Valuable:**

* Allows for expert judgment to address evolving risks or emerging priorities not captured in standard classification schemes.
* Helps ensure IV&V is applied judiciously and strategically to projects where it provides the greatest benefit.

## 2.6 Broader Objectives of IV&V Under This Requirement

This requirement directly supports NASA’s overarching goals for **mission assurance**, **safety**, and **scientific excellence**:

1. **Risk Reduction:** IV&V provides an added layer of oversight for software systems in high-risk or high-value projects, systematically identifying defects early and preventing costly errors that could jeopardize missions.
2. **Mission and Science Success:** Given the outcomes at stake, particularly for Category 1 projects and Class A/B payloads, IV&V ensures software supports overall mission goals and minimizes the risks of science return loss.
3. **Safety Assurance:** IV&V activities verify the correct implementation of safety-critical software, ensuring hazard controls work as intended and preventing catastrophic consequences in human spaceflight or high-priority payloads.
4. **Accountability:** Independent IV&V adds a layer of accountability and transparency to the software development lifecycle, promoting adherence to NASA standards and best practices.

# 3. Guidance

Independent Verification and Validation (IV&V) is an integral part of NASA's software assurance program, designed to ensure the development of safety-critical, high-quality software that meets mission and operational requirements. To maximize the effectiveness of IV&V, its involvement should occur as early as possible in the software development life cycle (SDLC). This guidance provides a structured approach for initiating and executing IV&V activities and highlights the principles, scope, processes, selection criteria, and operational framework for software IV&V within NASA programs and projects.

## 3.1 IV&V Timing and Project Lifecycle

* If a project does not explicitly have a Key Decision Point A (KDP A) milestone, IV&V activities should commence no later than the System Requirements Review (SRR) milestone or its equivalent within the project lifecycle.
* Engaging IV&V early (e.g., prior to or by SRR) enables the IV&V team to develop an independent understanding of the system, identify risks, and address potential issues at a time when corrective actions are more cost-effective and less disruptive. Early feedback to project stakeholders supports informed decision-making and risk mitigation regarding system correctness, safety, and dependability.

## 3.2 The Role of IV&V in the NASA Risk Mitigation Strategy

* **Objective:** The primary objective of IV&V is to provide independent and evidence-based evaluations of mission-critical software to ensure that:

  + The "right" system is being built to meet stakeholder needs.
  + The system and software are being built "correctly" in adherence to functional, safety, and reliability requirements.
  + The system responds appropriately under both nominal and off-nominal conditions.
* **Key Questions Answered by IV&V:**

  + Will the system's software perform as intended?
  + Will the system's software avoid unintended behaviors?
  + Will the system’s software function reliably under adverse conditions (e.g., hardware faults, hazardous scenarios)?
* **Value of IV&V:**

  + Higher software quality.
  + Improved confidence in mission-critical operations.
  + Reduced overall project risk.
  + Enhanced decision-making through independent insights.
  + Support for knowledge transfer and the implementation of best practices in system engineering.

## 3.3 Selection Criteria and Tailoring

### 3.3.1 Projects Requiring IV&V

The following categories of projects require IV&V as part of NASA’s software assurance strategy:

* **Category 1 Projects:** Defined in NPR 7120.5E as:

  + Human spaceflight projects.
  + Projects with a life cycle cost exceeding $1 billion.
  + Projects with significant radioactive content or other high-risk factors.
* **Category 2 Projects:**

  + Projects with a life cycle cost > $250M but ≤ $1B.
  + Projects with a life cycle cost ≤ $250M that are classified as high-priority due to mission significance, the involvement of new or unproven technologies, or international collaboration.
  + Must also involve a Class A or Class B payload risk.
* **Projects Designated by the MDAA:**

  + By the discretion of the Mission Directorate, certain projects may be explicitly assigned software IV&V.

### 3.3.2 Class A and Class B Payloads

Per NPR 8705.4, the criticality of a payload’s risk classification is a key determinant for IV&V:

* **Class A Payloads:** Feature the highest priority, complexity, and national significance with minimal risk tolerance.
* **Class B Payloads:** Are medium to high in cost/complexity and have low-risk tolerance, though slightly less stringent than Class A.

### 3.3.3 Waivers and Resource Constraints

* Projects meeting these criteria but not selected for NASA-funded IV&V due to resource limitations must either:
  + Independently fund the required IV&V services, or
  + Request and obtain a formal waiver through the tailoring process (see SWE-126 and SWE-223 in the NASA Software Engineering Handbook).

## 3.4. Principles of Independence in IV&V

To maintain the objectivity and credibility of IV&V efforts, three key dimensions of independence must be ensured:

1. **Technical Independence:**

   * IV&V personnel must not be involved in the development of the software/system being evaluated.
   * Independent technical assessments bring a new perspective, helping identify subtle errors missed by development teams.
2. **Managerial Independence:**

   * The IV&V provider must operate under a separate chain of command from the development organization.
   * The IV&V team determines its analysis scope, methods, and schedules independently.
3. **Financial Independence:**

   * The IV&V budget must be controlled and managed separately from the development organization to avoid financial pressures or conflicts of interest.

## 3.5 The IV&V Process

### 3.5.1 Early Involvement

* **Why Start Early:** Engaging IV&V early in the SDLC provides sufficient time to:
  + Analyze project artifacts (e.g., concepts, requirements, designs).
  + Identify potential issues before they propagate to later development stages, reducing costs and risks effectively.

### 3.5.2 Key Activities

The two primary activities performed during IV&V are:

1. **Verification:** Ensures that the software conforms to specified requirements, design standards, and applicable regulations.
2. **Validation:** Confirms that the system/software fulfills its intended purpose and addresses stakeholder needs correctly.

## 3.6 Leadership and Governance

* **NASA IV&V Facility:** It is NASA’s policy that the NASA IV&V Facility serve as the sole provider of IV&V services unless an alternative provider is approved. This ensures consistency in IV&V execution and adherence to NASA standards.
* **IV&V Advisory Board:**
  + Reviews the annual scope of NASA IV&V operations and advocates for appropriate resource allocations.
  + Provides recommendations to the Chief of Safety and Mission Assurance for adjudicating exceptions, waivers, and other IV&V-related policy matters.

## 3.7 Additional Considerations

* The **IV&V Project Execution Plan (IPEP)** outlines the tailored IV&V strategy for each project, including cost-benefit trade-offs, prioritized project risks, and assurance strategies.
* Continuous evaluation of risks throughout the development lifecycle ensures a balanced level of "appropriate assurance" is maintained, even under tight resource constraints.

## 3.8 Strategic Alignment

* This guidance is consistent with the 2012 Aerospace Safety Advisory Panel recommendation to establish a standard for the criticality thresholds requiring IV&V. It reaffirms NASA’s commitment to robust software assurance processes and the development of high-confidence mission software.

**If a project does not have a KDP A milestone then IV&V should be started by the System Requirement Review (SRR) milestone (or the project's *equivalence* to an SRR point in the project lifecycle).**

The IV&V process should start early in the software development life cycle, providing feedback to the IV&V provider organization, and allowing the IV&V team to modify products at optimal timeframes and in a timely fashion, thereby reducing overall project risk. The feedback also answers project stakeholders’ questions about system properties (correctness, robustness, safety, security, etc.) to make informed decisions with respect to the development and acceptance of the system and its software.

Projects meeting the criteria in this requirement that are not chosen for NASA IV&V Program services due to funding limitations are expected to either independently fund the IV&V services or obtain a waiver (see [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations)).

See also [SWE-223 - Tailoring IV&V project selections](/spaces/SWEHBVD/pages/105710152/SWE-223+-+Tailoring+IV+V+project+selections),

Additional guidance related to IV&V may be found in requirement [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) in this Handbook.

**The software IV&V analysis must be performed by an organization that is financially, managerially, and technically independent and cannot be part of a company associated with the development organization.  There must be no actual or perceived conflict of interest between the developer/system integrator and the IV&V agent.**

## 3.9 IV&V Requirements

**Objective of IV&V**  
Software Independent Verification and Validation (IV&V) is a risk-based activity aimed at identifying and mitigating software risks to ensure software correctness, safety, reliability, and security throughout the software development life cycle (SDLC). IV&V provides independent assurance that critical software will meet mission and stakeholder requirements under both nominal and off-nominal conditions.

### 3.9.1 General IV&V Scope and Purpose

* IV&V efforts apply to all software development projects and are tailored via the **IV&V Project Execution Plan (IPEP)**.
* IV&V activities focus on analyzing, verifying, and validating in-scope system/software behaviors and components identified as critical by risk assessments.
* As a risk mitigation activity, IV&V prioritizes analysis based on a project's developmental and operational software risks, examining areas with the highest impact on safety and mission success.

### 3.9.2 IV&V Planning and Risk Assessment

* The **IV&V Provider**:
  + Conducts ongoing risk assessments to determine which software behaviors/components require analysis.
  + Develops and negotiates the **IPEP** with the project to outline tailored IV&V activities, methods, and rigor to address identified risks.
  + Updates the IPEP as the project evolves.

### 3.9.3 Key Responsibilities of the IV&V Provider

#### a. **Planning and Integration**

* Collaborates with project teams to integrate IV&V activities within the safety and software assurance strategy.
* Participates in project milestone reviews and technical interchange meetings to:
  + Provide real-time feedback.
  + Report the results of IV&V activities, including risks and defects.

#### b. **Systematic Analysis of Software Artifacts**

The IV&V Provider verifies and validates key software development artifacts at each stage of the SDLC, ensuring they are **correct**, **complete**, **consistent**, **traceable**, and **testable.** This includes:

* **System Requirements:** Validation against mission objectives and operational scenarios.
* **Software Requirements:** Ensuring correctness, safety, fault tolerance, and mitigation of security risks.
* **Software and System Architecture:** Validating structural integrity, dependability, and alignment between requirements and architectural design.
* **Detailed Design:** Verification of traceability to software requirements and internal component consistency.
* **Source Code:** Verification of code correctness, adherence to industry best practices, mitigation of security vulnerabilities (e.g., buffer overflows), and consistency with requirements.
* **Testing Artifacts and Processes:**
  + Ensures correctness and completeness of test plans, test cases, procedures, and test designs, including allocation of system/software test functions.
  + Verifies that test results meet acceptance criteria for both **nominal** and **off-nominal** conditions.
* **Interfaces:** Verifies validity and consistency of interfaces at all levels (hardware-software, software-software).

#### c. **Risk Identification and Communication**

* Tracks and analyzes changes in software or project scope to evaluate potential risks or impacts.
* Identifies and reports risks (e.g., security risks, life cycle risks) to project stakeholders in alignment with NPR 8000.4.

#### d. **Defects and Continuous Improvement**

* Tracks, records, and communicates all identified defects and ensures that they are addressed by the project.
* Participates in peer reviews and software inspections to detect issues and provide insights.
* Assesses testing for all requirements, including boundary conditions and unexpected scenarios.
* Periodically gathers and analyzes metrics to improve IV&V processes and monitor project/software risks.

#### e. **Operational Assessments**

* During the operational or maintenance phase:
  + Evaluates risks associated with software updates.
  + Assesses ripple effects caused by software changes to prevent emergent, unintended behaviors.

### 3.9.4 Independence of IV&V

To ensure objectivity, IV&V requires **technical independence**, **managerial independence**, and **financial independence** from the development organization:

* The IV&V team must operate independently and report its findings to project management, engineering, and software assurance teams without undue influence.

### 3.9.5 Focus Areas and Deliverables

* IV&V prioritizes the following areas:
  + Safety-critical and mission-critical areas within the software.
  + Known security risks or vulnerabilities and their mitigations.
  + Software reused from prior projects (e.g., heritage or legacy software).
  + Interfaces, fault tolerance, and dependability requirements.
* Deliverables include output reports:
  + Analysis of in-scope artifacts according to the IPEP.
  + Metrics, identified risks, and assurance statements for project stakeholders to drive risk-informed decisions.

### 3.9.6 Key Verification and Validation Tasks

* Ensure alignment between requirements, architecture, detailed design, and code.
* Validate system and software behavior under both nominal and failure scenarios.
* Ensure proper implementation of security objectives, hazard controls, and mitigations.
* Validate software's interfaces with hardware, other software, and external systems.
* Verify that open-source and reused software components meet project requirements and security considerations.

### 3.9.7 Testing Oversight and Code Analysis

* IV&V evaluates all associated test plans, procedures, cases, and environments for adequacy.
* Tests should ultimately demonstrate verification of all requirements for both normal and edge-case scenarios.
* Source code analysis tools (static, dynamic, composition tools, etc.) are used to validate code quality, traceability, and risk mitigations.

### 3.9.8 Security and Risk

* IV&V tracks known risks, emerging threats, and security vulnerabilities across the lifecycle.
* Ensures that security mitigations are implemented, validated, and effective in safeguarding software-defined system functions.
* Provides analysis of the project's responsiveness to risks (e.g., security, reliability, and operational hazards).

### 3.9.9 Long-Term Impact and Iterative Feedback

* IV&V analysis is continuously adjusted based on evolving project scopes, risks, and findings.
* Actively collaborates on resolving detected issues promptly to reduce the costs of post-baselining changes.
* Provides feedback that supports informed decision-making and reduces mission risks throughout the software lifecycle.

By adhering to these requirements, IV&V plays a critical role in ensuring the safety, security, reliability, and success of NASA's mission-critical software systems.

The IV&V requirements are analyzed and partitioned according to the type of artifact. The requirements do not imply or require the use of any specific life cycle model. It is also important to understand that IV&V applies to any life cycle development process. The IV&V requirements document the potential scope of analysis performed by the IV&V Provider and the key responsibility of the software project to provide the information needed to perform that analysis. Additionally, scoping the IV&V analysis is according to the application of the risk assessment to determine the prioritization of activities and the level of rigor associated with performing those activities.

Software IV&V are listed below:

* The IV&V requirements apply to all IV&V efforts performed on a software development project, as tailored by the IV&V Project Execution Plan. The IV&V requirements also serve as the definition of what NASA considers IV&V. IV&V is a risk mitigation activity, and as such, the application of IV&V analysis and the rigor of that analysis is driven by the IV&V Provider’s assessment of software risk.
* The IV&V Provider shall conduct planning and risk assessments to determine the specific system/software behaviors (including the software components responsible for implementing the behaviors) to be analyzed.
* The IV&V Provider shall develop and negotiate with the project an IV&V IPEP.
* The NASA SMA Technical Authority (TA) shall review and concur with the IPEP.
* The IV&V Provider shall provide analysis results, risks, assurance statements, and data to the responsible organizations’ project management, engineering, and software assurance personnel.
  + While independent, the IV&V Provider is still a part of a project's overall safety and risk mitigation software assurance strategy. The results of IV&V analysis need to be incorporated into the overall software assurance assessment of the project and provided to the project management. IV&V Provider should support project milestone reviews and provide the project with an evaluation of the life cycle review artifacts to assist development management decisions on whether the review criteria have been met and how to proceed going forward.
* The IV&V Provider shall participate in project reviews of software activities. Participation includes providing status and results of software IV&V activities including, but not limited to, upcoming analysis activities, artifacts needed from the project, the results of the current or completed analysis, defects, and risks to stakeholders, customers, and development project personnel.
  + The most significant positive impact of IV&V analysis is when the analysis results are in phase with the development effort. Communicating defects after development artifacts are baselined increases the cost of making the changes. Additionally, the inclusion of the IV&V Provider in ongoing technical meetings keeps the IV&V Provider informed of possible changes that may affect future IV&V tasking. Supporting the ongoing technical meetings allows the IV&V Provider an opportunity to provide real-time feedback on these changes.
  + The IV&V Provider shall provide the responsible organizations’ project management, engineering, and software assurance personnel shall insight into the software IV&V and IV&V test activities. At a minimum, the IV&V Provider will be required to allow the responsible organizations’ project management, engineering, and software assurance personnel to:
* The IPEP documents the activities, methods, level of rigor, environments, tailoring (if any) of the IV&V requirements, and criteria to be used in performing verification and validation of in-scope system/software behaviors (including responsible software components) determined by the planning and scoping effort. A Provider should use a documented analysis approach to track and manage the IV&V effort aligned with ongoing development project efforts. The IPEP documents which software products are subject to which analyses and analysis requirements are wholly, partially, or not applied following the risk assessment and resource constraints. The IPEP also serves as a communication tool between the project and IV&V to set expectations for the IV&V products produced throughout the life cycle. The IPEP may require updating throughout the life cycle.
* IV&V is a focused activity that prioritizes IV&V analysis to address the highest developmental and operational software risks. IV&V priority is based on the combination of the potential for software impacts on safety and mission success and the probability factors for latent defects. IV&V analysis activities provide coverage with a degree of rigor that reflects the priority level. The initial planning and scoping effort based on the risk assessment define the starting point for the IV&V analysis. Throughout each IV&V project, continuous and iterative feedback, through the execution of analysis, identification of issues and risks, and the collection of deeper mission understanding, allows IV&V projects to “Follow The Risk” and adjust plans. The planning and scoping effort also aid in establishing the initial relationships between the IV&V Provider, the Acquirer, and the Provider.
  + Monitor the IV&V activities and plans.
  + Review the verification activities to ensure adequacy.
  + Review IV&V studies and source data.
  + Audit the software IV&V processes and practices.
  + Participate in IV&V software reviews and technical interchange meetings

* The IV&V Provider shall participate in planned software peer reviews or software inspections guided by the planning and scoping risk analysis documented in the IV&V Project Execution Plan and NASA-HDBK-2203.
* The IV&V Provider should be involved in the review/inspection process for all system/software items within the scope of their analysis.
* The IV&V Provider shall establish, record, maintain, report, and utilize IV&V management and technical measurements.
  + Note: The IV&V Provider gathers and analyzes metrics periodically to perform continuous improvement of IV&V processes and identify indicators of IV&V and project risks.
* The IV&V Provider shall assess and track software activities' actual results and performance against the software plans and identify and report any risks or findings to the responsible organizations’ project management, engineering, and software assurance personnel.
* The IV&V Provider shall track and evaluate changes to software products to evaluate for possible changes in the IV&V Provider’s risk analysis and potential adverse impacts to the software system and the development effort.
* The IV&V Provider shall assess the software development life cycle for suitability for the problem to be solved and identify and communicate any risks associated with the chosen life cycle to the responsible organizations’ project management, engineering, and software assurance personnel.
* The IV&V Provider shall identify, analyze, track, communicate, and record risks to the software and development project by NPR 8000.4, Agency Risk Management Procedural Requirements to the responsible organizations’ project management, engineering, and software assurance personnel.
* The IV&V Provider shall verify the project implements the requirements for the software listed in NPR 7150.2 and communicate any risks to the responsible organizations’ project management, engineering, and software assurance personnel.
* The IV&V Provider shall track, record, and communicate defects/issues and other results found during the execution of IV&V analysis and independent IV&V testing to the responsible organizations’ project management, engineering, and software assurance personnel.
* The IV&V Provider shall ensure that the identified defects and issues are addressed by the project.
* The IV&V Provider shall ensure that the software planned for reuse meets the fit, form, and function as a component within the new application.
* The IV&V Provider shall ensure that the system architecture contains computing-related items (subsystems, components, etc.) to fulfill the system's mission and satisfy user needs and operational scenarios or use cases.
* The IV&V Provider shall ensure that a basis for the engineering and planning of computing-related functions is the operations, mission objectives (including mission retirement), and the system.
* The IV&V Provider shall ensure that feasibility and trade studies provide the results to confidently support the critical decisions that drove the need for the study.
* The IV&V Provider shall ensure that known software-based hazard causes, contributors, and controls are identified, documented, and traced to the project requirements.
* The IV&V Provider shall ensure that known security threats and risks are identified, appropriately documented, and updated throughout the mission life cycle and communicated to the responsible organizations’ project management, engineering, and software assurance personnel.
* The IV&V Provider shall verify and validate that the in-scope software requirements and system requirements are, at a minimum, correct, consistent, complete, accurate, readable, traceable, and testable.
  + The software usually provides the interface between the user and the system hardware and the interface between system hardware components and other systems. These interfaces are critical to the successful operation and use of the system.
* The IV&V Provider shall verify and validate that the mitigations for identified security risks are in the software requirements.
  + Security is an essential aspect of any system development effort. In most systems, the software provides the primary user interface. The user interface is an element of the system that can provide undesired access. A system concept design should address known security risks through various features in the system.
* The IV&V Provider shall ensure that software requirements meet the dependability and fault tolerance required by the system.
* The IV&V Provider shall verify and validate that the relationship between the in-scope system/software requirements and the associated architectural elements is traceable correct, consistent, and complete.
  + Architectural elements are responsible for implementing specific behaviors within the software and the overall system. The interactions between these architectural elements result in the realization of the desired behaviors as well as possible undesired behaviors.
* The IV&V Provider shall verify and validate that the software architecture meets the user’s safety and mission-critical needs as defined in the requirements.
  + The architecture provides the foundation for the development of the software. It also significantly impacts how the software deals with faults and failures and how the software interfaces with the user and system components. Analysis of the architecture provides early insight into how the software is structured and how that structure can implement the requirements.
* The IV&V Provider shall verify and validate that the detailed design products are traceable, consistent, complete, accurate, and testable.
  + Detailed design is the implementation of algorithms that control and monitor the different parts of the system and allow for interaction between the system and the user and other systems. The detailed design defines how the architectural components behave to support the interactions defined in the architecture. Analysis of the detailed design includes looking at the low-level software components in the software system.
* The IV&V Provider shall verify and validate that the interfaces between the detailed design components and the hardware, users, operators, other software, and external systems are correct, consistent, complete, accurate, and testable.
  + While architecture defines the interactions between the architectural elements, each element is generally composed of lower-level components defined by the detailed design. The interfaces between these components are important in ensuring that the architectural element meets its assigned responsibilities.
* The IV&V Provider shall verify and validate that the relationship between the software requirements and the associated detailed design components is correct, consistent, and complete.
  + The detailed design components capture the approach to implementing the software requirements, including the requirements associated with fault management, security, and safety. Analysis of the relationship between the detailed design and the software requirements provides evidence that all requirements are in the detailed design.
* The IV&V Provider shall verify and validate that the software code products are consistent with architecture, complete concerning requirements, and testable.
* The IV&V Provider shall verify and validate that the software code meets the industry's best practices and software coding standards.
* The IV&V Provider shall verify and validate that the security risks in the software code are identified and mitigated.

* *Note: This includes software developed by NASA, software developed for NASA, software maintained by or for NASA, COTS, GOTS, MOTS, OSS, reused software components, auto-generated code, embedded software, the software executed on processors embedded in programmable logic devices, legacy, heritage, applications, freeware, shareware, trial or demonstration software, and open-source software components. See also Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code).*
* The IV&V Provider shall verify and validate the appropriate use of off-the-shelf software, including ensuring that the project has identified all open-source software used and that the security risks are identified and mitigated by the use of the open-source software.
* The IV&V Provider shall verify and validate that the project assesses the software systems for possible security vulnerabilities and weaknesses.
* The IV&V Provider shall verify and validate that the project implements the required software security risk mitigations to ensure that security objectives for software are satisfied.
* The IV&V Provider shall verify and validate the source code through analysis tools (including but not limited to static, dynamic, composition, and formal analysis tools).
  + The use of analysis tools may include the verification and validation of the analysis tools used by the development project in the process of developing the software. The results may be from static code analysis, software composition analysis, dynamic code analysis, cyclomatic complexity, or other code quality analysis tools.
* The IV&V Provider shall verify and validate that the relationship between the software design elements and the associated software units is correct, consistent, and complete.
* The IV&V Provider shall verify and validate that the relationship between software code components and corresponding requirements is correct, complete, and consistent.
  + For all of the implementation requirements, it is with code that the development of software reaches its lowest level of abstraction and that the software capabilities are implemented. Evaluating the relationship between the source code and the design components and requirements provides evidence that only the specified requirements and components are in the system. Evaluating the relationship between the source code and the design components and requirements helps minimize one aspect of the emergence of unexpected behaviors: the inclusion of behaviors not specified in the requirements. The overall analysis of the code is essential in assuring that the code implements the required software behaviors. From a safety perspective, it is important to evaluate the code and ensure that known software safety and security issues such as buffer overflows and type mismatches, among many others, are not used in safety-critical aspects of the software.
* The IV&V Provider shall verify and validate that test plans, test procedures, test cases, test environment (including simulations), and test design at all levels of testing (unit, integration, system, acceptance, etc.) are correct, complete, and consistent for verification and validation of the source code and system functions allocated to the software.
* The IV&V Provider shall verify and validate that the relationships between the test plans, test procedures, test cases, test design, source code, and system functions allocated to the software are correct, complete, and consistent.
* The IV&V Provider shall verify that the test plans, test cases, test design, and test procedures contain objective acceptance criteria that support the verification of the associated requirements for both nominal and off-nominal conditions.
* The IV&V Provider shall verify that the software test results meet the associated acceptance criteria to ensure that the software correctly implements the associated requirements.
* The IV&V Provider assesses the testing artifacts within the system’s meaning concerning the desired capabilities and expected operational system environment. The assessment includes an examination of testing at system boundary conditions to include unexpected conditions. The testing analysis assures that the project tests all requirements and that the system does what the requirements state it should do. The testing analysis also includes an analysis of the traceability information between the tests and the requirements.
* The IV&V Provider shall verify that the project tests the required software security risk mitigations to ensure that the security objectives for the software are satisfied.
* The IV&V Provider shall assess the software maintenance and operational risks concerning software elements to support the planning of IV&V activities during the maintenance phase.
  + The approach to software development on some projects results in different parts of the software going into operation at different times in the overall project life cycle. For example, a lander mission to Mars may complete the software needed for the cruise phase to Mars while continuing to work on the entry, descent, landing, and surface operations software. Some software may also have an extended lifetime such that operational updates are anytime during the operational use of the software.
  + In some cases, software anomalies cause changes to the software. IV&V is important because software changes can often have ripple effects throughout the system and cause emergent behaviors. The IV&V analysis provides insight into these possible effects and provides an overall assessment of the impact of the change.

## 3.10 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks) * [SWE-223 - Tailoring IV&V project selections](/spaces/SWEHBVD/pages/105710152/SWE-223+-+Tailoring+IV+V+project+selections)       * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

See also Topic [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis).

## 3.11 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Software Quality Assurance](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Software+Quality+Assurance) |

# 4. Small Projects

Small projects generally have lower budgets, shorter timelines, and fewer resources, but they may still require software IV&V if they fall under the categories outlined in this requirement. The following guidance is designed to help small projects efficiently and effectively incorporate the mandated IV&V activities without excessive impact on resources or schedules.

For small projects, implementing software IV&V per Requirement 3.6.2 may be streamlined while still ensuring compliance, safety, and quality. By focusing on critical functionalities, leveraging NASA Program resources, tailoring IV&V activities, and documenting outcomes, small projects can meet IV&V expectations efficiently while minimizing resource strain and supporting mission success.

## 4.1 Determine IV&V Applicability

The first step for a small project is determining if the project falls under a category requiring IV&V. Focus on the classification criteria outlined in the requirement:

1. **Category 1 Projects (NPR 7120.5):**

   * Likely **not applicable** to most small projects, as Category 1 projects are typically large flagship missions. However, confirm the classification with appropriate program oversight.
2. **Category 2 Projects with Class A or Class B Payloads (NPR 8705.4):**

   * Determine if the payload is classified as **Class A** (life-critical/high-priority) or **Class B** (high-priority science/exploration mission). If either applies, IV&V is required.
   * Many small projects are likely to have Class C or below payloads, which may not require IV&V. Confirm the risk classification in consultation with the payload team and engineering groups.
3. **MDAA-Selected Projects:**

   * Small projects may be explicitly chosen for IV&V by the Mission Directorate Associate Administrator (MDAA) due to unique risks, high-priority science objectives, or novel approaches. Verify if any explicit selection criteria apply.
   * Check for communication or directives from the MDAA regarding IV&V applicability.

## 4.2 Tailor IV&V Activities

Small projects may not have the resources to implement full-scale IV&V activities. Tailoring IV&V to fit the size, complexity, and risk profile of the project is essential. Coordinate with IV&V experts to identify a manageable process within the project scope.

1. **IV&V Scope for Small Projects:**

   * Focus IV&V on **mission-critical software functions** that directly impact mission objectives or safety.
   * Prioritize **requirements validation** to ensure all software functionality aligns with mission and payload risk classifications.
   * Limit IV&V to high-risk areas (e.g., safety-critical functionality, interfaces between complex software components).
2. **Simplified IV&V Implementation:**

   * **Use automated tools** for defect detection, code inspections, and requirement verification (e.g., static analysis tools for small software systems).
   * Conduct **focused risk assessments** to identify potential software issues that could jeopardize mission-critical functions.
   * Implement **peer reviews** or streamlined inspections as part of IV&V activities, ensuring independent scrutiny with minimal overhead.

## 4.3 Coordinate with the NASA IV&V Program

Small projects should leverage resources and expertise from the NASA IV&V Program to reduce the burden of implementing IV&V activities. Reach out to the IV&V Program team during early planning stages to explore tailored support.

1. **Request Assistance from IV&V Program:**

   * Discuss project classification and risk details with the NASA IV&V Program.
   * Request guidance on IV&V scalability for small projects, including recommendations for high-impact areas to focus IV&V efforts.
   * Explore opportunities for limited resource-sharing, such as using IV&V expertise for strategic evaluations or risk identification.
2. **IV&V Tools and Technologies:**

   * Utilize automated IV&V tools provided by NASA’s IV&V Program or other trusted sources.
   * Leverage IV&V processes and checklists tailored for smaller-scale software systems.

## 4.4 Ensure Alignment with Standards

Even for small projects, adherence to NASA standards (NPR 7150.2, NPR 8705.4, and NASA-STD-8739.8) is critical for ensuring compliant implementation of IV&V processes. Tailor compliance levels without compromising minimum safety and quality thresholds.

1. **IV&V Compliance Checklist for Small Projects:**

   * Verify the software requirements are complete, traceable, and testable.
   * Ensure that testing plans include validation of mission-critical requirements and high-risk areas.
   * Document safety-critical requirements and confirm software properly mitigates hazards.
2. **Streamlined Reporting:**

   * Use simplified templates to document outcomes of IV&V activities, risk assessments, and testing results.
   * Clearly show evidence of IV&V implementation and compliance with NASA-STD-8739.8 standards.

## 4.5 Manage Costs and Resources

The program manager for a small project must carefully manage costs and resources to fulfill IV&V requirements efficiently.

1. **Budgeting for IV&V:**

   * Allocate a **dedicated portion of the budget** to IV&V activities, scaled appropriately to the project size and classification.
   * Work with the IV&V Program to avoid unnecessary duplication of efforts and optimize resource utilization.
2. **Resource Efficiency:**

   * Assign **qualified personnel** with IV&V expertise to focus on high-impact areas of the software lifecycle.
   * Minimize redundancy by integrating software assurance and IV&V processes wherever possible.

## 4.6 Documentation and Review

Small projects still need to provide clear documentation to demonstrate compliance with IV&V requirements. Keeping documentation simple yet sufficient allows the project to meet NASA oversight expectations without excessive effort.

1. **Required Documents:**

   * **IV&V Implementation Plan**: Tailored plan specifying the scope, timeline, and resources for IV&V activities.
   * **Risk Analysis Report**: Focused assessment of software risks related to mission and safety-critical functionality.
   * **IV&V Results Summary**: Concise report of validation outcomes, defect identification/resolution, and recommendations for improvement.
   * **Compliance Certification**: Evidence of conformance to NASA-STD-8739.8 standards.
2. **Review Activities:**

   * Conduct peer reviews or audits to validate IV&V implementation and confirm requirements compliance.
   * Submit documentation for review by relevant NASA program offices or IV&V representatives.

## 4.7 Key Considerations for Small Projects

1. **Focus on Critical Functions**:  
   For small projects, prioritize IV&V activities on high-risk components such as safety-critical systems, key interfaces, or functions directly supporting mission objectives.
2. **Scale Activities to Project Size**:  
   Use tailored processes and tools to fit IV&V into the constraints of smaller budgets, shorter timelines, and limited resources.
3. **Leverage NASA Expertise**:  
   Collaborate with the NASA IV&V Program to maximize efficiency through shared tools, resources, and scaled support.
4. **Demonstrate Compliance**:  
   Provide clear documentation of IV&V planning, execution, and results to meet NASA standards, even for lightweight IV&V implementations.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-048)

  [Risk Classification for NASA Payloads](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=4A "Click to open in new window")

  NPR 8705.4A, Office of Safety and Mission Assurance, Effective Date: April 29, 2021, Expiration Date: April 29, 2026
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-367)

  [IEEE Standard Dictionary of Measures of the Software Aspects of Dependability,](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1634994 "Click to open in new window")

  IEEE Computer Society, Sponsored by the Software Engineering Standards Committee, IEEE Std 982.1™-2005, (Revision of IEEE Std 982.1-1988),
* (SWEREF-518)

  [Independent Verification and Validation of Embedded Software](https://llis.nasa.gov/lesson/723 "Click to open in new window")

  Public Lessons Learned Entry: 723.
* (SWEREF-584)

  [Does Software IV&V Provide Clear Benefits to NASA Projects?](https://llis.nasa.gov/lesson/6656 "Click to open in new window")

  Public Lessons Learned Entry: 6656.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The NASA Lessons Learned database provides key insights into the effectiveness of Independent Verification and Validation (IV&V) for mission-critical and high-risk projects. The following lessons highlight the value and importance of IV&V, emphasizing its role in improving software quality, reducing risks, and ensuring mission success:

---

#### **1. Independent Verification and Validation of Embedded Software (Use of IV&V Procedures)**

**Lesson Number: 723**

* **Summary:**  
  "The use of Independent Verification and Validation (IV&V) processes ensures that computer software is developed according to its original specifications, performs satisfactorily in the operational mission environment for which it was designed, and does not execute unintended functions. Errors identified and resolved early in the development cycle are significantly less costly to correct than those found in later stages, and the quality and reliability of software are notably enhanced."
* **Relevance:**  
  IV&V acts as a critical safeguard against software errors, particularly for embedded systems in mission-critical environments, where unintended functionality could lead to catastrophic consequences. Leveraging IV&V early in the development lifecycle minimizes the cost and risk of downstream rework. Projects that incorporate IV&V processes can ensure software correctness, traceability, and operational reliability in unpredictable environments.

---

#### **2. Does Software IV&V Provide Clear Benefits to NASA Projects?**

**Lesson Number: 6656**

* **Summary:**  
  "Recent NASA spaceflight projects that have undergone IV&V of their mission software perceive the process as offering clear benefits beyond those accrued through validation and verification (V&V) performed solely by project personnel. The specific benefits of IV&V participation by the NASA IV&V Center for four recent JPL spaceflight projects are discussed, along with recommendations for future IV&V programs."
* **Relevance:**  
  Independent evaluations by the NASA IV&V Center provide a broader, unbiased perspective that complements in-house V&V efforts by project teams. The lessons acknowledge that IV&V strengthens the end-to-end review process, identifies overlooked risks, and enhances confidence in the quality of mission-critical software. A key takeaway is that IV&V is not redundant but rather additive, providing critical assurance for high-priority projects.

---

### **Additional NASA Lessons Learned Related to IV&V**

#### **3. Software Validation and Verification Requirements**

**Lesson Number: 0333**

* **Summary:**  
  "Inadequate specification or execution of software validation and verification requirements has been a recurring cause of mission failures. IV&V aids in ensuring comprehensive validation and verification of software systems, serving as a safeguard against incomplete requirements and unverified critical functions."
* **Relevance:**  
  This lesson underscores the significant role IV&V plays in ensuring that software V&V requirements are complete and effectively implemented. NASA’s focus on IV&V prevents overlooked validation activities, ensuring that safety-critical and mission-critical requirements are fully traced, tested, and verified. Applying IV&V systematically reduces the likelihood of unidentified gaps during project development that could lead to operational anomalies.

---

#### **4. Mars Climate Orbiter Mishap Investigation Highlights the Importance of IV&V**

**Lesson Number: 0639**

* **Summary:**  
  "The Mars Climate Orbiter mission failed due to a unit conversion error that went undetected during software design, development, and testing processes. A rigorous IV&V program could have identified the issue early and avoided the mission loss."
* **Relevance:**  
  This lesson illustrates how the omission of a rigorous IV&V process can allow critical issues such as software logic errors, integration faults, or unit inconsistencies to persist undetected through lifecycle phases. The Mars Climate Orbiter’s loss highlights the broader value of IV&V in early identification of risks during requirement definition, design, and testing stages. For projects with significant technical or operational risks (e.g., deep-space probes or crewed launches), ensuring that software receives independent scrutiny is essential.

---

#### **5. Fault Detection and Ensuring Nominal Performance in Safety-Critical Systems**

**Lesson Number: 1070**

* **Summary:**  
  "Software faults can compromise the reliability and safety of spacecraft systems. Independent Verification and Validation (IV&V) processes, when implemented rigorously, can identify software faults that might otherwise result in mission-critical anomalies or failures."
* **Relevance:**  
  For small or high-risk projects, safety-critical software must achieve very high reliability thresholds. IV&V ensures that fault management systems are robust, thoroughly analyzed for edge cases, and evaluated under nominal and off-nominal scenarios. This lesson demonstrates how IV&V can strengthen the development process of critical systems by systematically assessing failure modes and ensuring fault tolerance.

---

#### **6. IV&V: Value for Mission Assurance in Class A and Class B Payloads**

**Lesson Number: 1842**

* **Summary:**  
  "Class A and B payloads—those with the highest scientific or safety-critical importance—depend on highly reliable software systems that have been validated against stringent mission requirements. Independent IV&V provides the necessary assurance for these payloads, identifying mission-critical risks and ensuring design compliance at every development stage."
* **Relevance:**  
  Class A and B missions require careful attention to software functionality, safety, and cost-effectiveness. This lesson emphasizes IV&V as a resource that complements internal validation efforts, ensuring that all software-critical risks are addressed within a strict mission schedule. For these projects, IV&V is key to achieving acceptable failure probabilities and maximizing confidence in operational success.

---

#### **7. Integrating IV&V Early to Reduce Rework and Delays**

**Lesson Number: 5413**

* **Summary:**  
  "IV&V conducted late in the development cycle often leads to costly rework and project delays. Integrating IV&V early—especially at planning and requirements stages—significantly reduces risks and ensures fewer critical defects are identified in later lifecycle phases."
* **Relevance:**  
  IV&V is most effective when implemented during early project phases, such as requirements definition (Key Decision Point A). This lesson reinforces the requirement's emphasis on integrating IV&V early for eligible projects. Early intervention improves requirement completeness; identifies gaps, ambiguities, or errors; and minimizes cost impacts by addressing software issues before they escalate during the coding, integration, or testing phases.

---

**LL‑SW‑01 — Standards for Heritage Software Reuse and Testing**

* **Source LL ID(s):** IVV‑01
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** Program teams planned to reuse “legacy” flight software; significant defects emerged late, revealing the misconception that heritage code needs minimal testing.
* **Lesson Learned:** Treat heritage software **as if new**—perform full requirements validation, interface verification, regression testing, and environmental qualification for the new mission context.
* **Evidence/Observation:** PPE planned legacy reuse; issues were still open at the pause; reuse assumptions delayed defect discovery and correction.
* **Cause(s):** Belief that prior flight history obviates testing; lack of program‑level reuse standards.
* **Recommendation/Corrective Action:** Establish **project‑level reuse standards** specifying test scope (regression, interface, environment), verification criteria, and acceptance gates for heritage software.
* **Implementation Guidance:** Embed reuse criteria in plans (SWE‑013), trace reused functionality to requirements/design/tests (SWE‑052/059/064/072), and determine safety classification impacts (SWE‑133/134).
* **Success Criteria/Verification:** Documented reuse plan; executed test campaigns; evidence of bidirectional traceability and IV&V closure; defect rates comparable to new development baselines.
* **Applicability/Scope:** All mission/safety‑critical software; heritage and third‑party components.
* **Related Standards/Requirements:** **SWE‑027 (COTS/legacy use), SWE‑013 (Plans), SWE‑050 (Requirements), SWE‑052/059/064/072 (Traceability), SWE‑133/134 (Safety)**.

**LL‑SW‑02 — Heritage Knowledge vs. Heritage Code**

* **Source LL ID(s):** IVV‑10
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** Teams treated legacy code as “plug‑and‑play,” underestimating adaptation effort and verification for new architectures and interfaces.
* **Lesson Learned:** Leverage heritage **experience**, not **code** blindly; plan/budget as new development; invite IV&V **early** to requirements TIMs and merges to surface gaps sooner.
* **Evidence/Observation:** Late requirement updates and delivery slips affected dependent systems; IV&V participation earlier would have found gaps.
* **Cause(s):** Under‑scoped changes; late IV&V engagement.
* **Recommendation/Corrective Action:** Require **early IV&V engagement** (SWE‑141/131), define reuse criteria (LL‑SW‑01), and enforce full traceability from stakeholder needs through tests (SWE‑050/052/072).
* **Implementation Guidance:** Add IV&V coordination to contracts and schedules; include IV&V in requirements reviews; maintain authoritative baselines and snapshots.
* **Success Criteria/Verification:** Fewer late requirement changes; on‑schedule deliveries; reduced rework and nonconformances.
* **Applicability/Scope:** Any reuse effort across new mission contexts.
* **Related Standards/Requirements:** **SWE‑141, SWE‑131, SWE‑050, SWE‑052**.

**LL‑SW‑03 — Define Artifact Access vs. Delivery Expectations**

* **Source LL ID(s):** IVV‑07
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** It took ~6 months to obtain limited artifact “access,” insufficient for tool‑based analysis; effectiveness dropped sharply.
* **Lesson Learned:** Contracts must explicitly define **access** (portal read) vs. **delivery** (files for tooling), with rationale and intended use (traceability, FDIR analysis).
* **Evidence/Observation:** Tool‑driven analysis needs full artifacts to compute relationships across thousands of requirements; delays impede phase‑aligned feedback.
* **Cause(s):** Ambiguous contractual language; unclear IV&V needs.
* **Recommendation/Corrective Action:** Specify artifact delivery cadence, formats, and completeness (requirements snapshots, designs, code, tests) and repository permissions.
* **Implementation Guidance:** Tie to **SWE‑050** (requirements captured/maintained), **SWE‑052/072** (traceability across artifacts), **SWE‑131/141** (IV&V planning/execution).
* **Success Criteria/Verification:** IV&V receives complete, tool‑readable baselines at defined intervals; measurable reduction in analysis latency.
* **Applicability/Scope:** All mission/safety‑critical developments.
* **Related Standards/Requirements:** **SWE‑013, SWE‑050, SWE‑052, SWE‑072, SWE‑131, SWE‑141**.

**LL‑SW‑04 — Provide Direct Read‑Only Access to Code Repositories**

* **Source LL ID(s):** IVV‑04
* **Discipline(s):** Software Assurance, IV&V, Software Engineering
* **Context/Background:** Teams that granted IV&V read‑only repository access (e.g., GitLab) enabled near‑real‑time analysis and reduced packaging delays.
* **Lesson Learned:** Use industry‑standard practice: **IV&V read‑only repo access** to current versions for in‑phase feedback, ancillary build info, and improved coverage.
* **Evidence/Observation:** Latency dropped from 6+ months to near real‑time for VSM/CSM/MSM teams.
* **Cause(s):** Reliance on manual deliveries; limited visibility.
* **Recommendation/Corrective Action:** Require repo access in contracts; add secure, role‑based credentials; define supported branching and tagging schemes.
* **Implementation Guidance:** Align with **SWE‑131/141** (IV&V), trace requirements to code (**SWE‑064/052**), and ensure build artifacts support test traceability (**SWE‑072**).
* **Success Criteria/Verification:** IV&V confirms clean builds; timely defect reports aligned with development sprints; reduced false positives.
* **Applicability/Scope:** All projects using SCM.
* **Related Standards/Requirements:** **SWE‑064, SWE‑072, SWE‑131, SWE‑141**.
* **References:** Gateway S&MA LL deck; NASA SWEHB.

**LL‑SW‑06 — Provide Design Artifacts Early and In‑Phase with Development**

* **Source LL ID(s):** IVV‑02
* **Discipline(s):** Software Assurance, IV&V, Software Design
* **Context/Background:** Early design visibility enables cheaper, timely feedback; late delivery limits IV&V value.
* **Lesson Learned:** Share evolving designs **before coding**; IV&V supports iterative updates and identifies issues when change costs are lowest.
* **Evidence/Observation:** Difficulties obtaining early design artifacts on HALO/PPE reduced synchronization and defect prevention.
* **Cause(s):** Perception that IV&V slows design.
* **Recommendation/Corrective Action:** Include design artifact delivery milestones in IV&V PEP; allow early access to drafts.
* **Implementation Guidance:** **SWE‑013** (planning), **SWE‑018** (reviews), **SWE‑131/141** (IV&V).
* **Success Criteria/Verification:** Reduced design‑phase rework; fewer late defects; on‑time IV&V reviews.
* **Applicability/Scope:** All mission/safety‑critical designs.
* **Related Standards/Requirements:** **SWE‑013, SWE‑018, SWE‑131, SWE‑141**.

**LL‑SW‑07 — Share Requirement Implementation Status with IV&V**

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

**LL‑SW‑09 — Provide System Configuration Information for Clean Builds**

* **Source LL ID(s):** IVV‑09
* **Discipline(s):** Software Assurance, IV&V, DevOps
* **Context/Background:** Source deliveries lacked build scripts/configs; static analysis quality suffered; false positives increased.
* **Lesson Learned:** Deliver all **build scripts, instructions, dependencies, and planned operational configurations** to enable clean compilations and context‑correct analysis.
* **Evidence/Observation:** Highly configurable flight systems need operational modes to contextualize defects.
* **Cause(s):** Missing licensed deps; incomplete build info.
* **Recommendation/Corrective Action:** Define build deliverables in DRDs; ensure SCM includes CI configs; document operational parameter sets.
* **Implementation Guidance:** Tie to **SWE‑064** (design‑code traceability), **SWE‑072** (test‑req traceability), and IV&V (**SWE‑131/141**).
* **Success Criteria/Verification:** IV&V confirms reproducible builds; stable static/dynamic analysis; reduced false positives.
* **Applicability/Scope:** All software deliveries to IV&V.
* **Related Standards/Requirements:** **SWE‑064, SWE‑072, SWE‑131, SWE‑141**.

**LL‑SW‑10 — Early and Continuous IV&V Integration**

* **Source LL ID(s):** IVV‑03
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** IV&V entered post‑CDR on HALO/PPE; early defects were missed; rework and schedule churn increased.
* **Lesson Learned:** Integrate IV&V **from formulation** through test; deliver artifacts continuously to enable in‑phase analyses.
* **Evidence/Observation:** Early IV&V identifies requirements/design risks when changes are cheapest.
* **Cause(s):** Perception IV&V slows development; absent IV&V provisions in contracts.
* **Recommendation/Corrective Action:** Include IV&V requirements in acquisition; define PEP milestones; align sprint cadences.
* **Implementation Guidance:** **SWE‑131/141** (IV&V planning/execution), **SWE‑013** (project plans), **SWE‑018** (reviews).
* **Success Criteria/Verification:** Consistent, timely IV&V findings; reduced late rework; improved test readiness.
* **Applicability/Scope:** All mission/safety‑critical software.
* **Related Standards/Requirements:** **SWE‑131, SWE‑141, SWE‑013, SWE‑018**.

### **Summary of Key Takeaways from Lessons Learned**

* **Improves Software Reliability:** IV&V ensures that software functions as intended, avoiding critical errors that could compromise mission objectives.
* **Reduces Latent Risks:** IV&V acts as an independent check to identify risks that might escape detection during internal validation processes.
* **Enhances Mission Confidence:** Through rigorous, unbiased assessments, IV&V strengthens software quality and provides higher assurance of success for high-stake projects.
* **Cost Efficiency:** IV&V reduces costs associated with corrective measures by identifying issues early during software development.
* **Prevents Catastrophic Outcomes:** Past mission failures, including the Mars Climate Orbiter, highlight the crucial role of IV&V in addressing overlooked risks.

### **Link to Overall Requirement:**

The inclusion of these lessons learned strengthens the rationale for implementing software IV&V on Category 1 projects, Class A/Class B payloads, and other MDAA-selected missions. As software becomes more integral to mission-critical systems, IV&V continues to provide proven benefits in mitigating risks, improving safety, and ensuring mission success.

### 6.2 Other Lessons Learned

* **Software IV&V**
  + IV&V approaches and resources must align with the program's risk posture.
  + A closed-loop, auditable, corrective action toolset and process must be used to manage all IV&V identified issues and risks.

# 7. Software Assurance

**SWE-141 - Software Independent Verification and Validation**

3.6.2 For projects reaching Key Decision Point A, the program manager shall ensure that software IV&V is performed on the following categories of projects:

a. Category 1 projects as defined in NPR 7120.5.  
b. Category 2 projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4, Risk Classification for NASA Payloads.  
c. Projects selected explicitly by the Mission Directorate Associate Administrator (MDAA) to have software IV&V.

Integrating independent IV&V into software assurance helps reduce systemic risks and provides a mechanism for identifying issues early in development where corrections are most cost-effective. Software assurance personnel must actively monitor, review, and leverage IV&V outcomes to ensure alignment with project goals and NASA's overarching risk mitigation strategies. By maintaining oversight of IV&V compliance and integration, software assurance helps ensure a reliable, safe, and mission-successful software system.

See also [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts), [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks),

Software assurance considers using an audit approach to determine that the IV&V provider is performing the IV&V functions defined in these requirements. See also Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing).

See also Topic [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that IV&V requirements (section 4.4) are complete on projects required to have IV&V.

## 7.2 Software Assurance Products

1. **IV&V plan showing how the IV&V provider is planning on meeting the IV&V requirements**
2. **IV&V issues and risks**
3. **Focus on Issues and Risks:**

   * If IV&V is not executed as required by **NPR 7150.2**, unresolved issues in software design, functionality, reliability, or safety may lead to:
     + Increased likelihood of undetected defects.
     + Escalating software-related safety risks.
     + Limited visibility into software assurance gaps, potentially compromising mission success.
     + Higher costs and delays due to late identification of software issues after major development milestones.
4. **Confirmation of IV&V Involvement:**

   * Software assurance teams must ensure evidence is documented to confirm whether IV&V involvement is occurring (if applicable), particularly during critical milestones such as requirements review, design, coding, testing, and integration.

## 7.3 Metrics

To ensure that **Independent Verification and Validation (IV&V)** activities are effectively implemented and support compliance with this requirement, collecting and analyzing appropriate software assurance metrics is essential. These metrics help track the progress, quality, and outcomes of IV&V efforts, providing actionable insights for managing risks and improving software quality.

These metrics provide measurable insights into software quality, IV&V effectiveness, process efficiency, and risk mitigation for projects requiring software IV&V under this requirement. By consistently tracking and analyzing these metrics, program managers can ensure:

* Early identification and mitigation of software risks.
* Compliance with NASA standards and processes.
* Achievement of mission success within the allocated budget and timeframe.

The following metrics are recommended to monitor the effectiveness of IV&V and support requirement compliance for software assurance:

### 7.3.1 Requirements Metrics

#### **a. Requirements Verification Coverage**

* **Definition:** The percentage of software requirements that have been verified by the IV&V team to ensure correctness, completeness, and alignment with stakeholder expectations.
* **Formula:**  
  [ \text{Requirements Verified (%) = (Number of Requirements Verified / Total Number of Requirements)} \times 100 ]
* **Purpose:** Ensures that all mission-critical (and safety-critical) requirements are tested for accuracy and traceability, reducing the risk of undetected errors or gaps.

#### **b. Requirements Deficiency Rate**

* **Definition:** The number of software requirements identified as incomplete, inconsistent, ambiguous, or erroneous by the IV&V process.
* **Formula:**  
  [ \text{Requirements Deficiency Rate = (Number of Defective Requirements / Total Number of Requirements)} \times 100 ]
* **Purpose:** Measures the ability of the IV&V process to identify poorly defined or flawed requirements early, reducing costly rework during later development phases.

### 7.3.2 Defect Detection and Resolution Metrics

#### **a. Defect Detection Effectiveness (IV&V)**

* **Definition:** The percentage of total software defects detected by the IV&V process relative to all defects found (IV&V + project team).
* **Formula:**  
  [ \text{Defect Detection Effectiveness (%) = (Defects Found by IV&V / Total Defects Found)} \times 100 ]
* **Purpose:** Demonstrates how effective IV&V is at identifying software defects that might otherwise go unnoticed by the internal development team.

#### **b. Defect Density**

* **Definition:** The number of defects found per unit of code (e.g., per thousand lines of code (KLOC)) during the IV&V process.
* **Formula:**  
  [ \text{Defect Density = Total Number of Defects Detected / Total KLOC} ]
* **Purpose:** Tracks the quality of the software being reviewed by the IV&V process and identifies areas of the codebase needing increased focus.

#### **c. Defect Injection and Removal Rates**

* **Definition:** The total number of defects introduced per phase (e.g., design, development, integration, and testing) versus those removed via IV&V activities.
* **Purpose:** Identifies phases where defects are most frequently injected and helps assess the effectiveness of IV&V in removing those defects.

### 7.3.3 Risk and Safety Metrics

#### **a. Risk Identification Rate**

* **Definition:** The number of software-related risks identified by the IV&V process per month, phase, or milestone.
* **Formula:**  
  [ \text{Risk Identification Rate = Total Risks Identified by IV&V / Time Period (e.g., month, phase)} ]
* **Purpose:** Tracks how actively and effectively the IV&V team identifies software-related risks (e.g., safety, mission-critical functionality) at various project stages.

#### **b. Safety Non-Compliance Rate**

* **Definition:** The percentage of safety-critical components reviewed by IV&V that are found to be non-compliant with NASA safety standards.
* **Formula:**  
  [ \text{Safety Non-Compliance Rate = (Non-Compliant Safety Cases / Total Safety-Critical Software Components)} \times 100 ]
* **Purpose:** Measures how well software aligns with safety-critical requirements and identifies areas where additional scrutiny is required.

#### **c. Hazard Resolution Rate**

* **Definition:** The percentage of hazards identified by IV&V that have been mitigated or resolved.
* **Formula:**  
  [ \text{Hazard Resolution Rate (%) = (Hazards Mitigated by IV&V / Total Hazards Identified)} \times 100 ]
* **Purpose:** Tracks the progress of addressing software risks associated with safety-critical systems and ensures timely mitigation of hazards.

### 7.3.4 Process Performance Metrics

#### **a. IV&V Activity Completion Rate**

* **Definition:** The percentage of planned IV&V tasks or deliverables (e.g., reviews, audits, reports) that are completed on time at each project milestone.
* **Formula:**  
  [ \text{Activity Completion Rate (%) = (Completed IV&V Activities / Total Planned IV&V Activities)} \times 100 ]
* **Purpose:** Monitors how well the IV&V process adheres to the project schedule and ensures that IV&V activities are timely and effective.

#### **b. Effort Allocation for Critical Components**

* **Definition:** The percentage of IV&V effort focused on software components classified as mission-critical or safety-critical.
* **Formula:**  
  [ \text{Effort on Critical Components (%) = (Time Spent on Critical Components / Total IV&V Time)} \times 100 ]
* **Purpose:** Ensures the IV&V team allocates sufficient time and resources to high-risk areas, consistent with their importance to the mission.

### 7.3.5 Quality Metrics

#### **a. Compliance to Standards**

* **Definition:** The percentage of IV&V-reviewed software artifacts (e.g., requirements, design documents, test plans) that are fully compliant with applicable NASA technical standards (e.g., NASA-STD-8739.8).
* **Formula:**  
  [ \text{Compliance Percentage = (Compliant Artifacts / Total Reviewed Artifacts)} \times 100 ]
* **Purpose:** Tracks adherence to NASA-specific software assurance standards during each phase of development.

#### **b. Rework Reduction Due to IV&V**

* **Definition:** The reduction in defects requiring rework in later phases (e.g., testing, validation, or operations) due to issues identified early by IV&V.
* **Formula:**  
  [ \text{Rework Reduction (%) = (Defects Removed Early / Total Defects that Would Cause Rework)} \times 100 ]
* **Purpose:** Demonstrates IV&V’s contribution to preventing costly rework by identifying defects earlier.

### 7.3.6 Cost and Efficiency Metrics

#### **a. Cost of Defects Detected by IV&V**

* **Definition:** The cost savings achieved by IV&V through early detection of defects (compared to the cost of detecting those same defects during later project phases or post-launch).
* **Purpose:** Highlights the financial benefits of early IV&V intervention and supports the case for investing in IV&V at key project stages.

#### **b. IV&V Budget Utilization Rate**

* **Definition:** The percentage of the allocated IV&V budget utilized during the project.
* **Formula:**  
  [ \text{Budget Utilization Rate (%) = (Actual IV&V Costs / Budgeted IV&V Costs)} \times 100 ]
* **Purpose:** Tracks whether the IV&V process is staying within budget while effectively achieving its objectives.

### 7.3.7 Testing Metrics

#### **a. Testing Coverage (Requirements-Based)**

* **Definition:** The percentage of software requirements that are verified through testing.
* **Formula:**  
  [ \text{Testing Coverage (%) = (Number of Tested Requirements / Total Requirements)} \times 100 ]
* **Purpose:** Ensures adequate test coverage for mission-critical and safety-critical requirements identified in the IV&V process.

#### **b. Post-Release Defect Rate**

* **Definition:** The number of defects detected in operational software after delivery or deployment, specifically for areas reviewed by IV&V.
* **Purpose:** Measures the effectiveness of the IV&V process in preventing operational anomalies.

## 7.4 Guidance

### 7.4.1 Definition and Scope of IV&V

* IV&V, as described in **NASA-STD-8739.8 Section 4.4**, applies universally to all software projects where IV&V is required or selected.
* **Purpose of IV&V:**
  + To serve as a **risk mitigation activity** that identifies and addresses potential software risks to safety, reliability, performance, and mission success.
  + The rigor of IV&V analysis is determined by the **IV&V Provider’s risk assessment**, which focuses on areas of the highest software criticality and potential for latent defects.

### 7.4.2 IV&V as a Key Software Assurance Discipline

* **IV&V Integration:** IV&V is a technical and independent component of software assurance, applying rigorous analysis and testing methodologies to:
  1. Verify whether products and processes conform to **requirements and design specifications**.
  2. Validate whether systems/software meet **mission needs** under both nominal and off-nominal conditions.
* **Life Cycle Coverage:**
  + IV&V activities are performed throughout the **software development life cycle (SDLC)**.
  + Activities assess correctness, dependability, safety, fault management, and security during requirements definition, design, implementation, integration, testing, and operational phases.
* **Outcomes of IV&V:**
  + Provide **evidence-based assurance conclusions** that support decision-making across the development lifecycle.
  + Contribute insight into system properties, such as correctness, robustness, security, and adherence to requirements, enabling early risk mitigation.

### 7.4.3 Verification and Validation Activities

#### **Primary IV&V Activities:**

1. **Verification:** Ensures that the **software conforms** to specified requirements and design standards by evaluating software products at each phase of the SDLC.
2. **Validation:** Confirms that the software **meets its intended purpose** by assessing whether it satisfies system and user needs, stakeholder expectations, and mission objectives.

#### **Planning and Tailoring the IV&V Effort:**

* **IV&V Project Execution Plan (IPEP):**
  + Captures the planning, activities, risk prioritization, rigor level, and tailored IV&V requirements.
  + Serves as both a guiding document for IV&V execution and a **communication tool** between the project and the IV&V Provider.
  + Updated iteratively throughout the project to reflect evolving risks and changing scopes.
* **Risk and Scope Assessment:**
  + **Focus on High-Risk Areas:** IV&V concentrates resources on high-priority risks with the potential to significantly impact safety or mission success.
  + **Iterative Adjustments:** Plans and IV&V tasks evolve based on refined understanding of system risks, enabling a "Follow the Risk" strategy.

### **7.4.4 Software Assurance Responsibilities**

* **SA Oversight of IV&V:**
  + Review IV&V activities to ensure compliance with IV&V-related requirements, as outlined in **NPR 7150.2**.
  + Assess IV&V outputs (e.g., defect reports, risk assessments) and incorporate results into the overall **software assurance strategy**.
  + Ensure that identified issues and risks surfaced by IV&V are tracked, communicated, and addressed within the development project.
* **Independent Provider Criteria:**
  + Verify that the IV&V Provider operates with financial, managerial, and technical independence from the development organization, ensuring no conflict of interest.

### 7.4.5 Integration and Communication

#### **Supporting Project Reviews:**

* The IV&V Provider participates in key project reviews, including systems requirements reviews (SRRs), software requirements reviews (SwRRs), design reviews, and pre-test reviews.
* Contributions include:
  + Status updates on IV&V activities.
  + Evaluation of project lifecycle artifacts.
  + Identification of defects, risks, and concerns to support decision-making.

#### **Ongoing Involvement:**

* Regular participation in technical interchange meetings and peer reviews ensures that IV&V insights remain aligned with the development effort.
* Real-time feedback enables proactive adjustment of development plans based on IV&V findings and risk assessments.

### 7.4.6 Continuous Improvement and Risk Feedback

* **Monitoring and Reporting:** Software assurance (SA) monitors the performance of IV&V activities, ensuring alignment with project goals and expectations.
* **Performance Metrics:**
  + SA teams may implement periodic assessments to measure IV&V impact on defect reduction, risk mitigation, and project assurance goals.
* **Adapting to Change:**
  + SA tracks project changes (e.g., scope, requirements revisions) that may impact IV&V assessments and adapts plans accordingly.

### 7.4.7 Critical Focus Areas of IV&V Analysis

#### **Requirements and Design:**

* Assesses the correctness, completeness, and traceability of system/software requirements and their mapping to architectural and design elements.

#### **Implementation:**

* IV&V evaluates **source code** against coding standards, security best practices, and safety guidelines.
* Code analysis tools (e.g., static and dynamic analyzers) are used to identify defects and potential vulnerabilities.

#### **Security Risks:**

* Verifies the implementation of mitigations for known **security vulnerabilities** in the software requirements and code.
* Continuously assesses risks related to open-source software components and reused software.

#### **Testing:**

* Validates the adequacy of testing artifacts (e.g., test designs, plans, and procedures) and verifies traceability to software/system requirements.
* Confirms that test results meet defined acceptance criteria for both nominal and off-nominal conditions, including safety-critical scenarios.

#### **Operations and Maintenance:**

* IV&V ensures that operational risks are continuously monitored, especially for evolving or updated software systems.
* Supports impact assessments for software changes and analyzes ripple effects of modifications to system behavior.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks) * [SWE-223 - Tailoring IV&V project selections](/spaces/SWEHBVD/pages/105710152/SWE-223+-+Tailoring+IV+V+project+selections)       * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

# 8. Objective Evidence

This requirement mandates that software Independent Verification and Validation (IV&V) is applied to high-risk or critical projects. The primary purpose of IV&V is to increase confidence in the software by ensuring that it functions correctly, meets its requirements, and satisfies safety and mission-critical criteria identified early in the project life cycle.

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

Below is clear guidance and specific examples of objective evidence to demonstrate compliance with this requirement.

## 8.1. Documented IV&V Program Agreement

One of the clearest and most direct pieces of evidence is formal documentation showing the agreement to perform IV&V for applicable projects.

##### **Must Include**:

* Signed or approved **IV&V Agreement Plan**, Memorandum of Agreement (MOA), or Memorandum of Understanding (MOU) between the program/project and the NASA IV&V Program or an external IV&V provider.
* Evidence that the agreement clearly specifies:
  + The project's **risk category** (Category 1 or Category 2 with Class A or Class B payload).
  + The presence of a **requirement** for IV&V based on NPR 7120.5 and NPR 8705.4.
  + The **scope of IV&V**—including artifacts, lifecycle stages, and categories of software that will undergo IV&V.
  + The **IV&V provider** (e.g., NASA IV&V Program or another qualified independent organization).
* Commitment by required stakeholders, such as the program manager and participating IV&V teams, codified in signatures.

##### **Examples of Evidence**:

* A **dedicated IV&V inclusion statement** in the project plan or software management plan:
  + Example: “The IV&V Program has been engaged to perform software IV&V for Project X (Category 1, Class A). IV&V engagement will cover SRR through ORR and include verification of safety-critical software.”
* A formalized **MOA/MOU** signed and dated by:
  + **Program Manager.**
  + **IV&V Program Manager (or representative).**
  + **Mission Directorate Associate Administrator (if applicable).**

## 8.2 Software Classification and Project Categorization

Clear classification of the project and software is essential for determining whether IV&V applies.

##### **Must Include**:

* Documentation formally categorizing the project as **Category 1 or Category 2** in line with NPR 7120.5.
* For **Category 2 projects**, evidence confirming the payload risk classification is **Class A or Class B** as per NPR 8705.4.
* Evidence that explicitly confirms the project's inclusion in the list of IV&V-required projects submitted by the **Mission Directorate Associate Administrator (MDAA),** if applicable.

##### **Examples of Evidence**:

* **Project Categorization Worksheet**:
  + Formal worksheet or signed report documenting the project's classification and risk category, including:
    - Risk Category: Category 1 or Category 2.
    - Payload class: Class A, Class B, etc.
    - Applicable definitions as per NPR 7120.5 and NPR 8705.4.
    - Signed approval by project stakeholders and/or project leadership.
* **Correspondence from the MDAA**:
  + Emails, memos, or official directives identifying the project as explicitly selected for IV&V.

##### **Specific Supporting Evidence**:

* Software project documentation definitively identifying software’s criticality level (e.g., "Safety-critical Class A system under NPR 8705.4").
* Approval or sign-off from the **Mission Directorate** confirming the classification aligned to IV&V criteria.

## 8.3 IV&V Implementation Plan

An **IV&V Implementation Plan** outlines how and when IV&V will be conducted for the project. This provides strong evidence that IV&V responsibilities have been formally aligned with project goals.

##### **Must Include**:

* Documentation establishing the **scope and objectives** of IV&V for the project, including:
  + Identified software components subject to IV&V (e.g., flight software, ground software).
  + Artifacts that IV&V will assess (e.g., requirements, design, code, test plans).
  + Specific risks addressed through IV&V.
* Detailed **IV&V schedule** and corresponding project milestones (e.g., SRR, PDR, CDR).
* Assignments of responsibilities between the project and IV&V provider, including the specific software components and phases.

##### **Examples of Evidence**:

* **IV&V Implementation Plan**:
  + A dated and approved document describing scope, schedule, milestones, software items, and activities for IV&V.
* **IV&V Activity Reports**:
  + Records of IV&V work performed at lifecycle milestones such as:
    - Key Decision Point (KDP) reviews.
    - System Requirements Review (SRR), Preliminary Design Review (PDR), and Critical Design Review (CDR).
    - Test readiness or operational readiness stages.

## 8.4 Reports and Evidence of IV&V Engagement

Objective evidence of ongoing IV&V engagement demonstrates execution of the agreed-upon IV&V activities.

##### **Must Include**:

* **Records of IV&V Activities**:
  + Evidence showing that IV&V results were delivered and reviewed by project stakeholders at lifecycle milestones.
* **IV&V Risk Assessment Reports**:
  + Reports from the IV&V team highlighting risks, findings, and recommendations for each assessed artifact (e.g., requirements, test cases, code, design documents).
* **Anomaly Reports**:
  + IV&V-identified defects or anomalies, including corrective actions tracked and resolved.
* **IV&V Decision Packages**:
  + Documentation showing IV&V assessments influenced key technical, safety, or quality decisions.

##### **Examples of Evidence**:

* **Milestone Reports**:
  + Reports showing IV&V participation at SRR, SDR, PDR, CDR, TRR, etc.
  + Test reports showing IV&V involvement in validating mission-critical requirements.
* **Risk Reports**:
  + Outputs from IV&V risk assessments, including:
    - Risk ranking of software system components.
    - Recommendations for mitigation or corrective action.
* **Defect Logs and Resolutions**:
  + Logs of software issues identified and addressed through IV&V feedback during code review or testing.

## 8.5 Independent Verification of Compliance

Objective evidence must confirm that the program manager maintained oversight to ensure compliance with IV&V requirements.

##### **Must Include**:

* Evidence of independent oversight processes or audits confirming IV&V was engaged as required.
* Documentation of periodic reviews assessing IV&V compliance during project milestones.

##### **Examples of Evidence**:

* **Compliance Verification Checklist**:
  + Review checklists confirming the project meets all IV&V engagement criteria.
* **SA Assurance Reports**:
  + Reports from Software Assurance (SA) personnel verifying that IV&V engagement aligns with NPR 7150.2 requirements.
* **Technical Authority Approval**:
  + Approval documentation from the **Engineering Technical Authority (ETA)** confirming compliance with this requirement.

## 8.6 Records of Decisions for IV&V Exclusions

If a project does not meet the requirements for IV&V, it is important to document that decision formally.

##### **Must Include**:

* **Exclusion Criteria Documentation**:
  + Evidence that the project does not fall under Category 1 or Category 2 with Class A/B payloads or is not explicitly selected by the MDAA.
* Approval of any exceptions or waivers by the appropriate governing authority.

##### **Examples of Evidence**:

* Approved **IV&V Exclusion Declaration** by the project manager and technical/governing authorities.
* Supporting rationale, such as risk analysis showing lower levels of criticality or complexity.

## 8.7 Summary of Objective Evidence

| **Category** | **Examples of Evidence** |
| --- | --- |
| IV&V Program Agreement | Signed MOA/MOU with NASA IV&V Program, signed IV&V inclusion statements in project plans. |
| Software Classification | Project classification worksheets (Category 1 or 2) and documentation of payload risk class (Class A or B). |
| IV&V Implementation Plan | Approved IV&V Implementation Plans with scope, schedule, and activities. |
| Reports of IV&V Activities | Milestone IV&V reports, risk assessment reports, findings, recommendations, and anomaly resolutions. |
| Compliance Verification Reports | Checklists and audits ensuring IV&V implementation is reviewed at each phase, signed off by the Engineering Technical Authority. |
| Records of Exclusion Decisions | Documented rationale for exclusions, if IV&V does not apply or waiver was granted. |

The collection of these artifacts provides robust, comprehensive proof of compliance with Requirement 3.6.2, ensuring that software IV&V is appropriately implemented and maintained throughout the project lifecycle.
