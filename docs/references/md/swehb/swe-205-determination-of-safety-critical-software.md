# SWE-205 - Determination of Safety-Critical Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695539. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software

SWE-205 - Determination of Safety-Critical Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695539)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695539&showCommentArea=true&showComments=true#addcomment)

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

3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-205 History

SWE-205 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8. |
| Difference between C and D | No change. |
| D | 3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |

# 2. Rationale

It is important to determine the safety criticality of each software component to identify the most critical software system components and to ensure that the software safety-critical requirements and processes are followed.

This requirement ensures a disciplined and systematic approach to identifying software components with safety implications. By involving the project manager and SMA organization, projects can balance operational priorities with safety requirements, mitigate hazards early, and ensure compliance with NASA’s rigorous standards. Proper identification of safety-critical software is fundamental to protecting lives, achieving mission success, and minimizing project risks.

Why Is This Requirement Important?

## 2.1 Ensures Mission and Human Safety

* Safety-critical software poses a direct impact on system behavior, personnel safety, and mission success. Identifying safety-critical components ensures that software components that **control, monitor, or mitigate hazardous functions** undergo the necessary level of scrutiny and assurance.
* Missed identification of safety-critical software may lead to dangerous system failures, catastrophic hazards, or loss of life.

## 2.2 Provides a Structured Methodology for Risk Identification

* Using the criteria in **NASA-STD-8739.8 [278](#_tabs-<p></p>)**, this requirement ensures **consistency in determining safety-criticality**, providing an industry-standard approach to identifying risks in software components. These criteria assess whether a failure in the software could cause or contribute to hazardous conditions.

## 2.3 Drives Appropriate Level of Software Assurance

* Safety-critical components demand **higher levels of assurance, testing, verification, and validation** to establish confidence in their safety, reliability, and operational readiness. Early identification allows for the allocation of resources (IV&V, safety reviews, additional testing) to manage these high-risk components effectively.

## 2.4 Supports Requirements Flow Down and Traceability

* Safety-critical assessments support the proper flow down of safety-critical requirements (e.g., redundancy, fault tolerance, fail-safe mechanisms) to software components. Clear identification ensures that these components:
  + Meet safety-critical design and operational constraints.
  + Are aligned with higher-level system safety requirements.

## 2.5 Reduces the Likelihood of Costly Changes or Delays

* Failing to identify a safety-critical component during the early stages of development can lead to costly redesigns, schedule delays, or system rework. Assessing safety-criticality early allows the project team to address risks proactively.

## 2.6 Strengthens Collaboration Between Project Management and SMA

* By involving both the **project manager** and the **SMA organization**, the process benefits from both technical and safety perspectives:
  + The project manager ensures alignment with system architecture, resources, and project goals.
  + The SMA organization ensures compliance with safety standards, hazard analysis, and system assurance.

## 2.7 Enhances Compliance With NASA Standards

* NASA projects with safety-critical software components must comply with rigorous assurance requirements defined in **NASA-STD-8739.8** and **NPR 7150.2**. This requirement ensures that safety-critical software is properly identified and can be developed, verified, and validated in accordance with these standards.

## 2.8 Provides Accountability and Documentation

* The process of determining safety-criticality requires clear reasoning and alignment with defined criteria, providing **traceable accountability** for the designation of software components. This accountability ensures all team members are aware of safety-critical determinations and makes these decisions auditable throughout the project lifecycle.

## 2.9 Criteria for Safety-Critical Determination

Per **NASA-STD-8739.8 [278](#_tabs-<p></p>)** , software components are considered safety-critical if:

1. The software directly controls or mitigates hazards.
2. The software performs functions essential to hazard detection, notification, or mitigation.
3. Failure of the software could result in loss of life, injury, loss of mission, or significant property damage.

# 3. Guidance

## 3.1 Purpose of Software Classification

Software classification is a critical step in tailoring software engineering, safety, and assurance requirements based on the complexity, criticality, and intended use of the software being developed. It provides a structured framework that ensures the appropriate level of rigor is applied to software processes, ensuring that risks are appropriately managed and that resources are efficiently allocated.

Beyond merely classifying software, each project must evaluate every software component to determine safety criticality, focusing on managing hazards that could result in severe injury, property damage, or mission failure.

Classifying software and assessing safety-criticality is essential for ensuring that all software components, regardless of complexity, align with the project’s overall safety, engineering, and assurance goals. The process described in **NASA-STD-8739.8 [278](#_tabs-<p></p>)** ensures a systematic, thorough, and consistent approach for managing software-related hazards throughout the project lifecycle. From tailoring requirements to identifying and addressing safety-critical components, this process is vital for minimizing risk, protecting lives, and ensuring mission success.

## 3.2 The Importance of Classifying Software

### 3.2.1 Pre-Tailoring of Requirements

* Classification enables the **pre-tailoring of software requirements**, meaning the project's software engineering, safety, assurance, and other requirements are pre-scoped based on the specific class assigned to the software. NASA’s classification system considers software function, risk, and criticality within the broader system.
* Without classification, projects risk applying excessive rigor where it is unnecessary (leading to wasted resources) or inadequate rigor to systems that are highly critical (introducing risk to safety and mission success).

### 3.2.2 Enables a Hazard-Centric Approach

* Classification ensures a systematic process for determining whether software is **safety-critical**, aligning with the criteria established in **NASA-STD-8739.8**.
* Software that interacts with safety-critical systems, hardware, or operations contributes to system-level risk mitigation. Early identification of safety-criticality ensures these components comply with specific safety and assurance augmentations.

## 3.3 Key Definitions and Their Context

### 3.3.1 Safety-Critical Software

* Safety-critical software is defined as software that contributes to conditions, events, or operations that could cause:
  + **Severe injury** to personnel.
  + **Major system or property damage**.
  + **Mission failure**, especially in scenarios requiring precise, uninterrupted operation.
* This designation guides the project's application of safety-specific requirements.

### 3.3.2 Software Safety

* Software safety is the discipline within software engineering and assurance that focuses on:
  + **Identifying, mitigating, and controlling hazards** related to how software functions within its system.
  + **Ensuring safe operation of the system**, whether the software directly controls hazards or mitigates their impact.
* This systematic process involves analyzing how software failures could contribute to or fail to prevent hazards, ensuring the system operates without introducing unacceptable safety risks.

## 3.4 Classifying Software for Safety Criticality

Safety-critical assessments are guided by **NASA-STD-8739.8**, which provides specific criteria to determine if software is safety-critical. The process involves evaluating:

1. **Direct Contribution to Hazard Mitigation or Control**: Does the software play an active role in controlling hazardous functions within the broader system?
2. **Possible Contribution to Hazards**: Could a failure in the software create or exacerbate an unsafe condition, leading to mission failure or physical risk?
3. **System-Level Considerations**: The process considers **independent protections** (hardware, software, or administrative barriers) during hazard analysis. Safety-critical software is not determined in isolation but as a component of the overall system hazard management plan.

### Key Tools for Classification

* Use **Appendix A of NASA-STD-8739.8** for guidance on incorporating software into hazard definitions, and reference **Table 1 and SWE-205** for additional criteria.
* Ensure alignment with [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) to identify required safety augmentations based on safety-criticality findings.

## 3.5 Additional Complexity: Artificial Intelligence (AI) and Machine Learning (ML)

For projects involving AI/ML-based software systems, the classification process must account for the unique characteristics of these technologies, such as:

* **Non-deterministic behavior** (i.e., adaptive learning and decision-making).
* **Complex failure modes** stemming from training data, biases, or latent learning conditions. Attention should be given to evolving standards for AI/ML classification and safety, as outlined in topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

## 3.6 Determining Software Safety Criticality

Once software is classified, the next step is to assess **software safety criticality**. This process begins in the **formulation phase** and continues throughout the software lifecycle as more system details are defined. This iterative approach ensures that all safety-critical software components are identified as the system architecture evolves.

### Key Points in Determining Software Safety Criticality

1. **Initial Assessment in the Formulation Phase**:

   * During the early stages of the project, high-level hazard and risk analyses help identify safety-critical software.
   * Evaluations follow the criteria in **NASA-STD-8739.8** to identify software components with potential safety implications.
2. **Reassessment as the System Evolves**:

   * As the system architecture is developed, including the identification of CSCIs, interfaces, models, and simulations, the safety-critical designation should be reassessed to account for design trade-offs or changes made during development.
   * Changes to legacy or heritage systems must undergo the same level of scrutiny, especially because these systems may have differences in design documentation, hardware/software integration, or testing history.
3. **Planning for Software Safety**:

   * Every safety-critical software component requires a tailored safety plan that includes additional requirements from **NASA-STD-8739.8**, supplementing the baseline software class requirements.
   * Planning includes identifying hazards, implementing controls, tracking risks, and validating that these controls and mitigations are effective throughout the software lifecycle.
4. **Additional Requirements for Safety-Critical Software**:

   * Safety-critical components require **stricter standards** for design, verification, and validation activities.
   * These components undergo **independent assessments**, **thorough hazard-specific testing**, and **enhanced quality assurance** to confirm their reliability and safe operation.

## 3.7 Why Use NASA-STD-8739.8?

NASA-STD-8739.8 is the **definitive resource** for software safety within NASA, providing:

1. A **systematic approach** for evaluating safety-criticality, ensuring consistency across all NASA missions.
2. Augmented safety processes and requirements for software interacting with hazardous systems.
3. Guidelines for tracing software's contributions to or control of system-level hazards.

This standard ensures that safety-critical software fulfills its role while managing risks inherent to complex systems.

**NASA-STD-8739.8B - SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD**

## 4.2 Safety-Critical Software Determination

Software is classified as safety-critical if the software is determined by and traceable to a hazard analysis. Software is classified as safety-critical if it meets at least one of the following criteria:

a. Causes or contributes to a system hazardous condition/event,

b. Controls functions identified in a system hazard,

c. Provides mitigation for a system hazardous condition/event,

d. Mitigates damage if a hazardous condition/event occurs,

e. Detects, reports, and takes corrective action if the system reaches a potentially hazardous state.

See Appendix A for guidelines associated with addressing software in hazard definitions. See Table 1, 3.7.1, SWE-205 for more details. Consideration for other independent means of protection (software, hardware, barriers, or administrative) should be a part of the system hazard definition process.

See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements). Topic [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality)

See also [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance). 

**Software safety requirements contained in NASA-STD-8739.8B**

Derived from NPR 7150.2D para 3.7.3 SWE 134: Table 1, SA Tasks 1 - 6

1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l."

2. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone.

3. Confirm that the values of the safety-critical loaded data, uplinked data, rules, and scripts that affect hazardous system behavior have been tested.

4. Analyze the software design to ensure the following:  
   a. Use of partitioning or isolation methods in the   
         design and code,  
   b. That the design logically isolates the safety-critical   
         design elements and data from those that are   
         non-safety-critical.

5. Participate in software reviews affecting safety-critical software products.

6. Ensure the SWE-134 implementation supports and is consistent with the system hazard analysis.

See the software assurance tab for Considerations when identifying software subsystem hazard causes and for Considerations when identifying software causes in general software-centric hazard analysis.

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) [a](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)        * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [PAT-006 - Design Practices for Safety](/spaces/SITE/pages/114327707/PAT-006+-+Design+Practices+for+Safety) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

# 4. Small Projects

Small projects often have:

* Fewer resources (time, budget, and personnel).
* Limited access to dedicated safety or assurance experts.
* Tightly scoped missions, which can lead to under-prioritization of processes perceived as “extra.”  
  Despite these constraints, small projects must still follow NASA’s rigorous standards for safe and reliable software development, particularly for safety-critical systems.

Following these recommendations, small projects can achieve compliance with this requirement while balancing efficiency, mission safety, and system reliability. Every software component—from simple tools to critical navigation systems—will receive attention appropriate to its scope and impact.

### **4.1 General Recommendations for Small Projects**

#### **4.1.1 Start Early with Software Classification**

* Identify software requirements and functionality early in the project’s formulation phase.
* Collaborate with system engineers to understand how software integrates with hardware, human factors, and overall system functionality.
* **Practical Tip**: Use a simple spreadsheet or checklist for documenting software classification decisions based on the **NASA-STD-8739.8** [278](#_tabs-<p></p>) **classification criteria**.[278](#_tabs-<p></p>) **classification criteria**.

#### **4.2.2 Leverage NASA-STD-8739.8 for Tailoring Requirements**

* Use **Table 1** in NASA-STD-8739.8 to identify the appropriate software classification for each component. This ensures resources are allocated to areas of highest criticality.
  + **Class D-F Software**: Typically used for research-grade or less critical software (reduced requirements rigor).
  + **Class A-B Software**: High-assurance standards apply (mission/safety critical).
* For small projects with limited scope or non-critical systems, lower-class software (Class D-F) may be common. This allows for:
  + Reduced documentation burdens.
  + Streamlined assurance activities.
* **Recommendation**: Work with the Safety and Mission Assurance (SMA) organization to confirm classification decisions early in the lifecycle.

#### **4.2.3 Identify Safety-Critical Software Components**

* Even in small projects, software may interact with hazardous operations or systems. Use the safety-criticality criteria from **NASA-STD-8739.8** to assess software components.
  + Answer these questions for each software component:
    - Could failure of this software cause injury, mission-critical failure, or property damage?
    - Does this software mitigate hazards in the overall system?
    - Does this software control hazardous system functions (e.g., propulsion, navigation, life support)?
* If a software component is determined to be **safety-critical**, NASA requires additional safety standards and assurance activities to mitigate the risks.

#### **4.2.4 Use Existing Tools and Resources**

* Small projects often lack the budget to procure or develop extensive tools for hazard and classification analysis. Instead:
  + Reuse **existing NASA tools** or open-source safety analysis and software management tools whenever possible.
  + Partner with other projects for **knowledge sharing, lessons learned, and templates**.
  + Ask the organization’s SMA team for historical examples or smaller-scale approaches used in prior projects of similar complexity.
* **Examples of tools**:
  + **Hazard Analysis Tools** (e.g., FMEA/FTA tools).
  + **Requirement Traceability Tools**: Lightweight tools like Excel for smaller scope.

#### **4.2.5 Collaborate with the SMA Team**

* Small projects may not have dedicated safety engineers or assurance teams, but collaboration is key:
  + Leverage SMA expertise early in the project (even on a part-time basis).
  + Use SMA team guidance for hazard analysis, safety-critical determination, and documentation.
* Document safety decisions and classification outcomes collaboratively with SMA personnel to ensure compliance with this requirement and **NASA-STD-8739.8**.

#### **4.2.6 Be Realistic and Proportional**

* Use the **“small but sufficient” approach** to tailor software assurance and engineering activities realistically:
  + Apply stricter levels of testing, documentation, and verification only to safety-critical components, as dictated by **NASA-STD-8739.8**.
  + Minimize overhead on lower-risk components of the software by tailoring requirements proportionally to their classification.

### **4.3 Steps for Applying Classification and Safety-Criticality Determination in Small Projects**

#### **Step 1: Understand the Scope of the Mission**

* Review the mission objectives, hardware/software integration, and the role of software within the system. Determine if any systems have higher risks due to human operations, hazardous hardware (e.g., propulsion), or mission-critical tasks.

#### **Step 2: Perform Software Classification**

* For each software component, determine the class (A–F) based on Table 1 of NASA-STD-8739.8:
  + Start with a small team review (including the project manager, software engineer, and SMA representative) to classify software based on its role in the system.
  + Document classification decisions to allow for future traceability.

#### **Step 3: Determine Safety-Critical Software Components**

* Evaluate all software components, using the safety-criticality criteria provided in **NASA-STD-8739.8**:
  + Does the software directly control hardware or hazardous systems?
  + Does the software function as a hazard mitigator (e.g., fail-safe functionality)?
  + Could software failure contribute to major loss (life, mission, or property)?
  + Components answering "yes" to any of these should be designated **safety-critical**, regardless of overall project scope.

#### **Step 4: Add Augmented Requirements for Safety-Critical Components**

* Once the software is determined to be safety-critical, apply **NASA-STD-8739.8**'s additional safety-specific requirements:
  + Enhanced software assurance testing.
  + Hazard mitigation validation processes.
  + Independent verification and validation (IV&V) if risk warrants.
* Document the rationale for augmented processes in the project plan.

#### **Step 5: Reassess Safety-Criticality Through Lifecycle**

* As the software evolves (e.g., changes are made, components are re-architected, or legacy systems are integrated), **reassess classification and safety-criticality**:
  + This ensures no previously non-critical software becomes safety-critical due to new interactions or functionality changes.

### **4.4 Special Considerations for Small Projects**

#### **4.4.1 Incremental Documentation**

* Use lightweight methods to maintain compliance:
  + Maintain decision logs for classification and safety-criticality assessments.
  + Create a **simple risk matrix** for tracking risks associated with safety-critical software.

#### **4.4.2 Manage Artificial Intelligence/ML Software Proportionally**

* If your small project includes **AI/ML systems**, classify the unique behaviors (e.g., non-determinism, training data dependence) using the guidance in Topics **7.25 and 8.25: Artificial Intelligence in Software Engineering and Software Assurance**.
  + Treat AI/ML components as **presumptively safety-critical** if their outputs influence hazardous systems.

#### **4.4.3 Close Collaboration With Experts**

* Resource constraints on small projects shouldn’t mean reduced rigor. Collaborate regularly with safety engineers, software assurance experts, and SMEs outside the project if needed.

### **4.5 Key Takeaways for Small Projects**

1. Start classification at the **formulation phase**, involving SMA to ensure alignment with NASA-STD-8739.8 requirements.
2. Focus effort on **safety-critical software components**, tailoring assurance rigor to high-risk areas and minimizing non-essential overhead.
3. Use **lightweight documentation and tools** to manage classification decisions, risk tracking, and compliance verification for smaller-scale systems.
4. Maintain an **iterative process**, revisiting classification and safety-critical status as systems evolve.
5. Leverage NASA guidance, historical data, and external expertise to optimize processes for reduced resources.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

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

Lessons learned related to identifying safety-critical software components underline the importance of early and collaborative determination, consistency in applying NASA-STD-8739.8 criteria, and robust communication between the project manager and SMA. Below are some relevant lessons learned from the **NASA Lessons Learned Information System (LLIS)** and other documented NASA experiences applicable to this requirement.

### **1. Lesson Learned: Importance of Early Identification**

**LLIS Entry**: "Early Identification of Safety-Critical Software"

* **Summary**: Failure to identify safety-critical software components early in the lifecycle leads to delayed risk mitigation, unplanned corrective actions, and increased project costs and schedule overruns. Early identification ensures proper focus on safety, testing, and assurance for safety-critical components.
* **Recommendation**:
  + Conduct a comprehensive analysis with SMA early in the lifecycle (e.g., during System Requirements Review or Preliminary Design Review) to identify safety-critical components.
  + Involve the Safety and Mission Assurance (SMA) team in all hazard analysis discussions during system design activities to ensure software contributions to hazards are understood.
  + Ensure traceability between safety-critical software and system-level hazards.
* **Example**: In a planetary mission, thermal control software was identified as safety-critical late in development, requiring significant redesign to ensure redundant fail-safe mechanisms.

### **2. Lesson Learned: Collaborative Engagement Between SMA and PM**

**LLIS Entry**: "Safety-Critical Software Determination Requires Partnership"

* **Summary**: SMA and Project Manager misalignment on defining the criteria for safety-criticality led to gaps in hazard analysis and a lack of consensus on software assurance practices. Collaboration ensures consistent safety-critical software identification and classification using agreed-upon criteria.
* **Recommendation**:
  + Schedule formal working sessions between SMA and the project team early in the lifecycle to:
    - Review NASA-STD-8739.8 criteria together.
    - Conduct joint walkthroughs of hazard analysis to identify software contributions to risk.
  + Maintain open communication between SMA and the project team throughout the project lifecycle to revisit safety-critical determinations when changes occur in project scope, software design, or system architecture.
* **Example**: A spacecraft's ground system software was initially assessed as non-safety-critical without significant SMA involvement. After SMA review, it was reclassified as safety-critical due to its role in commanding emergency corrective actions.

### **3. Lesson Learned: Consistent Application of NASA-STD-8739.8**

**LLIS Entry**: "Inconsistent Criteria Application Leads to Risk Exposure"

* **Summary**: Inconsistent interpretation of NASA-STD-8739.8 criteria across engineering teams resulted in misclassified software components and insufficient attention to safety-critical requirements. Standardized criteria interpretation and detailed reviews reduce ambiguity.
* **Recommendation**:
  + Require both the project manager and SMA team to explicitly reference specific sections of NASA-STD-8739.8 when assessing safety-critical software.
  + Train project managers, system engineers, and SMA representatives on consistent application of the criteria to avoid misclassification.
  + Incorporate checklists and standardized tools for assessing safety-critical components based on NASA-STD-8739.8 to enforce uniformity.
* **Example**: In a Mars rover project, a propulsion monitor system was overlooked as safety-critical due to inconsistent use of the criteria, creating risk exposure later in testing.

### **4. Lesson Learned: Linking Hazard Analysis to Software Safety**

**LLIS Entry**: "Inadequate Hazard Analysis Leads to Critical Oversights"

* **Summary**: Software contributions to system hazards were underestimated due to siloed hazard analysis processes that excluded software SMEs. Ensuring software integration into hazard analysis improves risk identification and mitigates safety-critical software oversights.
* **Recommendation**:
  + Always engage software engineers in hazard identification meetings.
  + Document all hazards related to system functionality and include discussions addressing software control or failure contributions (e.g., improper command sequencing, timing issues, or loss of redundancy).
  + Perform traceability analysis to link hazards to software requirements and safety-critical classification decisions.
* **Example**: For a deep-space mission, navigation software unexpectedly triggered system-level hazards due to insufficient software consideration during hazard analysis.

### **5. Lesson Learned: Dynamic Reassessment of Safety-Critical Software**

**LLIS Entry**: "Software Safety-Criticality Changes Throughout the Lifecycle"

* **Summary**: Software initially classified as non-safety-critical evolved into a safety-critical role due to system design changes during development. Periodic reevaluation ensures accurate classification throughout the lifecycle.
* **Recommendation**:
  + Establish formal reviews at critical lifecycle milestones (e.g., SRR, PDR, CDR) to confirm or update safety-critical classifications as requirements, system architecture, or interface designs change.
  + Involve SMA in evaluating risk impacts related to software changes.
  + Implement rigorous configuration control processes to ensure updated software classification information is properly documented and disseminated.
* **Example**: In a crewed vehicle program, non-critical communication software became safety-critical after new operators were assigned real-time control duties requiring emergency commands.

### **6. Lesson Learned: Insufficient Documentation of Criteria Application**

**LLIS Entry**: "Document Safety-Critical Software Decisions Thoroughly"

* **Summary**: Failure to document the rationale behind safety-critical decisions led to confusion during audits, miscommunication of risk, and difficulty ensuring compliance. Comprehensive documentation supports informed decision-making and helps during reviews and audits.
* **Recommendation**:
  + Develop and maintain detailed documentation of each software component assessment, including criteria from NASA-STD-8739.8, traceability to hazards, and safety-critical classification decisions.
  + Include SMA concurrence in all decision documents to ensure clarity and accountability.
  + Use standardized templates for documenting software classification results.
* **Example**: A flight software module’s safety classification was questioned during an Independent Review Team (IRT) audit due to incomplete rationale documentation.

### **7. Lesson Learned: Integration with Overall Risk Management**

**LLIS Entry**: "Safety-Critical Software Must Align with Risk Management Strategy"

* **Summary**: Missed integration of safety-critical software identification with broader risk management efforts resulted in gaps in mitigation plans for key risks. Proper alignment ensures comprehensive risk reduction for critical software.
* **Recommendation**:
  + Explicitly link safety-critical software assessments to the project's risk management plan.
  + Assign software safety as a key risk category to ensure proper visibility and focus throughout lifecycle phases.
  + Confirm SMA representation in all risk mitigation discussions.
* **Example**: A lunar lander project integrated safety-critical classification results into its overall risk mitigation strategy to ensure redundant safety mechanisms were implemented for identified software.

### **Summary of NASA Lessons Learned**

| **Lesson** | **Key Recommendations** | **Example** |
| --- | --- | --- |
| Importance of Early Identification | Identify safety-critical software early to manage risks effectively. | Thermal control software was identified late, causing redesign delays. |
| Collaborative Engagement Between SMA and PM | Strengthen collaboration between SMA and project team to align on safety-critical classifications. | Ground system software was reclassified after SMA involvement. |
| Consistent Application of NASA-STD-8739.8 | Use standardized criteria, checklists, and tools to ensure consistent determinations across teams. | Propulsion monitor system misclassified due to varied interpretation of safety-critical criteria. |
| Linking Hazard Analysis to Software Safety | Integrate software SMEs into hazard analysis processes to ensure risk identification for software contributions. | Navigation software caused hazards due to overlooked software in early hazard analysis. |
| Dynamic Reassessment of Safety-Critical Software | Reevaluate software safety-criticality at lifecycle milestones as system designs change. | Communication software became critical after changes to operator roles. |
| Insufficient Documentation of Criteria Application | Document all rationale for safety-critical classifications thoroughly to support audits and reviews. | Flight software module audit revealed missing justification for safety-critical assessment. |
| Integration with Overall Risk Management | Link safety-critical software identification to broader risk management efforts for comprehensive mitigation. | Lunar lander safety classification integrated into risk management for redundant mechanisms. |

These lessons learned emphasize the importance of early collaboration, consistent application of standards, dynamic reevaluation, hazard analysis integration, thorough documentation, and alignment with risk management in determining safety-critical software per this requirement. These insights improve project outcomes and reduce risk significantly.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-205 - Determination of Safety-Critical Software**

3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8.

The identification and mitigation of software’s contributions to hazards are critical for safe and successful mission execution. Following the steps outlined in this guidance ensures that hazard analyses are complete, safety-critical components are correctly identified, and all safety contributions are explicitly addressed and traceable. By maintaining alignment with **NASA-STD-8739.8** and leveraging the recommended best practices, projects can confidently manage software risks while ensuring compliance with NASA's safety assurance standards.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8**

1. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.

2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.

3. Assess that hazard analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.

4. Confirm that the traceability between software requirements and hazards with software contributions exists.

5. Develop and maintain a software safety analysis throughout the software development life cycle.

### **7.2 Software Assurance Products**

The purpose of software assurance products is to provide comprehensive coverage of software's role in system hazards and ensure hazards are mitigated throughout the development lifecycle. This involves identifying, evaluating, and communicating the contributions of software to system hazards and validating its role in hazard prevention and mitigation.

#### **Key Deliverables for Software Assurance:**

1. **Hazard Analyses**:

   * Identify and assess all potential system hazards involving software, ensuring software’s role in contributing to or mitigating these hazards is analyzed.
2. **Assessment of Hazard Analyses and Reports**:

   * Conduct independent reviews of hazard analyses to verify they account for all software-related contributions to system safety.
3. **List of Software Safety-Critical Components**:

   * Maintain a detailed list of all software components deemed safety-critical based on the system hazard analysis and software safety assessment.
4. **Software Safety Analysis Results**:

   * Include all findings, risks, and software safety concerns identified, with proper documentation and recommendations for resolution.
5. **Analysis of Updated Hazard Reports at Review Points**:

   * Assess hazard reports regularly at major review milestones to evaluate newly identified hazards or changes to software’s role in system safety.
6. **Record of Software Safety Determination**:

   * Document all decisions regarding the safety-criticality of software components based on traceability from hazards to requirements and software contributions.
7. **Traceability of Software Requirements and Hazards**:

   * Provide evidence of traceability between software requirements and the hazards they address, including how software detects, mitigates, or prevents hazardous scenarios.
8. **Confirmation of Software Safety Contributions in Hazard Reports**:

   * Confirm that hazard reports reflect all software safety contributions, ensuring software's role in addressing hazards is documented and verifiable.

### **7.3 Metrics: Tracking Software Safety Performance**

To monitor safety assurance activities and assess the performance of software safety processes, the following metrics should be collected and analyzed over time:

1. **Non-Conformances by Life Cycle Phase**:

   * Number of software-related Non-Conformances detected at each life cycle phase, tracked over time to identify trends.
2. **Safety-Related Requirement Issues**:

   * Number of safety-impacting requirements issues (open, closed) by life cycle phase.
3. **Safety-Related Non-Conformances**:

   * Number of safety-related Non-Conformances identified by life cycle phase.
4. **Hazards Containing Software Contributions**:

   * The number of hazards with software-related functions that have been tested versus the total hazards identified with software contributions, tracked over time.
5. **Safety-Critical Component Trends**:

   * Track the percentage of software components designated as safety-critical and their testing outcomes.

These metrics will help project teams evaluate the effectiveness of hazard analyses and software assurance activities, detect potential issues in a timely fashion, and improve overall project safety.

### **7.4 Guidance: Safety-Critical Software and Hazard Traceability**

#### **Definition of Safety-Critical Software**

Safety-critical software directly or indirectly contributes to or mitigates a hazard. According to **NASA-STD-8739.8**, software is **classified as safety-critical** if:

* It causes or contributes to a system hazardous condition/event.
* It controls functions identified in a system hazard.
* It provides mitigation for a system hazardous condition/event.
* It mitigates damage if a system hazard occurs.
* It detects, reports, or acts on a potentially hazardous state.

Safety-critical software is identified through hazard analysis and must be traceable to specific hazards in the system.

#### **Key Considerations for Small and Large Projects Alike:**

1. **Hazard Reports and Traceability of Software Contributions**:

   * Hazard reports must include all **known software contributions**, specifying how software contributes to or mitigates hazards during system operation.
2. **Independent Protection**:

   * Hazard analyses should consider independent means of protection (e.g., hardware redundancies, interlocks, barriers, or administrative controls) to supplement software’s contributions and mitigate risk from single points of failure.
3. **Systematic Examination of Software’s Role in Hazards**:

   * Pay special attention to hazards where software contributes to:
     + Monitoring safety-critical thresholds.
     + Issuing critical alerts or warnings.
     + Preventing unsafe actions through interlocks or redundant design.
     + Performing autonomous functions such as triggering fail-safe conditions.
4. **Interaction of Redundant Systems**:

   * Assess for common-mode failures where redundant components share software that could fail in the same way, violating redundancy independence.

---

### **7.5 Recommended Steps for Software Assurance:**

#### **1. Early Engagement in Hazard Analysis**

* Begin evaluating potential software hazards as early as possible, during system concept development.
* Collaborate with system engineers, safety analysts, and mission planners to ensure a thorough understanding of software’s role in the system.

#### **2. Leverage Initial Project Documents**

* Review system-level documents such as:
  + Preliminary Hazard Analyses (PHA).
  + Concept of Operations (ConOps).
  + Science Requirements Documents.
  + System Risk Assessments.
* Use these documents to build a foundation for identifying software contributions to hazards and their resulting safety-critical classification.

#### **3. Assess Safety-Critical Components and Updates at Each Milestone**

* At each project review point, update hazard reports and design analyses to identify new or modified software components that may have become safety-critical based on evolving system requirements.

#### **4. Confirm Traceability Between Requirements and Hazards**

* Use a traceability matrix to confirm that:
  + Software components contributing to hazards are traceable to specific software requirements.
  + Each requirement is linked to software tests that validate its proper implementation.

#### **5. Develop and Maintain a Robust Software Safety Analysis**

* Regularly update the software safety analysis to reflect changes in design, requirements, or hazard reports.
* Ensure the analysis supports system hazard reports and aligns with phased safety reviews.

### **7.6 AI/ML-Specific Considerations**

For AI/ML-based systems, special attention must be given to:

1. **Non-deterministic Behavior**: Analyze hazards arising from unpredictable or evolving outputs generated by AI/ML systems.
2. **Training Data Risks**: Address hazards introduced by biased or incomplete training datasets.
3. **Interpretability Requirements**: Ensure traceability of how AI/ML decisions affect system safety, particularly in critical decision-making contexts.

See **Topics 7.25 and 8.25** for specific information on AI/ML safety engineering and assurance.

### **7.7 Additional Considerations: Software Contributions to Hazards**

In assessing software contributions to hazards:

1. Does software control safety-critical hardware?
2. Does software trigger hazard mitigations or safety controls (e.g., fail-safe operations)?
3. Does software ensure system fault tolerance in failure scenarios (e.g., switchovers, redundant hardware management)?
4. Are interlocks implemented in software to prevent accidental activation of hazardous operations?
5. Does software provide critical monitoring or fault diagnosis that affects safety decisions?

By answering these questions, project teams can determine whether software plays a safety-critical role and ensure all necessary assurance actions support hazard controls.

**NASA-STD-8739.8B - SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD**

## 4.2 Safety-Critical Software Determination

Software is classified as safety-critical if the software is determined by and traceable to a hazard analysis. Software is classified as safety-critical if it meets at least one of the following criteria:

a. Causes or contributes to a system hazardous condition/event,

b. Controls functions identified in a system hazard,

c. Provides mitigation for a system hazardous condition/event,

d. Mitigates damage if a hazardous condition/event occurs,

e. Detects, reports, and takes corrective action if the system reaches a potentially hazardous state.

**Note: Software is classified as safety-critical if the software is determined by and traceable to hazard analysis. See Appendix A of NASA-STD-8739.8 for guidelines associated with addressing software in hazard definitions. See SWE-205. Consideration for other independent means of protection (e.g., software, hardware, barriers, or administrative) should be a part of the system hazard definition process.**

Safety-Critical: A term describing any condition, event, operation, process, equipment, or system that could cause or lead to severe injury, major damage, or mission failure if performed or built improperly, or allowed to remain uncorrected. (Source NPR 8715.3)

Safety-Critical Software: Software is classified as safety-critical if the software is determined by and traceable to a hazard analysis*.* Software is classified as safety-critical if it meets at least one of the following criteria:

1. Causes or contributes to a system hazardous condition/event,
2. Controls functions identified in a system hazard,
3. Provides mitigation for a system hazardous condition/event,
4. Mitigates damage if a hazardous condition/event occurs,
5. Detects, reports, and takes corrective action if the system reaches a potentially hazardous state.

Safety-Critical Software can cause, contribute to, or mitigate human safety hazards or damage facilities. Safety-critical software is identified based on the results of the hazard analysis and the results of the Orbital Debris Assessment Report/End-Of-Mission Plan (where applicable). Examples of safety-critical software can be found in all types of systems, including Flight, Ground Support systems, Mission Operations Support Systems, and Test Facilities. See Appendix A for guidelines associated with addressing software in hazard definitions. Consideration for other independent means of protection (software, hardware, barriers, or administrative) should be a part of the system hazard definition process.

See also Topic [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis),

**Task 1:** Confirm that the hazard reports or safety data packages contain all known software contributions or events where software; either by its action, inaction, or incorrect action, lead to a hazard.

It is necessary for software assurance and software safety personnel to begin examining possible software hazards and determining whether the software might be safety-critical as early as possible. Several steps are important in determining this:

A. Learn who the key project personnel are and begin establishing a good working relationship with them. In particular, systems analysts, systems safety personnel, requirements development personnel, end-users, and those establishing operational concepts are some of the key people with initial knowledge of the project.

B. Gather all of the initial documents listed in the requirement as well as any others that the project is developing that may contain critical information on the project being developed. Don’t wait for signature copies, but begin getting acquainted with them as early as possible. Through the working relationships established, stay informed about the types of updates that are being made as the system concepts continue to be refined. Keep a list of the documents collected and their version dates as the system matures. Potential documents that may contain critical information include:

* + Preliminary System-Level Preliminary Hazard Analyses (PHA)
  + Concept of Operations (ConOps)
  + Generic Hazard Lists (e.g. for project type, for software, or just generic hazards)
  + Critical Item List(s) (CIL)
  + Preliminary System Reliability Assessment or Analyses
  + Project/System Risk Assessments
  + Request for Proposals (RFP)
  + Computing System Safety Analyses
  + Software Security Assessment (NPR 7150.2, [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks), [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks))
  + Science Requirements Document

C. Become familiar with the documents in Step 2 and pay particular attention to the risks and potential hazards that might be mentioned in these documents. While reviewing these risks and potential hazards, think about the ways that the software might be involved in these risks. Possible examples of software contributions to potential hazards are found in the section below titled: **Software Contributions to Hazards, Software in system hazard analysis**

D. As the initial hazard analyses are being done, software assurance and software safety people confirm that these analyses are as complete as possible for the stage of the project.

**Task 2:** Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD- 8739.8 Appendix A.

Review each hazard report to see that the software components associated with the system hazards are identified, using the criteria defined in NASA-STD- 8739.8 Appendix A. The Hazard Analysis done at this point should identify the initial set of planned safety-critical components. A list of all the safety-critical components should be included in the hazard reports. Keep this safety-critical components list for Tasks 4 and 5.

**Task 3:** Analyze the updated hazard reports and design at review points to determine if any newly identified software components are safety-critical.

At each milestone or review point, review any updated hazard analyses or new hazard reports. Review the current design to determine whether any new software has been identified as safety-critical. By this point in the project, some of the software may have been identified as control or mitigation software for one of the previously identified hazards and it may not have been thought about in earlier hazard reports. Verify that this newly identified software is now included in a hazard report, is included on the safety-critical components list, and has a corresponding requirement. As the project continues and requirements mature, any newly identified safety-critical software should be added to the hazard reports, so the reports contain a complete record of all safety-critical components.

**Task 4:** Confirm that the traceability between the software requirements and the hazards with software contributions exists.

As the project progresses, review the hazard reports with software contributions and confirm that the associated safety-critical component is listed in the hazard reports and can be traced back to a requirement in the requirements document. Confirm these requirements trace to one or more tests, and that they include testing of the software-critical capabilities required.

**Task 5:** Develop and maintain a software safety analysis throughout the software development life cycle.

Throughout the software development, starting during the requirements phase, develop a software safety analysis. Topic [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) guides on doing a software safety analysis.

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

### 7.7.1 Software Contributions to Hazards, Software in system hazard analysis:

Hazard Analysis must consider the software’s ability, by design, to cause or control a given hazard. It is a best practice to include the software within the system hazard analysis. The general hazard analysis must consider software common-mode failures that can occur in instances of redundant flight computers running the same software. A common mode failure is a specific type of common cause failure where several subsystems fail in the same way for the same reason. The failures may occur at different times and the common cause could be a design defect or a repeated event.

Software Safety Analysis supplements the system hazard analysis by assessing the software performing critical functions serving as a hazard cause or control. The review assures the following:

1) Compliance with the levied functional software requirements, including [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements),

2) That the software shouldn’t violate the independence of hazard inhibits, and

