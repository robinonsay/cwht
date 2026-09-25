# SWE-034 - Acceptance Criteria

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695413. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria

SWE-034 - Acceptance Criteria

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695413)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695413&showCommentArea=true&showComments=true#addcomment)

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

3.1.5 The project manager shall define and document the acceptance criteria for the software. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-034 History

SWE-034 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.5.3 The project shall define and document or record the acceptance criteria and conditions for the software. |
| Difference between A and B | No change |
| B | 3.12.3 The project manager  shall define and document the acceptance criteria and conditions for the software. |
| Difference between B and C | Removed "conditions" from requirement. |
| C | 3.1.5 The project manager shall define and document the acceptance criteria for the software. |
| Difference between C and D | No change |
| D | 3.1.5 The project manager shall define and document the acceptance criteria for the software. |

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

Acceptance criteria synchronize the visions of the client and the development team. They ensure that everyone has a common understanding of the requirements: Developers know exactly what kind of behavior the feature must demonstrate, while stakeholders and the client understand what's expected from the feature.

This requirement guarantees that acceptance criteria are **defined, documented, and aligned** with mission objectives, stakeholder expectations, and safety requirements. By mandating formal criteria, the project manager ensures software readiness is objectively evaluated, risks are proactively managed, compliance standards are met, and communication across stakeholders is improved. **In mission-critical environments like aerospace, this structured approach is vital for ensuring safe, reliable, and successful software deployment**.

This requirement is critical for ensuring that aerospace software meets **mission objectives**, **operational requirements**, **stakeholder expectations**, and **safety standards**. By defining and documenting acceptance criteria, the project manager establishes a clear, measurable, and objective basis for evaluating whether the software is ready for deployment.

**Key Reasons Why This Requirement Matters**

1. **Clarity in Expectations**: Establishes a clear definition of acceptable software outcomes to prevent misunderstandings or disputes.
2. **Measurable Validation**: Enables objective and repeatable testing processes for software readiness.
3. **Mission Objectives Protection**: Ensures the software meets critical goals and safety requirements.
4. **Regulatory Compliance**: Provides criteria for meeting certification and regulatory requirements.
5. **Focus for Testing**: Facilitates comprehensive testing and validation processes tied to specific criteria.
6. **Risk Management**: Helps identify and mitigate risks before acceptance.
7. **Accountability**: Provides a formal benchmark for evaluating deliverables and ensuring team accountability.
8. **Change Management**: Supports controlled adaptation of criteria to reflect changes in project scope or requirements.
9. **Stakeholder Collaboration**: Improves communication and alignment across teams, vendors, auditors, and users.
10. **Deployment Readiness**: Confirms the software’s readiness for operational use, ensuring safety and reliability.

Below is the rationale for this requirement:

## 2.1 Establishing Clear Expectations

* **Why It Matters**:
  + Defining acceptance criteria ensures that all stakeholders (e.g., project teams, customers, end users) have a shared understanding of what constitutes a "completed" software product. Without clear criteria, disagreements or confusion about deliverables could arise during the acceptance process.
  + Acceptance criteria outline exactly what functionality, performance, reliability, and compliance the software must meet to be considered successful.
* **Rationale**:
  + Documented criteria eliminate ambiguity by creating a shared understanding of deliverables and outcomes, improving alignment between project teams and stakeholders.

## 2.2 Ensuring Measurable Validation

* **Why It Matters**:
  + Acceptance criteria provide measurable and testable standards to evaluate the software. This includes functional performance metrics (e.g., "software must process telemetry data within X milliseconds"), compliance standards (e.g., "must meet DO-178C DAL-A requirements"), and environmental requirements (e.g., "software must operate in microgravity conditions").
  + Without measurable criteria, acceptance becomes subjective, and critical defects or gaps may remain unidentified.
* **Rationale**:
  + Measurable acceptance criteria allow objective testing and validation of the software, ensuring gaps in functionality or compliance are addressed before deployment.

## 2.3 Safeguarding Mission Objectives

* **Why It Matters**:
  + Aerospace missions are high-risk endeavors where software reliability is paramount. Defining acceptance criteria ensures the software meets risk, safety, and mission-critical functionality requirements. For example:
    - Safety-critical systems (e.g., automated abort functionality or hazard detection).
    - Mission operations (e.g., navigation, data transmission to ground systems).
    - Operational resilience in unforeseen scenarios (e.g., handling input errors, equipment malfunctions).
  + Failure to define these critical thresholds risks deploying software that compromises mission success or human safety.
* **Rationale**:
  + Acceptance criteria act as a safeguard to confirm that the software supports all mission-critical goals and safety standards required for operational success.

## 2.4 Supporting Regulatory and Certification Requirements

* **Why It Matters**:
  + Aerospace software must comply with stringent regulatory standards, such as:
    - DO-178C (Software Considerations in Airborne Systems): Verification methods tied to software levels of criticality.
    - NASA NPR 7150.2D: Software engineering requirements.
    - Agency-specific directives for cybersecurity, functional performance, and reliability.
  + Acceptance criteria document the compliance standards that the software must meet, providing traceability for audits and reviews.
* **Rationale**:
  + Documenting acceptance criteria ensures compliance requirements are formally addressed, facilitating certifications, regulatory approvals, and stakeholder confidence.

## 2.5 Streamlining the Testing Process

* **Why It Matters**:
  + Acceptance criteria serve as the foundation for test cases by explicitly outlining the conditions under which the software is deemed acceptable. For example:
    - Defining functional tests for expected behaviors.
    - Specifying edge cases to confirm robustness under off-nominal conditions.
    - Detailing performance thresholds (e.g., memory usage or execution timing).
  + Without defined acceptance criteria, testing efforts may become unfocused or inconsistent, risking overlooked defects or gaps in validation.
* **Rationale**:
  + Established criteria streamline testing and validation processes by directly connecting tests to measurable requirements, ensuring the software is thoroughly examined before acceptance.

## 2.6 Managing Risk and Contingencies

* **Why It Matters**:
  + Defining acceptance criteria proactively identifies critical metrics that must be met to reduce risk and address contingencies. Examples include:
    - How the software handles unexpected sensor data or system faults.
    - Minimum requirements for cybersecurity protection against attacks.
    - Recovery expectations in the event of software failure or reboot.
  + Acceptance criteria establish thresholds for risk mitigation and define how failure conditions are managed and tested.
* **Rationale**:
  + Criteria ensure that risk areas are fully addressed during evaluation and testing, providing confidence that failure scenarios have been mitigated.

## 2.7 Improving Accountability

* **Why It Matters**:
  + Acceptance criteria provide a formal basis for holding project teams accountable during development. By documenting these standards, it becomes clear when:
    - Deliverables are incomplete, missing functionality, or failing to meet required thresholds.
    - Certain modules or components require corrective action before acceptance.
    - Performance defects prevent the software from achieving operational goals.
  + The criteria are a documented benchmark by which team performance and deliverables can be objectively evaluated.
* **Rationale**:
  + Accountability is improved by using documented criteria to prevent disputes or misaligned expectations during the acceptance process.

## 2.8 Supporting Change Management

* **Why It Matters**:
  + In aerospace projects, mission requirements evolve for a variety of reasons (e.g., new regulations, stakeholder demands, or technical challenges). Accepted changes to software functionality or scope must be reflected in the updated acceptance criteria.
  + Maintaining documented acceptance criteria allows the project manager to adapt to changing needs while ensuring clarity and alignment across all affected teams.
* **Rationale**:
  + Acceptance criteria provide a structured way to manage changes, ensuring evolving requirements are smoothly incorporated without introducing ambiguity or additional risks.

