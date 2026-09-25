# SWE-223 - Tailoring IV V project selections

> NASA Software Engineering Handbook (SWEHB Ver D), page id 105710152. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/105710152/SWE-223+-+Tailoring+IV+V+project+selections

SWE-223 - Tailoring IV&V project selections

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/105710152/SWE-223+-+Tailoring+IV+V+project+selections#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=105710152)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=105710152&showCommentArea=true&showComments=true#addcomment)

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

2.1.2.7 The NASA Chief, SMA shall make the final decision on all proposed tailoring of SWE-141, the Independent Verification and Validation (IV&V) requirement. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-223 History

SWE-223 - Used first in NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B | RESERVED |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | First use of this SWE in D  In previous versions this was a will statement |
| D | 2.1.2.7 The NASA Chief, SMA shall make the final decision on all proposed tailoring of SWE-141, the Independent Verification and Validation (IV&V) requirement. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

Independent validation and verification (IV&V) is a part of Software Assurance playing a role in the NASA software risk mitigation strategy. OSMA is responsible for determining which projects have IV&V for NASA in conjunction with the responsible Mission Directorate. The rationale for independent validation and verification (IV&V) on a project is to reduce the risk of failures due to software and provide assurance that the software will operate as intended, not operate unexpectedly and respond appropriately to adverse conditions. Performing IV&V on projects yields greater confidence that the delivered software products are error-free and meet the customer’s needs.  IV&V across the project life cycle increases the likelihood of uncovering high-risk errors early in the life cycle.

Independent Verification and Validation (IV&V) plays a pivotal role in ensuring the safety, reliability, and success of NASA software systems. [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation), which mandates IV&V, is particularly critical for software that is safety-critical, mission-critical, or involves significant technical complexity and risk. Allowing the NASA Chief, SMA to have the authority to approve or reject all proposed tailoring of this requirement ensures that such decisions are made with the highest level of accountability, oversight, and expertise.

## 2.1 Key Rationale for the Requirement

### 1. Safeguards Mission and Safety-Critical Software

The [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) (IV&V) requirement is designed to ensure the flawless operation of NASA’s most critical software systems by independently verifying their correctness and validating their performance. Tailoring IV&V requirements comes with inherent risks, especially for software impacting human spaceflight, mission safety, and significant investments.

* **Why This Requirement Matters**:  
  Empowering the NASA Chief, SMA, as the final authority ensures that any tailoring proposal for IV&V is thoroughly evaluated with mission safety and assurance as the primary focus. It prevents compromises on the rigor or scope of IV&V activities that could expose NASA software to undetected critical defects.

### 2. Centralized Oversight for Agency-Wide Consistency

Having the NASA Chief, SMA, as the final authority ensures that decisions regarding [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) tailoring are aligned with NASA's overarching safety and mission assurance goals. Decentralized or inconsistent tailoring approvals across different Centers or projects could lead to a lack of uniformity in the application of IV&V practices.

* **Why This Requirement Matters**:  
  A centralized decision-making authority maintains consistency across the Agency, ensuring that IV&V tailoring aligns with NASA's stringent standards and that exceptions are applied uniformly across projects with similar software classifications.

### 3. Prevents Under-Tailoring of Critical Risk Areas

Some projects may underestimate software risks or opt to reduce the scope of IV&V to save time, costs, or resources. This may lead to critical software risks being insufficiently addressed or overlooked.

* **Why This Requirement Matters**:  
  The NASA Chief, SMA, has the technical expertise and broad Agency perspective to weigh the justification for tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) against the potential risks. This requirement provides a safeguard against under-tailoring that could compromise software quality, reliability, or safety.

### 4. Ensures Alignment with Mission Assurance Processes

IV&V is a crucial aspect of NASA’s mission assurance framework. Tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) must be evaluated holistically within the context of the entire software assurance and systems engineering processes.

* **Why This Requirement Matters**:  
  The NASA Chief, SMA, ensures that proposed IV&V tailoring decisions do not conflict with broader mission assurance goals and are fully aligned with other standards (e.g., NASA-STD-8739.8 [278](#_tabs-<p></p>), NPR 7150.2 [083](#_tabs-<p></p>)). This integration reduces the likelihood of gaps in assurance processes.

### 5. Balances Risk and Resource Allocation

Different projects have varying levels of software criticality, risk profiles, and constraints on budget, schedule, or resources. Tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) allows flexibility for projects to allocate IV&V resources proportionately to the specific risks of their software. However, this flexibility must be applied judiciously to maintain the rigor required for high-risk projects.

* **Why This Requirement Matters**:  
  The ultimate authority of the NASA Chief, SMA, ensures that tailoring requests are balanced against the risk context of the software system, considering the implications of any reduction or adjustment in IV&V scope. Tailoring is scrutinized to ensure mission-critical software receives the necessary resources for robust assurance.

### 6. Incorporates Lessons Learned from Past Software Failures

NASA has experienced significant mission failures in the past due to undetected software issues that could have been caught through rigorous IV&V processes. For example:

* **Mars Climate Orbiter (1999)**: A software-related unit conversion error led to the failure of the mission.
* **Mars Polar Lander (1999)**: Software misinterpretations caused the early shutdown of descent engines.
* **Ariane 5 Flight 501 (1996)**: A software exception handling flaw resulted in a catastrophic failure.
* **Why This Requirement Matters**:  
  Lessons learned from such incidents demonstrate the importance of stringent IV&V. Centralized approval of tailoring ensures that historical lessons are considered when evaluating whether reducing the scope of IV&V is justifiable.

### 7. Preserves Independence of IV&V Activities

The independence of IV&V is fundamental to its role in identifying risks and verifying compliance. Tailoring IV&V requirements improperly may compromise its independence by reducing the scope or introducing conflicts of interest.

* **Why This Requirement Matters**:  
  The NASA Chief, SMA, ensures that IV&V retains its objectivity and independence, even when or if tailoring occurs. This guarantees that the integrity of the IV&V process is not compromised by project-specific pressures or constraints.

### 8. Promotes Accountability by Requiring High-Level Review

Tailoring any part of [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) is a high-stakes decision, as it involves determining whether to modify or reduce verification and validation processes for critical software. Such decisions must be subjected to the highest levels of accountability and oversight.

* **Why This Requirement Matters**:  
  Requiring final approval from the NASA Chief, SMA, ensures that tailoring decisions are scrutinized by a high-level authority who is removed from day-to-day project pressures. This high-level review adds an extra layer of accountability, promoting rigorous justification for all deviations from [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation).

### 9. Encourages Thorough Documentation and Justification

The process of obtaining approval for tailoring from the NASA Chief, SMA, ensures that projects must provide clear, documented reasoning for tailoring requests. This includes risk assessments, mitigation strategies, and evidence that the proposed tailoring will not compromise safety or mission goals.

* **Why This Requirement Matters**:  
  This requirement ensures tailoring decisions are not arbitrary but based on thorough analyses and well-documented justifications. This transparency strengthens confidence in the decision and ensures alignment with NASA's safety protocols.

### 10. Aligns with NASA’s Safety and Mission Assurance Culture

NASA’s emphasis on safety and mission assurance is a core value that underpins the Agency’s work. Rigorous IV&V and centralized decision-making on tailoring reflect this culture.

* **Why This Requirement Matters**:  
  By mandating that the NASA Chief, SMA, has final authority on tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation), NASA reinforces its commitment to prioritizing safety and mission assurance in all its processes, further strengthening the culture of excellence and risk mitigation.

## 2.2 Conclusion

Giving the NASA Chief, SMA, the authority to make final decisions on proposed tailoring of [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) safeguards the integrity and rigor of the IV&V process, ensuring that any adjustments are fully justified, transparent, and aligned with Agency-wide standards and safety goals. This centralized decision-making ensures consistency, mitigates risks, upholds independence, and incorporates lessons learned, ultimately helping NASA maintain its legacy of excellence and mission success.

# 3. Guidance

This improved guidance provides clarity and actionable steps for interpreting and implementing the requirements associated with tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation). Additionally, it reinforces the critical role of Independent Verification and Validation (IV&V) as part of NASA's software assurance processes and ensures proper accountability through leadership involvement.

## 3.1 Purpose of the Guidance

The goal of this guidance is to ensure:

1. IV&V remains integral to NASA's mission and software assurance processes by rigorously analyzing software artifacts to detect risks.
2. Tailoring decisions about [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) are justified, balanced, and aligned with NASA’s safety, reliability, and mission assurance standards.
3. A harmonious balance is achieved between flexibility for projects and NASA’s commitment to risk-based assurance and compliance.

## 3.2 IV&V Overview and Supporting Elements

IV&V is a fundamental software assurance discipline that provides independent assessments of both the processes and products of the software development lifecycle. It emphasizes early, continuous verification of risks and the independent validation of software performance per mission requirements. It ensures the software is built correctly (verification) and fulfills its intended purpose (validation) during nominal and off-nominal conditions.

Three parameters critical to the independence of IV&V—a key element of [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation)—are outlined below:

1. **Technical Independence**:

   * IV&V analysts are not involved in the development process, enabling them to objectively analyze software artifacts without biases.
   * This independence reduces the likelihood of subtle errors being overlooked, particularly by teams deeply focused on development.
2. **Managerial Independence**:

   * The IV&V provider reports to an organizational structure separate from the software development team.
   * Managerial independence ensures objectivity in determining what analysis needs to occur, when findings are provided, how they are communicated, and the methods used.
3. **Financial Independence**:

   * Funding for IV&V originates independently of the software project's budget, preventing undue financial pressure to reduce scope.
   * This independence empowers the IV&V team to focus exclusively on technical and assurance quality, as highlighted in the *IV&V Project Execution Plan (IPEP).*

For more information on the IPEP, see [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) and Topics [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) and [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan).

## 3.3 IV&V Guidance and Processes

### 3.3.1  IV&V Project Involvement

The IV&V activities begin early in the software development lifecycle (e.g., at concept phases) and provide continuous feedback throughout development, integration, and operational readiness. The intent is to reduce risk proactively by addressing software inconsistencies, defects, and risks when they are most cost-effective to resolve. Feedback focuses on:

* Correctness, safety, robustness, and security of the system/software.
* Addressing off-nominal conditions, such as handling faults and hazardous responses.

#### The IV&V Provider’s Key Activities include:

1. **Verification Tasks**:
   * Checking that software artifacts, such as requirements, design documents, implementation, and test cases, align with the original specifications.
   * Ensuring that each development phase satisfies entry/exit criteria for subsequent phases.
2. **Validation Tasks**:
   * Ensuring that developed software meets user expectations and intended mission behaviors.
   * Evaluating robustness and how well the software supports user and stakeholder needs in real-world conditions.

IV&V Provider requirements are documented in NASA-STD-8739.8 [278](#_tabs-<p></p>). Also see Topic [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance).

### 3.3.2  The Role of Objective Evidence

Objective evidence serves as the cornerstone of IV&V assessments, providing artifacts that enable the identification of inconsistencies, errors, and risks.

1. **Guiding Principles of Evidence Compilation**:
   * **Early and Continuous Assessment**: Generating objective evidence throughout the lifecycle prevents compounding risks in later stages.
   * **Risk-Based Prioritization**: IV&V resources are applied where they are most critical, balancing risk with resource constraints.
2. **Use of Evidence by IV&V Providers**:
   * Analyze evidence such as system requirements, concepts of operations, and mission-critical engineering artifacts.
   * Establish an independent baseline understanding that validates or challenges the software project’s artifacts and results.
3. **Documentation in IPEP**:
   * The *IV&V Project Execution Plan (IPEP)* captures the tailored IV&V approach, specifying how trade-offs in scope and resource use address risks while minimizing gaps in assurance.

### 3.3.3  Tailoring SWE-141: The Decision Process

NASA recognizes that projects may vary in size, criticality, classification, and risk profile. This entails tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) to focus IV&V where it delivers the most significant return on investment while addressing risk. The following steps establish how to tailor IV&V requirements:

1. **Tailoring Proposal:**
   * Projects seeking to modify [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) must document and justify the tailoring request.
   * The proposal must identify:
     + Software classification, associated risks, and mission criticality.
     + Trade-offs, including resource reductions and mitigations for uncovered areas.
     + Clear evidence of why tailoring will not compromise software performance, safety, or reliability.
2. **Adjudication by IV&V Advisory Board (IAB)**
   * The NASA IV&V Advisory Board reviews tailoring requests and provides recommendations to the NASA Chief, SMA.
   * The Board ensures the proposal aligns with technical, managerial, and financial independence and compliance with SMA goals.
3. **Final Authority of NASA Chief, SMA:**
   * The NASA Chief, SMA, holds ultimate authority to approve or deny tailoring requests based on the mission's risk profile, criticality, and compliance requirements.
   * This ensures centralized accountability and consistency in decision-making across all NASA projects.

## 3.4 Role of the NASA IV&V Facility

* **IV&V Sole-Source Provider**: NASA mandates that the **[Katherine Johnson IV&V Facility](https://www.nasa.gov/katherine-johnson-ivv-facility/)** serve as the sole provider of IV&V services to safeguard independence, consistency, and technical excellence when [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) requirements are applied.
* **Funding and Management**: IV&V is funded independently of the project to maintain its impartiality, focusing only on technical quality, safety, and mission risks.

## 3.5 Policy for Additional Involvement

1. The **Mission Directorate Associate Administrator** may extend IV&V support to additional projects that do not meet [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) criteria.
2. Projects in other developmental phases, de-risked software, or projects without a payload risk classification may be subject to required IV&V under the direction of the Associate Administrator or **NASA Chief, SMA**.

## 3.6 Annual Review and Budget Planning

* The scope of IV&V services is evaluated annually by the IV&V Advisory Board, ensuring that IV&V activities address project needs in alignment with NASA’s broader budgetary constraints.
* Input from this review informs updates to the scope of work for the NASA IV&V Facility.

## 3.7 Independent Review Goals

1. Align Resources to Risk: The IPEP ensures resources are distributed appropriately based on system safety, time sensitivity, software complexity, and mission-critical needs.
2. Promote Stakeholder Confidence: Tailored [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) decisions promote program transparency while balancing flexibility and assurance.

## 3.8 Conclusion

This guidance outlines the importance of preserving the integrity and independence of the IV&V process. It ensures tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) remains a rigorous, centralized decision that addresses unique project needs without compromising mission safety or accountability. Through continuous IV&V assessments and collaboration with technical stakeholders, NASA ensures its software meets the highest standards of quality, reliability, and mission assurance.

## 3.9 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation)        * [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

## 3.10 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small projects, by nature, often operate with limited budgets, resources, and personnel. However, even small projects can have significant impacts on mission success, especially when their software involves safety-critical or mission-critical operations. Tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) for small projects requires a thoughtful balance between reducing unnecessary IV&V burden while maintaining adequate software assurance for project risks. This guidance provides a streamlined approach to help small projects address this requirement effectively.

## 4.1 Guidance for Small Projects

### 4.1.1  Objective of the Requirement

The purpose of this requirement is to ensure that any tailoring of IV&V services via [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) prioritizes software assurance while balancing risks and resources. For small projects, tailoring decisions should:

1. Address the software’s risk classification and criticality.
2. Ensure sufficient validation of safety, reliability, security, and functionality.
3. Align with NASA’s software assurance processes and standards, even for resource-constrained projects.

### 4.1.2  Key Considerations for Small Projects

Small projects often support less complex missions or systems; however, their software may still possess characteristics requiring rigorous assurance. Tailoring of [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) for small projects should account for:

1. Software Classification: Is the software defined as Class D or E? These classifications often have fewer requirements than higher-class software but should still consider critical use cases and risks.
2. Mission Risk Profile: Does the software interact with safety-critical systems, mission-critical components, or external interfaces where failure could result in operational or reputational damage?
3. Resource Constraints: Does the project have limited personnel, funding, or tools available for implementing full IV&V?

### 4.1.3  Step-by-Step Guidance for Tailoring IV&V Requirements for Small Projects

#### 4.1.3.1. Assess Software Classification and Risks

Begin by evaluating your software’s classification and its associated risks using NASA’s classification guidelines (**NPR 7150.2** [083](#_tabs-<p></p>)). This classification will determine the baseline level of assurance needed for the software.

1. **Focus on Risk Assessment:** Clearly identify potential failure points, safety hazards, operational risks, and any interfaces that could affect higher-class systems or payloads.
2. **Prioritize Critical Areas:** If risks are minimal (e.g., non-safety-critical infrastructure software classified as Class F or H), the IV&V effort may benefit from tailoring to focus only on high-impact areas such as cybersecurity vulnerabilities or edge-case functional testing.

#### 4.1.3.2. Document Tailoring Justification

Tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) requires thorough documentation to justify the proposed changes to IV&V activities. This documentation will be reviewed by the Center SMA organization, the NASA IV&V Advisory Board, and ultimately the NASA Chief, SMA.

For Small Projects:

* **Simplified Justification**: Small projects can develop a concise justification focused on the following:
  + The software’s risk profile and classification.
  + Why tailoring (e.g., reducing IV&V scope) will not compromise safety or mission success.
  + Alternative measures (e.g., internal reviews, automated testing tools, additional oversight) that will mitigate risks associated with reduced IV&V.
* **Tailored Scope**: Provide details on what elements are excluded (if tailoring eliminates specific analyses) or prioritized (e.g., cybersecurity risks, testing reliability for specific components).

Use **NASA’s Software Risk Assessment** tools and templates to support this documentation.

#### 4.1.3.3. Collaborate with the Center SMA Organization

The Center SMA organization is responsible for reviewing tailoring proposals before they are delivered to the NASA IV&V Advisory Board (IAB). For small projects:

1. **Engage Early:** Work with the Center SMA team during early phases (e.g., planning or requirements) to identify opportunities for tailoring IV&V scope without compromising assurance.
2. **Leverage Expertise:** Where resources are limited, rely on the experience of the SMA organization to recommend alternative assurance processes.

#### 4.1.3.4. Submit to NASA IV&V Advisory Board

The NASA IV&V Advisory Board adjudicates tailoring requests before they are escalated to the NASA Chief, SMA. Small projects should:

1. Provide Clear Documentation: Ensure the Board can quickly understand the justification for tailoring and the mitigating factors for risks resulting from the reduced IV&V scope.
2. Request Risk-Based Feedback: Allow the Board to propose adjustments or augmentations to your tailoring plan based on their understanding of IV&V best practices.

#### 4.1.3.5. Final Approval by NASA Chief, SMA

Once adjudicated by the NASA IV&V Advisory Board, the tailoring request goes to the NASA Chief, SMA, for final approval. For small projects:

* Ensure your tailoring request emphasizes a balance between minimizing IV&V burden and maintaining mission safety, software reliability, and compliance with NASA standards.
* Highlight the cost-benefit trade-offs of your proposal, especially if retaining full IV&V scope would overwhelm project resources.

### 4.1.4  IV&V for Small Projects: Alternative Assurance Approaches

Small projects may tailor IV&V by leveraging alternative assurance practices to reduce the scope without compromising quality:

1. **Focused IV&V Scope:**
   * Limit IV&V to high-risk components, such as safety-critical functions, external interfaces, or cybersecurity vulnerability testing.
   * Exclude non-critical areas, where appropriate (e.g., supporting software that does not impact payload success).
2. **Automated Testing Tools:**
   * Use automated tools for functions like static code analysis and automated test case execution, which can reduce the manual burden for IV&V while maintaining rigorous testing.
3. **Internal Peer Reviews:**
   * Conduct formal, independent code reviews and software risk audits within the development team to achieve assurance goals.
4. **Alignment with Center SMA Oversight Activities:**
   * Work with your Center SMA organization to determine whether existing reviews, layers of oversight, or engineering safety boards can fulfill part of the IV&V role.

### 4.1.5  IV&V Project Execution Plan (IPEP)

For any IV&V involvement, even if tailored, the IV&V provider and small project team must document the approach in the *IPEP*:

1. Ensure risks and priorities are defined clearly, such as focusing IV&V resources on areas posing the greatest mission threat.
2. Create a roadmap for IV&V activities, including trade-offs made to align resources with the most critical software components.

For small projects, the IPEP provides transparency into how IV&V scope is tailored and demonstrates accountability to stakeholders during high-level reviews.

For more information on the IPEP, see [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) and Topics [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) and [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan).

## 4.2 Annual Review

Small projects should expect their IV&V scope to be reviewed annually by the IV&V Advisory Board. This ensures:

1. Prioritization of IV&V resources remains relevant to the project’s development phase.
2. Any changes to budgeting or available resources for IV&V are considered for future tailoring adjustments.

## 4.3 Example Tailoring Scenarios for Small Projects

Below are examples of how [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) can be tailored for small projects:

1. **Software with Minimal Risk (Class F):**
   * **Tailor IV&V Scope:** Exclude non-critical verification tasks, such as redundant requirements analysis, while retaining essential validation for edge cases.
   * **Alternative Assurance:** Perform internal reviews and use automated testing tools.
2. **Infrastructure Software Without Payload Risk:**
   * **Tailor IV&V Scope:** Focus exclusively on cybersecurity assessments and system interface testing.
   * **Alternative Assurance:** Collaborate with Center SMA teams to fulfill assurance gaps.
3. **Small Mission with Tight Budget:**
   * **Tailor IV&V Scope:** Concentrate efforts only on safety-critical areas (e.g., fail-safe mechanisms in automation software).
   * **Alternative Assurance:** Augment IV&V with documented peer reviews and smaller risk audits.

## 4.4 Conclusion

For small projects, tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) must balance reduced IV&V scope with appropriate assurance measures to ensure safety, reliability, and mission success. By following the outlined steps and engaging with the Center SMA organization, IV&V Advisory Board, and NASA Chief, SMA, small projects can implement a streamlined approach that maximizes resources while adhering to NASA’s safety and assurance standards.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-518)

  [Independent Verification and Validation of Embedded Software](https://llis.nasa.gov/lesson/723 "Click to open in new window")

  Public Lessons Learned Entry: 723.
* (SWEREF-584)

  [Does Software IV&V Provide Clear Benefits to NASA Projects?](https://llis.nasa.gov/lesson/6656 "Click to open in new window")

  Public Lessons Learned Entry: 6656.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following Lessons Learned from NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** emphasize the importance and benefits of Independent Verification and Validation (IV&V).

### 6.1.1  Existing Lessons Learned Related to IV&V:

#### 6.1.1.1. Independent Verification and Validation of Embedded Software  (Use of IV&V Procedures) [518](#_tabs-<p></p>)

* **Lesson Number: 723**
* **Key Takeaway:**  
  IV&V processes ensure software development aligns with specifications, performs correctly in the intended operational environment, and prevents unintended functions. Early identification and correction of errors in software development cycles can reduce costs significantly and improve software reliability and quality.
* **Relevance to SWE-141 Tailoring:**  
  Allowing undue tailoring of IV&V requirements risks missing errors early in development, which could have significant implications in later phases. This lesson demonstrates why the NASA Chief, SMA, as the final authority, must ensure tailoring decisions do not compromise these benefits.

#### 6.1.1.2. Does Software IV&V Provide Clear Benefits to NASA Projects? [584](#_tabs-<p></p>)

* **Lesson Number**: 6656
* **Key Takeaway:**  
  IV&V delivers concrete benefits beyond verification and validation performed solely by project personnel. Recent NASA projects have found that IV&V provides independent and objective insights, increasing the likelihood of identifying risks and ensuring compliance. Recommendations suggest enhancing IV&V programs to better support mission objectives.
* **Relevance to SWE-141 Tailoring:**  
  This lesson underscores that tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) to reduce IV&V scope should only be considered when alternative mitigations can provide comparable assurance. The unique, independent perspective of IV&V offers benefits that are difficult to replicate through internal processes alone.

### 6.1.2 Additional Applicable Lessons Learned

#### 6.1.2.1. Software Errors Contributing to Mars Polar Lander Loss

* **Lesson Number**: 1778
* **Key Takeaway:**  
  The Mars Polar Lander mission failed due to an improperly detected software error that shut off descent engines prematurely. This error went undetected because of inadequate testing and lack of early independent software assurance processes. Had IV&V been more rigorously applied, it might have identified this critical anomaly.
* **Relevance to SWE-141 Tailoring:**  
  This lesson emphasizes why independent oversight, such as IV&V, is crucial to catching subtle but catastrophic anomalies, particularly for safety-critical or mission-critical software. Tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) should never reduce IV&V just to save costs if software functions involve fault handling or operational-critical sequences.

