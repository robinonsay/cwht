# SWE-152 - Review Requirements Mapping Matrices

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695508. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices

SWE-152 - Review Requirements Mapping Matrices

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695508)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695508&showCommentArea=true&showComments=true#addcomment)

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

2.1.1.3 The NASA OCE shall periodically review the project requirements mapping matrices.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-152 History

SWE-152 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 2.1.1.3 The NASA Office of the Chief Engineer (OCE) shall periodically review project compliance matrices. |
| Difference between B and C | Removed "Office of the Chief Engineer" and just left the acronym;  Changed "compliance" to "requirements mapping" matrix. |
| C | 2.1.1.3 The NASA OCE shall periodically review the project requirements mapping matrices. |
| Difference between C and D | No change |
| D | 2.1.1.3 The NASA OCE shall periodically review the project requirements mapping matrices. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The NASA OCE assesses project compliance matrices for a variety of reasons including the identification of patterns and trends that indicate areas of concern or potential need for requirements revision.  This requirement also helps address the **NPD 7120.4** policy for the NASA Chief Engineer:

**NASA Engineering and Program/Project Management Policy - NPD 7120.4E**

5.b.12 - Maintain periodic oversight of compliance with the Office of the Chief Engineer's policy, procedural requirements, and standards throughout the Agency and its contractor community.[257](#_tabs-<p></p>)

The rationale for requiring the NASA Office of the Chief Engineer (OCE) to periodically review the project requirements mapping matrices is to ensure the integrity, alignment, and continuous improvement of project outcomes. The following points provide a detailed explanation:

1. **Requirement Verification and Validation**: By periodically reviewing the mapping matrices, the OCE ensures that all project requirements are properly traced and aligned to higher-level mission objectives, safety standards, and performance expectations. This process validates that requirements are comprehensive and feasible, and helps identify any gaps or inconsistencies that could compromise the project’s success.
2. **Risk Management**: The mapping matrices review allows the OCE to identify and mitigate risks associated with inadequate, misaligned, or obsolete requirements. By detecting potential issues early, the OCE can help prevent cascading failures during later project phases, ultimately minimizing schedule delays, cost overruns, or mission failures.
3. **Compliance with Standards and Policies**: The OCE’s periodic review ensures adherence to NASA’s established engineering, safety, and programmatic standards. This oversight prevents deviation from agency-wide best practices and ensures that projects comply with updated policies, regulations, and guidelines.
4. **Adaptation to Change**: As NASA projects often span years, external factors, such as evolving technology, new mission priorities, or unexpected operational constraints, can affect requirements. Regular reviews allow the OCE to monitor and ensure the mapping matrices are updated appropriately in response to these changes.
5. **Stakeholder Alignment**: Periodic reviews help facilitate alignment among project stakeholders. The OCE ensures that the requirements are not only technically aligned but also clearly communicated, understood, and supported by all relevant parties including engineering teams, contractors, and mission managers.
6. **Lessons Learned and Continuous Improvement**: By consistently revisiting the requirements mapping matrices, the OCE can incorporate lessons learned from prior projects to improve the process of requirements development and traceability over time. This fosters a culture of continuous improvement and innovation within the organization.
7. **Accountability and Oversight**: As the central authority responsible for maintaining the quality of NASA’s engineering practices, the OCE’s periodic involvement promotes accountability. It reinforces the importance of rigorous requirements management as a core part of NASA’s mission assurance philosophy.

In summary, the periodic review of project requirements mapping matrices by the NASA OCE provides critical oversight, ensures alignment with mission goals and organizational standards, and enables the adaptability, accountability, and risk awareness necessary for the successful execution of complex aerospace projects.

# 3. Guidance

Projects maintain and record **NPR 7150.2** [083](#_tabs-<p></p>) compliance matrices for the life of the software project (see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)). These matrices contain all requirements, waivers, and deviations necessary to complete the software development life cycle.  See also Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) and tab 4 of Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) (Software Assurance Requirements Mapping Matrix.)

Projects provide approved compliance matrices (see [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations)) to the NASA OCE, upon request, to help address **NPD 7120.4** policy for managers and engineers to:

**NASA Engineering and Program/Project Management Policy - NPD 7120.4E**

5.j.8 - "Support and provide information for assessments of Centers' and contractors' capabilities and compliance with engineering and program/project management requirements and standards.”[257](#_tabs-<p></p>)

Projects also have compliance matrices available for review during OCE surveys and the Office of Safety and Mission Assurance (OSMA) Quality Audit, Assessment and Review (QAAR) audit. See also [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements).

Additional data calls requiring compliance matrix data may come from the NASA Software Working Group.

The NASA OCE reviews these compliance matrices looking for patterns and trends in waivers and deviations or tailoring of software engineering requirements.  Such patterns and trends may indicate where projects or particular Centers need assistance to meet specific requirements.  Such patterns may also indicate areas to be addressed in the next update of software engineering, software safety, or software assurance requirements to better clarify requirement intent, purpose, or means of fulfillment. See also [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) and [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements).

To ensure the successful implementation of the requirement that "The NASA OCE (Office of the Chief Engineer) shall periodically review the project requirements mapping matrices," it is essential to provide actionable and practical software engineering guidance. Proper execution will contribute to mission success, reduce risks, and ensure alignment with organizational priorities. Below is a detailed set of best practices in software engineering tailored to this requirement:

1. **Adopt Rigorous Requirements Traceability Practices**
   * **Use Requirements Management Tools**: Employ specialized tools such as IBM DOORS, Jama Connect, or Jira with traceability plugins to create and maintain the requirements mapping matrices. These tools can track relationships between high-level mission objectives, system requirements, software requirements, and test plans.
   * **Establish Bidirectional Traceability**: Ensure requirements can be traced both forward (to design, implementation, and testing) and backward (to their sources and mission objectives). This makes it easier for the OCE to verify completeness and alignment during the review.
   * **Integrate Version Control**: Tie the mapping matrices to a version-controlled repository to track changes over time and ensure that the reviewed artifacts reflect the most up-to-date project requirements.
2. **Employ an Effective Review Schedule and Process**
   * **Define a Review Cadence**: Schedule reviews at key project milestones (e.g., Preliminary Design Review [PDR], Critical Design Review [CDR], etc.) or periodically (e.g., quarterly or semi-annually). Adjust the frequency based on project size, complexity, and risk.
   * **Build Review Checklists**: Provide the OCE with comprehensive checklists to ensure consistency and rigor during reviews. The checklist should include:
     + Verification of alignment to mission objectives, safety standards, and software engineering policies.
     + Identification of gaps, conflicts, or changes in requirements mapping.
     + Confirmation of traceability from high-level requirements to implementation and testing.
     + See [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) and [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment).
   * **Collaborative Stakeholder Involvement**: Include software engineers, system engineers, project leads, and quality assurance teams in the review process to provide context and clarity while addressing concerns raised by the OCE.
3. **Automate Traceability Analysis and Reporting**
   * **Leverage Automation Tools**: Use automated tools to generate traceability reports that can be directly presented for OCE review. Modern tools can highlight incomplete mappings, missing links, or changes to the matrices since the last review.
   * **Implement Requirement Change Alerts**: Set up notification systems to alert the project team and OCE of any changes made to requirements, their mappings, or downstream dependencies. This ensures that the review process remains focused and efficiently manages dynamic project requirements.
4. **Ensure Baseline and Consistency of Requirements**
   * **Establish a Requirements Baseline**: Ensure that all requirements in the mapping matrices are formally baselined (approved by project leadership) before presenting them for OCE review. This avoids the introduction of unapproved or unnecessary changes during the review process.
   * **Define a Change Management Process**: Implement a clear change control process, including impact analysis, to ensure that changes to requirements are documented, justified, and correctly propagated across the mapping matrices.
5. **Adopt Agile and Iterative Approaches for Complex Systems**
   * **Facilitate Incremental Updates**: For projects using Agile or iterative development methodologies, ensure that requirements mapping matrices are updated incrementally in alignment with sprints or iterations.
   * **Define “Definition of Done” for Matrix Updates**: Establish criteria for when updates to requirements mapping are considered complete (e.g., all requirements have been traced to test cases) to maintain consistency across reviews.
6. **Provide Training and Guidance to the Project Team**
   * **Train Engineers on Traceability and Review Standards**: Educate the development team on best practices for requirements traceability and mapping matrix development to ensure that the matrices meet OCE standards prior to review.
   * **Develop Review Documentation**: Provide templates, examples, and instructions for creating and maintaining requirements mapping matrices that are clear, structured, and aligned with OCE expectations.
7. **Enable Continuous Improvement Through Metrics and Lessons Learned**
   * **Establish Metrics for Traceability Compliance**: Track and report on key metrics, such as:
     + Percentage of requirements with complete mapping.
     + Average time to resolve mapping discrepancies.
     + Number of open vs. closed requirements-related issues.
   * **Incorporate Feedback Loops**: Gather feedback from each review and incorporate lessons learned to refine the requirements mapping process for future projects. Use this feedback to enhance the quality of matrices and the review process itself.
8. **Integrate Tools for Widespread Collaboration and Accessibility**
   * **Centralize Requirements Data**: Store requirements mapping matrices in a shared repository, such as Confluence, GitLab, or a cloud-based requirements tool, that allows stakeholders (including the OCE) to access, review, and annotate the data in real time.
   * **Enable Real-Time Collaboration**: Use collaborative platforms like Miro, Jamboard, or requirements management software with real-time capabilities for discussions and reviews.
9. **Align Reviews with Risk Management**
   * **Prioritize Critical Requirements**: Encourage the OCE to focus reviews on high-risk or high-priority areas of the requirements mapping matrices, such as those impacting mission-critical software components or safety-critical functions.
   * **Align Reviews with Hazard Analyses**: Collaborate with system safety and reliability teams to ensure that requirements linked to hazard controls (e.g., redundancy, fault tolerance software) are explicitly reviewed during the OCE analysis.
10. **Foster a Culture of Accountability and Quality**
    * **Clear Ownership**: Assign clear ownership of the requirements mapping matrices to specific individuals or teams to ensure accountability and follow-through on OCE feedback.
    * **Promote Quality Assurance Participation**: Involve QA teams in periodic internal audits of the requirements mapping matrices prior to OCE reviews to proactively identify and resolve issues.

By adhering to these software engineering guidelines, project teams can effectively maintain the quality and completeness of requirements mapping matrices, streamline the review process for the OCE, and contribute to the successful delivery of NASA’s engineering projects.

See also [SWE-021 - Transition to a Higher Class](/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class), and Topic [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) when reviewing compliance related to projects changing the Class of software.

## 3.1 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements)        * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) * [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment) |

## 3.2 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Classification](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Classification) |

# 4. Small Projects

For small projects, ensuring that NASA's Office of the Chief Engineer (OCE) periodically reviews the project requirements mapping matrices requires a tailored and scalable approach. Small projects often have fewer resources, simpler requirements, and shorter schedules relative to large-scale missions, so the guidance should emphasize efficiency, simplicity, and automation while still meeting NASA’s rigorous standards. Below are recommendations designed specifically for small projects:

## 4.1 Guidance for Small Projects

1. **Simplify the Requirements Mapping Process**
   * **Use a Lightweight Tool or Platform**: Instead of robust enterprise tools like IBM DOORS or Jama Connect, consider simpler tools such as Excel, Google Sheets, or lightweight project management tools (e.g., Trello, Asana). These tools can still capture traceability but are more manageable for small projects.
     + Create columns or tabs for mapping matrices that include requirement IDs, parent requirement references, descriptions, corresponding design elements, and linked test cases.
   * **Minimalist Traceability Matrices**: Focus on the core aspects:
     + Map high-level requirements to system/software requirements.
     + Connect system/software requirements to design artifacts, code modules, and test cases.
     + Ensure traceability exists for all critical requirements impacting the project objectives.
2. **Define Clear and Simple Review Cadence**
   * **Milestone-Based Reviews**: Schedule reviews at specific project milestones, such as:
     + **Kickoff**: Initial review to ensure the mapping framework is established.
     + **Preliminary Design Review (PDR)**: Verify that requirements are aligned with the overall design.
     + **Acceptance Testing**: Final review to confirm that all mapped requirements are validated via test cases.
     + For very short projects, aim for at least **two reviews**: once at the design phase and once before testing.
   * **Frequency Based on Complexity**: If the project is highly iterative, conduct internal reviews monthly or quarterly, but keep OCE external reviews less frequent unless updates are significant.
3. **Assign Dedicated Ownership**
   * **Role Assignment**: Designate a single person—such as a project manager, systems engineer, or requirements analyst—as the owner of the traceability process. This individual will be responsible for maintaining the requirements mapping matrices, coordinating with stakeholders (including the OCE), and responding to review feedback.
   * **Leverage a Small, Cross-Functional Team**: Ensure the mapping matrices owner collaborates closely with design, implementation, and testing leads to ensure traceability and accuracy. This collaboration streamlines the process in small teams where resources are limited.
4. **Establish Lightweight Change Management**
   * **Document Changes with Low Overhead**: For small projects, avoid overly formal change control processes. Instead, use simple tools (e.g., shared spreadsheets, version-controlled documents) to track requirement changes. Include details such as:
     + What changed (e.g., new requirement, deletion, update).
     + Why it changed (e.g., stakeholder feedback, scope adjustment).
     + Impact on design and testing (e.g., modules or test cases affected).
   * **Communicate Updates Frequently**: Small teams often thrive on informal communication channels. Use regular team meetings or small project syncs to discuss requirement changes, enabling transparency before formal OCE reviews.
5. **Automate Where Possible**
   * **Generate Mapping Matrices Automatically**: If using tools like Trello, Jira, or GitHub, simplify traceability by linking tickets or issues (e.g., feature request → code module → test case). For spreadsheets, use formulas or basic scripts to ensure consistency across requirements.
   * **Enable Automatic Traceability Reporting**: For software projects, tools like GitHub, GitLab, or basic scripts can generate reports showing code-level traceability to requirements. This minimizes manual work and enables verification before OCE reviews.
6. **Prepare for OCE Reviews with Targeted Focus**
   * **Focus on Critical Requirements**: Prioritize key requirements in mapping matrices that are essential to mission success, safety, performance, and compliance with NASA standards. For small projects, the OCE is unlikely to require exhaustive documentation for less impactful requirements.
   * **Use Concise Documentation**: Develop streamlined documents for reviews. For instance:
     + Include only essential columns (e.g., requirement ID, description, design element, test case ID).
     + Provide visual summaries (e.g., charts, mapping diagrams) for easier understanding without requiring large datasets.
   * **Address High-Level Objectives**: Ensure the review connects the small project’s requirements back to agency-level objectives, mission goals, and key engineering guidelines.
7. **Track Review Feedback for Quick Action**
   * **Create a Simple Feedback Tracker**: After each OCE review, document the feedback in a shared file or a task management tool (e.g., Trello board or Excel tracker) with columns for:
     + Feedback item.
     + Responsible person.
     + Deadline for addressing.
     + Status (e.g., open, in progress, closed).
   * **Prioritize Action Items**: Focus resources on resolving feedback for high-priority or safety-critical areas first while planning less critical updates for subsequent reviews.
8. **Enable Continuous Improvement**
   * **Apply Lessons Learned From Each Review**: Use feedback from initial OCE reviews to refine the process. For example:
     + Streamline mapping matrices further to focus on areas highlighted by the OCE.
     + Improve communication formats (e.g., better presentations or documents).
   * **Build Templates for Future Use**: Develop reusable templates for requirements mapping matrices, review checklists, and process documentation. This proactive approach reduces effort for future projects.
9. **Use Agile Approaches for Dynamic Requirements**
   * **Iterative Traceability Updates**: For small projects following Agile or iterative development processes, update the matrices at the end of each sprint or iteration. This ensures traceability aligns with any requirement changes resulting from dynamic development environments.
   * **Definition of Done Includes Traceability**: Add traceability updates (e.g., linking new test cases to the relevant requirement) to the “Definition of Done” for tasks, ensuring the matrices stay current with project progress.
10. **Keep It Simple for Small Projects**  
    For smaller projects, emphasize simplicity and clarity while ensuring the rigor expected by NASA. Avoid over-complicating the process with unnecessary complexity or administrative burden. Instead:  
    * Focus on essential traceability and alignment to objectives.
    * Use collaborative tools accessible to the whole team.
    * Prepare succinct deliverables for OCE reviews.

## 4.2 Example Workflow for Small Projects

1. **Define Requirements**: Use a shared document or tool to capture and organize high-level and detailed requirements.
2. **Create the Mapping Matrix**: Develop a basic matrix in Excel or other lightweight tools to map requirements → design → test cases.
3. **Schedule a Review at Milestones**: Align OCE reviews with major project milestones like PDR or testing phases.
4. **Automate Updates as Development Progresses**: Track requirement changes in tools or through scripts.
5. **Prepare Concise Updates for Reviews**: Include only essential details in review documentation.
6. **Address Feedback Immediately**: Respond quickly to OCE review comments and refine the matrices accordingly.
7. **Learn and Improve**: Apply lessons learned to streamline future reviews.

## 4.3 Conclusion

By following this guidance, small projects can fulfill the requirement efficiently without compromising quality or overspending resources. Clear documentation, incremental updates, and collaboration ensure compliance with OCE expectations while keeping the process manageable for small teams.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

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
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

In the context of NASA projects, lessons learned related to the periodic review of **project requirements mapping matrices** by the **Office of the Chief Engineer (OCE)** can provide valuable insight into ensuring mission success and developing robust processes. NASA's [Lessons Learned Information System (LLIS)](https://llis.nasa.gov/) catalog includes lessons from past missions and projects, many of which highlight the importance of requirements traceability, reviews, and oversight. Below are some relevant lessons learned and their connection to the requirement:

### 6.1.1  Relevant NASA Lessons Learned

1. **Requirements Traceability Issues Can Lead to Program Failures**  
   **Source:** NASA LLIS, multiple projects (e.g., Constellation Program, Mars Climate Orbiter)  
   * **Lesson Description:** The absence of proper requirements traceability has been identified as a contributing factor in past mission failures. When requirements are not adequately mapped to their source and downstream development artifacts, it becomes difficult to identify gaps, inconsistencies, or misalignments. This increases the risk that stakeholder needs and mission objectives are not fully realized.
   * **Connection to the Requirement:** Regular OCE reviews of project requirements mapping matrices can ensure that proper traceability is maintained, reducing the risk of overlooked requirements or misaligned system implementation. This oversight ensures all requirements are connected to higher-level mission goals and are fully addressed in design and testing.
2. **Periodic Oversight Can Help Address Evolving Requirements**  
   **Source:** NASA's Engineering and Programmatic Best Practices
   * **Lesson Description:** Requirements often evolve during project development due to changes in scope, stakeholder input, or discoveries during testing phases. Without regular oversight, it may be difficult to reconcile these evolving requirements with the project's original objectives, leading to incomplete fulfillment of mission needs or scope creep.
   * **Connection to the Requirement:** Periodic reviews by the OCE provide a mechanism for catching and addressing evolving requirements in a systematic way. This allows the project team to update the mapping matrices to reflect current mission priorities while maintaining alignment with engineering standards and constraints.
3. **Misaligned Requirements Caused Safety and Mission Issues**  
   **Source:** Mars Polar Lander Loss Report
   * **Lesson Description:** Requirements for the Mars Polar Lander contained ambiguities, and downstream systems designs did not fully implement safety-critical requirements. A lack of sufficient oversight on requirements traceability contributed to the failure.
   * **Connection to the Requirement:** Regular checks of requirements mapping matrices by the OCE would help identify gaps or safety-critical issues early in development. By validating that all requirements are explicitly and correctly mapped to system designs and testing, the OCE can mitigate risks tied to inadequate requirements management.
4. **Insufficient Documentation and Reviews Cause Confusion During Project Execution**  
   **Source:** NASA LLIS - Apollo, Space Shuttle, and ISS Programs
   * **Lesson Description:** In several NASA programs, insufficient documentation of requirements traceability led to confusion among stakeholders, disagreements over scope, and redundant efforts to ensure compliance across subsystems. Consistent reviews could have streamlined processes and reduced misunderstandings.
   * **Connection to the Requirement:** Periodic OCE reviews of requirements mapping matrices ensure consistent documentation and facilitate alignment among stakeholders. By regularly validating traceability, the review process minimizes confusion and ensures all stakeholders are referencing the same version of the matrix.
5. **Effective Change Management is Critical to Project Success**  
   **Source:** LLIS, James Webb Space Telescope (JWST)
   * **Lesson Description:** The James Webb Space Telescope project highlighted that effective change management processes must be in place to handle evolving requirements and ensure updates are propagated across all systems and documentation. Ineffective change management for requirements led to delays and increased costs in several subsystems.
   * **Connection to the Requirement:** By periodically reviewing the project requirements mapping matrices, the OCE reinforces the importance of documenting and propagating requirement changes systematically. This oversight ensures updated requirements are reflected in designs, implementations, and test plans, reducing risks and improving overall project discipline.
6. **Integrated Requirements Reviews Enhance Cross-Team Collaboration**  
   **Source:** NASA LLIS - Systems Engineering Division Lessons
   * **Lesson Description:** Requirements reviews that include cross-functional teams improve communication, identify disconnects earlier, and align efforts toward mission goals. When requirements reviews are siloed or informal, errors in implementation persist longer and become harder to detect.
   * **Connection to the Requirement:** OCE-led periodic reviews provide an opportunity for integrated oversight across engineering, design, and testing teams. This ensures traceability is understood and implemented across teams, fostering collaboration and improving requirements ownership.
7. **Neglected Requirements Introduced Mission Risk**  
   **Source:** NASA LLIS - Lessons from the Challenger and Columbia Shuttle Disasters
   * **Lesson Description:** Systemic gaps in requirements management and oversight contributed to poor design decisions, miscommunication, and missed safety-critical requirements. Regular reviews of requirements traceability could have helped identify and address these issues before they became catastrophic.
   * **Connection to the Requirement:** Periodic requirements mapping matrix reviews ensure neglected or poorly defined requirements are identified before they can introduce significant mission risks. This is especially critical for safety-critical or high-priority requirements.
8. **Periodic Reviews Reduce Rework and Improve Efficiency**  
   **Source:** NASA LLIS - Lessons from Small Satellite Programs
   * **Lesson Description:** Small satellite programs noted that inconsistent requirements traceability often led to costly rework during later stages of development. Periodic reviews helped programs identify misalignments early, reducing schedule impacts and improving efficiency.
   * **Connection to the Requirement:** Regular OCE reviews enable early detection of errors in requirements mapping, reducing the likelihood of costly rework and delays. The periodic nature of reviews ensures issues are identified before they grow into larger problems, supporting efficient project execution.

### 6.1.2 Key Takeaways From NASA Lessons Learned

1. **Traceability is Essential:** Without complete traceability, projects risk misaligned implementation and overlooked requirements.
2. **Periodic Oversight Mitigates Risk:** Consistent reviews help address evolving requirements, avoid mission-critical gaps, and ensure alignment to project and agency goals.
3. **Collaboration Improves Results:** Regular OCE involvement fosters cross-team collaboration and ensures that requirements are well understood and appropriately implemented.
4. **Documentation and Change Control Are Vital:** Clear records of updates and mapped requirements simplify reviews, reduce confusion, and improve project discipline.

### 6.1.3 Recommendations Based on NASA’s Lessons Learned

* **Make Reviews Systematic and Timely:** Tie OCE review schedules to major milestones and evolving project needs.
* **Use Automated Tools for Traceability:** Simplify and enhance requirements traceability using tools that provide reports and alerts for missing or disconnected links.
* **Focus on Safety-Critical Requirements:** Prioritize the review of requirements that directly impact safety, mission success, and compliance with NASA standards.
* **Facilitate Communication Across Teams:** Include all relevant stakeholders and ensure alignment to avoid siloed or incomplete requirements implementation.

By applying these lessons learned, NASA projects can effectively fulfill the requirement for periodic OCE reviews of requirements mapping matrices while enhancing mission reliability, mitigating risks, and improving project efficiency.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-152 - Review Requirements Mapping Matrices**

2.1.1.3 The NASA OCE shall periodically review the project requirements mapping matrices.

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

Software Assurance's (SA) role is to ensure that all requirements included in the Requirements Mapping Matrices (RMMs) conform to **NPR 7150.2** **[083](#_tabs-<p></p>)**, are correctly tailored, fully justified for any deviations, and address risk and compliance appropriately. SA must also verify that RMMs accurately reflect the project's classification, criticality, and safety requirements throughout the project lifecycle.

This guidance focuses on how Software Assurance personnel will support, verify, and monitor the OCE’s periodic reviews of the RMMs at both the project and organizational levels.

### 7.4.2  Software Assurance Responsibilities

1. **Ensure Accuracy of the Requirements Mapping Matrix (RMM)**  
   This includes both the Software Engineering and SA RMMs. See Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) and tab 4 of Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) (Software Assurance Requirements Mapping Matrix.)  
   * **Verify Completeness and Compliance**
     + Check that all applicable requirements from **NPR 7150.2**, **NPR 7120.5** **[082](#_tabs-<p></p>)**, **NASA-STD-8739.8** **[278](#_tabs-<p></p>)**, and other applicable directives are correctly mapped to the project deliverables.
     + Confirm that requirements in the RMM are fully addressed and consistent with the Software Classification defined in Appendix D of **NPR 7150.2**.
     + To aid in these assessments, see [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) and [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment).
   * **Review Tailoring Decisions**
     + Validate whether tailoring decisions (e.g., waivers or deviations for requirements in the RMM) are clearly justified, properly documented, and formally approved by the appropriate Technical Authority (TA).
     + Ensure tailored requirements do not introduce unacceptable levels of risk to the software's reliability, functionality, or safety.
   * **Ensure Alignment with the Current Project Plan and Software State**
     + Confirm that the RMM is up to date and aligns with the evolution of the project (e.g., changes in software classification, risk re-evaluations, or changes in project scope).
2. **Support OCE Reviews of RMMs**
   * **Collaborate with the OCE**
     + Act as a partner for the OCE during these reviews by providing feedback specific to assurance-related requirements in the matrix.
     + Assist in identifying gaps or discrepancies in how assurance-related requirements are represented and implemented.
   * **Prepare Supporting Documentation**
     + Provide risk assessments, lessons learned, and historical assurance data to inform RMM reviews. Clearly indicate the impact of any potential omissions or non-compliances in the implementation of requirements.
   * **Highlight Assurance-Specific Requirements**
     + Identify assurance-heavy requirements (e.g., independent verification and validation, risk management, test coverage) that may require additional attention to ensure consistent compliance across the project lifecycle.
3. **Oversee Risk Management of Deviations in RMMs**
   * **Analyze Risks of Waivers and Deviations**
     + Evaluate risks introduced by waived or tailored requirements listed in the RMM. Ensure that all risks from deviations are:
       - Documented in the project’s risk management system.
       - Addressed with verifiable mitigation plans.
     + Confirm that risk-critical areas (e.g., safety-critical software or mission-critical subsystems) preserve sufficient rigor even when tailoring is applied.
   * **Escalate High-Risk Deviations**
     + Notify the Technical Authority (TA) and project leadership of any deviations that compromise safety, mission success, or software performance.
     + Collaborate with the OCE to recommend appropriate corrective actions or alternative approaches if review findings reveal unacceptable risk levels.
4. **Monitor RMM Traceability and Consistency**
   * **Review Traceability**
     + Ensure all requirements in the RMM have traceability to the following:
       1. **Formal Project Plans**: Verify that the RMM aligns with the Software Development/Management Plan (SDMP), Risk Management Plan, and assurance activities.
       2. **Software Lifecycle Artifacts**: Confirm traceability to design, implementation, testing, and validation outputs.
       3. **Applicable Standards**: Verify traceability to **NPR 7150.2**, **NASA-STD-8739.8**, and other software engineering and assurance standards.
   * **Check for Consistency**
     + Ensure the RMM reflects the current risk, scope, and classification of the project and is updated as necessary when requirements, classification, or tailoring evolve.
5. **Ensure Timely Updates and Follow-Up**
   * **Monitor Updates**
     + Verify that any changes resulting from RMM reviews conducted by the OCE are implemented into project plans promptly. Changes should be communicated to all relevant stakeholders, including the assurance team, engineering leads, and project management.
   * **Track Deficiencies and Corrective Actions**
     + Track deficiencies identified during OCE reviews and follow up to ensure corrective measures identified for the RMM, such as updating mappings, addressing deviations, or resolving gaps, are executed and closed.

### 7.4.3  Implementation Approach for Software Assurance

#### **Pre-Review Activities**

* Review the most recent RMM to ensure it is accurate and complete.
* Prepare a checklist of assurance-specific requirements to review during the periodic OCE reviews:
  + Requirements related to testing and verification (e.g., V&V, coverage analysis).
  + Metrics and reporting obligations (e.g., progress on defect resolution, risk metrics).
  + Safety-critical requirements (e.g., fault-tolerant behavior, hazard analysis).
  + See [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) and [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment).
* Ensure project documentation (e.g., plans, waivers, and analysis reports) is prepared and available to address concerns raised during the review.

#### **During Review Activities**

* Collaborate with the OCE to:
  + Discuss compliance with assurance-related requirements.
  + Clarify tailoring justifications, risk mitigations, and assurance methodologies used for the project.
  + Explore opportunities for improvement based on lessons learned from other projects or known industry guidance.

#### **Post-Review Activities**

* Document any findings or gaps identified during the RMM review related to software assurance activities.
* Track and verify closure of any action items or updates to the RMM that the OCE recommends.
* Advocate for relevant updates in assurance-specific plans if critical deficiencies in the RMM are identified. For example:
  + Update risk management plans if assurance gaps are noted in tailored requirements.
  + Adjust assurance strategies for future phases of the project lifecycle.
* Submit assurance-specific findings to the OCE or higher management to ensure oversight of unresolved issues.

### 7.4.4  Key Areas of Focus for Software Assurance in RMMs

1. **Safety-Critical Requirements**:
   * Verify that software requirements related to fault tolerance, safety controls, and anomaly management are robustly addressed in the RMM.
2. **Testing and V&V Standards**:
   * Ensure that testing, coverage, and independent verification requirements align with **NPR 7150.2, NASA-STD-8739.8**, and other relevant assurance standards.
3. **Classification Validation**:
   * Confirm that software classification is correct and consistent with RMM requirements, as software classification impacts the level of assurance rigor.
4. **Risk Management Integration**:
   * Check that all waived or tailored requirements appear in the project risk register with appropriate mitigating actions.

### 7.4.5  Expected Outcomes

By following this guidance on supporting the periodic OCE reviews of the RMM:

* All deviations or waivers are clearly identified, justified, and managed, minimizing risks to mission success, safety, and compliance.
* Software assurance requirements are consistently implemented across NASA Centers and projects.
* Software Assurance gains confidence that requirements mapped in the RMM directly align with **NPR 7150.2** and the project’s lifecycle.
* The RMM evolves as a reliable resource to drive compliance, maintain traceability, and reduce project risks.

### 7.4.6  Summary

Software Assurance plays a key supporting role in the OCE’s periodic reviews of RMMs by verifying compliance, ensuring alignment to requirements, monitoring risks, validating tailoring, and driving corrective actions when gaps are identified. By focusing on critical assurance areas, SA ensures that RMMs reflect the rigor and accountability required to achieve mission safety and software reliability.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements)        * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770876/PAT-052+-+Software+Assurance+Reqts+Mapping+Matrix+Assessment) * [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](/spaces/SITE/pages/198770886/PAT-057+-+Software+Engineering+Reqts+Mapping+Matrix+Assessment) |
