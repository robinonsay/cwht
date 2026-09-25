# SWE-021 - Transition to a Higher Class

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695406. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class

SWE-021 - Transition to a Higher Class

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695406)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695406&showCommentArea=true&showComments=true#addcomment)

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

2.2.8 If a system or subsystem development evolves to meet a higher or lower software classification as defined in Appendix D, then the project manager shall update their plan(s) and initiate modifications to any supplier contracts to fulfill the applicable requirements per the Requirements Mapping Matrix in Appendix C with approved tailoring.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-021 History

SWE-021 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.9 If a system or subsystem evolves to a higher software classification as defined in Appendix E, then the project shall update its plan to fulfill the added requirements per the Requirements Mapping Matrix in Appendix D. |
| Difference between A and B | Added requirements for downgrading software to a lower class and/or changing safety criticality. Added verbiage for having tailoring approved. |
| B | 3.5.4 If a system or subsystem evolves to a higher or lower software classification as defined in Appendix D, or there is a change in the safety criticality of the software, then the project manager  shall update their plan to fulfill the applicable requirements per the Requirements Mapping and Compliance Matrix in Appendix C and any approved tailoring. |
| Difference between B and C | "Added the word development for clarity;  Removed safety criticality as a factor; Changed ""tailoring"" to ""changes"";  Added ""initiate adjustments to applicable supplier contracts to fulfill the modified requirements""." |
| C | 2.2.8 If a system or subsystem development evolves to meet a higher or lower software classification as defined in Appendix D then the project manager shall update their plan to fulfill the applicable requirements per the Requirements Mapping Matrix in Appendix C and any approved changes, and initiate adjustments to applicable supplier contracts to fulfill the modified requirements. |
| Difference between C and D | Reworded requirement for clarity with respect to contracts. |
| D | 2.2.8 If a system or subsystem development evolves to meet a higher or lower software classification as defined in Appendix D, then the project manager shall update their plan(s) and initiate modifications to any supplier contracts to fulfill the applicable requirements per the Requirements Mapping Matrix in Appendix C with approved tailoring. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

This requirement is to ensure that the resulting product does not present safety or other critical issues when delivered and operated.

This requirement ensures that any changes to the **software classification** of a system or subsystem, as outlined in **Appendix D of NPR 7150.2**, are promptly addressed to align with the appropriate levels of required oversight, processes, and controls. Software classification defines the level of criticality, complexity, and risk associated with the software based on its role in the system and mission. As such, the classification impacts the requirements that the software must adhere to, as defined in the **Requirements Mapping Matrix (Appendix C)**.

If a project evolves to a higher or lower software classification, this requirement mandates updates to project plans, processes, and contracts to address the changes in applicable requirements and risks, ensuring mission success, safety, and compliance. Below is a detailed rationale for the requirement:

---

### **1. Ensures Compliance with Updated Standards**

Software classification is a critical factor in determining applicable requirements under NPR 7150.2, as different classifications impose varying degrees of rigor in processes such as **risk management**, **testing**, **documentation**, and **verification**. If a project's classification changes, the project manager must ensure compliance with the updated requirements:

* **Higher Classification**: Elevations in classification (e.g., from Class C to Class B or Class B to Class A) reflect an increase in criticality, risk, or safety requirements that necessitate stricter controls, particularly for **human-rated** systems or those supporting mission-critical operations.
* **Lower Classification**: Reductions in classification (e.g., Class B to Class C or Class D) may warrant tailoring and streamlining of processes to optimize resources without compromising compliance.

Failing to update plans and contracts after classification changes can lead to gaps in the implementation or oversight of requirements, which increases risks related to safety, performance, cybersecurity, or mission success.

---

### **2. Protects Safety-Critical Systems**

Software intended for **safety-critical systems** (Class A/B software) is subject to the most rigorous requirements. If a system’s classification changes to reflect **higher safety-criticality**, plans and contracts must be revised to ensure the supplier delivers to the updated standards. For example:

* **Class A or B software** requires rigorous **verification and validation (V&V)**, fault detection, and reliability testing that may not have been required under a lower classification.
* Contracts for suppliers must incorporate these requirements to guarantee safety-critical aspects are addressed.

By mandating updates to plans and contracts, this requirement helps ensure that the software is adapted to match the additional rigor required for safety-criticality, protecting human life and mission integrity.

---

### **3. Avoids Misalignment Between Project Scope and Contract Requirements**

Projects often rely on external suppliers for software development. If classification changes occur during the lifecycle, supplier contracts and agreements may not reflect these updates unless explicitly revised. Misalignment between the updated classification and the supplier’s deliverables can lead to the following risks:

* Suppliers might not implement newly required processes (e.g., cybersecurity standards, safety-critical testing methods).
* Deliverables may fail to meet required quality and compliance thresholds for higher-class software.

