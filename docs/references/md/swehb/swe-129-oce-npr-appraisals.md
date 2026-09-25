# SWE-129 - OCE NPR Appraisals

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695491. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695491/SWE-129+-+OCE+NPR+Appraisals

SWE-129 - OCE NPR Appraisals

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695491/SWE-129+-+OCE+NPR+Appraisals#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695491)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695491&showCommentArea=true&showComments=true#addcomment)

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

2.1.1.4 The NASA OCE shall authorize appraisals against selected requirements in this NPR to check compliance. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-129 History

SWE-129 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 6.3.8 The NASA Headquarters' Office of the Chief Engineer shall authorize appraisals against selected requirements in this NPR (including NASA Headquarters' Office of the Chief Engineer approved subsets and alternative sets of requirements) to check compliance. |
| Difference between A and B | Removed NASA HQ subsets and alternatives sets |
| B | 2.1.1.4 The NASA OCE shall authorize appraisals against selected requirements in this NPR  to check compliance. |
| Difference between B and C | No change |
| C | 2.1.1.4 The NASA OCE shall authorize appraisals against selected requirements in this NPR to check compliance. |
| Difference between C and D | No change |
| D | 2.1.1.4 The NASA OCE shall authorize appraisals against selected requirements in this NPR to check compliance. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The Headquarters' Office of the Chief Engineer (OCE) is responsible for promoting and monitoring software engineering practices throughout the agency. It achieves this in part by administering software requirements, policies, procedures, processes, statutes, and regulations. The Headquarters' OCE uses continuing periodic oversight of compliance at the Centers and programs/projects to verify that this responsibility is being met.

NPR 7150.2 serves as the basis for compliance appraisals for software engineering. The appraisal typically occurs during an OCE survey of processes and directives and thorough examinations of a project's official records. These surveys are one of the tools used by the OCE to provide oversight, maintain internal control, and review its operations.

While SWE-129 is written from the OCE point of view, the requirement also contains an inherent Center role, i.e., participation in the OCE survey activities. A Center's support of this SWE can be assessed by considering the extent of its preparations for and involvement in these OCE surveys.

### 1. Ensures Compliance with NASA Standards and Policies

The primary rationale for requiring the NASA OCE to authorize appraisals is to ensure that NASA projects comply with the policies, standards, and requirements set forth in the NASA Procedural Requirements (NPR) document. These requirements represent NASA’s collective institutional experience, engineering best practices, and mission-critical rules. Appraisals allow the OCE to verify that these established guidelines are being followed to uphold NASA’s high standards of engineering integrity, safety, and mission success.

### 2. Reduces Risk of Noncompliance and Associated Failures

Noncompliance with requirements increases the risk of technical failures, cost overruns, schedule delays, or even loss of mission. Appraisals serve as a mechanism to:

* Identify areas where projects fall short of compliance before these issues evolve into more serious problems.
* Highlight risks stemming from noncompliance and provide opportunities to implement corrective actions proactively, reducing downstream impacts. By authorizing appraisals, the OCE reinforces the importance of early and periodic compliance checks to prevent larger issues from arising during critical development phases.

### 3. Facilitates Early Detection of Deviations

Projects inevitably face dynamic and complex challenges that may lead to deviations from the initial requirements. Appraisals help ensure that deviations are identified early and are justified, documented, and mitigated appropriately. Early identification of noncompliant practices or artifacts enables corrective actions to be taken before they propagate to later stages of the project life cycle, where fixes are more costly and difficult to implement.

### 4. Supports NASA’s Mission Assurance Processes

NASA employs mission assurance processes to systematically eliminate or reduce risks to mission success. Regular appraisals against selected NPR requirements are an integral part of these processes because they:

* Validate adherence to safety-critical requirements.
* Confirm that the project is complying with protocols related to design, testing, and deployment.
* Provide a structured approach for independent verification and validation (IV&V) activities. The OCE’s role in authorizing appraisals bolsters mission assurance by adding independent oversight at key points in the project lifecycle.

### 5. Provides an Independent Oversight Mechanism

The OCE, as an independent office within NASA’s governance structure, plays a critical role in ensuring that individual projects and programs align with NASA’s overall strategic goals and objectives. Appraisals authorized by the OCE:

* Offer an unbiased and independent check on compliance, ensuring that projects remain accountable to the required standards.
* Reinforce the “check and balance” system that ensures engineering rigor and protects against internal risks such as team bias, groupthink, or organizational blind spots.

### 6. Promotes Continuous Improvement Across NASA

Appraisals often reveal common compliance issues or areas where processes, interpretations, or training could be improved. By identifying such trends across projects, the OCE can recommend updates to NPR requirements, tools, or training programs to improve NASA’s overall engineering excellence. This fosters a culture of continuous improvement to:

* Strengthen future compliance.
* Prevent recurring issues across projects.
* Refine and tailor NASA procedural requirements to reflect evolving best practices.

### 7. Verifies Appropriate Application of Tailoring or Waivers

Projects at NASA may require tailoring or waivers of specific NPR requirements to address unique mission needs, resource constraints, or technical challenges. An authorized appraisal ensures that:

* The rationale for tailoring is justified and documented.
* Adjustments to requirements still meet NASA’s safety, quality, and mission objectives.
* The tailoring or waiver process is conducted in conformance with NPR-defined procedures. This ensures that deviations from requirements do not compromise the project’s integrity or the broader agency’s standards.

### 8. Builds Stakeholder and Public Confidence

As a publicly funded agency, NASA is held to a high standard of accountability and transparency. The NASA OCE’s responsibility to authorize appraisals demonstrates due diligence in ensuring that project teams comply with NPR requirements, fostering trust among stakeholders, including:

* NASA leadership.
* External auditors (such as the Government Accountability Office or Office of Inspector General).
* The public, whose tax dollars fund NASA’s work. Visibility into compliance-checking and corrective actions strengthens NASA’s reputation for technical excellence.

### 9. Ensures Focus on High-Risk and High-Value Areas

Not all NPR requirements may carry equal weight or be applicable to every project. By authorizing appraisals selectively, the OCE ensures that compliance efforts are focused on areas of highest risk, complexity, or importance to mission success, such as:

* Safety-critical systems.
* Systems that interface with other projects, including International Space Station modules, launch vehicles, etc.
* Software-intensive systems, where noncompliance can have cascading effects.

This risk-based focus ensures that resources are used efficiently and that compliance activities remain aligned with mission-specific priorities.

### 10. Reinforces the Discipline of Formal Requirements Verification

A critical aspect of systems engineering is formal requirements verification. Appraisals authorized by the OCE ensure that projects consistently apply verification and validation (V&V) principles when assessing compliance with selected NPR requirements. This reinforces:

* The discipline of evidence-based compliance checking.
* The systematic documentation of how requirements are satisfied, tracing compliance from policy to implementation.

### 11. Aligns Projects to Agency-Wide Performance Goals

NPR requirements are designed to ensure consistency, reliability, and efficiency across NASA’s programs and projects. OCE-authorized appraisals check that the implementation of requirements aligns with agency-wide goals such as:

* Meeting budget and schedule constraints.
* Upholding NASA’s principles of engineering quality, system reliability, and rigorous safety protocols. These appraisals help ensure that individual project priorities do not conflict with the broader strategic objectives of the agency.

### Summary of Rationale

By authorizing appraisals against selected NPR requirements to verify compliance, the NASA OCE reinforces project discipline, reduces risks to mission success, promotes agency-wide consistency, and drives continuous improvement. This requirement ensures that NASA's policies and standards are not only implemented but are also periodically and independently reviewed, giving confidence to mission stakeholders and supporting the overall excellence and accountability of NASA's projects.

# 3. Guidance

To enhance the effectiveness and practicality of the OCE compliance survey process, the following improved software engineering guidance refines the methods described. This updated approach provides improved structure, contextual application, and actionable insights to support compliance with critical requirements and to drive continuous improvement in NASA’s software engineering practices.

### 1. Purpose of the OCE Compliance Survey

The purpose of the OCE compliance survey is to:

* Verify compliance with NASA software engineering policies, requirements, and standards.
* Assess the quality, maturity, and consistency of software engineering practices across Centers and projects.
* Highlight systemic issues and identify areas for improvement.
* Recognize and encourage excellence and the adoption of best practices.
* Collect feedback from Centers to refine policies, requirements, and guidance.

The surveys are not just compliance exercises; they are significant opportunities for process improvement, cross-Center alignment, and culture building within NASA's software engineering community.

### 2. Objectives of the OCE Appraisal Process

The OCE compliance appraisal achieves several targeted goals:

1. Ensure compliance in software engineering practices with NPR 7150.2 and other relevant policies, including:
   * NPD 7120.4: NASA Engineering and Program/Project Management Policy.[257](#_tabs-<p></p>)
   * NASA-STD-8739.8:[278](#_tabs-<p></p>) Software Assurance and Software Safety Standard.
2. Evaluate programmatic and process implementation at multiple levels:
   * Center-wide frameworks and infrastructure to support software engineering processes.
   * Specific project documentation (e.g., requirements, technical baselines, test artifacts) to verify traceability and validation against policy.
3. Identify and mitigate systemic issues or gaps within the framework of NASA’s software engineering and life cycle processes.
4. Highlight successes, best practices, and innovations in software engineering efforts.
5. Provide actionable feedback to Centers and Headquarters for process refinements, supporting both efficiency and effectiveness in future activities.

### 3. Key Core Elements of the Survey

OCE compliance surveys assess critical aspects of software engineering consistent with NASA’s standards for technical rigor. These include:

1. **Unified Program and Project Life Cycle Framework**:

   * Evaluation of Center and project alignment to the life cycle implementation requirements specified in NPR 7120.5 [082](#_tabs-<p></p>), NPR 7150.2 [083](#_tabs-<p></p>), and related standards.
   * Assessing how software engineering is incorporated at each phase of the life cycle.
2. **Program and Project Review Structure**:

   * Verifying the consistent application of milestone reviews, such as Software Requirements Reviews (SRR), Preliminary Design Reviews (PDR), and Critical Design Reviews (CDR).
   * Ensuring programmatic completeness in presenting software engineering elements.
3. **Technical Authority Implementation**:

   * Reviewing the effectiveness of the software technical authority in monitoring and addressing key risks.
   * Ensuring that dissenting opinions are documented and addressed when technical authority decisions are made.
4. **Deviation/Waiver Processes**:

   * Ensuring that deviation and waiver procedures are applied and documented in compliance with NPR 7150.2 requirements.
5. **Software Engineering Management**:

   * Evaluating software development plans (SDPs), schedules, and resources to determine their adequacy for meeting deliverables.
   * Reviewing risk management strategies specific to software engineering.
6. **Systems Engineering Integration**:

   * Ensuring software engineering processes are integrated into systems engineering and interface-driven development.
7. **Lessons Learned Incorporation**:

   * Reviewing project efforts to incorporate NASA's lessons learned (from sources such as the LLIS database) into their practices.
8. **Adoption of Technical Standards**:

   * Evaluating adherence to NASA’s software and systems engineering standards to ensure robustness, safety, and reliability.

### 4. Enhanced Scope Definition for Surveys

To refine the scope of a survey:

1. **Tailor the Survey to the Software Life Cycle Stage**:

   * Align the appraisal to the current phase of the project, ensuring the survey focuses on compliance relevant to that stage, such as requirements engineering early on or verification/testing during the later stages.
   * Assess whether software design elements meet milestone-specific exit criteria.
2. **Address Center-Wide and Project-Specific Concerns**:

   * Review how well OCE requirements have been flowed down from higher-level documents to Center and project-specific procedural documentation.
   * Evaluate individualized risks and strengths within a single project while capturing trends across multiple Centers.
3. **Leverage External Data**:

   * Analyze findings from previous surveys, OSMA audits, or project-specific assessments to identify recurring issues or refined areas to investigate during the survey.

### 5. Detailed Survey Planning and Preparation

1. **Baseline Questions and Data Requests**:

   * Clearly define a baseline set of survey questions relating to the project's compliance with NPR 7150.2 software engineering requirements and system-level processes.
   * Deliver these questions to the Center's survey manager 3–4 weeks in advance, ensuring sufficient preparation time.
   * Identify critical evidence and data required, such as Software Development Plans (SDPs), risk logs, software verification plans, and test reports.
2. **Checklist Customization**:

   * Customize the appraisal's software engineering questions based on identified project or Center-specific priorities.
3. **Review of Past Surveys and Audits**:

   * Use prior findings to steer the focus of the new survey, targeting problem areas while also checking for progress on any corrective actions.

### 6. Use of Objective Evidence in Compliance Surveys

Objective evidence serves as the foundation for verifying compliance. NASA Centers and project teams should ensure:

1. **Evidence Preparedness**:

   * Software project teams should have ready access to relevant documents and artifacts, categorized by their role in demonstrating compliance with requirements. For example:
     + Requirements Traceability Matrices (RTMs).
     + Peer review logs and inspection records.
     + Verification and validation (V&V) test results.
2. **Alignment of Artifacts**:

   * Ensure that all objective evidence shows traceability from software requirements to design, code, integration, and testing.
   * Include technical basis and rationale for any waivers or deviations from standard processes.
3. **CMMI-Inspired Metrics**:

   * Borrow best practices from the Capability Maturity Model Integration (CMMI®) methodology to assess the maturity of processes and the quality of evidence provided.

Definition of Objective Evidence

Objective evidence is an unbiased, documented fact showing that an activity was confirmed or performed by the software assurance/safety person(s). The evidence for confirmation of the activity can take any number of different forms, depending on the activity in the task. Examples are:

* Observations, findings, issues, risks found by the SA/safety person and may be expressed in an audit or checklist record, email, memo or entry into a tracking system (e.g. Risk Log).
* Meeting minutes with attendance lists or SA meeting notes or assessments of the activities and recorded in the project repository.
* Status report, email or memo containing statements that confirmation has been performed with date (a checklist of confirmations could be used to record when each confirmation has been done!).
* Signatures on SA reviewed or witnessed products or activities, or
* Status report, email or memo containing a short summary of information gained by performing the activity. Some examples of using a “short summary” as objective evidence of a confirmation are:
  + To confirm that: “IV&V Program Execution exists”, the summary might be: IV&V Plan is in draft state. It is expected to be complete by (some date).
  + To confirm that: “Traceability between software requirements and hazards with SW contributions exists”, the summary might be x% of the hazards with software contributions are traced to the requirements.
* The specific products listed in the Introduction of 8.16 are also objective evidence as well as the examples listed above.

### 7. Center Feedback Incorporation

An essential part of the survey process is to gather feedback from Centers regarding:

* Suggested improvements to Agency policy, NPRs, or guidelines based on their real-world applicability.
* Lessons learned from implementing NPRs at the Center or project level.
* Challenges faced with compliance and recommendations for solutions.

This feedback loop strengthens the software engineering processes by ensuring iterative updates and refinement of NASA policies.

### 8. Collaboration Between OCE and OSMA

While the OCE compliance surveys focus on software engineering process, integration, and management, the Office of Safety and Mission Assurance (OSMA) takes a deeper dive into software assurance and software safety. These two efforts can be coordinated to:

* Avoid redundancies in audits and assessments.
* Exchange findings to provide a more complete picture of compliance across software engineering domains.

### Conclusion

The guidance for the OCE compliance survey process ensures that NASA maintains its high standards for software engineering excellence. By carefully planning, leveraging objective evidence, adapting surveys to specific projects and Center contexts, and incorporating iterative feedback, the process ensures continual improvement, compliance, and mission success. Additionally, fostering collaboration across engineering and assurance disciplines allows the Agency to identify opportunities for greater synergy and efficiency.

See also [SWE-004 - OCE Benchmarking](/spaces/SWEHBVD/pages/102695394/SWE-004+-+OCE+Benchmarking)

See also [SWE-221 - OSMA NPR Appraisals](/spaces/SWEHBVD/pages/105709899/SWE-221+-+OSMA+NPR+Appraisals).

See also [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations), [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements).

Findings resulting from the survey are generally classified as strengths, weaknesses, observations, opportunities, and non-compliances. However, the survey team has a clear and overriding obligation to identify all items of non-compliance and items that adversely affect safety or quality. These items will be included in the final report. Significant issues are brought to the immediate attention of the surveyed organization's management via the survey manager.

## 3.1 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-004 - OCE Benchmarking](/spaces/SWEHBVD/pages/102695394/SWE-004+-+OCE+Benchmarking) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-221 - OSMA NPR Appraisals](/spaces/SWEHBVD/pages/105709899/SWE-221+-+OSMA+NPR+Appraisals) |

## 3.2 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

For small projects, where resources (budget, schedule, personnel) may be limited, simplifying the implementation of OCE compliance surveys while maintaining rigor and fulfilling NASA requirements is critical. Small projects can still achieve compliance by tailoring their approaches to meet the needs of the survey efficiently. The following guidance breaks down key elements and provides actionable recommendations specifically for small projects.

## 4.1 Guidance for Small Projects

### 4.1.1. Understand the Purpose and Scope for Small Projects

* **Focus on Relevant Requirements**: For small projects, compliance surveys should focus on core software engineering requirements that directly impact the project's success, safety, and mission-critical functionality. Some NPR 7150.2 requirements may be tailored or waived with proper documentation, reducing the burden on smaller projects.
* **Clarify the Appraisal Scope Early**: Work with the OCE and the Center's survey manager to clarify exactly which requirements and deliverables will be reviewed. For small projects, this scope is often narrower and should focus on:
  + Software engineering plans and processes.
  + Compliance with any safety-critical and mission-critical requirements.
  + The use of appropriate tools and processes scaled to the project's size.

### 4.1.2. Preparing for the Survey in a Resource-Constrained Environment

1. **Tailored Documentation**
   * Use streamlined documentation formats to provide the OCE with only what is necessary:
   * **Software Development Plan (SDP)**: Keep the SDP concise, focusing on development workflows, resource allocation, and tools (e.g., ticketing systems, CI/CD pipelines).
   * **Requirements Traceability Matrix (RTM)**: For small projects, an Excel-based RTM or one embedded in project management software (e.g., Jira) is often sufficient.
   * Verification and validation (V&V) evidence, such as unit test results and integration test logs.
2. **Leverage Pre-Existing Tools**
   * Use simple tools like:
     + Version-controlled repositories (e.g., GitHub, GitLab) for tracking design and code changes.
     + Lightweight project management tools (e.g., Trello, Jira) for tracking work packages, issues, and progress on requirements.
     + Automated testing frameworks and CI/CD pipelines to generate artifact logs that satisfy compliance without extra effort.
3. **Pre-Define Small, Focused Data Packages**
   * Prepare data packages ahead of time, containing:
     + Overview of the project lifecycle phase and scope.
     + Key artifacts including the SDP, RTM, and test summary reports.
     + Justifications or deviations/waivers for tailored or omitted requirements.

### 4.1.3. Communication and Survey Coordination

1. **Early Engagement**
   * Engage the survey lead and the assigned software point of contact (SW POC) as early as possible to understand expectations.
   * Ask for survey questions 3–4 weeks in advance and clarify deliverables aligned with the small project's scope.
2. **Establish the Primary Point of Contact (POC)**
   * Assign one software engineering leader (often the SW POC or a technical lead) as the single point of contact for all communications related to the survey. This reduces confusion and ensures tasks are prioritized effectively.
   * The SW POC should focus on gathering the requested evidence and aligning responses to the baseline set of questions.
3. **Leverage Frequent Touchpoints**
   * Schedule short check-ins with the survey team to provide updates on progress, clarify questions, or request advice on specific compliance items.

### 4.1.4. Focus on Core Elements for Small Projects

1. **Unified Program and Project Life Cycle**
   * Ensure the project aligns with NASA’s life cycle framework without overapplying processes that add unnecessary overhead.
   * Document life cycle milestones (e.g., requirements, design, testing) in an incremental and concise manner, possibly in bulleted formats or summary forms.
2. **Program and Project Reviews**
   * Map small project activities clearly to milestone reviews (e.g., PDR, CDR). Often, small projects can scale these reviews down to focus only on critical aspects of the software (e.g., safety-critical or mission-critical systems).
3. **Use of Technical Authority and Dissenting Opinions**
   * For small teams, designate a single technical authority reviewer or involve a senior software/system engineer for decisions and risk management.
   * Maintain a simplified log of dissenting opinions and their resolutions in meeting notes or other accessible team documentation.
4. **Software Engineering Management**
   * Simplify the Software Development Plan (SDP) into a concise document outlining:
     + Development tools and workflows.
     + Primary risks and how they are managed.
     + Key milestones or deliverables that integrate into the larger project.
5. **Lessons Learned and Feedback**
   * Document lessons learned in a lightweight format (e.g., a summary in Confluence, an Excel sheet), particularly as the project progresses through major software engineering milestones.

### 4.1.5. Use Objective Evidence Smartly

1. **Minimal yet Focused Evidence Collection**
   * Collect only essential objective evidence that corresponds to compliance items being appraised. Examples include:
     + Test logs from automated pipelines for software verification and validation.
     + Deployment scripts or build logs that demonstrate adherence to development and release requirements.
     + Risk records for safety-critical systems (e.g., likelihood and controls implemented).
2. **Automate Evidence Collection**
   * Use tools to automatically capture evidence. For small teams, Git version control logs or automated test reports can serve as formal compliance documentation.
3. **Document Tailoring Decisions and Deviations**
   * Provide simple justifications for tailored requirements or waivers:
     + Create a brief table summarizing deviations, their rationale, and any mitigating actions to address potential risks.

### 4.1.6. Survey Process Execution on Small Projects

1. **Efficient Question Responses**
   * Respond to the OCE baseline survey questions within the limited scope of the project. Focus on safety-critical areas, integration, and compliance with core NPR 7150.2 requirements.
2. **Engage Effectively During the Survey**
   * Conduct a focused review meeting with the survey team:
     + Present a high-level overview of the project.
     + Discuss compliance evidence and address OCE questions.
     + Highlight any innovative practices or lessons learned from the project.
3. **Accept Feedback Gracefully**
   * Use the feedback from the survey as actionable items for process improvement, tailoring future efforts, and addressing any outstanding compliance gaps proactively.

### 4.1.7. Post-Survey Follow-Up

1. **Act on Corrective Actions:**
   * Address deficiencies identified during the survey promptly and document the resolution clearly.
2. **Update Lessons Learned:**
   * If issues arise during the survey, document them as part of the project’s lessons learned to improve future processes.
3. **Provide Feedback to the OCE:**
   * Share any challenges the small project faced in meeting some requirements. This feedback allows the OCE to potentially refine future compliance survey processes for small-scale efforts.

### 4.1.8. Collaboration with OSMA

* If software assurance and software safety reviews by OSMA overlap with OCE survey requirements:
  + Consolidate Deliverables: Leverage the same objective evidence for both reviews to streamline preparation.
  + Coordinate with OSMA representatives during the OCE survey to minimize duplication of effort.

### 4.2 Key Principles for Small Project Success in Compliance Surveys

* **Keep it simple:** Focus on minimal yet sufficient evidence.
* **Be proactive:** Prepare deliverables well in advance and clarify questions before the survey begins.
* **Leverage automation:** Use tools to collect and present compliance evidence efficiently.
* **Focus on impact:** Prioritize safety-critical and mission-critical requirements, particularly where software has the greatest effect on project success.

By adhering to the above guidance, small projects can efficiently address OCE compliance surveys while maintaining high standards in software engineering practices, even with limited resources. This pragmatic approach ensures alignment with NASA’s rigorous requirements without overwhelming small project teams.

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
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-256)

  [NASA Directives and Charters Procedural Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_1400_001H_&page_name=main "Click to open in new window")

  NPR 1400.1H, NASA Office of Internal Controls and Management Systems, Effective Date: March 29, 2019, Expiration Date: March 29, 2024
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-261)

  [NASA Governance and Strategic Management Handbook,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=0C "Click to open in new window")

  NPD 1000.0C, NASA Governance and Strategic Management Handbook, Effective Date: January 29, 2020, Expiration Date: January 29, 2025
* (SWEREF-262)

  [NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.](https://nen.nasa.gov/web/oce/ta "Click to open in new window")

  NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-374) OCE Requirements Compliance Survey Process,Office of the Chief Engineer (OCE), NASA, 2010.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA missions and programs have yielded valuable lessons learned over the years, many of which underscore the importance of proper compliance checks, independent appraisals, and robust oversight mechanisms. Below are some relevant lessons from NASA's **Lessons Learned Information System (LLIS)** that directly or indirectly support this requirement for OCE-authorized appraisals.

### 6.1.1  Relevant NASA Lessons Learned

1. **Incomplete Oversight Increases the Risk of Programmatic Failures**
   * **Source:** LLIS-2227 – *Mars Climate Orbiter Mishap Investigation Findings*
   * **Description:** The Mars Climate Orbiter failure was attributed to a lack of rigorous systems engineering processes and compliance oversight, specifically in requirements definition and verification. There was insufficient independent review of requirements flowdown, and discrepancies (e.g., inconsistency between metric and imperial units) went undetected.
   * **Lesson Learned:** Independent compliance checks, such as appraisals authorized by the OCE, are vital to ensuring gaps or inconsistencies in requirements mapping, flowdown, and implementation are identified early. Regular appraisals create an opportunity to double-check critical areas before risks escalate.
   * **Connection to the Requirement:** This lesson reinforces the need for system-level compliance surveys led by the OCE to detect systemic or project-specific problems and verify accurate implementation of requirements.
2. **Lack of Independent Review Leads to Missed Noncompliance**
   * **Source:** LLIS-1772 – *Apollo 1 Fire Mishap Investigation*
   * **Description:** The Apollo 1 fire revealed serious non-compliances in materials used, pre-test procedures, and safety processes. Several flaws went unnoticed due to an absence of rigorous independent reviews.
   * **Lesson Learned:** Independent technical reviews, such as OCE-authorized appraisals, are critical to identifying gaps in compliance with policies, standards, and procedures that internal teams might overlook due to familiarity with the system or project.
   * **Connection to the Requirement:** OCE appraisals ensure compliance is checked systematically and independently, mitigating the risks associated with narrowly scoped or biased reviews.
3. **Systemic Issues Require Institutional Oversight**
   * **Source:** LLIS-1161 – *Columbia Shuttle Accident Investigation Report*
   * **Description:** The Columbia Shuttle disaster was influenced by systemic cultural and organizational deficiencies, particularly in the areas of safety and compliance. This included poor communication of dissenting opinions and insufficient oversight of waiver/deviation processes.
   * **Lesson Learned:** Institutional oversight, even at the project level, can help identify systemic issues such as weak dissenting opinion mechanisms or improperly documented deviations/waivers. OCE appraisals can serve as institutional “checks and balances” to ensure systemic risks are addressed.
   * **Connection to the Requirement:** Authorized appraisals by the OCE help identify systemic cultural, organizational, or technical deficiencies that may not be apparent at an individual project or Center level.
4. **Compliance Audits Can Identify and Disseminate Best Practices**
   * **Source:** LLIS-0905 – *Lessons Learned from a Focused Review Audit of Multiple NASA Projects*
   * **Description:** This review audit documented recurring issues in requirements traceability, risk management practices, and inconsistent application of NPR guidelines. However, it also uncovered instances of outstanding practices in requirements management that could be shared across the agency.
   * **Lesson Learned:** Compliance audits and appraisals should be designed to not only identify deficiencies but also recognize and disseminate best practices across Centers and projects. This improves organizational learning and strengthens future processes.
   * **Connection to the Requirement:** OCE-authorized appraisals are not punitive; they are opportunities to identify areas of excellence and share those lessons and innovations NASA-wide.
5. **Insufficient Verification of Requirements Tailoring Can Lead to Risks**
   * **Source:** LLIS-2024 – *James Webb Space Telescope Lessons on Requirements Tailoring*
   * **Description:** On the James Webb Space Telescope (JWST) project, tailoring key requirements to meet unique constraints was critical to success. However, some tailored requirements introduced risks that weren’t fully evaluated until late in the project lifecycle.
   * **Lesson Learned:** Tailored requirements need to be independently reviewed to ensure deviations from standard practices do not introduce unmitigated risks. Having an independent appraisal process to examine these tailored approaches ensures that risks are evaluated early and effectively.
   * **Connection to the Requirement:** This requirement ensures that OCE surveys review and verify tailored or waived requirements for their validity, appropriateness, and associated risks.
6. **Limited Compliance Checks Increase the Risk of Overlooked Errors in Software**
   * **Source:** LLIS-2215 – *Mars Polar Lander Loss*
   * **Description:** The loss of the Mars Polar Lander was partly caused by inadequate software engineering reviews and validation. Requirements were not verified thoroughly through independent compliance checks, and the software design introduced a critical failure mode in the descent sequence.
   * **Lesson Learned:** Regular compliance appraisals that include software-related requirements can significantly reduce the likelihood of introducing undetected errors into critical systems. A strong focus on appraising software engineering compliance, tools, and processes is key to project success.
   * **Connection to the Requirement:** OCE appraisals must include robust checks against software engineering processes to ensure compliance with NPR 7150.2 and related software assurance standards.
7. **Periodic Institutional Compliance Reviews Promote Early Detection of Issues**
   * **Source:** LLIS-1325 – *Johnson Space Center Institutional Best Practices*
   * **Description:** At Johnson Space Center (JSC), periodic institutional compliance reviews were credited with highlighting resource gaps, training needs, and risk mitigation shortfalls early in project lifecycles. This enabled timely course correction, which reduced cost and schedule impacts.
   * **Lesson Learned:** Regular appraisals authorized by oversight offices like the OCE are essential to detecting and correcting issues early, before they propagate to later, more expensive phases of project development.
   * **Connection to the Requirement:** This requirement aligns with the proven value of periodic, institutional-level reviews to prevent costly downstream impacts.
8. **Strong Feedback Mechanisms Are Critical for Policy Refinement**
   * **Source:** LLIS-2239 – *NASA Lessons on Organizational High-Reliability Practices*
   * **Description:** Feedback loops between project teams and agency policymakers are essential for improving compliance processes. Teams often identify misaligned or ambiguous requirements that, when corrected, improve project outcomes and compliance rates.
   * **Lesson Learned:** Compliance surveys should include robust mechanisms to capture feedback from Centers and projects regarding adherence to NASA policies and how they can be refined to better meet operational realities.
   * **Connection to the Requirement:** The OCE’s compliance surveys must include processes for gathering feedback, which can be used to refine NPR requirements and other agency policy documents for future projects.
9. **Tracking Trends Across Centers Improves Systemic Readiness**
   * **Source:** LLIS-1801 – *Space Shuttle Program Process Improvements*
   * **Description:** Lessons learned across different shuttle missions showed that recurring compliance deficiencies (e.g., in maintenance procedures and readiness practices) were addressed more effectively when tracked and rolled into system-level improvements.
   * **Lesson Learned:** Compliance surveys should track trends and recurring issues across Centers and projects to identify systemic risks and focus resources on priority areas for improvement.
   * **Connection to the Requirement:** This requirement provides an opportunity for the OCE to collect cross-Center data, informing systemic upgrades for processes, tools, and policies.

### 6.1.2  Final Summary of Lessons Learned for This Requirement

These lessons emphasize the necessity of an institutional compliance appraisal process authorized by the OCE to:

1. Verify requirements compliance early and regularly, especially for tailored or waived items.
2. Detect and mitigate systemic issues and recurring deficiencies across projects and Centers.
3. Highlight best practices and lessons learned to encourage cross-Center improvement.
4. Ensure critical areas, such as software engineering and safety, receive oversight consistent with NASA’s standards.
5. Build feedback loops that strengthen NPRs and other requirements for better applicability.

By leveraging lessons learned from past reviews and crises, this requirement ensures that NASA continues to foster a culture of rigorous compliance, mission assurance, and continuous improvement.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-129 - OCE NPR Appraisals**

2.1.1.4 The NASA OCE shall authorize appraisals against selected requirements in this NPR to check compliance.

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

The purpose of this requirement is to ensure that selected requirements in NPR 7150.2 [083](#_tabs-<p></p>) are assessed periodically to verify compliance across NASA projects and Centers. Software Assurance (SA) plays a key role in supporting and participating in these appraisals to ensure the effectiveness, consistency, and thoroughness of software assurance practices.

The following guidance outlines the responsibilities and actions Software Assurance personnel should take to support authorized appraisals of projects and programs.

### 7.4.2  Software Assurance Responsibilities

1. **Collaborate with the OCE on Appraisal Preparation**
   * **Engage Early in Planning**:
     + Work closely with the OCE and appraisal team to identify software assurance-related requirements from NPR 7150.2 that are included in the scope of the appraisal.
     + Help define clear criteria for evaluating compliance with assurance processes (e.g., requirements verification, risk management, defect tracking, test coverage).
   * **Assist in Appraisal Scoping**:
     + Ensure that assurance activities for critical software classifications (e.g., Class A/B safety-critical projects) are explicitly included in the appraisal scope.
     + Advocate for evaluating assurance processes in all lifecycle stages (planning, development, verification, and maintenance).
   * **Identify Projects or Centers for Focus**:
     + Work with the OCE to recommend projects or Centers with high-risk, high-visibility, or safety-critical software as candidates for appraisal, if applicable.
2. **Provide Assurance Artifacts to Support Compliance Reviews**
   * **Prepare and Organize Assurance Evidence**:
     + Collect key documentation that demonstrates compliance with NPR 7150.2 assurance-related requirements, such as:
       - Software Assurance Plans (per NPR 8739.8 [278](#_tabs-<p></p>)).
       - Verification and validation (V&V) reports.
       - Risk assessments and mitigation plans.
       - Test results, including coverage analysis and anomaly resolution reports.
       - Records of reviews, audits, and technical assessments.
   * **Ensure Traceability**:
     + Verify that assurance artifacts clearly trace back to their corresponding NPR 7150.2 requirements, ensuring that compliance is demonstrable.
3. **Participate in Appraisal Execution**  
   Software Assurance personnel should be active participants in the appraisal process to represent assurance-related responsibilities.  
   * **Present Assurance Matters During Appraisal Activities**:
     + Be prepared to explain how assurance-related practices align with NPR 7150.2 requirements.
     + Highlight key processes such as requirement verification, software safety risk evaluations, and independent testing efforts.
   * **Support Appraisal Evidence Reviews**:
     + Collaborate with the appraisal team in reviewing assurance documentation to verify compliance with selected NPR requirements.
     + Address any gaps or inconsistencies in assurance-related processes during the appraisal discussions.
   * **Facilitate Interviews and Data Reviews**:
     + Participate in or facilitate interviews of project SA personnel during appraisals to communicate how assurance processes are carried out in practice.
4. **Support Gap Analysis and Findings**
   * **Analyze SA-Specific Gaps**:
     + If non-compliance with assurance-related NPR 7150.2 requirements is identified, assist in evaluating the root cause (e.g., inadequate tailoring, resource issues, or incomplete implementation of assurance processes).
     + Document where and why assurance practices deviate from NPR requirements.
   * **Develop Gap Closure Recommendations**:
     + Recommend corrective actions to address assurance-related compliance gaps:
       - Enhance training or tools for software assurance staff.
       - Update assurance plans to clarify how each NPR assurance requirement is addressed.
       - Improve traceability between project plans and assurance deliverables.
   * **Prioritize Safety and Risk**:
     + Emphasize addressing gaps affecting safety-critical or mission-critical software as a first priority.
5. **Monitor and Ensure Closure of Findings**
   * **Track Corrective Actions**:
     + Collaborate with the OCE and project leadership to ensure corrective actions for software assurance compliance issues are documented, implemented, and completed.
     + Ensure updated assurance plans or processes address identified gaps effectively.
   * **Provide Follow-Up Evidence**:
     + For issues related to SA compliance, prepare follow-up artifacts to demonstrate that corrective actions have resolved any identified gaps.
6. **Contribute to Cross-Center Improvements**
   * **Analyze Trends from Appraisals**:
     + Identify systemic assurance issues across Centers or projects revealed during appraisals.
     + Share lessons learned related to software assurance gaps or best practices identified during appraisals to improve consistency across NASA projects.
   * **Advocate for Policy Refinements**:
     + Recommend updates to NPR 7150.2 or assurance plans if appraisal results reveal areas needing clarification, expansion, or improvement.

### 7.4.3  Key Assurance Areas to Address During Appraisals

Software Assurance should ensure appraisals verify compliance in critical areas, including:

1. **Planning and Documentation**:
   * Ensure software assurance plans (per NPR 8739.8) meet NPR 7150.2 requirements.
2. **Requirements Tailoring**:
   * Verify whether any tailored assurance requirements have been properly justified, approved, and mitigated for risks.
3. **Independent Verification and Validation (IV&V)**:
   * Confirm that IV&V is completed for required safety-critical or mission-critical software.
4. **Test Coverage and Validation**:
   * Ensure software assurance verifies adequate test coverage and validation results for requirements, including edge cases.
5. **Risk Management**:
   * Confirm that software assurance is actively engaged in identifying, tracking, and mitigating software risks.
6. **Compliance with Safety Standards**:
   * Verify assurance practices ensure safety-critical requirements are rigorously addressed.

### 7.4.4 Outcomes of Software Assurance Involvement

By following this guidance during OCE-authorized compliance appraisals:

1. **Enhanced Confidence in Assurance Compliance**:
   * Assurance processes will explicitly demonstrate compliance, reducing risks of unexpected findings.
2. **Clear Recommendations to Resolve Issues**:
   * Identified gaps will have actionable corrective actions to improve assurance effectiveness.
3. **Improved Assurance Practices Across Projects**:
   * Appraisal findings will drive consistent improvements in assurance process execution across NASA Centers.

### 7.4.5  Conclusion

Software Assurance plays an integral role in supporting OCE-authorized appraisals by ensuring accurate documentation, active participation, gap analysis, and corrective action tracking for assurance-related requirements in the RMM. By acting as the lead in determining and demonstrating compliance, SA ensures that mission safety, reliability, and overall software quality align with NASA's goals and NPR 7150.2 requirements.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-004 - OCE Benchmarking](/spaces/SWEHBVD/pages/102695394/SWE-004+-+OCE+Benchmarking) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-221 - OSMA NPR Appraisals](/spaces/SWEHBVD/pages/105709899/SWE-221+-+OSMA+NPR+Appraisals) |
