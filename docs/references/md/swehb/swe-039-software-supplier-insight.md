# SWE-039 - Software Supplier Insight

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695416. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight

SWE-039 - Software Supplier Insight

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695416)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695416&showCommentArea=true&showComments=true#addcomment)

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

3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:

1. 1. Monitor product integration.
   2. Review the verification activities to ensure adequacy.
   3. Review trade studies and source data.
   4. Audit the software development processes and practices.
   5. Participate in software reviews and technical interchange meetings.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-039 History

SWE-039 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.6.1.1 The project shall require the software supplier(s) to provide insight into software development and test activities; at a minimum the following activities are required:  monitoring integration, review of the verification adequacy, review of trade study data and results, auditing the software development process, participation in software reviews and systems and software technical interchange meetings. |
| Difference between A and B | No change |
| B | 3.12.8 The project manager shall require the software supplier(s) to provide insight into software development and test activities; at a minimum, the software supplier(s) will be required to allow the project manager or designate to:   1. 1. Monitor product integration.    2. Review the verification activities to ensure adequacy.    3. Review trade studies and source data.    4. Audit the software development process.    5. Participate in software reviews and systems and software technical interchange meetings. |
| Difference between B and C | Changed "supplier(s)" to "developer(s)";  Added requirement to periodically report status;  Added requirement for SA personnel to be given the same access as the PM;  Added auditing of development practices; Removed requirement to participate in "System" technical interchange meetings. |
| C | 3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:   1. 1. Monitor product integration.    2. Review the verification activities to ensure adequacy.    3. Review trade studies and source data.    4. Audit the software development processes and practices.    5. Participate in software reviews and technical interchange meetings. |
| Difference between C and D | No change |
| D | 3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:   1. 1. Monitor product integration.    2. Review the verification activities to ensure adequacy.    3. Review trade studies and source data.    4. Audit the software development processes and practices.    5. Participate in software reviews and technical interchange meetings. |

## 1.3 Applicability Across Classes

Classes F and G are labeled with “X (not OTS)”.  This means that this requirement does not apply to off-the-shelf software for these classes.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

Software supplier activities are monitored to assure the software work products are produced per the project and software requirements. Appropriate use of software project "insight" (surveillance mode requiring monitoring of customer identified and contracted milestones) allows NASA to detect problems early and take corrective action if necessary. The insight activities cited in this requirement comprise a minimum set that assures a continual knowledge of the work status achieved by the software developer/supplier when executed over the software product's life cycle.

The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:

* Monitor product integration,
* Review the verification activities to ensure adequacy,
* Review trade studies and source data,
* Audit the software development processes and practices,
* Participate in software reviews and technical interchange meetings.

This requirement is foundational for ensuring transparency, accountability, and collaboration between the project manager, software assurance personnel, and software developers. It ensures all parties have the necessary insight into the critical stages and activities of software development. The periodic reporting and access to development activities serve to manage risks, maintain quality, and ensure the project remains aligned with its technical, schedule, and mission objectives.

This requirement establishes a foundation for improved oversight, accountability, and collaboration between software developers, project management, and software assurance personnel. It promotes transparency and provides opportunities to identify and address issues early in the development life cycle. By allowing insight into integration, testing, trade studies, and development processes, it ensures that the project meets technical goals, adheres to quality standards, and mitigates risks, leading to the delivery of reliable, safe, and mission-critical software.

## 2.1 Facilitates Transparency and Visibility

* **Why It Matters:**
  + Software development activities, especially for complex or safety-critical systems, can become opaque without predefined mechanisms for sharing progress and activities with the project manager and software assurance personnel.
  + Regular reporting and access provide a window into the development process, enabling oversight and ensuring alignment with mission goals and regulatory standards.
* **Rationale:**
  + **Periodic status reporting and activity monitoring** ensure the project manager has continuous visibility into project progress, reducing the likelihood of surprises and ensuring potential risks are identified early.

## 2.2 Supports Early Risk Identification and Corrective Actions

* **Why It Matters:**
  + Regular status updates and the monitoring of product integration, verification, and trade studies allow the project manager to identify issues—such as design or integration problems, requirements gaps, or test inadequacies—as early as possible.
  + Delays or defects identified later in the development life cycle (e.g., during integration or operational testing) incur significantly higher costs and risks.
* **Rationale:**
  + Allowing insight into development and test activities enables **early detection of deviations** and provides a mechanism for implementing corrective actions before they cascade into larger issues.

## 2.3 Monitors Compliance with Requirements

* **Why It Matters:**
  + Software development must adhere to NASA standards, project-specific requirements, and regulatory constraints. Monitoring product integration, auditing processes, and participating in reviews ensures developers are meeting these obligations throughout development.
  + Without regular reporting and oversight, deviations from requirements could go unnoticed, leading to non-compliant software that jeopardizes mission or operational integrity.
* **Rationale:**
  + Providing the project manager and assurance personnel with the ability to review and audit development activities ensures continuous compliance with technical and safety-related requirements.

## 2.4 Ensures the Adequacy of Verification Activities

* **Why It Matters:**
  + Verification activities (e.g., test case design, test execution, and validation of results) are critical to ensuring software meets its requirements and functions as intended. Poorly designed verification processes or inadequate test coverage can lead to undetected defects or operational failures.
  + Oversight of verification activities ensures that testing efforts are robust, thorough, and sufficient to catch potential defects.
* **Rationale:**
  + By allowing the project manager and software assurance personnel to **review verification activities,** the project team gains confidence that identified tests sufficiently address mission-critical requirements and acceptable risk levels.

## 2.5 Promotes Data-Driven Decision-Making through Trade Study Reviews

* **Why It Matters:**
  + Trade studies are critical for selecting appropriate designs, architectures, or tools during software development, especially when evaluating competing alternatives. Poorly substantiated or unsupported trade studies can lead to suboptimal technical and programmatic choices that impact the project's cost, schedule, or performance.
  + Source data review ensures that all decisions are made with appropriate and robust analysis.
* **Rationale:**
  + Allowing the project manager and assurance personnel to **review trade studies and source data** ensures that decision-making is grounded in sound engineering principles and that all alternatives and impacts are properly analyzed and understood.

## 2.6 Maintains Process Quality through Audits

