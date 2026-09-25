# SWE-051 - Software Requirements Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695426. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis

SWE-051 - Software Requirements Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695426)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695426&showCommentArea=true&showComments=true#addcomment)

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

4.1.3 The project manager shall perform software requirements analysis based on flowed down and derived requirements from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-051 History

SWE-051 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.1.1.3 The project shall perform software requirements analysis based on flowed down and derived requirements from the top-level systems engineering requirements and the hardware specifications and design. |
| Difference between A and B | No change |
| B | 4.1.2.2 The project manager shall perform software requirements analysis based on flowed down and derived requirements from the top-level systems engineering requirements and the hardware specifications and design. |
| Difference between B and C | Added requirement to perform software requirements analysis based on safety and reliability analyses. |
| C | 4.1.3 The project manager shall perform software requirements analysis based on flowed-down and derived requirements from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design. |
| Difference between C and D | No change |
| D | 4.1.3 The project manager shall perform software requirements analysis based on flowed down and derived requirements from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design. |

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
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Rationale

**Software requirements are the basis of a software project.**

Analyzing software requirements allows a team to ensure that they are properly formed and accurately and clearly describe the software system to be built.  The analysis provides a structured method of reviewing requirements to identify any issues with them individually or as a collected set.  The team should address identified issues before using the requirements for further project work.  This reduces the need for future rework, not only of the requirements but also of any work based on those requirements.

## 2.1 Key Reasons for this Requirement

### **1. Ensures Alignment Between Software, System, and Stakeholder Goals**

Software requirements must flow down from the higher-level system, mission, and project objectives to provide consistency and alignment. Analyzing and deriving software requirements directly from **top-level systems engineering requirements** ensures that the functionality and behavior of the software contribute to achieving the overarching goals of the project.

* **Why it matters:**  
  Without proper analysis, software requirements may be insufficient, contradictory, or disconnected from the broader system objectives, resulting in misaligned or unusable software.
  + **Example:** If the system requires high-speed data processing as a key capability, but this requirement is not explicitly captured and analyzed at the software level, the resulting software may fail to meet performance needs.

---

### **2. Accounts for Safety and Reliability Requirements**

Safety and reliability are critical aspects of mission success, especially for high-risk, complex systems (e.g., aerospace, space exploration, critical infrastructure). Software requirements analysis ensures that:

* Safety-critical requirements are identified and implemented to mitigate hazards.
* Requirements maintain the reliability and robustness of the software under all operational conditions.
* **Why it matters:**

  + Hazards and potential failure scenarios identified in **safety and reliability analyses** must be traced to specific software requirements.
  + Failure to incorporate these considerations can lead to catastrophic mission failures, as seen in past incidents (e.g., the Mars Polar Lander loss caused by inadequate software-hardware interaction modeling of lander hardware transients).
  + A robust analysis ensures proper implementation of fault-tolerant design techniques, such as redundancy, fail-safes, or recovery mechanisms.

---

### **3. Provides a Strong Foundation for Derived Requirements**

Derived requirements address functions, constraints, or behaviors that are not explicitly stated in the top-level system requirements but are needed to fully implement the system. Software requirements analysis ensures that:

* All necessary **derived requirements** are identified.
* Dependencies between components (software, hardware, and external systems) are addressed.
* **Why it matters:**

  + Derived software requirements often account for software-internal needs such as error handling, performance optimization, or multi-threaded operations driven by real-time hardware interactions.
  + If derived requirements are overlooked, gaps could cause unexpected failures or system incompatibilities.

---

### **4. Enables Comprehensive Hardware-Software Integration**

Analyzing software requirements based on **hardware specifications and designs** ensures that the software and hardware components work together seamlessly in the final system. Hardware characteristics such as timing, communication interfaces, I/O signals, processing limits, and environmental boundaries directly impact software behavior and requirements.

* **Why it matters:**  
  Hardware might:

  + Introduce latency or response constraints that must be accommodated in the software requirements.
  + Require specific protocols for communication or system monitoring.
* **Outcome:** Software requirements analysis ensures that interactions between hardware and software are modeled accurately, tested, and documented. This reduces integration risks and unforeseen performance or reliability issues in the final system.

---

### **5. Prevents Requirements Ambiguity and Reduces Downstream Errors**

System requirements are often broad, high-level objectives that need to be decomposed and analyzed to generate **unambiguous, detailed, and testable software requirements**. Performing rigorous requirement analysis ensures that inconsistencies and ambiguities inherited from the higher-level system requirements do not propagate into the software design.

* **Why it matters:**

  + Software design errors traced back to poorly defined requirements are far more costly to resolve in the later stages of development, especially in highly complex or safety-critical systems.
  + Proper analysis prevents the inclusion of unnecessary, unverifiable, or conflicting requirements.
* **Example:** Failure to clarify a high-level system requirement for data transmission rates could result in miscommunication between software and hardware teams, leading to failure during hardware-software integration.

---

### **6. Promotes Early Detection of Design and Architecture Issues**

By performing requirements analysis, the project team can identify infeasibilities or design flaws at the earliest stages of the software lifecycle. Software issues stemming from unrealistic engineering expectations, hardware limitations, or safety constraints can be flagged early, allowing teams to address them before design and development begin.

* **Why it matters:**
  + Early detection minimizes rework, saves costs, and improves the project’s timeline.
  + It allows proper allocation of resources to address critical requirements while adhering to system constraints.

---

### **7. Supports Holistic Systems Engineering Process**

Requirement 4.1.3 is a critical component of the **systems engineering process**, which emphasizes the interdependence of hardware, software, and operational systems. Software requirements analysis ensures that:

* Requirements are validated against system-level constraints.
* Interdependencies between hardware and software are thoroughly understood and accounted for.
* Software supports and fulfills higher-level requirements across operational, functional, and environmental boundaries.

---

### **8. Ensures Proper Verification and Validation of Software**

Requirements analysis drives how software will be tested and verified. Clear, detailed, and traceable software requirements allow the development team to:

* Define appropriate validation test cases to ensure the software meets mission needs.
* Verify the software against its derived and flowed-down requirements to confirm correct implementation.
* **Why it matters:**

  + Poor requirement analysis could lead to missed or incomplete verification, leaving gaps in the system’s ability to meet its intended purpose.
  + Clear requirements ensure software verification efforts are comprehensive, targeted, and measurable.

---

### **9. Mitigates Risks of Requirement Volatility**

By performing rigorous analysis early, the project team reduces the likelihood of requirement changes or misunderstandings later in the lifecycle. Volatile or misunderstood requirements are a major source of project instability, scope creep, and resource overruns.

* **Why it matters:**  
  A comprehensive requirement analysis creates a stable baseline and helps preemptively address risks that could impact cost, schedule, and quality. It provides a defensible foundation for managing changes through a formal change control process.

---

### **10. Regulatory and Standards Compliance**

Many industry standards (e.g., ISO 12207, IEEE 29148, NASA-STD-8739.8) mandate systematic software requirements analysis to ensure the integrity, traceability, and completeness of requirements as part of engineering best practices.

* **Why it matters:**
  + Failure to comply with these standards can introduce risks not only to the project’s success but also to the safety and reliability of the final system, especially in aerospace or mission-critical contexts.
  + Performing requirements analysis demonstrates adherence to regulatory and contractual requirements.

---

### **Conclusion**

Performing software requirements analysis ensures that the software component of a system fully aligns with top-level system requirements, safety analyses, and hardware constraints. It promotes clarity, completeness, and quality, reducing risks of integration failures, system anomalies, and downstream costs caused by requirement misalignment. Strong software requirements analysis serves as the foundation for successful project execution, ensuring that software reliably contributes to the system’s overall mission and performance objectives.

# 3. Guidance

The software requirements analysis determines the safety criticality, correctness, consistency, clarity, completeness, traceability, feasibility, verifiability, and maintainability of the requirements. The software requirements analysis activities include the allocation of functional, non-functional, and performance requirements to all functions.

