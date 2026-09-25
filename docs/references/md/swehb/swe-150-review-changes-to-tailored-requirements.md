# SWE-150 - Review Changes To Tailored Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695506. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements

SWE-150 - Review Changes To Tailored Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695506)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695506&showCommentArea=true&showComments=true#addcomment)

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

2.2.7 The engineering, CIO, and SMA authorities shall review and agree with any tailored NPR 7150.2 requirements per the requirements mapping matrix authority column. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-150 History

SWE-150 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 2.2.10 Technical Authorities for requirements in this NPR shall review any tailored requirements whenever changes in project software plans or technical scope are made. |
| Difference between B and C | More specific on who the "Technical Authorities" are by replacing the term with "engineering, CIO, and SMA authorities";  Removed the requirement for "whenever changes in project software plans or technical scope are made" and added "per the requirements mapping matrix authority column." |
| C | 2.2.7 The engineering, CIO and SMA authorities shall review and agree with any tailored NPR 7150.2 requirements per the requirements mapping matrix authority column. |
| Difference between C and D | No Change |
| D | 2.2.7 The engineering, CIO, and SMA authorities shall review and agree with any tailored NPR 7150.2 requirements per the requirements mapping matrix authority column. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

To ensure that all technical authorities agree with the risk associated with any tailored NPR 7150.2 requirements.

The need for **Engineering**, **Chief Information Officer (CIO)**, and **Safety and Mission Assurance (SMA)** authorities to **review and agree** on any tailored NPR 7150.2 requirements, as outlined in the **Requirements Mapping Matrix (RMM) authority column**, ensures alignment, accountability, and oversight across the diverse technical, safety, and cybersecurity domains critical to NASA's software projects. This requirement has several important justifications:

---

### **1. Ensures Proper Oversight and Alignment Across Domains**

Tailoring requirements in NPR 7150.2—whether through deviations, waivers, or adjustments—affects the technical implementation, safety protocols, and cybersecurity postures of a project. The inclusion of Engineering, CIO, and SMA authorities ensures that:

* **Engineering Authority (ETA)** ensures the technical feasibility and compliance with mission-critical design needs and performance requirements.
* **CIO Authority** ensures that cybersecurity, data integrity, and IT-related standards are not compromised during tailoring.
* **SMA Authority** ensures that safety, mission assurance, and system hazards are appropriately evaluated for risk and mitigated.

This multidisciplinary approach ensures that tailoring decisions balance technical functionality, mission safety, and cybersecurity, avoiding siloed decision-making while promoting a unified risk assessment.

---

### **2. Promotes a Comprehensive Risk Management Approach**

Each authority represents a unique focus area of risk:

* **Engineering Risk** focuses on system integration risks, technical performance risks, and downstream implications for software reuse or extensibility.
* **SMA Risk** emphasizes safety-critical hazards (e.g., software failure modes, potential risks to humans or hardware) and evaluates the adequacy of mitigations for safety concerns.
* **CIO Risk** addresses threats to cybersecurity and IT-specific vulnerabilities, such as unauthorized access to data, insufficient encryption methods, and compliance with FIPS and NIST standards.

By requiring *all three authorities* to review and agree on any tailored requirements, NASA creates a formal mechanism where risks are viewed through multiple lenses. This multidisciplinary review substantially reduces the chances of missed risks. Tailoring decisions are only considered valid when all relevant stakeholders formally acknowledge and agree to the associated risks and mitigations.

---

### **3. Provides Accountability and Transparency**

The inclusion of all relevant Technical Authorities during requirement tailoring ensures individual accountability and collective ownership of decisions. This process:

* **Prevents unilateral tailoring**: No single authority can overlook critical risks or approve adjustments without input from others.
* **Documents decision-making**: Requirements Mapping Matrices (RMMs) serve as a centralized and traceable record of tailoring decisions, complete with documented approvals from all required authorities.

Accountability ensures that decisions are justified, risks are clearly communicated, and the tailoring process is not misused or improperly implemented.

---

### **4. Supports Mission Success and System Assurance**

Software requirements in NPR 7150.2 are designed to support **NASA’s critical missions**, where even minor deviations can result in risks to safety, performance, budgets, or long-term mission goals. Tailoring requirements introduces a potential for misalignment with these overarching objectives, particularly in software categories like:

* **Class A** (Human-rated systems or mission-critical systems).
* **Class B** (High-priority missions, including controlled payloads).

By mandating the agreement of Engineering, SMA, and CIO authorities, NASA ensures:

* Tailoring decisions **do not compromise mission-critical functionality**.
* Safety-critical and cybersecurity concerns are not overlooked in favor of expedience.
* Software meets the operational standards necessary to ensure mission success.

---

### **5. Protects Cybersecurity Throughout the Software Lifecycle**

Tailored requirements in NPR 7150.2 can directly impact software’s cybersecurity posture. The **CIO Authority’s involvement** guarantees:

* Mitigation of vulnerabilities introduced through tailored cybersecurity controls (e.g., in authentication, encryption, or logging practices).
* Compliance with NASA IT security standards, such as NPR 2810.2 or applicable NIST Special Publications.
* Protection of software against risks that could manifest later in the lifecycle, including retirement or disposal phases.

Including the CIO ensures cybersecurity considerations remain a **first-class concern** alongside engineering and safety risks, preventing vulnerabilities that could compromise national assets, data integrity, or project confidentiality.

---

### **6. Consistency with NASA Guidance and Lessons Learned**

This requirement aligns directly with key lessons from NASA’s historical failures and risk management practices:

* The **Columbia Accident Investigation Board (CAIB)** observed that "safety and engineering organizations were not sufficiently independent" during critical tailoring and safety-related decisions. This requirement addresses that shortfall by ensuring **independent review and agreement** across the engineering, safety, and IT/cyber disciplines.
* The **Mars Polar Lander failure (1999)** highlighted the importance of cross-disciplinary reviews for tailored requirements. Missing checks (e.g., hazards associated with software control systems) due to inadequate tailoring contributed to the mission's loss.
* Risk analysis from past **cybersecurity incidents** across NASA projects underscores the importance of aligning software tailoring decisions with the CIO to address evolving threats, ensuring that cybersecurity-related tailoring is thoroughly assessed.

Thus, harmonizing these reviews among Engineering, SMA, and CIO authorities mitigates risks evident in NASA’s previous lessons learned.

---

### **7. Enhances Adaptability While Maintaining Rigor**

NASA’s tailoring process allows projects flexibility to align requirements with unique circumstances, resource constraints, or mission scopes. However, with flexibility comes risk. By requiring approval from the Engineering TA, SMA TA, and CIO, NASA ensures:

* Tailoring remains **reasoned, justified, and controlled**.
* Flexibility does not come at the cost of increased safety, cybersecurity, or mission failure risks.
* Small and large projects alike are held to the same rigorous *evaluation criteria*.

This ensures that while projects can tailor to meet schedule, resource, and workflow constraints, they do not sacrifice the robustness of NASA’s requirements.

---

### **8. Harmonizes Interdisciplinary Collaboration**

Software engineering often intersects with multiple disciplines, including safety, systems engineering, and IT infrastructure. Tailoring decisions affect all these disciplines, so it is critical to ensure:

* Collaboration between Engineering, SMA, and CIO avoids oversights caused by disconnected decision-making processes.
* Disputes between authorities are handled appropriately using the **Technical Authority process**, ensuring resolution through NASA's governance structure.

This collaboration fosters **systemic alignment**, breaking potential silos and ensuring all changes remain mission and safety-focused.

---

### **Key Benefits of This Requirement**

1. **Risk Mitigation**: Multidisciplinary review ensures that all risks—technical, safety-related, and cybersecurity—are evaluated and mitigated.
2. **Mission Assurance**: Aligning tailoring decisions with cross-disciplinary input ensures tailored requirements support mission goals without compromising software's role in mission success.
3. **Accountability**: Formal agreement among all three authorities creates documented responsibility for tailoring decisions.
4. **Cybersecurity**: CIO involvement ensures the increasing cyber threats to NASA’s software are considered and addressed.
5. **Alignment with NASA Culture**: Maintains the rigor of NASA’s technical and safety culture while still allowing flexibility through tailored requirements.

---

### **Conclusion**

Requiring the **Engineering**, **CIO**, and **SMA Authorities** to collaboratively review and agree on tailored NPR 7150.2 requirements ensures a disciplined and comprehensive approach to risk evaluation, accountability, and alignment with mission objectives. This requirement balances flexibility with NASA’s high standards for technical excellence, safety, and cybersecurity while fostering collaboration across technical domains that drive mission success.

# 3. Guidance

Software projects often require tailoring of NPR 7150.2 requirements to accommodate specific project needs, technical constraints, or unique operational challenges. However, as a project evolves, changes in the **technical scope**, **schedule**, or **project plans** may invalidate the original rationale for approved tailored requirements. This guidance emphasizes the importance of re-assessing tailored requirements when significant changes occur and outlines a clear, actionable process.

**Purpose**:  
This guidance ensures that tailored requirements remain appropriate, valid, and consistent with the updated scope, risks, and mission objectives of the project. It helps prevent risks to safety, quality, technical performance, and mission success that could arise from outdated or incorrectly tailored requirements.

## 3.1 Re-Assessment of Approved Tailored Requirements

1. **When to Re-Assess**:  
   If a project experiences a **change in technical scope or planned activities**, particularly changes of 10% or more, or incorporates significant modifications to its plans, the **Technical Authorities (TAs)** responsible for the tailored requirements (per NPR 7150.2) must **re-assess the tailoring justifications**. The purpose of this re-assessment is to confirm:

   * The original rationale remains valid.
   * The tailored requirement continues to meet the evolving needs of the project.
   * Risks introduced by the changes are properly addressed and mitigated.
2. **Rationale for Re-Assessment**:  
   Tailored requirements are based on specific project conditions and constraints at the time of approval. If those conditions change, the tailoring may no longer align with mission objectives, safety-critical or cybersecurity requirements, or broader NASA goals. Re-assessment ensures:

   * The tailored requirements remain risk-informed.
   * Critical needs are not overlooked due to previously approved tailoring decisions.
3. **Process**:

   * The project team revisits the **justification materials** provided for the tailoring request, including:
     + Rationale during the initial request.
     + Risk evaluation (which must now be updated to reflect the scope or plan changes).
     + Supporting documents (e.g., technical analyses, simulations, compliance assessments).
   * Re-assessment follows NASA’s systematic review approach:
     + Evaluate if the changes **invalidate the tailoring rationale** (e.g., an approved deviation may no longer apply due to increased software complexity).
     + Assess new project risks due to scope or plan changes (e.g., changes in software reuse plans may increase technical or integration risks).
   * **Technical Authorities involved in the original tailoring approval**—such as Engineering TA (ETA), Safety and Mission Assurance TA (SMA TA), and CIO for cybersecurity—must be consulted during the re-assessment to ensure multidisciplinary input.
4. **Documentation**:

   * Update the tailored requirement’s justification (e.g., rationale, revised risk evaluations, and supporting documents).
   * Archive any updates via the project’s **configuration management system** as part of its formal records.

## 3.2 Triggers for Re-Assessing Tailored Requirements

Not all changes within a project require a re-assessment of tailored requirements. However, the following triggers indicate when a review is warranted. The **impact of the change** should be evaluated collaboratively by the project management and the Technical Authorities to determine whether the tailoring requires re-validation or modifications.

#### **Trigger Categories** (Non-Exhaustive):

1. **Organizational and Resource Changes**:

   * Changes in selected **suppliers or providers** (e.g., subcontractors tasked with software development or delivery).
   * **Significant changes in the project budget**, such as funding cuts or increases, that may affect software development timelines, resources, or scope.
   * **Changes in availability** of critical tools, models, simulations, systems, or facilities integral to validating tailored requirements.
2. **Project Plan Changes**:

   * **Schedule Changes**: Introduction of new development or delivery timelines, particularly for critical technologies or milestones.
   * Addition or deletion of **key features and functions** impacting software scope (e.g., expanding software to include a new module).
3. **Technical and System-Level Changes**:

   * Changes in the **application environment** (e.g., deployment in a new platform, change in embedded hardware constraints).
   * Updates to **safety-criticality** status (e.g., software originally not deemed safety-critical now becomes part of a system with significant safety risks).
   * A change in the **software classification** (e.g., from Class C to Class A, which has stricter requirements).
   * Changes in the **complexity** of the software or the system that it supports.
   * Updates in planned **software reuse** (e.g., tailoring may need re-evaluation if the software is now intended for use on multiple missions).
4. **Justification-Specific Changes**:

   * Changes to any assumptions, constraints, or supporting material used to justify the tailored requirement.

---

### **Post-Re-Assessment Actions**

Following the re-assessment of tailored requirements, the project team, in collaboration with the Technical Authorities, must perform the following actions:

1. **Document and Manage Changes**:

   * **Capture updated justifications** for any tailored requirements, particularly reflecting the adjusted rationale or new risk evaluations. Ensure these updated records are configuration-managed to maintain traceability.
   * Record all **revised approvals** if Technical Authorities make changes to previously approved tailoring decisions.
2. **Update Project Documentation**:

   * Review and **update project plans** and other associated documents (e.g., risk registers, mitigation plans) to reflect any changes to approved tailored requirements.
   * Update the **NPR 7150.2 compliance matrix** to reflect adjustments made during the re-assessment.
3. **Inform Relevant Stakeholders**:

   * Notify the **project team**, **management**, and relevant stakeholders (e.g., developers, contractors) of any changes to the approved tailored requirements to ensure timely compliance and implementation. Document communication records to ensure awareness and action.
4. **Ensure Ongoing Compliance**:

   * Monitor implementation of the updated tailored requirements to ensure they align with the revised project scope and constraints.
   * Continue collaborating with relevant Technical Authorities throughout the project lifecycle.

---

### **References for Additional Guidance**

* **Appendix C (NPR 7150.2)**: Details the requirements mapping and compliance matrix for software classification and tailoring.
* **SWE-121 - Document Tailored Requirements**: Defines the expectations for documenting tailored software requirements.
* **SWE-125 - Requirements Compliance Matrix**: Provides specific guidance on compliance matrix management.
* **SWE-126 - Tailoring Considerations**: Outlines key considerations for tailoring NPR 7150.2 requirements effectively.

---

### Key Takeaways:

* Tailored requirements are only valid under the conditions and constraints present at the time of approval. Significant changes to the project require a systematic re-assessment to ensure tailored requirements remain justified.
* A collaborative, multidisciplinary evaluation with **Technical Authorities** (Engineering, SMA, and CIO authorities) strengthens NASA’s approach to risk mitigation and safety assurance.
* The resulting updates must be well-documented, reflected in project plans, and clearly communicated to all relevant stakeholders to ensure ongoing compliance.

This structured reassessment approach reduces the likelihood of **gaps or hazards** introduced by invalid tailored requirements and aligns all project elements with NASA’s high standards for **safety**, **mission success**, and **cybersecurity**.

**NASA Space Flight Program and Project Management Requirements - NPR 7120.5F**

“The request for relief from a requirement includes the rationale, a risk evaluation, and reference to all material that provides the justification supporting acceptance.”[082](#_tabs-<p></p>)

See also [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix), [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements), [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix), [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations).

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Process Selection](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Process+Selection) |

# 4. Small Projects

Small projects often operate with fewer resources, smaller teams, and shorter timelines, but they are not exempt from the need to rigorously manage tailored requirements per NPR 7150.2. Tailored requirements allow small projects to stay nimble and efficient, but they must regularly validate that these adjustments are still appropriate, especially when changes occur in the project’s **technical scope**, **plans**, or **risks**.

This streamlined guidance is designed to help small projects efficiently, yet effectively, review and re-assess tailored requirements when changes occur.

---

### **Simplified Approach for Small Projects**

When the project’s tailored requirements are impacted by changes in **technical scope**, **project plans**, or other major factors, small projects can use the following process to ensure compliance while maintaining reasonable overhead:

---

#### **1. Identify Trigger Events for Re-Assessment**

Small project managers and technical leads should proactively monitor for **trigger events** that indicate a need for re-assessment of tailored requirements. For small projects, specific triggers to watch for include:

* **Supplier/Provider Changes**: If software development has switched to a new vendor or collaborator, the original justification for tailoring may no longer apply.  
  *(Example: A new provider may lack the tools or processes originally cited in the tailoring rationale.)*
* **Significant Schedule Changes**: If development milestones shift significantly, ensure the time-based assumptions justifying the tailoring remain valid.  
  *(Example: An extended schedule may allow compliance with a previously waived design requirement.)*
* **Budget Changes**: If major budget increases or cuts modify available resources or efforts, reassess the feasibility of addressing requirements initially waived through tailoring.  
  *(Example: Budget constraints may have initially justified a deviation, but a larger available budget could make compliance possible.)*
* **New Features or Functions**: Adding or removing major software features may introduce additional risks or change criticality levels that invalidate previous tailoring.  
  *(Example: Adding new safety-critical features may require compliance with stricter requirements.)*
* **Classification Changes**: A change in software classification (e.g., from Class D to Class C) will invoke more stringent NPR 7150.2 requirements that need immediate review.
* **Planned Software Reuse Updates**: If software scoped for single-use will now be reused in future missions, the original tailoring rationale might not address the long-term software quality and integration requirements vital for reuse.

These triggers should prompt a rule-of-thumb check: *“Does this change impact the original rationale or justification for the tailored requirements?”*

---

#### **2. Conduct a Lightweight Re-Assessment**

For small projects, a **lightweight process** can be used to re-assess tailored requirements without adding unnecessary complexity or delay. Follow these steps:

1. **Review the Justification for Approved Tailored Requirements**:

   * Revisit the project's **Requirements Mapping Matrix (RMM)** and the rationale originally approved for tailoring.
   * Identify if any specific conditions or assumptions (e.g., resource limitations, non-safety-critical classifications, schedule priorities) have changed as a result of the triggering event.
2. **Update the Risk Evaluation**:

   * Perform an informal qualitative risk re-evaluation:
     + What **risks** are newly introduced or no longer valid due to the project changes?
     + Are the existing **risk mitigations** still adequate or do they need adjustment?
   * Use simple tools, such as low/medium/high probability and impact charts for small projects, to assess risks against mission objectives.
3. **Consult Technical Authorities (TA)**:

   * Although small projects often operate with fewer stakeholders, it is critical to consult the appropriate **Engineering TA**, **SMA TA**, and **CIO TA** (if cybersecurity is involved).
   * Ensure each TA reviews the re-assessment to validate risks and provide input on necessary changes to requirements.
   * If your project doesn’t have dedicated Technical Authorities at your center, collaborate with center-level experts to ensure an independent perspective.
4. **Document Changes**:

   * Capture updates to the tailoring rationale, including any newly identified risks and mitigations, in the project’s **project records** or **compliance matrix**. Simplify documentation by aligning updates with existing project logs or using shared documentation templates.

---

#### **3. Update and Communicate Changes**

After completing the re-assessment, small projects should take these actions to document and share the updated information:

1. **Update the Compliance Matrix**:

   * Reflect any changes to tailored requirements in the **Requirements Mapping Matrix (RMM)**.
   * If new “tailored” or “not applicable” statuses are necessary, ensure they are justified according to the updated scope or plans.
2. **Update Relevant Project Documentation**:

   * Revise **project plans**, **technical designs**, or associated documents that reference tailored requirements.
   * Update **risk management documentation** to reflect changes determined during the re-assessment.
3. **Communicate Changes to Stakeholders**:

   * Notify your core project team, management, and key stakeholders of any new or revised tailored requirements.  
     *(For example: If a safety-critical requirement is re-applied, implementation tasks must be immediately updated to reflect this change.)*

---

### **Simplified Triggers for Small Projects**

While large projects may encounter significant formal changes, small projects should focus on the following simplified list of common triggers for re-assessing tailored requirements:

* New or removed key software features or functions.
* Transition to a smaller or larger provider/vendor for software development.
* Budget or schedule changes affecting the project's capacity to meet or exceed tailored requirements.
* Updates to **tools**, **models**, or **test environments** that affect the original tailoring context.
* Changes to **software classification** or **safety-criticality** as the project evolves.

---

### **Key Best Practices for Small Projects**

1. **Plan Early for Re-Assessment Needs**:

   * Incorporate periodic reviews into project timelines (e.g., during key milestones like Preliminary Design Review (PDR) or Critical Design Review (CDR)) to reduce the risk of missing triggers that require re-assessment.  
     *(For small projects, milestone meetings can double as review checkpoints.)*
2. **Leverage Simple Processes and Documentation**:

   * Utilize **Center-provided templates** or **compliance matrix examples** to streamline documentation. This minimizes time spent on administrative tasks while ensuring clarity and compliance.
3. **Engage Key SMEs Early**:

   * Informal consultations with TAs (or center-level experts) reduce the uncertainty of whether re-assessments are needed and speed up the process.
4. **Avoid Over-Tailoring**:

   * For small projects, reducing tailoring requests during the initial planning phase reduces the burden of ongoing re-assessments. Where possible, align with NPR 7150.2 requirements to simplify long-term compliance.
5. **Make Re-Assessments Proactive, Not Reactive**:

   * Proactively identifying the need to re-assess tailoring reduces the risk of rushing corrections late in the project lifecycle, which could increase costs or risks to mission success.

---

### **Summary of Small Project Process**

| **Step** | **Action** |
| --- | --- |
| **Identify Changes** | Look for trigger events (e.g., scope changes, classification updates, safety-criticality changes). |
| **Re-Assess Tailored Requirements** | Perform a lightweight re-evaluation: Check justification, update risk assessments, consult TAs. |
| **Update Compliance Matrix** | Modify the RMM to reflect any new or revised tailored requirements. |
| **Document Updates** | Update relevant project records, risk registers, and requirements documentation. |
| **Communicate Changes** | Notify all relevant stakeholders of updated requirements to ensure implementations are adjusted as needed. |

By streamlining this process, small projects can maintain compliance with NPR 7150.2 while minimizing resource strain and ensuring tailoring decisions remain appropriate throughout the project’s lifecycle.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,

### 5.2 Tools

  

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The re-assessment of tailored requirements is a critical process for ensuring that project outcomes align with NASA’s stringent safety, mission success, and system integrity standards. Past NASA missions and studies have revealed several key lessons related to managing tailored requirements effectively, which serve as guides for handling changes in scope, risks, or technical context.

Here are relevant NASA lessons learned that emphasize the importance of re-assessing tailored requirements for evolving project conditions:

---

