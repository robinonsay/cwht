# SWE-140 - Comply with Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695498. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements

SWE-140 - Comply with Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695498)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695498&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

# 1. Requirements

2.1.5.4 Center Director, or designee, shall comply with the requirements in this directive that are marked with an “X” in Appendix C.

## 1.1 Notes

The responsibilities for approving changes in the requirements for a project is listed for each requirement in the requirement mapping matrix. When the requirement and software class are marked with an “X,” the projects will record the risk and rationale for any requirement that is not completely implemented by the project. The projects can document their related mitigations and risk acceptance in the approved Requirements Mapping Matrix. Project relief from the applicable cybersecurity requirements, Section 3.11, Software Cybersecurity, has to include an agreement from the SAISO or Center CISO, as designated by the SAISO. The NASA Agency CIO, or Center CIO designee, has institutional authority on all Class F software projects.

## 1.2 History

Click here to view the history of this requirement: SWE-140 History

SWE-140 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 6.3.5 When the requirement and software class are marked with a "P (Center)," Centers and projects shall meet the requirement with an approved non-null subset of the "shall" statement (or approved alternate) for that specific requirement. |
| Difference between A and B | Removed the "P(Center)" designation along w/ updates made to Appendix D: Requirements Mapping Matrix |
| B | 2.1.3.4 Center Directors, or designees, shall comply with the requirements in this directive that are marked with an “X” in Appendix C. |
| Difference between B and C | No change |
| C | 2.1.5.4 Center Director, or designee, shall comply with the requirements in this directive that are marked with an ”X” in Appendix C. |
| Difference between C and D | No change |
| D | 2.1.5.4 Center Director, or designee, shall comply with the requirements in this directive that are marked with an “X” in Appendix C. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The purpose of this requirement is to reduce the risk associated with software development and use on NASA projects. This requirement emphasizes the accountability of the Center Director, or their designee, in ensuring compliance with specific, mandatory software engineering requirements outlined in the directive. The requirements marked with an "X" in Appendix C of **NPR 7150.2** [083](#_tabs-<p></p>) are mandatory, and adherence is critical for maintaining the safety, reliability, and effectiveness of NASA’s software development and engineering processes.

By assigning responsibility for compliance, NASA ensures that each Center operates in alignment with Agency-wide software engineering standards and best practices, minimizing risks and ensuring mission success.

## 2.1 Key Rationale for the Requirement

### 1. Ensures Standardization Across Centers

* **Why This Is Important**: NASA operates through multiple Centers, each with unique projects, missions, and constraints. While individual Centers may tailor some practices, compliance with the requirements marked in Appendix C ensures consistent application of key principles and processes across all Centers.
* **Implications**:
  + Standardization minimizes variability that could compromise software safety, quality, or reliability.
  + It fosters cohesive collaboration among Centers, contractors, and external stakeholders, especially when multiple Centers contribute to the same mission.

### 2. Supports Software Classification and Criticality

* **Why This Is Important**: The requirements in Appendix C of **NPR 7150.2** are carefully selected based on the classification (e.g., Classes A, B, C, D, E, F) and criticality (e.g., mission-critical, safety-critical) of the software. Compliance ensures that:
  + High-criticality software (like human-rated systems) adheres to strict development, assurance, and verification standards.
  + Less critical software, although less rigorous, still meets baseline requirements for quality and risk management.
* **Example**: For Class A software, the highest level of rigor applies to ensure system safety and reliability, as it may involve crewed missions or safety-critical systems. By following Appendix C, each Center commits to applying the appropriate level of scrutiny.

### 3. Reduces Risk to Missions, Personnel, and Assets

* **Why This Is Important**: Non-compliance with mandatory requirements increases the likelihood of software defects, system failures, mission delays, and safety risks. Such issues can have cascading impacts, including:
  + Loss of critical data or asset (e.g., a satellite, rover, or spacecraft).
  + Increased costs for troubleshooting, redesigns, or rework.
  + Endangerment of personnel or the public (e.g., during launch or system operations).
* **Historical Context**:
  + The **Mars Climate Orbiter (1999)** failed due to a software interface error between metric and imperial units, stemming from inadequate process compliance and verification at the project level.
  + The **Ariane 5 Flight 501 (1996)** failure due to unhandled software exceptions highlights the importance of rigorous compliance in flight-critical systems.

### 4. Ensures Compliance with NASA’s Policy Framework

* **Why This Is Important**: The requirements in Appendix C of **NPR 7150.2** are directly aligned with NASA's overarching software engineering directive (e.g., **NPR 7150.2**). Compliance ensures:
  + Adherence to Agency-level mandates and objectives.
  + Alignment with external standards, such as NASA Procedural Requirements (NPRs), the NASA Software Engineering Handbook, and industry standards (e.g., CMMI **[689](#_tabs-<p></p>)**, **IEEE 12207 [224](#_tabs-<p></p>)**).
* **Consequence of Non-Compliance**: Failure to comply with Appendix C requirements could result in audits, delays, or corrective action plans that consume resources and impact program schedules.

### 5. Establishes Accountability at the Center Level

* **Why This Is Important**: By placing the responsibility on the Center Director or their designee, this requirement ensures measurable accountability for compliance. This leadership accountability:
  + Creates a clear line of responsibility for ensuring that processes, activities, and standards are followed.
  + Promotes a culture of responsibility, where deviations from mandatory requirements are identified and corrected early.
* **How It Helps**: Accountability ensures that non-compliance risks are escalated, documented, and resolved promptly, avoiding project impacts at NASA or Center levels.

### 6. Provides Tailoring While Ensuring Mandatory Compliance

* **Why This Is Important**: NASA allows Centers to tailor processes to fit specific mission needs using approved engineering judgment and waiver processes. However, the requirements in Appendix C of **NPR 7150.2** are non-negotiable and ensure that no tailoring compromises:
  + Safety, reliability, or mission assurance.
  + Core compliance with Agency-mandated software policies.
* **Example**: While a Center may use Agile methodologies for development (tailored from waterfall processes), it must still meet requirements like adequate testing, configuration management, and safety-critical analysis.

### 7. Facilitates Reviews and Gatekeeping

* **Why This Is Important:** **NPR 7150.2,** Appendix C requirements often include mandatory compliance checkpoints (e.g., gate reviews, entrance/exit criteria) that ensure software is prepared to transition between lifecycle phases. Compliance allows:
  + Clear demonstration that readiness criteria are met.
  + Prevention of software or system integration with unresolved risks.
* **Examples of Such Reviews**:
  + **Preliminary Design Review (PDR)**: Verifies readiness to proceed to the design phase.
  + **Test Readiness Review (TRR)**: Confirms the software is ready for testing.
  + **Software Acceptance Review (SAR)**: Ensures delivered software meets contractual and quality standards.

### 8. Promotes Continuous Improvement

* **Why This Is Important**: Lessons Learned and feedback from software projects are often integrated into updated versions of directives like **NPR 7150.2**. Centers adhering to **NPR 7150.2,** Appendix C ensure their compliance reflects the latest best practices and incorporates critical lessons from NASA’s history.
* **Example**:
  + Updated requirements in Appendix C may include new cybersecurity practices to mitigate evolving threats.

### 9. Strengthens Contractor Oversight

* **Why This Is Important**: Many NASA projects involve contractor-developed software. Compliance with the requirements in **NPR 7150.2,** Appendix C ensures:
  + Contractor deliverables meet NASA’s expectations.
  + Clear benchmarks for contractor oversight, ensuring that software quality and safety do not fall below NASA standards.
* **Actionable Benefit**:
  + Centers can use Appendix C requirements to audit or inspect contractor capabilities during milestones or delivery reviews.

### 10. Ensures Mission Cost and Schedule Integrity

* **Why This Is Important**: Requirements in **NPR 7150.2,** Appendix C often emphasize processes and activities that mitigate common causes of project delays, cost overruns, and rework. Compliance enables:
  + Early identification and resolution of design or software risks.
  + More accurate cost and schedule estimation, preventing cascading impacts later.
* **Example**:
  + Ensuring thorough requirements verification and validation processes as outlined in Appendix C avoids issues like incomplete requirements causing late-stage changes.

## 2.2 Conclusion

This requirement ensures that NASA Centers consistently apply a baseline level of software engineering rigor as defined by the mandatory requirements in Appendix C of **NPR 7150.2**. By doing so:

1. Centers enhance the quality, safety, and reliability of software systems critical to mission success.
2. Agency-wide software practices are standardized, fostering collaborative development and avoiding variability-related risks.
3. Leadership accountability ensures focus on adherence, early issue detection, and continuous learning from past experience.

Complying with these non-negotiable requirements allows NASA to achieve its technical, operational, and safety objectives across a variety of complex missions, paving the way for sustainable and innovative advancements in space exploration, research, and technical development.

# 3. Guidance

## 3.1 Using the Compliance Matrix

Compliance with the requirements marked with an "X" in **NPR 7150.2** [083](#_tabs-<p></p>), Appendix C ensures adherence to NASA’s policy as outlined in **NPD 7120.4 [257](#_tabs-<p></p>)**. These requirements establish a consistent and mandatory framework for protecting the Agency’s investments in software engineering products, fulfilling NASA's responsibility to deliver safe, reliable, and quality software to support its missions and advance science and technology for the citizens of the United States.

### 3.1.1  Objectives of the Compliance Matrix

* **Protect the Agency's Investment**: The compliance matrix establishes a common foundation to reduce risks associated with software development and ensure delivery of high-quality products that align with mission objectives.
* **Enable Collaboration Across Centers**: By providing a standardized framework of requirements, the matrix fosters seamless communication and collaboration among Centers by eliminating variability in software engineering practices.
* **Mitigate Risk**: **NPR 7150.2** defines requirements that systematically reduce software engineering risks by addressing critical aspects such as system safety, mission assurance, and software quality.

### 3.1.2  Key Features of NPR 7150.2

* **Baseline Requirements**: **NPR 7150.2** delineates a default set of requirements (marked as "X") that apply depending on software classifications and safety-criticality.
  + **Software Classification**: Hardware/software systems are assessed according to their criticality to mission success, human safety, and cost implications.
  + **Safety-Criticality**: Special focus is given to requirements that directly impact human safety and overall system reliability.

### 3.1.3  Documentation of Compliance

Each project documents its compliance with the **NPR 7150.2** requirements in the Requirements Compliance Matrix (see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)). This matrix contains:

* **Tailoring**: Adjustments or modifications made to the requirements based on project-specific circumstances. Tailoring is applied to balance compliance and practicality without compromising safety or mission objectives.
* **Waivers and Deviations**: Any approved exceptions to the requirements (partial or complete relief) granted by the designated Technical Authorities.
* **Associated Risk**s: If relief is granted, the matrix includes:
  + Risks associated with the deviation.
  + Mitigation strategies to address any impact on project safety, reliability, or schedule.
  + Clear rationale behind the need for relief, including evidence that the requirement is impractical or imposes undue burden on the software effort based on its classification, criticality, or scope.

### 3.1.4  Supporting References:

Beyond the compliance framework, extra review steps enhance the quality and accuracy of matrices:

* [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices): Guidance for Office of the Chief Engineer (OCE) review of Requirements Mapping Matrices.
* [SWE-212 - NASA-STD-8739 Mapping Matrices](/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices): Instructions on mapping Software Assurance tasks to **NPR 7150.2** requirements.

## 3.2 Requests for Software Requirements Relief

Projects occasionally encounter situations where full compliance with a requirement is impractical or unnecessary due to constraints, mission scope, or tailored project needs. In these cases, requests for software requirements relief may be submitted for consideration and approval.

**Steps for Requesting Relief**:

1. **Submission of a Compliance Matrix**:

   * To request partial or complete relief, project managers submit a tailored compliance matrix to the appropriate Technical Authority listed in Appendix C.
2. **Approval Process**:

   * Approval requires signatures from designated Technical Authorities:
     + Engineering, Safety and Mission Assurance (SMA): For assessing safety and system engineering risks from relief.
     + CIO (Chief Information Officer): If applicable, for oversight of cybersecurity or digital infrastructure concerns.
   * The responsible parties will review the variances, associated risks, and mitigation strategies before approving relief.
3. **Documentation of Rationale and Risks**:

   * Ensure that the compliance matrix transparently captures:
     + The rationale for requesting relief.
     + Any associated risks and how they are mitigated.
   * Relief must not compromise mission assurance, safety, or compliance with Agency-level policies.

**Supporting References:**

For expanded guidance:

* + [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations): Tailoring considerations that enable thoughtful adjustments to requirements without increasing risks or barriers to mission success.
  + [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements): Guidance on "Shall" statements to clarify when compliance with requirements is mandatory, or where tailoring/relief may be appropriate.

## 3.3 Requirements by Software Class

### 3.3.1  Understanding the Classification Framework:

The Requirements Mapping Matrix in **NPR 7150.2** designates requirements by software classifications and safety-criticality. Each classification defines the applicability of specific requirements based on the criticality, complexity, and cost implications of the software effort.

### 3.3.2  Key Elements in the Matrix:

1. **Classification of Software Projects**:  
   Each software project is assigned a classification based on its risk, importance to the mission, and scope:  
   * Class A: Mission-critical software for human spaceflight or systems essential to crew safety.
   * Class B: Software supporting critical mission objectives but not directly related to human spaceflight.
   * Class C: Software with moderate risk; may support less significant mission objectives.
   * Class D and E: Low-risk software for support operations or general use.
2. **Institutional vs. Project Requirements**:
   * Institutional Requirements:

     + These are global, systemic requirements levied on NASA Headquarters and Centers.
     + They focus on ensuring overarching mission success and addressing risks that span multiple programs, projects, or Centers. Examples include requirements:
       - Managed oversight by OCE and SMA.
       - Consistent Center-wide policies for training and lifecycle management.
   * Project Requirements:

     + Applied specifically to project managers conducting software development at the program/project level.
     + Focused on ensuring software deliverables align with specific mission objectives and lifecycle requirements such as:
       - Configuration management.
       - Testing and validation.
       - Risk assessments and defect tracking.

### 3.3.3  Application of Requirements:

* Requirement applicability (marked “X”) is determined by:
  + Software classification (A–E).
  + Safety-criticality as determined through system engineering processes.
* Projects apply mandatory activities for their classification while tailoring requirements, as needed (under strict approval), to accommodate mission constraints.

## 3.4 Additional References for Compliance and Requirements Management

NASA provides detailed guidance and supporting materials to help Centers and programs effectively use the compliance matrix and apply associated requirements:

* [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices): Guidance on reviewing Requirements Mapping Matrices with OCE oversight.
* [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix): Instructions for documenting compliance, tailoring, and relief in the compliance matrix.
* [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations): Tailoring considerations to balance flexibility with risk mitigation.
* [SWE-212 - NASA-STD-8739 Mapping Matrices](/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices): Mapping Software Assurance tasks to **NPR 7150.2** requirements.
* [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements): Clarification of mandatory “shall” statements and how they apply in practice.

## 3.4 Institutional Requirements

Center Directors are responsible for institutional requirements (shown in Book B of this Handbook) and ensuring that projects fulfill project requirements identified in Appendix C of **NPR 7150.2**. The Center Director or designee regularly reviews the compliance matrix to make sure that projects remain in compliance with their approved requirements set.

Downloadable compliance matrices for each class of software are available for NASA users in the Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) and Tab 4 of Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) (Software Assurance Requirements Mapping Matrix)

## 3.5 Conclusion

The Requirements Mapping Matrix in Appendix C of **NPR 7150.2** provides a structured framework for ensuring NASA software development efforts meet Agency mandates for quality, safety, and mission success. Through compliance, requests for relief, and institutional/project distinctions, this matrix empowers Centers to balance flexibility and rigor while maintaining alignment with NASA’s overarching policies and goals. By integrating this guidance into their workflows, Centers can consistently adopt best practices across all software classifications and projects.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-029 - Validation Planning](/pages/viewpage.action?pageId=102695284) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices) * [SWE-212 - NASA-STD-8739 Mapping Matrices](/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.12 - Basics of Software Auditing](https://swehb.nasa.gov/display/SWEHBVD/8.12+-+Basics+of+Software+Auditing) * [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.59 - Audit Reports](https://swehb.nasa.gov/display/SWEHBVD/8.59+-+Audit+Reports) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small projects often face unique constraints such as limited resources, budgets, and schedules. This tailored guidance provides clear and practical steps to help small projects fulfill this requirement while balancing compliance, flexibility, and mission success.

This requirement ensures that small projects adhere to the minimum set of software engineering standards defined in Appendix C of **NPR 7150.2** [083](#_tabs-<p></p>). The requirements marked with an "X" are **non-negotiable** activities that keep software development aligned with NASA's high standards for quality, safety, and reliability.

For small projects, it’s critical to achieve compliance in a lightweight and efficient manner while addressing only the requirements applicable to the project's classification and safety-criticality. Tailoring these requirements, when necessary, can help align compliance with project constraints.

## 4.1 Guidance for Small Projects

### 4.1.1  Determine Software Classification and Safety-Criticality

Small projects must begin by determining the classification and safety-criticality of their software, as this defines the applicability of the requirements in **NPR 7150.2**, Appendix C.

* **Steps to Determine Classification**:

  + Refer to the definitions provided in **NPR 7150.2**, Appendix D, to identify the appropriate classification (A–F).
  + Consult with the Engineering Technical Authority (ETA) if there is uncertainty about classification decisions.
  + Document the software classification and safety-criticality in the project’s compliance matrix (see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)).
* **Example**:

  + A Class D or E software project that focuses on supporting ground-based operations will have fewer mandatory requirements compared to a Class A or B project that involves flight-critical components.

### 4.1.2  Use the Compliance Matrix to Identify Applicable Requirements

The Requirements Mapping Matrix (RMM) a.k.a. Compliance Matrix is a central tool for small projects to identify, plan, and track compliance with the requirements.

* **Steps for Compliance Using the Matrix**:

  1. **Review Appendix C**: Highlight the requirements marked with an "X" for your project's software classification and safety-criticality.
  2. **Tailor as Necessary**: For requirements that are not practical or applicable, submit a tailoring request or seek relief (see section 3.5 below).
  3. **Document Justifications**: In the compliance matrix, include details such as tailoring justifications, risks, and approved waivers or deviations.
  4. **Mitigate Risks:** For waived requirements, document the risks and any mitigation strategies planned to ensure mission success.
* **Tips for Small Projects**:

  + Focus initially on high-impact requirements (e.g., testing, verification, and safety assurance) to address project-critical risks.
  + Reuse existing compliance matrices from similar small projects—consult the Center’s **Process Asset Library (PAL)** [197](#_tabs-<p></p>) or the Software Engineering Process Group (SEPG) for templates.

### 4.1.3  Tailor Requirements Based on Project Needs

Small projects may not require full implementation of every applicable requirement. Tailoring allows the project to adjust the scope of certain requirements based on constraints while still meeting the intent of the directive.

* **How to Tailor Requirements**:

  + Collaborate with the relevant Technical Authorities (e.g., Engineering, Safety and Mission Assurance) to determine tailoring options.
  + Document tailored requirements in the compliance matrix, including:
    - Rationale for tailoring.
    - Any alternate approaches used to achieve the requirement's intent.
  + For example, small projects may tailor complex configuration management practices to lightweight tools (e.g., GitHub for version control).
* **Basic Tailoring Examples for Small Projects**:

  + **Documentation**: Replace lengthy formal documents with checklists or one-page summaries.
  + **Testing**: Use simplified test plans to verify requirements.
  + **Reviews**: Conduct informal peer reviews rather than larger, formal review boards.

### 4.1.4  Focus on Risk-Driven Compliance

Small projects should prioritize compliance with high-risk requirements that have the most direct impact on:

* **Safety**: For software that interfaces with humans or hardware that could fail catastrophically.
* **Mission Success**: For software components critical to achieving core mission objectives.
* **Steps for Risk-Driven Compliance**:

  + Conduct a brief risk assessment tied to the requirements in **NPR 7150.2**, Appendix C.
  + Prioritize implementing requirements that mitigate mission-critical and safety-critical risks.
  + For lower-risk requirements, tailor implementation where justified.

### 4.1.5  Handling Waivers and Deviations

In cases where full compliance with a requirement is impractical for a small project, seek relief in the form of waivers or deviations.

* **Steps to Request Relief**:

  1. Identify the requirement(s) that cannot be fully implemented.
  2. Justify the need for relief, specifying why the requirement is not feasible or necessary for your project (e.g., due to schedule, scope, low risk).
  3. Use a streamlined compliance matrix to document the rationale, associated risks, and mitigation strategies.
  4. Submit the request to the designated Technical Authorities for review and approval.
* **Tips for Small Projects**:

  + Focus waiver requests on low-risk areas or requirements that would disproportionately impact the project timeline and resources.
  + Highlight alternative measures that reduce risks despite the waiver.

### 4.1.6  Focus on Lightweight Tools and Processes

Resource constraints often mean small projects need to avoid unnecessary overhead while maintaining compliance. Leverage lightweight tools and agile processes to address requirements efficiently.

* **Examples of Lightweight Implementations**:
  + **Configuration Management** ([SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management)): Use a hosted version control system like GitHub to ensure source code access, traceability, and versioning without additional complexity.
  + **Testing and Validation** ([SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)): Use automated test tools such as JUnit (for Java) or Pytest (for Python) to streamline functional and unit tests.
  + **Issue Tracking** ([SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)): Employ simple tools like Jira or Trello to track defects and monitor progress.
  + **Requirements Management** ([SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements)): Use minimal tools like Microsoft Word or Excel for maintaining a traceability matrix when dedicated tools are not available.

### 4.1.7  Use Existing Templates and Resources

Small projects often benefit from reusing processes, tools, and templates rather than creating new ones from scratch.

* **Recommended Resources**:

  + Consult the Center’s **Process Asset Library (PAL)** for ready-to-use compliance matrices tailored to small projects.
  + Engage with the Software Engineering Process Group (SEPG) for streamlined processes, tools, and lessons learned from similar projects.
* **Examples of Resources**:

  + Pre-filled compliance templates specific to low-criticality software (e.g., Class D or E).
  + Simplified checklists for development and verification activities.

### 4.1.8  Conduct Peer Reviews Instead of Formal Reviews

While formal reviews like Preliminary Design Reviews (PDRs) or Critical Design Reviews (CDRs) are required for larger projects, small projects can often substitute these with peer reviews.

* **Benefits of Peer Reviews**:

  + Less resource-intensive while still catching potential errors in requirements, design, or code.
  + Ideal for Class C, D, or E small software projects.
* **Tips**:

  + Ensure reviewers have relevant expertise and an independent perspective.
  + Document findings and corrective actions from peer reviews in a lightweight review report.

## 4.2 Small Project Checklist for Compliance

1. **Classification and Safety-Criticality**:
   * Identify software classification and document safety-criticality.
2. **Compliance Matrix**:
   * Use a requirements compliance matrix (see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)) to document mandatory and tailored requirements.
   * Include rationale for tailoring, risks, and waivers where applicable.
3. **Tools and Processes**:
   * Use lightweight tools for configuration management, testing, and tracking.
   * Reuse existing templates and processes from the Center’s library.
4. **Tailoring**:
   * Submit requests for tailored requirements or relief with clear justification and risk mitigations.
5. **Testing and Verification**:
   * Focus on high-risk areas with simplified test plans or automation.
6. **Reviews**:
   * Leverage peer reviews or combined lifecycle reviews to reduce overhead.

## 4.3 Conclusion

For small projects, compliance with Appendix C of **NPR 7150.2** is attainable through a combination of lightweight implementations, tailoring, and focused risk management. Leveraging streamlined tools, shared resources, and tailored requirements ensures that small projects can maintain NASA-standard software quality while balancing limited resources and mission constraints. This approach enables small projects to stay nimble, cost-effective, and aligned with Agency goals.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-261)

  [NASA Governance and Strategic Management Handbook,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=0C "Click to open in new window")

  NPD 1000.0C, NASA Governance and Strategic Management Handbook, Effective Date: January 29, 2020, Expiration Date: January 29, 2025
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
* (SWEREF-683)

  [Anomalous Flight Conditions May Trigger Common-Mode Failures in Highly Redundant Systems](http://llis.nasa.gov/lesson/1778 "Click to open in new window")

  Public Lessons Learned Entry: 1778, Date: 2007-03-6. Submitting Organization: JPL, Submitted by: Martin Ratliff
* (SWEREF-689)

  [CMMI Model - Overview](https://cmmiinstitute.com/dashboard "Click to open in new window")

  Capability Maturity Model Integration (CMMI) Model V3.0, ISACA, April 6, 2023,  NASA users can access the CMMI models with a CMMI Institute account at: https://cmmiinstitute.com/dashboard. Non-NASA users may purchase the document from: https://cmmiinstitute.com

## 5.2 Tools

## Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN).  NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN. The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Implementing and complying with the requirements marked in Appendix C of **NPR 7150.2 [083](#_tabs-<p></p>)** involves applying lessons learned from past NASA projects where software engineering practices either contributed to mission success or highlighted areas for improvement. Below are detailed lessons learned from the NASA **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** that directly support the intent of this requirement.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Mars Climate Orbiter Mishap [529](#_tabs-<p></p>)

* **Lesson Number:** LLIS-0938
* **Title:** **Unit Conversion Error in the Mars Climate Orbiter Mission**
* **Summary**: **The failure of the Mars Climate Orbiter (1999) was attributed to a software error caused by the use of incompatible units—imperial vs. metric—between different teams. This issue highlighted a critical failure in systems-level requirements validation and verification and underscored the importance of standardization in engineering processes.**
* ****Relevant Takeaways for This Requirement**:**
  + When requirements are not consistently implemented across stakeholders (e.g., contractors, multiple Centers), costly errors can occur.
  + Compliance with **NPR 7150.2**, Appendix C ensures mandatory requirements for software validation, software interface testing (e.g., [SWE-029 - Validation Planning](/pages/viewpage.action?pageId=102695284)), and systems engineering coordination are adhered to, reducing integration risks.
* ****Actionable Application**:**
  + Small projects should double-check that their compliance matrix addresses system-level integration requirements explicitly, especially requirements that handle interfaces between software components.
  + Implement peer review and thorough validation processes ([SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)) when confirming compliance.

#### 2. Mars Polar Lander Failure [683](#_tabs-<p></p>)

* **Lesson Number:** LLIS-1778
* **Title**: Lack of Robustness in Design and Testing of the Mars Polar Lander Descent Engine Software
* **Summary:**  
  The Mars Polar Lander (1999) failed to land safely on the Martian surface due to a software error caused by premature shutdown of its descent engines. The lack of sufficient testing under realistic conditions and the absence of redundancy for critical software components were cited as underlying causes.
* **Relevant Takeaways for This Requirement**:
  + Testing ([SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)): Appendix C requirements highlight the importance of exhaustive software testing under all anticipated operating conditions. For safety-critical systems, the requirements marked "X" emphasize verification strategies that would catch issues before deployment.
  + Requirements compliance ensures software design and testing activities are robust enough to mitigate mission risks.
* **Actionable Application**:
  + Even for small projects, compliance with mandatory test requirements (e.g., [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)) should be prioritized.
  + Tailor testing requirements where applicable but ensure that critical failure scenarios are explicitly accounted for in test plans.

#### 3. Columbia Accident Investigation Findings

* **Lesson Number:** LLIS-3326)
* **Title: The Columbia Accident (2003) – Organizational Failures Related to Software and Process Oversight**
* **Summary**:  
  The catastrophic loss of Space Shuttle Columbia stemmed, in part, from organizational and communication failures within NASA, including inadequate oversight of safety-critical processes. This tragedy underscored the need for continuous organizational accountability and adherence to established safety requirements.
* **Relevant Takeaways for This Requirement**:
  + Organizational Compliance ([B. Institutional Requirements](/spaces/SWEHBVD/pages/102695220/B.+Institutional+Requirements)): Institutional requirements marked in **NPR 7150.2**, Appendix C ensure robust oversight processes, particularly for safety-related activities. Center Directors and designees play a key role in institutionalizing compliance and enforcing accountability.
  + A focus on leadership ensures that compliance with requirements is maintained at all organizational levels, regardless of project size.
* **Actionable Application**:
  + For small projects, the designee responsible for compliance should establish a lightweight compliance check process that involves early engagement of safety and mission assurance personnel.
  + Periodically assess compliance with institutional requirements to ensure no critical processes are overlooked during small-scale project planning.

#### 4. Lessons from JPL Software Engineering Process Improvement Efforts [572](#_tabs-<p></p>)

* **Lesson Number:** LLIS-2218
* **Title:** **Flight Software Engineering Lessons from JPL's Software Development Process Improvements**
* **Summary:**  
  The Jet Propulsion Laboratory (JPL) identified several best practices to reduce software risks during flight software development, including early involvement of software engineers in system design, better simulations of hardware interfaces, and using objective measures to monitor software engineering progress.
* **Relevant Takeaways for This Requirement:**
  + Compliance with Appendix C ensures systematic adherence to engineering processes such as early software involvement, development of simulations, and use of objective metrics.
  + Requirements such as [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) (software requirements development) and [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) (risk-based decision-making) ensure that software-related decisions are informed by rigorously validated architecture and risk assessments.
* **Actionable Application:**
  + Small projects should leverage lightweight tools like simulations (e.g., software-in-the-loop testing) to meet **NPR 7150.2**, Appendix C testing and verification requirements.
  + Ensure the compliance matrix explicitly incorporates checkpoints to validate software engineering progress against the requirements.

#### 5. James Webb Space Telescope (JWST) Software Development Lessons

* **Lesson Number:** LLIS-4646
* **Title:** **Managing Risks in Developing Large-Scale Software Systems (Lessons from the JWST Project)**
* **Summary:**  
  The development of software for the James Webb Space Telescope faced many challenges, including underestimating the complexity of software systems, lack of early risk identification, and insufficient attention to integration testing, which resulted in delays and cost overruns.
* **Relevant Takeaways for This Requirement:**
  + Adequate planning and compliance with mandated processes such as risk analysis ([SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)) and integration testing ([SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures)) are vital to avoid cascading development complications.
  + Even for smaller-scale systems, adhering to the requirements in **NPR 7150.2**, Appendix C provides a structured process to mitigate risks and identify integration challenges early.
* **Actionable Application:**
  + Plan integration testing as early as possible, even for small system components.
  + Include all interface-related requirements in the compliance matrix, ensuring alignment with [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) and ensuring smooth coordination between hardware, software, and systems.

#### 6. Orbital Spaceplane Software Management

* **Lesson Number:** LLIS-2943
* **Title:** **Lessons Learned from Orbital Spaceplane Software Development Challenges**
* **Summary:**  
  The Orbital Spaceplane software effort faced challenges associated with unclear requirements, inconsistent tailoring, and ineffective compliance tracking. These issues impacted software quality and delivery timelines.
* **Relevant Takeaways for This Requirement:**
  + The compliance matrix is central to ensuring consistent interpretation and adherence to software requirements. Requirements should not be tailored arbitrarily—tailoring must be systematically reviewed and approved by the appropriate Technical Authorities.
  + Institutional compliance requirements (marked in **NPR 7150.2**, Appendix C) ensure that oversight mechanisms are in place for tailoring decisions.
* **Actionable Application:**
  + For small projects, simplify compliance tracking by consolidating tailored requirements, risks, and mitigations into an accessible matrix format.
  + Engage the project’s technical authority early to validate all compliance or tailoring decisions.

#### 7. Software Assurance Lessons from the Mars Science Laboratory

* **Lesson Number:** LLIS-3170
* **Title:** **Software Development Risk Reduction for the Mars Science Laboratory (MSL)**
* **Summary:**  
  The MSL mission successfully integrated software assurance best practices by emphasizing requirements documentation, stringent testing protocols, and early involvement of assurance teams.
* **Relevant Takeaways for This Requirement:**
  + Compliance with Software Assurance Requirements (e.g.,[SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) in Appendix C) is a critical control to catch defects and ensure software safety.
  + Requirements ensure proper involvement of assurance personnel at every lifecycle phase, preventing late-stage issues.
* **Actionable Application:**
  + Small projects can leverage lightweight tools (e.g., checklists, automated static analysis tools) to meet software assurance requirements efficiently.
  + Include assurance responsibilities in the compliance matrix, ensuring a systematic review of critical software deliverables.

### 6.1.2  Conclusion

The highlighted lessons emphasize the importance of complying with the mandatory requirements in Appendix C of **NPR 7150.2**. For small projects, leveraging these historical insights can lead to improved planning, risk mitigation, and a streamlined approach to software engineering. By addressing these documented lessons, projects can reduce risks, maintain compliance, and ensure mission success, regardless of their scale.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-140 - Comply with Requirements**

2.1.5.4 Center Director, or designee, shall comply with the requirements in this directive that are marked with an “X” in Appendix C.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

None identified at this time.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support oversight, validate compliance, manage risks, and ensure the quality of delivered products. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

No specific deliverables are currently identified.

## 7.3 Metrics

No standard metrics are currently specified.

## 7.4 Guidance

### 7.4.1  Objective of the Guidance

The purpose of this requirement is to ensure that NASA Centers adhere to the specific requirements in the directive—particularly those marked with an “X” in Appendix C of **NPR 7150.2 [083](#_tabs-<p></p>)**, signifying mandatory compliance. These requirements are tailored to the classification and safety-criticality of the software being developed, acquired, or maintained.

Software Assurance (SA) personnel are responsible for verifying and ensuring that the compliance obligations of these marked requirements are fulfilled. This guidance provides clear steps for supporting the implementation and ongoing monitoring of the requirements indicated in Appendix C.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Understand the Requirements in Appendix C

1. **Review NPR 7150.2, Appendix C**:

   * Be familiar with the list of requirements in Appendix C of the directive.
   * Identify the requirements marked with an “X”, as these are mandatory for compliance based on the software’s classification, criticality, and project-specific context.
   * Be familiar with the SA Tasking in **NASA-STD-8739.8** **[278](#_tabs-<p></p>)** that corresponds to the **NPR 7150.2**, Appendix C requirements.
2. **Determine Applicability**:

   * Confirm Software Classification levels (e.g., Class A, B, C, etc.) using the criteria in **NPR 7150.2**, Appendix D.
   * Ensure there is an understanding of how these classifications affect which requirements that are marked as mandatory for the specific Center or project.

#### 7.4.2.2  Support the Center in Achieving Compliance

1. **Verify Implementation**:

   * Confirm that processes are in place to address each requirement marked with an “X”. For example:
     + Requirements related to verification and validation (V&V).
     + Requirements for tailoring, risk management, and software testing.
     + Documentation and reporting requirements in accordance with **NPR 7150.2** and related directives.
2. **Document Compliance Activities**:

   * Collaborate with Center personnel to document how each mandatory requirement is implemented.
   * Maintain records that trace compliance actions for all applicable requirements.
     + See the implementation aid in Topic [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool).
3. **Tailoring Decisions**:

   * Ensure that any requests for tailoring, waivers, or deviations from the requirements in Appendix C are justified, documented, and approved by the appropriate authority in compliance with NASA’s tailoring process.

#### 7.4.2.3  Perform Reviews and Audits

1. **Assess Compliance Status**:

   * Regularly review project activities to ensure they align with the requirements marked with an “X.”
     + Use the SA Tasking in **NASA-STD-8739.8** that corresponds to requirements marked with an “X” to aid in these reviews.
   * Confirm that each requirement is properly integrated into the software’s development or maintenance lifecycle.
2. **Conduct Audits**:

   * Include Appendix C requirements in software assurance audits and assessments per **NASA-STD-8739.8.** Verify:
     + Whether mandatory assurance activities (e.g., testing, safety assessments, peer reviews) are complete.
     + Whether artifacts (e.g., test results, metrics, or hazard analyses) meet the directive’s expectations.
   * See Topic [8.12 - Basics of Software Auditing](https://swehb.nasa.gov/display/SWEHBVD/8.12+-+Basics+of+Software+Auditing) and [8.59 - Audit Reports](https://swehb.nasa.gov/display/SWEHBVD/8.59+-+Audit+Reports) to aid in these audits and assessments.
3. **Monitor Metrics**:

   * Track progress and compliance metrics related to the execution of mandatory requirements to validate their consistent implementation.

#### 7.4.2.4  Communicate and Facilitate Compliance

1. **Promote Awareness**:

   * Work with Center leadership, project managers, and teams to ensure awareness of all Appendix C requirements marked with an “X.”
   * Provide training as needed to clarify roles and responsibilities for meeting the requirements.
2. **Report Issues or Gaps**:

   * If noncompliance with any marked requirement is identified, escalate the issue for resolution. Ensure corrective actions are taken to address gaps in compliance.
3. **Coordinate Cross-Functional Teams**:

   * Assist in coordinating between assurance, engineering, and management teams to ensure implementation of requirements across all project phases.

#### 7.4.2.5  Maintain Continuous Improvement

1. **Incorporate Lessons Learned**:

   * Use Lessons Learned from past projects to identify potential gaps or improvements in meeting Appendix C requirements.
   * Recommend updates to processes to ensure smoother compliance in future projects.
2. **Stay Current with Updates**:

   * Monitor for updates to the directive or changes in software classification and adjust compliance efforts accordingly.
3. **Provide Feedback to Leadership**:

   * Regularly report to the Center Director, or designee, on the status of compliance with Appendix C requirements, including risks, progress, and any areas needing enhancement.

### 7.4.3  Key Focus Areas for Software Assurance

1. **Thorough Documentation**:

   * Maintain comprehensive records of how marked requirements are addressed and fulfilled.
   * Ensure traceability between requirements, processes, and outcomes.
2. **Risk Management**:

   * Identify and manage risks associated with noncompliance or inadequate implementation of Appendix C requirements.
3. **Tailoring**:

   * Verify that deviations or tailoring of requirements are supported by risk analyses, formally documented, and approved.
4. **Stakeholder Awareness**:

   * Make sure all project stakeholders understand the importance of compliance with requirements explicitly marked with an “X” in Appendix C.
5. **Compliance Auditing**:

   * Conduct periodic checks to validate compliance with Appendix C requirements throughout the software lifecycle.

### 7.4.5  Expected Outcomes

Through the diligent performance of these responsibilities, Software Assurance personnel will:

1. Ensure all mandatory requirements marked with an “X” in  **7150.2,** Appendix C are properly implemented, reducing risks to software quality and safety-critical operations.
2. Facilitate a culture of compliance and accountability, helping projects meet NASA’s high standards for software reliability and performance.
3. Provide clear visibility to Center leadership of the status of compliance, including potential risks, progress, and any corrective actions.

### 7.4.6  Summary

The requirements marked with an “X” in  **7150.2**, Appendix C are non-negotiable and central to ensuring software quality, safety, and mission success. Software Assurance (SA) personnel play a critical role in verifying compliance, facilitating audits, contributing to process improvement, and maintaining documentation to meet these requirements. By ensuring proper implementation and monitoring, SA personnel directly contribute to NASA’s goal of producing reliable, high-quality software for its missions.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-029 - Validation Planning](/pages/viewpage.action?pageId=102695284) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices) * [SWE-212 - NASA-STD-8739 Mapping Matrices](/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.12 - Basics of Software Auditing](https://swehb.nasa.gov/display/SWEHBVD/8.12+-+Basics+of+Software+Auditing) * [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.59 - Audit Reports](https://swehb.nasa.gov/display/SWEHBVD/8.59+-+Audit+Reports) |