#### 6.1.2.2. Insufficient Validation of Software Interfaces: Mars Climate Orbiter

* **Lesson Number**: 0938
* **Key Takeaway:**  
  The Mars Climate Orbiter mission failure (1999) was attributed to insufficient testing of software interfaces, particularly the miscommunication between metric and imperial units. The lack of IV&V involvement limited thorough interface validation, allowing the oversight to persist.
* **Relevance to SWE-141 Tailoring:**  
  When tailoring IV&V, projects must ensure complex interfaces and integration points are thoroughly validated by independent perspectives. The absence of independent assessment increases the probability of undetected errors in multi-system interactions, as occurred in this high-profile failure.

#### 6.1.2.3. Ariane 5 Flight 501 Software Failure

* **Lesson Number**: Non-NASA Lesson Learned but Widely Cited, LLIS Number Not Assigned
* **Key Takeaway:**  
  The Ariane 5 launch failure was caused by software handling an exception incorrectly, resulting in catastrophic mission loss. Insufficient independent testing and verification allowed the defect to persist in the final flight software.
* **Relevance to SWE-141 Tailoring:**  
  This example showcases the hazards of tailoring IV&V requirements without fully considering the criticality of error-prone components. Tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) must focus on sufficiently assessing high-risk areas, such as fault handling, error recovery, and exception management.

#### 6.1.2.4. Proper Software Assurance is Crucial for Radiation-Hardened Systems

* **Lesson Number**: 07216
* **Key Takeaway:**  
  In radiation-hardened systems, faulty assumptions about software reliability in harsh environments led to unexpected behaviors during nominal and off-nominal operations. IV&V's independent review of software behavior in high-stress conditions can identify unanticipated edge cases, which internal teams may overlook.
* **Relevance to SWE-141 Tailoring:**  
  Tailoring IV&V for small or specialized projects must still consider unusual operational conditions (e.g., space radiation) and ensure adequate verification of software's ability to handle these real-world environments. Reducing IV&V prematurely increases the risk of improperly addressing these critical factors.

#### 6.1.2.5. Realized Benefits of Sustained Early IV&V Involvement