### **1. Columbia Accident Investigation Board (CAIB) Report, Vol 1, 2003 – Lesson: Rigorous Oversight of Tailored or Waived Requirements**

#### **Lesson Summary:**

The CAIB report stressed that a lack of independent oversight and systematic re-validation of requirements contributed to the **Columbia disaster**. Specifically, safety decisions were made without re-assessing prior assumptions about risks, and waivers and deviations from requirements were not systematically reviewed when project conditions changed.

#### **Relevance to Tailored Requirements Re-Assessment:**

* Tailored requirements, particularly those that exclude critical safety or risk-driven standards, must be re-assessed when **project scope or risks change**.
* Systematic and multidisciplinary reviews ensure that waived or tailored requirements are still appropriate under updated project conditions, reducing the likelihood of safety hazards going unnoticed.
* This underscores the need to consult Technical Authorities (TAs) and maintain continuous visibility over tailored requirements, as required by NASA's NPR 7150.2.

#### **Key Takeaway:**

When tailoring requirements, projects must formalize re-assessment protocols for changes in technical parameters, scope, or mission risks. Decisions made early in the project may become invalid under new conditions and must be revisited promptly.

---

### **2. Mars Climate Orbiter Failure (1999) – Lesson: Inadequate Validation of Evolving Assumptions**

#### **Lesson Summary:**

The loss of the Mars Climate Orbiter occurred in part due to unvalidated assumptions made during the integration of systems. Requirements for development and testing were tailored based on constraints known early in the project, but the tailoring did not account for changes in system complexity as the mission progressed.

#### **Relevance to Tailored Requirements Re-Assessment:**

* **Changing project complexity**: If a project adds new features or becomes more complex due to scope evolution, initially justified tailored requirements may omit critical integration or testing standards, leading to failures.
* The Mars Climate Orbiter emphasized the importance of continuous review of tailored decisions, especially when significant changes occur in project integration, interfaces, or applied technologies.
* Requirements re-assessment is critical to ensuring assumptions remain valid throughout the lifecycle, preventing mismatches between the software and the broader system it supports.

#### **Key Takeaway:**

Requirements tailoring that relies on early-stage assumptions must be revalidated during re-assessment to address **updated project risks**, especially when technical parameters or system-level requirements evolve.

---

### **3. Lesson Number: 0838 – Risk Management Lessons Learned (Risk Unawareness Due to Tailoring)**

#### **Lesson Summary:**

Projects failed in several instances because of risks being underestimated or overlooked during the tailoring of requirements. The tailoring process left gaps in the implementation of important standards, and changes in project conditions were not accompanied by re-evaluations of those tailored requirements.

#### **Relevance to Tailored Requirements Re-Assessment:**

* Tailored requirements often exempt projects from vital risk-reducing controls, but if risks change during project execution (e.g., due to added functionalities or reclassification of software), a **re-assessment process** ensures the project adapts to these evolving risks.
* For example, safety-critical software planned for a single-use project may evolve into reusable software, requiring adjustments to testing and assurance processes.

#### **Key Takeaway:**

Risk evaluation needs to be proactively revisited as part of tailoring re-assessment to ensure that requirement compliance aligns with the project’s **changing risk profile**.

---

### **4. NASA Constellation Program – Lesson: Early and Continuous Review with Technical Authorities**

#### **Lesson Summary:**

The Constellation Program emphasized the importance of involving **Technical Authorities (TAs)** early in tailoring decisions and maintaining their involvement throughout the project lifecycle. In cases where project scope evolved, project teams benefited from initiating **re-assessments** of previously justified requirements, avoiding unnecessary risks during later lifecycle phases.

#### **Relevance to Tailored Requirements Re-Assessment:**

* Small changes in technical scope or plans can accumulate into significant impacts on risks and safety. Collaboration with TAs ensures requirements remain aligned with evolving mission-critical objectives.
* Consistent collaboration with Engineering, Safety, and Mission Assurance (SMA), and Chief Information Officer (CIO) authorities ensures re-assessments are thorough, especially when project classification, safety-criticality, or system complexity changes.

#### **Key Takeaway:**

Engage TAs early and continuously during tailoring re-assessments to prevent gaps in requirement alignment caused by project changes.

---

### **5. Challenger Disaster / Rogers Commission Report (1986) – Lesson: Assessing the Operational Environment**

#### **Lesson Summary:**

The Rogers Commission Report identified that mission failures can occur when previously tailored or waived requirements are not reassessed in light of **operational changes** or updated risk contexts. The Challenger disaster illustrated the dangers of accepting prevailing decisions without verifying whether the rationale for those decisions was still applicable in a **changing operational environment**.

