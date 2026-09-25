# SWE-179 - IV V Submitted Issues and Risks

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695519. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks

SWE-179 - IV&V Submitted Issues and Risks

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695519)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695519&showCommentArea=true&showComments=true#addcomment)

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

3.6.5 If software IV&V is performed on a project, the project manager shall provide responses to IV&V submitted issues and risks and track these issues and risks to closure.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-179 History

SWE-179 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.6.5 If software IV&V is performed on a project, the project manager shall provide responses to IV&V submitted issues and risks, and track these issues and risks to closure. |
| Difference between C and D | No change. |
| D | 3.6.5 If software IV&V is performed on a project, the project manager shall provide responses to IV&V submitted issues and risks and track these issues and risks to closure. |

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
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |

# 2. Rationale

Software IV&V (Independent Verification & Validation) is a critical risk mitigation activity focused on ensuring the safety, reliability, and quality of NASA’s mission-critical and safety-critical software. The requirement for the project manager to provide responses to IV&V-submitted issues and risks, and to track them to closure, ensures that the concerns raised by the IV&V team are actively addressed and resolved. This is fundamental to reducing software-related risks and achieving mission success.

This requirement ensures that IV&V-submitted issues and risks are actively addressed, tracked, and resolved, fostering collaboration between project teams and the IV&V Provider. By meeting this requirement, project managers ensure critical software risks are mitigated, errors are resolved early, and the software is robust, reliable, and safe for mission success. This process not only reduces the likelihood of mission failure but also builds accountability, improves risk management, and enhances compliance with NASA software assurance standards.

## 2.1. Ensures Effective Risk Mitigation and Problem Resolution

* IV&V identifies defects, risks, and issues from an independent and objective perspective, often uncovering gaps or problems that may be overlooked by the development team.
* Responding to and resolving these issues ensures that risks (e.g., software safety, security vulnerabilities, design flaws) are addressed in a timely manner, reducing the likelihood of costly failures or operational impacts during later project phases or deployment.
* Tracking these issues and risks to closure ensures accountability and confirms that all identified risks are fully mitigated or accepted.

## 2.2. Strengthens Communication and Collaboration Between IV&V and the Project Team

* By providing responses to IV&V-submitted risks and issues, the project manager fosters transparent communication and collaboration between the project team and the IV&V team.
* Timely responses demonstrate commitment to addressing concerns raised by the IV&V team and build a cooperative environment that focuses on problem-solving rather than mismanagement or avoidance of identified risks.

## 2.3. Improves Software Assurance and Reliability

* Actively addressing and closing IV&V-submitted issues enhances the overall robustness, correctness, and completeness of the software being developed.
* This hands-on approach ensures that software meets system, stakeholder, and mission requirements (both nominal and off-nominal conditions), directly contributing to system reliability and user confidence.

## 2.4. Establishes Accountability and Traceability

* Tracking issues from submission to closure provides clear accountability for risk resolution, assigning ownership to specific team members or groups.
* This process creates a traceable record of the actions taken, which can be reviewed during audits, milestone reviews, or retrospectives, ensuring that every identified issue is formally considered and resolved.

## 2.5. Addresses Organizational and Mission Goals

* Mission success depends on reducing critical software risks to acceptable levels. IV&V-submitted issues often highlight risks that could directly impact the mission's goals, safety, cost, and schedule.
* By ensuring that these risks are addressed and tracked, the project ensures alignment with NASA’s broader safety-critical and mission-critical objectives while improving stakeholder trust.

## 2.6. Provides Early Opportunities to Address Defects and Risks

* Resolving IV&V-submitted issues early in a project’s lifecycle is significantly more cost-effective and less disruptive than addressing them during later phases (e.g., integration, testing, or deployment).
* This proactive approach minimizes rework and reduces the risk of encountering high-severity issues during operational phases, when corrections may jeopardize mission timelines and performance.

## 2.7. Supports Compliance with NASA Standards