3) That the software shouldn’t violate the independence of hardware redundancy.

The Software Safety Analysis should follow the phased hazard analysis process. A typical Software Safety Analysis process begins by identifying the must work and must not work functions in Phase 1 hazard reports. The system hazard analysis and software safety analysis process should assess each function, between Phase 1 and 2 hazard analysis, for compliance with the levied functional software requirements, including SWE-134. For example, Solar Array deployment (must work function) software should place deployment effectors in the powered off state when it boots up and requires initializing and executing (arm and fire) commands in the correct order within 4 CPU cycles before removing a deployment inhibit. The analysis also assesses the channelization of the communication paths between the inputs/sensors and the effectors to assure there is no violation of fault tolerance by routing a redundant communication path through a single component. The system hazard analysis and software safety analysis also assure the redundancy management performed by the software supports fault tolerance requirements. For example, software can’t trigger a critical sequence in a single fault-tolerant manner using single sensor input. Considering how software can trigger a critical sequence is required for the design of triggering events such as payload separation, tripping FDIR responses that turn off critical subsystems, failover to redundant components, and providing closed-loop control of critical functions such as propellant tank pressurization.

The design analysis portion of software safety analysis should be completed by Phase 2 safety reviews. At this point, the software safety analysis supports a requirements gap analysis to identify any gaps ([SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)) and ensure the risk and control strategy documented in hazard reports are correct as stated. Between Phase 2 and 3 safety reviews, the system hazard analysis and software safety analysis supports the analysis of test plans to assure adequate off-nominal scenarios ([SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) a). Finally, in Phase 3, the system hazards analysis must verify the final implementation and verification upholds the analysis by ensuring test results permit closure of hazard verifications ([SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)) and that the final hazardous commands support the single command and multi-step command needs and finalized pre-requisite checks are in place. See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

The following sections include useful considerations and examples of software causes and controls:

### 7.7.2 Considerations when identifying software subsystem hazard causes: (This information is also included in Appendix A of NASA-STD-8739.8) [278](#_tabs-<p></p>)

1. 1. Does software control any of the safety-critical hardware?
   2. Does software perform critical reconfiguration of the system during the mission?
   3. Does the software perform redundancy management for safety-critical hardware?
   4. Does the software determine when to perform a critical action?
   5. Does the software trigger logic to meet failure tolerance requirements?
   6. Does the software monitor hazard inhibits, safety-critical hardware/software, or issue a caution and warning alarm used to perform an operational control?
   7. Does the software process or display data used to make safety-critical decisions?
   8. Does the flight or ground software manipulate hazardous system effectors during prelaunch checkouts or terminal count?
   9. Does the software perform analysis that impacts automatic or manual hazardous operations?
   10. Does the software serve as an interlock preventing unsafe actions?
   11. Does the software contain stored command sequences that remove multiple inhibits from a hazard?
   12. Does the software initiate any stored command sequences, associated with a safety-critical activity, and if so, are they protected?
   13. Does software violate any hazard inhibits or hardware redundancy independence (channelized communication/power paths, stored command sequences/scripts, FDIR false positive, etc.)?
   14. Can the software controls introduce new hazard causes?
   15. Are the software safety-critical controls truly independent?
   16. Can common cause faults affect the software controls?
   17. Can any of the software controls used in operational scenarios cause a system hazard?
   18. Does the software control switch over to a backup system if a failure occurs in a primary system?
   19. Is the software process sensor data used to make safety-critical decisions fault-tolerant?
   20. Does the software provide an approach for recovery if the system monitoring functions fail?
   21. Does the software allow the operators to disable safety-critical controls unintentionally?
   22. Does the software provide safety-critical cautions and warnings?
   23. Is the software capable of diagnosing and fixing safety-critical faults that might occur in operations?
   24. Does the software provide the health and status of safety-critical functions?
   25. Does the software process safety-critical commands (including autonomous commanding)?
   26. Can the software providing full or partial verification or validation of safety-critical systems generate a hazard if the software has a defect, fault, or error?
   27. Can a defect, fault, or error in the software used to process data or analyze trends that lead to safety decisions cause a system hazard?
   28. Do software capabilities exist to handle the potential use cases and planned operations throughout all phases of use, and through transitions between those phases/states?

