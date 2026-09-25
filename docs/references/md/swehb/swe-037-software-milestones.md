# SWE-037 - Software Milestones

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695415. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones

SWE-037 - Software Milestones

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695415)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695415&showCommentArea=true&showComments=true#addcomment)

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

3.1.7 The project manager shall define and document the milestones at which the software developer(s) progress will be reviewed and audited. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-037 History

SWE-037 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.5.6 The project shall define the milestones at which the software supplier(s) progress will be reviewed and audited as a part of the acquisition activities. |
| Difference between A and B | No change |
| B | 3.12.6 The project manager  shall define the milestones at which the software supplier(s) progress will be reviewed and audited as a part of the acquisition activities. |
| Difference between B and C | Added the requirement to document the milestones; Changed "supplier(s)" to "developer(s)"; Descoped the reqts by removing "as a part of the acquisition activities" |
| C | 3.1.7 The project manager shall define and document the milestones at which the software developer(s) progress will be reviewed and audited. |
| Difference between C and D | No change |
| D | 3.1.7 The project manager shall define and document the milestones at which the software developer(s) progress will be reviewed and audited. |

## 1.3 Applicability Across Classes

Classes F and G are labeled as "X (not OTS)" which means that the project is required to meet this requirement for all software that is not considered off-the-shelf.

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

For any software project, it is critical for management to review progress early and periodically to ensure the project remains on schedule, is progressing toward implementation of the requirements, and ultimately is addressing the customer's needs. It is also important for management to confirm periodically that the technical goals of the project are being achieved and that the technical direction of the project is appropriate (NPR 7123.1, NASA Systems Engineering Processes and Requirements). [041](#_tabs-<p></p>) Milestone reviews provide this type of management visibility into a project.

Defining and documenting milestones for progress reviews and audits ensures the project manager can maintain oversight, provide consistent progress evaluation, detect risks early, and maintain compliance with regulatory standards. Milestones improve collaboration, align stakeholder priorities, and establish clear checkpoints for all phases of development, promoting efficiency, accountability, and quality assurance. These structured review points are essential for managing risk and ensuring mission success in aerospace software projects.

For software development that is acquired (supplied by a contractor), having regular progress reviews is even more important since these reviews are the keys to ensuring the contractor understood and will provide the product that NASA requested and that meets NASA's requirements for safety, quality, reliability, etc.

Milestone reviews can also serve to facilitate and ensure coordination between multiple development groups including development groups at multiple NASA Centers and contractors.

This requirement ensures that the software development effort is systematically monitored and evaluated to verify progress, detect issues early, and ensure alignment with project objectives, mission requirements, stakeholder expectations, and safety standards. Defining and documenting review and audit milestones provides a clear structure that promotes accountability, transparency, and compliance throughout the software development life cycle.

The rationale for this requirement is explained below:

## 2.1 Ensures Progress Tracking

* **Why It Matters:**
  + Defined milestones provide discrete points in the project where the software team's progress can be reviewed objectively. These checkpoints help prevent delays or deviations from the planned schedule.
  + Without milestones, project managers may lose visibility into the development timeline, increasing the risk of missed deadlines or compromised deliverables.
* **Rationale:**
  + Milestones enable periodic evaluation of progress and allow proactive measures if development falls behind schedule or strays from planned objectives.

## 2.2 Validates Deliverables

* **Why It Matters:**
  + Auditing development progress at predefined milestones ensures that intermediate artifacts and deliverables (e.g., specifications, designs, test cases, prototypes, etc.) meet established acceptance criteria before development proceeds.
  + Unverified or unchecked deliverables may result in defects propagating downstream, increasing the risk of rework and compromising overall quality.
* **Rationale:**
  + Milestone reviews ensure that deliverables are validated against acceptance criteria, minimizing the risk of issues in subsequent phases.

## 2.3 Provides Early Detection of Issues

* **Why It Matters:**
  + Regular reviews act as a checkpoint for identifying problems such as technical challenges, resource bottlenecks, or compliance gaps before they escalate and impact the project’s objectives.
  + Without defined milestones, issues may go unnoticed, leading to significant delays, budget overruns, or mission-critical failures.
* **Rationale:**
  + Milestones serve as early detection mechanisms to identify risks or deficiencies, enabling corrective actions to be taken before they jeopardize the project.

## 2.4 Promotes Accountability

* **Why It Matters:**
  + Milestones create clear expectations for progress and deliverables, ensuring accountability for the software development team, assurance personnel, and project leadership.
  + Without milestones, responsibilities may become unclear, leading to inefficiencies in team collaboration and a lack of visibility into individual contributions.
* **Rationale:**
  + Documenting review points fosters accountability among all stakeholders and ensures that each phase progresses according to the agreed schedule and requirements.

## 2.5 Aligns Teams Toward a Common Goal

* **Why It Matters:**
  + Milestone reviews facilitate communication between stakeholders, including developers, assurance personnel, customers, and the project manager. They serve as a forum to verify that all teams are aligned with the project’s goals and requirements.
  + Misalignment among teams can result in defects, unnecessary rework, or delays in integration.
* **Rationale:**
  + Milestones ensure consistent collaboration and alignment of priorities across all parties involved in the software development process.

## 2.6 Establishes Formal Verification and Compliance Checkpoints

* **Why It Matters:**
  + Aerospace software development is subject to strict compliance standards (e.g., NPR 7150.2 [083](#_tabs-<p></p>) , DO-178C [493](#_tabs-<p></p>) , NASA systems engineering requirements). Milestone reviews act as formal audits that verify adherence to these standards.
  + Failure to verify compliance during the project lifecycle can result in major penalties, rejection of deliverables, or even mission failure.
* **Rationale:**
  + Milestones provide formal compliance checkpoints, ensuring regulatory requirements and quality standards are continuously upheld.

## 2.7 Facilitates Risk Management

* **Why It Matters:**
  + Regular audits and reviews reduce uncertainty by uncovering risks related to technical failures, deviations from project scope, resource constraints, or integration issues.
  + Without milestones, risks may accumulate or remain unidentified until late in the project lifecycle, leading to costly and time-consuming corrections.
* **Rationale:**
  + Establishing milestones helps mitigate risks by allowing project teams to evaluate and address vulnerabilities at predefined intervals.

## 2.8 Enables Controlled Iterative Development

* **Why It Matters:**
  + Iterative approaches, especially in agile or phased software development, benefit from milestones that confirm progress before moving on to subsequent phases. Milestones ensure that iterations meet specific objectives before additional features or integrations are added.
  + Without controlled iteration, development efforts may result in wasted efforts, abandoned code, or insufficient system validation.
* **Rationale:**
  + Milestones structure iterative development, ensuring each phase delivers the foundation necessary for subsequent work.

## 2.9 Supports Efficient Resource Allocation

* **Why It Matters:**
  + Milestones provide opportunities to reassess resource allocation based on project progress and identified risks. If problems arise during a review, adjustments to manpower, budget, or tools can be made accordingly.
  + Unchecked progress may lead to over- or underutilization of resources, increasing inefficiencies.
* **Rationale:**
  + Documenting milestone audits allows the project manager to make timely resource adjustments, ensuring that development proceeds efficiently.

## 2.10 Improves Transparency for Stakeholders

* **Why It Matters:**
  + Clients, customers, and stakeholders benefit from visibility into project progress. Milestones provide key reporting points where stakeholders can review deliverables, approve outcomes, and provide feedback.
  + Lack of visibility can lead to stakeholder dissatisfaction, misaligned expectations, or delayed approvals.
* **Rationale:**
  + Milestones improve communication and transparency, keeping stakeholders informed and engaged throughout the development lifecycle.

## 2.11 Supports Certification and Approval

* **Why It Matters:**
  + Aerospace software often requires formal audits and certifications (e.g., flight readiness reviews, safety certifications). Milestones enable structured audits that provide evidence of the software's reliability and readiness for certification.
  + Late certification reviews without milestone-based evaluations risk missing essential verifications or delaying approvals.
* **Rationale:**
  + Milestones support systematic certification processes by ensuring the software undergoes necessary reviews and audits prior to acceptance.

## 2.12 Establishes Exit and Entrance Criteria

* **Why It Matters:**
  + Milestones serve as gating mechanisms that establish **exit criteria** for progress to the next phase and **entrance criteria** for subsequent activities. This ensures work is complete and verified before proceeding.
  + Lack of exit and entrance criteria risks incomplete preparation for downstream tasks or phases, leading to integration or testing complications.
* **Rationale:**
  + Defining milestones ensures prerequisites are satisfied before entering critical phases, reducing risks of downstream defects or delays.

## 2.13 Implementation Notes

* Milestones will vary depending on project complexity, scope, and lifecycle model (e.g., waterfall, agile, hybrid). For instance:
  + In **waterfall projects**, milestones typically align with phased delivery (e.g., requirements review, design review, testing phases).
  + In **agile projects**, milestones can include sprint reviews, backlog refinements, or customer acceptance points for iterative deliverables.
* Common milestone review types include:
  + **Requirements Review:** Ensures customer needs are fully defined and understood.
  + **Preliminary Design Review (PDR):** Verifies technical feasibility and compliance with system requirements.
  + **Critical Design Review (CDR):** Confirms the design is ready for implementation.
  + **Test Readiness Review (TRR):** Validates testing plans and resources.
  + **System Integration Review (SIR):** Ensures proper system-level integration and interoperability.
  + **Delivery Review:** Documents readiness for approval and handover.

See also topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews), [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)

# 3. Guidance

The purpose of the milestone review meeting is to review the overall milestone progress and accomplishments at selected milestones/phases during the project life cycle. Milestone reviews are generally defined by the project manager. This meeting also facilitates the project team to have a get-together with higher management and other stakeholders and to discuss project issues; share lessons learned and suggest improvements for the next milestones.

The milestone review guidance provides refined explanations to highlight the importance of milestones, detailed best practices for selecting and managing them, and practical steps for using milestones effectively. The aim is to promote clarity, consistency, and efficiency in managing milestone progress reviews across all types of projects, including acquired software development.

Milestone reviews are critical to monitoring progress, evaluating deliverables, managing risks, and maintaining alignment with project goals and schedules. By carefully selecting, documenting, and managing milestones, project managers can balance oversight with efficiency, ensuring mission success while fostering a strong foundation for project accountability and quality.

## 3.1 Purpose of the Milestone Review Meeting

The milestone review meeting serves to evaluate the project's progress and accomplishments at predetermined points during the software development life cycle. It is an opportunity to ensure alignment with project goals, address issues, and optimize plans for future work. Milestone reviews also enable the project manager and team to engage with higher-level management and other stakeholders to review performance, suggest improvements, and share lessons learned.

## 3.2 Why Milestones Matter

Milestones are an integral part of project planning and execution. They serve as **checkpoints** to measure progress, ensure alignment with the overall schedule, and enable course corrections if needed. Proper use of milestone reviews enhances clarity, accountability, and transparency across all phases of the project.

#### **Key Benefits of Milestones**

1. **Progress Tracking:**

   * Milestones provide clear, measurable points to compare actual progress with planned objectives. For smaller or simpler projects, milestones may be limited to critical points like project start and end dates.
   * In long-duration projects, milestones act as checkpoints to ensure steady progress. For example:
     + At 25% of the project timeline, approximately 25% of the deliverables should be complete, and the review evaluates whether this is on track.
2. **Early Problem Detection:**

   * Milestone reviews offer an **early warning system**. For instance, if the 25% milestone shows only 15% completion, the discrepancy signals potential risk and highlights areas that need immediate attention.
3. **Success Communication:**

   * Milestones provide a clear way to showcase accomplishments and build stakeholder trust. By communicating progress at each milestone, stakeholders remain updated on the project's status and outcomes.
   * This is especially useful in complex or mission-critical projects, where the timely completion of interim steps is vital.

Milestones are less common in **Agile projects** due to the flexibility of Agile methodologies, which focus on iterations rather than predefined phases. For Agile workflows, milestones are often tied to the **end of sprints or major objectives**, serving as reflections of progress over time rather than strict deadlines.

## 3.3 How to Select Milestones

### 3.3.1 Criteria for Identifying Milestones

When determining appropriate milestones, the following principles and questions can help ensure the right balance between too few and too many milestones:

1. **Essential Practice:** Select milestones tied to meaningful, high-impact points in the project, avoiding excessive or inconsequential milestones.
2. **Clear Definition:** Milestones must represent **well-defined events**, rather than activities that require time (e.g., completion of a design review, approval of requirements, delivery of a code base).
3. **Stakeholder Relevance:** Choose milestones that demand review and approval from stakeholders.

### 3.3.2 Guiding Questions to Define Milestones

* Is the milestone associated with a key deliverable or end product?
* Is this milestone time-sensitive (e.g., will missing it impact final deadlines)?
* Is this milestone critical to overall project success or indicative of significant progress?
* Does the milestone require review and sign-off by management, stakeholders, or customers?
* Does the milestone represent an **input dependency** from an external entity (e.g., subcontractors or vendors)?

### 3.3.3 Example Milestone Selection for Software Projects

* Software requirements review.
* Preliminary software design completion.
* Delivery of an initial build (prototyping).
* Completion of integration testing.
* Deployment readiness review.

### 3.3.4 For External Dependencies

* Subcontractor deliverables (e.g., materials, prototypes, or sub-assemblies).
* Critical delivery dates for items required to meet project deadlines.

## 3.4 How to Use Milestones in Project Management Software

Software tools can significantly enhance milestone tracking by linking tasks, deliverables, and progress to key checkpoints. Effective use of project management software allows for:

1. **Task-Milestone Organization**

   * Connect tasks to associated milestones to provide clarity on how individual contributions impact broader goals.
   * Example: For a software update, major milestones could be:
     + Finalizing software design → Design-related tasks mapped to this milestone.
     + Completing production → Assign production tasks.
     + Testing completeness → Link testing tasks.
2. **Defining Check-in Points**

   * Milestone reviews should be scheduled consistently with overall project goals. Key tasks and expectations for each milestone should be clearly defined.
3. **Progress Visualization**

   * Use milestone tracking features to provide a graphical or report-based view of overall project progress.
   * Notify team members when milestone deadlines or review meetings are approaching.

## 3.5 Tasks Associated with Milestone Reviews

Milestone reviews involve detailed preparation, organization, and follow-up actions. Below are the recommended steps for conducting these reviews effectively:

#### **Preparation Phase**

1. The project manager calculates milestone progress compared to planned deliverables and prepares a **milestone review report** based on established templates.
2. Send the agenda, review report, and meeting invitation to all relevant stakeholders as scheduled.

#### **During the Review**

1. Conduct milestone review meetings:
   * Assess progress and overall milestone status.
   * Discuss and resolve open issues.
   * Record lessons learned and improvement suggestions.
2. Document and log action items and issues into an **issue management system**.

#### **Follow-Up Phase**

1. Distribute the milestone review report, including meeting outcomes, to stakeholders and customer contacts.
2. Assign action items to team members or stakeholders, ensuring clarity of their responsibilities.
3. Track all action items to closure and provide regular updates on their resolution.

## 3.6 Acquired Software Development and Milestone Reviews

For **acquired software development**, milestone reviews must be explicitly incorporated into the contract to ensure compliance and enforceability. The contract serves as the binding document for defining:

* Contractor responsibilities.
* Deliverable review and approval timelines.
* Monitoring activities (e.g., audits, technical reviews, and progress reports).

#### **Key Considerations for Acquired Software Projects**

* Include review periods for contractor deliverables to facilitate approval and revisions.
* Define **entrance and exit criteria** for reviews as specified in **NPR 7123.1** [041](#_tabs-<p></p>) , **NPR 7120.5** [083](#_tabs-<p></p>), and related documents. See [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)
* Address unforeseen events:
  + Establish a framework for corrective actions.
  + Ensure that all reviews (e.g., design reviews, progress audits) are explicitly listed in the SOW and contract documents.
* For reviews not initially covered in the SOW, amendments may be necessary to incorporate them post-contract award.

### **Additional Considerations**

1. Consult **Center guidance** to supplement milestone selection, review approaches, and scheduling strategies.
2. Refer to Topic **[7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)** to define entrance and exit criteria while developing milestone checklists.
3. Collaborate with the technical authority and stakeholders during planning to ensure alignment with project needs.

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination)        * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control) |

# 4. Small Projects

Small projects often differ from larger, more complex efforts in terms of scope, resources, and timeline. However, maintaining structured **review plans** and **milestones** is equally critical to ensuring progress, achieving technical goals, and meeting stakeholder expectations. The following improved guidance refines this process by providing tailored advice for small projects to enable efficient oversight without introducing unnecessary complexity.

Small projects must still maintain structured review processes and milestones to ensure alignment with technical goals and mission success. Tailored, efficient planning allows for adequate oversight without excessive administrative overhead, providing the greatest insights into progress, risks, and technical direction. By leveraging simplified review processes, prioritizing critical content, and engaging stakeholders effectively, small projects can achieve strong outcomes while remaining resource-efficient.

## 4.1 Importance of Milestones and Project Reviews

Small projects are required to adhere to NASA’s established guidelines from **NPR 7120.5 [083](#_tabs-<p></p>)** , **NPR 7120.7 [264](#_tabs-<p></p>)**, **NPR 7120.8 [269](#_tabs-<p></p>)**, and **NPR 7123.1 [041](#_tabs-<p></p>)**.   These documents define milestone reviews and emphasize the integration of software components into specific project reviews. While smaller projects may not require the extensive documentation or frequency of reviews seen in larger projects, aligning software progress with key milestones remains essential for meeting mission objectives and ensuring technical direction.

#### **Key Advantages for Small Projects:**

* **Visibility into Progress:** Milestones provide clear checkpoints to assess whether the development effort is on track.
* **Alignment with Technical Goals:** Regular reviews ensure the project is progressing according to the technical and operational expectations defined during formulation.
* **Early Risk Detection:** Review milestones serve as opportunities to identify issues (technical, resource-related, or otherwise) before they impact project outcomes.
* **Focus on Mission Criticality:** Small projects typically have limited resources; milestones help prioritize essential tasks and streamline efforts on meeting critical deliverables.

## 4.2 Establishing Review Milestones for Small Projects

Small projects should determine a **review process** tailored to their scope and complexity. This process should:

1. **Reflect Project Requirements:** Ensure milestones and reviews align with the specific technical and customer requirements of the project.
2. **Promote Simplicity and Efficiency:** Streamline review activities to focus on the greatest insights into progress without overburdening the team.
3. **Integrate Software Deliverables:** Explicitly include software components in milestone planning to ensure compliance, traceability, and proper oversight.

#### **Guidelines for Tailoring Review Milestones:**

* **Simplify the Review Process:** Aim for fewer, high-impact reviews centered on critical project goals rather than exhaustive evaluations.
* **Combine Phases Where Appropriate:** If certain project phases (design, coding, testing) are straightforward or well-defined, their reviews can be conducted together.
* **Ensure Adequate Content:** Include only the most essential technical metrics, risks, and progress indicators in review discussions.
* **Balance Resources and Insights:** The review process must be robust enough to provide meaningful insights while remaining practical for the size of the project.

## 4.3 Suggested Review Milestones for Small Projects

Typical milestone reviews for small projects include the following:

#### **Formulation Phase:**

1. **Project Kickoff/Initial Requirements Review:**
   * Discuss customer needs, project scope, and establish technical goals.
   * Define entrance and exit criteria for subsequent milestones.

#### **Development Phase:**

1. **Software Requirements Review (SRR):**

   * Validate that system-level requirements are fully understood and adequately translated into software specifications.
   * Identify gaps or risks in requirement traceability.
2. **Preliminary Design Review (PDR):**

   * Confirm technical feasibility and alignment with project goals.
   * Review initial design elements, tools, and technologies for software implementation.
3. **Critical Design Review (CDR):**

   * Evaluate the final software design and readiness for coding.
   * Ensure alignment with operational requirements, including safety and performance benchmarks.
4. **Test Readiness Review (TRR):**

   * Assess testing plans, test cases, and resources for the verification and validation of software deliverables.

#### **Delivery Phase:**

1. **System Integration Review (SIR):**

   * Evaluate how the software integrates with hardware systems, legacy systems, or other mission elements.
   * Identify any interoperability risks.
2. **Acceptance/Deployment Review:**

   * Confirm software readiness for delivery and operational use.
   * Validate compliance with milestones, regulatory requirements, and customer expectations.

See also Topic [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria), [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews),

## 4.4 Practical Steps for Structuring Review Processes

To develop a tailored review process that meets project requirements, consider the following steps:

### 1. Identify Critical Milestones

* Narrow down review points to track essential technical and operational aspects of the project.
* Focus on deliverables that affect mission success, such as requirements validation, test readiness, and software integration.

### 2. Prioritize Content Over Documentation

* Optimize review agendas by focusing on metrics, risks, and goals pertinent to the size of the project.
* Simplify reporting by using templates or condensed summaries of milestone progress.

### 3. Include Stakeholders and Customers

* Engage relevant stakeholders in the review process to ensure alignment and buy-in on technical direction.
* Keep communication clear and precise for non-technical stakeholders to ensure shared understanding of progress and concerns.

### 4. Tailor Oversight for Small Teams

* Reduce administrative burden by incorporating agile feedback loops where appropriate.
* Avoid requiring extensive documentation for reviews unless mandated by external contracts or regulatory compliance.

### 5. Use NASA Resources

* Small projects should leverage existing NASA resources, such as **Center Process Asset Libraries (PALs)** or frameworks from **NPR 7120.5** and **NPR 7123.1**, to simplify milestone planning and execution.

## 4.5 Special Considerations for Acquired Software Development

When acquiring software, milestone reviews must be incorporated into contracts and development agreements to enforce contractor compliance and performance. For small projects, the following contractual elements are essential:

* **Defined Surveillance Activities:** Include monitoring activities, milestone reviews, technical audits, and decision points in the contract to ensure progress visibility.
* **Review and Approval Periods:** Specify deadlines for deliverable submissions and required corrections to resolve findings.
* **Entrance and Exit Criteria:** Ensure formal checklists for milestone approvals are included, enabling clarity for both the contractor and project team. See Topic  [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)

#### **Recommended Contractual Elements:**

* Technical Reviews (as defined in NPR 7120.5, 7120.7, or 7123.1).
* Review completeness checklists to verify milestone outputs.
* Progress reporting templates tied to milestones for efficient oversight.

## 4.6 Reference Guidance for Small Projects

Small projects can refer to the following documents for additional insights and requirements:

1. **NPR 7120 Family:** Defines milestone review standards and approaches for different project types.
2. **Topic** [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)**:** Describes review entrance and exit criteria, inputs, reviewed materials, and outputs.
3. **Acquisition Guidance (**[7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance)**):** Provides strategies for incorporating milestone reviews into contracts.
4. **Issue Management Systems:** Use automated tools to track and resolve action items generated during milestone reviews.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-048)

  [Risk Classification for NASA Payloads](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=4A "Click to open in new window")

  NPR 8705.4A, Office of Safety and Mission Assurance, Effective Date: April 29, 2021, Expiration Date: April 29, 2026
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
* (SWEREF-264)

  [NASA Information Technology Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=7A "Click to open in new window")

  NPR 7120.7A, Office of the Chief Information Officer, Effective Date: August 17, 2020,
  Expiration Date: August 17, 2025
  .
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-493)

  [Software Considerations in Airborne Systems and Equipment Certification,](http://www.verifysoft.com/en_DO-178C.html "Click to open in new window")

  RTCA DO-178C, January 5, 2012
* (SWEREF-528)

  [Acquisition and Oversight of Contracted Software Development (1999)](https://llis.nasa.gov/lesson/921 "Click to open in new window")

  Public Lessons Learned Entry: 921,
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

* **Acquisition and Oversight of Contracted Software Development (1999). Lesson Number 0921[528](#_tabs-<p></p>):**  Tailorable acquisition management and oversight processes for NASA contracted software development are essential to ensure that customers receive a quality product. A documented lesson from the NASA Lessons Learned database includes a cause of the loss of a mission "the lack of a controlled and effective process for acquisition of contractor-developed, mission-critical software." In this particular case, the quality of the contractor's product was not monitored as it would have been if the proper milestones for reviewing and auditing contractor progress were in place.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [All stakeholders should be aware of the project plan and schedule](https://software.gsfc.nasa.gov/lesson-details/63/). **Lesson Number 63**: The recommendation states: "All stakeholders should be aware of the project plan and schedule."
* [Assess status independently based on artifacts, not on reported status](https://software.gsfc.nasa.gov/lesson-details/141/). **Lesson Number 141**: The recommendation states: "Assess status independently based on artifacts, not on reported status."

# 7. Software Assurance

**SWE-037 - Software Milestones**

3.1.7 The project manager shall define and document the milestones at which the software developer(s) progress will be reviewed and audited.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that milestones for reviewing and auditing software developer progress are defined and documented.

2. Participate in project milestones reviews.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support project oversight, validate compliance, manage risks, and ensure the quality of delivered software throughout the software lifecycle. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

Below is a categorized list of Software Assurance products relevant to lifecycle requirements such as this requirement ("Define and document milestones for software developer reviews and audits") and other NASA software assurance and lifecycle guidelines.

### 7.2.1. Planning and Process Assurance Products

#### 7.2.1.1 Software Assurance Plan (SAP)

* **Description**: A document that defines all SA activities, tasks, responsibilities, standards, tools, and deliverables required for the project.
* **Purpose**: Provides a roadmap for SA activities to ensure compliance with software lifecycle requirements.
* **Contents**:
  + SA objectives and scope.
  + Defined roles and responsibilities of SA personnel.
  + Processes for risks, audits, reviews, testing, and metrics tracking.
  + Schedule of SA activities aligned with project milestones.

#### 7.2.1.2 Milestone Assurance Plan

* **Description**: A specialty plan dedicated to defining SA activities that will be conducted at each milestone (e.g., PDR, CDR, TRR, SAR).
* **Purpose**: Ensures SA participation and oversight in lifecycle reviews or audits aligned with milestones.
* **Contents**:
  + Milestone descriptions and objectives.
  + Entry/exit criteria for milestone reviews.
  + SA-specific review checklists and compliance criteria.

#### 7.2.1.3 Software Safety Plan

* **Description**: A plan that outlines assurance activities specific to software safety considerations, including hazard analyses and safety testing.
* **Purpose**: Documents activities aimed at promoting safe software design, implementation, and operation.
* **Contents**:
  + Identification of safety-critical software components.
  + Methods for software failure detection and mitigation.
  + Assurance tasks to verify risk controls for safety-critical systems.

### 7.2.2. Risk Management Products

#### 7.2.2.1 Risk Tracking Logs

* **Description**: A detailed list of all identified risks associated with the software development lifecycle, including status updates and mitigation plans.
* **Purpose**: Provides evidence that risks are identified, assessed, tracked, and resolved before key milestones.
* **Contents**:
  + Description and impact level of risks.
  + Risk status (e.g., Open, Mitigated, Closed).
  + Mitigation actions and ongoing monitoring activities.

#### 7.2.2.2 Risk Assessment Reports

* **Description**: Independent reports assessing risks raised during software milestone reviews or audits.
* **Purpose**: Documents critical risks flagged by SA personnel and provides recommendations for mitigation.
* **Contents**:
  + Prioritized risk rankings based on severity and probability.
  + Recommended actions to reduce risk and align with project goals.
  + Evidence of risk closure after mitigation.

#### 7.2.2.3 Risk Escalation Reports

* **Description**: Reports for unresolved risks that require management-level attention beyond standard mitigation.
* **Purpose**: Ensures risks impacting milestones are escalated appropriately for awareness and action.
* **Contents**:
  + Detailed description of the risk and potential milestone or schedule impact.
  + Justification for escalation and recommended strategies for resolution.

### 7.2.3. Review and Audit Products

#### 7.2.3.1 Milestone Review Checklists

* **Description**: Checklists used to verify compliance with milestone-specific entry, exit, and review criteria.
* **Purpose**: Ensures thorough SA assessment of developer progress at milestones.
* **Contents**:
  + List of criterion-based questions for requirements coverage, deliverable readiness, testing completeness, etc.
  + Areas flagged for non-compliance that require corrective action.

#### 7.2.3.2 Milestone Review Reports

* **Description**: Reports summarizing SA findings and feedback from participation in milestone reviews or audits (e.g., PDR, CDR, TRR).
* **Purpose**: Provides documentation of SA activities during milestone events while offering actionable recommendations.
* **Contents**:
  + Milestone objectives reviewed by SA.
  + Issues flagged, open action items, and risks tied to deliverables or processes.
  + Metrics and observations on developer maturity and compliance.

#### 7.2.3.3 Audit Reports

* **Description**: Comprehensive evaluation reports from lifecycle audits conducted by SA personnel.
* **Purpose**: Documents findings from audits of software deliverables, processes, and compliance with standards.
* **Contents**:
  + Scope of audit (e.g., process, artifact compliance, safety).
  + Findings and identified gaps in compliance with project requirements.
  + Corrective actions and follow-ups.

### 7.2.4. Deliverable Assurance Products

#### 7.2.4.1 Deliverable Traceability Matrix

* **Description**: A matrix illustrating traceability between requirements, design elements, code components, testing, and deliverables.
* **Purpose**: Ensures every deliverable meets requirements and is traceable across the lifecycle.
* **Contents**:
  + Mapping between requirements, design, and deliverables.
  + Evidence of compliance or validation coverage.
  + Traceability gaps flagged by SA for mitigation.

#### 7.2.4.2 Software Validation and Verification (V&V) Reports

* **Description**: Stand-alone reports combining validation and verification activities for deliverables such as source code, testing artifacts, and documentation.
* **Purpose**: Ensures deliverables are tested, meet functional requirements, and align with project specifications.
* **Contents**:
  + Test results and validation coverage.
  + Documentation of defects or gaps found during review or testing.
  + Corrective action tracking for non-compliant elements.

#### 7.2.4.3 Deliverables Compliance Checklists

* **Description**: Checklists used by SA personnel to evaluate the readiness and quality of deliverables being reviewed at milestones.
* **Purpose**: Provides targeted scrutiny toward deliverable quality and lifecycle maturity.
* **Contents**:
  + Specific deliverable compliance criteria tied to milestone objectives.
  + SA performance ratings of deliverables (e.g., complete, needs improvement).

### 7.2.5. Progress and Metrics Tracking Products

#### 7.2.5.1 SA Metrics Reports

* **Description**: Reports summarizing key measurable results from SA activities to track project progress and compliance.
* **Purpose**: Provides quantitative evidence of lifecycle maturity and SA contributions.
* **Contents**:
  + Compliance rates (e.g., percentage of compliant deliverables, documents).
  + Risk closure rates and milestone audit coverage.
  + Progress metrics such as defect trends, test coverage, and task completion rates.

#### 7.2.5.2 Development Oversight Dashboards

* **Description**: Visual dashboards summarizing milestone progress, deliverable readiness, defect trends, etc.
* **Purpose**: Provides stakeholders with high-level visibility into software assurance performance.
* **Contents**:
  + Charts summarizing key metrics (e.g., burn-down rates, milestone completion status).
  + Issue trend analysis (open actions, defect reports).

#### 7.2.5.3 Status Checklists

* **Description**: Milestone-specific checklists used to monitor progress toward entry/exit conditions for milestone events.
* **Purpose**: Tracks readiness of tasks, deliverables, and compliance steps relative to planned objectives.
* **Contents**:
  + Status summaries of planned tasks and actions flagged for review.
  + Closure status of prior milestone issues or risks.

### 7.2.6. Stakeholder Engagement Products

#### 7.2.6.1 Stakeholder Review Records

* **Description**: Logs documenting stakeholder involvement in milestone reviews or assurance reports.
* **Purpose**: Confirms stakeholder accountability and participation in milestone oversight.
* **Contents**:
  + Review logs showing stakeholder feedback and concerns.
  + Follow-up records of issues raised by stakeholders and resolved by developers or SA.

#### 7.2.6.2 Stakeholder Feedback Reports

* **Description**: Reports summarizing stakeholder-raised concerns, recommendations, and resolutions during reviews.
* **Purpose**: Tracks how stakeholder participation improves deliverables and processes.
* **Contents**:
  + Classification of feedback items by priority (e.g., critical, low).
  + Implementation evidence for accepted stakeholder feedback.

### 7.2.7 Summary of Software Assurance Products

| **Category** | **Example Products** | **Purpose** |
| --- | --- | --- |
| **Planning & Process Assurance** | Software Assurance Plan, Milestone Assurance Plan, Software Safety Plan | Define SA activities, tasks, and milestones for project oversight. |
| **Risk Management** | Risk Logs, Risk Assessment Reports, Risk Escalation Reports | Track and mitigate risks impacting software milestones or deliverables. |
| **Reviews & Audits** | Review Checklists, Milestone Review Reports, Audit Reports | Verify lifecycle compliance and developer progress at project milestones. |
| **Deliverables Assurance** | Traceability Matrix, V&V Reports, Deliverable Checklists | Evaluate deliverable quality and traceability across lifecycle stages. |
| **Progress Tracking** | Metrics Reports, Dashboards, Progress Checklists | Monitor development progress and SA contributions quantitatively. |
| **Stakeholder Engagement** | Review Records, Feedback Reports | Ensure stakeholder participation and accountability for milestone reviews. |

  

These Software Assurance products help ensure lifecycle oversight, compliance monitoring, and risk management, while serving as documentation for SA's independent validation activities throughout the project.

## SA Products for Milestone Reviews

| Review | Software Assurance Product for Review |
| --- | --- |
| **All Reviews** | * SA's general assessment of the status and quality of the software and safety activities * Any schedule/progress, quality, or safety concerns * High-level results of any audits, peer reviews, assessments, or analyses |
| **Additional Software Assurance /Safety Products for Milestone Reviews** | |
| **System Requirements Review (SRR)** | * Independent SA Software Classification or Concurrence on Software Engineering's Software Classification * SA Safety-Criticality Determination * Preliminary Hazard Analysis * Preliminary SA Plan, SA schedule, and SA processes |
| **Software Requirements Review (SwRR)** | * Software Assurance/Quality Plan * Preliminary Safety Plan * SA Requirements Assessment, including any issues with bidirectional traceability |
| **Mission Definition Review (MDR)** | * Updated Software Assurance/Safety Plan * Preliminary SA Safety Analysis * SA status, including results from any assessments, audits, peer reviews (See all reviews above) |
| **System Definition Review (SDR)** | * Software Safety Analysis * Software Assurance/Safety Plan (for baselining) * SA status, including results from any assessments, audits, peer reviews (See all reviews above) |
| **Preliminary Design Review (PDR)** | * Software Safety Analysis, including FTA, FMEA (if done) * SA Compliance Matrix * SA status, including results from any assessments, audits, peer reviews (See all reviews above) |
| **Critical Design Review (CDR)** | * Hazard Analysis * SA Safety Plan with verifications * SA assessment of design * SA analysis of software progress, metrics * SA status of safety and assurance activities, including results from any assessments, audits, peer reviews |
| **Production Readiness Review (PRR)** | * SA status (See all reviews above) |
| **System Integration Review (SIR)** | * SA status (as in all reviews), including any concerns with safety or the integration process * SA analysis of static code analysis results * SA assessment of integration plans, procedures, or handling of safety requirements * Status of system discrepancies, system test results |
| **Test Readiness Review (TRR)** | * SA assessment of test readiness, test procedures, witnessing plans (or SA participation plans) * SA analysis of software metrics, software progress * SA results of any code assessments, audits, peer reviews * SA results of Version Description Document (VDD) and Functional Configuration Audits (FCA) |
| **System Acceptance Review (SAR)** | * SA Status * Results of configuration audits: Functional Configuration Audits( FCAs) and Physical Configuration Audits (PCAs) * Status of documentation, previous testing, including assessment of metrics on non-conformance/Problem Reports (PRs)/Discrepancy Reports (DRs) |
| **Operational Readiness Review (ORR)** | * Physical Configuration Audit (PCA) results * SA assessment of V&V status and documentation * SA status on safety and security activities * SA assessment of readiness for operations and maintenance * Results of any other audits, assessments, and metrics analysis |
| **Flight Readiness Review (FRR)** | * SA assessment of readiness for flight * Any SA concerns with safety or security * SA sign-offs on certification packages |

See also Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis), [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis), [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing)

## 7.3 Metrics

Software Assurance (SA) metrics are measurable indicators used to evaluate the effectiveness of software development processes, compliance with requirements, progress toward milestones, software quality, and risk management. Metrics provide objective data to ensure oversight, monitor performance, and support continuous improvement throughout the software lifecycle.

Below are SA metrics organized by key areas relevant to Software Assurance responsibilities and compliance with this requirement and other similar lifecycle-focused requirements.

### 7.3.1. Metrics for Milestone Progress and Audit Coverage

#### 7.3.1.1 Milestone Completion Rate

* **Definition**: The percentage of planned software development milestones successfully completed on schedule.
* **Formula**: [ \text{Milestone Completion Rate} = \left( \frac{\text{Completed Milestones}}{\text{Total Planned Milestones}} \right) \times 100 ]
* **Purpose**: Measures adherence to the schedule and highlights delays in milestone achievement.

#### 7.3.1.2 Milestone Deliverable Readiness

* **Definition**: The percentage of required deliverables prepared and reviewed for a milestone prior to the scheduled review date.
* **Formula**: [ \text{Deliverable Readiness} = \left( \frac{\text{Deliverables Reviewed and Approved}}{\text{Total Deliverables Required for Milestone}} \right) \times 100 ]
* **Purpose**: Evaluates whether all necessary deliverables are ready for milestone reviews/audits.

#### 7.3.1.3 Audit Coverage Rate

* **Definition**: The percentage of executed audits/reviews that align with predefined milestones.
* **Formula**: [ \text{Audit Coverage Rate} = \left( \frac{\text{Milestones Audited}}{\text{Total Planned Milestones}} \right) \times 100 ]
* **Purpose**: Tracks whether audits/reviews are properly conducted for each milestone.

### 7.3.2. Metrics for Compliance and Quality

#### 7.3.2.1 Non-Compliance Rates

* **Definition**: The percentage of milestone deliverables, processes, or products flagged for non-compliance during review or audit.
* **Formula**: [ \text{Non-Compliance Rate} = \left( \frac{\text{Non-Compliant Items}}{\text{Total Items Reviewed}} \right) \times 100 ]
* **Purpose**: Tracks deviations from software development requirements, standards, or documented processes, enabling corrective actions.

#### 7.3.2.2 Defect Density

* **Definition**: The number of defects found in deliverables per unit of developed software or documentation.
* **Formula**: [ \text{Defect Density} = \frac{\text{Total Reported Defects}}{\text{Total Units of Code (e.g., KSLOC) or Pages of Documentation}} ]
* **Purpose**: Monitors the quality of software artifacts and documentation, enabling insight into areas needing improvement.

#### 7.3.2.3 Requirements Traceability Coverage

* **Definition**: The percentage of requirements that are appropriately traced to design, code, tests, and deliverables.
* **Formula**: [ \text{Traceability Coverage} = \left( \frac{\text{Tracked Requirements}}{\text{Total Requirements}} \right) \times 100 ]
* **Purpose**: Assesses the completeness of traceability across lifecycle phases.

### 7.3.3. Metrics for Risk Management

#### 7.3.3.1 Risk Closure Rate

* **Definition**: The percentage of identified risks that are resolved before a milestone is completed.
* **Formula**: [ \text{Risk Closure Rate} = \left( \frac{\text{Closed Risks}}{\text{Total Identified Risks}} \right) \times 100 ]
* **Purpose**: Evaluates the project's ability to proactively address risks prior to critical milestone events.

#### 7.3.3.2 Risk-to-Milestone Impact Metric

* **Definition**: The percentage of milestones affected by unresolved risks.
* **Formula**: [ \text{Risk Impact Rate} = \left( \frac{\text{Milestones with Outstanding Risks}}{\text{Total Milestones}} \right) \times 100 ]
* **Purpose**: Identifies milestones potentially delayed by unresolved risks.

#### 7.3.3.3 Risk Severity Reduction

* **Definition**: The percentage reduction in the severity of risks over time.
* **Formula**: [ \text{Severity Reduction} = \left( \frac{\text{Initial Risk Severity - Current Severity}}{\text{Initial Risk Severity}} \right) \times 100 ]
* **Purpose**: Measures progress in mitigating project risks effectively.

### 7.3.4. Metrics for Deliverables and Documentation

#### 7.3.4.1 Deliverable Compliance Rate

* **Definition**: The percentage of deliverables reviewed and meeting the project's compliance criteria.
* **Formula**: [ \text{Deliverable Compliance Rate} = \left( \frac{\text{Compliant Deliverables}}{\text{Total Reviewed Deliverables}} \right) \times 100 ]
* **Purpose**: Evaluates whether deliverables meet requirements and review/test criteria consistently.

#### 7.3.4.2 Documentation Approval Rate

* **Definition**: The percentage of milestone documentation reviewed and formally approved.
* **Formula**: [ \text{Approval Rate} = \left( \frac{\text{Approved Documentation}}{\text{Total Reviewed Documentation}} \right) \times 100 ]
* **Purpose**: Tracks the quality and readiness of documentation submitted for milestone reviews.

### 7.3.5. Metrics for Stakeholder Participation

#### 7.3.5.1 Stakeholder Review Involvement Rate

* **Definition**: The percentage of planned stakeholder reviews conducted for milestones.
* **Formula**: [ \text{Stakeholder Involvement Rate} = \left( \frac{\text{Stakeholder Reviews Completed}}{\text{Total Planned Reviews}} \right) \times 100 ]
* **Purpose**: Ensures all prescribed stakeholder reviews are performed for effective oversight.

#### 7.3.5.2 Stakeholder Review Feedback Rate

* **Definition**: The percentage of items flagged for corrective action during stakeholder reviews.
* **Formula**: [ \text{Feedback Rate} = \left( \frac{\text{Items Flagged by Stakeholders}}{\text{Total Review Items}} \right) \times 100 ]
* **Purpose**: Tracks the level of stakeholder engagement and feedback during milestone reviews.

### 7.3.6. Metrics for Software Progress Monitoring

#### 7.3.6.1 Task Completion Rate

* **Definition**: The percentage of planned software development tasks completed by the milestone review.
* **Formula**: [ \text{Task Completion Rate} = \left( \frac{\text{Completed Tasks}}{\text{Total Planned Tasks}} \right) \times 100 ]
* **Purpose**: Monitors software development progress relative to milestone objectives.

#### 7.3.6.2 Burn-Down Rate (Agile Projects)

* **Definition**: The rate at which remaining tasks or backlog items are completed leading up to a milestone.
* **Formula**: [ \text{Burn-Down Rate} = \left( \frac{\text{Total Items Completed During Milestone}}{\text{Total Items Scheduled}} \right) \times 100 ]
* **Purpose**: Tracks progress for Agile software development cycles.

#### 7.3.6.3 On-Time Status Percentage

* **Definition**: Percentage of milestone tasks completed on or ahead of schedule.
* **Formula**: [ \text{On-Time Status} = \left( \frac{\text{Tasks Completed On Time}}{\text{Total Planned Tasks}} \right) \times 100 ]
* **Purpose**: Measures developer team's adherence to planned schedules for milestone tasks.

### Summary of Metrics

| **Metric Category** | **Example Metrics** | **Purpose** |
| --- | --- | --- |
| **Milestone Progress** | Milestone Completion Rate, Audit Coverage Rate, Deliverable Readiness | Measure milestone adherence and readiness. |
| **Compliance and Quality** | Non-Compliance Rate, Defect Density, Requirements Traceability Coverage | Evaluate product and process quality. |
| **Risk Management** | Risk Closure Rate, Risk Impact Rate, Risk Severity Reduction | Ensure effective risk tracking and mitigation. |
| **Deliverables and Documentation** | Deliverable Compliance Rate, Documentation Approval Rate | Ensure deliverables and documentation meet criteria. |
| **Stakeholder Participation** | Stakeholder Involvement Rate, Review Feedback Rate | Evaluate stakeholder engagement in milestone reviews. |
| **Software Progress Monitoring** | Task Completion Rate, Burn-Down Rate, On-Time Task Status | Monitor software development progress leading to milestones. |

  

By implementing these metrics, Software Assurance personnel can provide actionable insights into milestone readiness, process compliance, stakeholder participation, and risk management. This ensures proactive oversight and supports objective decision-making throughout the software lifecycle.

## 7.4 Guidance

List of tasks for the software development required for the project’s software developers. - look at the software development schedule milestones (see [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews), software products required, and software processes used. Related to the SA tasks on [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination). 

This requirement ensures that the project's software development progress is systematically reviewed and audited at predefined milestones to monitor compliance with software plans, processes, and requirements. These reviews provide opportunities to assess alignment with project lifecycle maturity, technical performance, delivery schedules, and budget constraints. Software Assurance (SA) personnel support this requirement through independent evaluations to verify lifecycle progress, highlight risks, and ensure adherence to standards.

### 7.4.1 Objective of SA

The role of Software Assurance is to ensure proper definition, documentation, and execution of audit and review milestones, including validation of the following aspects:

1. **Milestone Planning**: Ensure that milestone events are documented in the project plans.
2. **Milestone Reviews and Objectives**: Confirm the purpose, review criteria, and expected artifacts for each milestone.
3. **Compliance Oversight**: Assess whether software developer progress aligns with documented plans, processes, and requirements.
4. **Risk Management**: Identify risks or gaps during milestone reviews and ensure corrective actions are implemented.
5. **Stakeholder Involvement**: Ensure that software milestone audits include representation from key stakeholders (e.g., customers, safety teams, and Government representatives).

### 7.4.2 Software Assurance Guidance Tasks

To meet the intent of this requirement, the following Software Assurance tasks and associated activities should be performed:

#### 7.4.2.1. Confirmation of Documented Milestone Definitions

* **SA Task**: **Review and confirm milestones in project documentation.**

  + Ensure the project's **Software Development Plan (SDP)** lists all key milestones for software development and defines them in sufficient detail.
  + Verify that milestones align with lifecycle phases (e.g., requirements, design, implementation, testing, integration, delivery).
  + Confirm the inclusion of software-specific deliverables and review objectives for each milestone **(e.g., completion criteria, exit/entry conditions).**
* **Artifacts to Review**:

  + **Software Development Plan (SDP).**
  + Project Plan and Integrated Master Schedule (IMS).
  + **Milestone Review Plan** or **Terms of Reference** (if provided separately).
  + **Configuration Management Plan** to track milestone artifacts and updates.
* **Key Questions**:

  + Are milestones comprehensive and covering all major points in the software lifecycle?
  + Are milestone objectives documented with measurable success criteria?
  + Are the roles and responsibilities of reviewers (including SA personnel) defined for each milestone?

#### 7.4.2.2. Ensure Milestone Alignment with Reviews and Audits

* **SA Task**: **Validate the types of reviews and audits defined for each milestone.**

  + Confirm that milestone reviews align with software lifecycle standards, such as NASA’s **SAR (Software Assurance Review)** process.
  + Verify the appropriate review types are defined, such as:
    - **Preliminary Design Review (PDR)**.
    - **Critical Design Review (CDR)**.
    - **Test Readiness Review (TRR)**.
    - **System Acceptance Review (SAR)**.
    - Incremental/Agile sprint reviews, if applicable.
  + Ensure plans for audits focus on risk areas and assess software quality processes, product compliance, and technical progress.
* **Artifacts to Review**:

  + List of milestone reviews/audits and their schedules.
  + Criteria for entrance and exit at milestone reviews (documented in review plans or SDP).
  + Checklists or templates used for milestone reviews.
* **Key Questions**:

  + Do review milestones include relevant audit activities for safety, quality, and compliance verification?
  + Are the reviews/audits specific to areas such as requirements traceability, design progress, test readiness, or build integrity?

#### 7.4.2.3. Assess Progress Monitoring Methods

* **SA Task**: **Evaluate how developer progress is tracked leading up to milestones.**

  + Assess whether the project tracks software development progress using:
    - **Development Metrics**: Code size, defect density, test status, etc.
    - **Schedule Milestones**: Task completion rates, burn-down rates (Agile).
    - **Budget Performance Metrics**: Earned Value Management (EVM).
  + Verify the planned use of progress reports and SA checklists/templates to assess entry/exit criteria for reviews.
  + Monitor the accuracy of progress indicators leading up to audits, ensuring they align with predefined performance goals.
* **Artifacts to Review**:

  + Defined progress indicators (metrics) from plans, schedules.
  + Interim reports on developer performance.
  + Risk tracking logs for in-progress tasks/deliverables.
* **Key Questions**:

  + Are clear metrics established for tracking developer progress toward milestones?
  + Are milestone entry and exit reviewed against accurate progress data?

#### 7.4.2.4. Oversight of Milestone Deliverable Readiness

* **SA Task**: **Monitor and confirm that required deliverables are prepared for each milestone.**

  + Validate the readiness of software products provided by developers at each milestone:
    - Prototypes or incremental builds.
    - Requirements or design documents updated from previous milestones.
    - Test results, defect reports, or analyses.
  + Verify bi-directional traceability to ensure deliverables are linked to their requirements and reviews.
* **Artifacts to Review**:

  + Deliverables list with required review artifacts for each milestone.
  + Results of static analysis, testing, or design validation conducted prior to key milestones.
* **Key Questions**:

  + Have the required deliverables for milestone reviews been completed and verified?
  + Are deliverables accurate, up-to-date, and compliant with project requirements?

#### 7.4.2.5. Attend Milestone Reviews/Audits and Generate Reports

* **SA Task**: **Participate in milestone reviews and document SA findings.**

  + Serve as an independent reviewer during all critical milestone events.
  + Use predefined checklists for milestone compliance and record findings, such as:
    - Progress risks (schedule/budget overruns, incomplete deliverables).
    - Deficiencies in software quality, design, or verification results.
    - Post-milestone action items for the development team or SA.
  + Generate Software Assurance reports after audits to summarize observations, risks, non-conformance items, and corrective actions.
* **Artifacts to Review or Provide**:

  + Milestone compliance checklists.
  + SA milestone review/audit reports and recommendations.
  + Status tracking logs for milestone deficiencies and corresponding resolutions.
* **Key Questions**:

  + Was software developer progress verified independently during the milestone review?
  + Did the review address all milestone objectives and corrective actions?

#### 7.4.2.6. Risk Management and Continuous Monitoring

* **SA Task**: **Track risks identified at milestones and ensure follow-up.**

  + Document risks or gaps observed during milestone reviews.
  + Ensure risks are mitigated before the next milestone by monitoring corrective actions or requiring interim risk reviews.
  + Review updates to milestone plans, deliverables, or processes as risks evolve.
* **Artifacts to Review**:

  + Risk tracking logs and mitigation plans.
  + Updated milestone plan (if changes in scope, schedule occur due to risks).
  + Status check against risk closure prior to subsequent milestones.
* **Key Questions**:

  + Were risks from earlier milestones addressed before subsequent reviews?
  + Are updated milestone plans reflective of risk mitigation activities?

### 7.4.3 Objective Evidence of Compliance

| **Category** | **Artifacts/Products Reviewed or Produced** |
| --- | --- |
| **Milestone Definitions** | Defined milestones in Software Development Plan (SDP) and schedule. |
| **Types of Reviews/Audits** | List of milestone review types, objectives, entry/exit criteria templates. |
| **Progress Monitoring** | Development metrics, interim reports, compliance reports on progress. |
| **Deliverable Readiness** | Deliverables list, requirements traceability matrix, validation records. |
| **Milestone Participation** | Milestone compliance checklists, SA milestone reports, status tracking logs. |
| **Risk Management** | Risk tracking logs, status updates, risk review meeting minutes. |

  

### 7.4.4 SA Guidance Summary:

* **Plan Reviews**: Ensure documented milestone definitions align with lifecycle phases and include clear entry/exit criteria.
* **Participate in Reviews**: Confirm developer progress through objective evidence collected at milestone reviews/audits.
* **Deliverable Assessment**: Ensure milestone deliverables are complete, traceable, and validated.
* **Track Progress**: Monitor developer metrics, readiness, and risks leading to milestones.
* **Risk Management**: Document and resolve risks or gaps identified during milestone reviews.

By following this guidance, Software Assurance personnel can support this requirement effectively, ensuring that milestone reviews foster transparency, accountability, and high-quality software development.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination)        * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence is the tangible, factual documentation or artifacts collected to demonstrate compliance with requirements, verify software development processes, assess deliverable quality, and confirm Software Assurance (SA) activities. This evidence is critical for independent oversight, audits, and reviews of the software development lifecycle.

Below is a detailed set of objective evidence categories relevant to Software Assurance and lifecycle oversight, with examples of artifacts related to requirements like this requitement ("Define and document milestones for software developer reviews and audits") and other standards.

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

## 8.1 Evidence for Software Development Planning

### 8.1.1 Software Development Plan (SDP) Review Evidence

* **Artifacts**:
  + Approved **Software Development Plan (SDP)** with clearly defined milestones, lifecycle phases, review schedules, and audit objectives.
  + Change logs showing updates to milestones or schedules during the project lifecycle.
  + Review records or meeting minutes documenting SA input during SDP creation or iteration.
* **Purpose**: Confirms that the milestone definitions, review timelines, and required deliverables are properly documented and aligned with project goals.

### 8.1.2 Configuration Management Plan

* **Artifacts**:
  + Approved plan describing methods for tracking software artifacts, deliverables, and baseline versions across milestones.
  + Configuration control logs showing the history of changes to critical software components and documentation.
* **Purpose**: Ensures proper tracking and versioning of lifecycle artifacts tied to milestones for auditability.

## 8.2 Evidence for Milestone Reviews

### 8.2.1 Milestone Review Records

* **Artifacts**:
  + Milestone review meeting minutes, including attendee lists (SA personnel and other stakeholders).
  + Review presentations summarizing developer progress, deliverables, and open issues.
  + Logs detailing compliance issues raised during reviews and their resolution status.
  + Signed review checklists showing criteria for entry/exit conditions being met.
* **Purpose**: Validates that milestone reviews were conducted as planned, with documented evidence of SA oversight and participation.

### 8.2.2 Milestone Review Assessment Reports

* **Artifacts**:
  + SA reports for key milestones such as Preliminary Design Review (PDR), Critical Design Review (CDR), Test Readiness Review (TRR), and System Acceptance Review (SAR).
  + Audit findings related to milestones that identify risks, non-conformance items, or areas for improvement.
  + Reports summarizing corrective actions taken between milestones to resolve flagged issues.
* **Purpose**: Demonstrates SA verification of developer progress at milestone reviews and audits.

## 8.3 Evidence for Deliverables

### 8.3.1 Deliverable Readiness Records

* **Artifacts**:
  + Deliverable tracking logs showing the completion status of software documentation, code builds, tests, and other required artifacts.
  + Approved deliverables (e.g., source code, test plans, design documents) submitted for review prior to the milestone.
  + Evidence of validation (e.g., test results, static/dynamic code analysis reports).
* **Purpose**: Confirms that required deliverables are prepared, reviewed, and validated for milestone compliance.

### 8.3.2 Requirements Traceability Matrix

* **Artifacts**:
  + Traceability matrix mapping requirements to design elements, code components, verification tests, and deliverables.
  + Peer review records showing SA validation of traceability completeness.
* **Purpose**: Ensures deliverables can be traced back to project requirements for verification.

### 8.3.3 V&V (Verification and Validation) Evidence

* **Artifacts**:
  + Results from verification activities (e.g., unit tests, integrations tests, system tests) tied to milestone deliverables.
  + Validation reports showing software compliance with functional and performance requirements.
  + SA oversight records for V&V tasks (e.g., validation checklists, test execution logs).
* **Purpose**: Confirms that deliverables meet the quality and functional expectations defined for each milestone.

## 8.4 Evidence for Compliance Oversight

### 8.4.1 Compliance Audit Findings

* **Artifacts**:
  + Audit reports detailing SA assessments of processes, deliverables, or artifacts against the project’s adopted standards (e.g., NASA standards, CMMI).
  + Records of non-conformance items flagged during audits and subsequent resolutions.
* **Purpose**: Tracks compliance with lifecycle processes and identifies areas for improvement.

### 8.4.2 Process Maturity Evaluations

* **Artifacts**:
  + SA evaluation logs comparing the software developer's processes to defined best practices (e.g., CMMI V2.0 or organizational-defined standards).
  + Evidence of improvements recommended by SA based on evaluations and follow-up actions taken.
* **Purpose**: Ensures lifecycle process maturity and alignment with prescribed standards.

## 8.5 Evidence for Risk Management

### 8.5.1 Risk Review Records

* **Artifacts**:
  + Risk identification and tracking logs showing potential risks to software development milestones (e.g., schedule, compliance gaps, deliverables).
  + Mitigation plans approved and monitored by SA.
  + Risk closure reports summarizing resolved risks tied to particular milestones.
* **Purpose**: Validates that risks identified during milestone audits or reviews are treated proactively to maintain project alignment.

### 8.5.2 Risk Escalation Reports

* **Artifacts**:
  + SA-provided risk escalation reports identifying systemic or unresolved risks that require management attention.
  + Logs showing the escalation status and communication history between SA personnel and key stakeholders.
* **Purpose**: Provides objective evidence of SA's role in mitigating milestone-related risks.

## 8.6 Evidence for Developer Progress Monitoring

### 8.6.1 Developer Metrics

* **Artifacts**:
  + Metrics reports showing task completion rates, defect density trends, test coverage, and other progress indicators tied to milestones.
  + Earned Value Management (EVM) or burn-down charts documenting milestone progress relative to schedules and budgets.
* **Purpose**: Tracks measurable indicators to verify developer progress and performance.

### 8.6.2 Status Reports

* **Artifacts**:
  + Developer progress reports submitted for SA review summarizing task status, outstanding action items, and risks.
  + SA status reports assessing the alignment of developer progress to defined milestone and review objectives.
* **Purpose**: Confirms that developer progress is aligned with project expectations and tracked by SA.

## 8.7 Evidence for Stakeholder Oversight

### 8.7.1 Stakeholder Review Participation

* **Artifacts**:
  + Attendance records and minutes showing stakeholder involvement in milestone reviews (e.g., customer representatives, Government reviewers).
  + Feedback logs documenting stakeholder concerns or recommendations raised during reviews.
* **Purpose**: Confirms that stakeholders are adequately engaged in oversight of milestone reviews.

### 8.7.2 Feedback Implementation Evidence

* **Artifacts**:
  + Logs showing integration of stakeholder feedback into deliverables or processes.
  + Follow-up review reports tracking the resolution of stakeholder-raised issues before subsequent milestones.
* **Purpose**: Tracks how stakeholder feedback improves the project outcomes.

## 8.8 Evidence for SA Activities

### 8.8.1 Software Assurance Plan Implementation

* **Artifacts**:
  + Approved **Software Assurance Plan** (SAP) defining SA processes, tasks, responsibilities, and metrics specific to the project.
  + Logs showing SA task completion (e.g., milestone review participation, deliverable assessments).
* **Purpose**: Confirms documented SA implementation throughout the project.

### 8.8.2 Metrics Dashboard

* **Artifacts**:
  + SA metrics reports (e.g., compliance rates, defect trends, risk closure rates, milestone audit coverage).
  + Charts or dashboards tracking SA progress against planned activities.
* **Purpose**: Provides objective quantitative evidence of SA effectiveness during the project lifecycle.

### 8.8.3 Milestone Review Checklists

* **Artifacts**:
  + Completed milestone review checklists showing SA assessments of deliverables, progress, compliance, and risks.
* **Purpose**: Confirms SA contributions toward milestone review objectives.

## 8.9 Summary of Objective Evidence

| **Category** | **Example Artifacts** | **Purpose** |
| --- | --- | --- |
| **Development Planning** | SDP (Software Development Plan), change logs, configuration management plans. | Confirm lifecycle milestones and planning for reviews. |
| **Milestone Reviews** | Review records, presentations, assessment reports, audit findings. | Validate milestone readiness and developer progress. |
| **Deliverables** | Deliverable tracking logs, traceability matrix, V&V reports. | Ensure deliverables meet quality, traceability, and compliance criteria. |
| **Compliance Oversight** | Audit findings, process maturity evaluations. | Demonstrate compliance with standards and lifecycle processes. |
| **Risk Management** | Risk tracking logs, mitigation plans, escalation reports. | Monitor risk resolution and proactive mitigation strategies. |
| **Developer Monitoring** | Progress metrics reports, developer status reports, milestone performance dashboards. | Verify developer progress and identify gaps or delays. |
| **Stakeholder Oversight** | Attendance records, feedback logs, implementation evidence. | Confirm effective stakeholder involvement in milestone reviews. |
| **SA Activities** | Software Assurance Plan (SAP), metrics dashboards, review checklists. | Demonstrate SA involvement and oversight throughout the software lifecycle. |

Objective evidence provides transparency, accountability, and traceability, ensuring that all aspects of Software Assurance and lifecycle milestone objectives are effectively monitored and documented.