* **Why It Matters:**
  + Software development processes and practices (e.g., requirements management, coding standards, testing, configuration management, and documentation) directly impact the quality of the software. Poor practices or inadequately managed processes can lead to defects, schedule delays, or mission risks.
  + Auditing these processes ensures compliance with NASA’s standards (e.g., NPR 7150.2 [083](#_tabs-<p></p>) ) and provides an opportunity to identify inefficiencies or areas for improvement.
* **Rationale:**
  + Allowing the project manager and software assurance personnel to **audit development processes** ensures practices meet quality standards and that deviations are immediately addressed.

## 2.7 Fosters Collaboration and Alignment

* **Why It Matters:**
  + Software reviews and technical interchange meetings are crucial for fostering collaboration between development teams, project managers, and assurance personnel. These interactions provide a forum for sharing progress, discussing challenges, and resolving issues.
  + Regular engagement ensures that all relevant parties remain aligned on technical goals, deliverables, and timelines.
* **Rationale:**
  + Participation in **reviews and technical interchange meetings** strengthens communication between stakeholders and maintains alignment throughout the software development life cycle.

## 2.8 Enhances Mission and Safety Assurance

* **Why It Matters:**
  + Software often serves as a critical component in NASA missions, and any failure can have catastrophic consequences (e.g., mission failure, loss of assets, or safety risks to personnel and the public). Continuous assurance of the development and testing activities is critical to ensuring software reliability, safety, and quality.
  + Lack of oversight at any stage of development increases the likelihood of defects that may lead to unacceptable risks.
* **Rationale:**
  + **Regular engagement with assurance personnel** ensures that mission-critical and safety-critical software components meet the stringent reliability standards necessary to support NASA missions.

## 2.9 Establishes Accountability

* **Why It Matters:**
  + Requiring the software developer to provide periodic updates and insight ensures accountability for progress and compliance with agreed-upon processes. Regular reporting pressures development teams to adhere to timelines, quality standards, and deliverables.
  + Without clear accountability mechanisms, progress reporting may be incomplete or not reflect actual project status, leaving risks hidden until they adversely affect the project.
* **Rationale:**
  + Regular reporting and insight promote a structured and disciplined approach to development, ensuring deliverables are tracked and accountability is maintained.

## 2.10 Aligns with NASA Lifecycle Standards

* **Why It Matters:**
  + NASA’s development standards (e.g., NPR 7150.2, NPR 7123.1 [041](#_tabs-<p></p>) ) emphasize lifecycle integration, product visibility, and risk management. Regular reporting and project alignment are direct implementations of these principles.
* **Rationale:**
  + This requirement directly supports adherence to NASA’s standards, ensuring the software development aligns with the Agency’s lifecycle management practices.

# 3. Guidance

This requirement establishes the **minimum NASA insight activities** that must be included in contracts with software suppliers to ensure consistent monitoring, evaluation, and progress tracking of software development. The key purpose of these activities is to provide NASA with sufficient knowledge and oversight of software development, test processes, and deliverables throughout the life cycle. While the requirement is primarily aimed at contracted suppliers, many of its principles can also be applied to internal supplier relationships to maintain consistency across projects.

This improved guidance provides a refined explanation of insight activities, clarifies their importance, and offers specific implementation advice for both external and internal supplier organizations.

## 3.1 Key Context: Insight vs. Oversight

* **Insight:**

  + Insight provides the customer (NASA) with the ability to monitor software development activities and deliverables with varying levels of intensity, ranging from low-level periodic reporting to active participation in meetings, audits, and on-site reviews.
  + Insight **requires collaboration and access** but does not directly control the supplier’s decisions or processes. Instead, it focuses on observation and evaluation of the developer’s adherence to contract requirements, metrics, and milestones.
* **Oversight:**

  + Oversight involves a **more active role in supervision** and decision-making by directly influencing the supplier’s processes, decisions, and outcomes. While oversight is not specifically covered in SWE-039, oversight activities are included in the project’s overall Software Management Plan (SMP) or the contract's Statement of Work (SOW) as appropriate.

## 3.2 Applying Insight Activities for External and Internal Suppliers

For external suppliers, the minimum insight activities must be included in the SOW, while for internal suppliers, a formal agreement (such as a memorandum of understanding or inter-organizational charter) must describe agreed-upon activities.

* **External Suppliers:**

  + The SOW should detail access rights, reporting requirements, and participation in reviews (e.g., trade studies, audits, and integration testing).
* **Internal Suppliers:**

  + Use internal agreements to explicitly define responsibilities, reporting obligations, and expected review participation to ensure alignment across NASA organizations.

Refer to **NPR 7120.5** [083](#_tabs-<p></p>) , **NPR 7120.7** [264](#_tabs-<p></p>) , **NPR 7120.8** [269](#_tabs-<p></p>) , and **NPR 7123.1**[041](#_tabs-<p></p>) for specific context and best practices in software integration, monitoring methodologies, systems reviews, and test planning.

## 3.3 The Value of Insight in Software Development

Insight ensures that the NASA software team can:

1. **Monitor Progress:** Gain continuous visibility into the supplier's software development lifecycle, ensuring alignment with critical milestones and deliverables.
2. **Validate Adequacy:** Confirm that developer processes and outputs are in line with the technical, quality, and safety requirements of the contract.
3. **Address Risks Early:** Detect and address integration, testing, or design issues as they arise, avoiding costly fixes later in the project.
4. **Support Decision-Making:** Leverage information from reviews and reports to guide engineering decisions and ensure contractual compliance.
5. **Ensure Transparency:** Enable open communication between NASA and the software supplier throughout the project lifecycle.

## 3.4. Spectrum of Insight Activities

The **level of insight** varies depending on the complexity, criticality, and nature of the project. These activities range from **low-intensity** (periodic reports) to **high-intensity** (on-site reviews, audits, and meetings). Below is an overview of the five key insight areas outlined in this requirement:

### 3.4.1 Monitoring Integration

Integration is a critical aspect of software development, where individual components are combined into a functioning system. Monitoring integration activities is essential to ensure interoperability between:

* Software components.
* Hardware systems.
* Communication protocols.
* Data and information architecture.

**Key integration monitoring goals:**

* Confirm compatibility between hardware and software systems.
* Validate that communication protocols, data transfer mechanisms, and interface architectures align with project requirements.
* Resolve discrepancies early, particularly for COTS (Commercial Off-The-Shelf) or legacy systems.

**Implementation Tips:**

* Add integration-specific milestones (e.g., subsystem tests, component integration) to the SOW.
* Ensure suppliers address legacy software issues (e.g., code re-hosting, translators, and middleware standards).
* Monitor testing results at the integration phase to inform go/no-go decisions.

See [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) and [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) for supplementary guidance.

### 3.4.2 Review of Verification Adequacy

Verification ensures the software meets the requirements that have been allocated to it. Proper insight into verification should focus on:

* The adequacy and breadth of testing (e.g., test cases, scenarios, and coverage).
* The results of inspections and audits.
* The thoroughness of documentation and audits undertaken during verification.

**Implementation Tips:**

* Specify verification reporting requirements (e.g., progress reports and test summaries) in the SOW.
* Include a clause in the SOW allowing NASA personnel to participate in **on-site verification reviews** and provide input during test execution.
* Ensure the developer uses **objective verification evidence** (e.g., quality metrics, test results) to substantiate claims.

### 3.4.3 Review of Trade Study Data and Results

Trade studies compare alternatives to ensure the most cost-effective, efficient, and technically viable solution is pursued. This process supports critical decision-making throughout the software life cycle.

**Key objectives for reviewing trade studies include:**

* Validating the analytical rigor and depth of studies.
* Ensuring alternatives have been appropriately compared against mission requirements.
* Maintaining traceability between trade studies and project-level decisions.

**Implementation Tips:**

* Require documentation of trade studies, including assumptions, evaluation criteria, and alternatives considered.
* Ensure contractual access to all trade study deliverables and source data.
* Use trade study reviews to evaluate design and implementation decisions (e.g., technology choices, tools, or frameworks).

### 3.4.4 Auditing the Software Development Processes

Audits ensure that the development processes comply with technical standards (e.g., NPR 7150.2, NASA-STD-8739.8 [278](#_tabs-<p></p>) ). Audits also assess the supplier’s compliance with contract requirements, processes, and deliverables.

**Key considerations:**

* Audits are independent examinations and must be performed by personnel who are external to the development process.
* Audits should assess both **products (e.g., software artifacts)** and **processes (e.g., coding standards, configuration management).**

**Implementation Tips:**

* Specify audit frequency and criteria in the contract or formal agreement.
* Include specific process areas for auditing, such as:
  + Code quality and adherence to coding standards.
  + Configuration management practices.
  + Test documentation and execution.

See Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) for additional details.

### 3.4.5 Participation in Software Reviews and Technical Interchange Meetings

Participation in reviews and technical interchange meetings enables NASA to maintain real-time insight into technical decisions, milestones, and issue resolution.

**Key activities:**

* Attend milestone reviews (e.g., **SRR**, **PDR**, **CDR**, **TRR**) and technical reviews.
* Provide recommendations and comments regarding software progress and risk mitigation.
* Use these meetings to gain insight into software architecture, requirements, design, and testing.

**Implementation Tips:**

* Specify meeting attendance frequency and topics in the SOW.
* Use periodic meetings to improve communication and strengthen accountability between the supplier and NASA.
* Where applicable, leverage services from external agencies (e.g., Defense Contract Management Agency) to assist in meeting oversight.

## 3.5 Final Considerations for Insight Activity Success

1. **Balance Insight Activities:**

   * Define an insight strategy that balances NASA's need for adequate visibility into the supplier's progress with the need for minimal disruption to the developer’s processes.
2. **Integrate Metrics in the SOW:**

   * Use metrics (e.g., schedule adherence, defect density) to assess progress consistently.
3. **Leverage Relevant Standards:**

   * Reference **NPR 7123.1**, [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) and other technical standards to define clear expectations for insight activities.
4. **Document Agreements with Internal Teams:**

   * Internal projects or inter-Center collaborations should have agreements specifying roles, responsibilities, and insight deliverables.

By adhering to this enhanced guidance, projects can optimize the application of SWE-039, ensuring effective monitoring, robust evaluation, and successful collaboration with software suppliers to meet mission-critical objectives.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)        * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control) |

# 4. Small Projects

This requirement applies to all projects regardless of size. For small projects, the focus should be on simplifying insight and milestone activities while ensuring adequate visibility into the software development lifecycle. By tailoring milestone reviews, streamlining reporting, and specifying insight effectively in contracts, small projects can balance resource constraints with NASA’s requirements for quality, accountability, and risk management. This approach ensures small projects achieve their objectives efficiently without unnecessary overhead.

Small projects may not require the full spectrum of oversight and insight detailed for large-scale developments. In these scenarios, oversight and insight should focus on critical areas to provide adequate monitoring without creating unnecessary workload.

## 4.1 Recommended Insight Activities for Small Projects:

1. **Simplified Integration Monitoring:**

   * Confirm compatibility of key interfaces (e.g., software-to-hardware, external data inputs).
   * Examine a few **key metrics** that indicate successful integration (e.g., communication latency, data transfer accuracy).
   * Focus on monitoring integration for high-risk or safety-critical components rather than every subsystem.
2. **Essential Verification Reviews:**

   * Perform high-level reviews of the **verification plan** and **test case results** to ensure software meets its requirements.
   * Focus on safety-critical or mission-critical test results and documents.
3. **Focused Trade Studies:**

   * Evaluate trade studies only for areas likely to heavily impact cost, performance, or schedule (e.g., choosing between third-party technology solutions or defining key design trade-offs).
   * Minimize review time by focusing on high-impact decisions rather than less significant trade-offs.
4. **Streamlined Audits:**

   * Conduct limited process audits, focusing on processes directly tied to milestone success or high-risk areas (e.g., requirements traceability, configuration management, defect resolution timelines).
   * Reduce the frequency of audits while ensuring critical contractual agreements and requirements are verified.
5. **Participation in Key Reviews and Meetings:**

   * Attend critical milestone reviews, rather than being present at all meetings. For example:
     + **Preliminary Design Review (PDR):** Confirm alignment with requirements.
     + **Test Readiness Review (TRR):** Assess test preparedness and risk areas before executing key tests.

## 4.2 Managing Insight Through Practical Documentation

Small projects typically have limited documentation resources, so reporting and review processes must be simplified while maintaining compliance and quality.

#### **Reporting Strategy for Small Projects:**

1. **Focus on Essential Data:**

   * Replace lengthy progress reports with **milestone dashboards** summarizing:
     + Milestone status (complete/in-progress/at-risk).
     + Key metrics (e.g., schedule completion, defect density, test coverage rates).
     + High-level risk updates.
2. **Use Existing Documentation Tools:**

   * Leverage simple tools (e.g., project tracking software, checklists, or spreadsheets) to track insights, deliverables, and issues.
3. **Combine Roles and Deliverables:**

   * If staffing is limited, one document can address multiple purposes. For example:
     + Verification reports with embedded test summaries.
     + Design documents with traceability included.
4. **Leverage Templates:**

   * Use standardized templates for milestone reports, verification plans, and action item tracking to reduce customization work.

## 4.3 Creating Tailored Milestone Reviews

#### **Recommended Milestones for Small Projects:**

The project manager should define a **reduced** number of logical review milestones tailored to the small project’s schedule and risk profile. Common milestones include:

1. **Project Initialization and Planning:**

   * Initial Requirements Review (**IRR**): Verify that software requirements are well understood and documented before development begins.
2. **Development Phase:**

   * Interim Software Build Review: For verifying critical features and deliverables (e.g., prototyping or early-phase integration).
   * Test Readiness Review (**TRR**): Evaluate whether software is ready for formal testing.
3. **Delivery or Finalization Phase:**

   * Acceptance Review: Assess whether software complies with requirements, passes all key tests, and is suitable for deployment.

#### **Key Adjustments for Small Projects:**

* **Combine Reviews:** Combine overlapping reviews (e.g., **SRR** with **PDR** or **CDR** with **TRR**) where appropriate.
* **Use Agile Checkpoints (if applicable):** Replace traditional early-phase milestones (e.g., SRR) with incremental Agile milestone reviews tied to sprint goals.
* **Leverage Remote Reviews:** Use video conferencing and digital collaboration tools to reduce travel and streamline review costs.

## 4.4 Insight Documentation in Contracts for Small Projects

For small projects, **Contracts or Agreements** (for external suppliers) or **Internal Charters** (for inter-organizational collaborations) must still specify insight activities, but they can focus on practical and streamlined requirements.

#### **Minimum Contractual Elements:**

1. **Defined Reporting Requirements:**

   * Specify the content and frequency of reports (e.g., monthly status reports tied to milestone progress).
2. **Access Provisions:**

   * Ensure appropriate NASA personnel have access to key artifacts (e.g., test plans, logs) and permission to attend critical reviews.
3. **Participation Clauses:**

   * Include NASA’s right to participate in major verification activities, milestone reviews, and technical interchange meetings.
4. **Critical Metrics for Insight:**

   * Define 2-3 essential metrics (e.g., defect density, progress against schedule) to track supplier performance.

## 4.5 Suggested Practices for Small Projects

* **Maintain Regular Communication:**

  + Frequent, informal touchpoints (e.g., bi-weekly progress calls) can replace more structured reporting while still fostering transparency.
* **Leverage Hybrid Oversight:**

  + Use a mix of **on-site visits for critical events** (e.g., integration testing) and **remote engagement** (e.g., video reviews, file sharing) to save resources.
* **Use NASA Resources:**

  + Refer to standardized small-project workflows and guidance from the **Center’s Process Asset Library (PAL)** when in doubt.
* **Prioritize Risks and Critical Deliverables:**

  + Focus on activities that directly impact safety, mission success, and contractual compliance.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-030)

  [Hardware Quality Assurance Program Requirements for Programs and Projects](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8735&s=2C "Click to open in new window")

  NASA Office of Safety and Mission Assurance, NPR 8735.2C, Effective Date: March 12, 2021
  Expiration Date: March 12, 2026
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
* (SWEREF-168) COTS Software: Vendor Demonstration Guidelines and Scripts, Defense Acquisition University, 2009.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-219)

  [IEEE Standard for Software Reviews and Audits](https://ieeexplore.ieee.org/document/4601584 "Click to open in new window")

  IEEE Std 1028, 2008. IEEE Computer Society, NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-222)

  [IEEE Computer Society, "IEEE Standard Glossary of Software Engineering Terminology,"](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=2238 "Click to open in new window")

  IEEE STD 610.12-1990, 1990. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-262)

  [NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.](https://nen.nasa.gov/web/oce/ta "Click to open in new window")

  NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.
* (SWEREF-264)

  [NASA Information Technology Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=7A "Click to open in new window")

  NPR 7120.7A, Office of the Chief Information Officer, Effective Date: August 17, 2020,
  Expiration Date: August 17, 2025
  .
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-274)

  [Safety and Mission Assurance Acronyms, Abbreviations, and Definitions,](https://standards.nasa.gov/standard/nasa/nasa-hdbk-870922 "Click to open in new window")

  NASA-HDBK-8709.22. Baseline, 2018-03-08, Change 5: 2019-05-14
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-321)  COTS and Legacy Software Integration Issues,  Smith, Dennis and Novak, Rhoda, Chairs. GSAW. February 26, 1998.
* (SWEREF-475)

  [Defense Contract Management Agency website.](http://www.dcma.mil/ "Click to open in new window")

  website http://www.dcma.mil/.  Accessed January, 2018.
* (SWEREF-528)

  [Acquisition and Oversight of Contracted Software Development (1999)](https://llis.nasa.gov/lesson/921 "Click to open in new window")

  Public Lessons Learned Entry: 921,
* (SWEREF-535)

  [Space Shuttle Program/External Tank (ET)/Super Light Weight Tank (SLWT)](https://llis.nasa.gov/lesson/1048 "Click to open in new window")

  Public Lessons Learned Entry: 1048.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

A documented lesson from the NASA Lessons Learned database notes the following:

* **Misalignment with Commercial Vendor Software Capabilities**

**Incident:**  
Misaligned expectations for vendor simulation, interface details, and heritage design significantly delayed testing and integration activities. COVID‑related limitations reduced the required face‑to‑face interaction needed to align on software behaviors.

**Lesson Learned:**

* + **Deep Early Integration:** NASA personnel must work side‑by‑side with commercial partners early to align on simulation capabilities, interface assumptions, and development processes.
  + **Contractual Clarity:** Software deliverables and testbed capabilities must be unambiguously specified in contracts.

**Implication:**  
Weak alignment with vendor software ecosystems causes delays, rework, and verification gaps that can push missions off launch schedules.

* ### **Lessons Learned: Class D Lean SMA Resulting in Reduced Insight and Oversight Into Software Engineering**

  **Problem/Observation:**  
  Lean Safety and Mission Assurance (SMA) resourcing on a Class D mission led to reduced institutional insight and oversight into software engineering activities. The Anomaly Review Board (ARB) noted that insufficient SMA presence contributed to unrecognized risks in flight software (FSW), fault protection (FP), and COTS integration.

  **ARB Context:**  
  The ARB explicitly stated that:  
  “Achieving appropriate institutional oversight of Class D missions is a challenge… and needs to be explicitly planned for, addressed, and right sized.”

  **Contributing Factors:**  
  • FP and FSW were never elevated as major risks to project management, limiting visibility and engineering attention.  
  • Monthly status reviews were discontinued to save cost, reducing opportunities for institutional insight.  
  • JPL’s onsite resident at Lockheed Martin was removed and never replaced, eliminating a key source of direct oversight.  
  • COTS subsystems were integrated with insufficient SMA rigor, limiting understanding of behavioral risks.

  **Resulting Impacts:**  
  Reduced insight limited the project’s ability to detect emerging software risks, independently assess contractor activities, and ensure engineering completeness. Several issues surfaced late or only after anomalies occurred, increasing mission risk during integration and operations phases.

  **Relevant SWEHB Guidance:**  
  Even when tailoring for Class D, the SWEHB maintains core expectations for software insight and supplier oversight.  
  • SWE‑039 and SWE‑040 (Supplier Insight/Monitoring) require oversight proportional to risk, even when processes are tailored.  
  • Projects must ensure adequate engineering insight into outsourced, subcontracted, or COTS-based FSW components regardless of mission class.

  **Lesson Learned:**  
  Class D tailoring should not eliminate essential SMA insight mechanisms. Institutional oversight, supplier monitoring, and direct engagement with development teams must be right‑sized—but not removed. Ensuring that FP, FSW, and COTS software risks are actively identified, reviewed, and monitored is critical to maintaining mission readiness and preventing late‑phase discoveries.
* **Space Shuttle Program/External Tank (ET)/Super Light Weight Tank (SLWT). Lesson Number 1048**[535](#_tabs-<p></p>): A discussion on the shuttle program's certification of its super lightweight tank attests to the value of exercising insight and guidance through limited oversight activities.
* **Acquisition and Oversight of Contracted Software Development (1999). Lesson Number 0921**[528](#_tabs-<p></p>): Tailorable acquisition management and oversight processes for NASA contracted software development are essential to ensure that customers receive a quality product. A documented lesson from the NASA Lessons Learned database includes a cause of the loss of a mission "the lack of a controlled and effective process for acquisition of contractor-developed, mission-critical software." In this particular case, the quality of the contractor's product was not monitored as it would have been if the proper milestones for reviewing and auditing contractor progress were in place.

* **Lesson Learned (Starliner CFT):** **Deep insight into suppliers and subcontractors is essential; shared accountability must be consistently applied.**

  **Project Context:**  
  Derived from Starliner CFT Investigation.

  **Problem/Observation:**  
  Limited access to subcontractor data and decisions reduced NASA’s ability to identify emerging risks; shared accountability and oversight were inconsistently understood.

  **Contributing Factors:**

  + Contract structures did not guarantee access to engineering artifacts (logs, design rationales, hazard analyses).
  + Variability in supplier reporting cadence and technical forum participation.

  **Impacts:**

  + Delayed discovery of risks and slowed anomaly resolution.
  + Reduced confidence in subsystem readiness and interactions.

  **Recommended Practices (Aligned to SWE‑039/040):**

  + Define **supplier insight plans** (artifacts, cadence, forums, liaisons).
  + Require **data‑access clauses** for engineering logs, design reviews, anomalies, and RCCA artifacts.
  + Maintain **joint technical boards** with clear decision authority and escalation paths.

  **Actionable Checks:**

  + Insight plans and schedules are baselined and audited.
  + Contracts include explicit data/insight language; access is exercised.
  + Joint boards’ minutes document supplier actions and accountability.
* **Incomplete Verification & Validation (V&V)**

**Incident:**  
The project faced major V&V shortfalls, including approximately 1,000 unverified system requirements and incomplete GNC, fault protection, and FSW test coverage. Immature and incompatible testbeds further hindered simulation and closed‑loop testing.

**Lesson Learned:**

* + **Comprehensive V&V Execution:** V&V must be resourced, scheduled, and monitored with the same rigor as hardware development.
  + **Validated Testbeds:** Testbeds and simulations must be synchronized early with vendor tools to ensure accurate system‑level testing.

**Implication:**  
Insufficient V&V undermines mission confidence and may conceal system defects until it is too late to correct them within the launch window.

* **Insufficient Staffing in Software, GNC, and Systems Engineering**

**Incident:**  
Psyche suffered from persistent understaffing in key areas such as flight software, GNC, systems engineering, and V&V. Many roles were filled with inexperienced personnel, with excessive reliance on stretch assignments and limited mentoring.

**Lesson Learned:**

* + **Adequate Expertise:** Complex missions require experienced staff in critical roles (e.g., Project Chief Engineer, GNC CogE, Fault Protection Lead).
  + **Sustainable Staffing Models:** Workforce planning must account for burnout, skill mix, mentoring, and retention of highly specialized talent.

**Implication:**  
Understaffing reduces software quality, increases risk of technical debt, delays development, and undermines mission execution.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Embed FSW team members into custom hardware development efforts](https://software.gsfc.nasa.gov/lesson-details/74/). **Lesson Number 74**: The recommendation states: "Embed FSW team members into custom hardware development efforts."
* [Ensure that the impacts of design decisions are clearly communicated](https://software.gsfc.nasa.gov/lesson-details/109/). **Lesson Number 109**: The recommendation states: "When Flight Software provides inputs to design decisions, ensure that the impacts of design decisions are clearly communicated."
* [Early engineering development on an instrument needs support from the scientific community](https://software.gsfc.nasa.gov/lesson-details/115/). **Lesson Number 115**: The recommendation states: "Accompany early engineering development on an instrument with support from the scientific community."
* [When using OTS software, consult early on with people familiar with the software](https://software.gsfc.nasa.gov/lesson-details/281/). **Lesson Number 281**: The recommendation states: "When using off-the-shelf (OTS) software, discuss design decisions related to this software with SMEs (and if possible with the OTS developers) early on, to catch any design problems as soon as possible."
* [Perform software prototyping early to increase confidence in selections](https://software.gsfc.nasa.gov/lesson-details/315/). **Lesson Number 315**: The recommendation states: "Identify and pursue early prototyping efforts in order to understand the design space and options, better prior to closing trade studies."
* [During initial design, explore available ground systems tools from other NASA Centers to include in design trade studies](https://software.gsfc.nasa.gov/lesson-details/317/). **Lesson Number 317**: The recommendation states: "Seek demos from other NASA centers during ground software initial trade studies, in-person when possible."
* [Integrated Simulator Development](https://software.gsfc.nasa.gov/lesson-details/320/). **Lesson Number 320**: The recommendation states: "Organize software simulators as an integrated effort supporting Flight Software, I&T, Operations, and any subsystems which require simulators for development.  Hire a Simulators lead with sufficient time to prepare for PDR. Ensure open communication between all teams who are developing simulation capabilities."

# 7. Software Assurance

**SWE-039 - Software Supplier Insight**

3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:

1. 1. Monitor product integration.
   2. Review the verification activities to ensure adequacy.
   3. Review trade studies and source data.
   4. Audit the software development processes and practices.
   5. Participate in software reviews and technical interchange meetings.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that software developer(s) periodically report status and provide insight to the project manager.

2. Monitor product integration.

3. Analyze the verification activities to ensure adequacy.

4. Assess trade studies, source data, software reviews, and technical interchange meetings.

5. Perform audits on software development processes and practices at least once every two years.

6. Develop and provide status reports.

7. Develop and maintain a list of all software assurance review discrepancies, risks, issues, findings, and concerns.

8. Confirm that the project manager provides responses to software assurance and software safety submitted issues, findings, and risks and that the project manager tracks software assurance and software safety issues, findings, and risks to closure.

## 7.2 Software Assurance Products

Software Assurance **products** are deliverables created by SA personnel to monitor, assess, and document compliance with the objectives of this requirement. Below are the key SA products:

### 7.2.1 Reporting Oversight Products

#### 7.2.1.1 SA Review of Developer Status Reports

* **Description**: Records documenting SA evaluation of periodic developer status reports to confirm completeness, accuracy, and insight provided.
* **Contents**:
  + SA findings regarding developer reporting gaps.
  + Recommendations to improve reporting completeness.
  + Status of deliverables, milestones, and risks flagged by SA based on developer reports.
* **Purpose**: Ensures developer reports are adequately meeting project expectations and providing actionable insights.

#### 7.2.1.2 SA Status Reports

* **Description**: Periodic reports compiled by SA personnel summarizing oversight activities, findings, discrepancies, risks, and progress in software development.
* **Contents**:
  + Dashboard summary (status of project, risks, findings).
  + Key contributions (audits, reviews, analyses).
  + Planned SA tasks and milestones.
  + Issue tracking updates (including discrepancies, risks, concerns).
  + Software Assurance metrics results (e.g., compliance rates, resolution rates, etc.).
* **Purpose**: Provides project management, engineering teams, and other stakeholders with periodic insight into SA activities and project health.

### 7.2.2 Verification and Validation (V&V) Products

#### 7.2.2.1 Verification Activity Assessment Report

* **Description**: Report evaluating the adequacy and completeness of verification tasks conducted by software developers.
* **Contents**:
  + Results from SA observations of verification methods (e.g., testing, inspections, analysis).
  + Metrics related to coverage and adequacy of verification.
  + Identified gaps (e.g., missing test cases, inadequate traceability) and recommendations for corrective actions.
* **Purpose**: Confirms that verification activities meet the project's requirements and demonstrate product quality.

#### 7.2.2.2 Test Observation Reports

* **Description**: Records of SA witnessing or reviewing test execution, including adequacy of test plans, test cases, and results.
* **Contents**:
  + SA conclusions on the sufficiency of test coverage.
  + Observed discrepancies in testing or validation processes.
  + Recommendations for improvement.
* **Purpose**: Provides objective evidence of SA participation in verification activities.

### 7.2.3 Product Integration Monitoring Products

#### 7.2.3.1 Integration Observations Report

* **Description**: Report documenting SA monitoring of product integration efforts, including the resolution of any integration-related risks or issues.
* **Contents**:
  + Integration schedule and milestones assessed.
  + SA observations of integration testing procedures and results.
  + Risks or issues identified during integration (e.g., interface mismatches, failed test cases).
  + Corrective actions recommended by SA.
* **Purpose**: Ensures the integration process is progressing as planned and producing cohesive software components.

#### 7.2.3.2 Configuration Assessment Report

* **Description**: A report by SA personnel assessing the integrity of configuration management during product integration (e.g., version tracking, baseline updates).
* **Contents**:
  + Assessment of delivered software integrity.
  + Issues related to configuration management flagged during integration.
* **Purpose**: Confirms that product integration follows baseline management and configuration standards.

### 7.2.4 Trade Studies and Source Data Review Products

#### 7.2.4.1 Trade Study Assessment Report

* **Description**: Analysis performed by SA to evaluate software developer trade studies for completeness, rationale, and impacts on safety-criticality.
* **Contents**:
  + SA assessment of decision criteria used in the studies.
  + Sources of data used (e.g., assumptions, consistency, accuracy).
  + Identified risks or issues (e.g., safety reclassification, poor decisions impacting design).
* **Purpose**: Confirms that trade studies meet project requirements and align with software lifecycle objectives.

#### 7.2.4.2 Criticality Reclassification Document

* **Description**: Documented evidence of software criticality classification changes resulting from source data reviews or trade studies.
* **Contents**:
  + Rationale for reclassification, including SA findings related to safety impacts.
  + SA review summary ensuring compliance with NASA-7150.2 and related standards.
* **Purpose**: Tracks changes to safety-critical software designation and implications.

### 7.2.5 Audit Products

#### 7.2.5.1 Software Development Process Audit Report

* **Description**: A formal report documenting findings and non-conformances identified during audits of software development processes and practices.
* **Contents**:
  + Audit scope and areas assessed (e.g., configuration management, risk management, design processes).
  + Non-conformance findings and root causes.
  + Recommended corrective actions and timelines for resolution.
* **Purpose**: Helps ensure adherence to project processes and industry standards.

#### 7.2.5.2 Audit Findings Tracking Log

* **Description**: A centralized log for tracking all findings, discrepancies, and risks identified during SA audits.
* **Contents**:
  + Finding descriptions, severity levels, and timestamps.
  + Resolution status (e.g., open, in progress, resolved).
  + Linkage to review item discrepancies (RIDs) or corrective actions.
* **Purpose**: Tracks audit results and maintains oversight of corrective action resolution.

### 7.2.6 Review and Meeting Participation Products

#### 7.2.6.1 Review Participation Summary

* **Description**: Documentation summarizing SA involvement, findings, and recommendations from participation in major reviews (e.g., **PDR**, **CDR**, **TRR**, **SAR**) and technical interchange meetings.
* **Contents**:
  + Review agenda and objectives.
  + SA feedback, discrepancies, and risks flagged.
  + Review Item Discrepancies (RIDs) submitted by SA based on the review process.
* **Purpose**: Provides evidence of SA contributions during major lifecycle reviews and meetings.

#### 7.2.6.2 Meeting Minutes and SA Feedback

* **Description**: Notes taken by SA personnel during technical interchange meetings (TIMs), including observations and insights provided by SA.
* **Contents**:
  + Summary of decisions discussed.
  + SA feedback on risks related to design, verification, and integration.
  + Action items assigned to developers or project teams to address concerns.
* **Purpose**: Documents SA engagement and proactive support during TIMs to optimize software development and testing.

## 7.3 Metrics:

Software Assurance (SA) metrics for this requirement are designed to measure the effectiveness, progress, compliance, and quality of processes and deliverables across these specified activities. These metrics help track the adequacy of developer reporting, SA participation, and the completeness of oversight tasks.

Below are the relevant key metrics for each aspect outlined in this requirement:

### 7.3.1 Metrics for Periodic Developer Reporting

#### 7.3.1.1 Reporting Frequency Compliance

* **Definition**: Measures how consistently software developers deliver periodic status reports on time.
* **Formula**:  
  [ \text{Reporting Frequency Compliance} = \left( \frac{\text{Reports Delivered on Time}}{\text{Total Reports Due}} \right) \times 100 ]
* **Purpose**: Ensures developers are meeting deadlines for periodic status reports. Non-compliance indicates possible gaps in communication.

#### 7.3.1.2 Reporting Completeness Rate

* **Definition**: Tracks the percentage of reports that meet project completeness criteria (e.g., scope, detail, insight).
* **Formula**:  
  [ \text{Reporting Completeness} = \left( \frac{\text{Reports Meeting Criteria}}{\text{Total Reports Submitted}} \right) \times 100 ]
* **Purpose**: Ensures that periodic reports provide actionable data and insight into development and testing activities.

#### 7.3.1.3 Insights Provided per Reporting Cycle

* **Definition**: Measures the average number of issues, risks, or decisions flagged by developers during reporting periods.
* **Formula**:  
  [ \text{Insights per Cycle} = \frac{\text{Developer Insights Flagged}}{\text{Total Reporting Cycles}} ]
* **Purpose**: Assesses developer engagement in identifying and reporting meaningful progress, risks, or issues.

### 7.3.2 Metrics for Product Integration Monitoring

#### 7.3.2.1 Integration Issue Rate

* **Definition**: The percentage of software product integration tasks that result in issues (e.g., defects, failures, interface mismatches).
* **Formula**:  
  [ \text{Integration Issue Rate} = \left( \frac{\text{Integration Issues}}{\text{Total Integration Tasks}} \right) \times 100 ]
* **Purpose**: Tracks the quality of integration processes and helps identify recurring problems.

#### 7.3.2.2 Integration Status Accuracy

* **Definition**: Percentage of integration updates reported by developers that align with independently observed task statuses.
* **Formula**:  
  [ \text{Integration Status Accuracy} = \left( \frac{\text{Verified Integration Updates}}{\text{Total Integration Updates Reported}} \right) \times 100 ]
* **Purpose**: Ensures developers’ integration reporting matches project reality.

#### 7.3.2.3 Time to Resolve Integration Issues

* **Definition**: Measures the average time taken to address and resolve integration issues.
* **Formula**:  
  [ \text{Time to Resolve} = \frac{\text{Total Time to Resolve All Issues}}{\text{Number of Integration Issues}} ]
* **Purpose**: Monitors how efficiently identified integration problems are resolved.

### 7.3.3 Metrics for Verification Activities

#### 7.3.3.1 Verification Coverage

* **Definition**: Measures the percentage of requirements verified through tests, inspections, or analysis.
* **Formula**:  
  [ \text{Verification Coverage} = \left( \frac{\text{Requirements Verified}}{\text{Total Requirements}} \right) \times 100 ]
* **Purpose**: Helps confirm whether verification activities adequately cover all functional and non-functional requirements.

#### 7.3.3.2 Discrepancy Resolution Rate

* **Definition**: Tracks the percentage of verification discrepancies/logs resolved.
* **Formula**:  
  [ \text{Discrepancy Resolution Rate} = \left( \frac{\text{Resolved Logs}}{\text{Total Discrepancy Logs}} \right) \times 100 ]
* **Purpose**: Monitors the effectiveness of resolving issues identified during verification activities.

#### 7.3.3.3 Verification Activity Alignment

* **Definition**: Percentage of verification tasks conducted on schedule.
* **Formula**:  
  [ \text{Activity Alignment} = \left( \frac{\text{On-Time Verification Tasks}}{\text{Total Verification Tasks}} \right) \times 100 ]
* **Purpose**: Tracks the timeliness of verification activities and identifies delays that may affect milestones.

### 7.3.4 Metrics for Trade Studies and Source Data Reviews

#### 7.3.4.1 Source Data Completeness Rate

* **Definition**: The percentage of trade studies and source data reviews considered complete (e.g., documented rationale, alternatives).
* **Formula**:  
  [ \text{Data Completeness Rate} = \left( \frac{\text{Complete Trade Studies}}{\text{Total Trade Studies Reviewed}} \right) \times 100 ]
* **Purpose**: Tracks the quality and thoroughness of trade studies and source data.

#### 7.3.4.2 Safety-Criticality Reclassification Rate

* **Definition**: Measures the frequency of decisions that result in changes to the software safety-criticality designation.
* **Formula**:  
  [ \text{Reclassification Rate} = \left( \frac{\text{Criticality Reclassification Events}}{\text{Total Source Data Reviews}} \right) \times 100 ]
* **Purpose**: Monitors how often trade studies and data reviews affect safety-critical software designation.

### 7.3.5 Metrics for Audit Activities

#### 7.3.5.1 Audit Coverage

* **Definition**: The percentage of planned audit tasks completed.
* **Formula**:  
  [ \text{Audit Coverage} = \left( \frac{\text{Audits Completed}}{\text{Audits Planned}} \right) \times 100 ]
* **Purpose**: Ensures that audit schedules are adhered to and that all planned areas are evaluated.

#### 7.3.5.2 Audit Finding Resolution Rate

* **Definition**: The percentage of identified audit findings (discrepancies, risks, issues) that are resolved within a defined period.
* **Formula**:  
  [ \text{Finding Resolution Rate} = \left( \frac{\text{Resolved Findings}}{\text{Total Audit Findings}} \right) \times 100 ]
* **Purpose**: Monitors the project's responsiveness and effectiveness in addressing audit findings.

### 7.3.6 Metrics for Review and Meeting Participation

#### 7.3.6.1 SA Meeting Participation Rate

* **Definition**: Measures the percentage of major software reviews or technical meetings attended by SA personnel.
* **Formula**:  
  [ \text{Participation Rate} = \left( \frac{\text{Meetings Attended by SA}}{\text{Total Planned Meetings}} \right) \times 100 ]
* **Purpose**: Ensures that SA personnel actively participate in all required major software reviews and TIMs.

#### 7.3.6.2 Review Discrepancy Rate

* **Definition**: Percentage of discrepancies or risks identified by SA during reviews.
* **Formula**:  
  [ \text{Review Discrepancy Rate} = \left( \frac{\text{Discrepancies Identified}}{\text{Total Items/Criteria Reviewed}} \right) \times 100 ]
* **Purpose**: Monitors SA effectiveness in identifying issues during major reviews.

#### 7.3.6.3 SA Input Closure Rate

* **Definition**: Percentage of SA-raised review items that are closed (e.g., addressed, resolved) by the project.
* **Formula**:  
  [ \text{Input Closure Rate} = \left( \frac{\text{SA Review Items Closed}}{\text{SA Review Items Submitted}} \right) \times 100 ]
* **Purpose**: Tracks the responsiveness of project teams to SA feedback.

### 7.3.7 Overall Project Metrics

#### 7.3.7.1 Risk Tracking and Closure Rate

* **Definition**: Tracks the percentage of SA-identified risks that are mitigated and closed during the project lifecycle.
* **Formula**:  
  [ \text{Risk Closure Rate} = \left( \frac{\text{Closed Risks}}{\text{Total Risks Identified}} \right) \times 100 ]
* **Purpose**: Ensures timely resolution of risks to prevent adverse impacts on milestones.

#### 7.3.7.2 SA Metrics Utilization

* **Definition**: Percentage of required SA metrics that are collected and used for reporting.
* **Formula**:  
  [ \text{Metrics Utilization Rate} = \left( \frac{\text{SA Metrics Collected and Used}}{\text{SA Metrics Defined in the SA Plan}} \right) \times 100 ]
* **Purpose**: Ensures that SA provides data-driven oversight and meets reporting requirements.

### Summary of Metrics by Key Aspect

| **Aspect of Requirement** | **Metrics** |
| --- | --- |
| Periodic Reporting | Reporting Frequency Compliance, Reporting Completeness Rate, Insights per Cycle |
| Product Integration Monitoring | Integration Issue Rate, Integration Status Accuracy, Time to Resolve Integration Issues |
| Verification Activities | Verification Coverage, Discrepancy Resolution Rate, Activity Alignment |
| Trade Studies and Source Data Reviews | Source Data Completeness, Safety-Criticality Reclassification Rate |
| Audit Activities | Audit Coverage, Audit Finding Resolution Rate |
| Reviews and Meetings | SA Meeting Participation Rate, Review Discrepancy Rate, Input Closure Rate |
| Overall Project Oversight | Risk Tracking and Closure Rate, SA Metrics Utilization |

 These metrics provide Software Assurance personnel with measurable indicators to evaluate whether the software development, reporting, process auditing, and meeting participation requirements of this requirement are being successfully implemented and maintained throughout the project lifecycle.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

This requirement tasks the project manager with ensuring that software developers periodically report status and provide insight into their software development and test activities. This includes monitoring product integration, reviewing verification activities, assessing trade studies and source data, auditing development processes, and participating in reviews/technical meetings. Software Assurance (SA) personnel play a pivotal role in facilitating, participating in, and overseeing these reporting and insight activities.

The implementation of this improved Software Assurance guidance will:

1. 1. Ensure the project manager and stakeholders have robust and reliable insights into software progress, risks, and product quality.
   2. Provide continuous validation and monitoring of processes, trade studies, integration activities, and verification tasks.
   3. Promote early identification of risks, discrepancies, or non-conformance issues to maintain project momentum and software quality.

Below is an improved and comprehensive Software Assurance guidance to reflect best practices and refined processes for meeting the requirements.

### 7.4.1 Guidance Goals

The SA activities aim to:

1. Enhance oversight and assess the status of development and verification activities.
2. Independently monitor risks, concerns, and discrepancies, especially for safety-critical software.
3. Provide timely feedback, detailed reports, and proactive risk management to the project.
4. Promote continuous improvement through audits, reviews, and engagement in decision-making.

#### 7.4.1.1 Ensure Periodic Reporting by Software Developers

* **Activity**:
  + Confirm that the software developer(s):
    - Periodically report progress against planned tasks.
    - Provide visibility into development and test activities through scheduled reports, technical meetings, or milestone reviews.
  + Ensure that software developer reports and documentation address:
    - Product integration updates.
    - Verification results and test status (e.g., planned vs. executed).
    - Status of trade studies and source data evaluations.
    - Changes to software safety-criticality designation and rationale.
    - Any risks, problems, or roadblocks impacting development progress.
* **SA Responsibility**:
  + Evaluate the completeness, clarity, and consistency of developer reports.
  + Independently verify the reported data via reviews, spot checks, and audits.
  + Request additional information or clarifications if gaps are identified.

#### 7.4.1.2 Monitor Product Integration

* **Activity**:
  + Observe integration activities to confirm software components are successfully integrated into the overall system/product as planned.
  + Identify risks, discrepancies, or defects related to:
    - Interfaces between software components.
    - External integrations with hardware/system components.
  + Assess the developer’s use of configuration management tools to ensure proper tracking of integrated products and versions.
* **SA Responsibility**:
  + Maintain oversight via direct observation, audits, or spot checks to ensure:
    - Integration schedules are met.
    - Integration quality and defect tracking.
    - Integration testing coverage.
  + Document observations and report any findings to the project manager.

#### 7.4.1.3 Analyze Verification Activities to Ensure Adequacy

* **Activity**:
  + Independently evaluate the adequacy and completeness of verification tasks, including:
    - Conformance to requirements.
    - Coverage of test cases and test environments.
    - Effectiveness of verification techniques (e.g., static analysis, dynamic testing).
  + Review test results to confirm functionality, performance, and safety requirements are met.
  + Ensure regression tests are conducted for updated software components.
* **SA Responsibility**:
  + Spot-check verification artifacts such as test plans, procedures, logs, and results for accuracy and completeness.
  + Identify gaps in verification coverage (e.g., missing test cases or overlooked edge cases).
  + Report issues, risks, or discrepancies to both the project manager and engineering teams.

#### 7.4.1.4 Assess Trade Studies and Source Data

* **Activity**:
  + Review the trade studies and source data to check:
    - The rationale behind software architectural or design decisions.
    - Whether the results of trade studies align with project requirements (e.g., cost, performance, safety).
    - Source data for potential inaccuracies, assumptions, or biases that could impact the software lifecycle.
  + Monitor decisions that might alter the software criticality classification and engage SA review for such scenarios.
* **SA Responsibility**:
  + Assess whether trade studies:
    - Address safety-criticality concerns appropriately.
    - Document clear decision criteria and alternatives.
  + Flag risks or deficiencies, such as unverified input data or overlooked options.

#### 7.4.1.5 Monitor and Participate in Software Reviews and Technical Interchange Meetings

* **Activity**:
  + Actively participate in:
    - Major software lifecycle reviews (e.g., **PDR**, **CDR**, **TRR**, **SAR**).
    - Regular technical interchange meetings (TIMs) as invited or available.
    - Ensure SA personnel review analysis, present feedback, and contribute findings in reviews.
  + Document discrepancies, risks, issues, and recommendations using the official report process (e.g., RIDs - Review Item Discrepancies).
* **SA Responsibility**:
  + Write detailed reports for each major review and TIM, including:
    - Observations, SA findings, flagged discrepancies, and potential concerns.
  + Provide recommendations to the project manager and engineering team for resolution.
  + Advocate for early closure of critical findings before subsequent reviews.

#### 7.4.1.6 Develop and Provide SA Status Reports

* **Activity**:
  + Prepare periodic SA status reports for delivery to the project manager, engineering team, and other stakeholders.
  + Include the following in SA status reports:
    - Dashboard summary (e.g., progress, schedule risks, compliance status).
    - Key accomplishments (e.g., completed audits, analyses, reviews).
    - Planned SA tasks for the next reporting period.
    - Risks, issues, obstacles/watch items flagged by SA during the reporter's period.
    - Final metrics and trends reflecting SA performance.
* **SA Responsibility**:
  + Use the optional content guidelines from NASA’s SA Handbook and tailor reports to stakeholder needs.
  + Track historical trends in metrics to inform future improvement actions.

#### 7.4.1.7 Develop and Maintain a List of Review Discrepancies, Issues, and Risks

* **Activity**:
  + Maintain a centralized tracking log that records:
    - All discrepancies, non-conformances, open issues, and risks identified during reviews, audits, or observations.
    - Efforts and actions needed for closure.
  + Use the issue-tracking log to track:
    - Critical risks associated with safety-critical software.
    - Risk resolution progress over time.
* **SA Responsibility**:
  + Share tracking data with the project manager regularly and ensure critical issues are escalated when necessary.
  + Report closure progress at major milestone events or reviews.

#### 7.4.1.8 Perform Audits on Software Development Processes and Practices

* **Activity**:
  + Conduct audits at least once every two years or more frequently based on project needs.
  + Audit software engineering process areas such as:
    - Change management processes.
    - Unit testing processes.
    - Configuration management and delivery processes.
    - Physical and functional configuration audits.
  + Ensure audits are scheduled strategically to provide the most benefit (e.g., auditing planning processes during early lifecycle phases).
* **SA Responsibility**:
  + Document audit findings, including non-conformances, observations, and recommendations.
  + Track audit outcomes and critical risks to closure, communicating findings in milestone reviews or immediately if urgent.

### 7.4.2 Audit Planning and Execution

#### Types of audits SA personnel should consider:

1. **Milestone Progress Audits**:
   * Check current project progress against milestones.
2. **Product Audits**:
   * Evaluate critical documentation, deliverables, or outcomes (e.g., development plans, test results).
3. **Process Audits**:
   * Confirm adherence to project processes and assess their effectiveness.
4. **Configuration Audits**:
   * Examine physical or functional configurations and ensure baselines are correct.
5. **Compliance Audits**:
   * Evaluate project compliance to NPR 7150.2 [083](#_tabs-<p></p>) , Center requirements, and NASA-STD-8739.8 [278](#_tabs-<p></p>)  standards.

### 7.4.3 Critical Guidelines

1. **Risk Reporting**:
   * Highlight critical risks immediately rather than waiting for scheduled reports.
2. **Frequency of SA Activities**:
   * Engage SA personnel consistently in reviews, audits, and developer reporting cycles to maintain oversight and provide proactive insights.
3. **Tailored Reporting**:
   * Adapt status reports and audit schedules to fit project phase, criticality, and lifecycle needs to maximize effectiveness.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)        * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence is concrete and documented artifacts that demonstrate SA activities were performed as required, and compliance was achieved.

## 8.1 Software Assurance Goals

1. Confirm adequate reporting by developers to provide insight into critical activities (development, testing, integration).
2. Track risks/issues across major processes (verification, integration, audits, reviews).
3. Provide documentation of SA participation in reviews and decision-making to ensure compliance and prevent safety-critical failures.
4. Record observations and flag discrepancies systematically to resolve issues and improve project outcomes.

By maintaining well-defined **products** and collecting **objective evidence** aligned with this requirement, Software Assurance personnel can ensure lifecycle oversight while providing actionable insights to the project manager and engineering teams.

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

#### **Key Objective Evidence Artifacts**

| **Aspect** | **Objective Evidence** | **Purpose** |
| --- | --- | --- |
| **Periodic Reporting** | Developer status reports, SA review reports, reporting adequacy checklists. | Ensure developers are reporting consistently and providing adequate insight. |
| **Product Integration Monitoring** | Integration test logs, SA observation reports, configuration management records. | Verify successful integration and highlight risks/issues. |
| **Verification Activities** | Test plans and results, validation reports, discrepancy resolution logs. | Confirm verification activities meet adequacy criteria. |
| **Trade Studies and Data** | Trade study reports, SA assessment of source data, criticality classification updates. | Ensure decisions are based on documented, accurate rationale and impacts are reviewed. |
| **Audits** | Audit reports, findings tracking logs, corrective action reports. | Validate adherence to processes and actions taken to resolve discrepancies. |
| **Reviews and TIM Participation** | Meeting minutes, SA findings and recommendations, RIDs submitted during reviews. | Provide evidence of SA participation and feedback at major reviews and TIMs. |
