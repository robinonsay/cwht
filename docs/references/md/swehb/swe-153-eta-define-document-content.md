# SWE-153 - ETA Define Document Content

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695509. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695509/SWE-153+-+ETA+Define+Document+Content

SWE-153 - ETA Define Document Content

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695509/SWE-153+-+ETA+Define+Document+Content#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695509)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695509&showCommentArea=true&showComments=true#addcomment)

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

2.1.5.12 The designated ETA(s) shall define the content requirements for software documents or records.

## 1.1 Notes

The recommended practices and guidelines for the content of different types of software activities (whether stand-alone or condensed into one or more project level or software documents or electronic files) are defined in NASA-HDBK-2203. The Center defined content should address prescribed content, format, maintenance instructions, and submittal requirements for all software related records. The designated TA for software approves the required software content for projects within their scope of authority. Electronic submission of data deliverables is preferred. “Software records should be in accordance with NPR 7120.5 [082](#_tabs-<p></p>), NPD 2810.1, NASA Information Security Policy [402](#_tabs-<p></p>), NPD 2800.1 [598](#_tabs-<p></p>), and NPR 2810.1 [403](#_tabs-<p></p>).”

## 1.2 History

Click here to view the history of this requirement: SWE-153 History

SWE-153 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 2.1.3.14 The designated Engineering Technical Authority(s) shall define the content requirements for software documents or records. |
| Difference between B and C | No Change |
| C | 2.1.5.14 The designated Engineering Technical Authority(s) shall define the content requirements for software documents or records. |
| Difference between C and D | Editorial fix for ETA(s) |
| D | 2.1.5.12 The designated ETA(s) shall define the content requirements for software documents or records. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

This requirement ensures that all software-related documents or records—such as requirements specifications, design documents, test plans, and verification reports—adhere to consistent, well-defined content expectations across NASA projects. By requiring the ETAs to define these content standards, NASA enables clear communication, compliance with agency policies, and alignment with project goals, while also ensuring that relevant information is properly captured, validated, and traceable throughout the software engineering lifecycle.

Clear and standardized content requirements minimize miscommunication, ensure compliance with technical and management policies, and facilitate seamless project execution across NASA Centers.

## 2.1 Key Rationale for the Requirement

### 1. Ensures Standardization Across Projects and Centers

* Science and exploration missions frequently involve contributions from multiple Centers and contractors, which can result in variations in documentation practices. This could lead to inconsistencies that impede collaboration, integration, and compliance efforts.
* The ETA-defined content guidelines ensure that software documents and records are uniformly structured, regardless of the project or Center, making it easier for all stakeholders to understand and work with them.

**Example**: A standardized software requirements specification (SRS) document ensures that requirements are consistently described in a format and level of detail understandable by all stakeholders, including developers, testers, and external contractors.

### 2. Clarifies Expectations and Communication

* By explicitly defining what content is required in software documents, the ETA eliminates ambiguity over what information needs to be captured and documented. This reduces misunderstandings during project planning and execution.
* Document content requirements also create a shared understanding among stakeholders, enabling smoother reviews, approvals, and audits.

**Example**: If a test plan must include a clear mapping of test cases to functional requirements, this explicit requirement ensures traceability from requirements to tests, reducing defects caused by overlooked requirements.

### 3. Improves Compliance with NASA Policies and Standards

* Documentation standards defined by ETAs ensure compliance with NASA-wide software engineering policies, such as **NPR 7150.2: Software Engineering Requirements**[083](#_tabs-<p></p>), and other relevant technical standards.
* Compliance ensures that all software records adequately support quality assurance, software safety, and mission assurance requirements, reducing the likelihood of deviations from key engineering principles.

**Example**: Defining the minimal content requirements for software configuration management plans ensures adherence to **NPR 7150.2** [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) and helps avoid costly mismanagement of software assets.

### 4. Supports Software Quality and Risk Management

* Clearly defined content requirements improve the clarity, comprehensiveness, and quality of software documentation. This ensures that critical design, safety, and operational details are not overlooked, reducing software defects, missteps, and communication failures.
* Strong documentation helps identify, track, and mitigate risks throughout the software lifecycle.

**Example**: Requiring a detailed "Risk Mitigation Section" in design documents ensures proactive identification and documentation of software risks and their mitigation strategies.

### 5. Enables Traceability and Lifecycle Management

* ETA-defined content requirements ensure that all software documents contain the necessary traceability information, such as links between requirements, designs, tests, and verification results. This full traceability supports auditability, reuse, and effective change management.
* Capturing the correct data at the right level of detail ensures that each phase of the software lifecycle is well-documented, making it easier to manage transitions between phases or resolve issues.

**Example**: Including a "Traceability Matrix" in verification documents ensures that all requirements are linked to test artifacts and verification results, which is critical for demonstrating that the software meets mission objectives.

### 6. Enhances Collaboration Across Multidisciplinary Teams

* NASA’s projects involve multiple disciplines—not just software engineers, but also systems engineers, testing teams, safety assurance engineers, and external partners. With well-defined content standards, multidisciplinary teams can easily understand and use software documentation, fostering collaboration and reducing the risk of conflicting interpretations.

**Example**: A standardized hazard analysis document ensures that both software developers and safety engineers can identify software elements contributing to mission-critical risks, leading to better collaboration on mitigation strategies.

### 7. Reduces Rework and Misalignment

* Poorly defined or vague content requirements can lead to incomplete or unclear documentation, leaving gaps that need to be revisited and revised. Rework delays software development timelines, increases costs, and introduces potential risks.
* Clear content definitions from the ETA ensure that documents and records are complete, accurate, and meet expectations the first time, reducing effort spent reworking deliverables.

**Example**: Including clear "Expected Inputs and Outputs" sections in interface control documents (ICDs) prevents misunderstandings between interfacing systems or teams, avoiding costly post-integration fixes.

### 8. Facilitates Project Oversight, Reviews, and Decisions

* Software documentation is a key component in decision-making processes, including design reviews, milestone assessments, and risk evaluations. ETA-defined content standards ensure that software documents include all the necessary information, making oversight more efficient and thorough.
* Effective oversight improves decision-making, reduces risks, and enhances the likelihood of project success.

**Example**: During a critical design review (CDR), an ETA-defined "Trade Study Section" ensures that reviewers can evaluate the key trade-offs behind architectural decisions, facilitating informed approval or requests for rework.

### 9. Maintains Institutional Knowledge for Future Use

* Software documentation serves as an enduring record of project activities, decisions, and lessons learned. By requiring clear, consistent content, ETAs ensure that these records can be effectively interpreted and reused by future teams.
* This strengthens institutional knowledge within NASA and benefits subsequent projects through better continuity and lessons learned.

**Example**: Clear and standardized end-of-life documentation from a completed software project (e.g., mission operation instructions) can serve as a basis for developing similar systems in future missions.

### 10. Enables Adaptability to Evolving Missions and Technologies

* Well-defined and consistent documentation requirements enable software documents to be more adaptable to evolving project needs, technologies, and mission objectives while still conforming to a universal standard.
* By clearly describing the document content for evolving technologies (such as AI-based systems or autonomous spacecraft), ETAs ensure that required documentation evolves alongside the software engineering discipline.

**Example**: If ETAs require bias evaluation and mitigation sections in documentation for machine-learning-based software, future teams working with similar technology will have the necessary framework to address such concerns.

## 2.2 Summary of the Rationale

**ETA-defined content requirements for software documents or records are critical to:**

1. Promote standardization and consistency across NASA Centers and projects.
2. Ensure compliance with NASA software engineering policies (e.g., **NPR 7150.2**).
3. Enhance software quality, reduce risks, and improve traceability.
4. Facilitate collaboration among multidisciplinary teams.
5. Reduce rework and associated costs by providing clear documentation expectations.
6. Support effective oversight, lifecycle management, and future knowledge transfer.

## 2.3 Conclusion

The ETA’s role in defining content requirements for software documents is foundational to NASA’s ability to build high-quality, reliable software systems for its missions. The inclusion of this requirement ensures that all stakeholders have clear, actionable, and complete documentation, enabling successful project execution, compliance, and long-term value.

# 3. Guidance

## 3.1 Document Content

Software documentation plays a critical role in ensuring clarity, traceability, and compliance with agency and Center-specific requirements throughout the software engineering lifecycle. The Engineering Technical Authority (ETA) is responsible for defining the content requirements for software documentation, balancing Center-level data management needs and project-specific requirements to ensure consistency and adaptability. Below is an enhanced set of guidance to ensure software documentation content is well-defined, tailored appropriately, and accessible to project teams.

### 3.1.1  Defining Documentation Content

The content requirements for software documentation are typically defined by each NASA Center's data requirements management system or equivalent process. These requirements outline the essential elements that software documentation must address.

1. **Coordination with the Engineering Office of Primary Responsibility (OPR)**
   * The ETA is responsible for approving and coordinating any proposed tailoring or modification to the defined documentation content.
   * Tailoring must ensure that software documentation still meets project needs, adheres to NASA policies, and complies with **NPR 7123.1: Systems Engineering Processes**[041](#_tabs-<p></p>).
   * Tailoring activities should always be coordinated with the Center’s Engineering OPR and software engineering organizations to ensure that any modifications are justified and acceptable.
2. **Baseline Content and Tailoring**
   * If the documentation content required for a software project aligns with the standard content defined in the Center’s data management requirements, the ETA’s role will be simple—ensuring compliance with those predefined content descriptions.
   * When project-specific content requirements differ or need enhancements, the ETA must define and document those changes while ensuring proper reviews and approvals.
3. **Minimum Content Requirements**
   * A minimum set of content elements for software project documentation is provided in Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) of this Handbook.
   * The ETA may adopt the Agency-wide minimum content “as is” or enhance it to develop Center-specific documentation requirements tailored to the needs of their software projects.
   * See also Topic [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) for additional content considerations.

### 3.1.2  Key Elements of Center-Specific Documentation Requirements

ETA-approved documentation descriptions for software-related records should include the following foundational elements:

1. **Specific Content**
   * Define the required topics and include clear descriptions of the material and information to be addressed. For example:
     + Functional requirements, constraints, and system interfaces.
     + Traceability matrices (linking requirements to design and verification).
     + Risk and issue management processes or summaries.
     + Test descriptions and results documentation.
2. **Content Format**
   * Specify the layout, structure, and formatting requirements for documents to promote consistency across projects. This includes:
     + Section organization (e.g., introduction, purpose, scope, and content sections).
     + Formatting and labeling of tables, figures, and appendices.
     + Preferred visual styles and document organization (e.g., header-footer usage, font choice).
3. **Maintenance Instructions**
   * Provide details for regular updates and maintenance, ensuring documents remain current throughout the software lifecycle. Maintenance guidance should address:
     + Update triggers, such as project milestones, changes in scope, or evolving requirements.
     + The frequency of reviews and revisions.
     + Responsibilities for document maintenance (e.g., project leads, software engineers, or verification leads).
4. **Submittal Requirements**
   * Define expectations for the delivery of software documentation to stakeholders, including:
     + **Delivery frequency**: e.g., aligned with life cycle milestones (e.g., SRR, PDR, CDR).
     + **Format**: Electronic submission is preferred, with files typically required in accessible, reproducible formats (e.g., PDFs, editable documents).
     + **Storage and access**: Deliverables must be stored in electronic repositories, such as Center Process Asset Libraries (PALs), accessible to authorized personnel.

**Note**: ETAs should align the content requirements with **NPR 7123.1** and Center-specific Data Management Guidance available in Center repositories.

### 3.1.3  Preference for Electronic Submission

Electronic submission of data deliverables is strongly encouraged. The ETA should prioritize delivery through electronic systems and define the expectations for:

* Content specification, including which materials can or must be delivered electronically.
* Preferred software tools, file types, and repository platforms for document storage.
* Proper archiving procedures to ensure the integrity of documentation throughout the life of the project.

## 3.2 Document Format

Software documentation can be specified in a wide array of formats that provide flexibility and usability for different project needs. By leveraging templates, data item descriptions (DIDs), database forms, and other standard formats, Centers can ensure consistency, accessibility, and ease of use for software engineering teams.

#### Defining Document Format Options

1. **Templates and Checklists**
   * Predefined templates provide a consistent structure and format for documentation. ETAs should develop and maintain templates for essential documents like:
     + [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan).
     + [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification).
     + Interface control documents (ICD).
     + [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description).
     + [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
     + [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures)
     + [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report).
     + Verification and Validation (V&V) Plans/Reports.
     + Safety Analysis and Hazard Reports (see [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis)).
   * Predefined checklists provide the basics for assessing and evaluating software engineering project assets (see Topic [8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists).)
2. **Data Item Descriptions (DIDs)**
   * DIDs define the characteristics and content required within specific software deliverables. They may be used as part of internal documentation or added to contractor agreements. Examples include:
   * Specifications for software product deliverables.
   * Performance metrics reporting formats.
3. **Database and Digital Formats**
   * Replacing traditional documents with database forms or other digital asset formats may improve access and traceability. These formats can centralize data such as:
   * Requirements traceability matrices stored in relational databases.
   * Automated logs (e.g., versioning records).
   * ETAs should encourage these formats where integrated with collaborative tools (e.g., JIRA, IBM DOORS).

#### Repository of Approved Documentation Guidance

* Center-level repositories (e.g., Process Asset Libraries, or PALs) should host all approved documentation guidance for ease of access by software engineering teams, acquisition personnel, and contractors.
* These repositories should also include Center-specific templates, examples, and instructions vetted by the ETA.

#### Contributions to SPAN (Software Processes Across NASA)

* ETAs should submit approved documentation guidance to the NASA SPAN repository for Agency-wide use whenever applicable. This ensures that proven templates, examples, and best practices are shared across Centers and contribute to NASA’s overall knowledge base.

## 3.3 Supporting Resources

1. **Center Process Asset Libraries (PALs)**
   * Center PALs provide access to consolidated guidance, templates, and data forms. Engineers should refer to these resources to maintain compliance with Center documentation standards.
   * Submissions to the PAL should be version-controlled and updated in alignment with Center Data Management Guidance.
2. **Software Processes Across NASA (SPAN)**
   * SPAN offers a centralized hub for NASA-specific documentation templates, examples, checklists, and workflows. ETAs should encourage engineers and contractors to utilize SPAN resources when available.

**Note**: Access SPAN from the SPAN tab in this Handbook for templates and documentation examples.

## 3.4 Conclusion

The ETA plays a vital role in defining precise requirements for software documentation content and format. This includes managing coordination with the Engineering OPR, tailoring documentation requirements to project needs, and ensuring compliance with Center-specific and Agency standards. By establishing clear content and format expectations, ETAs support consistency, traceability, and successful project outcomes while leveraging the broader institutional resources available at NASA.

Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) in this Handbook provides a minimum set of contents for software project documentation at the Agency level.  The designated ETAs at each Center can choose to use this minimum content “as is” or use it to define a set of Center documentation descriptions that are specific to the software projects at that Center. See also [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products).

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Center Libraries](https://nen.nasa.gov/web/software/wiki) |

# 4. Small Projects

Small projects often operate with limited resources, personnel, and timelines compared to larger missions. Despite these constraints, documentation remains a critical aspect of delivering high-quality software. This small project guidance provides streamlined recommendations for ensuring compliance with the requirement while balancing the unique needs and constraints of small projects.

## 4.1 Guidance for Small Projects

### 4.1.1  Key Considerations for Small Projects

Small projects generally prioritize agility, efficiency, and lightweight documentation while maintaining compliance with NASA policies. Documentation content requirements should account for the reduced complexity and resource availability, focusing on essential elements.

#### **Objectives for Small Projects**:

1. **Clarity**: Provide actionable guidance for documenting processes and deliverables without unnecessary detail or overhead.
2. **Simplicity**: Focus on lightweight, essential documentation tailored for the reduced complexity of small projects.
3. **Standardization**: Align documentation with existing templates and tools to avoid reinventing processes unnecessarily.
4. **Efficiency**: Minimize documentation burden while ensuring compliance and traceability.

### 4.1.2  Small Project Approach to Defining Document Content

#### 4.1.2.1  Tailored Content for Small Projects

ETAs should focus on ensuring that documentation requirements for small projects align with their scope. Prioritize lightweight content requirements for documents such as software development plans, test plans, risk management logs, and requirements traceability matrices.

**Recommended Essential Content for Small Projects:**

* **Software Requirements**
  + Define the functional requirements, interfaces, and constraints at a high level.
  + Use a simplified form of traceability (e.g., linking requirements directly to verification methods).
* **Design Documentation**
  + Include diagrams and descriptions of key architecture components.
  + Provide an overview of interfaces (internal and external) with minimal detail unless critical risks are identified.
* **Test Plans**
  + Summarize test objectives, test cases, and expected outcomes.
  + Provide a direct mapping of test cases to software requirements for traceability purposes.
* **Risk Management**
  + Simple tracking mechanisms for risks, mitigation strategies, and assigned responsibilities (e.g., spreadsheets or lightweight tools).
* **Software Verification and Validation Record**
  + Include a checklist of verification activities performed and evidence of validation (e.g., results from automated tests or functional demonstrations).

#### 4.1.2.2  Leverage Standardized Templates and Tools

* **Use NASA Templates**: Utilize templates available in Center Process Asset Libraries (PALs) or the **NASA SPAN repository (Software Processes Across NASA)** for essential documents.
  + These templates are pre-approved and align with Center-level and Agency-wide policies. Modify templates only as needed for project tailoring.
  + Examples: Software requirements specifications (SRS), design descriptions, test plans, and risk logs.
* **Electronic Submissions**: Use electronic repositories (e.g., PALs, JIRA, Confluence, or SharePoint) to streamline documentation and submission processes, avoiding paper-based recordkeeping.

#### 4.1.2.3  Align Documentation Expectations with Project Scope

Complete documentation is required to ensure compliance, traceability, and quality—even on small projects—but the level of detail should align with the reduced complexity of the project. ETAs should scale content expectations accordingly, focusing on delivering concise, highly focused documents.

**Example Scaling Approach**:

| Type of Project | Detailed Expectations | Small Project Expectations |
| --- | --- | --- |
| Large/Complex Mission | Comprehensive requirements document with full traceability to design/test. | High-level requirements document with basic traceability to tests. |
| Multi-Center Collaboration | Formalized risk matrix with assigned owners and weighted prioritization. | Simple risk log in a spreadsheet with brief mitigation notes. |
| Full Integration Testing Plan | Detailed test plan covering all functional/non-functional requirements. | Limited test plan with functional focus on critical subsystems. |

#### 4.1.2.4  Simplify Documentation Maintenance

Small projects will often experience rapid iteration or agile development cycles. To stay current with project progress while minimizing overhead:

* **Maintenance Guidelines**
  + Use lightweight, frequent update mechanisms for documentation (e.g., update logs electronically or maintain living documents in collaborative platforms).
  + Define update triggers, such as milestone reviews, requirements changes, or testing outcomes, rather than a fixed frequency.
  + Assign a single staff member (e.g., the project lead or software engineer) to maintain documents to avoid delays due to multi-stakeholder ownership.

**Example**: Updating a living document stored in Confluence after a sprint demo ensures the test plan reflects the most recent results without requiring separate offline work.

#### 4.1.2.5  Submittal Requirements for Small Projects

* Define clear delivery expectations for small projects that align with their scope:
  + **Delivery Frequency**: Synchronize document submission with major milestones (e.g., SRR, PDR, or handoff stages) rather than requiring frequent submissions.
  + **Electronic Format**: Deliver minimum-required documentation electronically through preferred repository systems (e.g., PDFs uploaded to PALs or shared drives).
  + **Timing**: Allow flexibility in submission timelines based on project priorities to reduce unnecessary administrative burden during periods of peak development activity.

#### 4.1.2.6  Focus on Collaboration Between ETA and Small Teams

For small projects, the ETA should provide additional support to ensure content requirements are easily defined and achievable. Regular collaboration between the ETA, project teams, and the Engineering Office of Primary Responsibility (OPR) ensures content expectations are right-sized for the project and any tailoring is effectively managed.

#### Steps for ETA Collaboration:

1. **Initiate Early Engagement**
   * During the early phases of the project, document key expectations for content and formats (e.g., during kick-off or preliminary reviews).
   * Provide small projects with access to templates and tools that reduce documentation effort.
2. **Facilitate Tailoring**
   * Collaborate with the team to identify tailoring needs. For instance, small projects may not need exhaustive design records but should maintain sufficient information for risk tracking and audits.
3. **Review Small Project Artifacts**
   * Help small teams refine deliverables and reduce unnecessary documentation overhead, keeping focus on core compliance and traceability goals.

### 4.1.4  Examples of Light Documentation Artifacts for Small Projects

Small projects should focus on providing essential elements while maintaining brevity:

1. **Software Requirements Documentation**
   * A concise document listing requirements, high-level system constraints, and a simple traceability table linking requirements to verification methods.
2. **Risk Log**
   * A single spreadsheet or lightweight form capturing identified risks, potential impacts, mitigations, and assigned owners.
3. **Test Plan**
   * A one-page map of test coverage, objectives, and key passes/fails for validation.
4. **Design Description**
   * Minimal diagrams and text that highlight the system architecture, critical interfaces, and major components.
5. **Verification Record**
   * A simple checklist summing up which tests were conducted, results, and whether they meet the defined software requirements.

### 4.1.5  Benefits of Approach for Small Projects

1. **Efficient Use of Resources**: Streamlined documentation reduces workload while ensuring compliance.
2. **Consistency Across Small Projects**: Alignment with Center templates and NASA policies ensures small projects meet agency-wide best practices.
3. **Improved Collaboration**: ETAs and project leads work together to tailor content while reducing administrative burdens.
4. **Enhanced Accessibility**: Electronic submission and standardized formats ensure easy access to project records for audits, reviews, and reuse.

## 4.2 Conclusion

For small projects, the ETA should focus on defining lightweight, tailored content requirements that provide essential clarity and compliance without imposing unnecessary burden. By leveraging existing NASA resources, aligning content with project scope, and simplifying documentation maintenance, small teams can achieve successful outcomes while supporting traceability, quality, and process governance. The practical recommendations above ensure that small projects deliver meaningful documentation while balancing agility and efficiency.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-031)

  [Manager's Handbook for Software Development,](http://www.everyspec.com/NASA/NASA-General/SEL-84-101_REV-1_1990_30283/ "Click to open in new window")

  SEL-84-101, Revision 1, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1990.
* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-402)

  [NASA Information Security Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2810&s=1E "Click to open in new window")

  NASA Office of the Chief Information Officer, May, 2015. NPD 2810.1E,
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-513)

  [Mars Climate Orbiter Mishap Investigation Board - Phase I Report](https://llis.nasa.gov/lesson/641 "Click to open in new window")

  Public Lessons Learned Entry: 641.
* (SWEREF-598)

  [Managing Information Technology](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2800&s=1E "Click to open in new window")

  NPD 2800.1E, Office of the Chief Information Officer, Effective Date: December 09, 2019, Expiration Date: December 09, 2024,

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** emphasizes the importance of establishing clear and well-defined requirements for documentation. Relevant lessons from past NASA projects highlight best practices, risks, and challenges associated with documentation content, particularly its role in ensuring traceability, uniformity, and project success. Below are lessons learned from the NASA LLIS database that align with this requirement.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Inadequate Documentation Can Lead to Misaligned Goals

* **Lesson Title**: *Deficiencies in Communication and Documentation Can Impact Mission Success*
* **Lesson Number**: 0270
* **Summary**:
  + In several projects, ambiguous or undefined documentation content led to misunderstandings between engineering teams, project stakeholders, and contractors. This misalignment caused delays, increased project costs, and led to additional iterations in the design and implementation phases. Clear documentation standards, including content expectations, could have prevented these issues.
* **Relevance to This Requirement**:
  + This lesson underscores the need for ETAs to define clear and actionable content requirements for all software documents. These defined requirements help ensure documentation communicates unambiguous details to all stakeholders, avoiding knowledge gaps and miscommunication.
* **Key Takeaway**:
  + NASA ETAs should enforce clearly articulated content requirements for documents such as Software Requirements Specifications (SRS), Interface Control Documents (ICDs), and Risk Management Plans to improve communication and minimize misunderstandings.

#### 2. Lack of Consistency in Documentation Hinders Integration

* **Lesson Title**: *Standardized Documentation is Critical for Multi-Center and Contractor Collaborations*
* **Lesson Number**: 0934
* **Summary**:
  + In multi-Center projects, inconsistent content and formatting in software documentation complicated integration efforts, particularly when transitioning between contractors and Centers. Confusion arose over requirements, test plans, and design assumptions because document formats varied widely and lacked standardized content. As a result, rework was required to establish a consistent baseline for understanding.
* **Relevance to This Requirement**:
  + Defining consistent documentation content standards ensures all teams—whether at NASA Centers, contractors, or external partners—are aligned on expectations. The ETA is critical to enforcing consistent standards, which are particularly useful in collaborative environments involving external entities.
* **Key Takeaway**:
  + The ETA must develop and enforce Center-wide content definitions for software documents that ensure consistent structure and content delivery, especially for projects requiring integration across multiple teams.

#### 3. Lessons from the Mars Climate Orbiter [513](#_tabs-<p></p>)

* **Lesson Title**: *Mars Climate Orbiter Mishap Due to Documentation and Communication Gaps*
* **Lesson Number**: 0641
* **Summary**:
  + The Mars Climate Orbiter spacecraft was lost due to a measurement unit mismatch between NASA and contractor teams. The critical error stemmed from insufficiently defined documentation for interface requirements, which did not specify the units of measurement. This gap in documentation led to catastrophic mission failure.
* **Relevance to This Requirement**:
  + This lesson highlights the critical role of defining content requirements in software documentation, particularly in interface control documents (ICDs) and design records. ETAs play a crucial role in ensuring that all necessary details, such as measurement units, data formats, and system constraints, are explicitly addressed in document content requirements.
* **Key Takeaway**:
  + ETAs must ensure that software documentation clearly defines interfaces, data exchanges, and critical technical parameters to eliminate ambiguity and avoid costly errors.

#### 4. Comprehensive Documentation Improves Knowledge Retention

* **Lesson Title**: *Documenting and Retaining Knowledge for Future Missions*
* **Lesson Number**: 1298
* **Summary**:
  + Many NASA programs have struggled to retain institutional knowledge between projects due to incomplete or inconsistently maintained documentation. For example, missing information about design decisions or verification methodologies made it difficult to transition lessons learned to similar missions down the line.
* **Relevance to This Requirement**:
  + This lesson emphasizes the necessity of defining comprehensive content requirements for software documentation to ensure that critical knowledge is captured and remains accessible to future programs. Properly defined content allows projects to build on past successes and avoid repeating mistakes.
* **Key Takeaway**:
  + ETAs should define documentation content requirements that explicitly include:
    - Design rationale and trade studies.
    - Historical context of decisions.
    - Verification and validation results.
  + These inclusions ensure long-term knowledge retention and support future mission success.

#### 5. Insufficient Traceability Leads to Verification Gaps

* **Lesson Title**: *Inadequate Traceability Between Software and System Requirements*
* **Lesson Number**: 1782
* **Summary**:
  + Several projects encountered severe challenges during the verification and validation (V&V) phase because software requirements were poorly documented and lacked clear traceability to system-level requirements and testing activities. This led to testing gaps and unmet mission objectives.
* **Relevance to This Requirement**:
  + This lesson highlights the importance of requiring strong traceability mechanisms within software documentation. ETAs must ensure that documentation explicitly includes traceability matrices or tables that connect system-level requirements with software features, design elements, and test results.
* **Key Takeaway**:
  + ETAs must define content requirements that include traceability matrices to ensure that all software requirements are linked to design and test phases, enabling thorough V&V processes.

#### 6. Clarity and Maintenance of Software Configurations

* **Lesson Title**: *Software Configuration Management Practices*
* **Lesson Number**: 0791
* **Summary**:
  + Poor configuration management practices were observed on several missions, particularly with insufficiently defined or outdated documentation. Missing or inconsistent documentation of software versions, baselines, or release notes caused confusion during debugging and integration. Clear documentation defined at the onset would have mitigated these issues.
* **Relevance to This Requirement**:
  + This lesson reinforces the importance of defining content requirements for software configuration management (SCM) documents, including critical details such as baseline definitions, version history, and release notes. By establishing clear guidelines for software configuration documentation, ETAs ensure better control over software evolution.
* **Key Takeaway**:
  + ETAs should define content expectations for software configuration documentation to help manage baselines, maintain consistency, and avoid integration issues.

#### 7. Documentation Tailoring for Small-Class Missions

* **Lesson Title**: *Lightweight Documentation Practices for Small Projects*
* **Lesson Number**: 2031
* **Summary**:
  + For small, resource-constrained projects, documentation requirements that were overly detailed or complex became challenging to implement, leading teams to skip critical aspects of documentation altogether. Tailored, lightweight documentation practices that maintain essential content were far more effective for achieving compliance.
* **Relevance to This Requirement**:
  + This lesson underscores the importance of tailoring documentation content requirements for small projects, balancing lightweight practices with the need to capture the essentials. ETAs play a key role in ensuring small projects can meet documentation requirements without overburdening their resources.
* **Key Takeaway**:
  + ETAs should adjust standard content expectations for small-class missions, ensuring lightweight, focused documentation without sacrificing key elements such as requirements traceability, risk logs, or test plans.

#### 8. Incomplete Test Documentation Can Threaten Mission Success

* **Lesson Title**: *Inadequate Test Planning and Result Documentation*
* **Lesson Number**: 0978
* **Summary**:
  + Inconsistent or incomplete documentation of test plans and results, including missing definitions of pass/fail criteria, made it difficult to verify that certain software systems met mission requirements. Without clear documentation, decision-makers lacked confidence in the test outcomes.
* **Relevance to This Requirement**:
  + Test documentation is one of the critical software records needed for successful project outcomes, and its content must be explicitly defined by the ETA. This includes test objectives, criteria, methodologies, procedures, and results.
* **Key Takeaway**:
  + Test documentation should include precise pass/fail criteria, traceability to requirements, and summaries of results. ETAs must define these content expectations to ensure all test plans and results are complete and actionable.

### 6.1.2  Overall Summary

These lessons highlight the importance of well-defined and consistent documentation practices, including:

1. **Standardization**: Ensuring uniformity of content across Centers and projects.
2. **Traceability**: Explicitly linking all software elements to their requirements, designs, and tests.
3. **Consistency and Completeness**: Avoiding gaps or ambiguities that threaten mission success.
4. **Tailoring**: Balancing scalability and compliance for projects of all sizes.

#### Actionable Insights for Compliance with This Requirement:

* ETAs must define content for software documents that align with mission needs while maintaining uniformity across NASA Centers.
* Clear content requirements for key software artifacts—such as requirements documents, test plans, risk logs, and design records—reduce risks and improve collaboration.
* Incorporate lessons learned into content requirements (e.g., defining unit conventions, emphasizing traceability, and tailoring content for small projects).

By applying these lessons, NASA can improve the quality, clarity, and impact of software documentation, reducing risks and enhancing mission success.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-153 - ETA Define Document Content**

2.1.5.12 The designated ETA(s) shall define the content requirements for software documents or records.

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

The purpose of this requirement is to ensure that the designated **Engineering Technical Authority (ETA)** defines consistent, clear, and complete content requirements for software documents and records. These requirements provide the foundation for ensuring software deliverables meet NASA engineering, safety, and assurance expectations and are aligned with standards.

Software Assurance (SA) personnel are responsible for verifying that the content requirements for software documents and records are clearly defined, comprehensive, and compliant with NASA standards, policies, and project needs.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Validate That the ETA Defines Content Requirements

1. **Verify Defined Content Requirements**
   * Confirm the ETA defines content requirements for all software engineering and assurance-related documents and records. These typically include:
     + [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan).
     + [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification).
     + [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description).
     + [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
     + [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures)
     + [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report).
     + Verification and Validation (V&V) Plans.
     + Risk Management Plans.
     + Safety Analysis and Hazard Reports (see [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis)).
     + [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report).
     + Lessons Learned.
2. **Ensure Completeness**
   * Verify that content requirements:
     + Include all relevant details necessary for clarity and completeness (e.g., scope, objectives, roles, assumptions, inputs/outputs, methods, results).
     + Address the needs of all document stakeholders, including engineers, safety specialists, and assurance personnel.
3. **Validate Consistency with Standards**
   * Confirm the content requirements align with applicable NASA standards, such as:
     + **NPR 7150.2: NASA Software Engineering Requirements**[083](#_tabs-<p></p>)
     + **NASA-STD-8739.8: Software Assurance and Software Safety Standard**[278](#_tabs-<p></p>)
     + Other applicable Center-specific requirements or project-level agreements.

#### 7.4.2.2  Verify the Definition Process Used by the ETA

1. **Collaborate with the ETA**
   * Engage with the ETA during the process of defining content requirements to ensure software assurance considerations (e.g., safety, risk, quality) are fully addressed in specified document content.
2. **Ensure Traceability**
   * Confirm that content requirements are traceable to overarching project or agency-level policies, goals, and objectives. For example:
   * Requirements in a Safety Analysis Report should trace to NASA’s safety standards.
   * Content in a Verification and Validation (V&V) Plan should align with the broader V&V process defined in project documentation.
3. **Ensure Customization for Mission/Class**
   * Verify that content requirements account for the specific needs of software classifications (e.g., Class A, B, C) and mission risk levels. Content for higher-class software should include higher levels of rigor for risk identification, testing, assurance, and reporting.

#### 7.4.2.3  Verify the Content Requirements Address Assurance-Specific Needs

1. **Assurance-Specific Content**
   * Ensure software documents or records include sections or content related to:
     + Software safety and criticality analysis.
     + Software assurance risk identification and management.
     + Compliance with assurance-related directives and standards.
     + Metrics for tracking assurance activities and quality performance.
   * Examples:
     + A Test Plan should identify responsibilities for recording and reporting test coverage and results for assurance reviews.
     + A Risk Management Plan should highlight assurance risks, their priorities, and mitigation strategies.
2. **Review Shared Content Across Teams**
   * Validate that documents shared between engineering and assurance perspectives (e.g., Risk Plans, Metrics Reports) contain sufficient mutual detail to support both functions' needs.

#### 7.4.2.4  Monitor Updates and Dissemination of Content Requirements

1. **Ensure Currency of Defined Content Requirements**
   * Verify the ETA periodically reviews and updates the defined content requirements to address:
     + Changes in NASA standards, policies, or project needs.
     + Lessons learned from project feedback or discrepancies.
   * Example: Updates to reflect emergent cybersecurity testing requirements or new safety-critical guidelines.
2. **Dissemination to Stakeholders**
   * Verify that content requirements are communicated to all relevant teams (e.g., software developers, testers, and assurance personnel) using appropriate training, documentation, or process standards.

#### 7.4.2.5  Perform Audits and Reviews of Documents Against Content Requirements

1. **Ensure Alignment of Documents with Requirements**
   * During SA audits and reviews, confirm that required documents comply with the ETA’s defined content requirements.
   * Check that documents are:
     + Properly complete and formatted.
     + Consistent with the required document or record structure.
     + Traceable to the processes or activities they intend to support.
2. **Identify Gaps**
   * If discrepancies are found during an audit (e.g., missing content sections, incomplete details), report the gaps and ensure corrective actions are taken.

#### 7.4.2.6  Provide Feedback for the Continuous Improvement of Content Requirements

1. **Suggest Improvements**
   * Provide suggestions to the ETA regarding content needs to enhance clarity, completeness, and usability of software documents. Examples:
     + Recommend templates for consistent document formatting or structure.
     + Advocate for inclusion of emerging concerns (e.g., lessons learned, cybersecurity risks).
2. **Foster Standardization**
   * Encourage alignment of Center-specific content requirements with NASA-wide standards to reduce redundancies and inconsistencies, especially for Agency-level or multi-Center projects.

### 7.4.3  Expected Outcomes

By implementing the above Software Assurance responsibilities, the following outcomes will be achieved:

1. **Comprehensive Content Requirements**:
   * The ETA-defined content requirements will ensure all software documents and records align with applicable NASA standards.
2. **High-Quality Software Documentation**:
   * Software documents developed according to the content requirements will be accurate, complete, and useful to all stakeholders, including those focused on software assurance.
3. **Improved Compliance Assurance**:
   * Defined content requirements will provide measurable criteria for SA reviews, improving audits' ability to detect and address gaps or misalignments.
4. **Alignment Across NASA**:
   * Shared, standardized content requirements ensure consistency across Centers while allowing customization for specific project or software classification needs.

### 7.4.4  Conclusion

Software Assurance (SA) personnel must verify that the content requirements for software documents and records, as defined by the ETA, align with NASA standards, address key assurance requirements, and provide sufficient details for their intended use. SA ensures these requirements are properly defined, disseminated, and applied across all relevant projects. By performing regular verification, audits, and feedback, SA contributes to the quality and consistency of software documentation, critical to achieving NASA’s software engineering and assurance objectives.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |
