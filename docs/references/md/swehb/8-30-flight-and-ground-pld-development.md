# 8.30 - Flight and Ground PLD Development

> NASA Software Engineering Handbook (SWEHB Ver D), page id 209846294. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/209846294/8.30+-+Flight+and+Ground+PLD+Development

8.30 - Flight and Ground PLD Development

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/209846294/8.30+-+Flight+and+Ground+PLD+Development#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=209846294)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=209846294&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. SA Responsibilities](#tabs-1)
* [2. Flight and Safety Critical PLD Developments](#tabs-2)
* [3. Ground PLD or Research Development](#tabs-3)
* [4. Guidance](#tabs-4)
* [5. Resources](#tabs-5)

## Assurance Responsibilities for Flight and Ground PLD Development

PLDs, especially FPGAs, are becoming increasingly critical in complex avionics and space systems. Establishing a standardized and scalable approach to their development and assurance will not only improve consistency across NASA projects but also enhance mission safety and reliability. By emphasizing early planning, hazard management, training, cross-center collaboration, and consistent application of best practices, NASA can address current limitations while building a foundation for future advancements.

Furthermore, integrating lessons learned from other high-assurance industries (e.g., aerospace, automotive, medical devices) can provide valuable insights for effective PLD assurance within NASA. This proactive and forward-looking approach will ultimately ensure NASA’s cutting-edge missions are supported by reliable, secure, and cost-efficient FPGA systems.

## 1.1 Background

A Programmable Logic Device (PLD) is an integrated circuit that can be configured by a user to implement digital logic functions. PLDs offer flexibility and are used in a wide range of applications, from simple logic gates to complex digital systems. They can be reprogrammable, allowing for design changes and updates without needing to replace the physical hardware.

**Types of PLDs:**

* **Simple Programmable Logic Devices (SPLDs):** These are the basic types of PLDs, including Programmable Read-Only Memory (PROM), Programmable Logic Array (PLA), and Programmable Array Logic (PAL).
* **Field-Programmable Gate Arrays (FPGAs):** FPGAs are the most complex type of PLD, containing thousands or even millions of logic gates and offering the highest level of flexibility and programmability.

**Programmable Logic Devices (PLDs)** are widely used in avionics systems, including NASA missions. However, NASA does not currently have a standardized approach for PLD development. Each NASA center has implemented its own methods for PLD design and assurance, leading to inconsistent application of requirements. This inconsistency is often caused by confusion between software and PLDs. As a result, communication gaps arise within project teams, causing delays, anomalies, integration challenges, and costly redesigns. These issues negatively impact schedules, budgets, and system reliability.

This topic defines a set of product assurance requirements for the development, reuse and maintenance of integrated circuits such as **ASICs** and **FPGAs**, and for **IP Cores** as reusable building blocks of complex integrated circuits, in space systems.

The objectives of **ASIC**, **FPGA** or **IP Core** product assurance activities are to provide adequate confidence to the customer and to the supplier that the PLD satisfies its requirements throughout the system lifetime. In particular, that the PLD is developed to perform properly and safely in its operational environment, meeting the quality objectives agreed for the project.

## 1.2 Purpose

This guidance defines assurance activities for critical Field-Programmable Gate Array (FPGA) developments in NASA projects. The goal is to outline clear responsibilities for ensuring the quality of PLD products supporting mission success, minimizing costs and delays, and reducing latent failures. Missions should tailor these requirements in collaboration with stakeholders, PLD Subject Matter Experts (SMEs), and other key personnel.

The emphasis is on a high-level framework for PLD standards, with detailed methodologies to be documented in the PLD handbook.

This topic provides a structured, high-level approach to ensure consistency in PLD software assurance across NASA projects, promoting mission success while controlling costs and risks.

## 1.3 Define Leadership Roles and Responsibilities

**Why:** Clear leadership and defined roles within projects and across centers ensure alignment on best practices for safety-critical PLDs.

**Suggestion:** Early in the project development cycle, specify the roles and relationships among PLD developers, Software Assurance SMEs, Hardware Assurance teams, Systems Assurance teams, IV&V, and Cybersecurity specialists. Include mechanisms for oversight, accountability, and collaboration.

## 1.4 Assurance Program-Logical-Device (PLD) tasks tailoring

**Program-Logical-Device (PLD) tasks tailoring** is the process of seeking relief from the PLD standard requirements in a manner consistent with program or project objectives, acceptable levels of risk, and defined constraints. Since PLD developments encompass a wide range of devices, technologies, and engineering contexts, tailoring allows for a flexible yet controlled adaptation of requirements. When PLD standard requirements are tailored, the associated **PLD assurance tasks** may also be tailored, provided such changes are justified, documented, and formally approved.

To provide governance and mitigate risks introduced by tailoring, NASA has established the **Technical Authority (TA) governance model**, which oversees the approval of any changes to PLD requirements. This model ensures that tailoring aligns with project goals, maintains software assurance integrity, and addresses the impact of deviations from baseline requirements.

#### **Levels of PLD Requirements Tailoring**

Tailoring of PLD requirements and assurance activities is governed by a two-level approach for consistency and alignment.

---

### **1. First Level of Tailoring: PLD Standard Tailoring**

The **first level of tailoring** involves adjusting the PLD standard requirements themselves to suit the specific needs of the program or project. This process ensures that the requirements align with the project’s unique objectives, constraints, risk appetite, and use of resources. Key aspects include:

* **Documentation of Justification**: Tailoring must be formally documented, detailing why specific requirements are not applicable or need adjustment for the given project.
* **Risk Considerations**: The tailored requirements must demonstrate that any reduction in scope or deviation from the standard does not introduce unacceptable levels of risk.
* **Approval by Technical Authority**: Final approval is granted by the designated Technical Authority, ensuring governance and consistency with NASA’s quality and safety standards.
* **Compliance with Overarching Standards**: Tailored requirements must remain consistent with higher-level organizational or program policies.

---

### **2. Second Level of Tailoring: Tailoring of PLD Assurance Activities**

The **second level of tailoring** focuses on modifying the **PLD assurance tasks** to align with the tailored PLD engineering activities. This ensures that assurance activities remain proportional, relevant, and synchronized with the project’s tailored requirements. Key aspects include:

* **Alignment with Tailored Engineering Practices**: As the engineering design, verification, and validation tasks are tailored, the assurance tasks are revised to match the scope, complexity, and criticality of the tailored engineering activities.
* **Assurance Risk Management**: During tailoring, the impact on software or hardware assurance coverage is evaluated to ensure risks introduced by tailoring are identified, mitigated, and managed effectively. For example, reducing the scope of verification assurance for a low-risk component may be acceptable if alternative testing compensates for the reduction.
* **Verification of Tailored Requirements**: Tailored assurance tasks must ensure that all tailored requirements are sufficiently verified, validated, and monitored.
* **Approval by Technical Authority**: Tailored assurance tasks must also receive approval through the TA governance model to confirm alignment with the updated PLD requirements.

---

### **Tailoring Governance Model and Process Overview**

Tailoring is governed by a structured process to ensure changes are well-documented, justified, and do not compromise quality, safety, or mission success. The following steps guide the tailoring process:

1. **Identify Tailoring Needs**: Determine which PLD standard requirements or assurance activities require tailoring based on project objectives, constraints, or unique characteristics of the development.
2. **Document Tailoring Requests**: Include rationale, justification, and details of any associated risks. Identify mitigation plans for potential risks introduced by tailoring.
3. **Analyze Impacts**: Evaluate the impacts of tailoring on system reliability, risk levels, schedule, and assurance coverage.
4. **Review and Approval**: The tailoring proposal is submitted to the Technical Authority for review, mitigation planning, and formal approval.
5. **Implement Tailored Requirements**: Incorporate tailored requirements into project plans, process controls, and assurance procedures.
6. **Monitor and Report**: Continuously monitor the implementation and impact of tailored requirements and assurance tasks. Provide updates and results to relevant stakeholders as needed.

---

### **Key Considerations for Tailoring Approval**

* Justification of tailoring should include adequate reasoning, balancing flexibility with acceptable risk.
* The tailoring process must align with program/project governance and comply with NASA’s higher-level engineering guidelines.
* Proactive communication between PLD engineers, assurance personnel, and the technical authority is essential to maintain seamless collaboration and oversight.
* Tailoring decisions must be supported with quantitative or qualitative risk analyses where applicable, ensuring traceability of approvals.

---

### **Conclusion**

The two-level tailoring process—modifying PLD standard requirements at the first level and aligning PLD assurance tasks to those tailored requirements at the second—ensures that projects can adapt to specific needs without compromising quality or safety. By adhering to the NASA **Technical Authority governance model**, tailoring decisions are systematically reviewed and approved to mitigate risks, maintain compliance, and support mission objectives. This structured approach helps projects remain agile while ensuring a robust foundation for development and assurance activities.

# 2. Assurance Activities

## 2.1 Assurance tasks by life cycle stage in a PLD development cycle

### 2.1.1 Planning Stage:

A comprehensive and well-documented approach to planning, documentation, and supplier oversight ensures effective assurance activities and accountability throughout the PLD lifecycle. The following steps should be undertaken to establish and maintain robust plans and ensure proper control over PLD processes:

### **1. Develop and Maintain an Assurance Activities Plan and Resource Estimates**

* Establish a clear and detailed **plan** for assurance activities, ensuring that it encompasses all phases of PLD development, verification, validation, and deployment.
* Include the following in the assurance plan:
  + Key tasks, milestones, and deliverables for assurance activities.
  + Assigned roles and responsibilities for assurance professionals within the project.
  + Integration of supplier assurance tasks and oversight processes.
* Estimate the resources required for assurance (e.g., staffing, tools, schedule, budget) to ensure all assurance activities are adequately supported and completed on time.
* Update the **assurance plan and resource estimates** as the project evolves to account for changes in scope, risks, or requirements.

### **2. Ensure NASA Has Access to Modifiable Source HDL and Project Files**

* Confirm that modifiable **source HDL (Hardware Description Language) code** and associated project files are made accessible to NASA for independent review, analysis, testing, and maintenance.
* Access should include, but is not limited to:
  + HDL source files (e.g., Verilog, VHDL, or SystemVerilog files) that define the PLD behavior.
  + Project configuration files, constraints, and simulation scripts used to create, synthesize, and verify the PLD design.
  + Documentation of the design, including high-level and detailed design specifications, testbench files, and verification collateral.
* Ensure access rights include unrestricted use for assurance and anomaly resolution, emphasizing modifiability to allow for future updates, debugging, or re-verification as needed.
* Establish a **clear agreement with suppliers** delineating the level of access and associated processes to deliver these artifacts to NASA as required.

### **3. Verify That Key Plans Are Documented**

The following essential plans must be created, documented, and reviewed to ensure compliance, accountability, and consistency across the PLD development process:

#### **PLD Verification Plan**

* Validate that a **PLD verification plan** exists, detailing the methodology, environment, tools, and procedures for ensuring the PLD design meets all requirements.
* Key components of the verification plan include:
  + Functional, interface, and timing verification approaches.
  + Unit-level, integration-level, and system-level verification processes.
  + Test coverage metrics and acceptance criteria.
  + The use of simulations, formal methods, and board-level testing in the verification lifecycle.
* Confirm the verification plan includes provisions for addressing:
  + **Safety-critical functions**, with traceability to hazard analyses.
  + Cybersecurity vulnerabilities and protections.
  + Regression testing for iterative implementations or updates.

#### **PLD Development Plan**

* Ensure that a **PLD development plan** is documented, addressing the complete design-to-deployment process. Key elements include:
  + Development phases, milestones, and timelines.
  + A breakdown of design activities, including architecture, coding, synthesis, and implementation.
  + Design review mechanisms at critical milestones (e.g., Preliminary Design Review (PDR), Critical Design Review (CDR), etc.).
  + Integration of dependability, safety, and security requirements into the design process.
* Confirm that the development plan aligns with system-wide schedules and interdependencies to prevent bottlenecks.

### **4. Ensure Proper Delegation and Oversight of PLD Assurance Tasks**

* Confirm that when **suppliers delegate PLD product assurance tasks** to lower-tier suppliers, the process is documented and controlled to maintain quality and accountability across all levels of the supply chain.
* Verify that delegation includes the following controls:
  + Contracts or agreements specifying the delegation scope, responsibilities, and requirements for compliance with agreed processes and standards.
  + Clearly defined mechanisms for reviewing and accepting assurance deliverables from lower-tier suppliers.
  + Evidence that lower-tier suppliers have the capability and resources to perform the delegated tasks, including validated tools and qualified personnel.
* Ensure the primary supplier retains full responsibility for the completion and quality of assurance tasks, regardless of delegation. This includes accountability for:
  + Delivering high-quality, verified PLD designs and assurance documentation to the customer.
  + Mitigating risks associated with lower-tier supplier performance.
* Audit and monitor lower-tier suppliers to verify proper execution of delegated tasks, ensuring traceability throughout the assurance process.

Planning and documentation are foundational elements of a successful PLD development and assurance framework. Maintaining a well-defined assurance activity plan with accurate resource estimates, ensuring access to modifiable HDL source code, and verifying documented plans for verification and development are critical steps. Additionally, establishing clear controls and accountability for delegated assurance tasks ensures that quality, safety, and dependability are preserved across all levels of the supply chain. Together, these actions provide a structured and transparent foundation for delivering high-quality PLD products while managing program risks effectively.

### 2.1.2 Development Stage:

The following steps ensure that the development of Programmable Logic Devices (PLDs) aligns with quality, safety, dependability, and cybersecurity criteria, while establishing robust foundations for successful implementation and maintenance throughout the project lifecycle.

### **1. Confirm that a Detailed PLD Specification Is Produced**

* Verify that a complete and detailed PLD specification is developed, including all hardware, software, and interface requirements.
* The specification must define functional behaviors, performance requirements, timing constraints, and operational scenarios, ensuring traceability to higher-level system and mission requirements.
* Ensure that the specification includes documentation of assumptions, boundary conditions, and any constraints relevant to the PLD design.

### **2. Assess the PLD’s Safety-Critical Status Based on System Hazard Analysis Traceability**

* Review system-level **hazard analyses** and verify traceability to PLD components to determine whether the PLD includes **safety-critical functionality**.
* Evaluate interactions between the PLD and other system components to identify potential design or operational risks related to:
  + Failure propagation paths.
  + Risks introduced at the PLD subsystem level.
* Confirm that safety mitigations and redundancies are defined for PLD-critical functions and are consistent with system-level safety requirements.

### **3. Ensure the Supplier Conducts PLD-Level Dependability and Safety Analyses**

* Confirm that the PLD supplier performs a **dependability and safety analysis** at the PLD level. This analysis should leverage system-level dependability and safety data to determine:
  + The criticality of each PLD function.
  + Failure modes, their potential effects, and mitigations (e.g., Fault Tree Analysis (FTA), Failure Modes, Effects, and Criticality Analysis (FMECA)).
  + Reliability targets and testability of critical functionality.
* Verify the results of these analyses are documented and inform both PLD design and assurance activities.

### **4. Verify That Cybersecurity Risks Are Identified and Appropriately Managed**

* Confirm that cybersecurity risks associated with the PLD are assessed as part of the overall mission or project cybersecurity analysis.
* Ensure that the PLD design incorporates security techniques, such as:
  + **Access controls** to protect programming and operational states.
  + Secure communication protocols for PLD interfaces.
  + Encryption schemes for critical data handled by the PLD.
* Validate that security risks are tracked and mitigation strategies are tested and implemented throughout the development lifecycle.

### **5. Confirm That Design Margins Are Defined and Supported by Data at Each Milestone**

* Review the definition of **design margins** (e.g., timing, power, thermal) at major project milestones to ensure they account for operating conditions, variability, and potential degradation over time.
* Verify that margins are explicitly quantified and supported by data collected from:
  + Calculations and simulations (e.g., timing analysis, thermal modeling).
  + Preliminary hardware testing when available.
* Ensure that the progression of design margins is monitored during development and remains within acceptable risk thresholds as the design matures.

### **6. Ensure Validation and Accreditation of PLD Tools**

* Confirm that all tools used in the creation, maintenance, and verification of the PLD (e.g., simulation software, synthesis tools, programming tools) are **validated** and **accredited** for use in the project.
* Review tool validation records to confirm:
  + Evidence that tools operate as intended and produce correct, repeatable results.
  + Any known tool limitations or risks are documented and mitigated.
* Ensure traceability of tool usage to the final delivered PLD to avoid introducing risks due to incorrect or inappropriate tooling.

### **7. Confirm That a PLD Design Architecture Is Developed**

* Validate that a detailed and well-documented **PLD design architecture** has been created, incorporating:
  + **High-level block diagrams** that explain subsystem interactions and data flows.
  + Detailed descriptions of the PLD's functional modules, behavioral specifications, and structural hierarchy.
  + Adequate consideration of constraints, such as timing, logic utilization, and power consumption.
* Verify that the architecture addresses both critical (e.g., safety, dependability) and non-critical functionality with appropriate prioritization.

### **8. Ensure Procedures Exist for Logging, Analysis, and Correction of Problems Encountered During PLD Development**

* Confirm that the development process includes **formalized procedures** for tracking and resolving PLD-related issues encountered during development.
  + Logs should capture detailed records of all identified problems, including the context, severity, and potential impacts.
  + Analysis procedures should prioritize root cause identification.
* Verify that mitigation or corrective actions are implemented, tested, and documented to confirm their effectiveness.
* Ensure that issue trends are evaluated to identify systemic problems or improvements to the overall PLD development process.

A rigorous and structured approach to PLD design, testing, and validation ensures that safety, dependability, and cybersecurity risks are effectively managed and that all requirements are traceable and verifiable at every stage. By confirming deliverables such as detailed specifications, validated tools, dependable architectures, and robust problem-tracking mechanisms, the development process establishes operational resilience for even the most critical PLD components. Integrating supplier and system-level analyses into PLD development further ensures alignment with mission-critical objectives..

### 2.1.3 Testing Stage:

The **Testing Stage** is crucial for validating that the programmable logic device (PLD) meets all specified requirements, performs as intended, and addresses critical concerns such as security, timing, and functionality. This stage integrates **simulation-based testing** and **board-level testing** to ensure thorough and reliable verification of PLD designs. The following tasks and considerations should guide the testing effort:

#### **1. Validate that PLD Testing Thoroughly Verifies the PLD Specification**

* Ensure comprehensive PLD testing covers all functional, timing, and interface requirements as defined in the PLD specification.
* Use **simulation tools** (e.g., ModelSim, Synopsys VCS) to verify functionality under multiple scenarios, including expected operating conditions, corner cases, and stress conditions.
* Perform **board testing** to validate PLD behavior in a real hardware context, ensuring that the PLD integrates seamlessly with other system components and performs as intended in its operational environment.

#### **2. Confirm that Testing Data Demonstrates Timing Requirements Are Met with Adequate Margin**

* Simulations should perform **timing analysis** to verify that timing constraints (e.g., setup, hold, propagation delays) are satisfied with sufficient margins under all operating conditions.
* Use **board-level testing** to validate timing performance in real-world hardware, ensuring no timing violations exist due to board-level factors (e.g., signal integrity issues, PCB trace delays).
* Provide documented evidence from both simulation and board testing to confirm the PLD timing analysis aligns with requirements.

#### **3. Verify Proper Version Descriptions Are Documented for Each PLD Release**

* Maintain detailed **version control** documentation for each release of the PLD, including changes made, test results, and any known defects.
* Ensure consistency between simulation models, synthesis outputs, and the hardware implementation during version transitions.

#### **4. Confirm That PLD Requirements Validation Activities Are Completed**

* Verify that all PLD requirements are validated through a combination of:
  + **Simulation-based testing**: Ensure functional, timing, and safety-critical requirements are validated via simulations covering a broad spectrum of conditions.
  + **Board-level testing**: Confirm that the PLD's actual physical implementation meets system-level requirements.
* Provide an end-to-end traceability matrix linking test cases to corresponding PLD requirements.

#### **5. Review Untested PLD Features and Agree on Rationale for Exceptions**

* Identify any PLD features that remain untested, document the rationale for excluding those tests, and ensure agreement with all stakeholders (e.g., project leads, technical authorities).
* Address untestable or hard-to-test features during the review process, ensuring no critical risks are overlooked.

#### **6. Ensure PLD Security Concerns Are Adequately Addressed**

* Validate that PLD testing includes scenarios to evaluate security-related requirements such as:
  + Protection against unintended access or tampering.
  + Validation of secure boot processes or encryption mechanisms, where applicable.
* Use board-level testing to confirm that security features remain robust in real hardware implementation.

#### **7. Confirm That Procedures Exist for Logging, Analysis, and Correction of PLD Problems Encountered During Testing**

* Establish formal procedures for:
  + Logging issues found during **simulation-based testing** (e.g., testbench discrepancies, uncovered corner cases).
  + Logging issues identified during **board-level testing** (e.g., unexpected hardware behavior, signal integrity problems).
* Ensure clear workflows for **analysis** (root cause identification) and **correction** of detected PLD problems.
* Implement feedback loops to improve test coverage for both simulations and board testing, reducing the likelihood of repeating issue-related gaps.

**Integration of Simulation and Board Testing**

To enhance the robustness of PLD testing, the process must integrate **simulation-based** and **board-level** techniques, ensuring thorough validation and coverage of all requirements and risks:

#### **Simulations**

* **Role**: Simulations validate the PLD design's logical functionality before hardware implementation. These tests are faster, cover a wide range of use cases, and allow easy repeatability.
  + Perform **functional simulations** to validate the correctness of the design for specified use cases.
  + Conduct **timing simulations** to verify that the design meets timing constraints under all conditions (e.g., worst-case delays, temperature extremes).
  + Test for **stress cases** or unusual conditions (e.g., rare input sequences, edge cases) that may not be feasible to test in hardware.

#### **Board Testing**

* **Role**: Board-level testing ensures real-world performance of the PLD in its intended environment. This step accounts for hardware imperfections and interactions with other system components.
  + Conduct **system-level testing** to verify proper communication between the PLD and other hardware components.
  + Perform **power-on tests**, **environmental testing** (temperature ranges, vibrations, etc.), and **signal integrity analysis** to validate robustness.
  + Test for **physical timing design limits**, ensuring proper behavior without degradation in actual hardware.

Simulations and board testing are complementary processes that together form a comprehensive PLD testing strategy. Simulation identifies logical or functional flaws early in the lifecycle, while board testing ensures real-world operability and reliability. The dual approach mitigates risks and improves confidence in PLD quality.

### 2.1.4 Auditing:

Auditing is a critical activity in Programmable Logic Device (PLD) development, ensuring that engineering processes comply with established standards, requirements, and best practices. Effective audits provide oversight, enhance traceability, and promote quality across the PLD lifecycle. The following steps outline key auditing tasks for PLD developments:

### **1. Audit Engineering Processes to Ensure Adherence to Standards**

* Conduct regular audits of **PLD engineering processes** to verify conformity with relevant standards, including NASA's PLD development guidelines, industry best practices, and system-level quality requirements.
* Focus audits on key aspects of the PLD lifecycle, including:
  + Requirements definition.
  + Design and architecture development.
  + Verification and validation activities.
  + Safety, dependability, and security analyses.
* Evaluate whether the PLD team follows documented procedures for simulations, board testing, risk assessments, and traceability.
* Identify gaps or deviations from standards and initiate corrective actions to address non-conformances.
* Ensure audit findings are documented and communicated to program leadership for continuous improvement.

### **2. Verify Configuration Management Records Are Maintained for the PLD Design**

* Confirm that the **configuration management system** for the PLD design is implemented and actively maintained throughout development.
* Review records to ensure they include:
  + Version-controlled source HDL (Hardware Description Language) files.
  + Synthesis outputs and constraints files associated with specific design iterations.
  + Documentation of any changes to the design, including reasons for changes and approval records.
  + Test results, including simulation and board-level testing, tied to corresponding PLD versions.
* Audit the consistency between configuration records and the physical hardware implementation of the PLD to verify correctness and traceability.
* Ensure that disaster recovery measures (e.g., backups, redundancy) are in place to safeguard PLD design data and configuration records.

### **3. Confirm That a Requirements Compliance Matrix Is Documented**

* Verify that the PLD team has developed and maintained a **requirements compliance matrix**, demonstrating adherence to applicable standards and requirements.
* Review that the matrix includes:
  + Mapping of each PLD requirement to corresponding sections of the applicable standards or contractual obligations.
  + Results of verification activities (e.g., simulations, test executions) showing compliance for each requirement.
  + Notes on compliance exceptions, with documented rationale and mitigation measures for any partially satisfied or waived requirements.
* Confirm that the compliance matrix is reviewed and updated at key milestones (e.g., Preliminary Design Review (PDR), Critical Design Review (CDR)) to reflect progress and changes in the PLD design.
* Use the compliance matrix as a basis for audits to identify gaps, confirm completeness, and assess adherence.

### **4. Additional Auditing Considerations**

Beyond the core tasks, auditing may include the following supplemental activities to strengthen oversight and ensure robust PLD development:

* **Tool Validation Audit**: Verify that tools used in PLD development (e.g., simulation, synthesis, validation tools) are accredited and validated prior to use, ensuring they produce reliable outputs.
* **Supplier Audit**: Evaluate supplier compliance with delegated assurance tasks to ensure traceability in multi-tier supply chains.
* **Safety and Security Audits**: Validate that safety-critical functions and cybersecurity measures in the PLD design comply with system-level safety and security requirements.

Auditing in PLD development focuses on ensuring adherence to standards, maintaining robust configuration management, and validating requirements compliance. By verifying engineering processes, configuration records, and compliance matrices at regular intervals, audits promote accountability, reduce risks, and enhance project transparency. Through continuous auditing, the team can proactively identify areas for improvement, align all activities with organizational and mission standards, and deliver high-quality PLD design

### 2.1.5 Milestone Reviews:

Milestone reviews are essential checkpoints in PLD development, ensuring that progress aligns with project requirements, quality standards, and mission objectives while addressing critical issues, such as safety, reliability, and environmental factors. The following tasks define how milestone reviews should be structured and evaluated to achieve optimal project outcomes:

### **1. Verify Project Milestones Include Defined and Documented Reviews of Developer Progress**

* Ensure that all critical milestones (e.g., Concept Development, Preliminary Design Review (PDR), Critical Design Review (CDR), Test Readiness Review (TRR)) have been defined, scheduled, and documented in the project timeline.
* Each milestone review should include:
  + A clear set of **entry and exit criteria**, tied to project deliverables and performance benchmarks.
  + Assessments of progress against the PLD development plan, verification plan, and resource estimates.
  + Identification and resolution of outstanding risks, issues, or anomalies.
* Confirm the availability of review artifacts, such as updated PLD requirements traceability matrices, test plans, functional verification results, and design documentation.
* Ensure milestones are treated as opportunities to assess the readiness of the PLD design to progress to the next development phase.

### **2. Ensure a Plan Exists for Safe In-Flight PLD Reconfiguration (If Required)**

* For missions where **in-flight PLD reconfiguration** is required:
  + Confirm the existence of a detailed, documented plan for performing PLD updates or reconfigurations during the mission without endangering the system or compromising its operation.
  + Verify that the reconfiguration plan includes mitigation measures for potential issues, such as incomplete reconfigurations, corruption, or system-level vulnerabilities during the update process.
  + Ensure the design incorporates features such as:
    - **Fallback mechanisms**: Safe recovery paths or rollbacks in the event of reconfiguration failure.
    - **Redundant PLD configurations**: Backup designs that can be activated as a failsafe.
  + Verify that **ground-based testing** at the system level confirms the reliability, timing, and safety of the in-flight reconfiguration process prior to launch.
* Ensure that the reconfiguration plan is well-integrated and aligned with overall mission requirements and operational procedures.

### **3. Confirm Design Addresses Radiation Concerns for the PLD Device**

* Review the **radiation hardening strategy** for the PLD device, ensuring that the design can operate reliably in the expected space or environmental conditions. Key considerations include:
  + **Mitigation of Single Event Effects (SEE)** such as Single Event Upsets (SEU), Single Event Transients (SET), or Single Event Latchups (SEL).
  + **Tolerance to Total Ionizing Dose (TID)**: Verify radiation test data for the PLD device against mission radiation environment profiles and ensure sufficient operational margins.
  + Use of techniques such as:
    - Triple Modular Redundancy (TMR) or other fault-tolerant architectures.
    - Error Detection and Correction Codes (EDAC) for memory reliability.
    - Hardened or radiation-tolerant PLD designs/components where necessary.
* Confirm radiation-related design decisions are documented and supported by simulation, analysis, or test data. Ensure this documentation is reviewed at key milestones (e.g., Radiation Review Boards).
* Track radiation-related issues or residual concerns and resolve them before critical project milestones.

### **4. Actively Participate in Project Milestone Reviews**

* Actively engage with PLD developers and project management teams during milestone reviews by:
  + Providing **technical and assurance input** on design progress, testing results, and risk mitigation efforts.
  + Reviewing and confirming the completion of milestone entry/exit criteria and alignment with the PLD development plan and mission objectives.
  + Evaluating supplier performance and ensuring their adherence to delegated responsibilities and documented standards.
  + Raising relevant questions or concerns during reviews to ensure comprehensive evaluation of the design's readiness.
* Ensure that findings or recommendations from milestone reviews are logged and addressed through a feedback loop, contributing to continuous improvement in subsequent development phases.
* Collaborate with cross-disciplinary teams, including hardware, software, system, and mission assurance teams, to ensure a holistic approach to milestone evaluations.

Milestone reviews enable the PLD development team to evaluate progress and address technical, safety, and environmental concerns at well-defined checkpoints. By verifying that reviews are documented and include plans for critical aspects such as in-flight reconfiguration and radiation resilience, these reviews ensure the readiness of the PLD to meet mission requirements. Active participation from stakeholders during milestone reviews fosters accountability, mitigates risks, and ensures that any identified issues are resolved before advancing to subsequent development phases. Through rigorous milestone reviews, the PLD development process becomes more predictable, reliable, and aligned with mission-critical objectives.

## 2.2 If the PLD is Safety-Critical

Safety-critical functions within Programmable Logic Devices (PLDs) require rigorous verification to ensure the device's reliability and its ability to mitigate hazards during operation. A thorough and systematic approach to testing and verification of safety-critical designs is essential to maintain system safety and compliance with mission and system-level safety requirements.

### **1. Validate the Inclusion of Safety-Critical Function Verification in the PLD Test Plan**

* Confirm that the **PLD test plan** explicitly identifies and includes all **safety-critical functions** derived from the design's safety analysis and functional requirements.
* Verify the incorporation of appropriate test cases for:
  + Normal operation scenarios.
  + Off-nominal conditions, fault injection tests, and edge cases to evaluate the design's ability to prevent or mitigate hazards.
* Ensure the test plan defines the methodology and criteria for verifying that each safety-critical function meets its intended behavior under all specified conditions.

### **2. Ensure Hazard Controls, Including Off-Nominal Scenarios and Interfaces, Are Adequately Tested**

* Verify that tests include evaluation of **hazard controls** defined for the PLD functionality to handle both:
  + Nominal scenarios (normal operation) where hazards are managed as part of standard operation.
  + **Off-nominal scenarios**, including situations outside nominal operating ranges, to ensure hazards are mitigated during failures, environmental extremes, or unexpected conditions (e.g., power anomalies, timing violations).
* Confirm that interface testing includes all safety-critical hardware and software integrations, evaluating:
  + Communication between the PLD and other system components.
  + The ability of the PLD to respond appropriately to system- or operator-mitigated fault conditions.

### **3. Verify That All Safety-Critical HDL Code Is Fully Tested**

* Confirm that **safety-critical HDL (Hardware Description Language) code** is fully exercised through simulation, functional testing, and on-device validation:
  + Simulations should test the code under a wide range of normal, off-nominal, boundary, and stress conditions.
  + On-device testing should verify that the synthesized hardware matches expected functional behavior.
* Validate that test results are documented, including pass/fail criteria for each safety-critical verification step.
* Ensure traceability between safety-critical HDL code and associated test coverage in simulation and hardware-testing environments.

### **4. Confirm 100% Test Coverage for Safety-Critical PLD Designs**

* Verify that test coverage analysis is performed to achieve 100% coverage for safety-critical PLD functions, including:
  + **Code coverage** (e.g., line coverage, toggle coverage, state coverage).
  + **Functional coverage**, ensuring all safety-specific behaviors and scenarios are tested.
* Confirm that testing environments include:
  + **Fault injection tests** to examine how safety-critical designs respond to unexpected or hazardous inputs and conditions.
  + Coverage of both normal and off-nominal operations.

#### **If Full Test Coverage Is Unattainable:**

* Validate that developers provide a **rationale or risk assessment** explaining why 100% coverage could not be achieved.
* Ensure the rationale:
  + Is technically justified.
  + Identifies gaps in coverage and specifies residual risks.
* Review the risk assessment to confirm its acceptability, ensuring that any decision to proceed with incomplete test coverage is documented and approved by the relevant safety authorities.

### **5. Verify Documentation of Safety Constraints, Controls, and Mitigations**

* Confirm that all **safety constraints, controls, mitigations, and dependencies** are thoroughly documented, including interactions between:
  + The PLD hardware.
  + Operators and system-level controls.
  + Associated software components.
* Ensure that safety documentation:
  + Clearly defines roles and responsibilities for mitigating hazards.
  + Describes the interfaces and coordinated efforts between hardware and software to maintain system safety during operations.
  + Provides traceability from safety analyses to specific design and test artifacts.

### **6. Confirm That Safety-Critical Requirements Are Documented in Development and Test Plans**

* Ensure that **safety-critical requirements** are explicitly documented in both:
  + The development plan: Clearly defining design priorities and safety-critical workflows.
  + The test plan: Identifying tests and verification steps necessary to validate compliance with safety-critical requirements.
* Verify consistency between system-level safety analyses, derived PLD requirements, and their inclusion in the development and test plans.

### **7. Ensure PLD Safety-Critical Requirements Are Derived from Safety Analysis**

* Confirm that all **PLD safety-critical requirements** arise directly from safety analyses conducted at the system and subsystem levels.
* Validate that these requirements address:
  + Identified hazards.
  + Risk mitigations for potential hardware and software interactions.
  + Mission-specific safety features required for reliability and redundancy.
* Cross-check safety requirements against initial hazard analysis documentation to ensure completeness and traceability.

Thorough and systematic verification of safety-critical PLD functions is essential for mitigating hazards and ensuring system reliability. By ensuring comprehensive test plans, off-nominal scenario testing, complete documentation of safety-related constraints, and a strong connection between design and system-wide safety analyses, the development process prioritizes the robust implementation of safety-critical functions. Rigorous adherence to 100% test coverage principles (or documented justifications for exceptions) ensures the credibility and reliability of safety-critical designs, reducing mission risk and maintaining compliance with stringent safety standards.

## 2.3 Risk and Issue Reporting

Effective communication and timely feedback are critical to mitigating risks and addressing issues during PLD development. By proactively engaging with the project team and PLD developers, risk resolution becomes faster, more efficient, and better aligned with mission goals. The following practices ensure structured, actionable, and impactful feedback:

### **1. Deliver Feedback Promptly and in the Appropriate Context**

* **Act early**: Provide feedback on identified risks and issues as soon as they are detected, ensuring they are addressed before they escalate or impact critical milestones.
* Tailor feedback to the **context of the development phase** (e.g., design, verification, integration) so the team can prioritize and act on it based on the current project stage.
* Categorize feedback by severity:
  + **Critical risks**: Require immediate action and resolution to avoid compromising safety, performance, or reliability.
  + **Moderate risks**: Require planned mitigations before the next milestone or phase.
  + **Low-level observations**: Suggestions for improvement or future monitoring.

### **2. Ensure Feedback Is Clear, Actionable, and Data-Backed**

* **Clarity**: Communicate feedback in a concise and unambiguous manner, explicitly stating the nature of the risk, its potential impact, and its relationship to PLD requirements or standards.
* **Actionable guidance**: Include specific recommendations for mitigating the identified risks or addressing the issues. Example:
  + Instead of: “Timing margin seems insufficient,” provide: “Simulations show a timing violation in Module A under condition X. Investigate increasing pipeline stages or relaxing timing constraints.”
* **Data-backed feedback**: When possible, provide supporting evidence (e.g., simulation results, test data, failure analyses, or compliance gaps) to give developers a clear rationale for acting on the feedback.

### **3. Establish a Continuous Feedback Loop**

* Facilitate an **iterative feedback loop** with the PLD development team:
  + Continually monitor progress to confirm that identified risks and issues are being addressed in a timely manner.
  + Provide updated feedback based on subsequent evaluations, further analysis, or resolution measures.
* Utilize routine project meetings, milestone reviews, or informal check-ins to provide ongoing clarification and refinement of feedback.
* Promote open dialogue to allow developers to query or challenge feedback constructively, ensuring shared understanding and alignment on resolutions.

### **4. Collaborate Across Teams to Accelerate Issue Resolution**

* Engage relevant stakeholders, including system architects, software teams, safety engineers, and assurance personnel, when providing feedback that affects broader system interactions or cross-disciplinary areas.
* Offer feedback in a collaborative manner to foster shared responsibility for resolving risks. This encourages a whole-systems perspective and prevents siloed solutions that could introduce secondary risks.

### **5. Track and Resolve Feedback in a Controlled Manner**

* **Document feedback** systematically using a project issue-tracking tool or risk register, associating each item with:
  + A unique identifier for traceability.
  + The specific PLD component, module, or function affected.
  + Proposed actions and deadlines for resolution.
* **Verify resolution**: Confirm that corrective actions or mitigations are fully implemented and verified before closing out risks or issues associated with the feedback.

Providing timely, clear, and actionable feedback on PLD development risks and issues is central to maintaining project momentum and achieving design reliability. By tailoring feedback to specific risks, basing it on data, fostering collaboration, and tracking resolution, the feedback process becomes an integral part of risk management. This continuous and structured approach ensures that the PLD development stays on track while mitigating risks proactively and effectively.

# 3. Assurance for Ground PLD or Research Development

No assurance activities are required for PLD development associated with ground or research purposes.

# 4. Key Areas for Strengthening the Guidance

The provided guidance outlines a clear and concise framework for assurance activities related to PLD development. Building on this, here are some additional thoughts and recommendations to refine NASA's approach to assurance for PLDs:

## 4.1 Define Leadership Roles and Responsibilities

* **Why:** Clear leadership and defined roles within projects and across centers ensure alignment on best practices for safety-critical PLDs.
* **Suggestion:** Early in the project development cycle, specify the roles and relationships among PLD developers, Software Assurance SMEs, Hardware Assurance teams, Systems Assurance teams, IV&V, and Cybersecurity specialists. Include mechanisms for oversight, accountability, and collaboration.

## 4.2 Promote Cross-Center Knowledge Sharing:

* **Why:** The lack of a standardized approach stems partly from NASA centers working independently on PLD processes. A culture of shared learning can drive consistency.
* **Suggestion:** Encourage the creation of a centralized PLD knowledge-sharing repository for best practices, lessons learned, and example artifacts (e.g., PLD verification plans, development plans, RCA examples).

## 4.3 Introduce Training on PLD-Specific Software Assurance:

* **Why:** Confusion between software and PLDs has been identified as a key challenge. A baseline training program is essential to bridge this gap.
* **Suggestion:** Develop and provide periodic mandatory training for developers, assurance personnel, and other stakeholders regarding:

+ The unique aspects of PLDs (e.g., HDLs, FPGA design flow, timing analysis).
+ The differences and overlaps between software and PLD assurance.
+ Safety-critical and cybersecurity considerations specific to PLDs.

## 4.4 Enhance Cybersecurity Guidance:

* **Why:** PLD cybersecurity risks are increasingly critical, especially in contexts involving reconfigurable FPGAs and external interfaces, such as space communications systems.
* **Suggestion:**

+ Augment the cybersecurity assurances to include hardware-backed security mechanisms within PLDs.
+ Mandate testing to detect and mitigate any malicious impacts on PLD performance.
+ Include PLD supply chain/vendor risk considerations to guard against counterfeit or vulnerable components.

## 4.5 Focus on Early Hazard Identification and Risk Management:

* **Why:** Late-stage hazard findings (or lack of safety integration) can lead to costly design rework.
* **Suggestion:** Expand the existing guidance to require:

+ Hazard analysis during concept and specification stages of PLD development.
+ Early identification of safety-critical PLD features to embed mitigations upfront.
+ Leveraging formal methods (if appropriate) to verify compliance with safety constraints.

## 4.6 Incorporate Metrics to Monitor Process Effectiveness:

* **Why:** Metrics will help ensure that assurance activities for PLDs are yielding the intended results.
* **Suggestion:** Examples of metrics to track include:

+ Testing coverage percentage achieved for safety-critical PLD components.
+ Number and severity of defects identified at various stages of development (e.g., specification, integration, testing).
+ Adherence to milestone schedules for reviews and audits.
+ Number of lessons learned incorporated into subsequent projects.

## 4.7 Consider PLD Toolchain Evolution:

* **Why:** PLD design tools, synthesis algorithms, and associated verification software are evolving rapidly. Without validation and accreditation, these tools could introduce errors.
* **Suggestion:** Establish regular reviews and accreditation timelines for FPGA toolchains. Evaluate tools for:

+ Reproducibility of results.
+ Potential constraints or limitations stemming from Commercial Off-The-Shelf (COTS) tools.
+ Compliance with NASA-specific assurance needs.

## 4.8 Standardizing Deliverables and Artifacts Across NASA Centers:

* **Why:** Inconsistencies between centers can lead to duplicated efforts and quality variance in project outcomes.
* **Suggestion:** Develop a baseline list of required deliverables/artifacts from PLD projects, such as:

+ PLD design plans (with milestones and metrics).
+ Safety-critical hazard analyses and validation results.
+ Cybersecurity risk management plans.
+ Test reports (including requirement validation and timing verification data).

## 4.9 Include PLDs in Broader System Integration Testing:

* **Why:** PLDs are often deeply embedded in larger systems. Failures often occur when PLDs are integrated into the entire system.
* **Suggestion:** Require comprehensive system-level tests to evaluate how PLD functionality interacts with software, hardware, and human operators across both nominal and off-nominal scenarios.

## 4.10 Periodic Updates to the PLD Assurance Framework:

* **Why:** As mission technologies evolve (e.g., deep space exploration, autonomous systems, and reuse of radiation-resistant designs), a static assurance framework may become obsolete.
* **Suggestion:** Plan periodic reviews of the PLD assurance processes and standards to ensure they align with industry advancements, regulatory updates, and emerging risks

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-686)

  [Programmable Logic Devices (PLD) Handbook](https://standards.nasa.gov/standard/nasa/nasa-hdbk-4008 "Click to open in new window")

  NASA-HDBK-4008, Revision: Baseline w/CHANGE 1, Document Date: 2013-12-02

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
|  |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only).

| SPAN Links |
| --- |
|  |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
|  |