Revising supplier contracts ensures alignment with the updated classification and prevents project delays or rework caused by mismatched expectations or requirements.

---

### **4. Supports Adaptive Risk Management Based on Classification Changes**

Higher software classifications often introduce new risks that require more stringent risk management practices. These risks may stem from factors such as:

* **Increased complexity**: Software supporting a higher-class system may require more complex functionality or integration.
* **Criticality**: Higher classification signifies increased risks related to mission failure or operational safety.
* **Cybersecurity risks**: Higher classified systems may require stricter controls to mitigate threats to critical infrastructure or sensitive data.

Mandatory updates to plans and contracts after classification changes incorporate revised risk evaluations, mitigations, and processes that align with the updated level of risk. Similarly, lowering classification reduces overburdening processes that are no longer necessary for less critical systems, optimizing resources.

---

### **5. Prevents Mission Failure Due to Inadequate Controls**

Historical lessons learned illustrate the dangers of not aligning processes, requirements, and controls with changes in system classification:

* **Mars Climate Orbiter (1999)**: Miscommunication and insufficient requirements for integration testing led to loss of the orbiter. A higher classification might have mandated additional requirements to address these risks.
* **Columbia Disaster (2003)**: Safety-critical systems lacked proper oversight, revealing how insufficient controls for high-class systems increase the risk of mission failures.

Changing classification mid-development is a key trigger for re-evaluating controls, ensuring sufficient coverage and rigor for higher classifications, or streamlining processes for lower classifications.

---

### **6. Ensures Budget, Schedule, and Resource Optimization**

Shifting classifications often impacts resource allocation:

* **Higher classification**: May require additional resources for rigorous processes like independent review, safety assessments, V&V, or multiple testing levels.
* **Lower classification**: Allows greater flexibility to streamline processes, reducing costs and project complexity.

Updating project plans ensures realistic budgets and schedules reflect the classification changes, preventing misallocation of resources and improving efficiency.

---

### **7. Maintains Stakeholder Alignment and Accountability**

A formal process for updating plans and contracts ensures all stakeholders—developers, suppliers, Technical Authorities (Engineering, SMA, CIO), project managers—are aware of classification changes and their implications. This prevents misalignment across teams and ensures accountability for implementing the new requirements.

Stakeholder awareness ensures:

* Suppliers revise deliverables according to the updated requirements.
* NASA teams address risks, documentation, and compliance for the new classification tier.

---

### **8. Formalizes Tailoring Decisions**

The requirement explicitly refers to **approved tailoring of requirements**, ensuring that reclassification does not introduce unwarranted deviations or omissions without proper justification. Tailoring is a critical tool for adapting to changes, but must follow NPR 7150.2 processes to ensure:

* All tailoring decisions are documented.
* Risk evaluations accompany tailored requirements.
* Stakeholders approve the tailoring via the Requirements Mapping Matrix (RMM).

This approach guarantees the integrity of tailoring processes while addressing classification changes efficiently.

---

### **9. Aligns with NPR 7150.2 Requirements Mapping Matrix (Appendix C)**

Appendix C includes detailed mapping of requirements for each software classification, ensuring that higher classifications impose stricter standards while lower classifications streamline less-critical processes. For example:

* Class A software must adhere to stringent **safety, cybersecurity**, and **testing requirements**, while Class C or D software allows tailoring to reduce overhead.

This requirement ensures project managers appropriately adjust project governance to reflect the correct classification tier, improving compliance and accountability across the software lifecycle.

---

### **Key Takeaways**

1. **Compliance Alignment**: Ensures software classifications are aligned with the appropriate NPR 7150.2 requirements, avoiding gaps in critical processes (e.g., for testing, safety, or cybersecurity).
2. **Safety and Mission Assurance**: Elevates safety-criticality controls and verification practices when moving to higher classifications, protecting mission integrity and human life.
3. **Efficient Resource Allocation**: Guarantees resources are optimized based on the updated classification (increased rigor where needed, streamlined processes where appropriate).
4. **Contract Modifications**: Prevents supplier misalignment by ensuring contracts reflect updated requirements for both higher and lower classifications.
5. **Risk Management**: Adapts risk evaluations and mitigations to align with new threats or reduced criticality as classifications change.
6. **Stakeholder Awareness**: Formalizes stakeholder alignment through updated plans and documented tailoring decisions.

By requiring updates to plans and contracts when software classification changes, this requirement enables NASA projects to adapt effectively, ensuring compliance, risk mitigation, and efficient resource utilization as system or subsystem development evolves.

# 3. Guidance

Software projects that begin with a lower classification (e.g., Class E research projects) may evolve to a **higher classification** as project scope, usage, complexity, or mission requirements change. Projects must transition to meet **NPR 7150.2 software engineering requirements** for the higher classification, and ensure updates are made to processes, documentation, and deliverables to reflect the new criticality and risk factors.

