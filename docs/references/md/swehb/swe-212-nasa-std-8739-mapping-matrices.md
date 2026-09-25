# SWE-212 - NASA-STD-8739 Mapping Matrices

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695331. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices

SWE-212 - NASA-STD-8739 Mapping Matrices

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695331)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695331&showCommentArea=true&showComments=true#addcomment)

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

2.1.2.4 The NASA Chief, SMA shall periodically review the project’s requirements mapping matrices.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-212 History

SWE-212 - Used first in NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B | RESERVED |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | First use of this SWE in D  In previous versions this was a will statement |
| D | 2.1.2.4 The NASA Chief, SMA shall periodically review the project’s requirements mapping matrices. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The NASA OSMA assesses project compliance matrices for a variety of reasons including identification of risk, the identification of patterns and trends that indicate areas of concern or potential need for requirements revision, and a general understanding of the intent of the requirements.

## 2.1 Introduction

The requirements mapping matrix is a critical tool for ensuring that all **software engineering (NPR 7150.2 [083](#_tabs-<p></p>))** and **software assurance/safety (NASA-STD-8739.8 [278](#_tabs-<p></p>))** requirements are properly mapped, implemented, verified, and validated throughout a project’s lifecycle. It details how requirements are addressed, whether they are tailored, waived, or accepted as-is, and serves as a bridge between high-level standards and practical implementation.

By periodically reviewing a project's requirements mapping matrices, the **NASA Chief, SMA (Safety and Mission Assurance)** performs a key oversight function that reduces the risk of missed, poorly implemented, or inconsistently applied requirements. This periodic review is critical to ensuring mission success, compliance, and risk mitigation for the agency’s diverse portfolio of projects.

## 2.2 Key Rationale for Periodic Reviews

### 1. Verifies Tailored Compliance with NASA Standards

* **Explanation:** Tailoring (modification, omission, or addition of requirements) is often necessary due to unique project constraints, including software classification, safety criticality, mission objectives, and resource availability. However, improperly tailored or waived requirements can create critical gaps.
* **Why It Matters:**
  + Tailored requirements must conform to the processes defined in **NPR 7150.2** and **NASA-STD-8739.8** to ensure they remain technically justified and risk-managed.
  + Tailoring decisions influence mission-critical and safety-critical software components, and unchecked tailoring could compromise compliance and reliability.
  + The periodic review ensures that requirement tailoring decisions:
    - Have been approved by the appropriate Technical Authority.
    - Are accompanied by sufficient justification and risk analysis.
    - Are implemented in ways consistent with NASA governance processes.

### 2. Ensures Traceability and Completeness Across All Lifecycle Phases

* **Explanation:** Traceability links each requirement to its corresponding implementation, verification, and validation activity, ensuring all requirements are addressed and no critical requirements are overlooked during the project lifecycle. This is critical for managing complex aerospace projects that involve numerous software systems and interfaces.
* **Why It Matters:**
  + Regular review of requirements mapping matrices ensures that:
    - All stated requirements are allocated to appropriate subsystems, software modules, or teams.
    - "Orphan" requirements (unimplemented) and "unverified" requirements (untested) are identified and resolved early.
    - Verification and validation (V&V) activities are planned and properly linked to their corresponding requirements.
  + For safety-critical and mission-critical projects, even one unmet requirement can result in mission failure or safety hazards. The periodic review prevents such gaps.

### 3. Facilitates Early Risk Detection and Mitigation

* **Explanation:** Software-related risks (e.g., incomplete implementation, noncompliance, disparate interpretations of requirements) are often rooted in unclear or incomplete mapping of requirements. Early reviews help detect risks tied to key requirements before they propagate.
* **Why It Matters:**
  + Regular assessments of mapping matrices enable projects to identify:
    - Requirements at risk of incomplete or incorrect implementation.
    - Tailored or waived requirements that introduce new hazards.
  + Preventative identification ensures that risks are managed proactively, reducing late-stage rework and improving overall project outcomes.
  + Risk analysis tied to requirements (e.g., hazard reports, safety-critical dependencies, cybersecurity priorities) ensures that high-risk areas receive appropriate resources and attention.

### 4. Reinforces Accountability and Cross-Disciplinary Communication

* **Explanation:** The requirements mapping matrix serves as a communication tool between software engineers, system engineers, safety and mission assurance teams, and other stakeholders. It ensures that all teams are aligned on what is required, what has been tailored, and how compliance is being achieved.
* **Why It Matters:**
  + Periodic review by the Chief, SMA reinforces accountability for the implementation and tracking of requirements.
  + It aids in resolving discrepancies early by bringing together multidisciplinary expertise to address unclear mappings, gaps, or risks.
  + It helps bridge communication across Centers and contractors managing different subsystems of the same project, ensuring consistency in assurance expectations.

### 5. Confirms Cybersecurity Assurance for Software Requirements

* **Explanation:** Modern NASA missions involve increasingly complex software connected to networks, making cybersecurity a critical part of software assurance. Key cybersecurity assurance requirements, such as those outlined in **NPR 7150.2 Chapter 3**, must be clearly mapped to project plans and verified throughout the lifecycle.
* **Why It Matters:**
  + A periodic review ensures cybersecurity requirements are not overlooked or improperly implemented.
  + It ensures cybersecurity assurance flows down to all contractors and is integrated into early software decisions.
  + By validating that cybersecurity-related requirements are addressed thoroughly, periodic reviews decrease the likelihood of vulnerabilities or system exploits.

### 6. Tracks Requirements Flow-Down to Contractors and Subsystems

* **Explanation:** Many NASA projects involve software developed by multiple contractors or external partners, each responsible for fulfilling specific requirements. The flow-down of requirements is critical to ensuring that external entities are aligned with NASA’s assurance standards.
* **Why It Matters:**
  + The periodic review ensures that all software-related requirements—whether safety-critical, mission-driven, or compliance-related—have been properly included in contractor agreements.
  + It validates that contractors' interpretations of requirements are consistent with expectations, reducing integration risks.

### 7. Supports Process Improvement and Lessons Integration

* **Explanation:** Periodically reviewing mapping matrices allows OSMA to identify patterns of success or deficiencies across projects. Insights gained from these reviews can then feed back into process improvements or future iterations of NASA software engineering policies (e.g., **NPR 7150.2**).
* **Why It Matters:**
  + Identifying systemic issues—such as recurring requirements gaps or implementation delays—allows NASA to refine its software engineering and assurance standards, templates, and tools.
  + Ensures that best practices and lessons learned from past projects are incorporated more effectively.

### 8. Prevents Requirements Drift Over Time

* **Explanation:** Throughout a project’s lifecycle, requirements can be modified, clarified, or even removed due to technical or programmatic constraints. Without periodic review, such modifications can lead to requirements drift, where original intent or scope is lost.
* **Why It Matters:**
  + Reviewing the mapping matrix periodically ensures that:
    - Modifications or deletions are justified and documented.
    - Requirements adjustments remain consistent with overall program goals and standards.
  + Proactively guards against mismatches between the engineering implementation and the originally specified objectives.

### 9. Enhances Audit and Review Preparedness

* **Explanation:** Many of NASA’s programs, both internally and externally, are periodically assessed through management, technical, or safety-oriented audits. Maintaining up-to-date and consistent requirements mapping matrices makes audits more efficient.
* **Why It Matters:**
  + Periodic reviews ensure that mapping matrices are audit-ready at all times and reduce the need for last-minute corrections or defenses during external reviews.
  + It saves time during critical milestone reviews, such as Preliminary Design Review (PDR) or Critical Design Review (CDR), by ensuring matrices and their traceability are already validated.

### 10. Aligns with NASA's Mission to Ensure Safety and Success

* **Explanation:** Adherence to **NPR 7150.2** and **NASA-STD-8739.8** is a cornerstone of NASA’s commitment to safety and mission success. Requirements represent the foundation upon which foundational mission objectives are built, and requirements mapping matrices ensure they are implemented correctly.
* **Why It Matters:**
  + Periodic review confirms NASA's alignment with its mission to ensure that all systems and subsystems function as intended, without unexpected failures caused by inadequate software assurance.

## 2.3 Conclusion

The periodic review of requirements mapping matrices by the **NASA Chief, SMA** is a vital step in ensuring mission success, safety, and compliance with agency standards. This oversight function verifies tailored compliance, ensures traceability, detects early risks, and improves communication across multidisciplinary teams. By reinforcing alignment with **NPR 7150.2** and **NASA-STD-8739.8**, it prevents issues such as requirements drift, unverified implementations, or cybersecurity vulnerabilities from jeopardizing projects. This proactive approach supports process improvement, consistent application of standards, and reductions in lifecycle risks agency-wide.

# 3. Guidance

Projects are required to document and maintain **NASA-STD-8739.8 [278](#_tabs-<p></p>) compliance matrices** throughout the software development lifecycle. These matrices serve as critical artifacts for tracking compliance with software assurance and software safety requirements. By providing clear mappings of requirements along with documented waivers, deviations, and tailored provisions, compliance matrices enable transparency, traceability, and proactive risk management for both project teams and oversight organizations such as the **Office of Safety and Mission Assurance (OSMA)**.

This guidance elaborates on how projects can develop, utilize, and maintain compliance matrices and specifies how OSMA uses these matrices to ensure proper implementation and sustained adherence to NASA software engineering and assurance standards (including **NPR 7150.2 [083](#_tabs-<p></p>)**).

## 3.1 Purpose and Lifecycle Management

1. **Maintain and Record Compliance Matrices**
   * Projects must develop and maintain their **NASA-STD-8739.8 compliance matrices** for the entire life of the software project.
     + See [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)
     + See Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) and tab 4 of Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) (Software Assurance Requirements Mapping Matrix.)
   * Compliance matrices document:
     + **All applicable requirements** derived from **NASA-STD-8739.8** and **NPR 7150.2** standards.
     + **Waivers**: Approved exceptions to specific requirements.
     + **Deviations**: Adjustments made to accommodate unique project situations.
     + Tailored provisions detailing how requirements are implemented or modified for the specific project.
2. **Lifecycle Usage**
   * Projects start creating the compliance matrices during the **P****lanning phase** (see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)) and maintain them as updated records throughout:
     + Requirement definition and tailoring.
     + Implementation and testing.
     + Verification and validation (V&V).
     + Post-deployment maintenance.
3. **Integration with NASA Guidance and Policies**
   * Projects should reference related processes outlined in this **NASA Software Engineering and Software Assurance Handbook** **(NASA\_HDBK-2203)**, including:
     + [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations): Tailoring requirements.
     + [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements): Drafting actionable "shall" statements.
     + [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements): Fulfilling requirements.
     + [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements): Reviewing changes made to tailored requirements.

## 3.2 How to Use Compliance Matrices

1. **Purpose of Compliance Matrices**
   * **Planning Tool**:
     + Compliance matrices help projects understand and map **NASA-STD-8739.8 requirements**, ensuring software assurance and safety activities are properly planned and resourced from the onset.
     + They enable prioritization of safety-critical and mission-critical requirements.
   * **Transparency and Traceability**:
     + These matrices create a traceable record of requirement implementation, deviations, and waivers.
     + They provide visibility into how tailored requirements align with project constraints and mitigate risks.
2. **Accessibility for Audits and Assessments**
   * Projects must ensure compliance matrices are accessible during audits, reviews, and assessments conducted by NASA OSMA or other oversight entities.
   * For **Office of Safety and Mission Assurance (OSMA) Quality Audit, Assessment, and Review (QAAR)** audits:
     + Matrices should be prepared with supporting documentation detailing assigned responsibilities, rationale for tailoring, and evidence of approval for waivers/deviations.
     + This ensures compliance matrices are audit-ready and serve as a source of accountability.
3. **Responding to NASA Data Calls**
   * Compliance matrix data may also be requested during recurring **NASA Software Assurance Working Group (SAWG)** activities.
   * Projects should anticipate data calls where OSMA requires additional matrices or analytical insights targeting patterns in waivers, deviations, or areas of improvement.

## 3.3 OSMA’s Role in Supporting Compliance Matrix Development

1. **Guidance and Support**
   * Projects encountering uncertainty in NASA assurance and engineering requirements, tailoring decisions, or fulfillment processes can seek support from NASA OSMA.
     + OSMA offers expertise in interpreting requirements from **NASA-STD-8739.8** and **NPR 7150.2** and applying them appropriately for software assurance, engineering, and safety needs.
     + The **NASA Software Engineering Handbook** (NASA\_HDBK-2203) provides detailed guidance and rationale for each requirement.
2. **Review Activities**
   * **Periodic Review of Matrices by OSMA**:
     + OSMA reviews compliance matrices submitted by projects for:
       - **Patterns and Trends**: Identifying systemic issues in requirements tailoring (e.g., frequent waivers of certain requirements or recurring deviations).
       - **Targeted Support**: Using review findings to assist Centers and projects in addressing specific challenges in meeting requirements.
       - **Feedback to Standards Updates**: Highlighting areas in NASA standards or policies (e.g., **NPR 7150.2**, **NASA-STD-8739.8**) that may need refinement to improve clarity or usability.
     + See [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) and [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment).

## 3.4 Benefits of Compliance Matrix Maintenance

1. Project Perspective
   * **Proactive Risk Mitigation**: Mapping and addressing requirements early helps reduce risks associated with untracked deviations, incomplete implementations, or hazards stemming from tailored requirements.
   * **Enhanced Visibility**: Compliance matrices facilitate communication between stakeholders, ensuring all teams (engineering, assurance, safety, and management) understand how requirements are met.
   * **Improved Audit Readiness**: Maintenance of matrices ensures readiness for audits (e.g., QAAR) and other assessments, minimizing disruptions during reviews.
2. Agency Perspective
   * **Tailoring Insight for Continuous Improvement**:
     + By analyzing patterns in tailored requirements, OSMA identifies areas where standards might need adjustment or clarification to better fit project constraints.
     + Example: Frequent waivers of cybersecurity-related assurance could highlight the need for updated guidance on cybersecurity in future versions of **NASA-STD-8739.8**.
   * **Center-Specific Support**:
     + Patterns in non-compliance or frequent tailoring requests may indicate organizational gaps within specific Centers, prompting targeted OSMA intervention and training.

## 3.5 Compliance Matrix Example Content

1. **Minimum Content**  
   Compliance matrices should include:
   1. **Full list of applicable NASA-STD-8739.8 and NPR 7150.2 requirements**.
      * Clearly categorize requirements by phase (e.g., design, build, test, operational).
   2. **Mapping of tailored requirements**.
      * For each requirement:
        + Specify any deviations and waivers.
        + Provide rationale or justification.
        + Include approval documentation.
      * Example: Safety-critical software requirements tailored for small projects due to resource constraints.
   3. **Connections to verification and validation activities**.
   4. **Approval records for tailored requirements**.
   5. See Guidance on Minimum Recommended Content in Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) and tab 4 of Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) (Software Assurance Requirements Mapping Matrix.)
2. **Tailoring Documentation**  
   Projects should ensure all tailored requirements are:  
   * Consistent with [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) and [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements).
   * Reviewed periodically for alignment with project needs and updated where necessary.

## 3.6 Continuous Feedback to Improve Standards

Compliance matrices not only ensure project success but also serve as data sources for enhancing NASA's overarching software assurance and engineering policies. OSMA uses matrix reviews to:

1. Pinpoint industry or project-specific challenges that require updates in Agency standards.
2. Suggest clarifications or refinements to improve the clarity and applicability of requirements across diverse missions.

## 3.7 Conclusion

Maintaining and recording **NASA-STD-8739.8 compliance matrices** is essential for ensuring software assurance and safety across all NASA projects. These matrices provide traceability for requirements, tailoring decisions, and implementation activities—serving as critical tools for both individual project success and long-term process improvement. OSMA plays a key role in assisting projects with compliance, periodically reviewing matrices, and identifying gaps or trends that feed into updates to NASA policies. Through proactive maintenance and collaboration with OSMA, projects align with **NASA-STD-8739.8** and facilitate safer, more reliable software development practices across the agency.

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) * [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small projects, such as CubeSats, prototypes, experimental payloads, technology demonstrators, or ground tools, operate with limited resources, simpler designs, and less complex risks compared to larger missions. However, documenting and maintaining **NASA-STD-8739.8 compliance matrices** is essential even for small projects to ensure proper adherence to NASA software assurance and safety standards. Tailored processes can enable small projects to manage compliance efficiently and reduce administrative burden while maintaining reliability and safety-critical standards.

This guidance provides strategies and recommendations for small projects to implement and align with the requirement in a scalable, resource-efficient manner.

## 4.1 Guidance for Small Projects

### 4.1.1  Contextualizing Compliance Matrices for Small Projects

#### Purpose of Compliance Matrices

* **Compliance matrices** track software engineering requirements, waivers, deviations, and tailored provisions against NASA’s software assurance and safety standards (**NPR 7150.2** [083](#_tabs-<p></p>) and **NASA-STD-8739.8** [278](#_tabs-<p></p>)).
* For small projects:
  + These matrices demonstrate how requirements critical to mission success (e.g., hardware/software integration, test validation, fault tolerance, etc.) are implemented.
  + They ensure that even limited-scope projects maintain a consistent approach to software assurance and safety.

#### Tailored Implementation for Small Projects

* Unlike large-scale missions, small projects can use streamlined compliance matrices focusing on high-risk areas (e.g., safety-critical software or cybersecurity-related requirements), allowing for efficient tracking without excessive complexity.
* Small projects generally have fewer requirements, which makes compliance manageable using simplified matrix templates.

### 4.1.2. Guidance for Maintaining Compliance Matrices

#### Streamlined Matrix Creation

* Start creating compliance matrices during **early project planning** (see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)).
  + Use NASA-provided templates or lightweight alternatives (e.g., Excel-based matrices, simple tables).
  + Focus on mapping software assurance and safety requirements relevant to your project classification (see [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations)).
* Ensure your matrix includes:
  + **Applicable requirements**: List only those requirements relevant to the project.
  + **Tailored requirements**: Include adjustments justified by resource constraints or mission scope.
  + **Waivers and deviations**: Identify any approved exceptions along with rationale and documentation.
  + **Verification linkages**: Map requirements to corresponding testing or validation activities.

#### Focus on Key Requirement Categories

* For small projects, prioritize the following categories of **NASA-STD-8739.8** requirements:
  + **Safety-critical software requirements**: Ensure proper classification and risk mitigation (e.g., [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements)).
  + **Verification and validation (V&V) processes**: Link requirements to lightweight test plans (e.g., [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)).
  + **Hazard analysis and risk identification**: Provide simplified hazard tracking for safety-critical operations (e.g., [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan)).
  + **Cybersecurity assurance**: Address cybersecurity risks (e.g., SWE-154), especially for internet-connected payloads or ground systems.

#### Use Lightweight Documentation Techniques

* Small projects can reduce administrative overhead by using simplified methods for maintaining compliance matrices:
  + **Templates provided by NASA PAL** (Process Asset Library) or open-source tools.
  + Minimal but focused documentation that includes tracking of tailored compliance and safety-critical requirements.
  + Reference this **NASA Software Engineering and Assurance Handbook (NASA\_HDBK-2203)** for guidance on tailoring matrices for small projects.

### 4.1.3. Preparing for Audits and Assessments

#### Audit Readiness

* Small projects should maintain regularly updated compliance matrices for review during **OSMA Quality Audit, Assessment, and Review (QAAR)** audits or evaluations by other oversight entities.
  + Ensure all requirements, waivers, deviations, and tailored provisions are documented clearly and sourced appropriately.
  + Use simplified approval workflows to justify tailored requirements.

#### Handling Data Calls

* Be prepared for data calls from stakeholders such as the **NASA Software Assurance Working Group (SAWG)**.
  + Submit focused compliance matrix data addressing specific requirements (e.g., patterns of tailoring for safety-critical software).
  + Retain all relevant documents (e.g., matrices, rationale for waivers) for rapid access during reviews.

### 4.1.4. Leveraging NASA Support for Small Projects

#### NASA OSMA Assistance

* The **Office of Safety and Mission Assurance (OSMA)** provides guidance and direct support for projects encountering challenges in interpreting or implementing software assurance requirements.
  + For small projects with limited expertise in compliance matrices, OSMA helps clarify the intent, implementation, and justification for requirements listed in **NASA-STD-8739.8** and **NPR 7150.2**.
  + Small projects should take advantage of OSMA’s resources to resolve complexity in tailoring and assure compliance efficiently.

#### Using NASA’s Handbook

* The **NASA Software Engineering Handbook (NASA\_HDBK-2203)** contains detailed rationale and guidance for all requirements in **NASA-STD-8739.8** and **NPR 7150.2**. Small projects should refer to this resource to ensure consistent interpretation and application of requirements.

### 4.1.5. Practical Strategies for Small Projects

#### Streamlining Efforts

* Use focused compliance matrices tailored for small-scale missions:
  + Limit documentation to mission-essential requirements.
  + Identify non-critical requirements that can be omitted or tailored for simplicity, while fully documenting safety-critical elements.

#### Automation and Templates

* Utilize pre-approved automation tools (e.g., spreadsheet templates, database programs) to simplify compliance matrix creation and maintenance.
* When available, adopt Center-specific templates designed for small projects to minimize duplicate efforts.
  + Example: Lightweight CubeSat-specific compliance matrices pre-configured for common requirements.

#### Collaborate with Teams

* Ensure stakeholders (software engineers, system engineers, assurance teams) collaborate on the development and updates of compliance matrices, fostering alignment between documentation and actual implementation.

### 4.1.6. Examples of Scaling Compliance Matrices for Small Projects

#### Scenario 1: CubeSat Mission

* **Focus**: Tailor compliance matrices to emphasize safety-critical functions (e.g., telemetry, command receivers).
* **Approach**:
  + Include full justification for waivers related to lifecycle phases skipped due to rapid development cycles.
  + Focus V&V testing on operational risks and critical hardware/software interactions.

#### Scenario 2: Experimental Payload

* **Focus**: Essential requirements covering data validation software and interfaces with controlling hardware.
* **Approach**:
  + Document minimal assurance activities focused on payload data validity and hardware/software integration. Tailor all non-critical requirements.

### 4.1.7  Benefits for Small Projects

1. **Efficiency and Simplicity**
   * Small projects save time and resources by focusing compliance matrices on relevant requirements tied to mission-specific risks.
   * Efficient documentation ensures audit-readiness without excessive complexity.
2. **Proactive Risk Management**
   * By documenting tailored compliance and deviations, small projects proactively address risks to safety, reliability, and cybersecurity.
3. **NASA-Wide Consistency**
   * Compliance matrices ensure small projects achieve consistent implementation of NASA standards, strengthening mission success across the agency.

## 4.2 Conclusion

Small projects, despite their unique constraints, can effectively maintain **NASA-STD-8739.8 compliance matrices** by adopting streamlined documentation practices, focusing on high-value safety and assurance requirements, and leveraging NASA-provided resources such as templates and OSMA support. Tailored approaches allow small projects to remain compliant with agency standards while optimizing resource use and fulfilling mission objectives efficiently. This guidance ensures scalability, minimizes administrative burden, and fosters alignment with NASA’s broader safety and mission assurance standards.

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
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-521)

  [Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999)](https://llis.nasa.gov/lesson/740 "Click to open in new window")

  Public Lessons Learned Entry: 740.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** contains case studies highlighting the importance of proper documentation, tracking, and adherence to software assurance requirements. Specific lessons demonstrate how maintaining and recording compliance matrices throughout the software lifecycle can prevent mission failures, ensure transparency, and improve risk management.

Below are selected relevant lessons learned, illustrating why compliance matrices are critical to meeting software assurance (SA) and software safety (SS) objectives as outlined in **NASA-STD-8739.8** [278](#_tabs-<p></p>).

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Lesson Learned: Deficiencies in Requirement Tracking Can Lead to Mission Failure

* **Case:** Mars Climate Orbiter - Software Error due to Unit Mismatch[521](#_tabs-<p></p>)
* **Lesson Number:** LLIS-0740
* **Incident Summary:**  
  The **Mars Climate Orbiter (MCO)** failed in 1999 due to an untracked software interface issue where one engineering team used Imperial units (pounds-force seconds), while another used metric units (Newton-seconds). This critical error was not documented, verified, or accounted for during the testing phase, underscoring a lack of rigor in tracking software requirements and tailoring decisions.
* **Lesson Learned:**
  + The absence of traceable compliance documentation and oversight led to a catastrophic discrepancy that could have been avoided with proper assurance tracking.
  + Projects must maintain detailed records of how requirements are implemented, tailored, and validated.
* **Relevance to the Requirement:**  
  Maintaining and recording compliance matrices prevents such oversights. A properly managed compliance matrix would have ensured software testing addressed critical units and conversion requirements, and deviations would have been reviewed and justified appropriately.

#### 2. Gaps in Requirement Validation Jeopardize Mission Reliability

* **Case:** Mars Polar Lander - Premature Shutdown of Descent Engines [529](#_tabs-<p></p>)
* **Lesson Number:** LLIS-0938
* **Incident Summary:**  
  The **Mars Polar Lander (MPL)** failed in 1998 due to inadequate validation of software requirements. The descent engines shut down prematurely because the software misinterpreted noise from the touchdown sensors as a valid landing signal. Requirements to account for transient signals during the descent phase were poorly tracked, and validation/testing activities were not rigorous enough to catch this oversight.
* **Lesson Learned:**
  + Inadequate or incomplete validation of software requirements can create unanticipated failure modes.
  + Traceable compliance matrices would have made it easier to identify missing validation activities for transient signal scenarios.
* **Relevance to the Requirement:**  
  Properly maintained compliance matrices ensure all requirements are verified and validated, reducing risks from poorly documented or untracked requirements.

#### 3. Tailoring Requires Consistent Documentation and Justification

* **Case:** International Space Station (ISS) Software Documentation Issues
* **Lesson Number:** LLIS-1873
* **Incident Summary:**  
  The **International Space Station (ISS)** program faced challenges when requirements were tailored inconsistently between modules developed by different contractors. Deviations and waivers were often undocumented or inadequately justified, making it difficult to trace changes and ensure software consistency. This lack of proper tailoring documentation caused delays during later integration and testing phases.
* **Lesson Learned:**
  + Tailoring decisions must be justified and properly documented in a manner accessible to all relevant stakeholders.
  + Compliance matrices are essential for tracking tailoring decisions and their impacts across a project’s lifecycle, especially for multi-contractor or multi-modular projects.
* **Relevance to the Requirement:**  
  Small and large projects alike must document all waivers, deviations, and tailored provisions in compliance matrices to ensure justification and accountability. This clarity is essential for later integration and audit phases.

#### 4. Failing to Monitor Compliance Across the Lifecycle Can Lead to Issues

* **Case:** Hubble Space Telescope (HST) Software Development Oversight
* **Lesson Number:** LLIS-0919
* **Incident Summary:**  
  During the Hubble Space Telescope development, gaps in monitoring software compliance throughout the lifecycle led to inconsistencies in subsystem behavior and significant late-stage rework. Early compliance lapses were not identified and corrected until late in the project, causing delays, cost overruns, and risks to mission success.
* **Lesson Learned:**
  + Software compliance must be tracked and documented throughout the entire development lifecycle, not just at the start.
  + Periodic reviews of compliance matrices would have identified early deviations for correction, preventing costly downstream impacts.
* **Relevance to the Requirement:**  
  Compliance matrices, when maintained for the life of the project, ensure continuous monitoring of software requirements and help projects catch issues early when corrections are less costly and disruptive.

#### 5. Inconsistent Documentation Hinders Risk Mitigation

* **Case:** Space Shuttle Columbia Accident Investigation
* **Lesson Number:** LLIS-0794
* **Incident Summary:**  
  The **Space Shuttle Columbia accident** revealed that many documentation processes related to safety assurance and risk management were inconsistent or incomplete. Tailored processes and deviations were inadequately tracked, which hampered effective risk communication and management during operations.
* **Lesson Learned:**
  + Consistently documenting requirements, tailoring, and compliance activities strengthens risk management and ensures risks are addressed proactively.
  + Compliance matrices act as a single, traceable source of truth to ensure tailored or waived requirements are thoroughly evaluated for their impacts on risk.
* **Relevance to the Requirement:**  
  A compliance matrix ensures clear risk accountability and traceability, making it easier to identify how tailored or waived requirements influence safety and mission risk.

#### 6. Lesson Learned: Effective Use of Compliance Matrices Enhances Audit-Readiness

* **Case:** Ground Software for Earth Observing Satellite
* **Lesson Number:** LLIS-1428
* **Incident Summary:**  
  During an Earth observing satellite program, an internal audit revealed that documentation of software compliance with assurance requirements was incomplete. The project team scrambled to reconstruct compliance records, which delayed the audit process and flagged potential gaps in safety assurance.
* **Lesson Learned:**
  + Keeping compliance matrices updated makes projects audit-ready and provides clear evidence of adherence to NASA standards and safety protocols.
  + Projects that neglected to maintain compliance matrices struggled to demonstrate software assurance compliance during audits.
* **Relevance to the Requirement:**  
  Compliance matrices reduce the risk of non-compliance findings during QAAR audits, making the project more efficient during scheduled and unscheduled reviews.

#### 7. Poor Integration of Software Safety and Assurance Leads to Hazard Accumulation

* **Case:** Software Assurance Gaps in Small Experimental Satellite Program
* **Lesson Number:** LLIS-2257
* **Incident Summary:**  
  A small satellite project experienced mission failure because software assurance activities were not sufficiently prioritized, particularly in terms of documenting and validating safety-critical software requirements. This resulted in untested hazards that emerged during operations.
* **Lesson Learned:**
  + Even small projects must document and track safety-critical requirements and associated hazards.
  + Compliance matrices offer a lightweight, effective way to ensure small, resource-constrained projects address high-priority software assurance areas.
* **Relevance to the Requirement:**  
  Small projects can use compliance matrices to document mission-critical and safety-critical requirements without unnecessary administrative burden, ensuring no critical hazards are overlooked.

#### 8. Patterns in Waivers and Deviations Can Inform Standards Improvements

* **Case:** Patterns in Tailoring Across Distributed Projects
* **Lesson Number:** LLIS-2734
* **Incident Summary:**  
  NASA observed recurring patterns in tailoring and waivers across multiple distributed projects, highlighting confusion about the intent of certain software assurance requirements. OSMA used these patterns to clarify requirements in future versions of **NPR 7150.2** [083](#_tabs-<p></p>) and **NASA-STD-8739.8** [278](#_tabs-<p></p>).
* **Lesson Learned:**
  + Tracking trends in waivers and tailoring helps improve NASA’s assurance standards by addressing areas of recurring complexity or ambiguity.
  + Compliance matrices help NASA-wide stakeholders identify systemic issues across Centers or projects.
* **Relevance to the Requirement:**  
  Recording compliance matrices not only benefits individual projects but contributes to improving overall software assurance policies at NASA.

### 6.1.2  Conclusion

The lessons above emphasize the critical importance of maintaining and recording compliance matrices for the lifecycle of software projects, regardless of size or scope. Compliance matrices provide traceability, ensure consistency across tailored requirements, and enhance risk mitigation. By documenting waivers, deviations, and tailored provisions, NASA ensures safety and mission success while also gathering insights to refine its assurance and engineering standards over time. These lessons learned offer a strong rationale for periodic compliance matrix maintenance and usage.

## 6.2 Other Lessons Learned

* No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-212 - NASA-STD-8739 Mapping Matrices**

2.1.2.4 The NASA Chief, SMA shall periodically review the project’s requirements mapping matrices.

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

The purpose of this requirement is to ensure that a project’s **Requirements Mapping Matrix (RMM)** accurately reflects and complies with NASA's software engineering and assurance directives—**NPR 7150.2** [083](#_tabs-<p></p>) and **NASA-STD-8739.8** [278](#_tabs-<p></p>)—and appropriately addresses tailored requirements, risks, and verification activities for software classification and criticality.

Software Assurance (SA) personnel must assist and support the **NASA Chief, Safety and Mission Assurance (SMA)** in performing periodic reviews of project RMMs to confirm alignment, identify issues, and ensure compliance with Agency-wide standards.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Collaborate in Preparation for Requirements Mapping Matrix Reviews

* **Understand the Scope**:
  + Familiarize yourself with the **NPR 7150.2 requirements**, software classification levels (Class A, B, C, etc.), and assurance responsibilities as outlined in **NASA-STD-8739.8**.
  + Review the tailoring process documented in the RMM to ensure justified deviations or waivers have been properly approved.
* **Gather Evidence**:
  + Collect relevant assurance and verification artifacts ahead of the SMA-led review, such as:
    - Software Assurance Plans (per **NASA-STD-8739.8**).
    - Documentation demonstrating compliance with mapped requirements.
    - Rationale for tailoring decisions, including risk assessments and mitigation plans.

#### 7.4.2.2. Verify the Accuracy and Completeness of the RMM

* **Ensure Compliance**:
  + Confirm that all applicable **NPR 7150.2** and **NASA-STD-8739.8** requirements are mapped and verified in the RMM, appropriate to the software's classification and criticality.
  + Check that assurance-related requirements, such as testing, risk analysis, safety controls, and metrics tracking, are fully addressed.
* **Assess Tailoring**:
  + Evaluate whether any tailored requirements (waived or modified) are:
    - Properly justified.
    - Approved by the Technical Authorities.
    - Supported by sufficient risk mitigation strategies to ensure mission safety and reliability.
* **Validate Traceability**:
  + Ensure that mapped requirements in the RMM are traceable to:
    1. The software development lifecycle products (e.g., requirements documentation, test plans, verification reports).
    2. Risk management strategies and plans, especially for safety-critical software.

#### 7.4.2.3. Support SMA During the Review

* **Facilitate Discussions**:
  + Assist the SMA in analyzing and discussing assurance-related requirements during the review. Be prepared to:
    - Explain the project’s assurance processes and their alignment with mapped requirements.
    - Identify and elaborate on any gaps, risks, or tailoring decisions impacting software safety or mission success.
* **Provide Insight**:
  + Highlight assurance-specific concerns, such as:
    - Adequacy of testing for critical requirements.
    - Coverage of verification activities (e.g., Independent Verification and Validation (IV&V) for safety-critical systems).
    - Risk tracking and mitigation effectiveness.

#### 7.4.2.4. Identify and Address Issues

* **Analyze Gaps**:
  + If the RMM review reveals missing or inconsistent requirements mapping, work with the project team to analyze:
    - Areas of non-compliance.
    - Associated risks, especially for safety-critical software.
* **Provide Recommendations**:
  + Propose corrective actions for issues identified during the review, such as:
    - Adding missing assurance requirements in the RMM.
    - Improving risk mitigation strategies for tailored requirements.
    - Updating artifacts to improve traceability and alignment with **NPR 7150.2**.

#### 7.4.2.5. Document Findings and Follow Up

* **Record Review Outcomes**:
  + Document all findings, gaps, and recommendations related to assurance requirements during the RMM review.
  + Ensure that unresolved issues are tracked in the project’s action management system, with clear accountability and deadlines for resolution.
* **Verify Implementation of Changes**:
  + Follow up with project teams to ensure corrective actions from the RMM review are implemented. Confirm that updated RMM mappings, artifacts, or processes fully address identified gaps.

#### 7.4.2.6. Promote Continuous Improvement

* **Identify Trends**:
  + Use findings from periodic RMM reviews to identify systemic issues across projects (e.g., recurring deviations, lack of traceability, or weak risk assessments).
* **Share Best Practices**:
  + Recommend improvements to assurance-related standards, templates, and tools, ensuring they address commonly identified gaps and lessons learned from reviews.

### 7.4.3  Key Areas of Focus for RMM Reviews:

Software Assurance should assist in ensuring the following during RMM reviews:

1. **Requirements Coverage**:
   * All **NPR 7150.2** requirements applicable to the project’s software classification are mapped in the RMM.
   * Safety-critical requirements have appropriate rigor in assurance activities.
2. **Tailoring Validation**:
   * Deviations from requirements are properly justified, approved, and managed.
   * Tailoring ensures that risks to software assurance and safety are sufficiently mitigated.
3. **Traceability**:
   * Requirements are clearly traceable to project deliverables (e.g., test plans, risk analyses, and assurance reports).
4. **Compliance**:
   * Mapped requirements are implemented with sufficient evidence of verification and validation.
5. **Safety and Risk Management**:
   * Software Assurance requirements related to safety controls, hazard tracking, and risk mitigation for safety-critical systems are fully mapped and addressed.

### 7.4.4  Expected Outcomes of the RMM Review

By supporting this requirement, Software Assurance helps:

1. **Ensure Compliance**:
   * Verify that the RMM reflects accurate and consistent implementation of assurance-related requirements.
2. **Mitigate Risks**:
   * Surface and resolve gaps or risks stemming from poorly mapped or tailored requirements.
3. **Promote Standardization**:
   * Drive consistent implementation of software assurance processes across Centers and projects.
4. **Enable Continuous Improvement**:
   * Use findings to refine assurance policies, guidance, and tools for improved compliance and project success.

### 7.4.5  Conclusion

Software Assurance plays a key role in supporting the **NASA Chief, SMA** during periodic reviews of Requirements Mapping Matrices. By ensuring completeness, compliance, and proper justification for tailoring decisions, SA personnel help mitigate risks, improve traceability, and foster standardization across NASA projects. These actions ensure software assurance activities are fully aligned with NASA’s directives and contribute to mission success and system safety.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) * [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment) |