* **Lesson Number**: 1329
* **Key Takeaway:**  
  Sustained involvement of IV&V starting early in the software life cycle provided significant cost benefits and reduced risks on several NASA projects, including those with limited resources. Early IV&V prevents "reinvention" or costly bug fixes later in development.
* **Relevance to SWE-141 Tailoring:**  
  Early engagement of IV&V should be prioritized. Tailoring should never result in deferring or skipping IV&V processes in early phases, as this negates one of IV&V's biggest cost-saving benefits: identifying risks before they propagate to later (and more expensive) development stages.

#### 6.1.2.6. Cybersecurity Assurance: Lessons Learned from NASA System Incidents

* **Lesson Number**: 22160
* **Key Takeaway:**  
  Several NASA ground systems and software have faced cybersecurity vulnerabilities due to the absence of rigorous validation processes. Inadequate testing for malicious code behavior, vulnerability assessment, and software updates created exploitable weaknesses.
* **Relevance to SWE-141 Tailoring:**  
  For software interfacing with mission-critical systems, tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) should explicitly retain cybersecurity-related IV&V analyses. The increasing importance of software security means that IV&V must evaluate risks from malicious behavior, integrity, and confidentiality of software.

#### 6.1.2.7. Tailored Software Assurance Requirements for Small Projects

* **Lesson Number**: 14758
* **Key Takeaway:**  
  Small projects have successfully tailored software assurance requirements and reduced the scope of work by focusing on high-priority risks and leveraging NASA IV&V Facility expertise. However, in some cases, tailoring too aggressively caused significant gaps in assurance, requiring costly post-delivery fixes.
* **Relevance to SWE-141 Tailoring:**  
  For small projects, tailoring can be beneficial but must be approached carefully to balance risk mitigation with resource constraints. Tailoring should focus on retaining IV&V for mission-critical components, safety-critical software, and high-risk interfaces.

### 6.1.3 Consolidated Lessons Learned: Recommendations for SWE-141 Tailoring

From these lessons, the following recommendations emerge:

1. **Focus on Risk-Driven IV&V:** Tailor IV&V requirements based on a software risk assessment, prioritizing mission-critical functions, safety-critical components, and areas with high complexity or dependencies.
2. **Retain Early and Continuous IV&V:** Avoid deferring or eliminating IV&V in the early software development phases, as early errors propagate and escalate costs in subsequent phases.
3. **Preserve Critical Analyses:** While tailoring may reduce IV&V's scope, it should not exclude cybersecurity evaluations, interface validation, or fault-handling assessments for safety-critical software.
4. **Leverage IV&V for Small Projects:** Consider scaling IV&V scope for small or non-critical projects but retain independent validation for high-priority areas. Introduce lightweight IV&V methods where appropriate.
5. **Document Tailoring Decisions:** Tailoring proposals must explicitly outline risks, corresponding mitigations, and impacts on assurance quality to ensure transparent decision-making.

### 6.1.4  Conclusion

IV&V has consistently proven invaluable in preventing mission-critical software failures and identifying defects overlooked during internal validation processes. It is essential that tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) requirements is done judiciously, always emphasizing mission success, safety, and assurance integrity. Lessons learned from past NASA projects reinforce the importance of maintaining independent oversight through IV&V processes, even when tailoring is applied.

## 6.2 Other Lessons Learned

* **Software IV&V**
  + IV&V approaches and resources must align with the program risk posture.
  + A closed-loop, auditable, corrective action toolset and process must be used to manage all IV&V identified issues and risks.

# 7. Software Assurance

**SWE-223 - Tailoring IV&V project selections**

2.1.2.7 The NASA Chief, SMA shall make the final decision on all proposed tailoring of SWE-141, the Independent Verification and Validation (IV&V) requirement.

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

The intent of this requirement is to ensure that any tailoring (modifications, waivers, or deviations) related to [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation)—the IV&V requirement—is reviewed, evaluated, and ultimately decided upon by the **NASA Chief, Safety and Mission Assurance (SMA)**. This decision ensures that critical risks and safety considerations for IV&V are adequately addressed and that tailoring decisions maintain consistency with NASA’s mission assurance objectives.

This guidance provides clear steps for Software Assurance (SA) personnel to support, prepare, and collaborate on proposed tailoring requests and their implementation.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Evaluate the Need for Tailoring (Proposed Modifications to SWE-141)

1. **Understand SWE-141 Requirements**:
   * Familiarize yourself with the full scope of [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation), including the criteria for IV&V applicability, how IV&V is applied for software classifications (e.g., Class A, B, C), and the activities required for compliance.