Faulty requirements may be due to incomplete, unnecessary, contradictory, unclear, unverifiable, untraceable, incorrect, in conflict with system performance requirements, otherwise poorly written, or undocumented requirements. It is important that operators properly identify and document safety requirements, and per industry standards, ensure that safety requirements are internally consistent and valid at the system level for the resulting computing system to work safely throughout its lifecycle.

After documenting the Software Requirements, run them through a requirements analysis tool (e.g., QVScribe) to analyze their quality. (QVScribe access may be obtained via a NAMS request.)

Software requirement analysis must be performed on all safety-critical software requirements on Class A, B, and C software.  This software requirement analysis should be performed on Class D software but is not required.

It is important to ensure that requirements have been evaluated adequately for completeness because incomplete requirements can cause several problems:

* Incorrect estimates of project resources.
* Missing or additional design elements.
* Additional cost and schedule rework to correct for missing/incorrect requirements.
* Added resources for verification and validation.
* Loss of customer confidence due to improperly described requirements.

The requirements analysis methodology needs to be "measurable or otherwise verifiable." [278](#_tabs-<p></p>) Checklists of questions to consider (such as those included in the Resources section of this guidance) may be helpful.

**CMMI for Development, Version 1.3: Improving processes for developing better products and services**

Requirements Analysis - Analyze requirements to ensure that they are necessary and sufficient - SP3.3  
"In light of the operational concept and scenarios, the requirements for one level of the product hierarchy are analyzed to determine whether they are necessary and sufficient to meet the objectives of higher levels of the product hierarchy. The analyzed requirements then provide the basis for more detailed and precise requirements for lower levels of the product hierarchy."  
"As products are defined, their relationship to higher level requirements and the higher level definition of the functionality and quality attributes should be understood. Also, the key requirements used to track progress are determined. For instance, the weight of a product or size of a software product can be monitored through development based on its risk or its criticality to the customer."[157](#_tabs-<p></p>)

Regardless of the methods chosen, the project team documents the methodology used for software requirements analysis in an appropriate project document, such as the Software Development Plan/Software Management Plan (SDP/SMP), and includes some minimum steps:

* Verify requirements safety criticality, correctness, consistency, and completeness.
* Verify the requirements are clear, precise, unequivocal, verifiable, testable, maintainable, and feasible.
* Verify requirements traceability.
* Verify that requirements have been properly flowed down from one level to the next (i.e., from the system requirements to the software subsystem requirements and the various levels of requirements within the software subsystem).
* Verify that requirements have been properly identified and flowed across from the software interfaces, including all computer hardware and fault management requirements.
* Examine the requirements "individually and as an integrated set.

See also topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)

The analysis of software requirements is performed in conjunction with the allocation and decomposition of requirements. Guidance on the logical decomposition of requirements may be found in [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements).

The following roles may be involved in software requirements analysis:

* Software Requirements Engineers including Software Engineers and Developers
* Software Safety Engineers, Software Assurance, Safety Assurance
* Systems Engineers
* Hardware Engineers
* Cybersecurity Engineers
* Operations Engineers
* Fault Management Engineers
* Customers/Users

Software requirements analysis begins after the System Requirements Review (SRR) milestone. The development team analyzes the software requirements for completeness and feasibility. The development team may use a structured or object-oriented analysis and a requirements classification methodology to clarify and augment the requirements. Prioritizing requirements may also occur as part of requirements analysis. Developers work closely with the requirements definition team to resolve ambiguities, discrepancies, and “to-be-determined” (TBD) requirements or specifications. Special emphasis should be placed on software reuse throughout the requirements analysis and the design phase, identifying potentially reusable architectures, designs, code, and approaches.

When the requirements analysis is complete, the development team prepares a summary requirements analysis report and holds a Software Requirements Review (SwRR). During the SwRR, the development team presents the results of their analysis for evaluation. Following the SwRR, the requirements definition team may need to update the requirements specification to incorporate any necessary modifications. The requirements analysis is revised based on changes to requirements made after SwRR. This revision work is completed by Preliminary Design Review (PDR) at the same time the requirements are baselined. The Entry/Exit Criteria for the SwRR milestone review are defined in Topic [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria).

Software requirements analysis is a continuous activity performed on all software requirements and software requirement changes.

The use of formal inspections is an excellent method of reviewing requirements with stakeholders because it brings multiple viewpoints to bear and also achieves a common understanding of the requirements. Information on formal inspections can be found in [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures). Software peer reviews/inspections ([SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)) are a recommended best practice for all safety and mission-success-related requirements, design, and code software components. Guidelines for software peer reviews/inspections are contained in Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

## 3.1 Determine safety criticality

Software safety personnel need to be involved in the analysis of software requirements to determine their safety criticality. Software safety personnel analyze software requirements in terms of safety objectives to determine whether each requirement has safety implications. Those requirements with safety implications are designated and tracked as "safety-critical."

Additional analysis steps typically performed by software safety personnel include:

* Verification that software safety requirements are derived from appropriate parent requirements, include modes, states of operation, and safety-related constraints, and are properly marked.
* Verification that software safety requirements "maintain the system in a safe state and provide adequate proactive and reactive responses to potential failures."

Additional information on the analysis performed by software safety personnel can be found in the Topics [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) and [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) of this Handbook (NASA-HDBK-2203).

The criterion for determining software safety criticality is defined in NASA-STD-8739.8.

See also [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist),

## 3.2 Determine correctness

Requirements are considered correct if they respond properly to situations and are appropriate to meet the objectives of higher-level requirements. A method for determining correctness is to compare the requirements set against operational scenarios developed for the project.

## 3.3 Determine consistency

Requirements are consistent if they do not conflict with each other within the same requirements set and if they do not conflict with system (or higher-level) requirements. Some examples of inconsistencies are using different terminology, values, or units of measure in different places when in fact they should be the same terminology/value/unit. It is helpful to have at least one person read through the entire set of requirements to confirm the use of consistent terms/terminology/values/units throughout. A requirements analysis tool may also be able to catch some of these inconsistencies.

## 3.4 Determine clarity

Requirements are clear if they are precise, unequivocal, and unambiguous (can only be interpreted one way) both individually and as a collection. Requirements need to be concise, stated as briefly as possible without affecting the meaning.

Suggested methods for confirming the clarity of requirements include:

* Reading the requirements and supporting documents.
* Formal inspection.

## 3.5 Determine completeness

Requirements are complete if there are no omissions or undefined conditions in the requirements set. Requirements are also complete if there are no "TBDs" in the requirements set.

Suggested methods for confirming the completeness of requirements include:

* Reading the requirements and supporting documents including the requirements traceability.
* Formal inspection.
* Reviewing the requirements set to confirm that availability, installation, maintainability, performance, portability, reliability, safety, security, and other requirements are included as appropriate to the project. [061](#_tabs-<p></p>)
* Review the requirements to confirm they are "sufficiently complete to begin design." [061](#_tabs-<p></p>)
* Review the requirements to confirm they have any necessary accompanying rationale and verifiable assumptions. [086](#_tabs-<p></p>)
* Review the requirements set against nominal and off-nominal operational scenarios developed for the project.
* Review the requirements using the various requirements checklists specified in Section 3.11 below.

## 3.6 Determine traceability

When determining requirement traceability, the team ensures that requirements are traced bi-directionally so that all software requirements have a parent (higher level) requirement, and all levels of software requirements flow down to the appropriate detailed (lower) levels for implementation. For requirements to be properly traced, they are also uniquely identified.

Suggested methods for this type of analysis include:

* Trace requirements from parent/source documents into the software requirements specification and vice versa.
* Review existing traceability matrices for completeness and accuracy ([SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability)).
* Review the requirements set to confirm there are no "extra" or "unneeded" requirements (those not necessary to meet the parent requirement).

## 3.7 Determine feasibility

Technically feasible requirements are reasonable, realistic requirements that can be implemented and integrated successfully to meet the operational concepts and system requirements of the project within the given operating environment, budget, schedule, available technology, and other constraints. [061](#_tabs-<p></p>)

Suggested methods for this type of analysis include:

* Reviewing requirements to confirm they do not "overly constrain the design." [061](#_tabs-<p></p>)
* Reviewing the requirements to confirm they do not unnecessarily "necessitate the use of non-standard, unusual, or unique hardware or software." [061](#_tabs-<p></p>)
* Review the requirements to confirm they are appropriate for the operation and maintenance of the project.
* Reviewing the requirements to confirm all requirements are realistic including performance requirements.

## 3.8 Determine verifiability

Requirements are verifiable if they are testable. They are also verifiable if there is “a technique to verify and/or validate the requirement."  001 Suggested techniques include testing, demonstration, inspection, and analysis. Engineering and Software Assurance have a joint responsibility for ensuring the requirements are verifiable.

Suggested methods for determining if requirements are verifiable include:

* Reviewing the requirements to confirm that they use verifiable terms (e.g., do not use terms such as "easy," "sufficient," and "adequate").
* Reviewing the requirements set to confirm requirements are "stated precisely to facilitate specification of system test success criteria." [086](#_tabs-<p></p>)
* Confirming that there is at least one feasible method/technique identified to verify the requirement

## 3.9 Determine maintainability

Requirements are maintainable if they are "written so that ripple effects from changes are minimized (i.e., requirements are as weakly coupled as possible)." [086](#_tabs-<p></p>) Maintainability can be achieved, by reviewing the requirements set and looking for unnecessarily coupled or interdependent requirements.

## 3.10 Communicate outcome

Although not considered a software engineering product, it is recommended that the results of software requirements analysis be captured in the project documentation and communicated to those who need this information to make decisions or to develop (or update) project documents. The stakeholders and the project will decide how to address the results of the analysis, including any changes that need to be made to address the findings. The methodology used for the software requirements analysis and the results of the software requirements analysis is communicated at multiple project formal reviews as defined in the software development or management plan. Specifically, according to the NASA Software Assurance and Software Safety Standard (NASA-STD-8739.8).Guidance for the analysis report content may be found in Topic [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content).

## 3.11 Requirements Checklists

There are several checklists that aid in the analysis of software requirements. They look at the various aspects described in the previous sections. The available requirements checklists are:

* [PAT-003 - Functional Requirements Checklist](/spaces/SITE/pages/112656804/PAT-003+-+Functional+Requirements+Checklist)
* [PAT-004 - Safety Requirements Analysis Checklist](/spaces/SITE/pages/112656824/PAT-004+-+Safety+Requirements+Analysis+Checklist)
* [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements)
* [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist)
* [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist)
* [PAT-079 - Requirements Quality Checklist](/spaces/SITE/pages/207290572/PAT-079+-+Requirements+Quality+Checklist)
* [PAT-080 - Requirements Contents Checklist](/spaces/SITE/pages/207290574/PAT-080+-+Requirements+Contents+Checklist)
* [PAT-081 - Requirements Editorial Checklist](/spaces/SITE/pages/207290577/PAT-081+-+Requirements+Editorial+Checklist)
* [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software)

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Product Requirements related to Human Rated Software.

## 3.12 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)       * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [PAT-003 - Functional Requirements Checklist](/spaces/SITE/pages/112656804/PAT-003+-+Functional+Requirements+Checklist) * [PAT-004 - Safety Requirements Analysis Checklist](/spaces/SITE/pages/112656824/PAT-004+-+Safety+Requirements+Analysis+Checklist) * [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements) * [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist) * [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist) * [PAT-042 - Requirements Development and Mgmt Audit](/spaces/SITE/pages/198770759/PAT-042+-+Requirements+Development+and+Mgmt+Audit) * [PAT-056 - Software Development Management Plan Assessment](/spaces/SITE/pages/198770884/PAT-056+-+Software+Development+Management+Plan+Assessment) * [PAT-059 - Software Requirements Specification Assessment](/spaces/SITE/pages/198770890/PAT-059+-+Software+Requirements+Specification+Assessment) * [PAT-079 - Requirements Quality Checklist](/spaces/SITE/pages/207290572/PAT-079+-+Requirements+Quality+Checklist) * [PAT-080 - Requirements Contents Checklist](/spaces/SITE/pages/207290574/PAT-080+-+Requirements+Contents+Checklist) * [PAT-081 - Requirements Editorial Checklist](/spaces/SITE/pages/207290577/PAT-081+-+Requirements+Editorial+Checklist) |

## 3.13 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

# 4. Small Projects

For projects with small budgets, limited personnel, or other resource constraints, it is critical to ensure that software requirements analysis is thorough despite scaling down processes or team roles. Requirements analysis remains foundational to project success, and skipping important activities can lead to downstream issues, such as costly rework, integration issues, or unmet project goals. The following enhanced guidance provides practical, efficient strategies to perform high-quality requirements analysis within the constraints of smaller projects.

---

### **1. Consolidate Activities Without Compromising Quality**

* **Streamline Reviews:**  
  Small projects may limit the number of formal reviews or overlapping activities typically involved in requirements analysis. However, it is important to retain the core steps, such as:

  + Verifying requirement clarity, correctness, and completeness.
  + Tracing requirements to parent/system-level requirements to ensure alignment.
  + Ensuring requirements are testable, unambiguous, and feasible.
* **Use Checklists or Guides:**  
  Create or adopt checklists to ensure all critical analysis activities are addressed systematically. Checklists act as simple guides for validating requirements without needing extensive resources. Key elements to include in the checklist are:

  + Alignment with higher-level requirements.
  + Consistency and feasibility.
  + Safety, security, and interface requirements.
  + Hardware/software compatibility considerations.

  **Example Checklist Tools:**

  + NASA’s Requirements Compliance Checklist. (see Topic **[7.16 - Appendix C. Requirements Mapping and Compliance Matrix](https://swehb.nasa.gov/display/SWEHBVD/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix))**
  + Templates from standard frameworks like ISO 29148 or IEEE.

---

### **2. Leverage Cross-Disciplinary Experts or Fresh Perspectives**

* **Multiple Roles on Small Teams:**  
  When team members fill multiple roles (e.g., project manager also acting as software engineer or tester), there is a risk of oversight due to limited viewpoints. In such cases:

  + Engage external experts (e.g., from a Center of Excellence, advisory board, or SMEs) to review the requirements.
    - **Benefits:** “Fresh eyes” can spot ambiguous or unclear requirements, identify missing safety elements, and provide domain-specific insights.
  + Use these experts to fulfill specialized roles, such as safety and reliability analysis or independent verification. Freelancers, retired professionals, or collaboration with other NASA projects may be good sources for this expertise.
* **Example:**  
  If no one on the team has expertise in software-hardware integration, consult engineers from the hardware-focused team or organization experts to assess that aspect of the requirements.

---

### **3. Use Lightweight Tools for Efficiency**

Small projects can leverage free or low-cost tools to improve the efficiency and quality of requirements analysis. These tools can simplify the process, automate parts of the analysis, and reduce manual effort.

#### **Recommended Tools:**

1. **QVScribe:**

   * Features: Evaluates requirement completeness, clarity, and compliance with standards.
   * Benefits: Frees up time by flagging poorly written requirements and suggesting improvements.
2. **Natural Language Processing (NLP) Tools:**  
   Some NLP tools identify ambiguous wording, incomplete formatting, or inconsistencies in requirements language.
3. **Traceability Tools (e.g., Excel or Free Alternatives):**

   * Use spreadsheets or lightweight, free tools like ReqView or Open Source Requirements Management (OSRMT) for managing traceability.
   * Ensure traceability between system-level and software-level requirements, as well as links to test cases.
4. **Interactive Software Diagrams (e.g., a whiteboard tool):**

   * Tools like Lucidchart or Miro (free for small projects) can make reviewing functional and system relationships much clearer.

---

### **4. Prioritize Requirements for Critical Focus**

When resources are limited, focusing on the requirements that are most critical to the project’s success is essential. Not all requirements have equal importance, so prioritize your analysis efforts by categorizing requirements as follows:

* **Mission-critical requirements:** Ensure these requirements are complete, testable, and unambiguous, as they affect the key objectives of the project.
* **Safety-sensitive or hardware-dependent requirements:** Give additional scrutiny to requirements tied to safety-critical functions or hardware/software interfaces.
* **Low-priority requirements:** Defer detailed analysis of "nice-to-have" or low-impact requirements if time and resources are constrained.

---

### **5. Build in Collaborative Reviews**

Even if formal review boards cannot be convened due to resource constraints, informal **peer reviews** can still be a cost-effective way to ensure requirements quality.

* Use collaborative tools for asynchronous reviews if team members or external experts are in different locations. Shared documents or repositories (e.g., Google Docs, GitHub, NASA Box, or NASA's software engineering tools) allow team members to review and adapt requirements collaboratively.
* **Example:**  
  Share the requirements document and request comments from a blend of system engineers, software developers, and testers. Incorporate their feedback iteratively.

---

### **6. Define and Address COTS/GOTS/MOTS/OSS Requirements**

When the software includes Commercial Off-The-Shelf (COTS), Government Off-The-Shelf (GOTS), Modified Off-The-Shelf (MOTS), or Open Source Software (OSS), account for their unique requirements during analysis.

* Ensure compatibility between these components and project hardware/software.
* Identify specific constraints and limitations (e.g., licensing, scalability, security risks, performance bottlenecks).
* Tools like SPDX for license tracking or simple compatibility checklists can assist small teams.

---

### **7. Take Advantage of Reused Work Products**

Leverage existing resources to avoid "reinventing the wheel." This is particularly beneficial for small projects with limited personnel:

* Review requirements from similar past projects that address comparable hardware or mission contexts.
* Use organizational libraries of templates, requirements databases, or even guidelines from well-documented NASA projects.

---

### **8. Monitor Progress Using Lean Metrics**

Even for small projects, metrics help track the quality and progress of requirements analysis. Examples of simple metrics to implement:

1. **% of requirements validated:** Number of verified software requirements vs. total requirements.
2. **Traceability completeness:** Percentage of detailed requirements that trace back to parent/system requirements.
3. **Defect rate:** Percentage of requirements identified as deficient during peer reviews or SA reviews (e.g., ambiguous, unverifiable, etc.).

---

### **Summary**

For small projects with limited resources, performing effective software requirements analysis requires combining light processes with practical tools and leveraging external expertise as needed. By focusing on:

* Core analysis activities,
* Using simple, free tools to reduce manual effort,
* Engaging external experts for specialized roles,  
  small teams can deliver high-quality software requirements while adhering to constraints. This ensures alignment with top-level goals and helps mitigate risks associated with incomplete, ambiguous, or poorly analyzed software requirements.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-061)

  [Software Requirements Engineering: Practices and Techniques,](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=875d04783add30ea3ed1381f682207a992169ebc "Click to open in new window")

  JPL Document D-24994, NASA Jet Propulsion Laboratory, 2003.
   See Page 20.
  Approved for U.S. and foreign release.
* (SWEREF-086)

  [Product Requirements Development and Management Procedure,](https://sw-eng.larc.nasa.gov/files/2013/05/5526_7-21-06_Req_RevA_generic-R1V0.doc "Click to open in new window")

  5526\_7-21-06\_Req\_RevA\_generic-R1V0, 2006.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-105) Software System/Subsystem Requirements Specifications (SSRS) Checklist,  NASA Marshall Space Flight Center (MSFC) , 2012. This NASA-specific information and resource may be available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-174)

  [Systems Engineering Fundamentals,](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-885j-aircraft-systems-engineering-fall-2005/readings/sefguide_01_01.pdf "Click to open in new window")

  Department of Defence Systems Management College, Supplementary text prepared by the Defense Acquisition University Press, Fort Belvoir, VA, 2001.
* (SWEREF-189) Writing an SRS,  Foster, C.M. (1993). Analex Corporation for Glenn Research Center. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-559)

  [Orbital Space Plane - Stay true to the process!](https://llis.nasa.gov/lesson/1501 "Click to open in new window")

  Public Lessons Learned Entry: 1501.
* (SWEREF-576)

  [Software Requirements Management](https://llis.nasa.gov/lesson/3377 "Click to open in new window")

  Public Lessons Learned Entry: 3377.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Process Asset Templates

**SWE-051 Process Asset Templates**

Click on a link to download a usable copy of the template.

* (PAT-003 - )

  [PAT-003 - Functional Requirements Checklist,](https://swehb.nasa.gov/download/attachments/112656804/PAT-003%20-%20Functional%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, Tab 4,
* (PAT-004 - )

  [PAT-004 - Safety Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/112656824/PAT-004%20-%20Safety%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  8.54 - Software Requirements Analysis, tab 3, Also used in Peer Review Checklists (A.10).
* (PAT-007 - )

  [PAT-007 - Checklist for General Software Safety Requirements](https://swehb.nasa.gov/download/attachments/114327720/PAT-007%20-%20Checklist%20for%20General%20Software%20Safety%20Requirements.docx?api=v2 "Click to open in new window")

  Topic 6.2, Topic Group: Programming Checklists
* (PAT-013 - )

  [PAT-013 - Software Requirements Checklist,](https://swehb.nasa.gov/download/attachments/114328303/PAT-013%20-%20Software%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.1, Also in Peer Review and Requirements Analysis categories.
* (PAT-034 - )

  [PAT-034 - SA Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/154501148/PAT-034%20-%20SA%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, Tab 2.3.1 - SA Requirements Analysis Checklist
* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management.
* (PAT-056 - )

  [PAT-056 - Software Development Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770884/PAT-056%20-%20Software%20Development%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Development - Management Plan. Based on the minimum recommended content for a Software Development - Management Plan.
* (PAT-079 - )

  [PAT-079 - Requirements Quality Checklist](https://swehb.nasa.gov/download/attachments/207290572/PAT-079%20-%20Requirements%20Quality%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.2 Requirements Quality Checklist
* (PAT-080 - )

  [PAT-080 - Requirements Contents Checklist](https://swehb.nasa.gov/download/attachments/207290574/PAT-080%20-%20Requirements%20Content%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.3 Requirements Contents Checklist
* (PAT-081 - )

  [PAT-081 - Requirements Editorial Checklist](https://swehb.nasa.gov/download/attachments/207290577/PAT-081%20-%20Requirements%20Editorial%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.4 Requirements Editorial Checklist The purpose of this checklist is to aid the analyst when reviewing the software requirements from an editorial perspective.

**Requirements Development and Analysis Process Asset Templates**

Click on a link to download a usable copy of the template. (ReqAn)       10/2/2025 - 10 items

**Requirements Development and Analysis Process Asset Templates**

* (PAT-003 - )

  [PAT-003 - Functional Requirements Checklist,](https://swehb.nasa.gov/download/attachments/112656804/PAT-003%20-%20Functional%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, Tab 4,
* (PAT-004 - )

  [PAT-004 - Safety Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/112656824/PAT-004%20-%20Safety%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  8.54 - Software Requirements Analysis, tab 3, Also used in Peer Review Checklists (A.10).
* (PAT-007 - )

  [PAT-007 - Checklist for General Software Safety Requirements](https://swehb.nasa.gov/download/attachments/114327720/PAT-007%20-%20Checklist%20for%20General%20Software%20Safety%20Requirements.docx?api=v2 "Click to open in new window")

  Topic 6.2, Topic Group: Programming Checklists
* (PAT-013 - )

  [PAT-013 - Software Requirements Checklist,](https://swehb.nasa.gov/download/attachments/114328303/PAT-013%20-%20Software%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.1, Also in Peer Review and Requirements Analysis categories.
* (PAT-034 - )

  [PAT-034 - SA Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/154501148/PAT-034%20-%20SA%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, Tab 2.3.1 - SA Requirements Analysis Checklist
* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management.
* (PAT-059 - )

  [PAT-059 - Software Requirements Specification Assessment](https://swehb.nasa.gov/download/attachments/198770890/PAT-059%20-%20Software%20Requirements%20Specification%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Requirements Specification. Based on the minimum recommended content for a Software Requirements Specification.
* (PAT-079 - )

  [PAT-079 - Requirements Quality Checklist](https://swehb.nasa.gov/download/attachments/207290572/PAT-079%20-%20Requirements%20Quality%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.2 Requirements Quality Checklist
* (PAT-080 - )

  [PAT-080 - Requirements Contents Checklist](https://swehb.nasa.gov/download/attachments/207290574/PAT-080%20-%20Requirements%20Content%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.3 Requirements Contents Checklist
* (PAT-081 - )

  [PAT-081 - Requirements Editorial Checklist](https://swehb.nasa.gov/download/attachments/207290577/PAT-081%20-%20Requirements%20Editorial%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.4 Requirements Editorial Checklist The purpose of this checklist is to aid the analyst when reviewing the software requirements from an editorial perspective.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database provides valuable insights into best practices and challenges encountered during software requirements analysis. These lessons reflect the importance of rigorous processes, stakeholder involvement, and early validation of requirements. Below is an improved collection of lessons learned, along with additional relevant lessons not previously included.

---

### **Lessons Learned Related to Software Requirements Analysis**

#### **1. Early Identification of Requirements Deficiencies Minimizes Downstream Impacts**

**Lesson Title:** Software Requirements Management  
**Lesson Number:** 3377

* **Key Point:**  
  Incomplete, incorrect, or changing software requirements significantly impact cost, schedule, and functionality. These issues become exponentially more expensive to address later in the software lifecycle.
* **Key Takeaways:**
  + Rigorous upfront requirements analysis and validation reduce the risk of errors propagating into later phases like design, testing, and integration.
  + Implement tools or processes for capturing and stabilizing requirements early in the design phase to mitigate incremental risks.

#### **2. Follow a Rigorous Systems Engineering Process for Requirements Development**

**Lesson Title:** Orbital Space Plane - Stay True to the Process!  
**Lesson Number:** 1501

* **Key Point:**  
  Requirements development that deviates from established systems engineering principles leads to poor alignment between requirements, system design, and project goals. In the Orbital Space Plane project, issues included functional decomposition gaps, poorly defined feasibility processes, and lack of synchronization between requirements and system design.
* **Key Takeaways:**
  + Ensure that requirements follow systems engineering guidelines, including performance and functional allocation, feasibility assessments, and validation.
  + Synchronize requirements development with system design activities to prevent misalignment and ensure traceability between requirements and design decisions.
  + Avoid prematurely baselining incomplete requirements before key analyses are conducted.

---

#### **Additional Relevant NASA Lessons Learned**

#### **3. Ensure Adequate Integration of Hardware and Software Requirements**

**Lesson Title:** Probable Scenario for Mars Polar Lander Mission Loss  
**Lesson Number:** 0938

* **Key Point:**  
  Software requirements were not fully aligned with known hardware characteristics, resulting in operational failures. This highlighted the necessity of incorporating hardware operational transients and behavior into software requirements.
* **Key Takeaways:**
  + Synchronize software requirement analysis with hardware specifications and design to account for real-world interactions.
  + Prioritize thorough verification and validation of hardware-software compatibility.
  + Include safety and operational constraints in requirements documentation to avoid disconnects between hardware and software performance.

---

#### **4. Stability and Traceability of Requirements Are Essential for Program Success**

**Lesson Title:** Chandra X-ray Observatory Development Program "Lessons Learned"  
**Lesson Number:** 0987

* **Key Point:**  
  A stable set of requirements drives successful software and system development. The Chandra program benefited from maintaining traceable and consistent requirements throughout the lifecycle, while involving all relevant stakeholders.
* **Key Takeaways:**
  + Avoid scope creep by stabilizing requirements prior to baselining.
  + Ensure requirements traceability both upward (to system-level requirements) and downward (to design and test cases).
  + Involve all stakeholders, including operations, throughout the requirements development process to account for cross-functional inputs and reduce downstream issues.

---

#### **5. Prioritize Involvement of Software Assurance in Requirements Analysis**

**Lesson Title:** Software Validation (Lessons Learned from Space Shuttle GPS Navigation System)  
**Lesson Number:** 1370

* **Key Point:**  
  Software Assurance teams must be actively involved in reviewing and validating requirements, especially for dependencies on external components like COTS, GOTS, or MOTS software. In the Space Shuttle program, gaps in independent validation contributed to technical and operational challenges.
* **Key Takeaways:**
  + Engage Software Assurance early in the requirements definition process to identify risks tied to safety and reliability.
  + Use structured, independent reviews to validate compatibility of external software with project-specific requirements.
  + Apply metrics to track requirement coverage and identify gaps that may affect validation.

---

#### **6. Coordination Across Teams Prevents Integration Challenges**

**Lesson Title:** Operations/User Requirements Not Integrated Early Enough  
**Lesson Number:** 1842

* **Key Point:**  
  Failure to incorporate operations/user requirements early in the software requirements phase can lead to disconnects between system design and operational goals, resulting in costly redesigns later.
* **Key Takeaways:**
  + Ensure requirements analysis includes inputs from operations, user teams, and those responsible for human interfaces.
  + Use iterative reviews with user representatives to clarify operational performance needs during requirements development.

---

#### **7. Address External Software Dependencies Proactively in Requirements**

**Lesson Title:** Lessons Learned from Use of External Software (COTS/GOTS/MOTS Integration Challenges)  
**Lesson Number:** 2219

* **Key Point:**  
  Software projects often fail to adequately define requirements related to externally sourced components (e.g., COTS, GOTS, OSS). This leads to compatibility, security, or licensing issues during development and integration.
* **Key Takeaways:**
  + Clearly define requirements for external components during the analysis phase, including functionality, compatibility, and performance.
  + Account for risks such as licensing restrictions, system integration challenges, and proprietary changes.

---

#### **8. Avoid "Engineering-By-Presentation" and Informal Requirement Practices**

**Lesson Title:** Pitfalls of "Engineering-by-Presentation"  
**Lesson Number:** 1715

* **Key Point:**  
  Relying on informal communication methods (e.g., presentations, emails, or outdated documentation) for requirement definition prevents traceability and verifiability. This leads to unclear software requirements and unstructured decision-making.
* **Key Takeaways:**
  + Document requirements formally and ensure all decisions are traceable.
  + Use structured communication methods to finalize and communicate requirements to all stakeholders.
  + Maintain a single source of truth for requirement versions and updates to avoid inconsistencies.

---

#### **9. Incomplete Requirement Validation Contributes to Poor Testing Outcomes**

**Lesson Title:** Software Requirements Validation Lessons Learned (General NASA Guidance)

* **Key Point:**  
  Poor validation of software requirements prior to baselining disrupts testing and delays integration. Unvalidated requirements often result in missing test cases or untested scenarios, leading to failures in critical systems.
* **Key Takeaways:**
  + Ensure all software requirements are verifiable and tied to test cases or validation criteria.
  + Conduct systematic validation reviews to verify feasibility and correctness before baselining requirements.
  + Include subject matter experts during validation to ensure coverage of edge cases and operational risks.

---

### **10.** Lessons Learned: In Class D, Fault Protection Becomes the Safety Net—So It Must Be Excellent

**Problem/Observation:**  
Class D missions accept higher hardware and redundancy risk, which places greater reliance on software‑based fault protection (FP). The Anomaly Review Board (ARB) emphasized that FP must be robust enough to compensate for these elevated risks. For LTB, several FP weaknesses emerged that limited the system’s ability to autonomously protect itself.

**ARB Context:**  
The ARB explicitly stated:  
“On a Class D mission that assumes risk, ensure that the safety net of fault protection can adequately mitigate some of the risks.”

**Contributing Factors:**  
• Incorrect or insufficiently validated FP thresholds.  
• Fault protection logic split across multiple authorities and implementation paths.  
• Sequence‑based safing behaviors and FSW‑based safing behaviors were never tested together end‑to‑end.  
• Missing telemetry limited situational awareness and inhibited on‑orbit diagnosis.  
• Reset behavior and recovery paths were not fully characterized or validated.

**Resulting Impacts:**  
The spacecraft’s ability to safely respond to anomalies was compromised. Fragmented FP design, incomplete testing, and unclear behavior under reset conditions reduced system resilience during off‑nominal events.

**Relevant SWEHB Guidance:**  
Core SWEHB requirements remain applicable even when tailored for Class D:  
• SWE‑057 (Software Architecture) requires the design and documentation of fault management behavior.  
• SWE‑050, SWE‑051, and SWE‑055 require verifiable, traceable FP‑related requirements and logic.  
• SWE‑070 and SWE‑073 require modeling, simulation, and end‑to‑end testing to validate FP behavior under nominal and off‑nominal conditions.

**Lesson Learned:**  
Class D missions rely disproportionately on software fault protection because hardware redundancy is limited. For this reason, FP must be designed, validated, and tested with exceptional rigor. Software fault protection is a mission‑critical system—not an optional enhancement—and must be treated as such from architecture through ATLO and operations.

### **11.** **Lesson Learned (Starliner CFT):** **High‑level requirements invite misinterpretation; safety‑critical behavior must be fully specified and traceable.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Key propulsion/command requirements were high‑level; hazard analyses and safety requirements were not fully decomposed into verifiable software behavior with end‑to‑end traceability.

**Contributing Factors:**

* Ambiguity in expected behaviors (thresholds, timing, reset handling, telemetry fidelity).
* Weak linkage between hazard mitigations and software requirements/tests.

**Impacts:**

* Misinterpretation across teams; gaps persisted into integrated test.
* Incomplete verification evidence for safety‑critical functions.

**Recommended Practices (Aligned to SWE‑050/051/055):**

* Perform **behavioral decomposition**: translate safety requirements into concrete, measurable software requirements (thresholds, timing, state transitions, telemetry).
* Maintain **bidirectional traceability** from hazards → safety requirements → software requirements → test evidence.
* Use **structured requirement reviews** with SA participation and defect tracking.

**Actionable Checks:**

* RTM (Requirements Traceability Matrix) shows full chain from hazards to evidence.
* Safety requirements include quantitative parameters and acceptance criteria.
* Review minutes capture issues and resolutions with SA sign‑off.

### **Conclusion**

The lessons learned emphasize the criticality of structured, thorough, and consistent software requirements analysis for NASA projects. Deficient or unclear requirements can lead to project failures, cost overruns, unsafe operations, or system incompatibilities. By adhering to systems engineering guidelines, engaging cross-functional stakeholders, tracing requirements thoroughly, involving Software Assurance, and leveraging lessons from past NASA efforts, teams can ensure high-quality requirements that drive mission success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Consider impact on testing when developing requirements in early lifecycle phases](https://software.gsfc.nasa.gov/lesson-details/84/). **Lesson Number 84**: The recommendation states: "Consider impact on testing when developing requirements in early lifecycle phases, and ensure a critical review by operations team members."
* [Validation of the science data earlier in the life cycle](https://software.gsfc.nasa.gov/lesson-details/92/). **Lesson Number 92**: The recommendation states: "Plan for and implement validation of the science data earlier in the life cycle, particularly for externally provided instruments."
* [Primary Instruments should have a Programmable Processor](https://software.gsfc.nasa.gov/lesson-details/105/). **Lesson Number 105**: The recommendation states: "Primary Instruments should have a Programmable Processor."
* [Develop science data processing requirements to the necessary level](https://software.gsfc.nasa.gov/lesson-details/116/). **Lesson Number 116**: The recommendation states: "Develop science data processing requirements to the necessary level to support development."
* [Project's hardware designers to include a debug register that is both readable and writable](https://software.gsfc.nasa.gov/lesson-details/160/). **Lesson Number 160**: The recommendation states: "Advise the project's hardware designers to include a debug register that is both readable and writable, to enable software developers to test read and write accesses to the hardware."
* [Systems Engineer should revisit requirements every build](https://software.gsfc.nasa.gov/lesson-details/285/). **Lesson Number 285**: The recommendation states: "Software Systems Engineer should work with the customer stakeholder to fully understand the Parent REQ (i.e. the original reason/purpose of REQ) when writing the related Child REQ. This should be captured in the Child REQ Rationale for use by the software developer during implementation.  Refer to GPR 7123.1C: Systems Engineering. Section 4, Key Systems Engineering Functions, addresses this Lesson, particularly Sections 4.1.1, Understanding the Objectives, and 4.1.4, Requirements Identification, where it states, “Rationale should be documented for each requirement. Capturing the reasoning behind requirements is critical to future management of requirement changes.”"
* [Engage system test leads in flight software (FSW) requirements](https://software.gsfc.nasa.gov/lesson-details/299/). **Lesson Number 299**: The recommendation states: "Before the System Requirements Review (SRR), reach out to your system test lead (or someone with experience with testing similar systems) to review your electrical and flight software (FSW) architecture, requirements, and use cases. Specifically, ask them to identify any changes that would simplify the system testing."
* [Satisfy critical functionality with systems developed against key requirements, not as a Tech Demo](https://software.gsfc.nasa.gov/lesson-details/341/). **Lesson Number 341**: The recommendation states: "It is risky to assume that functionality developed as Tech Demo will receive sufficient attention/resource to achieve operational status. Instead, designate desirable functions as requirements, so they receive project resources and priority."
* [Goddard Dynamic Simulator (GDS) Fault Management derived Requirements](https://software.gsfc.nasa.gov/lesson-details/344/). **Lesson Number 344**: The recommendation states: "The Goddard Dynamic Simulator (GDS) team needs to review the GDS requirements when the fault management table is initially defined (as well as when there are changes to the tables), and during the FSW Build Testing phase, at the start of Systems Testing. This review should include working with the Flight Software team at the contents of the Fault Detection and Correction (FDC) tables to determine what telemetry needs to be simulated. This review may result in new GDS requirement(s)."

# 7. Software Assurance

**SWE-051 - Software Requirements Analysis**

4.1.3 The project manager shall perform software requirements analysis based on flowed down and derived requirements from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Perform a software assurance analysis on the detailed software requirements to analyze the software requirement sources and identify any incorrect, missing, or incomplete requirements.

## 7.2 Software Assurance Products

The results of independent Software Assurance analysis performed on the detailed software requirements are a critical product for ensuring requirement correctness and addressing potential issues before design and development. The key outputs for this SA Tasking should include:

* **Software Requirements Analysis Results or Report:**
  + This report should identify unclear, conflicting, incomplete, unverifiable, or incorrect requirements, prioritizing impacts on functionality, safety, reliability, and traceability.
  + Include actionable feedback in the form of recommendations to resolve identified issues.
  + Track requirement deficiencies using formal tools (e.g., problem tracking system or issue tracker) to ensure all issues are addressed and resolved before requirements baselining.

**Outputs:**

1. **List of Requirement Issues Identified:**

   * Items such as ambiguity, missing requirements, conflicts, orphaned requirements, unverifiable requirements, and circular traceability issues.
   * Include a classification (e.g., safety-critical, performance-impacting, usability-related) for prioritization.
2. **Problem Tracking System Records:**

   * All identified requirements issues should be logged and routinely updated in a system for traceability and resolution tracking Enginering activity but SA should ensure that this is done by the prject)
   * Include metrics (e.g., issue status: Open/Closed, resolution time, etc.) to monitor defect trends and accountability.
3. **Analysis of COTS, GOTS, MOTS, OSS, or Reused Software Requirements:**

   * A dedicated analysis addressing requirements for third-party and reused components, including compatibility, performance, and safety validation.
   * Highlight risks tied to licensing, modification needs (MOTS), or external dependencies.

---

## 7.3 Metrics for Software Assurance

Using metrics is essential for monitoring requirement quality throughout the project lifecycle and identifying trends or recurring issues. Below is an enhanced set of metrics tied to Requirement 7.2 to help quantify assurance activities and measure requirement health.

#### **Key Metrics:**

1. **Non-Conformances Identified by Lifecycle Phase Over Time:**

   * Count how many requirement issues or non-conformances are identified during critical phases (e.g., requirements development, design, testing) and track resolution rates.
   * **Purpose:** Isolate phases with high defect generation and implement process improvements.
2. **# of Software Requirements Categorized by Scope:**

   * Track requirements by category (e.g., system-level, subsystem-level, application-level) to ensure proper functional decomposition.
3. **# of Software Requirements Without Parent Traceability:**

   * Track orphaned requirements (those that do not trace back to higher-level requirements).
   * **Purpose:** Prevent requirement misalignment and ensure proper flow-down from top-level systems and overarching mission goals.
4. **Defect Trends in Traceability Quality:**

   * Count circular traces, orphaned requirements, or widowed requirements across the project lifecycle.
   * **Purpose:** Highlight traceability gaps or issues that could compromise validation.
5. **# of Detailed Software Requirements vs. Estimated Source Lines of Code (SLOC):**

   * Ratio of requirements to estimated code complexity.
   * **Purpose:** Detect over-specification (too many requirements per code block) or under-specification (too few requirements for software functionality).
6. **Defect Rates Over Time:**

   * Track incorrect, incomplete, or missing requirements (both identified and resolved).
   * Include issue resolution status for trend monitoring and accountability.
7. **Safety-Related Requirements Metrics:**

   * Count the number of safety-related requirement issues over time and track Open vs. Closed safety deficiencies.
   * **Purpose:** Ensure all safety-critical functionality is addressed and validated effectively.

---

## 7.4 Guidance

The Software Assurance (SA) guidance refines how SA can independently evaluate, track, and address deficiencies in software requirements to prevent costly downstream issues and ensure mission success. This enhanced version integrates best practices, actionable strategies, and highlights key areas for robust analysis, aligning with NASA requirements and industry standards.

**Deficient requirements are the largest single factor in software and computing system project failure, and deficient requirements have led to a number of software-related aerospace failures and accidents.**

Faults in requirements can originate from the adoption of requirements that are incomplete, unnecessary, contradictory, unclear, unverifiable, untraceable, incorrect, in conflict with system performance requirements, otherwise poorly written, or undocumented. It is important that operators properly identify and document safety requirements, and per industry standards, ensure that safety requirements are internally consistent and valid at the system level for the resulting computing system to work safely throughout its lifecycle.

#### **1. Impact of Deficient Requirements**

Deficient requirements are widely recognized as the leading cause of software project failures and delays. NASA Lessons Learned from software-related aerospace incidents confirm that:

* Faulty requirements (e.g., incomplete, ambiguous, unverifiable) can propagate errors into design, coding, integration, and operations, leading to downstream cost increases and even mission loss.
* Safety-related software deficiencies have contributed to critical aerospace failures, underscoring the need for robust requirement quality assurance.

#### **2. Techniques for Independent SA Analysis**

Ensure Software Assurance activities utilize industry best practices to analyze, review, and validate requirements rigorously:

* Refer to guidelines in *Topic 8.54,* **Software Requirements Analysis Techniques:**
  + Use checklists to verify clarity, correctness, completeness, consistency, feasibility, and traceability.
  + Challenge unverifiable or ambiguous requirements with test-based validation exercises.
  + Include safety engineers and subject matter experts (SMEs) to identify potential operational hazards tied to requirements.

#### **3. Address COTS/GOTS/MOTS/OSS Requirements**

Detailed software requirements must explicitly address third-party and reused software components to prevent integration and operational risks. SA should ensure such requirements include:

* Compatibility and performance metrics.
* Licensing, security, and dependency management issues.
* Safety validation aligned with NASA standards (e.g., NASA-STD-8719.13).

#### **4. Requirements Coverage in Logical Decomposition**

NASA missions use logical decomposition to define parent-child relationships between system requirements and software requirements. SA analysis should ensure all requirements flow down correctly, covering:

* **Functional and Performance Requirements:** Ensure requirements fully define software functionality and operational goals.
* **Hardware-Dependent Requirements:** Confirm proper software-hardware interaction and compatibility boundaries.
* **Interfaces Requirements:** Validate interfaces with external systems, services, and hardware components.
* **Quality and Reliability Requirements:** Ensure requirements address fault tolerance and system dependability.
* **Safety and Security Requirements:** Validate safety-critical scenarios and security provisions (e.g., data protection, unauthorized access prevention).
* **Human Interfaces/Data Definitions:** Confirm proper user interface definitions, data requirements, and accessibility.
* **Installation, Acceptance, User Operation, and Maintenance Requirements:** Verify requirements coverage for long-term usability and support.

---

### **5. Leverage SA Engagement Across the Lifecycle**

Software Assurance must continuously engage with requirements analysis throughout the lifecycle to validate and monitor evolving requirements and system dependencies. Steps include:

1. **Early Engagement in Requirement Development:** Facilitate joint reviews with requirements authors to detect and address deficiencies before baselining.
2. **Traceability Verification:** Continuously monitor the traceability between system-level and software-level requirements, ensuring changes are incorporated appropriately.
3. **Safety and Risk Analysis:** Prioritize safety impact reviews for software requirements, using techniques such as hazard analysis, fault trees, and FMECA (Failure Modes Effects and Criticality Analysis).
4. **Validation Through Metrics:** Use SA metrics to monitor trends, defect rates, and requirement quality, implementing corrective actions where needed.

---

### **Summary**

This updated SA guidance emphasizes the importance of identifying and addressing requirement deficiencies early. Independent Software Assurance analysis, combined with traceability verification, robust safety reviews, metrics monitoring, and logical decomposition, ensures detailed software requirements are correct, complete, and aligned with mission objectives. This systematic approach prevents costly downstream failures, ensures hardware/software compatibility, and enhances the overall safety, reliability, and success of NASA projects.

From [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), The results of the independent SA analysis performed on the detailed software requirements, including the list of requirements issues identified and records in a problem tracking system.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

When evaluating the software requirements, use the list of items in the [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist) [PAT-034](#tabs-5)

There are several **additional** checklists that aid in the analysis of software requirements. They look at the aspects various aspects described on **tab 3**. The **other** available requirements checklists are:

* [PAT-003 - Functional Requirements Checklist](/spaces/SITE/pages/112656804/PAT-003+-+Functional+Requirements+Checklist)
* [PAT-004 - Safety Requirements Analysis Checklist](/spaces/SITE/pages/112656824/PAT-004+-+Safety+Requirements+Analysis+Checklist)
* [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements)
* [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist)
* [PAT-079 - Requirements Quality Checklist](/spaces/SITE/pages/207290572/PAT-079+-+Requirements+Quality+Checklist)
* [PAT-080 - Requirements Contents Checklist](/spaces/SITE/pages/207290574/PAT-080+-+Requirements+Contents+Checklist)
* [PAT-081 - Requirements Editorial Checklist](/spaces/SITE/pages/207290577/PAT-081+-+Requirements+Editorial+Checklist)
* [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software)

Consider if the requirements being analyzed are SMART requirements “specific, measurable, attainable (achievable/actionable/appropriate), realistic, timebound (timely, traceable)”.

To confirm that the software requirements satisfy the conditions in SWE-051 make sure that the flowed down and derived requirements are from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design.

Software safety personnel need to be involved in the analysis of software requirements to determine their safety-criticality. Any software requirements that trace are determined to have safety implications. Those requirements with safety implications are tracked as "safety-critical."

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)       * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [PAT-003 - Functional Requirements Checklist](/spaces/SITE/pages/112656804/PAT-003+-+Functional+Requirements+Checklist) * [PAT-004 - Safety Requirements Analysis Checklist](/spaces/SITE/pages/112656824/PAT-004+-+Safety+Requirements+Analysis+Checklist) * [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements) * [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist) * [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist) * [PAT-042 - Requirements Development and Mgmt Audit](/spaces/SITE/pages/198770759/PAT-042+-+Requirements+Development+and+Mgmt+Audit) * [PAT-056 - Software Development Management Plan Assessment](/spaces/SITE/pages/198770884/PAT-056+-+Software+Development+Management+Plan+Assessment) * [PAT-059 - Software Requirements Specification Assessment](/spaces/SITE/pages/198770890/PAT-059+-+Software+Requirements+Specification+Assessment) * [PAT-079 - Requirements Quality Checklist](/spaces/SITE/pages/207290572/PAT-079+-+Requirements+Quality+Checklist) * [PAT-080 - Requirements Contents Checklist](/spaces/SITE/pages/207290574/PAT-080+-+Requirements+Contents+Checklist) * [PAT-081 - Requirements Editorial Checklist](/spaces/SITE/pages/207290577/PAT-081+-+Requirements+Editorial+Checklist) |

# 8. Objective Evidence

Objective evidence demonstrates compliance with the requirement by providing clear, verifiable, and traceable documentation that supports the Software Assurance (SA) activities performed during the analysis of detailed software requirements.

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

Below is a comprehensive list of objective evidence that satisfies this requirement:

---

### **1. Software Requirements Analysis Reports**

#### Evidence:

* **Software Requirements Analysis Results or Report**:

  + A detailed report summarizing the independent SA findings on the software requirements specification (SRS).
  + Report contents:
    - Identified issues, such as ambiguous, incomplete, or unverifiable requirements.
    - Gaps in bi-directional traceability (e.g., orphaned or widowed requirements).
    - Specific recommendations for resolving issues.
    - Verification of alignment between system-level and software-level requirements.

  **Example Evidence:**

  + *"SA Review of Software Requirements – Summary Document, Rev. 2.1: Includes 15 actionable findings related to clarity and traceability."*
* **Requirements Issues Log**:

  + A log of all issues identified in the requirements, categorized by type (e.g., ambiguity, missing safety-critical elements, traceability issues).
  + Includes statuses (open/closed), timestamps, owners, and resolution descriptions.

#### Tools/Artifacts:

* Requirements review reports.
* Marked-up software requirements specification (annotated requirements document).
* Meeting minutes documenting reviews with developers/project teams.

---

### **2. Problem Tracking System Records**

#### Evidence:

* **Problem/Defect Tracking Information Related to Requirements:**

  + Records of identified issues tracked in a designated tool (e.g., JIRA, Bugzilla, or NASA-specific systems).
  + Logs of requirement deficiencies showing status, priority, type, and resolution timeline.
  + Metrics showing open vs. resolved issues, aging reports, and breakdown by severity.

  **Example Evidence:**

  + *Tracking system export showing 12 open requirements-related issues (3 safety-critical, 2 ambiguous requirements) as of the most recent review cycle.*

---

### **3. Requirements Traceability Matrix (RTM)**

#### Evidence:

* **SA-Verified RTM Documentation:**

  + A completed traceability matrix showing bi-directional mapping of:
    - System-level to software-level requirements.
    - Software requirements to test cases.
    - Safety and security requirements to specific functional requirements.
  + Includes SA comments or observations where gaps exist (e.g., orphans, widows, or circular traces).

  **Example Evidence:**

  + RTM files (Excel sheets or tool-generated outputs) with comments from SA.
  + Screenshots of validated traces in requirements management tools (e.g., DOORS, Jama Connect).

---

### **4. Safety and Risk Analysis Review Documentation**

#### Evidence:

* **SA Verification of Safety-Related Requirements**:

  + An SA report or checklist explicitly addressing safety-critical requirements.
  + Coverage of hazard analysis or fault-tree requirements to ensure risk mitigation.
  + Records identifying missing or deficient safety requirements and recommendations for resolution.

  **Example Evidence:**

  + Signed-off hazard analysis checklist from SA showing coverage of safety-critical software functions.

#### Tools/Artifacts:

* Fault tree/hazard analysis with SA validations.
* Requirements gap analysis report for safety-critical elements.

---

### **5. COTS/GOTS/MOTS/OSS/Reuse Software Requirements Analysis**

#### Evidence:

* **Analysis of Third-Party or Reused Component Requirements:**

  + A documented review of requirements for external software (COTS, GOTS, MOTS, OSS) ensuring:
    - Functionality and integration requirements are explicitly defined.
    - Licenses, dependencies, and constraints are identified.
    - Safety and security risks of external software components are reviewed.

  **Example Evidence:**

  + *COTS Risk Assessment Report – Component XYZ: Identifies licensing restrictions and interoperability risks with hardware ABC.*
  + Spreadsheet of COTS requirements validation (e.g., format compatibility, scalability considerations).

---

### **6. Validation and Verification Checklists**

#### Evidence:

* **Completed SA Checklists for Software Requirements Elements:**

  + Checklists covering completeness, clarity, consistency, traceability, verifiability, and feasibility of requirements (e.g., following *NASA-STD-8739.8* or other SA-based guidelines).
  + Validation results ensuring that the requirements meet all specified criteria.

  **Example Evidence:**

  + Checklist results showing all requirements deemed testable and verifiable.

---

### **7. Metrics and Key Performance Indicators**

#### Evidence:

* **SA Activity Metrics:**  
  Metrics reporting the results of requirements analysis, including:

  + # of requirement defects (by phase, by type).
  + Trends in traceability gaps over time (orphaned, circular, missing traces).
  + Breakdown of safety/security-related requirement defects (open vs. closed).
  + Resolution rates of SA-identified issues categorized by criticality.

  **Example Evidence:**

  + *SA Metrics Report Q3 2023: 25 defects identified in requirements validation (15 safety-critical; 90% resolved within 2 months).*

#### Tools/Artifacts:

* Graphs, charts, or tables derived from tracking tools.
* Historical trends comparing requirement non-conformance.

---

### **8. Peer Review and Meeting Records**

#### Evidence:

* **Meeting Documentation for Joint SA Reviews:**

  + Minutes from requirements review meetings documenting SA input and resolution of concerns.
  + Evidence of stakeholder involvement in safety, reliability, and performance requirement reviews.

  **Example Evidence:**

  + Signed-off review notes showing resolution of a critical ambiguity in a mission-critical flight software requirement.
  + Action Item Tracker output showing status of SA-raised issues.

---

### **9. Compliance to Standards (Internal and Industry)**

#### Evidence:

* **SA Verification of Standards Compliance:**

  + Reports or checklists ensuring requirements align with NASA, industry-specific (e.g., DO-178C, ISO 29148), or project-specific standards.
  + Records of findings for non-compliance with associated corrective actions and closure statuses.

  **Example Evidence:**

  + *SA Compliance Checklist – NASA-STD-8739.8: Non-conformance report resolved for Section 5.2 of flight requirements.*

---

### **10. Independent Validation Review for High-Risk Projects**

#### Evidence:

* **Independent Review Records:**

  + Evidence of an external or third-party review of the SRS, particularly for high-risk projects.
  + Records of findings categorized as critical, major, or minor with associated recommendations.

  **Example Evidence:**

  + Reports from SMEs or third-party audits confirming software safety and security coverage.
  + Signed-off summary validating adherence to system-level functional requirements.

---

### **Key Takeaways**

Objective evidence ensures traceability, visibility, and accountability of SA activities during software requirements analysis. The artifacts listed above demonstrate SA’s role in delivering high-quality, complete, and verified requirements that align with system goals, meet NASA standards, and mitigate risks. Capturing detailed, quantifiable reports and tracking issue resolution lends confidence in the development process, preventing failures and ensuring mission success.