## 2.9 Facilitating Communication Across Stakeholders

* **Why It Matters**:
  + Aerospace projects involve collaboration across diverse stakeholders, including:
    - Internal project teams (e.g., software developers, systems engineers).
    - External vendors and contractors.
    - Regulatory agencies and auditors.
    - End-users (e.g., astronauts, mission operators, ground control teams).
  + Documented acceptance criteria serve as a communication tool, ensuring all parties clearly understand what constitutes software readiness and success.
* **Rationale**:
  + This requirement ensures consistent communication between stakeholders, facilitating smoother collaboration and avoiding misunderstandings about deliverables.

## 2.10 Ensuring Mission Readiness

* **Why It Matters**:
  + Before deployment, the software must undergo rigorous validation to verify readiness for operational use. Acceptance criteria ensure final evaluations focus on confirming that:
    - All functional capabilities are reliable under nominal and off-nominal conditions.
    - Software integrates seamlessly with hardware and other mission systems.
    - Reliability and safety have been fully tested and satisfied.
  + Launching or deploying software without meeting explicitly defined acceptance criteria risks failures that could compromise mission success or human lives.
* **Rationale**:
  + Acceptance criteria ensure software is assessed for operational readiness before deployment to avoid costly failures or unsafe operations.

# 3. Guidance

The supplemented and refined guidance emphasizes the critical aspects of developing, documenting, and executing acceptance criteria and acceptance testing. It incorporates the rationale provided above to reinforce the importance of aligning functional requirements, operational objectives, customer expectations, and regulatory compliance as part of the software acceptance process.

## 3.1 Definition of Acceptance Criteria

Acceptance criteria should be defined as **specific, measurable requirements** which a software system or component needs to fulfill to be approved by the customer, user, or other authorized personnel. These criteria include, but are not limited to:

1. **Functional Requirements**: The ability of the software to meet its intended functionality (e.g., operational processes, end-user features).
2. **Performance Requirements**: Specific thresholds the software must meet, including speed, reliability, availability, memory optimization, communications throughput.
3. **Correctness and Precision Criteria**: Exactness and consistency in calculations, round-off, and accuracy.
4. **Compliance Criteria**: Adherence to regulatory or contractual requirements (e.g., **DO-178C**, NASA **NPR 7150.2D**).

This definition should align with international standards (**ISO/IEC/IEEE 24765:2010**) and project-specific guides (PMBOK, contractual agreements) while tailoring to the unique needs of the mission.

## 3.2 Purpose of the Requirement

This requirement drives collaboration between the software development team and the customer to define, document, and review acceptance criteria to:

1. **Guide Development**: Ensure the software development team understands the customer’s expectations and incorporates them into the software design and implementation process.
2. **Enable Testing**: Create measurable and testable benchmarks to validate the software through formal acceptance testing activities.
3. **Support Transition**: Establish conditions for a successful transition of the software from development to operations and maintenance teams.
4. **Mitigate Risk**: Reduce uncertainties by clearly defining what constitutes an acceptable software product, preventing late-stage disputes or project delays.
5. **Facilitate Certification**: Define milestone-based acceptance criteria necessary for flight certification or regulatory approval processes.
6. **Promote Accountability**: Ensure that the software team, assurance personnel, and customers are accountable for agreed-upon criteria and deliverables.

## 3.3 Improved Guidance for Acceptance Criteria Creation

### 3.3.1 Establishing Acceptance Criteria

Acceptance criteria development begins in the Formulation phase and evolves throughout the project to align with:

* New requirements or emerging constraints,
* System design and integration details, and
* Insights gained during development and testing activities.

#### Steps in Developing Acceptance Criteria

1. 1. **Collaborative Development**: The project manager, software lead engineer, development team, and the customer should collaboratively define acceptance criteria, ensuring alignment with mission objectives.
   2. **Include Interim Deliverables**: Define criteria for interim products (e.g., prototypes, test results) and final deliverables, ensuring progressive evaluation of the software.
   3. **Integration and System Level Criteria**: Address unit-level features, integration validation, and system-wide operational readiness.
   4. **Rank Importance**: Establish prioritization and rank criteria by criticality, such as mission-critical functionalities, user experience, risks, and system reliability.
   5. **Consider Lifecycle Costs and Operations**: Acceptance criteria should include considerations for long-term costs (e.g., maintenance), environmental constraints (e.g., space-based operations), and schedule impact.

#### Acceptance Criteria Scope

The criteria must encompass all facets of software deliverables, such as:

1. **Software Components**: Code, databases, models.
2. **Artifacts**: Documentation (e.g., user manuals, technical specifications), test results.
3. **Licensing and Rights Transfer**: Data rights, intellectual property, certifications.
4. **Integration and Operational Readiness**: System maintenance plans, networking compatibility.

#### Documentation

The criteria should be formally documented in:

1. A **Software Development/Management Plan (SDP/SMP)**,
2. **Verification and Validation (V&V) Plan**,
3. **Contractual documents** (e.g., Statements of Work or DRDs).

### 3.3.2 Acceptance Testing

Acceptance testing evaluates the software’s compliance with the documented acceptance criteria and validates its readiness for operational use. Acceptance testing is linked directly to the criteria to ensure that key requirements are met systematically.

#### Types of Testing

1. 1. **Alpha Testing**: Internal testing at developers' sites to validate basic functionality.
   2. **Beta/Field Testing**: External testing by select end-users under real-world conditions.
   3. **System Testing**: Comprehensive testing of the software’s integration within system-wide processes.
   4. **User Acceptance Testing (UAT):** Final testing to confirm the software fulfills mutually agreed-upon requirements.

#### Process

1. Develop the test procedures (test suites) based on acceptance criteria.
2. Execute tests under predefined environmental and input conditions.
3. Compare test results against expected outputs or tolerances defined in the acceptance criteria.

#### Planning Considerations

1. 1. **Adequate Time**: Provide sufficient time for review, testing, and debugging before acceptance.
   2. **Environment Preparation**: Ensure test environments and tools are available and ready.
   3. **Team Availability**: Ensure software testing personnel and software assurance personnel are available to support testing activities.

### 3.3.3 Decision-Making Based on Testing Results

Acceptance testing must lead to formal decisions about software readiness:

1. 1. **Acceptance with Conditions**: Criteria that aren't fully met but can be deemed acceptable based on prior agreements.
   2. **Rejection/Remediation**: Deficiencies requiring corrective action before acceptance can be granted.
   3. **Negotiation of Deviations**: Deviations from requirements must be reviewed and negotiated with the customer.

### 3.3.4 Ongoing Updates to Criteria

Acceptance criteria must be updated throughout the project:

1. 1. Responding to changes in system requirements or customer needs.
   2. Refining criteria based on test results or lessons learned during development and testing stages.
   3. Ensuring criteria remain aligned with the system being built.

### 3.3.5 Contractual Criteria for Acquired Software

Acceptance criteria for software acquired via contracts should be incorporated into:

1. 1. **Statements of Work (SOW)**: Clearly define deliverables and acceptance conditions,
   2. **Contract Clauses**: Document technical requirements and essential conditions,
   3. **Data Requirements Documents (DRDs)**: Ensure documentation milestones are specified and verifiable.

## 3.4 Importance of Acceptance Planning

Acceptance criteria and acceptance testing are central to system-level readiness. They enable:

1. 1. Efficient software delivery,
   2. Robust Validation & Verification (V&V) processes,
   3. Structured decision-making during project reviews (e.g., System Acceptance Reviews).

The System Acceptance Review marks the final gateway for software approval. Entrance and exit criteria for this review should be informed directly by the acceptance criteria and testing outcomes.