* NASA standards (e.g., NASA-STD-8739.8 [278](#_tabs-<p></p>) and NPR 7150.2) emphasize the need for rigorous software assurance and effective risk management to achieve mission success.
* Ensuring that IV&V-submitted issues and risks are resolved and tracked is aligned with these standards, reinforcing compliance across all project activities.

## 2.8. Reinforces the Role of IV&V as an Effective Assurance Activity

* IV&V serves to provide independent, unbiased assessments of software quality, safety, and performance. Ignoring or failing to address IV&V-submitted concerns reduces the effectiveness and benefits IV&V can provide to a project.
* Actively resolving these issues validates the trust placed in IV&V and ensures its recommendations are considered integral to the project’s risk management and assurance efforts.

## 2.9. Reduces the Likelihood of Software Failures

* Failure to adequately address IV&V-identified risks or defects increases the likelihood of software failures that could have significant financial, operational, or safety consequences.
* This requirement ensures that all identified risks are tracked to resolution, minimizing the chance of critical failure during operation or testing.

## 2.10. Enhances Decision-Making for Project Leadership

* Regular responses and progress tracking of IV&V-identified issues provides project leadership with better insight into the health of the software development process, the severity of risks, and the effectiveness of mitigation strategies.
* By responding to and addressing these concerns diligently, project leadership ensures confident, data-driven decision-making throughout the project lifecycle.

## 2.11 Responsibilities of the Project Manager

To meet the intent of this requirement, the project manager must:

1. **Acknowledge IV&V-Submitted Issues and Risks**:

   * Review the risks and issues raised by the IV&V team.
   * Evaluate the validity, scope, and potential impact of these concerns.
2. **Provide Timely and Actionable Responses**:

   * Respond with clear actions to address, mitigate, or justify acceptance of the risks or issues identified by IV&V.
   * Establish realistic timelines for issue resolution and assign accountability to the relevant project teams.
3. **Implement Tracking Systems**:

   * Use tracking tools (e.g., defect or issue management systems) to monitor the progress of risk resolution and ensure no issues are overlooked.
   * Keep a detailed status of issues, including current action items, dates, responsible parties, and resolution status.
4. **Ensure Risk and Issue Closure**:

   * Verify that resolution efforts have fully mitigated the risk or defect before closing an issue.
   * Work in alignment with IV&V to confirm that their concerns have been satisfied or otherwise documented if accepted risks remain.
5. **Engage in Transparent Communication**:

   * Regularly update the IV&V Provider on mitigation progress, outcomes, or any deviations from submitted resolutions.
   * Ensure open channels of communication to clarify doubts, gather feedback, or address new findings from IV&V.

## 2.12 Benefits of Adhering to the Requirement

#### **For the Project**:

* Improved alignment between development and assurance goals through active collaboration with IV&V.
* A stronger foundation of software quality that increases overall mission success.
* Fewer post-deployment issues, reducing costs and rework associated with late-stage fault resolution.

#### **For Project Managers**:

* Increased confidence in the software’s ability to meet requirements under both nominal and off-nominal conditions.
* Effective tools for decision-making and risk prioritization throughout the project lifecycle.

#### **For NASA Missions**:

* Greater assurance of mission-critical software safety, reliability, and security.
* Improved stakeholder confidence in NASA’s ability to manage large-scale, high-risk software systems effectively.

# 3. Guidance

Independent Verification and Validation (IV&V) is a key component of NASA's Software Assurance risk management strategy, providing independent evaluations of safety- and mission-critical software to ensure correctness, reliability, and compliance with requirements. When IV&V identifies risks or submits issues for consideration, the project manager is responsible for ensuring these concerns are acknowledged, evaluated, tracked, and closed. This collaborative process ensures that potential problems are addressed effectively and the software meets the operational reliability and safety needs of its intended mission.

By responding to IV&V-submitted risks and issues, performing a thorough evaluation, tracking concerns to closure, and maintaining collaborative communication, the project manager empowers NASA to deliver software systems that are safe, reliable, and mission-ready. This process integrates independent assessments with efficient risk management strategies to ensure mission success while complying with NASA's rigorous software assurance standards.

## 3.1 Importance of Addressing IV&V-Submitted Issues and Risks

Effective response and tracking of IV&V-submitted issues contribute to:

1. **Risk Mitigation**: Proactively resolving IV&V-identified risks reduces the likelihood of critical software failures, missed requirements, or mission-compromising safety issues.
2. **Accountability**: Tracking issues and risks to closure ensures that every concern raised is fully addressed and that decisions are traceable, enforceable, and compliant with NASA standards.
3. **Collaboration and Communication**: Engaging with IV&V as partners enhances transparency, builds trust, and creates a cooperative environment focused on successful resolution.
4. **Continuous Improvement**: Incorporating lessons learned from IV&V assessments into development efforts improves project processes and software quality across both short-term goals and long-term missions.

## 3.2 IV&V's Role in NASA Risk Mitigation

#### **Independent Assurance Through Key Principles**:

* **Technical Independence**: Enhances objectivity by separating IV&V from the software development team to identify risks impartially.
* **Managerial Independence**: Ensures that IV&V operates outside of project management to maintain unbiased reporting.
* **Financial Independence**: Allows IV&V to evaluate risks without external pressures related to funding allocation or project success.

IV&V addresses critical questions through its analysis:

1. Does the software perform its intended functions correctly, reliably, and safely?
2. Does the software avoid unintended and hazardous behaviors?
3. Does the software handle off-nominal conditions and adverse scenarios as expected?

#### **Value Added by IV&V**:

* Higher-quality products.
* Reduced risk through proactive problem identification.
* Insight into technical and operational challenges.
* Cost savings through early detection of defects and improved design.
* Knowledge transfer of best practices in system and software engineering.

## 3.3 Risk and Issue Evaluation Process

When IV&V submits risks or issues, the following considerations should guide their evaluation:

#### **Project Impact Analysis**:

1. **Gather Appropriate Stakeholders**:

   * Include procurement, quality assurance, risk management, subject matter experts, and management in the review process.
   * Ensure representation from safety and software assurance personnel to address all concerns, including hazards and regulatory compliance.
2. **Evaluate the Impact on the Following Areas**:

   * **Schedule and Cost**: Assess the time and resources required to make, test, and verify the change, including regression testing.
   * **Resources and Groups**: Analyze consequences for other project teams, dependencies, and allocation of resources.
   * **Functions and Features**: Determine whether critical functionality, interfaces, or resource requirements are affected.
   * **Baseline Products**: Evaluate design, test documentation, traceability matrices, and other artifacts for dependencies or required updates.
   * **Performance, Reliability, and Quality**: Identify potential impacts on system performance, availability, maintainability, and quality.
   * **Software Safety**: Consider potential safety impacts and whether safety-critical hazards are introduced or mitigated.
   * **Alternatives**: Identify alternative solutions to address the risk or issue.

#### **Risk vs. Reward**:

Evaluate the balance between the risks of implementing the change versus leaving the issue unresolved. Consider:

* Complexity and criticality of the change.
* Whether the change request is within the scope of the project or necessary to meet requirements.

#### **Safety Analysis** (In accordance with **NASA-STD-8739.8** [278](#_tabs-<p></p>) ):

* **Hazard Contribution**: Evaluate whether new hazards are introduced or existing hazards are modified.
* **Control and Mitigation**: Assess whether hazard controls remain valid or become ineffective.
* **System and Software Safety**: Analyze how the proposed change affects overall software and system safety.

#### **Capture Evaluation Outcomes**:

* Maintain detailed records of analysis results, decisions, and applicable action items.
* Document the rationale behind evaluations to ensure traceability.

## 3.4 Tracking Issues and Risks to Closure

#### **Best Practices for Efficient Tracking**:

1. **Change Control Systems**:

   * Use a change management system compatible with the project environment to track issues until their resolution.
   * Log all components of the change request, including problem reports, impact analyses, evaluation board notes, and meeting minutes.
2. **Traceability Across Artifacts**:

   * Map each defect or risk back to the related system hazard or requirement.
   * Record changes to impacted artifacts such as requirements documents, design specifications, tests, code, and user manuals.
3. **Verification Before Closure**:

   * Close issue or risk records only after verifying that corrective actions have been completed.
   * Ensure all ancillary documents (e.g., trace matrices, test reports, software version description documentation) reflect the implemented solution.

#### **Collaborative Efforts to Achieve Closure**:

* Engage IV&V and development teams jointly in dispositioning risks.
* Achieve consensus between the project and IV&V teams as risks or issues are ultimately resolved or accepted.

## 3.5 IV&V Collaboration Through the Project Execution Plan (IPEP)

The scope of IV&V services and risk management efforts is documented in the **IV&V Project Execution Plan (IPEP)**, a collaborative document developed by the IV&V Provider and approved by the NASA IV&V Program.

* The IPEP formalizes how issues and risks will be identified, tracked, and resolved.
* Use the IPEP to guide IV&V interactions with the project team, including communication paths, roles, responsibilities, and reporting methods.

## 3.6 Benefits of Following This Process

#### **For the Project**:

* Risks are identified, evaluated, and mitigated proactively, reducing late-stage rework and deployment issues.
* Improved communication and visibility into project status and concerns, enhancing decision-making.

#### **For Project Managers**:

* Greater accountability and assurance that critical risks affecting mission success are addressed.
* Confidence that software meets requirements under nominal and adverse conditions.

#### **For Mission Success**:

* Enhanced software reliability and safety, ensuring operational success in critical NASA missions.
* Reduced long-term costs associated with defect repair, system downtime, or safety incidents.

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Software Quality Assurance](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Software+Quality+Assurance) |

# 4. Small Projects

On smaller projects, resource constraints, simpler software systems, and limited personnel can make fulfilling this requirement challenging. However, it is still essential to manage IV&V-submitted issues and risks effectively to ensure software quality and mission success. Small projects can adopt **streamlined, tailored, and lightweight processes** to meet this requirement while maintaining compliance and minimizing overhead.

This small project guidance focuses on the following principles:

1. **Simplify Processes:** Use existing tools and methods to manage issues and risks without adding unnecessary complexity.
2. **Prioritize Issues and Risks:** Focus on addressing mission-critical and safety-critical concerns based on the project’s scope and risk level.
3. **Ensure Clear Communication:** Foster close collaboration between the development and IV&V teams to quickly resolve concerns.
4. **Document and Track to Closure:** Use simple tracking mechanisms (e.g., spreadsheets or lightweight tools) to track and close out IV&V-raised issues.

By implementing these tailored approaches, small projects can meet this requirement effectively, ensuring risks and issues raised by IV&V are resolved in a timely and efficient manner.

## 4.1 Establish a Communication and Collaboration Framework

Small projects rely on collaboration between the project team and the IV&V team to address issues efficiently. Establishing communication channels ensures that IV&V issues are raised, discussed, and resolved in a timely manner.

* **Action Items:**

  + Assign a **single point of contact (POC)** or liaison on the project team who is responsible for interacting with the IV&V team. This will help streamline communications.
  + Schedule **regular coordination meetings** (e.g., bi-weekly or monthly) with the IV&V team to review and discuss submitted issues and risks.
  + Develop a **simple escalation process** for IV&V-identified critical or high-priority issues to ensure management is aware and involved quickly.
* **Tools & Techniques:**

  + Use email or meeting agendas to document issues for discussion with IV&V.
  + Leverage tools like Microsoft Teams, Slack, or other communication platforms to maintain real-time interaction with IV&V representatives.

## 4.2 Develop and Document an Issue and Risk Management Plan

Documenting the process for responding to and tracking IV&V issues and risks creates alignment between the project manager and the IV&V team.

* **Action Items:**

  + Include an **issue and risk response plan** in the project’s risk management plan or IPEP (IV&V Project Execution Plan).
    - Specify how IV&V-submitted issues will be prioritized and responded to.
    - Outline roles and responsibilities for both the project team and the IV&V team.
  + Define clear criteria for **issue/risk severity and prioritization:**
    - Mission-critical and safety-critical risks should receive the highest priority.
    - Lesser risks may be addressed as resources allow or deferred with acceptable justifications.
  + Establish timelines for responding to IV&V concerns, such as ensuring acknowledgment or response within **1-3 business days.**
* **Example Severity Categories:**

  1. **Critical:** Direct impact on mission success or safety, requires immediate action.
  2. **High:** Major impact on system functionality or performance, needs prompt resolution.
  3. **Medium:** Minor impact, but should be addressed within the project timeline.
  4. **Low:** Best addressed in future activities or may not require action.

## 4.3 Provide Timely Responses to IV&V Issues

It is critical that the project manager responds quickly and effectively to IV&V-raised issues, even for small projects. Responses should demonstrate that the project is actively addressing the issues.

* **Action Items:**

  + Acknowledge receipt of the issue or risk submitted by the IV&V team as soon as possible (e.g., within 1-3 business days):
    - Ensure that the acknowledgment includes a tracking ID and summary of the issue or risk.
    - Communicate the initial disposition to IV&V, such as whether the issue will be "Accepted," "Deferred," or "Rejected."
  + Provide a detailed response within an agreed-upon timeframe, including:
    - **Root Cause Analysis:** Understand the root cause of the issue.
    - **Proposed Resolution Plan:** Define what actions will be taken to mitigate or resolve the risk/issue.
    - **Schedule Impact Assessment:** Explain if the resolution impacts the project timeline.
    - **Feedback on Closure Criteria:** Agree on what constitutes closure of the issue or risk.
* **Best Practices:**

  + Group similar or related issues together to address them collectively, minimizing redundant efforts.
  + Provide justifications for deferred or rejected issues to ensure alignment with the IV&V team.

## 4.4 Track Issues and Risks to Closure

Small projects can use simple tools to log and track the status of issues and risks raised by the IV&V team. Tracking ensures that no issues or risks are overlooked and that they are resolved in a timely manner.

* **Action Items:**

  + Create an **IV&V Issue and Risk Tracking Log**. Key fields to include:
    - Issue ID.
    - Date submitted by IV&V.
    - Description of the issue or risk.
    - Severity level (Critical, High, Medium, Low).
    - Status (e.g., “Open,” “In Progress,” “Closed”).
    - Response timeframe (e.g., deadline for acknowledging and addressing).
    - Assigned responsibility (e.g., the individual or team addressing the issue).
    - IV&V closure confirmation.
  + Update the log regularly (e.g., weekly) to reflect the progress of each issue/risk.
* **Tools & Techniques:**

  + Use **spreadsheets** (e.g., Microsoft Excel, Google Sheets) for small projects with few issues.
  + If your project uses software management tools such as **JIRA, Trello, or Microsoft Project**, configure them to include IV&V risk/issue tracking.
  + Ensure visibility of the tracker to both the project team and the IV&V team.

## 4.5 Collaborate on Risk Mitigation and Issue Resolution

Small projects benefit from close collaboration between the project team and IV&V when resolving issues and mitigating risks.

* **Action Items:**

  + Work with the IV&V team to develop and agree on:
    - **Mitigation strategies** for risks (e.g., redesign, additional testing, safety analysis).
    - **Root cause resolutions** for issues, validating the fix before marking it as “closed.”
  + Collaboratively define **closure criteria** for every issue or risk:
    - What evidence or actions are needed to satisfy the IV&V team that the risk/issue is resolved?
* **Best Practices:**

  + Leverage small meetings, workshops, or design reviews to resolve issues in collaboration with IV&V.
  + Ensure detailed documentation of the resolution process, particularly for significant or high-severity issues.

## 4.6 Close Out Issues and Risks

Closure involves confirming with the IV&V team that the issue/risk has been addressed and no further actions are required.

* **Action Items:**
  + Review and document the evidence supporting closure of each risk/issue, such as:
    - Test results.
    - Code fixes or updates.
    - Updated requirements or documentation.
  + Obtain **formal approval from the IV&V team** to confirm closure:
    - Send a formal sign-off email or closure acknowledgment for each resolved issue.
  + Retain all closure evidence for compliance and lessons-learned purposes.

## 4.7 Document Lessons Learned

Small projects should use the experience of addressing IV&V-raised issues to improve risk management practices in current and future projects.

* **Action Items:**
  + Record lessons learned in a **final project report or post-project evaluation**:
    - What were the most common types of IV&V risks and issues?
    - How could responses and tracking be improved to minimize delays or misunderstandings?
  + Share best practices with project team members and future small project teams.

## 4.8 Example Tools and Documentation for Small Projects

1. **IV&V Issue and Risk Tracking Log:**
   * Simple Excel or Google Sheets log.
   * Key fields: Issue ID, Description, Severity, Date Opened, Status, Owner, IV&V Closure Approval.
2. **Meeting Minutes and Action Items:**
   * Track agreements and decisions related to resolving IV&V issues.
3. **Emails and Correspondence:**
   * Document acknowledgments and responses to IV&V concerns.
4. **Resolution Evidence:**
   * Test results, code updates, and other supporting documents.
5. **Lessons Learned Report:**
   * Record areas for improvement in managing IV&V issues and risks.

## 4.9 Summary of Small Project Guidance

| **Step** | **Description** |
| --- | --- |
| **Communication Framework** | Define a POC, set regular meetings, and establish clear communication channels with IV&V. |
| **Issue and Risk Management Plan** | Document the process for responding to and resolving IV&V-submitted issues. |
| **Timely Responses** | Acknowledge and address IV&V issues within agreed timelines, prioritize based on severity. |
| **Track to Closure** | Use a simple tracker to monitor the status and disposition of all IV&V-submitted risks/issues. |
| **Collaborate with IV&V** | Work with the IV&V team on resolving issues and defining closure criteria. |
| **Close Issues** | Validate fixes, obtain IV&V approval, and document closure evidence. |
| **Document Lessons Learned** | Capture lessons learned to improve issue/risk management in future projects. |

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-028)

  [IV&V Project Execution Plan (IPEP) Template,](https://swehb.nasa.gov/download/attachments/16450397/t2103_-_ver_f.pdf?api=v2 "Click to open in new window")

  T2103, NASA Independent Verification and Validation Program, 2011.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

**Context:**  
In a spacecraft software development project, risks identified by the IV&V team were not appropriately prioritized or tracked to closure due to limitations in project resources and a lack of formal tracking mechanisms. Some unresolved risks ultimately impacted the operational readiness of the mission, causing delays and schedule impacts.

**Key Insights:**

* **Tracking Issues Ensures Accountability:** Without a formal process for tracking and resolving risks to closure, issues can be forgotten or improperly mitigated, exposing the project to technical and schedule risks.
* **Prioritize Critical Risks:** Not all risks require immediate action. Allowing insufficient prioritization can lead to time wasted on low-severity risks while higher-severity risks remain unaddressed.

**Relevance to Requirement 3.6.5:**  
This lesson reinforces the importance of implementing a risk tracking mechanism to monitor, prioritize, and resolve IV&V-raised risks effectively. Small projects can use lightweight tools (e.g., spreadsheets or simple tracking logs) to maintain visibility and accountability for all submitted risks and issues.

---

### **Lesson No. 2528: Poor Communication Led to Mismanagement of IV&V Issues**

**Context:**  
A NASA ground system software team experienced a breakdown in communication with the IV&V team. IV&V-submitted issues and risks were either misunderstood or ignored. This lack of communication resulted in incomplete risk mitigation, leading to performance gaps discovered late during integration testing.

**Key Insights:**

* **Collaborative Communication is Key:** Effective communication between development and IV&V teams is critical for understanding the nature of submitted risks and responding accurately.
* **Timely Responses Avoid Escalation:** Delayed responses to IV&V submissions led to escalation and inefficiencies, which negatively impacted the testing phase.

**Relevance to Requirement 3.6.5:**  
To effectively address IV&V-identified risks, project managers must establish clear communication protocols with the IV&V team. Timely responses ensure transparency and better alignment between stakeholder expectations.

---

### **Lesson No. 723: Delayed Resolution of Critical IV&V Defects Increased Costs**

**Context:**  
During software development for a NASA mission-critical system, the IV&V team identified several critical defects early in the lifecycle, but project constraints led to delays in resolving them. These unresolved defects carried forward to later stages and required costly fixes during integration testing.

**Key Insights:**

* **Respond Early to Minimize Cost:** Delaying responses to IV&V-raised issues increases cost and effort, particularly when problems persist into later testing stages.
* **Track Issues to Closure:** Projects benefit from tracking all issues to ensure none are missed, especially critical defects related to software functionality.

**Relevance to Requirement 3.6.5:**  
This lesson highlights the importance of responding promptly to IV&V findings to avoid costly fixes later. Small projects should prioritize addressing high-severity risks and ensure mechanisms are in place to track defects from identification through resolution.

---

### **Lesson No. 1945: Lack of IV&V Issue Tracking Increased Integration Risks**

**Context:**  
A software project saw discrepancies between the development team and the IV&V team in tracking identified risks. IV&V raised concerns about incomplete code reviews and missing test coverage during early iterations. However, the project team failed to resolve and close identified risks, leading to integration challenges with upstream systems.

**Key Insights:**

* **Formal Risk Closure Process:** All risks raised by IV&V must be tracked and formally closed through validation. Lack of formal closure increases the likelihood of unresolved issues spilling into later project stages.
* **Accountability Drives Resolution:** Clear assignment of responsibility for resolving risks ensures that issues do not linger.

**Relevance to Requirement 3.6.5:**  
Projects must define formal processes for tracking and closing risks raised by IV&V. Assigning owners to IV&V-raised issues ensures accountability and facilitates timely closure.

---

### **Lesson No. 5451: Misaligned Expectations Between Development Team and IV&V Caused Delays**

**Context:**  
A software team did not fully align expectations with the IV&V team regarding closure criteria for risks. IV&V repeatedly flagged risks as unresolved, leading to stalled progress and disagreements over whether corrective actions were sufficient.

**Key Insights:**

* **Define Closure Criteria:** Both teams must agree on what constitutes "closure" for an IV&V-submitted issue or risk.
* **Collaborate on Corrective Actions:** The development team should work closely with IV&V to define acceptable actions for resolving risks.

**Relevance to Requirement 3.6.5:**  
Projects must align expectations with IV&V regarding issue/risk closure—criteria should clearly indicate when a risk is considered resolved. This collaboration avoids miscommunication and unnecessary delays.

---

### **Lesson No. 3183: Effective Tools Enabled Better Tracking of IV&V Issues**

**Context:**  
In a software development project, implementing lightweight tools like shared tracking logs and dashboards improved visibility and accountability for addressing IV&V-raised issues. These tools ensured that both the development and IV&V teams had real-time insight into the status of all risks and issues.

**Key Insights:**

* **Accessible Tools Simplify Tracking:** Simple tools for tracking work well for small teams and reduce complexity.
* **Shared Visibility Promotes Collaboration:** When both the development team and IV&V team have shared views of issue/risk status, collaboration and progress improve.

**Relevance to Requirement 3.6.5:**  
Small projects can leverage lightweight tools such as Google Sheets, shared dashboards, or basic project management tools (e.g., Trello, JIRA) to track and manage IV&V-raised issues effectively.

---

### Summary of NASA Lessons Learned for Requirement 3.6.5

| **Lesson** | **Key Takeaway** | **Small Project Guidance** |
| --- | --- | --- |
| **Failure to Prioritize Issues (Lesson 3438)** | Use tracking tools to manage accountability and ensure critical risks are resolved promptly. | Develop a lightweight tracking process for IV&V issues. Prioritize risks based on severity levels. |
| **Poor Communication (Lesson 2528)** | Collaborative communication with IV&V avoids misunderstandings and improves risk mitigation. | Hold regular meetings with IV&V to clarify issues and progress. Define response timelines. |
| **Delayed Resolution of Defects (Lesson 723)** | Early responses to IV&V findings minimize cost escalation. | Respond promptly to IV&V-raised issues and resolve high-priority concerns quickly. |
| **Lack of Tracking (Lesson 1945)** | Ensure all IV&V concerns are formally tracked through validation and closure. | Use simple tracking logs or shared dashboards to ensure no risks remain unresolved. |
| **Misaligned Expectations (Lesson 5451)** | Agree on clear closure criteria to avoid stalled progress. | Collaborate with IV&V to define closure criteria for all risks/issues raised. |
| **Effective Tools (Lesson 3183)** | Accessible, lightweight tools like spreadsheets or shared dashboards facilitate tracking and closure. | Use simple tools (spreadsheets, Trello, JIRA) to manage issue/risk tracking efficiently. |

---

### **Key Takeaways for Small Projects**

1. **Prioritize Critical Risks:** Focus on mission-critical and safety-critical issues raised by IV&V.
2. **Simplify Issue Tracking:** Use lightweight tools such as Excel or shared dashboards to track IV&V-raised risks and issues.
3. **Collaborative Communication:** Schedule regular meetings with IV&V to review issues, risks, and resolutions.
4. **Define Closure Criteria:** Work closely with IV&V to agree on criteria for closing issues and risks.
5. **Timely Responses:** Respond promptly to IV&V feedback to avoid delayed progress and increased costs.

By incorporating lessons learned from past projects, small projects can efficiently address IV&V-raised risks and issues, track them to closure, and ensure compliance with Requirement 3.6.5, enhancing overall software quality and mission success.

 

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-179 - IV&V Submitted Issues and Risks**

3.6.5 If software IV&V is performed on a project, the project manager shall provide responses to IV&V submitted issues and risks and track these issues and risks to closure.

This guidance establishes a process for effectively documenting, tracking, and addressing IV&V-submitted issues, concerns, and risks as part of NASA’s Software Assurance processes. It ensures that IV&V contributions are maximized, risks are mitigated, and projects maintain compliance with NASA software assurance standards.

By following this refined guidance, project teams can manage IV&V findings, issues, and risks with greater rigor, ensuring alignment with NASA’s Software Assurance expectations for safety-critical and mission-critical software projects.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project manager responds to IV&V submitted issues, findings, and risks and that the project manager tracks IV&V issues, findings, and risks to closure.

## 7.2 Software Assurance Products

**Deliverable:**

* **Records of IV&V Issues and Risks:**  
  Maintain detailed records of all IV&V issues and risks, including:
  + **Status** (e.g., accepted, in work, closed).
  + Associated risk severity levels (e.g., red, yellow, green).
  + Risk mitigation plans.
  + Links to related artifacts (e.g., requirements, design, testing documentation, traceability matrices).

**Confirmation Evidence:**  
Document evidence confirming IV&V involvement in the project. This includes:

* Records of IV&V participation in relevant milestone reviews.
* Written confirmation of access provided to IV&V teams (e.g., to artifacts, personnel, systems).
* Records of IV&V findings delivery and evidence of project responsiveness (e.g., timely resolution decisions).

## 7.3 Metrics

Recommended Metrics for IV&V Monitoring and Risk Management: To assess the effectiveness of IV&V involvement and track software assurance performance:

1. **Product Non-Conformances:**

   * The number of **software work product Non-Conformances** identified by lifecycle phase over time.
   * Categorize Non-Conformances by the type of impact (e.g., requirements, design, code, testing, security, documentation).
2. **Risk Tracking:**

   * The number of **risks identified** by each lifecycle phase (open risks, closed risks).
   * The **severity of risks** (e.g., red, yellow, green) tracked over time.
   * The number of **risks with mitigation plans** compared to the total identified risks.
   * Trends in risks over time:
     + **Upward trending risks (increasing severity or occurrence).**
     + **Downward trending risks (resolved or mitigated).**
3. **IV&V Contributions and Outcomes:**

   * The number of IV&V-identified Non-Conformances, issues, and risks:
     + Categorize them by status (**open, closed, accepted by project**).
     + Track by severity level.
     + Associate findings with lifecycle phase and the category of Non-Conformance (e.g., requirements, design, code, testing, security, etc.).
   * Trends in IV&V findings:
     + Track the ratio of open versus closed Non-Conformances over time (improvement trend).

These metrics provide visibility into the overall health and progress of software assurance activities, ensuring IV&V issues and risks are effectively managed.

For additional metrics and processes, see topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

### 7.4.1 Confirm IV&V Involvement

1. **Determine if IV&V is Required**:  
   Consult **NASA-STD-8739.8** [278](#_tabs-<p></p>) , section 4.4, to establish IV&V applicability to the project and ensure compliance with IV&V requirements.  
   Reference [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) for guidance on IV&V implementation.
2. **Collaborate With IV&V Providers**:  
   If IV&V is required:

   * Ensure findings, concerns, and risks are clearly documented and delivered periodically by the IV&V team to the project team during milestone reviews or status updates.
   * Provide appropriate access to SA personnel for reviewing IV&V findings.

### 7.4.2 Tracking IV&V Findings and Risks

1. **Review and Track Findings to Closure**:

   * Confirm all IV&V findings (including concerns, issues, and risks) are actively tracked using project tracking tools.
   * Assign owners and timelines for resolution, ensuring issues are closed in a timely fashion.
2. **IV&V Status Updates at Milestones**:

   * Confirm IV&V findings are presented at milestone reviews, enabling them to serve as an additional indicator of status and performance.
3. **Progress Monitoring**:

   * If the project is not addressing IV&V findings promptly:
     + Elevate this through the assurance chain of command for visibility and resolution prioritization.
     + Ensure risks related to delayed closure are clearly documented and presented to decision-makers.

### 7.4.3 Risk Identification and Documentation

1. **Map Software Risks to IV&V Findings**:  
   SA personnel should identify specific software risks associated with IV&V findings, issues, and concerns. These risks should:

   * Be documented alongside mitigation and management plans.
   * Be categorized based on severity and lifecycle phase for alignment with project risk registers.
2. **Analyze Unaddressed Findings**:

   * Assess IV&V findings that have not yet been mitigated or accepted by the project team.
   * Identify the impacts on mission reliability, schedule, cost, and compliance.

### 7.4.4 Comparison and Assessment

1. **Assess SA Processes Against IV&V Findings**:

   * Review the findings, issues, and concerns submitted by IV&V and compare them to those identified independently through SA assessments.
   * Identify gaps where SA has failed to uncover findings raised by IV&V.
2. **Evaluate Why SA Missed Findings**:

   * Perform root cause analysis to understand why SA overlooked findings flagged by IV&V.
   * Improve SA processes as necessary to align with IV&V methodologies and practices, ensuring more robust identification of potential risks.

### 7.4.5 Enabling Improvements in SA Practices

1. **Feedback Loop for SA Improvement**:

   * Use IV&V findings to strengthen SA methodologies by incorporating lessons learned.
   * Integrate identified gaps into training, tools, and criteria for future SA reviews.
2. **Collaborative Risk Disposition**:

   * Maintain iterative collaboration with IV&V personnel to ensure consensus is achieved on risk status, mitigation approaches, and closure criteria.

### 7.4.6 Further Recommendations

#### **Continuity of Process**:

Ensuring the seamless handling and disposition of IV&V findings requires:

* Periodic audits of tracking systems to confirm all findings are dispositioned appropriately.
* Bi-directional communication between IV&V and SA to avoid duplicated efforts and gaps in coverage.
* Documentation of key decisions related to IV&V findings and risks for traceability.

#### **Responsiveness and Accountability**:

Ensure timely responses to IV&V issues and risks submitted. Delays in addressing findings can increase project risks, reduce stakeholder confidence, and impact mission outcomes.

### 7.4.7 Benefits of Adhering to Guidance

#### **For the Project**:

* Earlier identification and mitigation of risks that could jeopardize mission-critical software performance or safety.
* Consistent tracking of issues and risks ensures no concerns are overlooked.

#### **For Stakeholders**:

* Increased transparency and trust in the assurance process through timely and effective tracking and resolution of IV&V findings.

#### **For Mission Success**:

* Greater confidence in software quality and reliability, reducing risk exposure and enhancing mission readiness.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

# 8. Objective Evidence

To demonstrate compliance with this requirement, **objective evidence** must be gathered to show that the project manager responded to issues and risks submitted by the IV&V team, tracked their status, and ensured closure. Below are examples of acceptable evidence categories and specific artifacts that can be used to verify compliance.

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

By systematically documenting and organizing objective evidence, small projects can ensure compliance with Requirement 3.6.5, while also improving communication, collaboration, and efficiency in managing IV&V-submitted issues and risks.

## 8.1 IV&V Issue and Risk Tracking Log

* **Description:** A tracking mechanism that documents all issues and risks raised by the IV&V team and their current status.
* **Examples of Evidence:**
  + A spreadsheet or database (e.g., in Excel or Google Sheets) detailing:
    - Issue/Risk ID.
    - Description of the issue or risk.
    - Severity level (e.g., critical, high, medium, low).
    - Date identified by the IV&V team.
    - Assigned owner (the person/team responsible for resolving it).
    - Status (e.g., Open, In Progress, Resolved, Closed).
    - Closure evidence (e.g., test report, code updates).
    - Resolution date and sign-off (from both the project and IV&V teams).
  + Screenshots from project management tools (e.g., JIRA, Trello, Microsoft Planner) showing tracked IV&V-raised risks and their statuses.

## 8.2 Acknowledgment and Response Records

* **Description:** Documentation confirming that the project acknowledged and responded to issues and risks submitted by the IV&V team.
* **Examples of Evidence:**
  + Email communications or meeting minutes indicating acknowledgment of IV&V-raised issues, along with the project manager's initial responses.
  + Formal response documents summarizing how the project team plans to address the IV&V-raised issues and risks.
  + Response timelines (e.g., tracking logs indicating the date when the issue was acknowledged and when a response was provided).

## 8.3 Corrective Action Plans

* **Description:** Plans that outline specific actions to be taken to mitigate or fix the IV&V-raised risks and issues.
* **Examples of Evidence:**
  + Action plans or detailed responses for addressing specific IV&V-raised risks or issues.
  + Root Cause Analysis (RCA) reports for critical or high-priority defects.
  + Risk mitigation strategies, including timelines and owners for each action item.
  + Impact assessments showing the schedule, cost, or performance implications of addressing the IV&V-raised concerns.

## 8.4 Closure Artifacts and Evidence

* **Description:** Documentation proving that issues and risks raised by IV&V were successfully resolved and closed with approval from both the project team and the IV&V team.
* **Examples of Evidence:**
  + Test or verification reports verifying that corrective actions have been successfully implemented.
  + Meeting minutes where the closure of the issue or risk was discussed and approved.
  + Formal closure approvals or sign-off documentation from IV&V (e.g., signoff emails or "Resolved/Closed" status in tracking tools).
  + Change Request (CR) closure records associated with IV&V-identified risks or issues.

## 8.5 Communication and Collaboration Records

* **Description:** Evidence of consistent communication and collaboration between the project team and the IV&V team regarding submitted issues and risks.
* **Examples of Evidence:**
  + Regular IV&V status reports or risk reports submitted to the project team with open issues.
  + Meeting agendas, minutes, or action items showing discussions on addressing IV&V issues/risks.
  + Issue progress updates sent via email, team channels, or shared collaboration tools (e.g., Slack, Microsoft Teams).
  + Risk Review Board (RRB) or Configuration Control Board (CCB) meeting documentation showing IV&V-related risk discussions.

## 8.6 Risk Management Documentation

* **Description:** Evidence that IV&V-raised risks were integrated into the overall project’s risk management process and tracked within the project’s risk register.
* **Examples of Evidence:**
  + Updated risk registers including IV&V-raised risks, with fields such as:
    - Risk description.
    - Probability and impact assessments.
    - Mitigation actions.
    - Risk status (e.g., Active, Mitigated, Retired).
  + Links between IV&V-raised risks and corrective actions (e.g., references to task tickets or trackers).
  + Risk matrices showing how IV&V-raised risks have been prioritized and managed.

## 8.7 Tools and System Access Logs

* **Description:** If an automated tool was used to track IV&V issues and risks, system-generated evidence can demonstrate project compliance.
* **Examples of Evidence:**
  + Access logs showing that IV&V had visibility into the tracking system (e.g., JIRA, Bugzilla, Trello).
  + Risk escalation notifications within the tool, showing that project managers reviewed and responded to IV&V risks.
  + Status change logs or history records showing the progress and closure of IV&V-raised tickets/issues.

## 8.8 Lessons Learned and Process Improvement Evidence

* **Description:** Evidence of how the project team documented lessons learned and potential process improvements related to managing IV&V-raised issues and risks.
* **Examples of Evidence:**
  + Lessons Learned documents summarizing:
    - Challenges encountered with IV&V issue tracking.
    - Resolution outcomes.
    - Recommendations to improve future issue/risk resolution processes.
  + Post-project retrospective reports identifying successes and areas for improvement in collaboration with the IV&V team.

## 8.9 Verification and Validation of Deliverables

* **Description:** Evidence that deliverables affected by IV&V-raised issues were updated and validated to address the concerns.
* **Examples of Evidence:**
  + Updated requirements specifications, system designs, or user manuals reflecting changes made in response to IV&V-raised issues.
  + Regression test results showing that defects raised by IV&V have been resolved and no new issues were introduced.
  + Updated baseline change records with version numbers for affected deliverables and sign-offs.

## 8.10 Schedule and Milestone Alignment

* **Description:** Evidence that IV&V-raised issues were managed within the project’s constraints (e.g., deadlines, milestones).
* **Examples of Evidence:**
  + Project schedules or Gantt charts showing tasks related to resolving IV&V-raised risks/issues.
  + Milestone review reports confirming that all IV&V-raised issues were addressed before specific milestones (e.g., Critical Design Review, Test Readiness Review).
  + Email communications or meeting minutes confirming alignment between IV&V risk reviews and project milestones.

## 8.11 Summary Table of Objective Evidence

| **Category** | **Objective Evidence Examples** |
| --- | --- |
| **Issue Tracking** | IV&V Issue and Risk Tracking Log, tool screenshots (e.g., JIRA, Trello), Excel/Google Sheets tracker. |
| **Acknowledgment Records** | Emails or meeting minutes confirming acknowledgment of issues, formal risk response documents. |
| **Corrective Action Plans** | Action plans, root cause analyses, risk impact assessments. |
| **Closure Evidence** | Test results, meeting minutes confirming closure, sign-off emails, closure reports. |
| **Communication Logs** | Email threads, meeting agendas/minutes, shared discussion logs (e.g., Slack, Teams), Risk Review Board documentation. |
| **Risk Management** | Updated risk registers, risk matrices showing prioritization, and links to mitigation actions. |
| **Tool Logs** | System records showing issue activity, tool access logs, status update histories. |
| **Lessons Learned** | Retrospective reports, recommendations for future management of IV&V issues. |
| **Verification Artifacts** | Updated deliverables (e.g., design specs, requirements), regression test results, baseline change requests. |
| **Schedule Alignment** | Project schedules indicating IV&V issue mitigation tasks, milestone approval reports. |

## 8.12 Best Practices for Managing Objective Evidence

1. **Centralize Documentation:** Maintain all IV&V-related documentation and evidence in a shared repository (e.g., SharePoint, Google Drive, Confluence) for easy access and review.
2. **Update Regularly:** Ensure the IV&V Issue and Risk Tracking Log is updated on a regular basis (e.g., weekly) to reflect the current status of all risks and issues.
3. **Involve IV&V:** Share all tracking and closure evidence with IV&V to ensure their approval is documented.
4. **Be Proactive:** Address issues as early as possible to minimize impact on the project schedule and resources.