#### **Relevance to Tailored Requirements Re-Assessment:**

* Tailored requirements based on the current operational context must be reviewed if the environment changes, such as:
  + Introduction of new **features or functions**.
  + Design updates that create dependencies between previously independent systems or software.
* Re-assessing requirements ensures that the risk of cascading failures is reduced when operating conditions evolve.

#### **Key Takeaway:**

Any operational or environmental changes during the project lifecycle should serve as triggers for reviewing the assumptions and justifications for tailored requirements.

---

### **6. Lesson Number: 1122 – Decision Documentation is Critical**

#### **Lesson Summary:**

On several NASA projects, tailoring decisions were made but inadequately documented. This led to confusion during project handovers, integration with other systems, and long-term software reuse. Without clear records, teams could not re-assess tailoring decisions as conditions changed.

#### **Relevance to Tailored Requirements Re-Assessment:**

* Clearly documented justifications and records of tailored requirements provide the necessary context for re-assessment when triggers like scope changes, classification updates, or added system complexity arise.
* Small projects must ensure even lightweight tailoring processes are appropriately documented and archived.

#### **Key Takeaway:**

Proper documentation of initial tailoring decisions reduces the likelihood of misunderstandings during re-assessment and simplifies the re-validation of tailored requirements when triggers for changes occur.

---

### **7. Mars Polar Lander Loss (1999) – Lesson: System Complexity Requires Tailoring Re-Validation**

#### **Lesson Summary:**

The Mars Polar Lander mission highlighted the importance of revisiting tailoring decisions when changes in complexity and functionality were introduced during the project. Tailored testing requirements led to critical gaps in detecting software faults, which ultimately caused mission loss.

#### **Relevance to Tailored Requirements Re-Assessment:**

* Changes in **functionality**, **features**, or **software integration challenges** must be triggers for re-assessing tailored requirements. For example, initially waived testing requirements may require reconsideration when software complexity increases.
* Multidisciplinary reviews during re-assessment ensure that tailored decisions remain effective in mitigating potential failures.

#### **Key Takeaway:**

Tailored requirements must be reviewed when system complexity increases during the lifecycle, ensuring that risks introduced by complexity are adequately mitigated.

---

### **Final Summary: Lessons Learned for Tailored Requirements**

NASA’s historical mission experiences consistently emphasize:

* **Re-Validation**: Tailored requirements must undergo systematic re-assessment when project plans, scope, or risks evolve.
* **Risk Awareness**: Re-assessment ensures risks linked to evolving conditions—such as increased complexity, software classification changes, or new safety-critical features—are addressed.
* **Documentation and Traceability**: Maintaining clear records of tailoring rationale and decisions simplifies future re-evaluations when changes occur.
* **Involvement of Experts**: Multidisciplinary review, especially with Technical Authorities in Engineering, SMA, and CIO, ensures robustness during re-assessment.

Applying these lessons learned strengthens compliance with NPR 7150.2 while protecting project success across small and large endeavors.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

### **Objective of the Guidance**

The purpose of this requirement is to ensure that any tailored requirements in **NPR 7150.2** (NASA Software Engineering Requirements) are properly reviewed, agreed upon, and approved by the relevant authorities:

1. **Engineering Authority** oversees technical feasibility and compliance with software engineering standards.
2. **Chief Information Officer (CIO)** ensures compliance with IT and cybersecurity requirements.
3. **Safety and Mission Assurance (SMA) Authority** validates that tailored requirements meet safety, reliability, software assurance, and quality standards.

**Software Assurance (SA)** personnel are responsible for verifying that this process is followed, ensuring tailored requirements do not compromise safety, cybersecurity, or software quality while meeting the project's specific needs.

---

### **Software Assurance Responsibilities**

---

#### **1. Understand Tailored NPR 7150.2 Requirements**

1. **Review Tailored Requirements**

   * Assess the **Requirements Mapping Matrix (RMM)** to identify tailored requirements (those modified from their original form or designated as “Not-Applicable” or with modified applicability).
   * Understand the project’s rationale for tailoring, including any risks or mitigations documented in the RMM.
2. **Verify Authority Designations in Appendix C**

   * Cross-check the tailored requirements with the **"Authority" column in Appendix C** of NPR 7150.2 to determine which authority (Engineering, CIO, SMA, or a combination) is responsible for reviewing and agreeing with the tailoring.
3. **Assess Alignment with Software Classification**

   * Confirm that the tailored requirements fit the software classification (Class A–E, per **Appendix D of NPR 7150.2**) and that the tailoring rationale is appropriate for the software’s criticality and complexity.

---

#### **2. Verify the Review Process**

1. **Ensure Tailoring Justifications Are Documented**

   * Confirm that the project provides clear and detailed justification for each tailored requirement, including:
     + Why the requirement is being tailored.
     + Any associated risks.
     + Mitigations for those risks.
2. **Ensure Collaboration Among Authorities**

   * Verify that the Engineering and SMA authorities collaborate to review and evaluate the tailored requirements. Collaboration could involve formal tailoring review meetings, individually signed approvals, or electronic agreement via project management systems.
3. **Validate Consistency During the Approval Process**

   * Check that all authorities review tailoring decisions consistently, ensuring that the same standards and evaluation criteria are applied across all tailored requirements.

---

#### **3. Assess Key Focus Areas for Each Authority**

1. **Engineering Authority**

   * Ensure tailored requirements preserve technical feasibility and adhere to NASA’s software engineering standards.
   * Confirm that technical risks introduced by tailoring are adequately mitigated.
2. **Safety and Mission Assurance (SMA)**

   * Confirm tailored requirements maintain safety, reliability, quality, and adherence to assurance standards (e.g., **NASA-STD-8739.8**).
   * Evaluate whether the project addresses any safety-critical risks associated with non-compliance or tailoring.

---

#### **4. Verify Agreement and Approval of Tailored Requirements**

1. **Check for Proper Signatures or Approvals**

   * Verify that the Engineering and SMA authorities officially document their agreement with the tailored requirements. This may include:
     + Signed approvals in the Requirements Mapping Matrix.
     + Approvals within the project’s configuration management or documentation system.
2. **Ensure No Unapproved Tailoring**

   * Confirm that no tailored requirement is deemed final without signed agreement from all designated authorities.
3. **Document Feedback and Iterations**

   * If any authority disapproves a tailored requirement, ensure the project records the rationale for disapproval, along with iterative changes made to address the concerns.

---

#### **5. Monitor Compliance and Traceability**

1. **Track Tailoring Decisions**

   * Maintain records of tailored requirements, their justifications, and associated approvals for future audits and reviews.
2. **Ensure Alignment with NPR 7150.2 Tailoring Processes**

   * Confirm the tailoring process followed the prescribed steps in **NPR 7150.2**, ensuring no step or authority was bypassed.
3. **Include in Software Assurance Records**

   * Archive evidence of authority approvals (e.g., signatures) and risks/mitigations for each tailored requirement as part of the project’s retrievable records.

---

#### **6. Ensure Continuous Involvement**

1. **Ongoing Review During the Life Cycle**

   * Verify that tailored requirements are reviewed and agreed upon at major project milestones (e.g., Preliminary Design Review, Critical Design Review, Test Readiness Review). This ensures tailoring continues to be valid and appropriate for changing project or risk conditions.
2. **Perform Regular Assurance Checks**

   * Audit the project’s adherence to tailored requirements throughout the development and verification life cycle.
3. **Report Non-Compliance**

   * Report any tailoring bypasses, risks not addressed, or omitted authority approvals to appropriate leadership for resolution before project execution proceeds.

---

#### **7. Cybersecurity-Specific Activities**

1. **Involve the SAISO (or Delegate)**

   * Collaborate with the Senior Agency Information Security Officer (SAISO) or their delegate as part of the CIO authority review process to ensure that cybersecurity risks are considered in all tailoring decisions.
2. **Evaluate Potential Cybersecurity Weaknesses**

   * Verify that no tailoring decision compromises critical cybersecurity requirements, even if validated by other authorities.
3. **Track Mitigations**

   * Confirm that tailored cybersecurity provisions include specific mitigation plans and are monitored throughout the life cycle.

---

### **Expected Outcomes**

By following the above guidance, SA ensures that:

1. All tailored requirements comply with NPR 7150.2 tailoring processes and receive agreement from designated authorities (Engineering, CIO, SMA).
2. Tailoring justifications are reasonable, well-documented, and include associated risks and mitigations.
3. Approval signatures are obtained and traceable in the Requirements Mapping Matrix.
4. Cybersecurity considerations are integrated into every tailored requirement.
5. Tailored requirements preserve safety, reliability, technical feasibility, and compliance with NASA standards.

---

### **Summary**

**Software Assurance (SA)** personnel play a key role in verifying that any tailoring of NPR 7150.2 requirements is properly reviewed, justified, and approved by the Engineering, CIO, and SMA authorities as defined in the directive. SA ensures all tailoring decisions are accurate, reasonable, and compliant, while maintaining documentation and traceability throughout the project life cycle. Regular reviews and cybersecurity oversight protect against unacceptable risks and ensure alignment with NASA’s software assurance policies.