### 3.4.1 Summary of Improvements

The refined guidance clearly integrates the rationale and practical considerations for developing acceptance criteria and ties acceptance testing activities directly to these criteria. It emphasizes:

1. 1. Collaborative and iterative development of acceptance criteria.
   2. Comprehensive documentation practices for traceability and accountability.
   3. Testing methodologies that validate adherence to criteria and enable informed decision-making.
   4. Contractual clarity for acquired software.
   5. Flexibility to adapt criteria as requirements evolve throughout the software lifecycle.

This improved guidance underscores the role of acceptance criteria in mitigating risk, ensuring compliance, and achieving mission readiness while fostering transparency and structured collaboration across teams and stakeholders.

### 3.4.2 Examples:

The **software development team and the customer** work together to ensure that they do the following:

1. 1. Identify interim and final products that will be part of acceptance activities.
   2. Develop the acceptance criteria and activities schedule.
   3. Plan how and by whom each acceptance activity will be performed.
   4. Schedule adequate time for the customer to examine and review the product.
   5. Prepare the acceptance plan.
   6. Perform formal acceptance testing at scheduled times.
   7. Plan the decision-making process that is based on the results of acceptance testing.

The **software lead engineer works with the software team** (including the software assurance personnel) to develop appropriate product reviews, tests, and any audits necessary. This work includes identifying:

1. 1. The types of criteria to consider, such as customer expectations and requirements, technology limitations, environmental impact, safety, risks, total ownership, life cycle costs, and schedule impact.
   2. The variations in criteria for computer software configuration items (CSCI), units, and or systems.
   3. The acceptable range of the criteria.
   4. The rank of each criterion by its importance.

**Acceptance criteria** may include:

1. 1. Product V&V was completed successfully.
   2. V&V of individual products, integration of products into systems, and that system V&V has been performed or witnessed by the technical team.
   3. The technical data package is current (as-built) and complete.
   4. Transfer of certifications, warranties, or representations is complete.
   5. Transfer of software products, licenses, data rights, intellectual property rights, etc., is complete.
   6. If an acquisition: Technical documentation required in contract clauses is complete (e.g., new technology reports).
   7. Correctness criteria (e.g., round-off, accuracy, precision).
   8. Performance criteria (e.g., speed, time).
   9. Throughput criteria.
   10. System availability.
   11. System reliability.
   12. Input/output (I/O) performance.
   13. Memory performance.
   14. System communications.
   15. Networking capability.
   16. Software compatibility.
   17. System maintenance (component level/systems level) plan availability.
   18. Documentation availability.
   19. Readiness for the software release. [373](#_tabs-<p></p>)

The **planning for acceptance testing** may consider:

1. 1. Acceptance period (is it open? is it constrained?).
   2. Diagnostics tests (are they part of the software requirements specification?).
   3. Functionality tests (what is the software work product designed to do?).
   4. Use of the latest production version of code (are earlier versions acceptable?).
   5. Differences/discrepancies (when are they acceptable? or the cause for an issue and corrective action activity?).
   6. Availability and readiness of the test environment.
   7. Availability of test and software assurance personnel to support the testing.

**Acceptance testing activities** include:

1. 1. Alpha testing takes place at developers' sites and involves testing the operational system by internal staff before it is released to external customers.
   2. Beta testing takes place at customers' sites and involves testing by a group of customers who use the system at their locations and provide feedback before the system is released to other customers. This is often called "field testing."
   3. System testing is invariably performed by the development team or preferably by someone independent of the developer
   4. User Acceptance Testing (UAT) is a process to obtain confirmation that a system meets mutually agreed-upon requirements. In software development, UAT is one of the final stages of a project and often occurs before a customer accepts the new system

Acceptance tests may also be used as regression tests before a production release. This means that new acceptance tests must be created for each iteration of the software build.

See also: [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior), [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)

All software products should have acceptance criteria defined, this includes items like software documents, software code, databases, software models, and software defect and change reports. The acceptance criteria can be documented in the software development or management plans or the contract documentation, an example of acceptance criteria in contract documentation could be the Data Requirements Documents (DRDs). Criteria for software acceptance testing are often documented in the software test plans.

 After a software work product is designed, coded, and tested against its requirements, if any deviations from the requirements and acceptance criteria still exist, they will have to be negotiated with the customer to determine if they can be accepted, or if they must be fixed before the customer accepts the product. The customer must review and agree to the acceptance test plan.

The entrance criteria and the exit (success) criteria are developed and documented during the acceptance planning activities (see topic [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)) for the System Acceptance Review.

See also Topic [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels). [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance)

## 3.5 Additional Guidance

Additional guidance related to acceptance testing may be found in the following related requirements in this handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only).

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation)      * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

This requirement ensures that projects establish clear **acceptance criteria** to determine when the software is complete, meets stakeholder expectations, and performs as intended.

For **small projects**, this requirement can be streamlined while still maintaining full compliance. The following guidance offers actionable steps tailored to small-scale projects, focusing on simplicity, clarity, and efficiency.

### Key Benefits of Small Project Guidance

1. **Efficiency**: Keeps documentation lightweight and focused on the key deliverables most critical to project success.
2. **Traceability**: Links acceptance criteria to project requirements, enabling clear tracking and accountability.
3. **Stakeholder Alignment**: Ensures all stakeholders agree on measurable criteria for assessing software completion.
4. **Verification Support**: Simplifies the process for reviewing test results and tracking whether acceptance criteria are satisfied.

By following these steps, small projects can comply with this requirement effectively while streamlining processes and avoiding overburdening the team.

## 4.1 Define What Software Acceptance Criteria Are

### What are Software Acceptance Criteria?

Acceptance criteria are measurable conditions and requirements that the software must meet to be considered complete and successfully delivered. These criteria ensure that all stakeholders agree on the measurable benchmarks for software quality, functionality, performance, and compliance.

**For Small Projects**:

* Keep criteria focused on essential aspects that stakeholders care about most—such as basic functionality, performance, security, and compliance.
* Avoid unnecessary complexity; prioritize concise, clearly understandable criteria that reflect the project’s size, scope, and software classification.

## 4.2 Process for Defining and Documenting Acceptance Criteria

### Step 1: Engage Stakeholders

* **Why**: The acceptance criteria must align with the needs and expectations of stakeholders, including customers, users, NASA oversight groups, and internal teams (e.g., developers, testers).
* **What to Do**:
  + **Plan Stakeholder Engagement**:
    - Arrange a short meeting or a collaborative planning session to define acceptance criteria.
    - Include input from all relevant groups (e.g., project manager, SA personnel, end users) to ensure acceptance criteria cover usability, quality, and mission objectives.
  + **Gather Input**:
    - Gather specific expectations for functionality, performance, and delivery milestones.
    - Example: “System must process at least 1,000 simultaneous transactions with ≤1-second response time.”
* **For Small Projects**:
  + Use simple formats like checklists or templates during meetings to capture stakeholder expectations directly.

### Step 2: Align Criteria with Requirements

* **Why**: Acceptance criteria must directly correspond to the project's software requirements and objectives to ensure alignment between planned and delivered software.
* **What to Do**:
  + Cross-reference each criterion with the project’s Software Requirements Specification (SRS).
  + Ensure acceptance conditions are traceable to system-level requirements, safety-critical requirements (if applicable), and software assurance objectives.
* **For Small Projects**:
  + Focus on high-priority requirements and safety-critical features if applicable. Document the alignment using simple tables or spreadsheets.

### Step 3: Define Measurable Acceptance Conditions

* **Why**: Acceptance criteria should be specific and measurable to avoid ambiguity during validation and verification.
* **What to Include**:
  + **Functional Criteria**:
    - Examples: “Software meets all functional requirements specified in the SRS, including error-handling features.”
  + **Performance Criteria**:
    - Example: “Software achieves a throughput of 500 requests per minute under target load conditions as verified by performance tests.”
  + **Interface/Integration Criteria**:
    - Example: “Software integrates successfully with specified hardware systems and third-party interfaces.”
  + **Safety & Security Compliance Criteria**:
    - Example: “Software complies with identified security standards such as NASA IT Security Handbook; high-priority vulnerabilities are resolved.”
  + **Documentation Criteria**:
    - Example: “User manuals and training materials are reviewed and approved.”
  + **Verification/Validation Testing Criteria**:
    - Example: “All test cases defined in the Software Test Plan are executed and pass successfully, with critical defects resolved.”
* **For Small Projects**:
  + Limit criteria to essential dimensions (e.g., functional performance, integration) and avoid highly detailed breakdowns unless critical.

### Step 4: Select a Simple Documentation Format

* **Why**: Documented acceptance criteria provide a clear reference for validation, sign-off, and tracking whether the software is ready for deployment.
* **Documentation Methods for Small Projects**:
  + **Checklist Format**:
    - Create a simple checklist that lists each criterion for easy tracking during reviews. Example:

      | Acceptance Criterion | Requirement Link | Verification Method | Status |
      | --- | --- | --- | --- |
      | Successfully passes functional tests | Linked to requirement R-1 | Verified via system-level tests | ✅ Passed |
      | Integrates with approved hardware | Linked to requirement R-2 | Verified during integration tests | ❌ Pending |
  + **Acceptance Plan**:
    - Write an easy-to-use Acceptance Plan that includes:
      * Objectives.
      * Criteria (with descriptions and measurable targets).
      * Validation methods (e.g., testing, reviews).
      * The format can be a short document (2-5 pages), even in Word or Excel.
  + **Combine with Other Plans**:
    - For simplicity, integrate acceptance criteria into the Software Test Plan or Software Requirements Specification (SRS).

### Step 5: Define Verification Methods

* **Why**: Ensuring acceptance criteria are testable makes it easier for SA personnel and the project manager to track whether the software satisfies them.
* **What to Do**:
  + List the verification methods for each criterion:
    - Functional testing.
    - Performance/load testing.
    - Code reviews.
    - Demonstrations (e.g., user acceptance testing or feature walkthroughs).
    - Compliance audits for safety/security requirements.
  + Use evidence from defect reports, test cases, and execution logs to validate criteria.
* **For Small Projects**:
  + Limit testing to project scope.
    - Example: For a limited deployment, prioritize integration tests and system-level functional tests over exhaustive validation.

### Step 6: Obtain Stakeholder Approval

* **Why**: Stakeholder buy-in ensures that defined acceptance criteria satisfy project goals, while formally approving the criteria helps avoid disputes during final delivery.
* **What to Do**:
  + Present the acceptance criteria in a meeting or email approval cycle for stakeholder consensus.
  + Record feedback, update criteria if needed, and obtain formal sign-off (e.g., via email agreement or signed document).
* **For Small Projects**:
  + Simplify approvals using emails or team consensus in a meeting.

## 4.3 Example of Small Project Acceptance Criteria Documentation

### Acceptance Criteria Checklist

| Acceptance Criterion | Requirement Traceability | Verification Method | Status |
| --- | --- | --- | --- |
| Software meets all functional requirements | Linked to Requirement R-1 | System-level functional tests | ✅ Passed |
| Performance: Minimum 500 req/min throughput | Linked to Performance Req R-3 | Performance testing results | ❌ Pending |
| Integrates with target hardware interfaces | Linked to Requirement R-4 | Integration testing | ✅ Passed |
| No critical defects remain after testing | Linked to Quality Req R-5 | Final defect report results | ✅ Passed |
| Updated user documentation is delivered | Linked to Documentation Req R-6 | Review of user manuals | ❌ Pending |

---

## 4.4 Review and Monitor Acceptance Criteria

### Tips for Small Projects:

1. **Integrate Into Existing Processes**:
   * Include acceptance criteria discussions in project status meetings or milestone reviews.
   * Have the Software Assurance (SA) personnel confirm alignment between the acceptance criteria and test results.
2. **Track Progress**:
   * Use an action tracker (simple spreadsheet or task management tool) to update the checklist with the results of validation activities.
3. **Verify Completeness**:
   * Perform a final review of all criteria before delivery.
   * Ensure signed approval is obtained from stakeholders.

## 4.5 Tools and Techniques for Small Projects

* **Templates**: Use simple templates for documenting acceptance criteria. Examples include:
  + Word, Excel, or Google Sheets tables for tracking criteria.
  + Pre-designed templates for lightweight acceptance plans.