### 7.7.3 Considerations when identifying software causes in a general software-centric hazard analysis:

See also Topic [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis),

| **Software Cause Areas to Consider** | **Potential Software Causes** |
| --- | --- |
| Data errors | 1.     Asynchronous communications  2.     Single or double event upset/bit flip or hardware induced error  3.     Communication to/from an unexpected system on the network  4.     An out-of-range input value, a value above or below the range  5.     Start-up or hardware initiation data errors  6.     Data from an antenna gets corrupted  7.     Failure of software interface to memory  8.     Failure of flight software to suppress outputs from a failed component  9.     Failure of software to monitor bus controller rates to ensure communication with all remote terminals on the bus schedule's avionics buses  10.  Ground or onboard database error  11.  Interface error  12.  Latent data  13.  Communication bus overload  14.  Missing or failed integrity checks on inputs, failure to check the validity of input/output data  15.  Excessive network traffic/babbling node - keeps the network so busy it inhibits communication from other nodes  16.  Sensors or actuators stuck at some value  17.  Wrong software state for the input |
| Commanding errors | 1.     Command buffer error or overflow  2.     Corrupted software load  3.     Error in real-time command build or sequence build  4.     Failure to command during hazardous operations  5.     Failure to perform prerequisite checks before the execution of safety-critical software commands  6.     Ground or onboard database error for the command structure  7.     Error in command data introduced by command server error  8.     Incorrect operator input commands  9.     Wrong command or a miscalculated command sent  10.  Sequencing error, failure to issue commands in the correct sequence  11.  Command sent in wrong software state or software in an incorrect or unanticipated state  12.  An incorrect timestamp on the command  13.  Missing software error handling on incorrect commands  14.  Status messages on command execution not provided  15.  Memory corruption, critical data variables overwritten in memory  16.  Inconsistent syntax  17.  Inconsistent command options  18.  Similarly named commands  19.  Inconsistent error handling rules  20.  Incorrect automated command sequence built into script containing single commands that can remove multiple inhibits to a hazard |
| Flight computer errors | 1.     Board support package software error  2.     Boot load software error  3.     Boot Programmable Read-Only Memory (PROM) corruption preventing reset  4.     Buffer overrun  5.     CPU overload  6.     Cycle jitter  7.     Cycle over-run  8.     Deadlock  9.     Livelock  10.  Reset during program upload (PROM corruption)  11.  Reset with no restart  12.  Single or double event upset/bit flip or hardware induced error  13.  Time to reset greater than time to failure  14.  Unintended persistent data/configuration on reset  15.  Watchdog active during reboot causing infinite boot loop  16.  Watchdog failure  17.  Failure to detect and transition to redundant or backup computer  18.  Incorrect or stale data in redundant or backup computer |
| Operating systems errors | 1.     Application software incompatibility with upgrades/patches to an operating system  2.     Defects in Real-Time Operating System (RTOS) Board Support software  3.     Missing or incorrect software error handling  4.     Partitioning errors  5.     Shared resource errors  6.     Single or double event upset/bit flip  7.     Unexpected operating system software response to user input  8.     Excessive functionality  9.     Missing function  10.  Wrong function  11.  Inadequate protection against operating system bugs  12.  Unexpected and aberrant software behavior |
| Programmable logic device errors | 1.     High cyclomatic complexity levels (above 15)  2.     Errors in programming and simulation tools used for Programmable Logic Controller (PLC) development  3.     Errors in the programmable logic device interfaces  4.     Errors in the logic design  5.     Missing software error handling in the logic design  6.     PLC logic/sequence error  7.     Single or double event upset/bit flip or hardware induced error  8.     Timing errors  9.     Unexpected operating system software response to user input  10.  Excessive functionality  11.  Missing function  12.  Wrong function  13.  Unexpected and aberrant software behavior |
| Flight system time management errors | 1.     Incorrect data latency/sampling rates  2.     Failure to terminate/complete process in a given time  3.     Incorrect time sync  4.     Latent data (Data delayed or not provided in required time)  5.     Mission elapsed time timing issues and distribution  6.     Incorrect function execution, performing a function at the wrong time, out of sequence, or when the program is in the wrong state  7.     Race conditions  8.     The software cannot respond to an off-nominal condition within the time needed to prevent a hazardous event  9.     Time function runs fast/slow  10.  Time skips (e.g., *Global Positioning System* time correction)  11.  Loss or incorrect time sync across flight system components  12.  Loss or incorrect time Synchronization between ground and spacecraft Interfaces  13.  Unclear software timing requirements  14.  Asynchronous systems or components  15.  Deadlock conditions  16.  Livelocks conditions |
| Coding, logic, and algorithm failures, algorithm specification errors | 1.     Auto-coding errors as a cause  2.     Bad configuration data/no checks on external input files and data  3.     Division by zero  4.     Wrong sign  5.     Syntax errors  6.     Error coding software algorithm  7.     Error in positioning algorithm  8.     Case/type/conversion error/unit mismatch  9.     Buffer overflows  10.  High cyclomatic complexity levels (above 15)  11.  Dead code or unused code  12.  Endless do loops  13.  Erroneous outputs  14.  Failure of flight computer software to transition to or operate in a correct mode or state  15.  Failure to check safety-critical outputs for reasonableness and hazardous values and correct timing  16.  Failure to generate a process error upon detection of arithmetic error (such as divide-by-zero)  17.  Failure to create a software error log report when an unexpected event occurs  18.  Inadvertent memory modification  19.  Incorrect "if-then" and incorrect "else"  20.  Missing default case in a switch statement  21.  Incorrect implementation of a software change, software defect, or software non-conformance  22.  Incorrect number of functions or mathematical iteration  23.  Incorrect software operation if no commands are received or if a loss of commanding capability exists (inability to issue commands)  24.  Insufficient or poor coding reviews, inadequate software peer reviews  25.  Insufficient use of coding standards  26.  Interface errors  27.  Missing or inadequate static analysis checks on code  28.  Missing or incorrect parameter range and boundary checking  29.  Non-functional loops  30.  Overflow or underflow in the calculation  31.  Precision mismatch  32.  Resource contention (e.g., thrashing: two or more processes accessing a shared resource)  33.  Rounding or truncation fault  34.  Sequencing error (e.g., failure to issue commands in the correct sequence)  35.  Software is initialized to an unknown state; failure to properly initialize all system and local variables are upon startup, including clocks  36.  Too many or too few parameters for the called function  37.  Undefined or non-initialized data  38.  Untested COTS, MOTS, or reused code  39.  Incomplete end-to-end testing  40.  Incomplete or missing software stress test  41.  Errors in the data dictionary or data dictionary processes  42.  Confusing feature names  43.  More than one name for the same feature  44.  Repeated code modules  45.  Failure to initialize a loop-control  46.  Failure to initialize (or reinitialize) pointers  47.  Failure to initialize (or reinitialize) registers  48.  Failure to clear a flag  49.  Scalability errors  50.  Unexpected new behavior or defects introduced in newer or updated COTS modules  51.  Not addressing pointer closure |
| Fault tolerance and fault management errors | 1.     Missing software error handling  2.     Missing or incorrect fault detection logic  3.     Missing or incorrect fault recovery logic  4.     Problems with the execution of emergency safing operations  5.     Failure to halt all hazard functions after an interlock failure  6.     The software cannot respond to an off-nominal condition within the time needed to prevent a hazardous event  7.     Common mode software faults  8.     A hazard causal factor occurrence isn't detected  9.     False positives in fault detection algorithms  10.  Failure to perform prerequisite checks before the execution of safety-critical software commands  11.  Failure to terminate/complete process in a given time  12.  Memory corruption, critical data variables overwritten in memory  13.  Single or double event upset/bit flip or hardware-induced error  14.  Incorrect interfaces, errors in interfaces  15.  Missing self-test capabilities  16.  Failing to consider stress on the hardware  17.  Incomplete end-to-end testing  18.  Incomplete or missing software stress test  19.  Errors in the data dictionary or data dictionary processes  20.  Failure to provide or ensure secure access for input data, commanding, and software modifications |
| Software process errors | 1.      Failure to implement software development processes or implementing inadequate processes  2.      Inadequate software assurance support and reviews  3.      Missing or inadequate software assurance audits  4.      Failure to follow the documented software development processes  5.      Missing, tailored, or incomplete implementation of the safety-critical software requirements in NPR 7150.2  6.      Missing, tailored, or incomplete implementation of the safety-critical software requirements in Space Station Program 50038, Computer-Based Control System Safety Requirements  7.      Incorrect or incomplete testing  8.      Inadequate testing of reused or heritage software  9.      Failure to open a software problem report when an unexpected event occurs  10.   Failure to include hardware personnel in reviews of software changes, software implementation, peer reviews, and software testing  11.   Failure to perform a safety review on all software changes and software defects  12.   Defects in COTS, MOTS, or OSS Software,  13.   Failure to perform assessments of available bug fixes and updates available in COTS software  14.   Insufficient use of coding standards  15.   Missing or inadequate static analysis checks on code  16.   Incorrect version loaded  17.   Incorrect configuration values or data  18.   No checks on external input files and data  19.   Errors in configuration data changes being uploaded to spacecraft  20.   Software/avionics simulator/emulator errors and defects  21.   Unverified software  22.   High cyclomatic complexity levels (over 15)  23.   Incomplete or inadequate software requirements analysis  24.   Compound software requirements  25.   Incomplete or inadequate software hazard analysis  26.   Incomplete or inadequate software safety analysis  27.   Incomplete or inadequate software test data analysis  28.   Unrecorded software defects found during informal and formal software testing  29.   Auto-coding tool faults and defects  30.   Errors in design models  31.   Software errors in hardware simulators due to a lack of understanding of hardware requirements  32.   Incomplete or inadequate software test data analysis  33.   Inadequate built-in-test coverage  34.   Inadequate regression testing and unit test coverage of flight software application-level source code  35.   Failure to test  all nominal and planned contingency scenarios (breakout and re-rendezvous, launch abort) and complete mission duration (launch to docking to splashdown) in the hardware in the loop environment  36.   Incomplete testing of unexpected conditions, boundary conditions, and software/interface inputs  37.   Use of persistence of test data, files, or config files in an operational scenario  38.   Failure to provide multiple paths or triggers from safe states to hazardous states  39.   Interface control documents and interface requirements documents errors  40.   System requirements errors  41.   Misunderstanding of hardware configuration and operation  42.   Hardware requirements and interface errors, Incorrect description of the software/hardware functions and how they are to perform  43.   Missing or incorrect software requirements or specifications  44.   Missing software error handling  45.   Requirements/design errors not fully defined, detected, and corrected)  46.   Failure to identify the safety-critical software items  47.   Failure to perform a function, performing the wrong function, performing the function incompletely  48.   An inadvertent/unauthorized event, an unexpected, unwanted event, an out-of-sequence event, the failure of a planned event to occur  49.   The magnitude or direction of an event is wrong  50.   Out-of-sequence event protection  51.   Multiple events/actions trigger simultaneously (when not expected)  52.   Error or exception handling missing or incomplete  53.   Inadvertent or incorrect mode transition for required vehicle functional operation; undefined or incorrect mode transition criteria; unauthorized mode transition  54.  Failure of flight software to correctly initiate proper transition mode  55.  Software state transition error  56.  Software termination is an unknown state  57.  Errors in the software data dictionary values |
| Human-machine interface errors | 1.     Incorrect data (unit conversion, incorrect variable type)  2.     Stale data  3.     Poor design of human-machine interface  4.     Too much, too little, incorrect data displayed  5.     Ambiguous or incorrect messages  6.     User display locks up/fails  7.     Missing software error handling  8.     Unsolicited command (command issued inadvertently, cybersecurity issue, or without cause)  9.     Wrong command or a miscalculated command sent  10.  Failure to display information or messages to a user  11.  Display refresh rate leads to an incorrect operator response  12.  Lack of ordering scheme for hazardous event queues (such as alerts) in the human-computer interface (i.e., priority versus time of arrival, for example, when an abort must go to the top of the queue)  13.  Incorrect labeling of operator controls in the human interface software  14.  Failure to check for constraints in algorithms/specifications and valid boundaries  15.  Failure of human interface software to check operator inputs  16.  Failure to pass along information or messages  17.  No onscreen instructions  18.  Undocumented features  19.  States that appear impossible to exit  20.  No cursor  21.  Failure to acknowledge an input  22.  Failure to advise when a change takes effect  23.  Wrong, misleading, or confusing information  24.  Poor aesthetics in the screen layout  25.  Menu layout errors  26.  Dialog box layout errors  27.  Obscured instructions  28.  Misuse of color  29.  Failure to allow tabbing navigation to edit fields (mouse-only input) |
| Security and virus errors | 1.     Denial or interruption of service  2.     Spoofed or jammed inputs  3.     Missing capabilities to detect insider threat activities  4.     Inadvertent or intentional memory modification  5.     Inadvertent or unplanned mode transition  6.     Missing software error handling or detect handling  7.     Unsolicited command  8.     **Stack-based buffer overflows**  9.     **Heap-based attacks**  10.  Cybersecurity vulnerability or computer virus  11.  Inadvertent access to ground system software  12.  Destruct commands incorrectly allowed in a hands-off zone  13.  Communication to/from an unexpected system on the network |
| Unknown Unknowns errors | 1.     Undetected software defects  2.     Unknown limitations for COTS (operational, environmental, stress)  3.     COTS extra capabilities  4.     Incomplete or inadequate software safety analysis for COTS components  5.     Compiler behavior errors or undefined compiler behavior  6.     Software defects and investigations that are unresolved before the flight |

Some safety-critical aspects are addressed in hardware, for example, valves failing to close when a fault occurs.

Safety products (including hazard reports, responses to launch site requirements, preliminary hazard analyses, etc.) begin with the PHA, evolving and expanding throughout the project life cycle.  See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing), [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

## 7.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) [a](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)        * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [PAT-006 - Design Practices for Safety](/spaces/SITE/pages/114327707/PAT-006+-+Design+Practices+for+Safety) |

# 8. Objective Evidence

**SWE-205 - Determination of Safety-Critical Software**

3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8.

This requirement mandates the systematic identification and classification of safety-critical software components based on NASA's standards for software safety. The objective evidence provides verification that this activity was done collaboratively between the **project manager** and the **Safety and Mission Assurance (SMA) organization**, as per the safety-critical criteria outlined in **NASA-STD-8739.8**.

## 8.1. Safety-Critical Software Determination Worksheet

The **Safety-Critical Software Determination Worksheet** provides formal documentation to verify that each software component has been evaluated per NASA-STD-8739.8.

##### **Must Include**:

* **Criteria Used for Evaluation**:
  + Evidence that the software components were assessed against the formal criteria in NASA-STD-8739.8:
    - Could the software impact health and safety (e.g., injury or loss of life to personnel)?
    - Could the software compromise mission success (e.g., loss of system control or mission-critical functionality)?
    - Could the software contribute to hazards related to hardware, operations, or cybersecurity?
    - Does the software handle or interface with safety-critical systems/components?
* **List of Software Components Evaluated**:
  + A complete inventory of software components (modules, subsystems, interfaces, etc.) evaluated for safety-critical designation.
* **Classification Results**:
  + Final classification of each software module:
    - "Safety-Critical" or "Non-Safety-Critical."
* **Signatures/Approval**:
  + Documented concurrence of results by both the **project manager** and the **SMA representative**.

##### **Examples of Evidence**:

* A determination worksheet showing:
  + Component: Flight Control Module.
  + Assessment: Handles real-time commands for mission-critical spacecraft operations → **Safety-Critical**.
  + Signed by the Project Manager and SMA Lead.
* Completed NASA-STD-8739.8 checklist for each software component, with supporting rationale.

## 8.2 Hazard Analysis Report

The **Hazard Analysis Report (HAR)** provides comprehensive evidence that safety-critical software components were identified through hazard evaluations performed collaboratively by the project manager and SMA.

##### **Must Include**:

* **System-level Hazard Identification**:
  + A list of system-level hazards identified early in the project's lifecycle.
* **Software Contribution to Hazards**:
  + Documentation of specific software contributions to hazards (e.g., flight control software contributing to a collision hazard).
* **Linkage of Hazards to Software Components**:
  + Evidence that specific software elements were assessed as contributing factors to system safety-critical hazards.
* **Safety-Critical Component Identification**:
  + Determination of software components classified as "safety-critical" due to their linkage to hazardous conditions.

##### **Examples of Evidence**:

* An excerpt from the Hazard Analysis Report:
  + Hazard: "Loss of Thrust Control" → Cause: Errors in safety-critical thrust control software.
  + Identified Safety-Critical Software Component: **Thrust Control Algorithm Module**.
* Signed hazard assessment showing collaboration between SMA and project personnel.

## 8.3 Software Safety Criticality Checklist

A **Software Safety Criticality Checklist** is often developed specifically to align with the criteria defined in NASA-STD-8739.8.

##### **Must Include**:

* A step-by-step checklist applied to each software component to assess whether it meets the "safety-critical" designation.
* Clear documentation referencing NASA-STD-8739.8 criteria for determining safety-criticality.
* Evidence that the checklist was completed as part of a collaborative review between the project manager and SMA.

##### **Examples of Evidence**:

* **Checklist Results**:
  + Component: Autonomy Software Module.
  + Does this software control or directly contribute to hazardous operations? → Yes → **Safety-Critical**.
  + Signed by the SMA lead and Project Manager.
* Summary of checklist entries compiled into a document indicating all evaluated components and classifications.

## 8.4 Risk Management Plan

The **Risk Management Plan** contains information pertaining to how risks are identified, assessed, and managed throughout the lifecycle. It includes data supporting safety-critical software determinations.

##### **Must Include**:

* **Identification of Safety-Critical Software Risks**:
  + Documentation of specific risks associated with safety-critical software components identified during early project phases.
* **Risk Mitigation Strategy** for Safety-Critical Components:
  + Planned actions for risk reduction, including enhanced testing, redundancy, or stricter configuration management for safety-critical software.
* Collaboration notes confirming SMA's involvement in evaluating risks.

##### **Examples of Evidence**:

* Excerpt from the Risk Management Plan:
  + Risk: "Software fails to send abort command to propulsion system in emergency scenario."
  + Classification: **Safety-Critical**.
  + Identified Component: Emergency Propulsion Handler Software.
  + SMA Representative: "Verified proper classification per hazard analysis."

## 8.5 Software Safety Plan

The **Software Safety Plan** details how safety-critical software components are identified, managed, and tracked throughout the life cycle.

##### **Must Include**:

* **Safety-Critical Classification Results**:
  + Explicit identification of components evaluated and determined to be safety-critical.
* **Alignment with NASA-STD-8739.8**:
  + Documentation showing alignment with criteria outlined in the standard.
* **Testing and Assurance for Safety-Critical Components**:
  + Specific plans for testing, verification, validation, and assurance tailored to safety-critical software.
* **Roles and Responsibilities**:
  + Evidence that SMA and project teams collaborated to classify components and implement safety measures.

##### **Examples of Evidence**:

* **Software Safety Plan Results**:
  + Identified Safety-Critical Software: "Thermal Management System Software."
  + Assessed by SMA team using NASA-STD-8739.8 guidelines.
  + Plan: Perform enhanced validation testing at TRR milestone.

## 8.6 SMA Review and Approval Documents

Objective evidence that Safety and Mission Assurance (SMA) signed off on the safety-criticality classifications is crucial for demonstrating compliance.

##### **Must Include**:

* **Concurrence Memorandum**:
  + SMA organization's written approval of the safety-critical software determinations made by the project manager.
* **Review Meeting Minutes**:
  + Official minutes of a meeting where SMA and the project manager formally reviewed safety-critical classifications and signed off on the results.

##### **Examples of Evidence**:

* SMA review document stating:
  + "Following application of NASA-STD-8739.8 criteria, the following software components have been determined to be safety-critical: ..."
  + Signed by both SMA representative and project manager.

## 8.7 Technical Authority (TA) Approval

Technical authorities (e.g., Engineering Technical Authority, Software Technical Authority) may also document concurrence with safety-critical software determinations.

##### **Must Include**:

* Evidence Technical Authorities were consulted and approved safety-critical classifications following SMA and project manager collaboration.

##### **Examples of Evidence**:

* Concurrence documents or approval memos signed by appropriate Technical Authorities.

## 8.8 Summary Table of Objective Evidence

| **Category** | **Examples of Objective Evidence** |
| --- | --- |
| **Safety-Critical Determination Worksheet** | Completed worksheet indicating classification results, rationale, NASA-STD-8739.8 criteria, and signatures from SMA and project manager. |
| **Hazard Analysis Report** | Hazard-to-software trace results identifying safety-critical software components linked to system hazards. |
| **Safety Criticality Checklist** | Checklist results applying NASA-STD-8739.8 criteria to each software component, signed by SMA and project manager. |
| **Risk Management Plan** | Risks documented for safety-critical software with associated mitigation strategies confirming SMA involvement. |
| **Software Safety Plan** | Plan specifying identification, testing, and validation actions to ensure safety-critical software compliance. |
| **SMA Review and Approval Documents** | Signed SMA concurrence statements, meeting minutes documenting agreement on safety-critical classifications. |
| **Technical Authority Approval** | Signed concurrence memos ensuring TA support for classifications determined collaboratively between SMA and project manager. |

  

This robust set of objective evidence verifies collaboration between the **project manager** and **SMA organization** while ensuring compliance with NASA-STD-8739.8 criteria for identifying and properly classifying safety-critical software components

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