This guidance provides improved clarity on how to approach such transitions, handle potential gaps, and ensure compliance with **NPR 7150.2**, while minimizing programmatic and technical risks.

---

### **1. Understanding Valid Software Re-classification Transitions**

#### **Valid Transition Scenarios**

Transitions involve upward classification changes within the **defined boundaries of software classification types**:

* **Engineering Classes (A–F)**: Transitions like Class E (prototype/research software) to Class C (mission-critical engineering software).
* **Business Classes (F–H)**: Transitions like Class H (general business application) to Class F (complex financial system).

#### **Invalid Transition Scenarios**

Classification transitions are strictly limited to the same software domain, either **engineering** or **business** applications. For example:

* A **business classification (Class F)** cannot transition to an **engineering classification (Class D)**. This ensures alignment with software domain requirements, processes, and expectations as defined by NASA’s overall classification approach.

---

### **2. Key Drivers for Re-classification**

Classification changes to a **higher level** are often triggered by critical evolutions in the project. These changes necessitate increased rigor and oversight in software processes, even in non-safety-critical scenarios. The following situations typically trigger reclassification:

1. **Change in Usage of Software**:
   * Transition from a lab or prototype environment to deployment in a flight vehicle or operational mission system.
   * Movement from localized software applications to enterprise-wide or multi-Center use cases.
2. **Increased Human Dependence**:
   * Transitioning software to systems where human life, mission safety, or other mission-critical outcomes depend significantly on software behavior and reliability.
3. **Additional Investment or Scope**:
   * Expanded Agency-wide or program-level investments that increase stakeholder dependencies on software outcomes.
4. **Increased Complexity**:
   * Changes in software architecture, integration, or intended functionality that increase technical or integration risks.

#### **Examples:**

* Moving software from human-in-the-loop laboratory simulations to autonomous operations on a robotic spacecraft.
* Expanding a research application to an enterprise-level decision-support system accessible across multiple NASA Centers.

Even when **safety-criticality** is unchanged, transitions between higher engineering or business classes demand careful **re-assessment of requirements** and rigorous planning.

---

### **3. Key Steps for Re-classifying and Transitioning Software**

Re-classifying software to a higher class involves multiple assessments and updates to ensure rigor, alignment with **NPR 7150.2**, and minimal disruption to project goals. Follow these steps to structure the transition:

### 3.1 Evaluate the NPR 7150.2 Requirements for the New Classification

* Revisit the **requirements compliance matrix** (Appendix C) to determine new requirements based on the updated classification.
* Identify areas where additional rigor (e.g., heightened **verification and validation (V&V)**, documentation, reviews) is necessary for compliance with the higher classification.

### 3.2 Address Waivers and Deviations

* **Review waivers/deviations** granted under the lower classification. Determine if they are still applicable under the higher classification.
* Submit **new waiver/deviation requests** as needed, particularly when processes performed under the lower classification fall short of higher-class requirements.

### 3.3 Conduct a Gap Analysis

* Establish a **gap list** comparing work performed under the original classification to what should have been done under the higher classification from the beginning. Key gaps to examine include:
  + Test coverage and rigor.
  + Documentation (e.g., formal requirement traceability).
  + Risk and hazard analysis.
* Document gaps with risk and mitigation plans for each shortfall.

### 3.4 Perform a Risk and Hazard Analysis

* Work with **Software Assurance and Safety personnel** to evaluate risks introduced by transitioning to the higher classification. Focus on:
  + System risks affected by updated operational scope or conditions.
  + Hazards introduced by incomplete or insufficiently rigorous work from the lower classification.

### 3.5 Update Project Plans

* Revise affected plans to reflect the updated classification and its impact:
  + **Software Development/Management Plan (SDMP)**: Revise development and oversight processes to align with higher classification requirements.
  + **Software Maintenance Plan (if minor updates)** or create a new version for substantial transitions.
* Update resource allocation for gaps introduced by higher-class requirements:

### 3.6 Develop a Transition Strategy

With input from the project team, stakeholders, and Technical Authority staff, craft a strategy to address the transition:

1. Decide whether to **transition the software** or **develop a new solution**.
   * Transitioning software is viable if the cost, time, and resource impact is acceptable and risks can be managed.
2. Evaluate the need for repeating previously completed work.
   * If necessary, repeat critical work (e.g., testing in the operational environment) that might compromise the project’s success if left undone.
3. Allocate additional resources, if needed:
   * Personnel, schedule extensions, funding, tools, and facilities may be required to close identified gaps.

---

### **4. Involvement of the Technical Authority (TA)**

The **Technical Authority (TA)** plays a vital role in overseeing and approving the reclassification process. The TA, with support from Software Assurance and project leads, evaluates and validates the following:

1. **Risk and Hazard Assessment**:
   * Confirms that identified risks are within acceptable tolerances and appropriate mitigation measures are planned.
2. **Transition Strategy**:
   * Approves the approach for meeting higher classification requirements, including the plan to close gaps or transition software.

---

### **5. Special Considerations for Significant Re-classification**

When re-classification results in major changes (e.g., a jump from Class E to Class A or operational software on higher-criticality human-rated systems), engage:

* **Center-level Engineering Technical Authority** for guidance on re-planning.
* **Headquarters-level Engineering Technical Authority**, when needed, for high-profile or safety-critical transitions.
* Evaluate potential updates to **Technology Readiness Levels (TRLs)**, as described in **NPR 7120.8, Appendix J**.

---

### **6. Keeping Plans and Stakeholders Aligned**

The project strategy must involve clear updates to all necessary plans, and documentation should reflect the reclassification in the following ways:

1. Keep **project plans (SDMP, SMP, risk management plans)** current to maintain management visibility and accountability.
2. Communicate updates to key stakeholders, including suppliers, the development team, and oversight groups, to ensure compliance with classification-driven changes.

---

### **Summary of Actions**

| **Task** | **Responsibility** |
| --- | --- |
| Identify updated requirements | Project Manager, Software Lead |
| Conduct gap and risk analysis | Software Assurance and Safety Personnel |
| Update project plans/documents | Software Project Lead and Development Team |
| Define transition strategy | Project Manager, TA, Software Lead |
| Secure required approvals | Technical Authority Team, Stakeholders |
| Allocate additional resources | Project Manager |

Transitioning software to a higher classification ensures alignment with **NPR 7150.2**, protects mission integrity, safety, and system quality, and accounts for evolved project risks and complexities.

See also topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix),

Record keeping requirements for classifications are found in [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records).

See also [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices),

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices) * [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records)        * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Classification](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Classification) |

# 4. Small Projects

This requirement applies to **all projects**, regardless of size, unless a waiver is granted by the appropriate **Technical Authority (TA)**. Small projects with limited financial or personnel resources must take a strategic approach to meet the demands of transitioning to a higher classification. While resource limitations can pose challenges, properly managed transitions ensure compliance with NPR 7150.2 and mitigate risks to safety, mission success, and overall system integrity.

---

### **Key Considerations for Small Projects**

#### **1. Scope the Transition Effort**

Small projects must begin by evaluating the **impact of the classification change** on completed and yet-to-be-performed work.

* **Assess Completed Work**: Identify which activities and deliverables completed under the prior classification no longer meet the rigor required by the higher classification.

  + Examples: Requirements reviews, design documentation, verification plans, test coverage, or risk analysis.
  + Focus on **critical areas** that directly impact mission success, safety, or compliance.
* **Prioritize Remaining Work**: Break down higher classification requirements into **manageable tasks** and prioritize according to their criticality, complexity, and risk significance.

---

#### **2. Perform a Gap Analysis**

A **gap analysis** helps determine where completed work does not meet the higher classification’s requirements. This analysis helps the team focus its limited resources on the activities that provide the greatest value.

* Compare completed activities, processes, and artifacts against the **higher classification requirements** using the **Requirements Mapping Matrix (RMM)**.
* Categorize gaps as:
  1. **Critical Gaps**: Areas that are essential for mission success or compliance (e.g., insufficient safety reviews, incomplete hazard analysis, missing verification artifacts).
  2. **Secondary Gaps**: Non-critical areas where work falls short but poses less overall risk if not repeated.

---

#### **3. Perform a Risk Assessment**

Small projects with constrained resources must weigh the **risks** of not addressing gaps against the cost of performing additional work to meet the higher classification requirements:

* Collaborate with the project’s **Software Assurance (SA)** and **Safety personnel** to identify any mission, safety-critical, or high-risk gaps.
* Evaluate the following:
  + **Consequences of not addressing the gap**: Could this result in system failures, unsafe operations, or non-compliance?
  + **Likelihood of adverse outcomes**: Assess the probability of risks materializing due to unmet requirements.
  + **Mitigation options**: Identify alternative ways to address risks without repeating all prior work (e.g., targeted testing in key areas instead of a full system re-verification).

---

#### **4. Decide on Work to Repeat or Adapt**

Small projects must adopt a pragmatic approach to repeating completed work while keeping constraints in mind:

* **Repeat Critical Work**: When the risks of not meeting higher classification requirements outweigh the cost, repeat that work to a level sufficient for higher classification compliance.

  + Examples: Full safety-critical V&V for systems supporting human-rated operations or redoing testing to comply with tougher standards.