* **Automation**:
  + Leverage lightweight tools like Trello, Jira, or spreadsheet trackers to manage acceptance criteria.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-219)

  [IEEE Standard for Software Reviews and Audits](https://ieeexplore.ieee.org/document/4601584 "Click to open in new window")

  IEEE Std 1028, 2008. IEEE Computer Society, NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-230)

  [ISO/IEC/IEEE 24765:2017 Systems and software engineering -- Vocabulary.](https://www.iso.org/standard/71952.html "Click to open in new window")

  ISO/IEC/IEEE 24765:2017  It was prepared to collect and standardize terminology. Copy attached.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-302)

  [A Guide to the Project Management Body of Knowledge (PMBOK® Guide) -- Fifth Edition.](http://marketplace.pmi.org/Pages/ProductDetail.aspx?GMProduct=00101095501 "Click to open in new window")

  Project Management Institute (2013).
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-034 - Acceptance Criteria**

3.1.5 The project manager shall define and document the acceptance criteria for the software.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm software acceptance criteria are defined and assess the criteria based on guidance in the NASA Software Engineering Handbook, NASA-HDBK-2203.

## 7.2 Software Assurance Products

Software Assurance (SA) personnel produce a variety of products to ensure compliance with the requirement: **focusing on defining**, **validating**, and **monitoring the acceptance** **criteria process**. These products provide traceability, alignment, assessment, and documentation of the acceptance criteria for the project's software deliverables. Below is a detailed list of Software Assurance products related to this requirement.

These Software Assurance products  ensure compliance with the requirement by documenting, validating, and managing acceptance criteria at every stage of the software development lifecycle. These artifacts provide traceability, evidence, and actionable insights that enhance the reliability, safety, and quality of the software, while supporting successful delivery in both traditional and Agile environments.

### 7.2.1 Documentation and Review Products

#### 7.2.1.1 Acceptance Criteria Review Reports

* **Purpose**: Confirm completeness, traceability, and relevance of defined acceptance criteria.
* **Content**:
  + Results of SA analysis of the documented acceptance criteria.
  + Recommendations for improvement (e.g., missing criteria, unmeasurable metrics).
  + Traceability between requirements and acceptance criteria.
* **Key Outputs**:
  + Formal report or checklist documenting SA review of acceptance criteria.

#### 7.2.1.2 Requirements Traceability Matrix Assessment

* **Purpose**: Ensure acceptance criteria are linked to corresponding system/software requirements.
* **Content**:
  + Assessment verifying alignment between acceptance criteria and software lifecycle objectives.
  + Identification of any missing links in the traceability matrix.
* **Key Outputs**:
  + Annotated traceability matrix with assessment notes.

#### 7.2.1.3 Stakeholder Alignment Assessment

* **Purpose**: Confirm acceptance criteria reflect stakeholder expectations.
* **Content**:
  + Documentation of stakeholder feedback.
  + Evaluation of acceptance criteria alignment with mission goals and operational needs.
* **Key Outputs**:
  + Stakeholder approval review log capturing SA observations.

### 7.2.2 Validation and Testing Products

#### 7.2.2.1 Validation Coverage Reports

* **Purpose**: Demonstrate that all acceptance criteria are validated via designated methods.
* **Content**:
  + Summary of tests, inspections, and demonstrations validating acceptance criteria.
  + Evidence of test execution results and defect resolution.
* **Key Outputs**:
  + Validation coverage report linking test results to acceptance criteria.

#### 7.2.2.2 Corrective Action Reports

* **Purpose**: Address non-conformances impacting acceptance criteria validation.
* **Content**:
  + List of defects or gaps identified during testing.
  + Description of corrective actions implemented to resolve issues tied to criteria validation.
* **Key Outputs**:
  + Corrective Action Request (CAR) reports with closure status.

#### 7.2.2.3 Test and Verification Evidence

* **Purpose**: Provide documentation of verified acceptance criteria.
* **Content**:
  + Test plans and procedures for validating criteria.
  + Test results (e.g., log files, execution summaries).
  + Final evidence logs demonstrating validation success.
* **Key Outputs**:
  + Test execution summaries tied to specific acceptance criteria.

### 7.2.3 Software Assurance and Safety Evaluation Products

#### 7.2.3.1 Software Assurance and Software Safety Plan

* **Purpose**: Define acceptance criteria for Software Assurance and Software Safety deliverables.
* **Content**:
  + Planned activities and specific acceptance conditions for SA and safety work products.
  + Traceability to higher-level project goals and requirements.
* **Key Outputs**:
  + Approved Software Assurance and Software Safety Plan.

#### 7.2.3.2 Compliance Assessments

* **Purpose**: Verify compliance of SA deliverables.
* **Content**:
  + Evaluation of SA deliverables against their documented acceptance criteria.
  + Documentation of compliance with NASA and project-specific standards (e.g., NASA-HDBK-2203).
* **Key Outputs**:
  + SA compliance report or checklist for project artifacts.

#### 7.2.3.3 Risk Assessment Reports

* **Purpose**: Ensure safety and risk criteria related to software acceptance are appropriately addressed.
* **Content**:
  + Evaluations of risk mitigation activities and safety requirements validation.
  + Gap analysis of software safety assurance deliverables.
* **Key Outputs**:
  + Safety risk assessment documents.

### 7.2.4 Agile/Incremental Development Products

#### 7.2.4.1 Definition of Done (DoD) Compliance Assessment

* **Purpose**: Assess whether Agile sprint deliverables align with acceptance criteria at the system level.
* **Content**:
  + Verification that all sprint-level DoD components meet project-level acceptance conditions.
  + Traceability from Agile user stories to project acceptance criteria.
* **Key Outputs**:
  + Compliance reports for each sprint, summarizing gaps and achievements relative to the DoD.

#### 7.2.4.2 Sprint Validation Checklist

* **Purpose**: Ensure incremental deliverables (code, tests, docs) meet interim acceptance goals.
* **Content**:
  + Checklist documenting completed validation activities for sprint deliverables.
  + List of open items for roll-over tracking into subsequent sprints.
* **Key Outputs**:
  + Sprint validation checklist confirmed by SA personnel.

#### 7.2.4.3 Integration Testing Validation Products

* **Purpose**: Validate acceptance criteria for working code segments integrated across and between sprint teams.
* **Content**:
  + Summary of integration test results proving compatibility and function alignment.
  + Documentation of reliability and safety testing for integrated products.
* **Key Outputs**:
  + Integration test logs captured by SA and signed off at sprint milestones.

### 7.2.5 Stakeholder Communication and Approval Products

#### 7.2.5.1 Stakeholder Sign-Off Documentation

* **Purpose**: Ensure formal approval of acceptance criteria and results.
* **Content**:
  + Stakeholder acceptance forms or meeting notes.
  + Final sign-off summary for acceptance criteria and validation results.
* **Key Outputs**:
  + Stakeholder approval documentation (e.g., formal acceptance letters).

#### 7.2.5.2 Customer Agreement Records

* **Purpose**: Demonstrate consistent communication between SA personnel and customers regarding criteria expectations.
* **Content**:
  + Documentation of customer alignments, expectations, and agreed milestones.
* **Key Outputs**:
  + Agreement records or signed meeting minutes capturing customer approvals.

### 7.2.6 Process and Standards Compliance Products

#### 7.2.6.1 Standards Compliance Checklists

* **Purpose**: Show alignment of acceptance criteria with NASA guidelines.
* **Content**:
  + Checklist verifying compliance with NASA-HDBK-2203 and NASA Software Engineering Handbook standards.
* **Key Outputs**:
  + Standards compliance checklist.

#### 7.2.6.2 Configuration Management Audit Products

* **Purpose**: Ensure acceptance criteria are placed under proper configuration control.
* **Content**:
  + Version-controlled documentation of acceptance criteria across milestones.
  + History of updates tracked for change management purposes.
* **Key Outputs**:
  + Configuration management audit report.

### Summary of Software Assurance Products

| Category | SA Product Examples |
| --- | --- |
| Documentation & Review | Acceptance Criteria Review Reports, Stakeholder Alignment Log |
| Validation & Testing | Validation Plans, Corrective Action Reports, Test Results Logs |
| SA & Safety Evaluation | Software Assurance Plan, Compliance Report, Risk Assessment |
| Agile/Incremental Deliverables | Sprint Validation Checklist, DoD Compliance Report |
| Stakeholder Communication | Stakeholder Sign-Off Documentation, Customer Alignment Records |
| Process Compliance | Standards Checklist, Configuration Management Audit |

Assessment that acceptance criteria for Software Engineering are reasonable per Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) of this Handbook, including corrective actions.

## 7.3 Metrics

For Software Assurance (SA) personnel, metrics for this requirement are essential to measure the quality, completeness, and effectiveness of the acceptance criteria, as well as the assurance processes employed to validate those criteria. These metrics provide visibility into compliance with the requirement and help improve SA practices throughout the project lifecycle.

These metrics help Software Assurance personnel track compliance with this requirement, identify gaps, and continuously improve acceptance criteria development and validation processes.

Below is a detailed list of Software Assurance Metrics for this requirement, organized by areas of focus: documentation, validation and verification, stakeholder alignment, agility in development, and readiness for acceptance.

### 7.3.1 Metrics for Documentation of Acceptance Criteria

#### Metric 1: Completeness of Documented Acceptance Criteria

* Definition: Percentage of software requirements covered by documented acceptance criteria.
* Formula: [ \text{Completeness Rate} = \left( \frac{\text{Accepted Requirements Covered by Criteria}}{\text{Total Requirements}} \right) \times 100 ]
* Purpose: Ensures that all requirements, including functional, performance, safety, and security, have corresponding acceptance criteria.
* Target Value: ≥95%.

#### Metric 2: Traceability of Acceptance Criteria

* Definition: Percentage of acceptance criteria that are traceable to specific software requirements and project objectives.
* Formula: [ \text{Traceability Rate} = \left( \frac{\text{Criteria Linked to Requirements}}{\text{Total Acceptance Criteria}} \right) \times 100 ]
* Purpose: Verifies alignment and traceability between acceptance criteria, requirements, and stakeholder expectations.
* Target Value: 100%.

#### Metric 3: Stakeholder Review Coverage

* Definition: Percentage of acceptance criteria reviewed and approved by stakeholders (e.g., project manager, engineers, customers).
* Formula: [ \text{Review Coverage} = \left( \frac{\text{Criteria Reviewed and Approved}}{\text{Total Acceptance Criteria}} \right) \times 100 ]
* Purpose: Tracks stakeholder involvement in approving acceptance criteria.
* Target Value: ≥90%.

### 7.3.2. Metrics for Validation and Verification

#### Metric 4: Validation Coverage

* Definition: Percentage of acceptance criteria validated by tests, reviews, or demonstrations during the project’s lifecycle.
* Formula: [ \text{Validation Coverage} = \left( \frac{\text{Criteria Validated by Execution or Evidence}}{\text{Total Acceptance Criteria}} \right) \times 100 ]
* Purpose: Ensures that all acceptance criteria are verified through planned validation methods, such as testing or peer reviews.
* Target Value: ≥95%.

#### Metric 5: Defect Impact Rate

* Definition: Percentage of defects identified during validation that directly impact compliance with acceptance criteria.
* Formula: [ \text{Defect Impact Rate} = \left( \frac{\text{Acceptance Criteria Impacted by Defects}}{\text{Total Acceptance Criteria}} \right) \times 100 ]
* Purpose: Identifies the proportion of acceptance criteria affected by defects, helping to focus on high-risk areas.
* Target Value: ≤5%.

#### Metric 6: Corrective Action Closure Rate

* Definition: Percentage of corrective actions related to acceptance criteria validation issues successfully closed before project milestones.
* Formula: [ \text{Corrective Action Closure Rate} = \left( \frac{\text{Closed Corrective Actions}}{\text{Total Corrective Actions Identified}} \right) \times 100 ]
* Purpose: Tracks the resolution of identified issues during the verification process.
* Target Value: ≥95%.

### 7.3.3. Metrics for Stakeholder Alignment

#### Metric 7: Stakeholder Approval Rate

* Definition: Percentage of acceptance criteria explicitly approved or signed off by stakeholders.
* Formula: [ \text{Stakeholder Approval Rate} = \left( \frac{\text{Criteria Approved by Stakeholders}}{\text{Total Acceptance Criteria}} \right) \times 100 ]
* Purpose: Tracks the extent to which stakeholders validate and approve acceptance criteria, ensuring alignment with project expectations.
* Target Value: 100%.

#### Metric 8: Number of Revisions to Acceptance Criteria

* Definition: Count of revisions to acceptance criteria based on stakeholder feedback or evolving requirements.
* Formula: No formula required; simply track the count.
* Purpose: Monitors how often criteria are revised to improve clarity or address stakeholder concerns.
* Target Value: ≤10 revisions (depending on project size and complexity).

### 7.3.4. Metrics for Agile and Incremental Development

#### Metric 9: Definition of Done (DoD) Compliance Rate

* Definition: Percentage of sprint-generated features or tasks that meet the Definition of Done (DoD) and contribute to meeting acceptance criteria.
* Formula: [ \text{DoD Compliance Rate} = \left( \frac{\text{Features Meeting DoD for Sprint}}{\text{Total Features Implemented}} \right) \times 100 ]
* Purpose: Ensures alignment between sprint deliverables and higher-level software acceptance criteria.
* Target Value: ≥95%.

#### Metric 10: Sprint Acceptance Criteria Validation Rate

* Definition: Percentage of acceptance criteria verified and validated at the end of each sprint in Agile development environments.
* Formula: [ \text{Validation Rate per Sprint} = \left( \frac{\text{Criteria Validated After Sprint}}{\text{Total Criteria Applicable to Sprint Deliverables}} \right) \times 100 ]
* Purpose: Tracks progress toward meeting acceptance criteria across iterative software development cycles.
* Target Value: ≥90%.

#### Metric 11: Daily Regression Testing Update Frequency

* Definition: Frequency at which regression testing suites are updated to include new features or functions added during Agile sprint cycles.
* Formula: No formula required; track the update frequency (e.g., daily or weekly logs of regression suite updates).
* Purpose: Ensures regression tests align with evolving project acceptance criteria.
* Target Value: Daily or as features are added.

### 7.3.5. Metrics for Readiness for Acceptance

#### Metric 12: Final Build Acceptance Rate

* Definition: Percentage of acceptance criteria satisfied by the finalized integrated software build.
* Formula: [ \text{Final Build Acceptance Rate} = \left( \frac{\text{Criteria Met in Final Build}}{\text{Total Acceptance Criteria}} \right) \times 100 ]
* Purpose: Measures whether the final software product meets all documented acceptance criteria for delivery.
* Target Value: 100%.

#### Metric 13: Readiness for Software Milestones

* Definition: Percentage of milestone-specific acceptance criteria validated at each milestone review stage.
* Formula: [ \text{Milestone Readiness Rate} = \left( \frac{\text{Criteria Validated at Milestone Stage}}{\text{Total Criteria for Milestone}} \right) \times 100 ]
* Purpose: Ensures milestone reviews, such as Preliminary Design Review (PDR) or Critical Design Review (CDR), track validation status for acceptance goals.
* Target Value: ≥90%.

#### Metric 14: Documentation Approval Rate

* Definition: Percentage of required technical documentation (e.g., user guides, test reports) approved for acceptance.
* Formula: [ \text{Documentation Approval Rate} = \left( \frac{\text{Approved Documentation Deliverables}}{\text{Total Planned Documentation Deliverables}} \right) \times 100 ]
* Purpose: Ensures delivery of documentation as part of overall software acceptance readiness.
* Target Value: 100%.

### 7.3.6. Metrics Reporting

#### Reporting Frequency:

* Milestone-Based Reporting: Monitor and report these metrics at key project reviews, such as PDR, CDR, Test Readiness Review (TRR), and Software Acceptance Review (SAR).
* Sprint-Based Reporting: For Agile projects, report metrics at the end of each sprint or increment.

### Visualization of Metrics:

Use dashboards and visual formats, such as:

* Bar charts for traceability metrics or validation coverage.
* Line charts for trends in revisions or defect impacts.
* Pie charts for stakeholder approval rates or completeness of acceptance criteria.

### Summary of Metrics Categories

| Category | Metric Examples | Purpose |
| --- | --- | --- |
| Documentation | Completeness Rate, Traceability Rate | Ensure acceptance criteria are traceable and complete. |
| Validation & Verification | Validation Coverage Rate, Corrective Action Rate | Validate acceptance criteria through testing or evidence. |
| Stakeholder Alignment | Stakeholder Approval Rate | Confirm stakeholder sign-off and alignment. |
| Agile Development | DoD Compliance Rate, Daily Regression Testing | Ensure Agile increments meet acceptance criteria. |
| Readiness for Acceptance | Final Build Rate, Documentation Approval Rate | Measure readiness for delivery and milestone reviews. |

See also [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products),

## 7.4 Guidance

This guidance addresses how Software Assurance (SA) personnel support this requirement. SA personnel must ensure that acceptance criteria are well-documented, measurable, reasonable, and aligned with the project goals, providing traceability to software requirements and ensuring software safety, quality, and reliability. This guidance expands upon the basic steps and adds actionable recommendations, especially in traditional and Agile environments.

By proactively defining, managing, and validating software acceptance criteria, Software Assurance personnel ensure project success while driving quality, safety, and reliability. The structured approach described above allows SA personnel to assess and guarantee that no steps are overlooked, whether for Agile projects or traditional development. The ultimate goal is to deliver software that meets defined objectives and contributes to mission success.

### 7.4.1 Key Steps for Software Assurance Personnel

#### Step 1: Determine That Acceptance Criteria Are Documented

* **What to Do**:

  + Verify that the project or engineering team has documented software acceptance criteria for all software products and deliverables.
  + Review required documentation, such as:
    - Software Requirements Specification (SRS).
    - Acceptance Plan (if standalone).
    - Software Assurance and Software Safety Plans (as applicable).
  + Where missing, work with the project manager and stakeholders to ensure acceptance criteria are defined and documented.
* **SA Actions**:

  + Audit project processes to confirm there is a well-structured framework for defining acceptance criteria.
  + Confirm traceability of acceptance criteria to high-level software and system requirements.
    - Example: Ensure key functional, performance, reliability, and safety requirements translate into specific acceptance thresholds.
* **Objective Evidence**:

  + Review documented criteria for completeness and version control, ensuring artifacts are accessible to all stakeholders.
  + Collect audit logs showing confirmation that acceptance criteria meet expected standards.

#### Step 2: Assess the Acceptance Criteria for Completeness and Relevance

* **What to Do**:

  + Validate that the acceptance criteria conform to NASA-HDBK-2203 and NASA Software Engineering Handbook recommendations.
  + Ensure acceptance criteria address project needs in terms of measurable conditions, high-priority requirements, and intended operational environments.
* **SA Actions**:

  + Evaluate the reasonableness of the acceptance criteria:
    - Is the criterion measurable or testable? Example: "Response time ≤ 2 seconds under normal load."
    - Are technical and risk-related dimensions sufficiently addressed (e.g., risk, reliability)?
    - Do the criteria reflect the customer’s expectations for software functionality, quality, and safety?
  + Review alignment with any contractual obligations (if applicable).
  + Verify traceability between acceptance criteria and higher-level project plans (e.g., Software Management Plan, Quality Assurance Plan).
* **Objective Evidence**:

  + Assessment reports with findings/recommendations on the adequacy and completeness of acceptance criteria.
  + Meeting minutes or stakeholder review notes reflecting alignment discussions.

#### Step 3: Develop Acceptance Criteria for Software Assurance and Safety Products

* **What to Do**:

  + Collaborate with the Software Assurance and Software Safety team to define acceptance criteria for assurance and safety-related products and activities.
  + Address criteria for:
    - SA deliverables (e.g., verification/validation plans, compliance assessments, audits).
    - Safety analyses (e.g., fault trees, hazard reports, risk reports).
    - Milestone reviews (e.g., Software Test Plan review, Safety Compliance review).
* **SA Actions**:

  + Develop clear objectives for evaluating SA and safety activities/products.
    - Example: “Verify that the software assurance audit plan contains actionable criteria for identifying safety-critical gaps.”
  + Ensure that SA acceptance criteria cover elements such as:
    - Correctness of work products: Are SA and safety deliverables complete and accurate?
    - Alignment with stakeholder expectations: Is SA input consistent with system needs, risk analyses, and operational conditions?
    - Reliability and Non-conformance: Have SA outputs met established criteria for quality and consistency?
* **Objective Evidence**:

  + A documented Software Assurance and Software Safety Plan outlining acceptance criteria for SA deliverables.
  + Review findings that verify safety reports and technical documents against acceptance goals.

#### Step 4: Verify Software Engineering and SA Criteria for Reasonableness

* **What to Do**:

  + Review whether software engineering and assurance acceptance criteria are reasonable, actionable, and achievable within project constraints (timeline, resources, and scope).
* **SA Actions**:

  + Perform side-by-side analysis of software engineering criteria and SA criteria:
    - Ensure alignment across all deliverables.
    - Validate interdependencies (e.g., SA criteria often rely on outputs validated through engineering testing processes).
    - Confirm alignment to stakeholder priorities for mission goals, security, and reliability.
  + Recommend changes if criteria are overly restrictive, ambiguous, or unaligned with the system’s operational environment.
* **Objective Evidence**:

  + Reports documenting SA assessments of alignment, completeness, and gaps in engineering and SA criteria.
  + Correspondence with stakeholders showing agreement or resolution of identified issues.

### 7.4.2 Guidance for Developing Detailed Acceptance Criteria

The following best practices apply to software assurance product acceptance criteria and general software acceptance criteria development, with guidance tailored for traditional and Agile projects.

#### Key Focus Areas for Acceptance Criteria

1. **Completion Criteria**:

   * Ensure all documented deliverables (e.g., code, tests, data, reports) meet planned functional and quality objectives.
2. **Correctness Criteria**:

   * Validate results through independent reviews or audits.
   * Ensure any non-conformances are addressed before approval.
3. **Risk Criteria**:

   * Verify that hazard mitigation and risk assessment activities are performed and appropriate risk levels are achieved.
4. **Verification of Requirements**:

   * Confirm successful execution of all test plans, system-level and safety-specific validation activities, including any regression testing results.
5. **Reliability**:

   * Perform analyses based on documented reliability goals. For example, ensure all safety-critical functions meet target reliability thresholds and failure scenarios have been tested.
6. **Documentation and Data**:

   * Confirm that accompanying deliverables (e.g., user manuals, test cases, hazard reports, and defect logs) are completed, organized, and configuration managed.

#### Agile and Incremental Projects

SA personnel play a key role in ensuring acceptance criteria align with Agile workflows:

1. **Definition of “Done” (DoD)**:

   * Collaborate with Agile teams to define robust DoD for every sprint or task.
   * Ensure DoD for each sprint aligns with system-wide acceptance criteria, such that the accumulated deliverables meet project-level goals.
2. **Daily and Sprint Verification**:

   * Monitor testing during sprints to validate functionality, reliability, and safety.
   * Ensure test artifacts (e.g., test cases, documentation, updates) are captured, linked to acceptance criteria, and configuration managed.
   * Confirm regression testing during daily activities incorporates new features and checks for adverse impacts on prior sprint deliverables.
3. **Periodic Assessments of Sprint Products**:

   * Perform interim reviews (per sprint or release) to verify cumulative sprint outputs meet interim acceptance goals.
   * Ensure all acceptance-related deliverables (e.g., requirements validation, safety ratings, quality checks) are built incrementally.
4. **Final Build Review**:

   * Ensure all acceptance criteria are met for the final integrated release, including any late-stage testing requirements for reliability, safety, and operational readiness.

#### Additional Considerations

**Communication**:

* Foster regular collaboration between SA, project teams, and stakeholders to ensure that acceptance goals remain well-defined and traceable.
* Provide periodic updates to all stakeholders regarding SA performance versus acceptance plans.

**Continuous Review**:

* Conduct periodic audits of acceptance criteria and processes to address deficiencies early in the lifecycle.
* Use lessons learned to improve future acceptance practices.

## 7.5 Additional Guidance

Additional guidance related to acceptance testing may be found in the following related requirements in this handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) |

# 8. Objective Evidence

Objective evidence is a collection of verifiable artifacts, records, and documentation that demonstrate compliance with the requirement. The **Software Assurance (SA) team** is responsible for identifying, collecting, and maintaining this evidence to show that acceptance criteria are well-defined, correctly documented, validated, and aligned with project requirements and objectives.

By ensuring these objective evidence items are gathered, Software Assurance personnel can confirm that the project is in full compliance with the requirement, demonstrating that acceptance criteria are properly defined, documented, and validated for successful software delivery.

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

This guidance outlines key categories of objective evidence that Software Assurance personnel must produce to confirm compliance with this requirement.

## 8.1 Evidence of Documented Acceptance Criteria

### 8.1.1 Acceptance Criteria Documentation

* **Description**: Evidence that acceptance criteria have been defined and properly documented by the project manager.
* **Artifacts**:
  + Software Requirements Specification (SRS), with documented acceptance criteria traced to each requirement.
  + A standalone Acceptance Plan or section within the Software Management Plan (SMP), outlining acceptance criteria for deliverables.
  + Agile artifacts (e.g., Definition of Done, Sprint/Releases Acceptance Checklist).
* **SA Role**:
  + Validate that the document exists, is complete, traceable, and has been reviewed for accuracy.
  + Ensure that acceptance criteria align with the software lifecycle classification and system objectives.

### 8.1.2 Traceability Matrix

* **Description**: Evidence that acceptance criteria are traceable to specific requirements, objectives, or stakeholder expectations.
* **Artifacts**:
  + Requirements Traceability Matrix (RTM), linking requirements to acceptance criteria, test cases, and validation methods.
  + Verification Matrix showing how each criterion will be validated/tested.
* **SA Role**:
  + Verify that all acceptance criteria are fully traced to project requirements or other approved sources (e.g., customer agreements, safety standards).

### 8.1.3 Stakeholder Approved Acceptance Criteria

* **Description**: Evidence that the acceptance criteria have been reviewed and approved by relevant project stakeholders.
* **Artifacts**:
  + Stakeholder meeting minutes referencing discussion and approval of the acceptance criteria.
  + Email correspondence or signed approval documents (e.g., confirmation that stakeholders agree with the criteria).
* **SA Role**:
  + Review stakeholder feedback records and ensure appropriate sign-off has been obtained.

## 8.2. Evidence of Validation and Completeness

### 8.2.1 Validation Plans

* **Description**: Evidence that plans have been established to verify and validate acceptance criteria.
* **Artifacts**:
  + Software Test Plan (STP), highlighting validation methods for each acceptance criterion.
  + Software Test Description documents with detailed test procedures for validating acceptance.
  + Agile task boards, showing completed stories meeting the Definition of Done (DoD) and mapped to acceptance criteria.
* **SA Role**:
  + Confirm that planned tests or other verification methods adequately validate the documented criteria.

### 8.2.2 Validation Results

* **Description**: Test execution results that demonstrate compliance with acceptance criteria.
* **Artifacts**:
  + Test Results Reports, showing successful execution of tests tied to acceptance criteria.
  + Test logs and defect reports addressing issues related to acceptance criteria validation.
  + Simulation results, code reviews, or peer reviews conducted to verify compliance.
* **SA Role**:
  + Check that all tests or reviews corresponding to acceptance criteria have been executed and recorded.
  + Verify defect logs to confirm that any issues related to acceptance criteria have been resolved.

### 8.2.3 Corrective Action Evidence

* **Description**: Records showing issues identified during validation have been resolved or mitigated.
* **Artifacts**:
  + Corrective Action Request (CAR) logs, documenting actions taken to fix gaps in meeting acceptance criteria.
  + Issue tracking records showing all issues closed or reduced to acceptable risk before final acceptance.
* **SA Role**:
  + Validate that all critical corrective actions are tracked to completion and outcomes are reviewed.

## 8.3 Evidence of Software Assurance and Safety Activities

### 8.3.1 SA-Developed Acceptance Criteria

* **Description**: Evidence of acceptance criteria specifically developed for Software Assurance and Software Safety products (e.g., hazard analyses, compliance audits).
* **Artifacts**:
  + Software Assurance and Software Safety Plan, explicitly defining criteria for SA and safety deliverables.
  + Evidence logs for completion, review, and approval of SA artifacts (e.g., safety case analyses, fault trees).
* **SA Role**:
  + Ensure that SA and safety plans include specific, documented, and traceable acceptance criteria for their work products.

### 8.3.2 Audit and Review Artifacts

* **Description**: Records demonstrating that SA personnel audited engineering plans, processes, and artifacts to ensure compliance with acceptance criteria.
* **Artifacts**:
  + SA audit reports highlighting findings and recommendations on acceptance criteria completeness, correctness, and alignment.
  + Results of milestone reviews (e.g., PDR, CDR), with SA assessments of acceptance criteria compliance.
* **SA Role**:
  + Confirm that audit and review findings align with the documented acceptance standards for software deliverables.

## 8.4 Agile and Incremental Development Evidence

### 8.4.1 Sprint-Level Validation of Criteria

* **Description**: Evidence that acceptance criteria were validated incrementally during Agile development cycles.
* **Artifacts**:
  + Definition of Done (DoD) documentation for each sprint, traceable to higher-level acceptance criteria.
  + Sprint demonstration (demo) reports showing that interim deliverables met acceptance expectations.
  + Daily build/test logs for continuous integration activities and regression testing.
* **SA Role**:
  + Verify that Agile artifacts (e.g., DoD) include specific criteria related to safety, quality, and functionality, and that criteria are validated within the sprint cycle.

#### 8.4.2 Final Integrated Build Compliance

* **Description**: Objective evidence that the final integrated system meets all acceptance criteria established during the project.
* **Artifacts**:
  + Release Checklists mapping final software deliverables to acceptance criteria and verification results.
  + Verification reports confirming compliance of integrated software with performance, reliability, and safety expectations.
* **SA Role**:
  + Ensure the final build is validated against all documented acceptance criteria, and discrepancies are resolved.

## 8.5 Evidence from Stakeholder Alignment

#### 5.1 Communication and Review Records

* **Description**: Documentation of the collaborative process between the project team, Software Assurance, and stakeholders.
* **Artifacts**:
  + Review meeting records summarizing discussions of acceptance criteria.
  + Stakeholder survey or feedback results confirming alignment on deliverables and criteria.
* **SA Role**:
  + Check that stakeholder priorities are adequately integrated into the acceptance criteria.

### 8.5.2 Customer Approval Records

* **Description**: Evidence that the customer has reviewed and approved the acceptance criteria and final product.
* **Artifacts**:
  + Formal sign-off documents (e.g., Software Acceptance Report, Contract Acceptance Letters).
  + Customer review reports demonstrating final assessment of delivered software.
* **SA Role**:
  + Ensure formal approval is obtained for acceptance of delivered software.

## 8.6 Process Compliance Evidence

### 8.6.1 Standards and Process Alignment

* **Description**: Evidence showing that acceptance criteria and associated processes align with NASA standards and guidelines.
* **Artifacts**:
  + Compliance checklists for NASA-HDBK-2203 and NASA Software Engineering Handbook standards.
  + Gap analysis reports showing any deviations from standards and how they were addressed.
* **SA Role**:
  + Verify alignment with required NASA standards for developing and documenting acceptance criteria.

### 8.6.2 Configuration Management Records

* **Description**: Evidence that acceptance criteria and associated documents are under configuration control.
* **Artifacts**:
  + Version-controlled acceptance criteria records.
  + Configuration management logs showing traceability of criteria changes and approvals.
* **SA Role**:
  + Confirm that version control practices are applied and that changes to acceptance-related artifacts are properly tracked.

## 8.7 Summary of Objective Evidence Categories

| Category | Key Artifacts |
| --- | --- |
| Documented Acceptance Criteria | Acceptance Plan, Requirements Traceability Matrix, Stakeholder approvals. |
| Validation and Completeness | Test Results Reports, Validation Plans, Corrective Action Logs. |
| Software Assurance Activities | SA Audit Reports, Safety Plan Acceptance Criteria, Compliance Assessments. |
| Agile Evidence | Sprint DoD, Daily Regression Testing Logs, Integrated Build Validation Reports. |
| Stakeholder Alignment | Stakeholder Review Notes, Customer Sign-Off Documents, Communication Meeting Records. |
| Process Compliance | Standards Compliance Checklists, Gap Analysis Reports, Configuration Management Logs. |

See also [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing),
