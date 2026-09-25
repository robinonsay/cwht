# SWE-018 - Software Activities Review

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695404. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review

SWE-018 - Software Activities Review

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695404)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695404&showCommentArea=true&showComments=true#addcomment)

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

3.3.2 The project manager shall regularly hold reviews of software schedule activities, status, performance metrics, and assessment/analysis results with the project stakeholders and track issues to resolution.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-018 History

SWE-018 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.6 The project shall regularly hold reviews of software activities, status, and results with the project stakeholders and track issues to resolution. |
| Difference between A and B | No change |
| B | 3.3.2 The project manager shall regularly hold reviews of software activities, status, and results with the project stakeholders and track issues to resolution. |
| Difference between B and C | Added metrics and specified "schedule" activities. |
| C | 3.3.2 The project manager shall regularly hold reviews of software schedule activities, metrics, status, and results with the project stakeholders and track issues to resolution. |
| Difference between C and D | Reworded requirement to indicate performance metrics and assessment/analysis results were what was being included in stakeholder reviews |
| D | 3.3.2 The project manager shall regularly hold reviews of software schedule activities, status, performance metrics, and assessment/analysis results with the project stakeholders and track issues to resolution. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

Regular reviews of software status and activities assure that all needed tasks and deliverables are managed and achieved. The technical reviews and assessments are used to monitor the progress of the software technical effort and provide software product status information. A key aspect of the technical assessment process is the conduct of life cycle and technical reviews throughout the software life cycle. These reviews provide a periodic assessment of the program's or project's software technical and progress status and health at key points in the life cycle.

The practice of holding regular reviews of software schedule activities, performance metrics, and assessment/analysis results is vital to ensuring that software development remains on track, risks are managed effectively, and challenges are addressed promptly. This requirement not only reinforces alignment with broader project goals but also creates a culture of accountability, collaboration, and transparency—contributing directly to the success of NASA's missions.

Regular reviews of software schedule activities with project stakeholders ensure that the development process remains aligned with the project's goals, schedule, and overall mission success. Stakeholder engagement at regular intervals helps maintain transparency, identify issues early, and foster collaboration necessary for timely resolution of challenges. Here's why this requirement is crucial:

## 2.1 Alignment With Project Goals

* **Why It's Important**: Software development activities are just one component of the broader project/system. Regular reviews ensure that software progress is in sync with the overall project requirements, milestones, and deliverables, avoiding misalignments and minimizing the risk of delays.
* **How It Helps**: By continuously verifying alignment, the project manager ensures that software work products are completed when required for integration, testing, and operational readiness.

## 2.2 Early Identification of Risks and Issues

* **Why It's Important**: Software development schedules are subject to uncertainties, such as changes in requirements, resource limitations, or technical complexities. If risks or delays are not identified promptly, they can cascade into larger project-level obstacles.
* **How It Helps**: Incorporating regular reviews creates an opportunity to discuss current issues, track pending action items, and mitigate risks before they impact critical paths or downstream activities.

## 2.3 Improved Decision-Making Through Assessment Metrics

* **Why It's Important**: Performance metrics (e.g., adherence to schedule, cost, resource utilization, and quality) provide data-driven insights into the project's progress and challenges. Without these metrics, decisions may rely on incomplete or outdated information.
* **How It Helps**: Regular assessment and analysis of metrics during reviews enable the project manager and stakeholders to make informed decisions about reallocating resources, adjusting timelines, modifying requirements, or addressing inefficiencies.

## 2.4 Stakeholder Engagement and Accountability

* **Why It's Important**: Stakeholders, such as technical leads, system engineers, and program managers, bring diverse expertise and perspectives that are critical for reviewing and addressing issues. Regular reviews also ensure accountability by requiring project participants to demonstrate progress and resolve problems.
* **How It Helps**: Engaging stakeholders fosters collective responsibility for the schedule and ensures that everyone is informed about progress, risks, and the path forward. This helps build trust and encourages collaborative problem-solving across disciplines.

## 2.5 Monitoring of Critical Dependencies

* **Why It's Important**: Software schedules often involve dependencies on other components like hardware, testing environments, and external tools or teams. Regular reviews provide a mechanism to monitor these dependencies and address potential bottlenecks.
* **How It Helps**: Ensuring that dependencies are being met and addressing delays from external or internal sources improves the overall project's coordination and efficiency.

## 2.6 Effective Tracking and Resolution of Issues

* **Why It's Important**: Unresolved issues can accumulate and derail project timelines. Regular reviews provide a platform for tracking these issues, assigning action items, and holding individuals accountable for resolving them.
* **How It Helps**: By ensuring that issues are actively managed and closed out, the project manager keeps the team focused on completing tasks in a timely manner and avoids the impact of unresolved problems on future activities.

## 2.7 Enhanced Transparency and Communication

* **Why It's Important**: Clear and consistent communication of progress, risks, changes, and decisions is crucial for project success, especially when coordinating across multiple teams or stakeholders. Lack of transparency can lead to misunderstandings, misaligned priorities, and delayed decision-making.
* **How It Helps**: Regular reviews foster communication and ensure that everyone involved in the project has a shared understanding of the current status, upcoming tasks, and risks, reducing misunderstandings and improving collaboration.

## 2.8  Adherence to NASA Standards and Best Practices

* **Why It's Important**: Regular reviews are consistent with NASA's emphasis on systems integration, mission assurance, and risk management. Reviews provide structured opportunities to verify compliance with NASA project management requirements (NPRs) and software engineering best practices.
* **How It Helps**: Structured reviews demonstrate adherence to NASA's established standards for accountability, transparency, and risk management, while reinforcing a culture of rigor and discipline in project execution.

## 2.9 Summary of Key Benefits

* **Proactive Risk Mitigation**: Identify and mitigate risks early to avoid cascading impacts.
* **Enhanced Schedule Performance**: Maintain alignment with project milestones and critical paths.
* **Data-Driven Decisions**: Use metrics to ensure informed decision-making.
* **Improved Collaboration**: Enhance stakeholder engagement and interdisciplinary coordination.
* **Accountability and Transparency**: Foster clarity by regularly addressing issues and progress.

# 3. Guidance

Life cycle reviews are critical events for ensuring the health, maturity, and alignment of a project’s technical and programmatic baselines throughout the software development life cycle. These reviews provide opportunities for structured evaluations, transparent communication, and proactive risk management, enabling projects to maintain alignment with goals and requirements while mitigating risks early. Below is enhanced guidance to clarify the process, focus, and best practices for performing regular life cycle reviews.

Regular life cycle reviews are foundational to ensuring software development remains aligned with technical and project goals. By tailoring review frequency and content to project phase and maturity, leveraging metrics and risk management tools, engaging appropriate stakeholders, and tracking issues to resolution, project teams can successfully monitor progress, mitigate risks, and make informed decisions to navigate challenges effectively. Adopting structured review practices enhances transparency, accountability, and technical rigor, driving mission success.

## 3.1 Perform Regular Life Cycle Reviews

#### **Purpose of Life Cycle Reviews**

Life cycle reviews are event-driven evaluations of a project’s progress, readiness, and adherence to requirements. They are conducted based on technical maturity and entrance criteria rather than arbitrary calendar milestones. Reviews ensure the project has met predefined objectives and can proceed confidently to the next phase of development while maintaining alignment with governing requirements, Center practices, and project needs.

#### **Key Considerations:**

1. **Review Frequency**:

   * Life cycle reviews should be scheduled according to the maturity of the technical baseline, not strictly on a periodic timeline (e.g., quarterly or annually). For example:
     + Major milestone reviews (e.g., Preliminary Design Review [PDR], Critical Design Review [CDR]) occur when entrance criteria are satisfied.
     + Interim reviews (e.g., weekly, monthly, or phase-specific reviews) occur depending on the size, scope, and complexity of the project.
   * Frequency and content should reflect the software classification (see SWE-020) and safety criticality determination processes (NASA-STD-8739.8 [278](#_tabs-<p></p>) ).
2. **Planning Life Cycle and Technical Reviews**:

   * The software and project management technical teams collaborate to document and plan review schedules, ensuring alignment with software project planning processes and milestones.
   * Review schedules are documented in project planning documents, such as the Software Development/Management Plan (SDP/SMP), and integrated into the overall project timeline.
   * NASA Center procedures should take precedence. *See Topic [7.08 - Maturity of Life Cycle Products at Milestone](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews)*  for guidance on maturity expectations during reviews.
3. **Guidance Source**:

   * The review process builds upon requirements from NPR 7150.2 [083](#_tabs-<p></p>) , NPR 7123.1 [041](#_tabs-<p></p>) , NPR 7120.5 [082](#_tabs-<p></p>) , NPR 7120.7 [264](#_tabs-<p></p>) , NPR 7120.8 [269](#_tabs-<p></p>) , and individual Center procedures, ensuring compliance with NASA’s standards and best practices.

## 3.2 Work Covered in a Review

#### **Content of Regular Software Reviews**

Software reviews assess the maturity and progress of various aspects of software development based on the current phase of the life cycle. Content includes:

1. **Software Development Tasks**:

   * Planning, requirements development, architecture, detailed design, coding, integration, testing plans, and testing results.
   * Progress against key deliverables and evidence of readiness for system integration or flight.
2. **Major Technical Milestone Reviews**:

   * Provide evidence for achieving entrance and exit criteria, such as satisfaction of specific project objectives, requirements validation, or technical readiness.
   * See [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) for review criteria examples.

#### **Customization to Project Needs**:

Each review should address the specific goals and outputs of the current life cycle phase. Projects should tailor review content to meet unique project needs, while reflecting safety criticality, classification, and other applicable guidelines such as [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones).

## 3.3 Metrics and Risk Management in Reviews

#### **Use of Metrics to Measure Progress**

Reviews leverage quantitative metrics to assess progress, identify bottlenecks, and manage performance effectively. Metrics can be drawn from the software measurement process, including:

1. **Performance Metrics**:
   * Adherence to schedule, milestone completion rates, resource utilization, defect rates, and testing results.
   * Metrics provide data-driven insights into current progress and future risks.
   * **Reference**: [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository), [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data), [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data), and [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis).

#### **Risk and Problem Management**:

1. **Tracking Known Risks**:
   * Reviews include updates on ongoing risk mitigation efforts and emerging risks identified in development.
   * Use continuous risk management tools (see [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)) for tracking and resolving risks systematically.
2. **Problem Identification and Resolution**:
   * Identify and resolve issues in testing, design, or integration, ensuring they are tracked effectively until closure.

## 3.4 Issue Tracking During Reviews

#### **Process for Issue Tracking**

Issues identified during reviews that cannot be resolved immediately are documented and tracked to closure. Use appropriate tools based on project needs and configuration management practices:

1. **Tracking Methods**:

   * Issues may be tracked using a risk management system, problem reporting and corrective action (PRACA) systems, or configuration management tools.
   * Ensure tracking processes are consistent with the project’s Configuration Management Plan ( [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan)).
2. **Disposition and Closure**:

   * Assign clear ownership and timelines for resolving each issue.
   * Regularly review progress on issue resolution during subsequent reviews.

## 3.5 Stakeholders

#### **Who Participates in Reviews?**

Stakeholders are individuals or groups materially affected by the project's outcomes and who play an active role in development and decision-making. They include:

1. **Internal Stakeholders**:

   * Quality assurance, systems engineering, operations, independent verification and validation (IV&V), independent testing teams, and software assurance professionals.
   * Project management and engineering team members.
2. **External Stakeholders**:

   * External stakeholders (e.g., principal investigators, science/education communities, Mission Directorate sponsors) typically participate in formal milestone reviews (e.g., **PDR**, **CDR**) rather than internal reviews.

#### **Best Practices for Stakeholder Involvement**:

1. **Targeted Invitations**:
   * Determine and invite only relevant stakeholders to each review. Stakeholders should have a vested interest in the work products or be engaged in the development effort.
2. **Communication of Outcomes**:
   * Ensure stakeholders are informed through regular updates on progress, risks, and resolutions for transparency and advocacy of the project’s goals.

## 3.6 Decision Points and Technical Maturity

#### **Key Decision Points (KDPs)**

Progress between life cycle phases is marked by KDPs, during which technical and management teams evaluate:

1. **Technical Maturity**:
   * Assess whether the technical development has progressed as planned and is ready for the next phase.
2. **Resource Sufficiency**:
   * Evaluate staffing and funding adequacy to support the current and next phases of development.
3. **Internal Factors**:
   * Examine technical issues, risks, and changes in stakeholder expectations.

#### **Example Review Goals**:

* Ensure resources align with technical and non-technical needs.
* Confirm readiness for system integration or operational deployment.
* Monitor whether stakeholder expectations have shifted, impacting the project.

## 3.7 Additional Guidance

Additional guidance related to holding a review of software activities, status, and results may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting) |

# 4. Small Projects

Software projects vary significantly in size, complexity, classification, and risk level, and as such, the frequency and scope of life cycle reviews should be appropriately tailored to meet project-specific needs. While this requirement applies to all projects, small projects with lower risks may justify less frequent reviews depending on their software classification (see [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)) and an assessment of risk to the overall program or mission.

Small projects must strike a balance between rigorous oversight and maintaining streamlined processes. By tailoring review frequency to software classification, risk levels, and specific project constraints, teams can reduce overhead while addressing critical risks and achieving timely progress. The guidance provided by [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) and Center-specific procedures serves as valuable tools to ensure reviews support the project's health and mission success without imposing unnecessary complexity. Periodic evaluation of classification and risk enhances flexibility, ensuring the review schedule adapts to changing project realities.

## 4.1 Determining Review Frequency

The frequency of reviews for small projects can be adjusted based on an evaluation of:

1. **Software Classification**:

   * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) categorizes software into classes based on their contribution to mission success and impact on safety.
   * A lower classification level (e.g., non-critical or minimal operational impact) may justify reduced review frequency for small projects.
2. **Risk Level**:

   * Assess the risk posed by the software to mission outcomes, safety, cost, and schedule. If the risk is deemed low, less frequent reviews may be sufficient.
   * Perform periodic evaluations of both the software classification and risk level during the project lifecycle. Such evaluations may either validate reduced review frequency or identify the need to increase reviews.
3. **Project Size and Complexity**:

   * Projects with fewer deliverables, simple designs, and short timelines (e.g., prototypes or small R&D efforts) may not require the same review cadence as higher-complexity, critical systems.

## 4.2 Importance of Flexibility

While general guidance exists, small projects must maintain flexibility in their review schedule to remain responsive to changing conditions. Factors prompting adjustments include:

* An increase in risk due to evolving dependencies or requirements.
* External factors or integration needs with larger systems, which may necessitate tighter review oversight.
* Changes in stakeholder expectations or priority shifts.

## 4.3 Guidance and Tools for Small Projects

#### **NASA Approved Guidance**

NASA's [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) provides a helpful chart summarizing maturity guidance for software engineering life cycle products at various reviews. The highlights include:

* Recommended maturity levels of deliverables at life cycle stages.
* Examples of criteria to evaluate readiness for integration or transition.

This chart is intended as general guidance only. Projects should defer to the applicable **NASA Center procedures**, which take precedence for tailoring reviews to Center-specific processes and standards.

## 4.4 Best Practices for Small Project Reviews

1. **Tailored Review Frequency**:

   * Schedule reviews strategically based on key project milestones rather than strictly following periodic calendar intervals.
   * Consider holding reviews at critical points in the software lifecycle, such as before moving from design to coding or from testing to integration.
2. **Focus on Risk and Impact**:

   * For small projects, reviews should focus on factors that could pose significant risks to successful project outcomes, such as technical integration challenges, unresolved design issues, or dependencies.
   * Use [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) risk classification and safety criteria to prioritize reviews effectively.
3. **Clarity and Simplicity**:

   * Keep reviews straightforward by limiting content to core areas, such as milestone progress, readiness for transition to the next phase, and risk updates.
   * Avoid unnecessary overhead; emphasize transparency and actionable outcomes.
4. **Periodic Risk Reevaluation**:

   * Regularly reassess whether the project’s classification or risk profile has changed as technical maturity progresses. These updates inform whether review frequency should be increased or decreased.
5. **Leverage Guidance from 7.08**:

   * Use the chart provided in [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) as reference for expected deliverable maturity at each review stage, ensuring compliance with broader NASA standards.

## 4.5 Implementation for Small Projects

Small projects should consider creating a lightweight "review plan" that outlines:

* The project’s classification and risk level as determined by [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification).
* Proposed review frequency and rationale for adjustments based on classification or risk assessments.
* Review scope, focusing on milestone progress, readiness evaluations, and risk mitigation.
* Use of the *7.08 Maturity of Life Cycle Products* chart and alignment with NASA Center procedures.

This plan can be incorporated into the Software Development/Management Plan (SDP/SMP) or similar planning documents. See Topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan).

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

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
* (SWEREF-261)

  [NASA Governance and Strategic Management Handbook,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=0C "Click to open in new window")

  NPD 1000.0C, NASA Governance and Strategic Management Handbook, Effective Date: January 29, 2020, Expiration Date: January 29, 2025
* (SWEREF-264)

  [NASA Information Technology Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=7A "Click to open in new window")

  NPR 7120.7A, Office of the Chief Information Officer, Effective Date: August 17, 2020,
  Expiration Date: August 17, 2025
  .
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-509)

  [Informal Design Reviews Add Value to Formal Design Review Processes (1996)](https://llis.nasa.gov/lesson/582 "Click to open in new window")

  Public Lessons Learned Entry: 582.
* (SWEREF-539)

  [Aero-Space Technology/X-34 In-Flight Separation from L-1011 Carrier](https://llis.nasa.gov/lesson/1122 "Click to open in new window")

  Public Lessons Learned Entry: 1122.
* (SWEREF-547)

  [Project Management: Integrating and Managing Reviews](https://llis.nasa.gov/lesson/1281 "Click to open in new window")

  Public Lessons Learned Entry: 1281.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains the following lessons learned related to or applicable to the software reviews:

* **Aero-Space Technology/X-34 In-Flight Separation from L-1011 Carrier, Lesson Number 1122[539](#_tabs-<p></p>):** The following entry in the lesson learned database, among other things, points to a concern for holding an adequate software review of validation activities to reduce risk on a particular part of the X-34 mission. "The X-34 technology demonstrator program faces safety risks related to the vehicle's separation from the L-1011 carrier aircraft and to the validation of flight software. Moreover, safety functions seem to be distributed among the numerous contractors, subcontractors, and NASA without a clear definition of roles and responsibilities." The recommendation is that "NASA should review and assure that adequate attention is focused on the potentially dangerous flight separation maneuver, the thorough and proper validation of flight software, and the pinpointing and integration of safety responsibilities in the X-34 program.".
* **Informal Design Reviews Add Value to Formal Design Review Processes (1996), Lesson Number 0582[509](#_tabs-<p></p>):** "A JPL study of in-flight problems on Voyager I and II, Magellan, and Galileo (up to late 1993) revealed that 40% of the problems would likely have been identified by better technical penetration in reviews of the detailed designs performed well before launch. An additional 40% (for a total of 80%) might also have been found by similarly in-depth reviews." Also, "Since formal reviews emphasize verification of the project status and attainment of milestones, their chief benefit lies in the investigative work performed in preparation for the review. In contrast, informal reviews feature detailed value-added engineering analysis, problem-solving, and peer review.".
* **Project Management: Integrating and Managing Reviews, Lesson Number 1281[547](#_tabs-<p></p>):** This lesson learned discusses some caveats to running reviews. "The Project underwent several reviews throughout its life cycle. In general, these reviews helped the Project maintain its course and manage its resources effectively and efficiently. However, at times these review groups would provide the Project with recommendations that were inconsistent with the Project's requirements. For example, these recommendations included the recommendations of other review teams and past recommendations of their team. The result was that the Project had to expend resources trying to resolve these conflicts or continually redraft its objectives." The Recommendation is that "Projects should develop and maintain a matrix of all the reviews they undergo. This matrix should have information such as the review team roster, their scope, and a record of all their recommendations. Before each review, this matrix should be given to the review team's chairperson so that the outcome of the review remains consistent and compatible with the Project's requirements. Senior Management should be represented at these reviews so that discrepancies between the review team and the Project can be resolved immediately.".

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Software/Operations needs a voice at the Project mission level](https://software.gsfc.nasa.gov/lesson-details/1/). **Lesson Number 1**: The recommendation states: "Software/Operations needs a voice at the Project mission level. Software/Operations knowledgeable senior managers, with (budget) authority and responsibility for the efforts, is a major key to success."
* [Pressing software schedule and staffing plans too hard](https://software.gsfc.nasa.gov/lesson-details/5/). **Lesson Number 5**: The recommendation states: "Beware of pressing software schedule and staffing plans too hard to help meet competitive cost caps."
* [Drive issues up through both the Engineering and Projects management chains](https://software.gsfc.nasa.gov/lesson-details/6/). **Lesson Number 6**: The recommendation states: "Drive issues up through both the Engineering and Projects management chains."
* [Project schedules and commitments should be evaluated after any significant events](https://software.gsfc.nasa.gov/lesson-details/62/). **Lesson Number 62**: The recommendation states: "Project schedules and commitments should be evaluated after any significant events."
* [All stakeholders should be aware of the project plan and schedule](https://software.gsfc.nasa.gov/lesson-details/63/). **Lesson Number 63**: The recommendation states: "All stakeholders should be aware of the project plan and schedule."
* [Integrated project schedules, with dependencies, ensure the proper sequencing of deliverables](https://software.gsfc.nasa.gov/lesson-details/67/). **Lesson Number 67**: The recommendation states: "Integrated project schedules, with dependencies, ensure the proper sequencing of deliverables."
* [If a program undergoes a change in structure, consider a re-baselining of project documents](https://software.gsfc.nasa.gov/lesson-details/70/). **Lesson Number 70**: The recommendation states: "If a program undergoes a change in structure (such as a contracted effort coming back in-house), consider a re-baselining of project documents (project plans, requirements) and technical approach."
* [Embed FSW team members into custom hardware development efforts](https://software.gsfc.nasa.gov/lesson-details/74/). **Lesson Number 74**: The recommendation states: "Embed FSW team members into custom hardware development efforts."
* [Include sustaining engineers early in the life cycle](https://software.gsfc.nasa.gov/lesson-details/78/). **Lesson Number 78**: The recommendation states: "Include sustaining engineers early in the life cycle (for example, during build testing). This can be particularly beneficial to lower class missions."
* [Projects should work with the Space Network (SN)](https://software.gsfc.nasa.gov/lesson-details/83/). **Lesson Number 83**: The recommendation states: "Projects should work with the Space Network (SN) to understand and consider the mission's (and other SN customer's) operational constraints."
* [Ensure that the impacts of design decisions are clearly communicated](https://software.gsfc.nasa.gov/lesson-details/109/). **Lesson Number 109**: The recommendation states: "When Flight Software provides inputs to design decisions, ensure that the impacts of design decisions are clearly communicated."
* [Gather lessons learned throughout the project life cycle](https://software.gsfc.nasa.gov/lesson-details/110/). **Lesson Number 110**: The recommendation states: "Gather lessons learned throughout the project life cycle."
* [Take advantage of the Space Physics Data Facility](https://software.gsfc.nasa.gov/lesson-details/117/). **Lesson Number 117**: The recommendation states: "Take advantage of the Space Physics Data Facility (SPDF). Engage with the SPDF early in the project and sustain that engagement throughout development."
* [Work with NASA Integrated Services Network (NISN) early](https://software.gsfc.nasa.gov/lesson-details/137/). **Lesson Number 137**: The recommendation states: "Work with the NASA Integrated Services Network (NISN) early to ensure data and voice circuit implementation is planned and executed according to agreed upon commitments."
* [Assess status independently based on artifacts, not on reported status](https://software.gsfc.nasa.gov/lesson-details/141/). **Lesson Number 141**: The recommendation states: "Assess status independently based on artifacts, not on reported status."
* [End-to-End Testing through satellite I&T](https://software.gsfc.nasa.gov/lesson-details/172/). **Lesson Number 172**: The recommendation states: "End-to-End Testing should be planned for smaller events spread out through satellite (i.e., spacecraft with integrated payload/science instruments) I&T."
* [Each mission partner should identify a single assignee in the project management office](https://software.gsfc.nasa.gov/lesson-details/174/). **Lesson Number 174**: The recommendation states: "All stakeholders in end-to-end system testing should identify a person in their project management office responsible for the success of the end-to-end testing. These assignees should be at the proper level to assign resources and prioritize work of engineers, if necessary."
* [Involving dedicated V&V team earlier is effective](https://software.gsfc.nasa.gov/lesson-details/286/). **Lesson Number 286**: The recommendation states: "If the project has a dedicated V&V team,  this team should get involved earlier, rather than waiting until developers make the software available to V&V for the start of the “formal” build testing. Overlapping development and V&V leads to reduced build testing time at the completion of build development, in favor of additional development time. Moreover, developers will get earlier feedback about defects and can address them as they are uncovered."
* [Integrated Simulator Development](https://software.gsfc.nasa.gov/lesson-details/320/). **Lesson Number 320**: The recommendation states: "Organize software simulators as an integrated effort supporting Flight Software, I&T, Operations, and any subsystems which require simulators for development.  Hire a Simulators lead with sufficient time to prepare for PDR. Ensure open communication between all teams who are developing simulation capabilities."
* [Key Paths Schedule Visualization for Ground / Operations Readiness](https://software.gsfc.nasa.gov/lesson-details/322/). **Lesson Number 322**: The recommendation states: "Track multiple key dependency paths in top-level schedule visually."
* [Close Collaboration between Geographically Separated Operations Teams](https://software.gsfc.nasa.gov/lesson-details/323/). **Lesson Number 323**: The recommendation states: "Acknowledge that internal/external or "us"/"them" distinctions are natural and unavoidable for large projects. Promote a mindset of communicating with geographically distant operations partners even more closely than non-operations project components at GSFC."
* [Use Risk and Schedule for communicating “up the chain”](https://software.gsfc.nasa.gov/lesson-details/326/). **Lesson Number 326**: The recommendation states: "Use quantitative tools (risk and schedule) for communicating, in addition to qualitative status reports."
* [Communicate directly about bad news](https://software.gsfc.nasa.gov/lesson-details/327/). **Lesson Number 327**: The recommendation states: "Communicate promptly and directly with project and line management, especially on problems."
* [Carefully consider team organization structure during planning](https://software.gsfc.nasa.gov/lesson-details/335/). **Lesson Number 335**: The recommendation states: "Ensure that team structure provides clear lines of responsibility and sufficient avenues for communication."

# 7. Software Assurance

**SWE-018 - Software Activities Review**

3.3.2 The project manager shall regularly hold reviews of software schedule activities, status, performance metrics, and assessment/analysis results with the project stakeholders and track issues to resolution.

Software assurance activities for this requirement ensure regular and effective reviews of the software schedule’s performance, status, and risks, while supporting the tracking and resolution of issues. Through preparation, validation of metrics, risk analysis, facilitation of reviews, and issue tracking, assurance activities provide independent oversight and enforce accountability for schedule management. Proper execution of these activities helps ensure mission success and compliance with NASA standards.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm the generation and distribution of periodic reports on software schedule activities, metrics, and status, including reports of software assurance and software safety schedule activities, metrics, and status.

2. Confirm closure of any project software schedule issues.

## 7.2 Software Assurance Products

Lists of the non-conformances found during reviews with their corrective action status. See tab 8.

## 7.3 Metrics

To satisfy this requirement, project reviews must encompass meaningful metrics that highlight schedule progress, risks, performance, and issue resolution to enable stakeholders to assess project health and make informed decisions. Below are **good metrics** tailored to this requirement, organized by category to align with its main focus areas.

### 7.3.1 Schedule Performance Metrics

#### 7.3.1.1 Schedule Compliance Rate

* **Definition**: Percentage of tasks completed on or before their planned end dates.
* **Purpose**: Evaluates adherence to the software schedule and its milestones during development.
* **Formula**:

  ```
  Schedule Compliance (%) = (Number of Tasks Completed on Time / Total Number of Tasks Completed) × 100
  ```
* **Interpretation**:
  + **Higher percentage** indicates better schedule adherence.
  + **Lower percentage** signals delays requiring attention.
* **Acceptance Criteria**: ≥90% compliance is generally desirable.

#### 7.3.1.2 Schedule Variance (SV)

* **Definition**: The difference between the planned work (BCWS) and the work completed to-date (BCWP).
* **Purpose**: Indicates whether the project is ahead of schedule, on schedule, or behind schedule.
* **Formula**:

  ```
  SV = BCWP - BCWS
  ```

  + BCWP = Budgeted Cost of Work Performed (reflects completed work).
  + BCWS = Budgeted Cost of Work Scheduled (reflects planned work).
* **Interpretation**:

  + **Positive SV**: Ahead of schedule.
  + **Negative SV**: Behind schedule.
  + **SV = 0**: On schedule.
* **Acceptance Criteria**:

  + SV close to **0** or positive values is ideal.

#### 7.3.1.3 Schedule Performance Index (SPI)

* **Definition**: A ratio describing how efficiently planned activities are being completed relative to the schedule.
* **Purpose**: Helps measure progress against the original schedule plan.
* **Formula**:

  ```
  SPI = BCWP / BCWS
  ```
* **Interpretation**:
  + **SPI ≥ 1.0**: Work is being completed at or faster than the planned rate.
  + **SPI < 1.0**: Schedule is off track, and delays may occur.
* **Acceptance Criteria**: SPI ≥ 1.0 is desired.

#### 7.3.1.4 Milestone Completion Rate

* **Definition**: The percentage of scheduled milestones achieved within their planned timeframes.
* **Purpose**: Tracks progress toward high-level project and software milestones.
* **Formula**:

  ```
  Milestone Completion Rate (%) = (Number of Milestones Completed On Time / Total Scheduled Milestones) × 100
  ```
* **Interpretation**:
  + **Higher percentage** signals adherence to major deliverables.
  + **Lower percentage** points to delays requiring corrective action.
* **Acceptance Criteria**: ≥90% milestone completion rate is generally desirable.

### 7.3.2 Issue Tracking Metrics

#### 7.3.2.1 Resolution Rate for Review-Identified Issues

* **Definition**: The percentage of issues identified during reviews that have been resolved within the agreed timeframe.
* **Purpose**: Ensures that issues raised during schedule reviews are tracked and closed in a timely manner.
* **Formula**:

  ```
  Resolution Rate (%) = (Number of Resolved Issues / Total Number of Identified Issues) × 100
  ```
* **Interpretation**:
  + **Higher percentage** indicates effective issue tracking and resolution processes.
  + **Lower percentage** may signal bottlenecks in addressing schedule-related concerns.
* **Acceptance Criteria**: ≥90% resolution rate to ensure timely mitigation.

#### 7.3.2.2 Issue Aging

* **Definition**: Tracks the average amount of time unresolved issues remain open since their identification.
* **Purpose**: Highlights lingering issues that could impact project execution.
* **Formula**:

  ```
  Issue Aging = Total Duration of Open Issues / Number of Open Issues
  ```
* **Interpretation**:
  + Longer average aging time indicates delayed issue resolution, potentially affecting project timelines.
* **Acceptance Criteria**:
  + Threshold duration depends on issue criticality, but shorter aging periods are preferable for critical issues.

#### 7.3.2.3 Stakeholder Escalation Rate

* **Definition**: Percentage of issues escalated to higher-level stakeholders for resolution due to non-resolution at the project level.
* **Purpose**: Identifies recurring challenges that require external intervention to maintain schedule adherence.
* **Formula**:

  ```
  Stakeholder Escalation Rate (%) = (Number of Escalated Issues / Total Identified Issues) × 100
  ```
* **Interpretation**:
  + **Higher percentage** may indicate recurring schedule-related risks or inefficiencies in issue resolution processes.
* **Acceptance Criteria**: <10% escalation rate is ideal, with a focus on minimizing unresolved issues.

### 7.3.3 Risk Management Metrics

#### 7.3.3.1 Percentage of Critical Path Delays

* **Definition**: Percentage of activities on the critical path that are delayed beyond their planned durations.
* **Purpose**: Monitors delays on tasks that could impact overall project delivery timelines.
* **Formula**:

  ```
  Critical Path Delay Rate (%) = (Number of Delayed Critical Path Tasks / Total Critical Path Tasks) × 100
  ```
* **Interpretation**:
  + **Higher percentage** indicates risks to achieving schedule milestones.
  + **Lower percentage** aligns with successful execution of the critical path.
* **Acceptance Criteria**: ≤5% delay rate is desired (threshold varies by project risk level).

#### 7.3.3.2 Risk Resolution Rate

* **Definition**: Tracks the percentage of identified risks that have been mitigated or closed within the review period.
* **Purpose**: Assesses effectiveness of risk identification and mitigation efforts as part of the review process.
* **Formula**:

  ```
  Risk Resolution Rate (%) = (Number of Resolved Risks / Total Identified Risks) × 100
  ```
* **Interpretation**:
  + **Higher percentage** demonstrates proactive risk management supporting schedule adherence.
* **Acceptance Criteria**: ≥80–90% resolution rate is generally desired.

### 7.3.4. Stakeholder Engagement Metrics

#### 7.3.4.1 Review Participation Rate

* **Definition**: Measures the percentage of invited stakeholders who actively participate in schedule reviews.
* **Purpose**: Ensures engagement of all critical stakeholders in review discussions.
* **Formula**:

  ```
  Review Participation Rate (%) = (Number of Stakeholders Attending / Number of Invited Stakeholders) × 100
  ```
* **Interpretation**:
  + **Higher participation rate** ensures that decisions are informed by all relevant stakeholders.
  + **Lower participation rate** may lead to gaps in representation or slower resolution of issues requiring higher-level input.
* **Acceptance Criteria**: ≥95% is ideal.

#### 7.3.4.2 Review Feedback Implementation Rate

* **Definition**: Tracks the percentage of actionable stakeholder feedback incorporated into subsequent schedule updates.
* **Purpose**: Ensures stakeholder concerns and insights directly shape improvements to scheduling and issue resolution processes.
* **Formula**:

  ```
  Feedback Implementation Rate (%) = (Stakeholder Feedback Addressed / Total Feedback Provided) × 100
  ```
* **Interpretation**:
  + **Higher percentage** demonstrates responsiveness to stakeholder engagement and iterative review improvements.
* **Acceptance Criteria**: ≥90% feedback implementation rate is preferred.

### 7.3.5 Summary of Metrics

| **Category** | **Metric** | **Purpose** |
| --- | --- | --- |
| **Schedule Performance** | Schedule Compliance Rate | Task adherence to planned timelines. |
|  | Schedule Variance (SV) | Planned vs. completed work. |
|  | Schedule Performance Index (SPI) | Efficiency in schedule execution. |
|  | Milestone Completion Rate | Progress toward key software milestones. |
| **Issue Tracking** | Resolution Rate for Identified Issues | Timely closure of issues identified in reviews. |
|  | Issue Aging | Average time for issue resolution. |
|  | Stakeholder Escalation Rate | Level of unresolved issues needing escalation. |
| **Risk Management** | Percentage of Critical Path Delays | Delays impacting overall project delivery. |
|  | Risk Resolution Rate | Effectiveness in mitigating schedule risks. |
| **Stakeholder Engagement** | Review Participation Rate | Stakeholder engagement in reviews. |
|  | Feedback Implementation Rate | Responsiveness to stakeholder inputs. |

### **Recommendations**

* **Tailoring Metrics**: Select metrics based on the project's complexity and criticality. For small projects, focus on a few core metrics like Schedule Compliance, SPI, and Issue Resolution Rate.
* **Automating Reports**: Use project management tools that can automatically calculate metrics (e.g., earned value tools, schedule tracking platforms) for efficient tracking and updates.
* **Prioritize Actionable Insights**: Metrics should drive meaningful corrective actions, risk mitigations, or stakeholder decisions rather than simply reporting data.

These metrics ensure the project's software schedule activities, status, and performance metrics are regularly reviewed and transparently assessed, providing the shared accountability necessary for mission success.

* Deviations of actual schedule progress vs. planned schedule progress above defined threshold
* # of open versus # of closed issues over time and latency.  See metrics in [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking)
* The trend of change status over time (# of changes approved, # in implementation, # in test, # closed)

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

Software assurance (SA) plays a critical role in supporting, verifying, and validating compliance with this requirement to ensure effective schedule management, issue resolution, and stakeholder engagement. Below is a detailed list of software assurance activities tailored to this requirement.

### 7.4.1 Preparation for Software Schedule Reviews

Software assurance must ensure that all necessary inputs, artifacts, and metrics are prepared and reviewed before stakeholder meetings to maximize review effectiveness.

#### **Activities:**

1. **Review Meeting Agenda**:

   * Verify that the agenda includes all necessary topics: schedule activities, performance metrics, assessments, analysis results, and identified issues.
   * Cross-check if the agenda aligns with project phase and milestones (e.g., critical design review, testing readiness review).
2. **Artifact Validation**:

   * Ensure key artifacts are prepared and complete, including:
     + Updated software development schedule.
     + Performance metrics reports (e.g., SPI, SV, milestone completion reports).
     + Risk assessments and mitigation plans.
     + Analysis results (e.g., issue trends, testing progress vs. schedule).
   * Confirm these artifacts reflect the latest project status.
3. **Stakeholder Requirements Validation**:

   * Validate that the review content meets the needs of all stakeholders (e.g., project manager, developers, assurance team, mission leads).
   * Ensure critical paths, dependencies, and decision points are highlighted.

### 7.4.2 Metrics and Performance Validation

Software assurance is responsible for assessing the accuracy, relevance, and completeness of performance data and metrics presented during the review.

#### **Activities:**

1. **Validate Metrics**:

   * Assess schedule-related metrics for correctness, including:
     + **Schedule Variance (SV)**: Are discrepancies between planned and actual progress clearly highlighted?
     + **Schedule Performance Index (SPI)**: How efficiently is the project progressing relative to expectations?
     + On-time task and milestone completion rates.
     + Testing progress against planned timelines.
   * Ensure metrics are calculated consistently and use reliable data sources.
2. **Analyze Trends**:

   * Evaluate trends in performance metrics to identify risks or patterns (e.g., recurring delays, resource constraints, bottlenecks).
   * Collaborate with the development team to interpret trends and assess impacts.
3. **Identify Missing Metrics**:

   * Recommend additional metrics for review if current ones lack sufficient granularity or do not capture risks (e.g., critical path completion rates, effort deviations).

### 7.4.3 Risk Assessment and Schedule Analysis

Software assurance plays an important role in evaluating risks related to schedule delays, compression, or changes.

#### **Activities:**

1. **Assess Risk Reports**:

   * Review risks and issues from the schedule, such as dependency conflicts, resource shortages, or overloading of tasks on the critical path.
   * Validate that risks are prioritized correctly and mitigation plans are actionable.
2. **Critical Path Analysis**:

   * Evaluate the plan for managing critical path activities to ensure no unexpected delays or bottlenecks occur during execution.
3. **Simulation and Scenario Analysis**:

   * Conduct "what-if" analyses for risks (e.g., consequences of missed milestones or reduced buffer allocations).
   * Validate existing contingency plans address plausible risks and assess whether contingency buffers need adjustment.

### 7.4.4 Supporting Review Execution

During the review, software assurance ensures that stakeholders discuss schedule-related concerns thoroughly, and that decisions align with the project's goals and strategies.

#### **Activities:**

1. **Facilitate Structured Discussions**:

   * Ensure that discussions during the review follow agreed priorities: schedule activities, performance, risks, analysis results, and issue tracking.
   * Steer discussions to address areas with significant variance or potential risks.
2. **Provide Independent Assessments**:

   * Share assurance analyses of the schedule’s status, performance metrics, and risks to provide independent insight into project health.
   * Confirm that the project's technical and programmatic objectives remain feasible based on the schedule.
3. **Track Stakeholder Input**:

   * Document stakeholder feedback, decisions, and issue resolution actions during the review for traceability.
4. **Issue Escalation Recommendations**:

   * Highlight unresolved issues or systemic risks that require escalation to higher-level management for resolution or additional resources.

### 7.4.5 Issue Tracking

Software assurance ensures that issues identified during schedule reviews are documented, tracked, and resolved in a timely manner.

#### **Activities:**

1. **Issue Log Validation**:

   * Verify all issues raised during schedule reviews are documented in an issue log or tracking system.
   * Ensure proper categorization for severity, priority, and expected resolution timeframe.
2. **Monitor Issue Resolution Progress**:

   * Regularly review the status of identified issues and ensure actions are completed to resolve them.
   * Validate that corrective actions are implemented effectively, particularly for schedule risks or delays.
3. **Track Dependencies**:

   * Ensure issues involving external dependencies (e.g., hardware readiness, third-party software) are actively managed and reflected in updates to the software schedule.
4. **Closure Confirmation**:

   * Validate that resolved issues no longer impact milestones or critical path progress.

### 7.4.6 Post-Review Activities

After the review, SA focuses on ensuring follow-up actions and updating the schedule as needed.

#### **Activities:**

1. **Review Minutes and Decisions**:

   * Confirm all review decisions are accurately documented (e.g., changes to the schedule, identification of new risks, mitigations, or resource reallocations).
   * Validate that minutes capture agreed actions with owners, deadlines, and resolutions.
2. **Assess Schedule Adjustments**:

   * Review updated software schedules post-review to confirm alignment with decisions made during the meeting.
   * Validate the integration of new actions or mitigations into the schedule.
3. **Follow-Up on Open Items**:

   * Ensure follow-up actions are completed for unresolved issues, such as detailed impact analyses or resource adjustments.

### 7.4.7 Reporting and Communication

Software assurance produces reports and presentations to summarize findings and ensure persistent project focus on reviewing and managing software schedules.

#### **Activities:**

1. **Prepare Assurance Reports**:

   * Generate reports summarizing:
     + Current schedule status and metrics.
     + Risks and mitigations.
     + Trends and performance analysis results.
   * Highlight unresolved issues and recommend next steps.
2. **Stakeholder Communication**:

   * Communicate assurance findings to project stakeholders between reviews to support proactive decision-making.
3. **Compliance Auditing**:

   * Confirm that the review process itself complies with the project’s requirements and NASA standards (e.g., SWE-016 for software schedule management).

### 7.4.8 Key Best Practices

* **Encourage Structured Reviews**: Software assurance ensures that reviews are well-organized and focused on actionable discussions about schedule performance, risks, and corrective actions.
* **Focus on Data-Driven Insights**: Assurance activities should prioritize validation of metrics, trends, and analysis results to drive informed decisions.
* **Collaborate with Stakeholders**: Effective assurance activities involve close collaboration with project managers, developers, and stakeholders to ensure all issues are addressed comprehensively.
* **Proactively Manage Risks**: Software assurance must bring attention to emerging risks and help stakeholders adopt mitigation plans that minimize downstream effects on the schedule.

## 7.5 Items To Be Discussed Or Reported

Examples of items to be discussed or reported are found below:

### 7.5.1 Examples of items on software assurance schedule activities could include:

* Software assurance plan,
* Software assurance audit,
* Software assurance status reports,
* Software assurance and software safety requirements mapping table for the SASS standard requirements, the cost estimate for the project’s software assurance support, Software Assurance reviews and software assurance review support,
* IV&V planning and risk assessment, if required.
* The IV&V Execution Plan, if required.
* System hazard analysis assessment activities,
* Software Safety Analysis,
* Software assurance independent static code analysis for cybersecurity vulnerabilities and weaknesses,
* Software assurance independent static code analysis, on the source code, showing that the source code follows the defined secure coding practices,
* Software assurance analysis performed on the detailed software requirements,
* Software assurance design analysis, SA peer reviews,
* Software assurance metric data, reporting, and analysis activities,
* Software assurance status reviews.

### 7.5.2 Examples of Software Assurance Metrics:

* The number of software assurance findings (e.g., # open, closed, latency) mapped against SA activities.
* Planned software assurance resource allocation versus actual SA resource allocation.
* The number of audit findings per audit, including the number of findings from process non-compliances and process maturity.
* Software cyclomatic complexity data for all identified safety-critical software components;
* Test coverage data for all identified safety-critical software components.
* Percentage completed for each area of traceability.
* Software test coverage percentages, including the percentage of testing completed and the percentage of the detailed software requirements, successfully tested to date;
* The number of compliance audits planned vs. the number of compliance audits completed.
* Number of peer reviews performed vs. # planned; the number of defects found in each peer review;
* The number of root cause analyses performed; list of finding identified by each root cause analysis.

Content guidelines for a good Software Assurance status report: (see [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports)) See also Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing)

### 7.5.3 Software Assurance and Software Safety Status Report

The following section defines the content for a software assurance Status Report. The Status Report Plan is a scheduled periodic communication tool to help manage expectations between the software assurance representative(s) and project engineering and management, OSMA stakeholders. It provides insight into the overall status relative to value-added and performance to software assurance plan. Pre-coordinate and define the specifics/content of the status report in the software assurance Plan. The software assurance Status Report content, in no specific order, addresses:

1. 1. SA Project Title and Date – Identify the project and the date(s) of the reporting period.
   2. Overall Status Dashboard or Stoplight Table – Provide a high-level status of progress, risk, schedule, and whether or not assistance/awareness is required. Typically a Green/Yellow/Red scheme for indicating go, no go status, and approaching minimum threshold or limits.
   3. Key Contributions/Accomplishments/Results (Value Added) – Identify any activities performed during the reporting period that has added value to the project. The reporting should include key SA contributions, accomplishments, and results of SA Tasking activities performed in Table 1 (SA Requirements Mapping Matrix). Examples are:
      * Analyses performed (e.g., PHAs, HAs, FMEAs, FTAs, Static Code Analysis)
      * Audits performed (e.g., process, product, PCAs, FCAs, )
      * Products Reviewed (e.g., Project Plans, Requirements, Design, Code, Test docs)
      * Tests witnessed
      * Assessments performed (e.g., Safety Criticality, Software Class, Risk, Cybersecurity)
   4. Current/Slated Tasks – Identify in-work and upcoming assurance activities. Identify (planned and unplanned) software assurance and oversight activities for the next reporting period. Examples are:
      * Analyses (e.g., PHAs, HAs, FMEAs, FTAs, Static Code Analysis)
      * Audit (e.g., process, product, PCAs, FCAs, )
      * Products Reviews (e.g., Project Plans, Requirements, Design, Code, Test docs)
      * Tests witnessing
      * Assessments (e.g., Safety Criticality, Software Class, Risk, Cybersecurity)
   5. Issue Tracking – Record and track software issues to follow progression until resolution. Track issues by priority status, safety, criticality, or some other criteria combination.
   6. Metrics – Identify the set of SA metrics used and analyzed for the reporting period. At a minimum, collect and report on the list of SA metrics specified in the SA Standard. Include analysis results, trends, or updates and provide supportive descriptions of methodology and criteria.
   7. Process Improvement suggestions and observations
   8. Obstacles/Watch Items – Identify and describe any obstacles, roadblocks, and watch items for the reporting period. Obstacles/Watch Items are an informal list of potential concerns.
   9. Risk Summary – List and provide status on SA risks associated with any activities/tasks required by the SA Standard. Highlight status changes and trends.
   10. Funding (As Applicable) – Provide funding status and trending information as needed to support the SA tasking for the project. Consider how the data/information can be used for future planning and cost estimating
   11. Schedule – Provide the necessary schedule/information to communicate the status of the SA tasking in support of the scope and timeline established for the project.

See also Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis)

## 7.6 Additional Guidance

Additional guidance related to holding a review of software activities, status, and results may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) |

# 8. Objective Evidence

Objective evidence involves tangible, verifiable, and auditable artifacts or documentation that demonstrate compliance with this requirement. The evidence must reflect that reviews are being conducted regularly, stakeholders are engaged, performance metrics and analysis results are being shared, and issues are tracked to resolution. Below is a list of examples of objective evidence for this requirement, organized into categories aligned with its key elements.

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

## 8.1 Evidence of Regular Reviews

#### **Artifacts:**

1. **Meeting Agendas and Invitations**:

   * Documentation of planned review meetings (e.g., recurring calendar events, formal invitations) showing regularity and purpose (e.g., weekly, monthly reviews).
   * Agenda items should include topics related to software schedule activities, milestones, metrics, performance assessments, and risks.
2. **Stakeholder Attendance Records**:

   * Attendance logs, participant lists, or sign-in sheets from schedule review meetings indicating stakeholder engagement.
   * Confirmation of stakeholder representation (e.g., developers, project manager, assurance team, mission leads).
3. **Meeting Minutes and Action Items**:

   * Minutes documenting:
     + Review discussions on schedule status, performance metrics, risks, and issues.
     + Decisions, feedback, and assigned actions.
     + Follow-up items for unresolved issues or updated metrics requested.
   * Evidence of stakeholder agreement on next steps.
4. **Review Frequency Logs**:

   * Records of when reviews occurred (date/time stamps) to confirm regularity (weekly, biweekly, monthly, etc.).
   * Ensure the review frequency aligns with project phase complexity or criticality.

## 8.2 Evidence of Software Schedule Activities Assessment

#### **Artifacts:**

1. **Software Schedule Documentation**:

   * Updated Gantt charts, timelines, or task-tracking documents presented and reviewed during meetings.
   * Demonstration of progress against milestones, critical paths, and dependencies.
2. **Critical Path Analysis Reports**:

   * Evidence of discussed critical path tasks and dependencies, including schedule constraints and bottlenecks that may delay key milestones or completion.
3. **Performance Metrics Reports**:

   * Metrics shared during the review, such as:
     + **Schedule Variance (SV).**
     + **Schedule Performance Index (SPI).**
     + Milestone completion rates or testing status compared to the plan.
   * Evidence that metrics are analyzed and presented to track performance and pinpoint risks.
4. **Risk Reports**:

   * Risk assessments tied directly to schedule-related risks (e.g., delayed tasks, resource constraints, or dependency issues).
   * Contingency discussions documented or mitigation plans generated.

## 8.3 Evidence of Metrics Analysis

#### **Artifacts:**

1. **Performance Metrics Presentations**:

   * Slide decks, graphs, or reports presented during reviews showing analyzed performance metrics (e.g., earned value analysis, milestone tracking metrics, milestone variance reports).
   * Evidence of trends, interpretations, or observations made based on these metrics.
2. **Testing Progress Reports**:

   * Metrics tracking how far along testing efforts are relative to planned schedules (e.g., percentage completion or testing delays identified).
   * Includes risk impacts if delays are noted.
3. **Schedule Health Reports**:

   * Comprehensive evaluations that detail schedule risks, buffer utilization, resource allocation efficiency, schedule compression, or corrective strategies.
4. **Stakeholder Questions/Inputs**:

   * Documentation reflecting detailed discussions based on metrics presented (e.g., identification of delays, contingency actions, or updated resource allocation requests).

## 8.4 Evidence of Issue Tracking and Resolution

#### **Artifacts:**

1. **Issue Tracking Logs**:

   * Logs documenting all issues raised during reviews, including:
     + Issue descriptions, priority levels, owners, and status (open, in progress, resolved).
     + Expected resolution timelines and associated actions.
     + Links to task dependencies and schedule impacts.
2. **Changes Linked to Resolved Issues**:

   * Evidence demonstrating changes made to the software schedule based on issue resolution (e.g., updates to tasks, milestones, or critical path adjustments).
   * Documentation showing corrected risks, mitigations executed, and lessons learned.
3. **Resolution Records**:

   * Evidence confirming issue closure (e.g., emails, meeting notes, status updates in tracking tools like JIRA, Issue Log updates).
4. **Escalation Records**:

   * Logs detailing unresolved issues escalated to higher-level stakeholders or management, including escalation decisions, resolutions, and impact on the overall schedule.

## 8.5 Evidence of Stakeholder Engagement

#### **Artifacts:**

1. **Stakeholder Participation Logs**:

   * Records documenting stakeholder attendance and active involvement during scheduling reviews.
   * Examples include recorded participation rates and verification of key stakeholders (e.g., technical leads, schedule owners, assurance team) consistently attending.
2. **Stakeholder Feedback Documentation**:

   * Feedback from stakeholders provided during reviews, captured in meeting minutes or action item trackers.
   * Evidence that feedback is incorporated into updated schedules or plans.
3. **Review Feedback Implementation Logs**:

   * Documentation showing stakeholder recommendations or observations discussed during reviews are addressed, with updated schedules or risk mitigations implemented accordingly.
4. **Stakeholder Consensus Records**:

   * Documentation demonstrating stakeholder agreement on decisions made during the reviews (e.g., email summaries, signed meeting minutes).

## 8.6 Review Artifacts or Deliverables

#### **Artifacts:**

1. **Review Slide Decks**:

   * Presentation materials prepared for schedule reviews, including all necessary content (software task status, metrics, and analysis results).
   * Summary of discussed risks, concerns, and next steps.
2. **Updated Baseline Documentation**:

   * Evidence confirming updates to project baselines post-review, including approved schedule changes and adjustments reflected in configuration repositories.
3. **Action Tracker Updates**:

   * Deliverable demonstrating fully closed action items arising from schedule reviews.
4. **Compliance and Audit Reports**:

   * Independent reports confirming compliance with review processes and alignment with project requirements (e.g., NASA directives on schedule visibility).

## 8.7  Evidence of Ongoing Improvement

#### **Artifacts:**

1. **Review Improvement Logs**:

   * Documentation showing iterative improvement of software schedule reviews over time (e.g., enhancement of stakeholder feedback collection, revised metrics tracking, better resolution timelines).
   * Meeting minutes reflecting lessons learned from prior reviews.
2. **Documented Review Adjustments**:

   * Evidence confirming adjustments to review formats, tools, or methodologies to better address stakeholder needs or resolve recurring issues.

## 8.8 Summary of Objective Evidence

| **Category** | **Example Artifacts** |
| --- | --- |
| **Regular Reviews** | Meeting agendas, attendance records, minutes. |
| **Schedule Activities** | Updated schedules, critical path reports, WBS. |
| **Metrics Analysis** | SPI/SV reports, milestone tracking reports. |
| **Issue Tracking** | Issue logs, resolution documentation, updates. |
| **Stakeholder Engagement** | Feedback logs, participation records, consensus. |
| **Deliverables** | Baseline schedules, presentation slides, audits. |

## 8.9 Key Considerations

1. **Traceability**: Ensure all evidence can be traced to the specific stakeholder review meetings and aligns with project-level documentation.
2. **Accessibility**: Evidence should be easily accessible and stored in configuration management systems for auditing purposes.
3. **Stakeholder Input**: Incorporate stakeholder contributions into the evidence to reflect collaborative review processes.
4. **Focus on Resolution**: Ensure evidence supports tracking of issues and risks to closure, minimizing impacts on the software schedule and mission success.

By generating and maintaining objective evidence across these categories, projects can demonstrate compliance with this requirement effectively while ensuring review processes contribute to project health and delivery success.