* **Adapt or Tailor**: For activities that add value but are not safety-critical or high-risk, consider tailoring the work. For instance:

  + Executing spot checks or limited testing rather than full regressions.
  + Delivering streamlined or summarized documentation instead of recreating all lower-class-level records.
* Justify deviations or omissions with a well-documented **risk-based rationale**.

---

#### **5. Engage with the Technical Authority (TA) Early**

* If gaps cannot be addressed within the project’s constraints, request a **waiver or deviation**.

  + Clearly articulate in the waiver request:
    - Why completing the higher-class work is infeasible based on cost, time, or resource limitations.
    - The risk assessment findings supporting why the omitted work does not compromise mission safety, quality, or objectives.
  + **All unmet requirements require an approved waiver**, regardless of project size.
* Consult the appropriate **Center or Headquarters Engineering, Safety, and Mission Assurance (SMA), or CIO TA** to validate the scope of work and identify suitable areas for tailoring or risk acceptance.

---

#### **6. Update Relevant Project Plans**

Ensure project plans reflect changes necessary for supporting the transition:

* **Software Development/Management Plan (SDMP)**:
  + Adjust lifecycle activities, resource allocations, and milestones to account for higher classification requirements.
* **Risk Management Plan**:
  + Document all identified risks, their mitigations, and any residual risks from unmet requirements.
* **Software Maintenance Plan** (if applicable):
  + Update to address additional compliance concerns for ongoing software usage in the higher classification.

---

#### **7. Maximize Efficiency in Resource-Limited Environments**

Small projects must approach transitions with efficiency by focusing on high-impact areas:

1. **Leverage Expertise and Tools**:
   * Seek **center-level technical expertise**, where available, to reduce redundant efforts.
   * Use pre-developed frameworks, templates, tools, and checklists to streamline higher-class compliance efforts.
2. **Take a Phased Approach**:
   * Focus initially on the most critical areas (e.g., requirements traceability, safety-critical systems) rather than attempting to meet all higher-class requirements simultaneously.
3. **Plan for Resource Adjustments**:
   * Evaluate whether additional time, budget, or personnel are needed to execute the transition.
   * If resources are inadequate, raise this as a concern to the project’s stakeholders and discuss trade-offs.

---

### **Executing the Transition with Limited Resources**

Small projects can follow this simplified process to adapt to classification changes with manageable effort and risk:

1. **Baseline Assessment**: Review completed work and planned activities against higher classification requirements. Focus on mission-critical or safety-critical gaps.
2. **Prioritize Efforts**: Evaluate gaps based on risk, importance, and available resources.
3. **Develop a Transition Plan**:
   * Determine the balance of repeated work, alternative approaches, or waiver requests.
   * Update plans to reflect resource resources and the strategy for meeting gaps.
4. **Engage Stakeholders**:
   * Work with Software Assurance personnel and the Technical Authority to validate decisions and ensure approvals for waivers where appropriate.
5. **Monitor and Adjust**: Ensure the transition strategy is revisited as risks and constraints evolve.

---

### **Key Considerations for Waivers in Small Projects**

If limited resources make it infeasible to complete all requirements of the higher classification:

1. **Provide Justification**: Detail why specific omissions or deviations are necessary.
   * Use risk-based analysis to demonstrate minimal mission or safety risk.
2. **Highlight Mitigations**: Document how unaddressed gaps will be minimized or accepted.
3. **Obtain Technical Authority Approval**: Ensure all waivers and deviations are formally approved.

---

### **Summary of Actions for Small Projects**

| **Action** | **Responsibility** |
| --- | --- |
| Assess completed vs. higher-class requirements | Project Manager, Software Lead |
| Risk-assess gaps in unmet higher-class work | Software Assurance (SA), Safety Teams |
| Develop and implement a transition plan | Project Team with TA input |
| Justify risks or request waivers for gaps | Project Manager, Technical Authority |
| Update project plans for classification change | Software Project Management Team |

---

**Reminder**: Classification changes are critical even for small projects and must be treated accordingly. **Mission success, safety, and compliance depend on adapting to higher classification requirements**, even if adjustments or waivers are needed for small-project constraints. Always document decisions, engage the Technical Authority early, and prioritize risks strategically to achieve NPR 7150.2 compliance effectively.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-069) Transition of Software to a Higher Classification, GRC-SW-7150.10, Rev. C, Software Engineering Process Group, NASA Glenn Research Center, 2011.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-309) Robonaut 2 Risk Analysis and Waiver, NASA Johnson Space Center, 2010.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

Transitioning software to a higher or lower classification as defined in Appendix D of **NPR 7150.2** is a critical process that ensures software meets the appropriate level of rigor, oversight, and controls based on its risk, criticality, and role within the system or mission. The following **NASA lessons learned** emphasize the importance of addressing classification changes and managing their associated risks:

---

### **1. Columbia Accident Investigation Board (CAIB) Report (2003): "The Dangers of Inadequate Oversight"**

#### **Summary:**

The CAIB Report highlighted that decisions on developing and certifying flight hardware and software were based on assumptions that often failed to consider evolving risks in mission-critical systems. This lack of systematic re-evaluation and oversight of design and requirements as systems evolved contributed to the **Columbia disaster**.

#### **Relevance to Software Re-classification:**

* Re-classification of software introduces new risk profiles, which require **updated plans and processes** to meet higher safety, testing, and validation requirements.
* Failing to reassess completed work or identify gaps when transitioning to a higher classification can leave critical risks unaddressed, jeopardizing mission success.

#### **Key Takeaway:**

Requiring careful analysis of work performed under the lower classification versus the higher classification ensures risks introduced by the new classification are fully understood and mitigated.

---

### **2. Lesson Learned - Mars Climate Orbiter (1999): "Inadequate Risk Management and Reviews"**

**Lesson Number:** 0641

#### **Summary:**

The failure of the Mars Climate Orbiter was caused largely by assumptions made during development and testing under a classification that did not adequately address mission-critical software integration risks. Specifically, a **unit mismatch between metric and imperial systems** went unnoticed, ultimately leading to the spacecraft's loss.

#### **Relevance to Software Re-classification:**

* Projects transitioning to a higher classification must rigorously analyze completed work (e.g., testing, integration, risk management) to ensure it aligns with the **additional rigor** required for complex, mission-critical software.
* Skipping steps or failing to re-assess system interfaces when classification changes can lead to **catastrophic failures.**

#### **Key Takeaways:**

* For projects affected by classification changes, incomplete or insufficiently rigorous work should be reviewed for compliance with higher standards.
* Pay special attention to system-wide interfaces and integration processes, which often require more stringent validation in higher classes.

---

### **3. International Space Station (ISS) Software – Lesson Learned: “Underestimated Software Complexity and Risks”**

#### **Summary:**

The ISS software team encountered significant delays and overruns because early classification underestimated the system-level operational complexity of the software, contributing to **insufficient hazard analysis and late identification of gaps** in testing. As the mission needs evolved, earlier assumptions about testing and requirements no longer aligned with higher criticality.

#### **Relevance to Software Re-classification:**

* Re-classification often reflects the **increasing complexity or criticality** of software. Without adjusting plans (e.g., updating testing rigor, integration points, risk analysis), the project risks uncontrolled delays, resource overruns, or operational failures.
* Hazard analyses, system risks, and safety-critical processes must be reviewed and updated to reflect new classification levels.

#### **Key Takeaway:**

When transitioning to a higher classification due to complexity or criticality, conduct **system-wide analyses** to reassess testing and hazard management for newly classified risks.

---

### **4. Space Shuttle Software Development – Lessons on the "Cost of Meeting High Safety and Criticality Standards"**

**Lesson Number:** 0330

#### **Summary:**

The Space Shuttle program demonstrated that software designated as **Class A (human-rated)** required **immense rigor and expense** to meet NPR software engineering standards. This included multiple safety reviews, independent V&V teams, and risk management tailored for human-rated systems. Many of these processes were not in place at the beginning of the program, requiring substantial rework when gaps were later identified. Early assumptions about classification created delays and added costs in later stages.

#### **Relevance to Software Re-classification:**

* Re-classifying software to a higher level introduces new oversight, testing, and resource requirements. If the completed work does not align with these requirements, projects face significant risks of delays, cost overruns, and safety concerns.
* Small projects and constrained teams in particular must carefully **weigh the cost of rework** required to meet higher classifications against risks of proceeding with substandard deliverables.

#### **Key Takeaways:**

* Early planning for re-classification scenarios can reduce costly transitions.
* Projects that experience classification upgrades should focus resources on **critical coverage gaps**, such as safety reviews and independent testing.

---

### **5. Mars Polar Lander (1999) – Lesson: “Inadequate Testing at Higher Safety Levels”**

#### **Summary:**

The Mars Polar Lander failed due to undetected software errors in the descent engine control logic, which caused the spacecraft to crash during landing. The software’s safety-criticality required more rigorous testing than was initially assumed. Early development under a lower classification failed to account for the eventual **mission-critical nature** of the software.

#### **Relevance to Software Re-classification:**

* A lower classification may result in **less rigorous testing and validation** during early development. When transitioning to a higher classification, testing methodologies (e.g., for safety-critical functions) must be re-examined to ensure they are sufficient for the software’s new role.
* Small projects, in particular, must assess whether additional resources are needed for testing once software gains higher mission-critical importance.

#### **Key Takeaway:**

For software transitioning to a higher classification, **augment testing processes** where necessary to prevent critical errors, even if the budget is constrained. Ensure hazard-related functionalities receive adequate validation.

---

### **6. James Webb Space Telescope (JWST) - Lesson: "Iterative Rework Due to Expanding Program Scope"**

#### **Summary:**

The JWST software project experienced several phases of expanded mission responsibility, which necessitated transitioning software components to higher classifications. Many of the additional V&V activities and operational tests required under the new classification were not included in earlier project phases, leading to costly delays and rework.

#### **Relevance to Software Re-classification:**

* Increased scope or mission-critical usage often necessitates **increased classification**, which imposes stricter requirements (e.g., detailed documentation, system V&V, hazard testing). Without planning for the transition, resource re-allocation and rework can overwhelm the original budget and schedule.
* Projects of all sizes must carefully map classification changes to the needed **allocation of additional resources**.

#### **Key Takeaway:**

Budget, scope, and resource plans must **account for adjustments** necessary to align early software work with higher-level classification requirements. Projects should assess and secure additional resources early if classification transitions are likely.

---

### **7. Lesson Learned: Use of Waivers to Manage Resource Constraints on Small Projects**

**Lesson Number:** 0529

#### **Summary:**

This lesson highlights the importance of NASA's **waiver process** for addressing **challenging requirements** that cannot feasibly be met, particularly for small projects. While NPR 7150.2 defines strict standards for software engineering, projects with limited resources can use **well-documented waivers or deviations** to avoid unnecessary burdens while still managing risk effectively.

#### **Relevance to Software Re-classification:**

* For small projects transitioning to a higher software classification, resource constraints may make it impossible to address all process gaps while maintaining schedules and budgets.
* Waivers can be used to **focus resources strategically** by mitigating the most critical gaps and formally acknowledging risks for less critical unmet requirements.

#### **Key Takeaways:**

* Document decisions around resource trade-offs when transitioning to a higher classification.
* Use waivers judiciously to ensure resource-limited projects maintain **NASA’s focus on safety and mission assurance** without unnecessary delays or overruns.

---

### **8. NASA Constellation Program – Lesson: Importance of Technical Authority Engagement**

#### **Summary:**

Significant classification changes during the Constellation Program highlighted the necessity of involving **Technical Authorities (TAs)** at the earliest possible stage of a reclassification process. Their involvement reduced misalignment on updated requirements and helped mitigate risks introduced by necessary tailoring.

#### **Relevance to Software Re-classification:**

* TAs play a critical role in validating transition strategies, prioritizing risks, and ensuring all waivers are appropriately documented and approved.
* For small projects, TA engagement ensures a balanced approach between complying with higher classification requirements and tailoring work to align with limited resources.

#### **Key Takeaway:**

Technical Authorities help projects navigate re-classification efficiently, offering guidance on transitioning work while maintaining compliance and mission goals.

---

### **Final Thoughts**

NASA’s lessons learned consistently emphasize the need to:

1. Perform **risk-based gap analyses** when transitioning to a higher classification.
2. Revisit completed work to ensure compliance with new requirements.
3. Engage **Technical Authorities (TAs)** early to assess whether waivers, rework, or additional resources are appropriate.
4. Focus on **safety-critical processes** and **mission-critical testing**, as these areas frequently demonstrate the highest potential for catastrophic failure if improperly addressed.

Leveraging these lessons enhances a project’s ability to navigate classification changes successfully while maintaining compliance, safety, and mission assurance.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

### **Objective of the Guidance**

The goal of this requirement is to ensure the appropriate adjustment of software assurance, engineering, and contractual requirements as the software classification changes during the development lifecycle (higher or lower classifications). This ensures compliance with **NPR 7150.2**, proper alignment with project needs, and accurate supplier contracts based on the updated classification.

**Software Assurance (SA)** personnel play a key role in verifying these updates to documentation, supplier contracts, and requirements, ensuring compliance and mitigating risks introduced by classification changes.

---

### **Software Assurance Responsibilities**

---

#### **1. Verify Change in Software Classification**

1. **Understand the Trigger for Classification Updates**

   * Ensure the project identifies why the system or subsystem’s classification has changed, such as:
     + Changes in the software’s criticality or complexity.
     + Revised mission objectives.
     + Modifications related to safety, reliability, or operational needs.
   * Confirm that the new classification aligns with the definitions provided in **Appendix D of NPR 7150.2**.
2. **Assess Impact on Requirements**

   * Determine how the updated classification affects applicable requirements. For example:
     + Moving to a **higher classification (e.g., Class B or A)** may require stricter software assurance, testing, and risk mitigation.
     + Moving to a **lower classification (e.g., Class D or E)** may reduce assurance efforts where appropriate.
3. **Confirm Timely Notification**

   * Ensure the project manager promptly notifies affected stakeholders, including suppliers, contracting officers, and Software Assurance leaders, about the classification change.

---

#### **2. Verify Changes to Project Plans**

1. **Review Updated Plans**

   * Evaluate the updated project plan(s) to verify alignment with the new classification requirements, ensuring updates address:
     + Revised technical, assurance, and risk mitigation strategies.
     + Updated Requirements Mapping Matrix (RMM) reflecting applicable requirements from **Appendix C**.
     + New testing, V&V, and cybersecurity provisions, if required.
2. **Ensure Consistency Across Documentation**

   * Verify that all relevant documentation (Software Development Plan, Software Assurance Plan, Configuration Management Plan, etc.) is revised to reflect the updated classification and associated requirements.
3. **Provide Assurance Feedback**

   * Collaborate with the project manager to address gaps or errors in the updated plans and ensure compliance with NPR 7150.2.

---

#### **3. Verify Tailoring and Updates to Requirements Mapping Matrix**

1. **Review Updated Requirements Mapping Matrix (RMM)**

   * Ensure the RMM is updated to reflect the classification change and corresponding applicable requirements in **Appendix C**.
   * Assess whether tailoring modifications (if any) are justified, properly documented, and aligned with risk mitigations.
2. **Evaluate Tailoring Justifications**

   * Confirm that tailored requirements include appropriate rationale based on the new classification, risks, and project needs.
   * Work with approval authorities (Engineering, CIO, SMA) to review and approve/disapprove tailored requirements.
3. **Document Final RMM Updates**

   * Ensure the finalized RMM reflects the updated classification requirements, approved tailoring modifications, and applicable risks/mitigations.

---

#### **4. Verify Modifications to Supplier Contracts**

1. **Check Contract Modifications**

   * Confirm the updates to supplier contracts reflect the revised software requirements based on the updated classification. This may include:
     + Stricter assurance, testing, or documentation requirements.
     + Adjustments to software quality, configuration management, and cybersecurity provisions.
     + Risk mitigation measures or expanded scope for higher classifications.
2. **Verify FAR/NFS Clause Updates**

   * Ensure appropriate Federal Acquisition Regulation (FAR) and NASA Federal Acquisition Regulation Supplement (NFS) clauses are modified or added, such as:
     + **NFS 1852.227-88** – Government-Furnished Computer Software and Related Technical Data.
     + **FAR 52.227-16** – Additional Data Requirements.
3. **Collaborate with Contracting Authority**

   * Work with contracting officers and agreement managers to ensure contract modifications address all necessary updates based on the classification change.
4. **Audit Contractual Adjustments**

   * Periodically review supplier contract updates and tailored requirements to ensure they are compliant with the new classification and NPR 7150.2.

---

#### **5. Assess Risks and Mitigations**

1. **Evaluate Risks Associated with Classification Changes**

   * Identify risks introduced by changes to higher or lower classifications, such as:
     + Additional safety-critical functionality.
     + Reduced assurance for less critical software.
     + Added complexity or cybersecurity requirements.
2. **Verify Risk Mitigations**

   * Ensure all identified risks are addressed through appropriate mitigations.
3. **Review Impact on Quality and Safety**

   * Confirm classification changes do not compromise the quality, reliability, or safety of the system or subsystem.

---

#### **6. Ensure Proper Traceability and Documentation**

1. **Track Classification Changes**

   * Verify that classification changes and the resulting updates to requirements, plans, and contracts are traceable in project records.
2. **Archive Final RMM and Contract Modifications**

   * Ensure the revised RMM and updated supplier contracts are archived as part of the project’s retrievable records.
3. **Include in Software Assurance Records**

   * Document assurance findings and verification results related to classification updates and contract modifications, ensuring traceability for audits and reviews.

---

### **Expected Outcomes**

By following this guidance, Software Assurance ensures that:

1. **Software Requirements Are Revised Appropriately**

   * All requirements, plans, and contracts are modified to align with the updated classification.
   * Tailored requirements are justified and approved by the proper authorities.
2. **Compliance with NPR 7150.2**

   * The project remains compliant with applicable requirements in Appendix C, even after classification changes.
3. **Supplier Contracts Are Accurate**

   * Contracts reflect the new requirements and are updated without gaps or omissions.
4. **Risks Are Mitigated**

   * Risks associated with classification changes are addressed and managed effectively.
5. **Traceability Is Maintained**

   * All classification updates and corresponding modifications are documented and retrievable for audits, reviews, and future reference.

---

### **Summary**

**Software Assurance (SA)** personnel must verify that a system or subsystem's classification change is promptly reflected in updated project plans, tailored requirements mapping matrices, and modified supplier contracts. SA ensures requirements are aligned with the updated classification from Appendix D and that modifications adhere to NPR 7150.2 and Appendix C. By monitoring risks, contractual adjustments, and documentation, SA safeguards traceability, compliance, and project success.