2. **Assess Justification for Tailoring**:
   * Review the details of the proposed tailoring request to ensure the rationale aligns with:
     + The **classification** of the software.
     + The **safety-criticality** of the system.
     + Mitigations for risks related to reduced IV&V scope, if applicable.
   * Ensure that the justification outlines the specific circumstances requiring tailoring, such as resource constraints, lower safety-criticality, or alternative assurance strategies.
3. **Engage Key Stakeholders**:
   * Collaborate with project teams, software engineers, and safety personnel to assess whether the proposed tailoring is justified and feasible.

#### 7.4.2.2  Prepare Tailoring Documentation

1. **Develop a Tailoring Request**:
   * For all tailoring requests, ensure the following documentation is prepared:
     + **Proposed Changes**: Clear description of the [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) activities to be tailored.
     + **Justification**: Comprehensive rationale for the proposed tailoring, addressing why standard IV&V practices cannot be fully applied.
     + **Risk Assessment**: Documentation of risks and potential impacts resulting from tailoring, including the mitigation plans for IV&V-related risks.
     + **Alternative Approach**: Any alternative strategies or assurance methods that will be adopted to compensate for reduced or modified IV&V efforts.
2. **Confirm Adequacy of Tailoring Information**:
   * Ensure that the tailoring request provides clear and complete information for the NASA Chief, SMA, to make an informed decision.

#### 7.4.2.3  Support Tailoring Review by the NASA Chief, SMA

1. **Facilitate the Review Process**:
   * Submit the documented tailoring proposal to the appropriate channels as required by NASA’s tailoring process.
   * Be available to provide explanations and clarifications during the review process led by the NASA Chief, SMA.
2. **Address Feedback and Questions**:
   * Respond to requests for additional information or analysis needed to support the tailoring decision.
   * Ensure risk assessments and mitigation plans are robust and meet the Chief, SMA’s expectations.

#### 7.4.2.4  Implement Tailoring Decision

1. **Monitor and Communicate Decision**:
   * Once the NASA Chief, SMA, makes the final decision, communicate the outcome to all relevant project teams.
     + If **approved**, ensure that updates are made to project assurance plans to reflect the tailored IV&V requirements.
     + If **denied**, work with project teams to comply fully with [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) or revise and resubmit the request if feasible.
2. **Document Tailoring Decision**:
   * Properly archive the tailoring decision and related documentation in project records for traceability.

#### 7.4.2.5  Follow Up on Tailored Projects

1. **Monitor Compliance with the Approved Tailoring Plan**:
   * If tailoring has been approved, ensure that the project follows the tailored approach and implements the outlined mitigation strategies.
   * Confirm that software assurance activities remain effective despite the reduced or modified IV&V scope.
2. **Evaluate the Impact of Tailoring on Risk**:
   * Continue assessing whether any risks emerge as a result of tailoring [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) and act to address new risks promptly.
3. **Report Back to SMA as Needed**:
   * Provide progress updates, compliance audits, or safety risk reports to the NASA Chief, SMA, especially for tailored projects involving safety-critical software.

### 7.4.3  Key Considerations for SWE-141 Tailoring Requests

1. **Safety-Critical Impacts**:
   * Tailoring should not compromise the identification and mitigation of software-related risks for safety-critical systems.
2. **Software Classification**:
   * IV&V is typically required for higher classification (e.g., Class A or safety-critical Class B) software. Tailoring must demonstrate why IV&V is not feasible or appropriate for the classification.
3. **Risk Mitigation**:
   * Proposed tailoring must provide alternative risk mitigation strategies if full IV&V is not applied.
4. **Project Scope and Mission Impact**:
   * Tailoring decisions should consider the scope, importance, and uniqueness of the mission. Modifications to IV&V should not introduce unacceptable risks to mission success.

### 7.4.4  Expected Outcomes

When following these steps, Software Assurance personnel will:

1. Support the NASA Chief, SMA in making informed decisions on [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) tailoring requests.
2. Ensure tailoring requests are well-documented, justified, and risk-aware.
3. Promote compliance with agency software assurance policies and safety-critical requirements.
4. Bolster the integrity of assurance activities even when tailoring is approved, ensuring risks remain mitigated and missions are safeguarded.

### 7.4.5  Conclusion

For tailoring requests of [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation), Software Assurance (SA) teams must provide clear documentation, robust risk assessments, and alternative assurance strategies to facilitate a final decision by the NASA Chief, SMA. Following the decision, SA personnel must ensure that tailored plans are fully implemented, risks are managed, and assurance objectives remain intact to safeguard mission success and software safety.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation)        * [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |
