# SWE-216 - Internal Software Sharing List

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695547. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List

SWE-216 - Internal Software Sharing List

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695547)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695547&showCommentArea=true&showComments=true#addcomment)

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

2.1.5.14 The Center Director, or designee, shall ensure that all software listed on the internal software sharing or reuse catalog(s) conforms to NASA software engineering policy and requirements.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-216 History

SWE-216 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 2.1.5.16 The Center Director or designee shall ensure that all software listed on the internal software sharing or reuse catalog(s) conforms to NASA software engineering policy and requirements. |
| Difference between C and D | No Change |
| D | 2.1.5.14 The Center Director, or designee, shall ensure that all software listed on the internal software sharing or reuse catalog(s) conforms to NASA software engineering policy and requirements. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

To ensure that we share quality software, the requirement ensures that all shared software conforms to the NASA quality standards and meets the NASA software engineering and software assurance requirements contained in **NPR 7150.2 [083](#_tabs-<p></p>)**. To support software centralization and inventory visibility, NASA requires internally developed software applications under the technical authority of the Office of Chief Information Officer (Class F) to be registered within the Agency’s repository for application management.

This requirement ensures that the software listed in NASA's internal software sharing or reuse catalog adheres to the agency's software engineering policies and requirements outlined in **NPR 7150.2** and complementary directives. NASA’s mission objectives require reliable, consistent, safe, and high-quality software across various projects and missions. The reuse of software that fails to meet policy and engineering standards can introduce significant risks, delays, and inefficiencies, jeopardizing safety, reliability, and mission success.

This rationale explains why such conformity is crucial, emphasizing technical, operational, legal, and organizational considerations.

## 2.1 Key Rationale for the Requirement

### 1. Mitigation of Operational and Mission Risks

* **Ensuring Software Quality and Reliability**
  + Software listed in the sharing or reuse catalog is likely to be integrated into mission-critical systems or used for tasks of significant complexity. If the software does not conform to NASA engineering standards, it could introduce bugs, defects, or vulnerabilities into new projects, leading to cascading failures that compromise operational performance or mission success.
  + Conformance ensures the software has been developed, tested, and verified under established practices to meet quality and reliability objectives, fostering confidence in its dependability.
* **Examples of Potential Issues Without Conformance**
  + Mismanagement of software interfaces might lead to integration failures.
  + Inadequate verification and validation (V&V) processes could leave critical defects unaddressed.
* **Key Point**: Ensuring conformity reduces technical debt and mitigates risks that could propagate during the reuse of low-quality or non-compliant software.

### 2. Promoting Reuse of High-Value, Compliant Software Assets

* **Maximizing the Value of Shared Software**
  + The NASA internal software catalog is a repository of reusable assets intended to reduce development costs, improve project schedules, and leverage prior investments. Listing only software that meets engineering standards ensures other projects can confidently adopt these assets without needing extensive rework, patches, or custom development.
  + Non-compliant software may dilute the value proposition of the catalog by requiring significant updates or fixes, defeating the fundamental motivation behind reusability.
* **Fostering Inter-Project Consistency**
  + Software reuse allows projects to benefit from standardized practices and ensures that shared software integrates smoothly into new projects. Conformance promotes compatibility between systems, reducing unforeseen challenges arising from inconsistent practices.
* **Key Point**: The reuse catalog must act as a trusted source of high-value and consistent software assets that meet agency-wide standards to deliver the expected benefits.

### 3. Ensuring Compliance with NASA Policies and Federal Regulations

* **Alignment with Agency Policies**
  + NASA’s software engineering requirements, such as **NPR 7150.2**, establish baseline expectations for software safety, security, quality, and maintainability. Failing to enforce standards compliance risks undermining these policies, creating legal, technical, and operational vulnerabilities.
  + This requirement ensures that software shared or reused internally adheres to the same level of scrutiny as newly developed software, avoiding compliance gaps.
* **Compliance with Federal Mandates**
  + As a U.S. Government agency, NASA must also comply with federal laws like the **[Federal Information Security Modernization Act (FISMA)](https://www.congress.gov/113/plaws/publ283/PLAW-113publ283.pdf)** and **[OMB Circular A-130](https://obamawhitehouse.archives.gov/omb/circulars_a130_a130trans4)** related to information security and software integrity. Including non-compliant software in catalogs could introduce vulnerabilities and create regulatory liability.
* **Key Point**: Adherence to this requirement ensures that the reuse catalog aligns with internal and external rules, avoiding non-compliance or the need for costly remediations.

### 4. Maintaining Safety and Security Standards

* **Ensuring Mission and System Safety**
  + Software failures can have catastrophic consequences for personnel safety, mission success, and assets. Conformance to NASA software engineering policies ensures that software has undergone rigorous processes for risk management, safety analysis, and fault tolerance verification.
* **Mitigating Security Vulnerabilities**
  + Non-compliant software may lack proper cybersecurity safeguards, making it vulnerable to exploitation, data breaches, or unauthorized access during reuse. This is especially critical for high-profile NASA missions that could be targeted by cyber-attacks. Conformance to software security requirements ensures that reusable software is appropriately secure.
* **Key Point**: Including only software conforming to NASA’s safety and security processes minimizes risks to systems, data, and human lives.

### 5. Supporting Efficient Software Development Practices

* **Reducing Costs and Development Time**
  + Resourcing compliant software from the catalog allows projects to avoid duplicating development efforts unnecessarily. Projects can trust that conforming software has already met baseline engineering requirements, saving time and resources that would otherwise be spent on validating or fixing software.
  + Non-conforming software in the catalog would negatively impact this streamlined process, as engineers would need to revalidate or modify the software, creating inefficiencies.
* **Promoting Continuous Improvement**
  + Clearly establishing conformance as the requirement for software inclusion incentivizes teams to improve their adherence to NASA’s engineering standards. Over time, this raises the overall quality of reusable software assets.
* **Key Point**: Conformance increases efficiency by making pre-validated, high-quality software accessible for reuse, while avoiding inefficiencies caused by low-quality entries.

### 6. Supporting Institutional Knowledge Preservation

* **Improving Knowledge Transfer**
  + Conformance ensures that software engineering knowledge and standards are preserved as part of reusable software artifacts. Well-developed, standards-compliant software includes proper documentation, interfaces, and design considerations that improve long-term understanding and use.
  + Poorly developed, non-conforming software without proper documentation or engineering rigor creates knowledge gaps and hinders effective reuse.
* **Key Point**: NASA catalogs should represent institutional knowledge in a clear, consistent, and reusable format by ensuring all listed software conforms to established engineering practices.

### 7. Maintaining Organizational and Public Trust

* **Protecting NASA’s Reputation**
  + Non-compliant software risks introducing failures or vulnerabilities that could compromise high-visibility NASA missions. A single failure caused by substandard software can damage NASA’s reputation as a leader in engineering and scientific exploration. By enforcing conformance, NASA demonstrates its commitment to excellence and risk mitigation for all software activities.
* **Ensuring Stakeholder Confidence**
  + NASA collaborates extensively with international, commercial, and governmental stakeholders. Ensuring that its reusable software meets stringent engineering standards cultivates trust in its technical capabilities and professionalism.
* **Key Point**: Maintaining strict conformance requirements protects NASA’s reputation and enhances stakeholder confidence in its mission execution.

### 8. Facilitating Modernization and Evolving Standards

* **Future-Proofing Shared Software**
  + Software that conforms to NASA’s requirements is better positioned for upgrades, modernization, and expansion as technology evolves. Standards-compliant software provides a strong foundation for adapting to new tools, systems, or operational environments.
  + Non-compliant software may rely on outdated practices or technologies, making future updates more difficult and costly.
* **Key Point**: A policy of enforcing conformance ensures shared software assets remain adaptable to future NASA and technological needs.

## 2.2 Conclusion

The requirement to ensure that all software listed on NASA’s internal software sharing or reuse catalog conforms to agency software engineering policies and requirements is critical for:

* **Mitigating operational risks** and ensuring mission success.
* **Maximizing efficiency** through high-quality and standards-compliant reusable software.
* **Maintaining compliance** with NASA policies and federal regulations.
* **Ensuring safety and security** across all software reuse scenarios.
* **Preserving institutional knowledge** and promoting continuous improvement.

By requiring conformance, NASA guarantees that the internal software catalog remains a trusted repository of high-value, high-quality assets. This supports NASA’s commitment to excellence, resource efficiency, and safety in all its software development and reuse initiatives.

# 3. Guidance

## 3.1. Introduction

The internal software sharing or reuse catalog(s) serves as a repository for reusable software assets across NASA Centers. It ensures collaborative efficiency, resource optimization, and high-quality engineering practices. However, for the software to be shared or reused seamlessly and safely, it must comply with NASA’s software engineering policies and requirements outlined in **NPR 7150.2 [083](#_tabs-<p></p>)** and related standards, such as **NASA-STD-8739.8 [278](#_tabs-<p></p>)**.

This guidance expands on the compliance process, promotes consistency, and clarifies how Center Directors, Technical Authorities, and project personnel can implement robust, transparent procedures for ensuring conformity with engineering requirements.

## 3.2. General Guidance

### 3.2.1 Applicability

* This requirement applies to all NASA Centers.
* It applies to all Software Classifications, as defined in **NPR 7150.2**, Appendix D.

## 3.3. Clear Steps to Meet Compliance

### Step 1: Verify Completion of NPR 7150.2 RMM and Compliance Matrix

Each software project must document its compliance with the relevant requirements in Appendix C of **NPR 7150.2** via the Requirements Mapping Matrix (RMM). This matrix verifies that the software adheres to the Agency-wide baseline requirements for engineering practices, tailored to its classification and safety-criticality.

**Actions**:

1. Ensure the Requirements Mapping Matrix from **NPR 7150.2** is completed.
   * Use the downloadable compliance matrices available in the [**NASA Engineering Network (NEN)****Software Engineering Community of Practice**](https://nen.nasa.gov/web/software) **[258](#_tabs-<p></p>) -** Document repository.
   * Check for the inclusion of both Project and Institutional requirements and validate applicability based on the designated "X" markers for each requirement.
2. Review the project’s tailoring documentation (if applicable) for deviations, waivers, or modifications to the default requirements.
   * Obtain Technical Authority (Engineering and SMA) approval for tailored requirements via [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) and [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations).

**Key Questions**:

* Has the Requirements Mapping Matrix been completed and approved by Engineering and SMA Technical Authorities?
* Were all mandatory “shall” statements either fulfilled or approved via relief requests (partial or complete)?

### Step 2: Verify Compliance with NASA Software Assurance and Safety Standards (NASA-STD-8739.8)

Software listed in the sharing catalog must also adhere to the **NASA-STD-8739.8:** **NASA Software Assurance and Software Safety Standard**. This standard outlines the software assurance and safety tasks required to ensure high quality and safety throughout the software lifecycle.

**Actions**:

1. Confirm that the software complies with all relevant software assurance and safety activities required by **NASA-STD-8739.8**.
2. Review implementation of assurance activities, including:
   * Peer reviews and inspections.
   * Validation, evaluation, and risk assessments.
   * Safety-critical analyses.
3. Ensure documentation captures evidence of compliance with assurance requirements (e.g., checklists, reports, testing logs).

**Key Questions**:

* Has the software met all the applicable software assurance and safety requirements?
* Are signed approvals from the responsible Technical Authorities available?

### Step 3: Confirm Institutional and Project-Level Requirements

Software must meet NASA's institutional and project-specific policies to ensure alignment across all Centers and missions.

**Actions**:

1. Confirm compliance with **[B. Institutional Requirements](/spaces/SWEHBVD/pages/102695220/B.+Institutional+Requirements)**:
   * Institutional requirements apply Agency-wide and focus on NASA business processes, risk management, and operational consistency.
   * These requirements are independent of any project and are overseen by Center Directors or designated leadership.
2. Confirm compliance with **[C. Project Software Requirements](/spaces/SWEHBVD/pages/102695222/C.+Project+Software+Requirements)**:
   * Project requirements apply explicitly to the planning, execution, and management of individual software projects.
   * Validate that project teams followed the project-level requirements in **NPR 7150.2**, Appendix C.

**Review Checklist**:

* Have institutional requirements from Appendix C been reviewed and fulfilled?
* Has the project-level compliance matrix been approved by the Technical Authority?

### Step 4: Register Class F Software in NASA's Enterprise Repository

The Office of the Chief Information Officer (OCIO) mandates that Class F software (internally developed applications) be registered within NASA’s **Application Rationalization Tool (AART) [404](#_tabs-<p></p>)**. This repository enhances visibility, reduces duplicative efforts, and helps identify obsolete software.

**Actions**:

1. Work with the OCIO to ensure all Class F software is properly registered.
2. Use AART for inventory tracking and verification of Class F applications.

## 3.4. Context and Practical Considerations

### 3.4.1 NPR 7150.2: Software Engineering Requirements

**NPR 7150.2** defines NASA's baseline software engineering policies, tailoring processes, and compliance documentation practices. Appendix C provides the Requirements Mapping Matrix, which identifies mandatory requirements for each Software Classification.

**Why It Matters:**

* **NPR 7150.2** reduces risks by ensuring consistent software engineering practices.
* Tailoring flexibility allows projects to modify requirements based on specific circumstances while preserving oversight via approved waivers and deviations.

### 3.4.2 NASA-STD-8739.8: Software Assurance and Software Safety Standard

**NASA-STD-8739.8** focuses on software assurance and safety requirements to ensure high-quality software performance across safety critical and non-safety critical applications.

**Key Objectives:**

* Detect and mitigate software defects early.
* Assess risks associated with software safety.
* Enhance overall software quality and reliability.

### 3.4.3 Shared Catalog’s Strategic Role

The internal software sharing catalog supports the reuse of software across NASA missions and programs, promoting efficiency and reducing redundancy. Ensuring listed software conforms to engineering standards helps build trust in catalog entries and fosters seamless integration into new projects.

**Risks of Non-Compliant Entries:**

* Reduced software reliability and increased integration costs.
* Introduction of safety-critical defects or cybersecurity vulnerabilities.
* Undermined consistency of software engineering practices across NASA projects.

## 3.5. Compliance Monitoring and Oversight

#### **Role of the Center Director or Designee**

The Center Director or their designee is responsible for overseeing software policy compliance for the internal sharing catalog:

1. **Review Approval Processes**: Ensure all projects complete compliance matrices with Technical Authority approval before submitting software for catalog inclusion.
2. **Conduct Regular Audits**: Perform periodic reviews of the catalog to ensure compliance documentation is updated.
3. **Support Remediation**: Request corrections from projects for incomplete or non-compliant submissions.

## 3.6. Key Resources and Tools

#### **Available Compliance Matrices**

Pre-defined downloadable compliance matrices are accessible via the **[NASA Software Engineering Community of Practice (CoP)](https://nen.nasa.gov/web/software)** on the NASA Engineering Network (NEN).

#### **Tailoring Waiver Guidance**

* Refer to [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) for compliance matrix procedures.
* Refer to [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) for tailoring considerations to document relief requests.

#### **Agency Repository Tools**

* Use the **Application Rationalization Tool (AART)** for Class F software registration.

#### **Training and Collaboration**

Center-level training programs and collaboration with relevant authorities ensure compliance processes are understood and executed effectively.

## 3.7. Summary of Responsibilities

**Project Managers**:

* Ensure all **NPR 7150.2** and **NASA-STD-8739.8** requirements are met.
* Submit compliance matrices for Technical Authority approval.

**Center Directors or Designees**:

* Oversee catalog compliance verification and handle periodic audits.
* Address deviations or incomplete matrices within their Center.

**Technical Authorities (Engineering and SMA)**:

* Approve tailoring, deviations, and waivers.
* Validate compliance matrices for completeness.

**OCIO**:

* Ensure all Class F software is logged in the enterprise repository (AART).

By adhering to this improved guidance, NASA ensures compliance with software engineering policies, minimizes risks, and promotes effective software sharing and reuse across programs and projects.

Agency’s repository for application management (Class F Software)

To support software centralization and inventory visibility, NASA requires internally developed software applications under the technical authority of the Office of Chief Information Officer (Class F) to be registered within the Agency’s repository for application management.   The current enterprise repository is the **Agency’s Application Rationalization Tool (AART)** [404](#_tabs-<p></p>).   This will enhance the ability to identify duplicative or obsolete software.

See also [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) and Tab 4 - SA RMM Content of Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan).

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.15 - SA Tasking Checklist Tool](https://swehb.nasa.gov/display/SWEHBVD/8.15+-+SA+Tasking+Checklist+Tool) * [8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

Small projects often have constrained resources, personnel, and time, but they must still ensure that any software shared internally within NASA adheres to **NPR 7150.2** [083](#_tabs-<p></p>)  standards and other relevant requirements, such as **NASA-STD-8739.8 [278](#_tabs-<p></p>)**. This guidance is tailored specifically to address challenges faced by small projects while ensuring compliance remains manageable and efficient.

#### Challenges for Small Projects

1. **Resource Constraints**: Small teams may have limited access to personnel dedicated to compliance or software assurance tasks.
2. **Streamlined Processes**: Agile development cycles may prioritize speed over formal documentation, increasing risks of overlooking compliance.
3. **Smaller Scope**: Small projects may have fewer software components and less complexity, leading to assumptions that rigorous compliance isn't necessary (but it is mandatory).

## 4.1 Guidance for Small Projects

### 4.1.1  Small Project Practical Approach to Compliance

#### Step 1: Understand Relevant Requirements

Small projects need to focus on the specific requirements applicable to their software classification and safety-criticality.

* + **Key References**:
    - **NPR 7150.2 Appendix C**: Includes the Requirements Mapping Matrix (RMM) that specifies default requirements based on Software Classification (A–F).
    - **NASA-STD-8739.8**: Covers assurance and safety tasks, particularly for software classified as safety-critical.
  + **Actions**:
    - Identify the Software Classification (refer to Appendix D of **NPR 7150.2**).
    - Check if the software has safety-critical functionality and apply additional safety assurance measures if necessary.

**Quick Tips**:

* + Software Classifications for small projects are often Class D, E, or F. Refer to the applicable requirements in the Requirements Mapping Matrix.
  + Avoid overcomplication. Focus on requirements explicitly relevant to your classification and safety-criticality, tailoring where appropriate.

#### Step 2: Complete the Requirements Mapping Matrix

The Requirements Mapping Matrix establishes whether the software meets the baseline requirements specified in **NPR 7150.2**. For small projects, the matrix can be streamlined, focusing on providing justifications and evidence for fulfilling only relevant requirements. Also see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix).

**Actions**:

1. 1. Download the Matrix Template:
      * Get the **NPR 7150.2** Requirements Mapping Matrix template from the **[NASA Engineering Network (NEN) - Software Engineering Community of Practice - Documents](https://nen.nasa.gov/web/software/documents?p_p_id=com_liferay_document_library_web_portlet_DLPortlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_document_library_web_portlet_DLPortlet_mvcRenderCommandName=%2Fdocument_library%2Fview_folder&_com_liferay_document_library_web_portlet_DLPortlet_navigation=home&_com_liferay_document_library_web_portlet_DLPortlet_folderId=1066622&_com_liferay_document_library_web_portlet_DLPortlet_displayStyle=descriptive)** repository.
      * Or get the current **NPR 7150.2** Requirements Mapping Matrix template from Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix).
   2. Map Compliance:
      * Highlight applicable requirements based on classification and assess your compliance status (compliant, tailored, waived).
   3. Document Tailoring:
      * Tailor requirements based on the project’s scale and complexity but obtain Technical Authority approval for all tailoring decisions.
   4. Simplify Documentation:
      * For small projects, use clear and lightweight explanations (e.g., "Requirement fulfilled via peer reviews and unit testing logs").

**Small Project Checklist**:

* + Does your matrix include all relevant requirements from Appendix C?
  + Have tailoring decisions been documented with rationale and risk mitigations?
  + Have Technical Authorities signed off on the compliance matrix?

#### Step 3: Implement Software Assurance and Software Safety Activities (NASA-STD-8739.8)

Safety and assurance tasks mandated by **NASA-STD-8739.8** reduce software engineering risks and ensure quality. While extensive assurance activities may be impractical for small projects, streamlined processes can be implemented. Also see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix).

**Actions**:

1. 1. Identify Critical Assurance Tasks:
      * Peer reviews, lightweight testing, fault analyses, and code coverage metrics.
      * The current **NASA-STD-8739.8** Requirements Mapping Matrix template is available in the **SA Tasking Checklist Tool** (see Topic [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool)).
   2. Simplify Risk Assessment:
      * For safety-critical software (e.g., Class D or above), focus on a simplified risk matrix that captures key risks and mitigations specific to your project.
      * For less complex software (e.g., Class E or F), focus on basic error detection (e.g., through automated testing tools or static analysis tools).
   3. Document Assurance:
      * Maintain simple logs of assurance activities (testing results, review minutes, etc.).

**Quick Checklist for Assurance**:

* + Were peer reviews conducted and logged?
  + Are testing results (unit testing, integration testing) documented?
  + Has safety-critical functionality been adequately assessed and mitigated?

#### Step 4: Register Class F Software in NASA's Repository (If Applicable)

If the small project develops Class F software (internally developed applications), the software must be registered in NASA’s **Agency** **Application Rationalization Tool (AART) [404](#_tabs-<p></p>)**. Registration promotes inventory visibility and allows NASA to identify duplicative or obsolete software.

**Actions**:

1. 1. Register the Software:
      * Collaborate with your Center's Office of Chief Information Officer (OCIO) to complete the registration process in **AART**.
   2. Maintain Visibility:
      * Provide documentation through AART detailing software functionality, dependencies, and any associated licenses.

#### Step 5: Submit Software for Internal Sharing Approval

Before submitting software to the internal reuse catalog, review all compliance requirements and obtain Technical Authority approvals as needed.

**Actions**:

1. 1. Verify Completion of Documents:
      * Ensure both the **NPR 7150.2** Requirements Mapping Matrix and **NASA-STD-8739.8** RMM/compliance matrix are finalized.
      * Confirm all tailoring or deviations are approved by the appropriate Technical Authority.
   2. Conduct Final Quality Review:
      * Simplify this process by using internal software development checklists.
   3. Submit to Your Center Director or Designee:
      * Obtain final approval before software is shared internally.

### 4.1.2  Streamlined Tools and Resources for Small Projects

#### **Simple Documentation Tools**:

* + Use lightweight tools (e.g., Excel spreadsheets or shared online folders) to document compliance matrices.
  + Automate testing and analysis tasks using tools like **SonarQube** for static analysis or **JIRA** for tracking assurance tasks.

#### **Checklist Templates**:

Provide concise checklists for small projects to simplify compliance workflows related to **NPR 7150.2** and **NASA-STD-8739.8**.

* + Example Template:
    - ✅ Documentation of relevant requirements completed.
    - ✅ Peer review logs finalized and archived.
    - ✅ Testing results match assurance metrics.

#### **Collaboration Resources**:

* + Engage with the **[NASA Software Engineering Community of Practice (CoP)](https://nen.nasa.gov/web/software)** through the NASA Engineering Network (NEN).
  + Utilize formal training or guides specific to small projects to streamline compliance activities.

### 4.1.3  Scenario Examples for Small Projects

#### **Scenario 1**: Internal Software Reuse for Data Analysis Tool

* + **Situation**: A small team developed Class F software for internally processing mission data and plans to share it across centers.
  + **Action**:
    1. Complete compliance matrix (e.g., "Functionality validated with unit tests, peer reviews performed").
    2. Register the tool in **AART**.
    3. Conduct one final assurance review focused on usability testing logs.

#### **Scenario 2**: Software Using Open-Source Library

* + **Situation**: A small project integrates open-source code and must verify its reuse permissions before internal sharing.
  + **Action**:
    - Map open-source licensing terms in the compliance documentation.
    - Conduct a lightweight licensing review (collaborate with Legal and OCIO).
    - Document risks for classified or proprietary restrictions.

### 4.1.4  Key Takeaways for Small Projects

1. **Streamlined Compliance**: Focus on lightweight tools and simplified documentation to avoid overwhelming teams.
2. **Tailoring Flexibility**: Tailoring requirements with Technical Authority approval allows small projects to adapt **NPR 7150.2** to their scale and scope.
3. **Early Engagement**: Collaborate with your Center, Technical Authorities, and OCIO early to make compliance smoother.
4. **Centralized Key Tasks**: Leverage the **AART** repository and the NASA CoP to simplify documentation, registration, and assurance approval.

## 4.2 Conclusion

By applying this tailored approach, small projects can efficiently meet the requirement while minimizing administrative burden and technical risks.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-081)

  [NASA Security Program Procedural Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1600&s=1A "Click to open in new window")

  NPR 1600.1A, Office of Protective Services, Effective Date: August 12, 2013, Expiration Date: December 12, 2021
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-258)

  [NASA Engineering Network, Software Engineering Community](https://nen.nasa.gov/web/software "Click to open in new window")

  Welcome to the Software Community. Software engineering is a core capability and a key enabling technology for NASA's missions and supporting infrastructure.  Software Community site covers topics such as software requirements, design, implementation, architecture, assurance, testing, training, tools, process improvement, best practices, software release, models and simulations, and software research and technology innovation.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-404)

  [Agency Application Rationalization Tool (AART)](https://aart.nasa.gov/aart-1.12.0/home "Click to open in new window")

  NASA's Agency Application Office, version 1.11,  NASA's authoritative source for inventorying all of NASA's software and is used to manage the Agency application portfolio through rationalization activities that leverage business value, technical health, and Agency strategic direction.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

### 5.2.1 Agency’s Application Rationalization Tool

To support software centralization and inventory visibility, NASA requires internally developed software applications under the technical authority of the Office of Chief Information Officer (Class F) to be registered within the Agency’s repository for application management.   The current enterprise repository is the Agency’s Application Rationalization Tool (AART) [404](#_tabs-<p></p>).   This will enhance the ability to identify duplicative or obsolete software.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following lessons learned from the NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** provide insights into challenges, best practices, and outcomes relevant to ensuring that shared software complies with NASA's software engineering requirements. These lessons focus on scenarios where non-compliance caused issues or where proper implementation of policies led to success.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Importance of Software Compliance for Reuse

* **Lesson Title**: *Non-Compliance with Software Standards Led to Integration Challenges*
* **Lesson Number**: 1056
* **Summary**:
  + A NASA project attempted to integrate software components from a previous mission into a new mission system. The reused software did not conform to updated software engineering standards, specifically **NPR 7150.2** **[083](#_tabs-<p></p>)**. As a result, significant rework was needed to address integration problems, including correcting outdated interfaces, incomplete documentation, and non-compliance with assurance requirements. The delays impacted the project’s schedule and budget.
* **Relevance to the Requirement**:
  + Software included in NASA’s reuse catalog must conform to current engineering requirements to ensure smooth integration into future projects. Listing non-compliant software creates downstream risks for other missions or programs, increasing costs and schedules.
* **Key Takeaway**:
  + Only software validated for compliance with applicable engineering standards (e.g., **NPR 7150.2** and **NASA-STD-8739.8 [278](#_tabs-<p></p>)**) should be shared or reused. Non-compliance shifts the burden to future users, increasing costs and technical debt.

#### 2. Documenting Compliance Improves Software Reusability

* **Lesson Title**: *Inadequate Documentation Hindered Software Reuse*
* **Lesson Number**: 0537
* **Summary**:
  + A software system developed for internal NASA use lacked clearly documented compliance matrices for software requirements. When the software was later shared between two Centers, the receiving team had difficulty verifying its reliability and safety because there was no evidence that applicable software engineering policies had been followed. This gap significantly increased the costs to validate the software for reuse.
* **Relevance to the Requirement**:
  + A completed compliance matrix serves as tangible evidence that shared software adheres to **NPR 7150.2** and **NASA-STD-8739.8**. Without a compliance matrix, future users must carry out expensive re-verification and validation processes, negating the benefits of software reuse.
* **Key Takeaway**:
  + Before adding software to a reuse catalog, ensure it is accompanied by a validated compliance matrix and supporting documentation to streamline future reuse efforts.

#### 3. Tailoring Software Requirements Requires Clear Documentation

* **Lesson Title**: *Undefined Tailoring Led to Misinterpretations about Compliance*
* **Lesson Number**: 1276
* **Summary**:
  + In one case, a project tailored certain software engineering requirements without documenting the rationale, accompanying risks, or Technical Authority approval. When this software was reused in another project, stakeholders assumed all original requirements had been met, leading to unknown risks during the adoption process. These risks caused late-stage problems, including software failures in test environments.
* **Relevance to the Requirement**:
  + Tailored requirements must be clearly documented, along with all risks, mitigations, and Technical Authority approvals, and recorded in the compliance matrix before the software is shared. This ensures transparency and prevents false assumptions about conformance.
* **Key Takeaway**:
  + For tailored software, ensure that deviations or waivers from standard requirements are documented, justified, and approved by the appropriate Technical Authorities.

#### 4. Software Safety and Assurance Must Be Integral to Sharing

* **Lesson Title**: *Inadequate Software Assurance Applied to Shared Tools*
* **Lesson Number**: 0932
* **Summary**:
  + NASA distributed internally developed software tools for data analysis through an internal sharing repository. However, these tools had skipped key verification and validation (V&V) steps required by **NASA-STD-8739.8** for internal assurance, leading to defects being discovered during use. Some defects impacted the accuracy of scientific analysis, undermining the tool’s value.
* **Relevance to the Requirement**:
  + Software must meet assurance and safety standards under **NASA-STD-8739.8** before inclusion in the reuse catalog. Assurance activities like V&V act as quality gates, preventing critical defects from propagating to downstream users.
* **Key Takeaway**:
  + Prioritize assurance and safety evaluations for software being shared internally. Document results of mandatory assurance tasks before adding the software to a reusable catalog.

#### 5. Continuity of Software Standards Ensures Long-Term Reusability

* **Lesson Title**: *Outdated Standards in Legacy Software Restricted Reuse Potential*
* **Lesson Number**: 1534
* **Summary**:
  + Legacy software developed using outdated methodologies and standards became unusable due to a lack of updates to comply with newer NASA software engineering policies. While the software had worked well for its original mission, its reuse in newer projects was infeasible without a complete overhaul. This lack of compliance prevented the cost savings initially assumed by reusing the software.
* **Relevance to the Requirement**:
  + Software intended for sharing and reuse must conform to current NASA software engineering requirements to avoid becoming obsolete. This emphasizes the importance of updating older software in accordance with current policies before adding it to internal reuse catalogs.
* **Key Takeaway**:
  + Ensure that legacy software is reviewed and updated as needed to conform to current **NPR 7150.2** and **NASA-STD-8739.8** standards before listing it for reuse.

#### 6. Integration of Commercial or Third-Party Software Must Be Assessed

* **Lesson Title**: *Third-Party Software Licensing Issues Impacted Reuse*
* **Lesson Number**: 0884
* **Summary**:
  + A NASA project included third-party software components for which the original licensing agreements did not allow redistribution. Despite being listed in the reuse catalog, the receiving team was unable to use the software due to licensing conflicts, leading to wasted integration efforts.
* **Relevance to the Requirement**:
  + All software listed for internal sharing must include documentation verifying ownership and licensing compliance. Without assessing legal and licensing constraints, projects risk redistributing software that cannot be reused or shared effectively.
* **Key Takeaway**:
  + Verify third-party software rights and licensing compliance before adding software to sharing catalogs. Ensure this information is included in the compliance matrix.

#### 7. Regular Audits of Shared Repositories are Essential

* **Lesson Title**: *Unverified Software in Internal Catalog Led to Reuse Failures*
* **Lesson Number**: 1647
* **Summary**:
  + A NASA Center did not enforce regular audits of its internal software sharing catalog. As a result, several pieces of software listed in the repository were outdated, non-compliant with current standards, or lacked documentation of previous compliance. When future projects attempted to reuse the software, these gaps created significant integration issues and duplicated validation efforts.
* **Relevance to the Requirement**:
  + The Center Director or their designee should ensure regular audits of the reuse catalog to remove non-compliant software or update entries to meet current standards.
* **Key Takeaway**:
  + Implement periodic reviews of software listed in sharing repositories to ensure continued compliance with current software engineering policies and requirements.

#### 8. Software Criticality Analysis Prevents Operational Risks

* **Lesson Title**: *Ignoring Software Safety-Critical Designations Introduced Hidden Risks*
* **Lesson Number**: 1193
* **Summary**:
  + A project team underestimated the potential safety-criticality of their software. When the software was shared internally for reuse, it was later identified as safety-critical during system safety analyses. Because it had not been developed to safety-critical standards, modifications were required to bring it into compliance, delaying critical integration timelines.
* **Relevance to the Requirement**:
  + The appropriateness of safety-critical designations should be evaluated early. Only software that has followed safety-critical assurance processes (when applicable) should be listed in the reuse catalog.
* **Key Takeaway**:
  + Ensure that software safety-criticality is assessed, and all safety-related requirements in **NASA-STD-8739.8** are met before sharing.

### 6.1.2  Conclusion

The NASA lessons learned referenced above consistently highlight the importance of ensuring software conforms to NASA engineering policies, safety standards, and compliance matrices before listing it in an internal reuse catalog. To implement this requirement effectively:

* Validate every software component using **NPR 7150.2's Requirements Mapping Matrix** and ensure tailoring decisions are documented and approved.
* Conduct assurance activities per **NASA-STD-8739.8** to ensure software quality and reliability.
* Confirm compliance with licensing and legal requirements for third-party or open-source software.
* Stress the importance of documentation and perform regular audits of shared repositories to maintain trust and promote efficient software reuse.

Adhering to these principles ensures that shared software is reliable, safe, and reusable, providing long-term value across missions and programs.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-216 - Internal Software Sharing List**

2.1.5.14 The Center Director, or designee, shall ensure that all software listed on the internal software sharing or reuse catalog(s) conforms to NASA software engineering policy and requirements.

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

This requirement ensures that all software listed in NASA's internal software sharing or reuse catalog(s) complies with NASA software engineering policies and requirements. The goal is to verify that software assets available for reuse meet applicable standards for performance, quality, safety, reliability, and assurance so they can be confidently shared and reused across NASA projects.

Software Assurance (SA) personnel are responsible for ensuring the software in these catalogs has undergone appropriate reviews and assessments for conformity and compliance with NASA’s engineering and assurance policies.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Verify Conformance to NASA Software Policies

1. **Ensure Compliance with****NPR 7150.2**[083](#_tabs-<p></p>)
   * Confirm that all software listed on the internal software sharing or reuse catalog complies with **NPR 7150.2** requirements, including:
     + Software Classification (e.g., Class A, B, C, etc.).
     + Compliance with software engineering processes (e.g., requirements capture, design, implementation, and testing).
     + Documentation of software development artifacts such as Software Development Plans (SDPs), Verification and Validation (V&V) Plans, and Test Reports.
2. **Validate Compliance with****NASA-STD-8739.8** [278](#_tabs-<p></p>)
   * Ensure that listed software complies with the **Software Assurance and Software Safety Standard**, including:
     + Software safety considerations for critical or high-risk applications.
     + Metrics or evidence of sufficient testing for safety, reliability, and quality.
     + Completion of appropriate assurance activities.
3. **Additional NASA Standards and Policies**
   * Verify that software conforms to other relevant NASA-specific standards or guidance, such as:
     + Cybersecurity requirements and protections (e.g., **NPR 1600.1**[081](#_tabs-<p></p>)**, NPR 2810.1**[403](#_tabs-<p></p>)).
     + Applicable mission- or Center-specific software policies.

#### 7.4.2.2. Assess Software Quality for Inclusion in the Catalog

1. **Review Software Documentation**
   * Verify the completeness and accuracy of documentation associated with the listed software. Examples include:
     + Requirements Specifications (SRS).
     + Software Design Documents (SDD).
     + Test Plans and Test Results Reports.
     + Risk Management Plans, including identification of any known limitations or risks associated with the software.
   * Checklists are available in Topic [8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists) to aid in assessing the quality of these work products.
2. **Ensure Adequate Code Quality**
   * Confirm that the software meets coding standards (e.g., NASA coding practices) and avoids known quality issues, such as:
     + Presence of major defects or unresolved anomalies.
     + Usage of deprecated or unsupported tools or libraries.
     + Insufficient test coverage.
3. **Verify Previous Validation Results**
   * Ensure the software has been validated through appropriate Verification and Validation (V&V) processes. Evidence should include:
     + Test results that demonstrate functionality and reliability.
     + Corrective actions completed for identified issues.
     + Software performance fully meeting documented requirements.

#### 7.4.2.3. Confirm that Software Meets Requirements for Sharing and Reuse

1. **Check Development and Maintenance Practices**
   * Ensure that software listed in the catalog adheres to robust development practices, such as:
     + Adherence to configuration management practices (e.g., version control, build management).
     + Documentation of changes and updates to the software for traceability.
     + Clear instructions for installation, implementation, and configuration.
2. **Assess Suitability for Reuse**
   * Verify that the software is sufficiently adaptable and reusable for other NASA projects. The catalog should list:
     + The intended application domain and use cases for the software.
     + Prerequisites for reuse, such as specific licenses, dependencies, or hardware considerations.
     + Known constraints, limitations, or caveats (e.g., software performance under specific conditions).

#### 7.4.2.4. Audit Software Listed in the Catalog

1. **Perform Regular Compliance Audits**
   * Periodically review the software listed on the catalog for continued conformance with NASA's policies and requirements. Specifically:
     + Spot-check new software entries as they are added to the catalog.
     + Verify that entries aligned with earlier versions of NASA's standards are updated as standards evolve.
   * Audit software for unresolved issues or known defects that could affect its reuse.
   * See Topic [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) for checklists to aid in performing these compliance audits.
2. **Verify Correct Classification**
   * Ensure the software is correctly classified (Class A, B, C, etc.) based on its criticality and intended use. Misclassified software may lead to improper assurance activities and risks during reuse.
3. **Review Past Usage Records**
   * Evaluate feedback associated with software reuse efforts to identify any gaps in compliance or usability issues that need resolution.

#### 7.4.2.5. Ensure License and Ownership Compliance

1. **Check Licenses**
   * Verify that all software listed in the catalog is properly licensed for NASA sharing and reuse, ensuring compliance with intellectual property policies.
2. **Confirm Ownership**
   * Ensure that software developed by third parties or contractors gives NASA proper rights for sharing and reuse within internal projects.
3. **Document Usage Permissions**
   * Include any usage restrictions, permissions, or licensing details directly in the catalog for transparency.

#### 7.4.2.6. Monitor Catalog Quality and Maintain Traceability

1. **Ensure Catalog Entries Are Complete**
   * Verify that every software entry in the catalog includes relevant metadata, such as:
     + Software class, domain/type, and applicable standards.
     + Version numbers and update history.
     + Contact information for the software-owner or responsible team within NASA.
2. **Maintain Traceability**
   * Ensure every piece of listed software is traceable to its origin, through development, testing, and validation artifacts.

#### 7.4.2.7. Recommend Process Improvements for Catalog Management

1. **Identify Gaps**
   * Provide feedback to the Center Director or designee if software in the catalog:
     + Is missing critical assurance or engineering artifacts.
     + Has unresolved compliance issues.
     + Is outdated or unsuitable for reuse.
2. **Promote Automation**
   * Recommend the use of automated tools or dashboards to assess compliance and track updates to listed software.
3. **Monitor Feedback**
   * Suggest improvements to catalog management based on feedback from engineers and assurance teams using the software.

### 7.4.3  Expected Outcomes

Through proactive software assurance activities, the following outcomes will be achieved:

1. **Compliance Assurance**
   * All software in the internal sharing or reuse catalog conforms to NASA software engineering policies and requirements.
2. **High-Quality Software for Reuse**
   * Software listed in the catalog is fully validated, functional, safe, and reliable for use in future projects.
3. **Improved Catalog Oversight**
   * Regular audits confirm conformance and compliance, preventing the inclusion of software with defects, risks, or unresolved assurance issues.
4. **Visible Software Metadata**
   * Each shared software entry contains clear metadata to support its safe and efficient reuse.
5. **Reduced Risk for Reuse Projects**
   * Software assurance and engineering efforts during reuse are supported by well-documented, compliant catalog entries.

### 7.4.4   Conclusion

Software Assurance (SA) personnel must ensure all software listed in NASA's internal sharing or reuse catalog adheres to NASA engineering policies (e.g., **NPR 7150.2**) and assurance standards (e.g., **NASA-STD-8739.8**). The software must be fully validated, traceable, and accompanied by clear documentation to support safe and efficient sharing/reuse. Through audits, assessments, and feedback, SA helps reduce risks and ensures compliance, contributing to the reliability and quality of software assets shared within NASA.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.15 - SA Tasking Checklist Tool](https://swehb.nasa.gov/display/SWEHBVD/8.15+-+SA+Tasking+Checklist+Tool) * [8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |
