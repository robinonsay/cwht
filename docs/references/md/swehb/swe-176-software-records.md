# SWE-176 - Software Records

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695517. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records

SWE-176 - Software Records

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695517)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695517&showCommentArea=true&showComments=true#addcomment)

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

3.5.2 The project manager shall maintain records of each software classification determination, each software Requirements Mapping Matrix, and the results of each software independent classification assessments for the life of the project. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-176 History

SWE-176 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.5.2 The project manager shall maintain records of each software classification determination, each software Requirements Mapping Matrix, and the results of each software independent classification assessment for the life of the project. |
| Difference between C and D | No change |
| D | 3.5.2 The project manager shall maintain records of each software classification determination, each software Requirements Mapping Matrix, and the results of each software independent classification assessments for the life of the project. |

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

The requirement for the project manager to maintain records of **software classification determinations**, **requirements mapping matrices**, and **independent classification assessments** by **Safety and Mission Assurance (S&MA)** ensures transparency, traceability, and accountability throughout the software development lifecycle. These records are critical for aligning software engineering practices with NASA policies, enabling teams to adhere to the appropriate requirements, effectively manage risks, and support oversight activities.

The rationale for this requirement lies in its ability to support informed decision-making, consistent compliance, and effective collaboration over the lifecycle of a project. The classification records, requirements mapping matrices, and S&MA assessments collectively define the compliance scope for the software and provide the traceability necessary to address project requirements confidently. These records are not just regulatory artifacts, but valuable tools for ensuring project success, improving oversight, and fostering adaptability in a dynamic development environment.

## 2.1 Key Purposes of This Requirement

### 2.1.1 Linking Classification to Applicable Requirements

Software classification determines which requirements from NPR 7150.2 [083](#_tabs-<p></p>) apply to a given system or subsystem.

* Maintaining a record of the software classification and the associated rationale ensures that project teams can clearly identify the requirements that need to be satisfied.
* These classifications, coupled with safety-critical determinations, dictate the level of engineering rigor, assurance activities, and tailored processes required.
* By documenting these decisions, the project ensures that individuals across engineering, assurance, and management roles understand the compliance obligations tied to each classification.

**Why This Matters**:

Misclassification can result in over-engineering low-risk systems (wasting resources) or under-engineering critical systems (jeopardizing safety or mission success). Complete records provide a solid foundation for applying the appropriate level of rigor and tailoring to meet project and agency standards.

### **2.1.2 Approved Tailoring of Requirements**

The requirements mapping matrix ensures every applicable NPR 7150.2 requirement is accounted for and specifies the planned method for compliance.

* Projects may tailor or waive certain requirements to reflect resource constraints, project size, or the specific classification of software components.
* Maintaining detailed records of approved tailoring decisions helps clarify how the project addresses its responsibilities without undermining safety, quality, or mission goals.

**Why This Matters:**

Approved tailoring allows for flexibility while maintaining accountability. Centralized documentation of tailoring decisions helps ensure all team members understand the tailored implementation of requirements, preventing miscommunication or gaps in compliance.

### **2.1.3 Eligibility for Reclassification Based on Scope or Change in Requirements**

Software classifications and safety-criticality designations may need to be revisited as a project evolves.

* Documenting the logic and rationale behind initial classification ensures project teams have a clear reference point for periodic reviews.
* Project requirements, project scope, or operational use changes may necessitate classification updates, such as transitioning software to a higher class (see SWE-021).
* Maintaining well-documented records helps ensure timely and accurate reclassification decisions, reducing the risk of applying insufficient requirements to systems whose criticality has increased.

**Why This Matters**:

Without clear documentation, teams may struggle to evaluate whether changes in mission requirements justify reclassification. This could lead to insufficient safeguards for critical systems or unnecessary overhead for lower-risk systems.

### 2.1.4 Support for Audits and Oversight Activities

Maintaining these records facilitates independent reviews, including appraisals by the Office of the Chief Engineer (OCE) (e.g., SWE-129 – OCE NPR Appraisals) to evaluate compliance with Agency software standards.

* Classification, requirements mapping, and assessment records ensure that the rationale and decisions made at each stage are transparent and auditable.
* The records also allow for assessment of whether the assigned classification and tailoring were applied consistently throughout the project lifecycle.

**Why This Matters:**

Oversight activities help NASA maintain internal control and assess compliance across its diverse projects. Accurate and complete records reduce project risks and demonstrate adherence to established policies.

## 2.2 Benefits of Records Maintenance

1. **Traceability of Decisions:**

   * Clear and detailed classification records make it easier to justify requirements applications and decisions to internal stakeholders, oversight bodies, and regulators.
   * Software-independent classification assessments by S&MA provide a valuable second perspective and ensure that classifications are well-grounded and aligned with safety-critical evaluations.
2. **Alignment Across Teams:**

   * Well-maintained records ensure that all teams involved—software engineering, S&MA, and project management—have consistent and shared understanding of the classification logic and tailored requirements.
   * This shared understanding facilitates collaboration, minimizes errors, and enables prompt resolution of any disagreements.
3. **Risk Management and Compliance:**

   * Proper records ensure compliance with NPR 7150.2 while managing risks arising from inappropriate application of requirements.
   * By linking classifications with their rationale and corresponding requirements, the records enable teams to consistently assess risks, accommodate changes, and address safety concerns effectively.
4. **Lifecycle Adaptability:**

   * Projects evolve, and requirements often change. Historical records provide the context needed to evaluate whether systems need to be reclassified or if tailoring needs updating.
   * Reclassification and appropriate tailoring based on lifecycle records ensure that software systems remain fit-for-purpose as project complexity grows.
5. **Efficient Testing Strategies:**

   * These records are invaluable in planning testing efforts, especially for systems containing multiple classifications (e.g., a mission-critical flight system integrated with analytical simulations).
   * Classification records inform the scope, rigor, and allocation of testing resources, ensuring no over-testing or under-testing occurs.
6. **OCE Reviews and Lessons Learned:**

   * During OCE surveys, records of classification and requirements mapping are used to evaluate project compliance and highlight best practices or gaps in classification logic.
   * Lessons learned from these reviews can inform future updates to NPR guidance and improve processes across NASA projects.

## 2.3 Alignment with NASA’s Broader Goals

This requirement supports NASA’s broader strategic objectives by:

* **Promoting Safety and Mission Success**: Ensuring that software requirements are properly tailored for safety-critical and high-risk systems.
* **Enabling Effective Oversight**: Providing detailed documentation that allows for transparent and accurate reviews.
* **Fostering Continuous Improvement**: Leveraging records as a knowledge bank for evaluating and improving software classification and engineering processes in future projects.

# 3. Guidance

Maintaining and retaining accurate records of software classification determinations, requirements mapping matrices, and safety-critical evaluations ensures traceability, compliance, and accountability throughout the software lifecycle. These records serve as critical references during audits, reviews, and project oversight activities, supporting effective decision-making and risk management.

## 3.1 Records Maintenance and Retention

**Purpose**:  
To ensure records documenting software classification, requirements mapping, and assurance evaluations are properly maintained for the life of the project. These records support traceability of decisions, compliance with directives, and effective oversight.

### 3.1.1 Software Classification Determination Records

**Description**:  
The project manager ensures software classification is performed for all systems and subsystems as defined in [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification).

**Important Considerations**:

1. **Multiple Software Classifications**:

   * Many projects include systems and subsystems with varying classifications (e.g., Class A for mission-critical systems, Class C for analytical tools).
   * **Appendix C of NPR 7150.2** dictates the applicability of requirements based on **software classification** and safety-criticality designation. See topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)
2. **Document Classification Rationale**:

   * Clearly define the rationale for classification decisions, including risk level, NASA investment, human dependency, and operational complexity.
   * Include traceability to hazards for systems classified as safety-critical based on **NASA-STD-8739.8**.

**Key Information to Document**:

* **System/Subsystem name**.
* **Software Classification** as defined in **Appendix D** of NPR 7150.2 [083](#_tabs-<p></p>) .
* **Safety-Critical Designation** determined using NASA-STD-8739.8 [278](#_tabs-<p></p>).
* **Rationale**for classification considering factors such as:
  + Purpose and usage.
  + Interaction with humans.
  + Development and operational complexity.

### 3.1.2 Project Software Requirements Mapping Matrix

**Description**:  
The Requirements Mapping Matrix ensures traceability between software classification and compliance with NPR 7150.2, including tailored or waived requirements.

**Important Considerations**:

1. **Applicability Across Software Classes**:

   * Create a requirements mapping matrix for each software classification present in the project. Different classifications may have distinct applicable requirements.
2. **Content of the Matrix**:

   * Mapped Requirements: List all applicable NPR 7150.2 requirements for the project’s software.
   * Compliance Methodology: Describe how each requirement will be fulfilled, including verification methods.
   * Tailored Requirements: Document any requirements tailored or waived per project needs, providing justification and approval records.

**Key Information to Document**:

* **Software Classification** for systems/subsystems (e.g., Class A, B, C).
* Mapping of **NPR 7150.2 requirements** to classification.
* **Tailoring Decisions**: Justifications for tailoring or waiving requirements, with appropriate authorization.

**Example (Matrix format):**

| Requirement | NPR 7150.2 Section | Applicable Software Class | Compliance Strategy | Tailoring Justification (if applicable) |
| --- | --- | --- | --- | --- |
| Design Verification | SWE-069 | Class B | Full compliance | N/A |
| Documentation Standards | SWE-073 | Class C | Streamlined documentation | Relevant only to non-critical components |

### 3.1.3 S&MA Independent Classification Assessment

**Description**:  
In cases where **Safety and Mission Assurance (S&MA)**performs an independent classification review, the results of this assessment should be documented and reconciled with the project's original software engineering classification.

**Important Considerations**:

1. **Resolution of Discrepancies**:

   * Any differences between the independent S&MA assessment and the project’s engineering classification should be resolved collaboratively through the Technical Authorities (TAs).
2. **Supporting Rationale**:

   * Include the methodology and rationale used for S&MA classification decisions.

**Key Information to Document**:

* Results of the S&**MA Independent Classification Assessment**: Findings, rationale, and supporting evidence.
* **Resolution Record**: Documentation of how discrepancies were resolved between engineering and S&MA classifications.

**Benefits**:

* Provides an additional layer of technical assurance for classification.
* Promotes alignment between engineering and assurance teams early in the lifecycle.

### 3.1.4 Using Records for Oversight and Lifecycle Operations

**Description**:  
These records are indispensable during operational audits (e.g., OCE surveys), major reviews (e.g., PDR, CDR), and examinations of official project documentation.

**Benefits of Maintaining Records**:

1. **Oversight and Accountability**:

   * Enables the Office of the Chief Engineer (OCE) to review classification and compliance processes across Centers.
   * Promotes adherence to internal control measures.
2. **Testing and Operational Insights**:

   * Classification documentation clarifies the relationship between software classes and project testing efforts.
   * Ensures testing rigor matches the classification and safety-criticality designation of each subsystem.

## 3.2 Periodic Review of Classification and Safety Criticality

**Description**:

Classification and safety-criticality require periodic reassessment throughout the lifecycle to reflect changes to requirements, scope, or mission objectives.

**Triggers for Review**:

1. **Major Milestones**:

   * Conduct reviews during Prelim Design Review (PDR), Critical Design Review (CDR), and other significant project milestones.
2. **Significant Scope Changes**:

   * Reassess classification when major requirements are added, removed, or modified, or if the software transitions to new operational environments.
3. **Safety-Critical Reevaluation**:

   * If new hazards or risks are identified during development or operations, reassess classification and software assurance processes.

**Benefits**:

* Prevents outdated classifications and ensures safety requirements remain appropriate for evolving project needs.

**Resources**:

* Topic [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) and Topic [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) in **NPR 7150.2** for transitioning software to a higher classification.

## 3.3 Records Location

**Description**:

The location of all classification-related records and matrices must be clearly documented in the project data management list. This ensures records can be retrieved efficiently by stakeholders throughout the lifecycle.

**Recommendations for Small Projects**:

1. **Records Management Strategy**:

   * Maintain records alongside the Software Development Plan (SDP) and Software Management Plan (SMP). See topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)
   * Reference the data management list to point reviewers to the latest classification and mapping matrices.
2. **Centralized Repository**:

   * Store classification records in shared folders, Center repositories, or cloud-based systems accessible to all project stakeholders.
3. **Update Continuously**:

   * Ensure classification records remain accurate and updated as the project progresses, particularly after milestone reviews or scope changes.

## 3.4 Key Classification Considerations

When classifying software, evaluate:

1. **All software within the system/subsystem** (individual subsystems may have unique classifications).
2. **Purpose and operational usage** of the software.
3. **Hardware and human interactions** (safety-critical operations typically require Class D or higher).
4. **Developmental and operational complexity** as aligned with classification definitions.
5. **Risk to NASA’s missions, personnel, and investments.**
6. **Relevant major programs or projects** the software supports.

If the software is tied to a hazard and deemed **safety-critical**, align it with **NASA-STD-8739.8** standards and classify accordingly. For small projects, straightforward classification processes can minimize overhead while ensuring compliance.

## 3.5 Benefits of Improved Guidance

1. **Traceability**: Clear documentation facilitates streamlined audits, lifecycle oversight, and classification reevaluations.
2. **Consistency**: Aligning all records and classification processes ensures harmonized compliance with **NPR 7150.2**.
3. **Adaptability for Small Projects**: Simplified matrix creation and classification records reduce administrative burden for low-risk systems while maintaining rigor for safety-critical software.
4. **Support for Testing Oversight**: Well-maintained records ensure adequate testing rigor is applied based on classification documentation.

This improved guidance ensures efficient records maintenance and supports NASA’s objectives of safety, accountability, and mission success.

If a software component is traceable to a hazard and is determined to be safety-critical software, per the software safety-critical determination process defined in **NASA-STD-8739.8**, [278](#_tabs-<p></p>)  then the software component classification must be Software Class D or higher.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-021 - Transition to a Higher Class](/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class) * [SWE-129 - OCE NPR Appraisals](/spaces/SWEHBVD/pages/102695491/SWE-129+-+OCE+NPR+Appraisals)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only).

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Classification](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Classification) |

# 4. Small Projects

Small projects typically involve fewer systems, reduced complexity, and limited resources, making it essential to tailor processes to meet requirements effectively without overburdening the team. Proper documentation and management of classification records, requirements mapping, and assessments are still crucial for demonstrating compliance, mitigating risk, and ensuring project success.

The benefits of this Small Project Approach include:

1. **Efficiency**: Minimized administrative overhead while maintaining compliance with NPR requirements.
2. **Clarity**: Simplified records make it easy to trace classification and requirement mapping decisions during reviews or audits.
3. **Scalability**: The approach ensures small projects can scale up their classification efforts only as needed.
4. **Flexibility**: Tailors processes to resource constraints commonly encountered in small projects.

By balancing efficiency with compliance, small projects can meet the objectives of this requirement while aligning with NASA's rigorous quality standards. This ensures that even lower-risk systems operate with the oversight and rigor necessary to achieve mission success.

This guidance outlines simplified practices tailored to small projects for fulfilling the requirements of maintaining classification records, mapping matrices, and classification assessments.

## 4.1 Key Challenges for Small Projects

1. **Limited Resources:** Small projects may lack dedicated resources for extensive documentation.
2. **Simplified Systems:** Many small projects feature straightforward software systems, reducing classification complexity.
3. **Single or Narrow Focus:** Small projects often address a specific goal, making it easier to manage classification determinations consistently across the project.

## 4.2 Simplified Approach for Record Maintenance

### 4.2.1 Software Classification Determination Records

Small projects can streamline classification determination documentation using a lightweight and consolidated approach.

**Recommended Steps:**

* **Document Classification for All Software Early:**
  + As soon as the project determines software is part of the system, complete the classification process and document it systematically.
  + Use a simple table to list all systems/subsystems, their classifications (Class A–F), safety-critical designations (if applicable), and classification rationale.

**Template Example for Small Projects**:

| **System/Subsystem Name** | **Software Role** | **Software Classification** | **Safety-Critical? (Yes/No)** | **Rationale for Classification** |
| --- | --- | --- | --- | --- |
| Data Collection Module | Collects experiment data | Class C | No | Moderate risk; critical for project delivery, not flight-related. |
| System Control Software | Operates primary system | Class B | Yes | Safety-critical due to interaction with hardware operators. |

**Keep It Simple:**

* Use a small-scale spreadsheet or document for classification records.
* Combine classification rationale and safety-critical designation outcomes into this concise format.

### 4.2.2 Software Requirements Mapping Matrix

Mapping requirements to software classifications may seem daunting for small projects, but it can be simplified to match the project scope.

**Recommended Steps:**

* **Use NASA’s Simplified Template for Appendix C Compliance:**
  + Identify the applicable requirements in **NPR 7150.2, Appendix C**, corresponding to each software classification. See topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)
  + Use a streamlined version of NASA’s mapping matrix (available at Centers or developed internally).

**Tailoring for Small Projects:**

* **List Requirements and Tailoring Justification in One Document:** Combine the requirements mapping and any tailoring decisions into a single document, ensuring clarity.
* **Small Teams and Roles:** Allow the project manager, team lead, or software assurance representative to sign off as both engineer and reviewer in smaller teams with limited staffing.

### 4.2.3 Optional: Independent Software Assurance (SA) Assessment

* **For Small Projects:** Independent classification assessments might not be required unless the system involves safety-critical software or significant complexity.
* **When Conducted:** If requested, the SA organization can document a brief confirmation of the classification or a concurrence with initial determinations using a concise memo format.

### 4.2.4 Lifetime Record Retention

* **Centralized Storage:** Maintain all classification records (system classifications, requirements mapping matrices, and SA assessments, if available) in a **single repository** for easy access throughout the project lifecycle.
* **Examples of Storage Approaches for Small Projects:**
  + Use cloud-based tools (e.g., Google Drive, SharePoint) or local version control systems to maintain records.
  + Ensure that electronic records are backed up and accessible to key stakeholders.

## 4.3 Guidance Notes for Small Projects

1. **Perform Classification As Early as Possible:**

   * Complete classification determination at project inception (prior to system requirements reviews). This ensures that all classifications align with the Software Engineering and Assurance processes from the start.
   * Use the definitions in **Appendix D (NPR 7150.2 [083](#_tabs-<p></p>) )** and the safety-critical guidance from **NASA-STD-8739.8** [278](#_tabs-<p></p>) for accurate classification.
2. **Focus on Project-Specific Risks:**

   * Small projects often have lower risks, but systems with hardware controls, human interactions, or safety-critical designations require additional care.
   * Make classification discussions a priority between software engineers and software assurance to prevent misclassification.
3. **Use Aligned Roles:**

   * Small projects may share specialists for multiple roles (e.g., a combined software engineer/Safety and Mission Assurance representative). Ensure classification agreements are documented with clear designations of authority.
4. **Escalate for Disagreements:**

   * If classification disagreements arise, leverage the Center’s Engineering Technical Authority (ETA) for swift resolution without adding unnecessary delays to the small project timeline.

## 4.4 Metrics Recommendations for Small Projects

1. **Distribution of Software Classifications**:  
   Track classifications for all software systems:

   * **Metric Example:**
     + Class A/B: 0%
     + Class C: 50%
     + Class D: 50%  
       This approach helps small projects justify their scaling of requirements.
2. **Tailored Requirements**:

   * Document the **number of tailored or waived requirements** for small projects.
   * **Metric Example:**
     + Number of tailored requirements = 2 (10% of total project requirements).

## 4.5 Example Use Case for Small Project

#### **Project Description**:

A small project is creating a **ground-based environmental data collection system** with software to manage sensor inputs, control system operations, and process collected data.

#### **Simplified Classification Process**:

1. **Identify Key Systems**:

   * Sensor Management: Software for collecting and processing environmental inputs.
   * Control Software: Software for calibrating sensors and sending commands.
2. **Classify Software Components**:

   * **Sensor Management Module**: Class C, since it involves moderate mission-critical operations but poses no risks to safety.
   * **Control Software**: Class B, as it directly impacts project success and involves interaction with control operators.
3. **Document Results**:

   * List classifications and rationale in a concise table.
4. **Requirements Mapping**:

   * Use the **Appendix C matrix** to apply the correct **NPR 7150.2** and **NASA-STD-8739.8** requirements to each classified system.
5. **Storage**:

   * Save classification and requirements mapping data in a secure project repository (e.g., shared folder).

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
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

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-176 - Software Records**

3.5.2 The project manager shall maintain records of each software classification determination, each software Requirements Mapping Matrix, and the results of each software independent classification assessments for the life of the project.

Maintaining comprehensive records of software classification determinations, requirements mapping matrices, and independent assessments ensures traceability, accountability, and adherence to NASA software engineering standards throughout the project lifecycle. These records are critical for audits, reviews, and ensuring that tailored requirements are both justified and appropriately applied.

This guidance ensures all classification-related activities are documented, consistently applied, and maintained for the lifecycle of the project to support mission success and align with NASA's software engineering and assurance standards.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that records of the software Requirements Mapping Matrix and each software classification are maintained and updated for the life of the project.

## 7.2 Software Assurance Products

### 7.2.1 Software Classification Determination Records

**Purpose**: Document the rationale and evidence for software classification decisions.  
**Contents**:

* **Systems/Subsystems Classification**: List the classification of each system and subsystem, along with justifications aligned with **Appendix D of NPR 7150.2** [083](#_tabs-<p></p>) and **NASA-STD-8739.8 [278](#_tabs-<p></p>)** .
* **Safety-Critical Designation Evaluations**: Include results from the software safety-critical determination process, with supporting rationale for classifications meeting **Class D or higher** requirements.
* **Signed Concurrence**: Evidence of agreement by Software Assurance (SMA TA) and Software Engineering (ETA).
* **Independent SA Assessment (Optional):** If an independent SA classification assessment is conducted, document the rationale and methodology used to arrive at the classification determination.

### 7.2.2 Software Requirements Mapping Matrix

Projects must maintain and track compliance via a **Requirements Mapping Matrix** that aligns the software classification with the applicable requirements from **NPR 7150.2** and **NASA-STD-8739.8**.  
**Contents**:

* **Mapping of NPR 7150.2 Requirements to Software Classifications**: Identify the requirements applicable to each class (Classes A–F) based on **Appendix C**. See topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)
* **Tailored Requirements**:
  + Document any requirements tailored for the project per local Center processes.
  + Justify any deviations or waivers filed against mapped requirements for approval.
* **Traceability to Authority Concurrence**: Include signed concurrence from both SMA TA and ETA for mapping matrices provided by each software development organization.

### 7.2.3 Independent Software Assurance Classification Assessment (Optional)

In cases where applicable or required by Center processes (or requested proactively for added assurance):  
**Contents**:

* **Assessment Results**: Results of independently performed SA classification reviews, including the detailed assessment rationale, methodology, and findings.
* **Rationale Document**: Rationale for agreement or disagreement with the project's initial classifications.
* **Resolution Notes**: Documentation of resolution reached between Software Assurance and Software Engineering (if conflicting classifications arose).

### 7.2.4 Records Retention

Per **NPR 7150.2**, all classification-related artifacts must be **maintained throughout the life of the project**.

* **Central Repository**: Retain classification records and matrices in a shared, centrally accessible repository aligned with Center record retention policies.

## 7.3 Metrics

Metrics provide valuable insight into the project’s software classification, requirements mapping, and tailoring processes. Suggested metrics include:

### 7.3.1 Distribution of Software Classifications

* **% of Total Source Code for Each Software Classification** (*organizational measure*):
  + Tracks the proportion of code across all classification levels (e.g., Class A, B, C, D, etc.), highlighting the relative scope and rigor applied.

### 7.3.2 Tailored Requirements

* **Metrics for Tailored NASA-STD-8739.8 Requirements** (*organizational measure*):
  + Tracks the number and percentage of requirements tailored by the project to meet software classification levels.
  + Provides data for tailoring trends across projects, identifying potential gaps or overuse of waivers.

### 7.3.3 Safety-Critical Compliance

* **% of Safety-Critical Components Evaluated as Class D or Higher**:
  + Tracks compliance with safety-critical designation standards outlined in **NASA-STD-8739.8** to ensure appropriately applied classifications.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

### 7.4.1 Classification Process

1. **Agreement on Classifications**:

   * Software Assurance and Software Engineering must collaborate to reach consensus on classifications for systems and subsystems.
   * SA concurrence may occur alongside the software engineering classification review when agreement exists.
2. **Independent Classification Assessment (Optional):**

   * Independent SA assessments are not required but may be conducted if deemed necessary by your Center or project.
   * If performed, document the findings, rationale, and signed concurrence for retention as part of the project lifecycle records.
3. **Multiple Classifications in Projects**:

   * Projects may contain subsystems with varying classifications depending on the nature of their purpose, risks, and safety-criticality.
   * Use **Appendix C** in **NPR 7150.2** to guide applicability of requirements across classifications. See topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)

### 7.4.2 Maintaining Records

Complete the classification process **as soon as software inclusion is confirmed** within the project scope. Records must:

1. Be maintained for the life of the project to facilitate compliance checks during audits and major reviews (e.g., PDR, CDR).
2. Include rationale for any tailored requirements or deviations based on the software classification matrix.
3. Document the resolution of any disagreements through the Engineering Technical Authority (ETA) or SMA Technical Authority (SMA TA) escalation process, if necessary.

### 7.4.3 Reclassification

Software classifications must be revisited under the following scenarios:

1. **Major Project Reviews**: Review classification at each key milestone, such as PDR or CDR, to align with evolving requirements and scope.
2. **Project Scope Changes**: Significant modifications to software usage or risk may warrant transitioning to a higher or lower classification level.

* Example: Software initially classified under **Class C** for research in a simulation environment may transition to **Class B** when integrated into operational mission systems requiring real-world use.

### 7.4.4 Benefits

1. **Traceability**: Maintained records provide long-term evidence of compliance, reducing risks during audits and post-project analyses.
2. **Consistency**: Documented processes ensure alignment of classification, requirements mapping, and tailored decisions across all systems/subsystems.
3. **Safety Assurance**: Clear documentation ensures safety-critical components are properly classified and adequately managed.
4. **Efficiency**: Metrics-based reviews help identify patterns in classification and tailoring, informing process improvements for future projects.

### 7.4.5 Guidance

When classifying software be sure to consider:

* All software for the system or subsystem (classification may need to be assessed separately).
* Purpose of the software.
* How the software is intended to be used.
* Relevance to major programs and projects.
* Hardware controls.
* Operations.
* Interaction with humans.
* Complexity (developmental and operational complexity is woven into the class definitions).
* The risk to the project, Center, and Agency Investment.

If a software component is traceable to a hazard and is determined to be safety-critical software, per the software safety-critical determination process defined in **NASA-STD-8739.8** [278](#_tabs-<p></p>),  then the software component classification must be Software Class D or higher. When classifying software be sure to consider: Topic [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-021 - Transition to a Higher Class](/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class) * [SWE-129 - OCE NPR Appraisals](/spaces/SWEHBVD/pages/102695491/SWE-129+-+OCE+NPR+Appraisals)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

**Objective evidence** is documented proof that demonstrates compliance with the classification determination and requirement mapping processes. This includes:

1. **Signed Documentation**:
   * Evidence of classification concurrence between Software Engineering (ETA) and Software Assurance (SMA TA).
   * Signed requirements mapping matrices verified by both technical authorities.
2. **Supporting Analysis**:
   * Rationale for classifications aligned with Appendix D definitions and NASA-STD-8739.8.
   * Documentation of safety-critical determination (as required for Class D or higher).
3. **Independent Assessments** (Optional):
   * Artifacts from independent SA assessments, if applicable, including rationale and signed concurrence records.

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

## 8.1 Objective Evidence to Be Maintained

1. **Software Classification Determination**:
   * Classification records for all systems and subsystems, including signed concurrence and supporting analysis.
2. **Requirements Mapping Matrix**:
   * Mapping of NPR requirements, tailored requirements, and justification for tailoring or waivers.
3. **Safety-Critical Designation Decisions**:
   * Explicit documentation of hazard traceability evaluations as defined in **NASA-STD-8739.8**.
4. **Revisions to Classifications**:
   * Documentation of classification updates due to design or project scope changes.
5. **Independent SA Assessment Records** (if performed):
   * Assessment methodology, findings, and rationale for changes resulting from these reviews.
