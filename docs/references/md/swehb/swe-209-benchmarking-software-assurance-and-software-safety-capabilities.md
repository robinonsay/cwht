# SWE-209 - Benchmarking Software Assurance and Software Safety Capabilities

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695329. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695329/SWE-209+-+Benchmarking+Software+Assurance+and+Software+Safety+Capabilities

SWE-209 - Benchmarking Software Assurance and Software Safety Capabilities

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695329/SWE-209+-+Benchmarking+Software+Assurance+and+Software+Safety+Capabilities#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695329)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695329&showCommentArea=true&showComments=true#addcomment)

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

2.1.2.3 The NASA Chief, SMA shall periodically benchmark each Center’s software assurance and software safety capabilities against the NASA-STD-8739.8, NASA Software Assurance and Software Safety Standard.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-209 History

SWE-209 - Used first in NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B | RESERVED |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | First use of this SWE in D  In previous versions this was a will statement |
| D | 2.1.2.3 The NASA Chief, SMA shall periodically benchmark each Center’s software assurance and software safety capabilities against the NASA-STD-8739.8, NASA Software Assurance and Software Safety Standard. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The Headquarters Office of Safety and Mission Assurance (OSMA) is responsible for ensuring that the Agency-level software assurance and software safety requirements and policies are being followed throughout the Agency.

Software assurance (SA) and software safety (SS) are essential components of NASA's mission success. These disciplines ensure that software functions correctly, meets mission requirements, and operates reliably in high-risk environments. Benchmarking each NASA Center’s software assurance and safety capabilities against the **NASA-STD-8739.8 [278](#_tabs-<p></p>)** standard provides a structured approach to evaluating, improving, and maintaining consistent assurance practices across the agency. This requirement promotes alignment, safety, and accountability in engineering practices for software—a critical enabler of NASA's missions.

## 2.1 Key Rationale Behind This Requirement

### 1. Promotes Consistency Across NASA Centers

* **Explanation:** NASA is a geographically distributed organization with multiple Centers responsible for different projects and missions. Without periodic benchmarking, there is a risk of variations in how software assurance and safety practices are interpreted, implemented, and maintained.
* **Supporting Points:**
  + The **NASA-STD-8739.8** establishes a consistent, agency-wide framework for software assurance and safety, covering topics such as requirements, V&V (Verification and Validation), safety-critical assessments, and risk reporting.
  + Regular benchmarking ensures that all Centers adhere to the same high standards, creating uniformity that reduces the potential for gaps or inconsistencies in software assurance practices.
* **Why It Matters:** For multi-Center collaborations, consistent assurance practices are vital to ensure seamless integration of software products, preventing issues that may arise from differing assurance methodologies.

### 2. Identifies Gaps and Drives Continuous Improvement

* **Explanation:** Periodic benchmarking highlights areas where a Center’s software assurance and safety capabilities may not fully align with **NASA-STD-8739.8**, enabling improvement plans to address gaps.
* **Supporting Points:**
  + Benchmarking provides an objective means of evaluating current practices against an established baseline. This keeps Centers focused on continuous process improvement, identifying gaps that may have emerged due to evolving technologies or unique project requirements.
  + Centers may struggle to address software assurance challenges in areas such as cybersecurity, AI/ML (Artificial Intelligence/Machine Learning), and autonomous systems. Comparing their performance against the standard helps ensure these challenges are addressed proactively.
  + Reporting benchmarks periodically ensures that improvement actions are consistently reviewed and reassessed.
* **Why It Matters:** Benchmarking leads to tangible improvements by providing an unbiased and agency-wide mechanism for measuring quality and compliance, ensuring Centers constantly evolve to maintain high assurance quality.

### 3. Ensures Compliance with NASA’s Software Assurance and Software Safety Standards

* **Explanation:** Compliance with **NASA-STD-8739.8** is mandatory for all software assurance and software safety efforts. Benchmarking ensures Centers are systematically evaluated for compliance and accountability.
* **Supporting Points:**
  + Software issues have been a root cause of several NASA mission failures (e.g., Mars Climate Orbiter, Mars Polar Lander). Many of these could have been avoided through stricter adherence to software assurance and software safety standards.
  + Benchmarking functions as an accountability mechanism, ensuring that all Centers comply with the standard and implement the processes it prescribes.
* **Why It Matters:** Establishing and maintaining compliance is critical for reducing risks in software assurance and safety, particularly for high-stakes missions involving large investments or human exploration.

### 4. Enhances Mission Safety and Reduces Overall Risk

* **Explanation:** NASA missions often operate in environments with no room for failure, especially human-rated missions and high-value projects. Software errors—even minor ones—can have catastrophic consequences.
* **Supporting Points:**
  + Benchmarking ensures that software developed or assured by each Center is rigorously tested and thoroughly analyzed to detect potential failures. This improves the reliability of safety-critical systems and mitigates risks to astronauts, equipment, and mission success.
  + By measuring adherence to software safety principles outlined in **NASA-STD-8739.8**, Centers can collectively reduce the likelihood of critical failures. For safety-critical software, this includes hazard analysis, fault prevention, and ensuring system redundancy for potential failures.
* **Why It Matters:** By periodically benchmarking, the Chief, SMA ensures that Centers prioritize software safety measures, ultimately safeguarding NASA’s missions and lives.

### 5. Fosters a Culture of Accountability and Excellence

* **Explanation:** Benchmarking encourages Centers to maintain high levels of accountability in their software assurance and safety practices. It opens the door for shared learning and collaboration when deficiencies are identified.
* **Supporting Points:**
  + Benchmarking motivates Centers to meet—or exceed—the requirements outlined in **NASA-STD-8739.8**, promoting a culture of technical discipline and pride in achieving compliance.
  + Results of benchmarking allow the Chief, SMA to identify Centers that excel in software assurance and safety, using them as examples of best practices or mentors for other Centers.
  + This accountability ensures systemic weaknesses or patterns of non-compliance do not persist due to oversight or resource constraints.
* **Why It Matters:** A culture of accountability and technical excellence ensures software assurance is treated as a strategic priority at every Center, rather than just a project requirement.

### 6. Supports Knowledge Sharing and Best Practices

* **Explanation:** Benchmarking efforts inevitably uncover insights into effective software assurance practices. These insights can be shared across Centers to strengthen the agency’s overall software capabilities.
* **Supporting Points:**
  + Centers that demonstrate exceptional practices can serve as examples to others. Periodic benchmarking facilitates knowledge-sharing opportunities among Centers, which helps standardize expertise.
  + Best practices in benchmarking may apply equally to agency-critical systems and smaller Class D or CubeSat projects, bridging gaps between complex and simpler missions.
  + Shared knowledge ensures that innovations or advancements at one Center benefit all Centers, improving software assurance and safety capabilities collectively.
* **Why It Matters:** Benchmarking strengthens collaboration across the agency, allowing NASA Centers to learn from each other’s successes and challenges.

### 7. Responds to Evolving Software Challenges

* **Explanation:** The increasing complexity of NASA’s software systems presents new challenges, such as artificial intelligence, autonomous vehicles, and cybersecurity. Benchmarking allows Centers to assess their readiness for these challenges.
* **Supporting Points:**
  + A key function of benchmarking is detecting how well Centers adapt to new and emerging standards. As software technologies evolve, the **NASA-STD-8739.8** standard evolves, and Centers must demonstrate capability in handling new complexities.
  + Topics like cybersecurity assurance and AI/ML validation are particularly important areas requiring clear assessment frameworks. Regular benchmarking ensures Centers scale their capabilities accordingly.
* **Why It Matters:** NASA remains proactive in preparing Centers for new technologies and challenges. By benchmarking capabilities periodically, the Chief, SMA ensures that software processes remain robust, even as novel systems are adopted.

### 8. Reduces Long-Term Costs of Software and Risk Management

* **Explanation:** Identifying weak assurance and safety practices early prevents costly rework, delays, or failures later in the software lifecycle.
* **Supporting Points:**
  + Benchmarking helps detect inefficiencies in assurance practices, preventing defects from propagating to later lifecycle phases where correction costs are higher.
  + For long-term or high-budget programs, periodic benchmarking ensures that Centers maintain high standards throughout the lifecycle, minimizing unexpected risks or delays that could result from lapses in compliance.
* **Why It Matters:** Ensuring adherence to software assurance standards reduces unforeseen costs and budget overruns, keeping projects on track and within resource limitations.

### 9. Aligns with NASA’s Strategic Objectives

* **Explanation:** The agency’s **Strategic Plan** emphasizes fostering technical excellence and employing consistent best practices across Centers. Benchmarking supports these objectives by promoting uniformity and effective process oversight.
* **Supporting Points:**
  + The **2018 NASA Strategic Plan [117](#_tabs-<p></p>)** highlights the importance of maintaining capabilities to meet evolving technical challenges. Benchmarking drives Centers to innovate while maintaining compliance with well-defined standards.
  + Aligning Center practices with **NASA-STD-8739.8** ensures the agency achieves its strategic goals, such as improving risk management and ensuring technical integrity.
* **Why It Matters:** Consistent benchmarking ensures that NASA’s software assurance and safety processes remain aligned with broader strategic goals, leading to mission success across the agency.

## 4.2 Conclusion

The requirement for the NASA Chief, SMA, to periodically benchmark each Center’s software assurance and software safety capabilities ensures agency-wide compliance, promotes continuous improvement, and fosters a culture of accountability and excellence. Comparing practices against the **NASA-STD-8739.8** standard drives alignment, improves collaboration, and enables Centers to prepare for the challenges of modern software complexity. With benchmarking, NASA ensures that software assurance and safety practices remain robust, consistent, and effective, reducing risks for high-value and safety-critical missions, and sustaining NASA’s position as a leader in space exploration.

# 3. Guidance

This guidance describes how the **Headquarters Office of Safety and Mission Assurance (OSMA)** assesses compliance with agency software assurance and safety requirements, evaluates the effectiveness of Center-level capabilities, and ensures consistency and continuous improvement across NASA through audits, reviews, and benchmarking activities.

## 3.1 NASA Organizational Agency Assessment Responsibilities

The overarching responsibility to guide, oversee, assess, and improve NASA’s safety, reliability, and software assurance requirements is divided across several organizational directives. Key documents and responsibilities include:

**NPD 1000.3E [066](#_tabs-<p></p>), Section 4.13: Role of the Office of Safety and Mission Assurance (OSMA)**

* + OSMA provides policy direction, functional oversight, and assessments to verify compliance with all safety, reliability, maintainability, and quality engineering and assurance requirements.
  + OSMA advises the NASA Administrator and senior officials on all matters involving safety and mission success.
  + For software assurance and software safety, OSMA ensures that Agency-wide standards, policies, and practices are aligned to guarantee mission success and reduce risks.

**NPD 1000.3E, Section 5.15: Role of the NASA Safety Center (NSC)**

* + The NSC manages the audit, review, and assessment process for evaluating adherence to Agency Safety and Mission Assurance (SMA) policies and requirements, including compliance with NASA software policies.
  + The NSC collaborates with OSMA to ensure findings and recommendations from audits and reviews are effectively addressed.

**NPD 8700.1E [036](#_tabs-<p></p>): NASA Policy for Safety and Mission Success**

* + The document requires verification and validation (V&V) of the life cycle implementation of SMA processes and safety requirements through continued surveillance of programs, projects, and contractor processes.
  + As part of OSMA’s responsibilities, surveillance involves reviewing all stages of the software life cycle to ensure adherence to safety-critical software assurance requirements.

**NPR 8705.6D [353](#_tabs-<p></p>): SMA Audits, Reviews, and Assessments (Role of the NSC AIO)**

* + The **NASA Safety Center Audit and Inspection Office (NSC AIO)** conducts audits, reviews, and assessments to verify that NASA programs and projects comply with applicable SMA requirements, including software assurance and software safety standards.
  + The NSC audits ensure compliance with **NPR 7150.2D: NASA Software Engineering Requirements** [083](#_tabs-<p></p>), and **NASA-STD-8739.8B: NASA Software Assurance and Software Safety Standard** [278](#_tabs-<p></p>)**.**

### 3.2 Periodic Assessments Performed by OSMA

The OSMA meets its assessment responsibilities through a combination of oversight mechanisms. These mechanisms ensure NASA Centers, programs, and projects are consistently designing, testing, and managing safety-critical software according to NASA standards. The following activities exemplify OSMA’s commitment to compliance and process improvement:

**Key Assessment Activities:**

* **NASA Quality Audit, Assessment, and Review (QAAR):**
  + Conduct compliance audits at the Center, program, and project levels to evaluate adherence to safety and mission assurance policies, including requirements in **NPR 7150.2D** and **NASA-STD-8739.8B**.
  + Ensure Centers are meeting their responsibilities under NASA software assurance and safety programs.
* **Capability Maturity Model Integration (CMMI®) Appraisals:**
  + OSMA reviews CMMI benchmarking results for software engineering process maturity at Centers.
  + Periodic appraisals assess maturity improvements and alignment with **NPR 7150.2** requirements for software development and assurance.
* **Program and Project Reviews:**
  + Participate in program/project milestone reviews to evaluate compliance and ensure proactive identification of assurance concerns in safety-critical and mission-critical systems.
* **Planning Document Reviews:**
  + Assess Center and project planning documents, schedules, and progress reports to ensure consistency with software assurance requirements.
* **Waiver Reviews:**
  + Evaluate waiver requests submitted by Centers and projects to ensure deviations from software requirements and standards are justified and appropriately mitigated.
* **Feedback During Working Groups:**
  + Collect status updates from the **NASA Software Assurance Working Group (SAWG)** to monitor Center-specific software activities and issues.
  + Use these forums to gather Center feedback, which may inform future revisions to Agency standards and requirements.
* **External Agency Inquiries and Internal Software Inventory Tracking:**
  + Respond to software audits or inquiries conducted by external agencies while maintaining an updated inventory of software in compliance with assurance standards to address Agency-level risks effectively.

## 3.3 OSMA’s Broader Responsibility in Ensuring Accountability

**Conducting Center and Organizational Surveys:**

* **Goal of Surveys:**
  + OSMA ensures oversight by conducting surveys across NASA Centers and headquarters organizations. The surveys include assessments of operations, compliance with Agency policy, and process maturity. These surveys provide:
    - A **compliance review** of Center processes and infrastructure with OSMA requirements.
    - A review of program/project files to identify systemic deficiencies or areas of best practice.

**Survey Objectives:**

1. **Identify Systemic Issues:** Highlight repeatable patterns of deficiency, promote better understanding of challenges, and develop solutions.
2. **Recognize Excellence:** Identify Centers or projects demonstrating exemplary assurance practices and use them as role models across NASA.
3. **Center Feedback Mechanism:** Gather feedback from Centers to identify gaps in current Agency policies, enabling improvements in requirements and standards like NPR 7150.2D and NASA-STD-8739.8B, respectively.

### 3.4 Key Focus of Periodic Audits by OSMA

The OSMA ensures that audits cover the broad scope of software engineering, assurance, and safety compliance. The following focus areas are prioritized:

**Scope of Software Assurance and Safety Audits:**

1. **Compliance Assessment:**
   * Review Center compliance with **NASA-STD-8739.8B** and **NPR 7150.2D** requirements.
2. **Risk-Based Approach:**
   * Identify software implementation risks and safety-critical gaps.
   * Assess tailored requirements and their rationale for any deviations.
3. **Specific Focus Areas:**
   * Safety-critical software designation processes.
   * Software requirements mapping matrices and documentation completeness.
   * Review of hazard reports, cybersecurity plans, and software testing approaches.
   * Integration of Independent Verification and Validation (IV&V) processes.
   * Coding standards usage, quality assessments, and hazard identification workflows.
   * Open-source and reused software policies.
   * Software risks and hazard management processes.

### 3.5 Benchmarking with Capability Maturity Model Integration (CMMI-DEV)

* **CMMI Benchmarking:**  
  NASA’s use of **CMMI® for Development (CMMI-DEV)** provides an objective, industry-standard methodology for evaluating the software engineering maturity of its Centers.
  + **Purpose of CMMI-DEV Appraisals:**
    - Measure a Center’s compliance with **NPR 7150.2D** process-related requirements.
    - Benchmark the maturity of internal and external software development organizations against widely recognized best practices.
    - Identify areas requiring process improvements to meet mission-critical deadlines, costs, and reliability goals.
* **Role of CMMI in NASA’s Software Processes:**
  + The CMMI model helps NASA assess potential risks in software development, understand progress made toward process maturity, and enable consistent development of reliable software for Class A and Class B projects. (See [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) for CMMI level requirements.)

## 3.5 Conclusion

Periodic benchmarking of NASA Centers’ software assurance and safety capabilities is integral to maintaining compliance with **NASA-STD-8739.8B** and achieving mission success. By combining standardized audits (QAAR), maturity appraisals (CMMI), and extensive Center feedback, OSMA ensures the consistent application of best practices across the Agency. These assessments further drive continuous improvement, identify systemic risks, and safeguard mission safety for NASA's most critical programs.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-098 - Agency Process Asset Library](/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

For many small projects, including CubeSats, prototypes, technology demonstrators, or low-criticality scientific tools, the process for benchmarking against **NASA-STD-8739.8** [278](#_tabs-<p></p>) can be tailored to ensure compliance without imposing an excessive administrative or technical burden. While the size and scope of small projects differ from large-scale missions, their implementation of safety-critical practices and adherence to software assurance standards are equally important to mission success. Small project guidance provides streamlined approaches for managing compliance, risk mitigation, and resource allocation.

## 4.1 Guidance for Small Projects

### 4.1.1  Key Tailoring Principles for Small Projects

1. **Risk-Based Tailoring:**
   * Focus on identifying and addressing software assurance priorities based on the project's classification and risk posture (e.g., Class C, D, E, or F software).
   * Emphasize safety-critical components and align software practices with mission objectives.
2. **Simplified Compliance Measures:**
   * Leverage lightweight tools, templates, processes, and checklists from NASA's Software Assurance and Software Safety Initiative.
   * Adopt assurance activities that are scaled to the project's resource constraints without compromising quality and reliability.
3. **Focus on Core Requirements:**
   * Implement essential verification and validation (V&V) processes highlighted in **NASA-STD-8739.8** rather than attempting full-scale benchmarking of all practices when not required.

### 4.1.2  Tailored Guidance for Small Projects

#### 4.1.2.1  Scope of Benchmarking Activities

Small projects should focus their benchmarking efforts on areas that align with their classification, scope, and importance to the mission. The following recommendations aim to limit unnecessary overhead while ensuring valuable assessments are conducted.

1. **Safety-Critical Software:**
   * Prioritize benchmarking of safety-critical software assurance practices (e.g., testing for failure modes, hazard analysis, safety-critical design validation).
   * If the software is not classified as safety-critical, focus on verifying adherence to basic assurance practices such as functional correctness, cybersecurity, and operational reliability.
2. **Lifecycle Processes:**
   * Evaluate simplified assurance processes across the lifecycle:
   * Requirements validation.
   * Unit testing and functional testing.
   * Verification of interfaces and dependencies (hardware/software).
3. **Requirements Compliance:**
   * Benchmark compliance against a relevant set of **NASA-STD-8739.8** requirements tailored to small software projects. Use NASA's **Software Requirements Mapping Matrix** (see Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)) for determining scaled-down responsibilities.
4. **Documentation:**
   * Utilize lightweight documentation templates (Software Assurance Plans and Safety Analysis Checklists). This ensures that documentation fulfills compliance needs without excessive complexity.

#### 4.1.2.2  Simplified Tools and Processes

Small projects can leverage NASA-provided tools and processes to efficiently implement software assurance practices while meeting benchmarking expectations.

1. **Templates:**
   * Use pre-defined, lightweight templates for Software Assurance Plans (SAP) and hazard analysis from the **NASA Process Asset Library (PAL)** (See [SWE-098 - Agency Process Asset Library](/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library)).
   * Review tailored requirements against **NPR 7150.2D [083](#_tabs-<p></p>)** and **NASA-STD-8739.8** matrices for minimal documentation workload.
2. **Automated Tools:**
   * Limit labor-intensive aspects of assurance by using automated software tools recommended by the **NASA Software Assurance Initiative** (see [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative)), such as:
     + **Static Analysis Tools**: Tools like SonarQube, Coverity, or Cppcheck for code quality and standards compliance.
     + **Testing Frameworks**: Use lightweight testing tools like PyTest (Python), JUnit (Java), or simple integration test utilities.
     + **Cybersecurity Scanners**: Basic automated security tools to detect vulnerabilities.
3. **Shared Resource Access:**
   * Leverage shared NASA software repositories, test cases, and pre-approved coding standards to reduce redundant development.

#### 4.1.2.3  Focused Audit Scope

While large projects undergo extensive audits, small projects can streamline their audits by focusing on high-risk areas and a narrower scope aligned with their classification.

1. **Risk-Centric Areas of Focus:**
   * **Safety:** Ensure baseline compliance with safety-critical requirements for hardware/software interactions, actuator controls, and data validation.
   * **Software Interfaces:** Evaluate the validation of any key software interfaces (with hardware, APIs, or external systems).
   * **Cybersecurity:** Conduct lightweight verification of cybersecurity controls to ensure compliance with cybersecurity assurance requirements.
2. **Audit Preparation:**
   * Prepare simple documentation summarizing tailored requirements, testing methods, and assurance approaches.
   * Consolidate results from automated tools to demonstrate compliance without requiring highly detailed manual tracing.

#### 4.1.2.4  Activities for Feedback and Continuous Improvement

Benchmarking small projects provides critical insights that drive improvement while maintaining simplicity in execution.

1. **Lightweight Surveys:**
   * Participate in OSMA surveys and feedback forums by providing concise updates about assurance processes tailored to the project.
2. **Center-Level Reporting:**
   * Submit summaries of how the project aligns with **NASA-STD-8739.8** and details of any tailored requirements or outstanding risks.
   * Provide feedback on challenges unique to small projects, which helps Centers refine tailored guidance over time.
3. **Learn from the NASA Software Assurance Working Group (SAWG):**
   * Engage with SAWG activities to leverage best practices shared across other small projects. Collaborative sessions may highlight reusable tools or insights specific to minimizing weaknesses in assurance practices.

#### 4.1.2.5  Utilize Existing CMMI Integration at the Center Level

Small projects may not need standalone Capability Maturity Model Integration (CMMI®) appraisals. Instead, they should benefit from the Center-level processes already implemented for larger projects.

1. **Efficient Appraisal Participation:**
   * Use the results of Center-level CMMI appraisals to align small project practices indirectly without duplicating benchmarking efforts.
   * Focus on applying recommendations learned from appraisals when key processes directly impact small project assurance needs.
2. **Adopt Best Practices:**
   * Small projects can adopt simplified versions of processes recommended by Center-level appraisals where relevant, ensuring scalable compliance.

### 4.1.3  Recommended Focus Areas for Small Project Benchmarking

When benchmarking small projects against **NASA-STD-8739.8**, the following key focus areas should drive streamlined compliance and risk mitigation:

1. **Requirements:**
   * Validate tailored requirements and safety-critical software categorization early.
   * Align scaled requirements mapping matrices with project scope.
2. **Testing and Validation:**
   * Conduct unit, integration, and safety-critical testing using automated tools.
   * Focus validation efforts on critical functions and dependencies.
3. **Resources and Planning:**
   * Ensure clear allocation of assurance roles and responsibilities, even if combined with other engineering roles.
   * Utilize lightweight software assurance plans optimized for the project’s scale.
4. **Risk Monitoring:**
   * Periodically assess risks, known issues, and hazard analyses related to software, particularly during critical milestones.
5. **Cybersecurity:**
   * Incorporate basic cybersecurity analysis to detect vulnerabilities that could compromise mission safety (aligned with **NPR 7150.2** cybersecurity requirements).
6. **IV&V Support:**
   * Engage with Independent Verification and Validation (IV&V) support appropriately for tailored assurance purposes. Utilize IV&V resources for key validations where independent scrutiny is most beneficial.

### 4.1.4  Benefits of This Guidance for Small Projects

1. **Efficiency:** Reduces excessive overhead while retaining compliance with critical assurance and software safety standards.
2. **Alignment:** Ensures small projects follow a tailored approach that aligns with agency-wide benchmarking requirements.
3. **Risk Reduction:** Focused assurance processes optimize failure prevention for safety-critical and mission-essential systems.
4. **Consistency:** Scaled-down benchmarking ensures uniform standards application across small and large projects.
5. **Continuous Improvement:** Small projects participate in ongoing benchmarking feedback loops, benefiting from lessons learned and best practices across the agency.

## 4.2 Conclusion

Small projects may be resource-constrained, but by tailoring their benchmarking procedures, they achieve compliance with **NASA-STD-8739.8** and contribute to NASA’s overall mission safety and success. By leveraging automated tools, simplified documentation, and risk-based auditing practices, small projects deliver reliable software while remaining aligned with Agency policy.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-036)

  [NASA Policy for Safety and Mission Success,](http://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=8700&s=1E "Click to open in new window")

  NPD 8700.1E, NASA Office of Safety and Mission Assurance, 2008. Effective Date: October 28, 2008, Expiration Date: April 28, 2020
* (SWEREF-066)

  [The NASA Organization w/Change 85](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=3E "Click to open in new window")

  NPD 1000.3E, Associate Administrator, April 15, 2015, Expiration Date: April 15, 2026
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-117)

  [2018 NASA Strategic Plan,](https://nodis3.gsfc.nasa.gov/npg_img/N_PD_1001_000C_/N_PD_1001_000C__main.pdf "Click to open in new window")

  NPD 1001.0C, NASA Office of Office of the Chief Financial Officer, 2018.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-294)

  [OSMA/NSC's SMA Technical Excellence Program (STEP) program.](https://nsc.nasa.gov/professional-development/safety-and-mission-assurance-technical-excellence-program "Click to open in new window")

  The Safety and Mission Assurance (SMA) Technical Excellence Program (STEP) is a career-oriented, professional development roadmap for SMA professionals.
* (SWEREF-353)

  [Safety and Mission Assurance (SMA) Audits, Reviews, and Assessments](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=6D "Click to open in new window")

  NPR 8705.6D, Effective Date: March 29, 2019, Expiration Date: March 29, 2024
* (SWEREF-521)

  [Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999)](https://llis.nasa.gov/lesson/740 "Click to open in new window")

  Public Lessons Learned Entry: 740.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA's **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** catalogs past experiences and incidents that emphasize the importance of comprehensive software assurance activities and organizational benchmarking. The following lessons learned provide critical insights and rationale for periodic benchmarking of software assurance and safety practices across NASA Centers, helping to prevent systemic issues, improve compliance, and align processes with **NASA-STD-8739.8** [278](#_tabs-<p></p>).

#### 1. The Importance of Tracking Mission Assurance Across Multiple Projects

* **Case:** Deficiencies in Software Oversight on the Mars Climate Orbiter [521](#_tabs-<p></p>)
* **Lesson Number:** LLIS-0740
* **Incident Summary:**  
  The Mars Climate Orbiter (MCO) failed in 1999 due to a critical software error involving mismatched units between English (pounds-force seconds) and metric (Newton-seconds). The root cause stems from insufficient oversight of software assurance processes, including failures in ensuring interfaces adhered to requirements and that teams properly verified unit consistency. The Software Management and Development Plan (SMDP) was also not followed consistently across the organization. Walkthroughs of requirements lacked proper stakeholder attendance, documentation, and resolution tracking.
* **Lesson Learned:**
  + Uniform implementation of software assurance standards is essential to ensure consistent oversight and compliance.
  + Programs must follow agency-wide software assurance documentation, standards, and requirements with periodic evaluations for gaps.
* **Relevance to the Requirement:**  
  This case highlights the need for periodic benchmarking of software assurance practices to identify and correct systemic issues, improve consistency across Centers, and monitor adherence to NASA-STD-8739.8. Benchmarking ensures all projects—large and small—maintain appropriate assurance rigor.

#### 2. Software Testing Lessons from the Mars Polar Lander

* **Case:** Mars Polar Lander Mission Loss (1998) [529](#_tabs-<p></p>)
* **Lesson Number:** LLIS-0938
* **Incident Summary:**  
  The Mars Polar Lander (MPL) mission failed because the flight software incorrectly interpreted transient signals as valid touchdown events, shutting down the descent engines prematurely. These transient signals were a known hardware characteristic, but this behavior was not properly accounted for in the software design, requirements, or testing. Software testing overlooked key operational conditions, and changes made after test failures were not retested sufficiently.
* **Lesson Learned:**
  + Systemic benchmarking of how Centers integrate hardware/software characteristics into assurance and testing could have revealed these deficiencies.
  + Benchmarking should emphasize requirements validation, risk-based testing, and the consistent application of standards across lifecycle checkpoints.
* **Relevance to the Requirement:**  
  Regular benchmarking ensures hardware/software integration practices align with NASA-STD-8739.8 and helps identify gaps in requirements validation, testing, and retesting processes to prevent critical mission failures.

#### 3. The Importance of Monitoring and Maintaining Process Consistency

* **Case:** Space Shuttle Software Process Improvements
* **Lesson Number:** LLIS-1862
* **Incident Summary:**  
  Early in the Space Shuttle program, it was realized that inconsistent software development and assurance processes across contractors created risks to mission success. The initial lack of standardization led to inefficiencies, undetected errors, and significant rework needs. Introducing methods to benchmark and align software engineering and assurance practices across contractors greatly improved the program’s success rate and reduced risks for subsequent missions.
* **Lesson Learned:**
  + Continuous process monitoring and benchmarking against established software assurance standards (like **NASA-STD-8739.8**) are critical for improving software safety and reliability.
  + Regular benchmarking helps ensure consistency, identify areas for improvement, and prevent process drift over time.
* **Relevance to the Requirement:**  
  Benchmarking NASA Centers ensures engineering and assurance practices are consistent across the agency. It helps monitor software safety maturity and ensures compliance with current standards.

#### 4. Risks of Overlooking Tailored Software Assurance Requirements

* **Case:** Lessons from Small-Scale Projects (CubeSats)
* **Lesson Number:** LLIS-2257
* **Incident Summary:**  
  Many resource-constrained small projects, such as CubeSats, tailor software assurance requirements too aggressively, creating gaps in assurance coverage. One CubeSat mission failed due to insufficient V&V practices, lack of complete hazard analysis, and the absence of rigorous software safety assessments. These failures were attributed to a lack of centralized oversight and inconsistent benchmarking for software assurance practices between smaller and major missions.
* **Lesson Learned:**
  + All projects must adhere to a baseline of software assurance practices, even when requirements are tailored.
  + Periodic benchmarking ensures that tailored assurance procedures for small projects remain compliant with **NASA-STD-8739.8** while accounting for unique project constraints.
* **Relevance to the Requirement:**  
  Benchmarking helps small and large projects alike align with the NASA Software Assurance and Software Safety Standard. It opens opportunities to track how effectively Centers are managing tailored requirements, ensuring quality even among smaller missions.

#### 5. Fostering Continuous Improvement Through Assurance Assessments

* **Case:** IV&V Lessons from the James Webb Space Telescope (JWST)
* **Lesson Number:** LLIS-2504
* **Incident Summary:**  
  During the development of the James Webb Space Telescope (JWST), strong collaboration between the Independent Verification and Validation (IV&V) program and project assurance teams helped identify critical software defects earlier in the lifecycle. IV&V assessments also highlighted necessary improvements in assurance practices at the Center level, ultimately feeding into the agency’s process improvement initiatives. Benchmarking these practices across multiple programs significantly enhanced software safety maturity.
* **Lesson Learned:**
  + Regular and rigorous assessments of software assurance processes provide feedback for both the current program and the agency as a whole.
  + Systematically benchmarking IV&V-interfaced software safety outcomes ensures that Centers adopt the most effective assurance practices.
* **Relevance to the Requirement:**  
  This case demonstrates the value of benchmarking software assurance practices and outcomes at the Center level. It emphasizes the connection between rigorous assessments and process improvement.

#### 6. Misalignment of Cybersecurity and Assurance

* **Case:** Ground Systems Security Challenges
* **Lesson Number:** LLIS-2705
* **Incident Summary:**  
  Software deployed for ground systems operations faced cybersecurity vulnerabilities that were not adequately accounted for in the software assurance process. The vulnerabilities stemmed from a failure to implement security requirements mandated by standards and policies. Benchmarking studies later revealed that the Center had not aligned its assurance practices fully with agency-level cybersecurity assurance standards.
* **Lesson Learned:**
  + Consistent benchmarking is necessary to detect and address misalignment in evolving areas like cybersecurity.
  + Benchmarking encourages proactive updates to assurance practices to meet modern challenges.
* **Relevance to the Requirement:**  
  Regular benchmarking efforts must include cybersecurity assurance evaluations to ensure Centers are meeting safety-critical requirements in today’s IP-connected environments.

#### 7. Systemic Software Risks in Distributed Development Environments

* **Case:** Hubble Space Telescope Software Development Oversight
* **Lesson Number:** LLIS-0919
* **Incident Summary:**  
  During the Hubble Space Telescope development, software was built in a distributed development environment with multiple contractors and NASA teams. Weaknesses in assurance practices—caused by an absence of consistent oversight and benchmarking—led to integration challenges. These issues delayed software delivery and caused significant cost overruns. Eventually, standardized benchmarks for software assurance helped mitigate risks during later phases of the project.
* **Lesson Learned:**
  + Benchmarking software assurance processes improves consistency in development environments with distributed teams and multiple vendors.
  + Early and regular software assurance benchmarking can prevent integration risks and improve reliability.
* **Relevance to the Requirement:**  
  This underscores the importance of benchmarking efforts that account for varied software development environments within Centers and across distributed teams.

### 6.1.2  Conclusion

The lessons above demonstrate the value of periodic benchmarking to assess and improve software assurance and safety practices across NASA Centers. By learning from the mistakes of past missions, NASA can ensure that compliance with **NASA-STD-8739.8** is stringently implemented, fostering consistency and improving the overall reliability and safety of software across all missions. These lessons reinforce the need for a proactive and unified approach to benchmarking, which helps mitigate risks, address systemic gaps, and drive process improvements agency-wide.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-004 - OCE Benchmarking**

2.1.1.2 The NASA OCE shall periodically benchmark each Center's software engineering capability against requirements in this directive.

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

The goal of this benchmarking requirement is to evaluate and compare each NASA Center’s software assurance (SA) and software safety (SS) capabilities to ensure compliance with **NASA-STD-8739.8** [278](#_tabs-<p></p>). This benchmarking effort helps identify strengths, weaknesses, and areas for improvement, fostering consistency and excellence in software assurance and safety practices across the Agency.

This guidance provides clear and actionable steps for Software Assurance personnel in supporting and participating in benchmarks.

### 7.4.2  Software Assurance Responsibilities

1. **Prepare for Benchmarking Activities**
   * **Review Applicable Criteria**:

     + Familiarize yourself with the content of **NASA-STD-8739.8**, ensuring that all requirements specific to software assurance and software safety are well understood.
     + Pay special attention to key areas that will be evaluated, such as planning, risk management, verification and validation (V&V), hazard analysis, metrics collection, and anomaly tracking.
   * **Organize Relevant Artifacts**:

     + Collect and prepare documentation that demonstrates your Center’s compliance with **NASA-STD-8739.8**. Examples of key artifacts include:
       - Software Assurance Plans and Software Safety Plans.
       - Risk analyses and mitigation strategies.
       - Test results, including safety assurance and V&V reports.
       - Metrics related to defect density, test coverage, and closure rates for safety-critical anomalies.
       - Audits, assessments, and previous benchmark reports.
   * **Engage Key Personnel**:

     + Identify and involve relevant software assurance and software safety personnel at your Center who can best represent current capabilities, address questions, and contribute to the benchmarking process.
2. **Actively Participate in Benchmarking Reviews**
   * **Provide Inputs and Evidence**:

     + During benchmarking sessions, ensure your Center provides clear evidence of how it implements software assurance and safety practices per **NASA-STD-8739.8**.
     + Highlight strengths, ongoing improvements, and innovative practices tailored to your Center’s unique projects or challenges.
   * **Collaborate Effectively**:

     + Work closely with the NASA SMA team leading the benchmark to ensure accurate representation of your Center’s processes. If gaps or uncertainties arise, seek clarification and document any findings for corrective action.
   * **Facilitate Demonstrations or Interviews**:

     + Be ready to provide demonstrations of processes or decision-making workflows (e.g., how your Center handles tailoring, performs safety-critical risk analysis, or verifies compliance for complex projects).
     + Participate actively in interviews to explain assurance and safety activities at a level of detail that ensures compliance is demonstrated clearly.
3. **Contribute to Gap Analysis**
   * **Assist in Identifying Gaps**:

     + If the benchmarking review identifies shortfalls in compliance with **NASA-STD-8739.8**, help identify the root cause. This may involve reviewing tailored processes, resource gaps, or specific misunderstandings of standard requirements.
   * **Evaluate Risks of Non-Compliance**:

     + Assess the implications of any identified gaps for software assurance and safety, including potential impacts on project success, risks to safety-critical systems, or deviations from best practices.
   * **Propose Corrective Actions**:

     + Collaborate with Center leadership and the benchmarking team to develop corrective actions for addressing non-compliance. This might include:
       - Updating or amending processes or plans.
       - Providing additional training for personnel.
       - Implementing new tools or metrics to track assurance and safety activities.
4. **Follow Through on Benchmarking Results**
   * **Implement Corrective Actions**:

     + Ensure any corrective actions assigned to your Center as a result of the benchmarking effort are followed through. Document progress and completion to demonstrate improvement.
   * **Monitor Progress**:

     + Establish mechanisms to track how well your Center addresses issues identified in the benchmarking report. Use regular internal reviews to verify progress.
   * **Communicate Improvements**:

     + Share details about corrective actions, process changes, or improvements to software assurance and safety practices with the SMA organization during follow-ups or for subsequent benchmarks.
5. **Support Cross-Center Collaboration and Knowledge Sharing**
   * **Learn from Other Centers**:

     + Leverage the benchmarking effort to compare your Center’s performance with others, identifying best practices that could be adopted to strengthen your Center’s capabilities.
   * **Share Lessons Learned**:

     + If your Center has well-established processes or innovative solutions for software assurance or safety, share these practices as part of the benchmarking effort so other Centers can benefit.
   * **Standardize Practices Where Possible**:

     + Support the adoption of consistent, NASA-wide software assurance and safety practices, especially for compliance with high-impact requirements.

### 7.4.3  Key Areas to Evaluate Against NASA-STD-8739.8

Ensure that benchmarking assessments account for the following core areas of software assurance and safety:

1. **Planning**:
   * Development of Software Assurance and Software Safety Plans in compliance with **NASA-STD-8739.8** and tailoring requirements as appropriate.
2. **Risk Management**:
   * Processes for identifying, tracking, and mitigating software risks, particularly for safety-critical software.
3. **Verification and Validation (V&V)**:
   * Execution of independent verification and validation processes to ensure correctness, completeness, and safety of software products.
4. **Requirements Compliance**:
   * Implementation and traceability of software assurance and safety requirements across the software lifecycle.
5. **Safety Analysis**:
   * Execution of hazard analyses, software fault analyses, and integration of these activities into the project lifecycle.
6. **Testing and Anomaly Resolution**:
   * Processes for systematic testing of software, adequate test coverage, and resolution tracking for any identified anomalies.
7. **Tailoring Justification**:
   * Adequacy of tailoring justifications for software assurance and safety requirements.
8. **Metrics and Continuous Improvement**:
   * Collection, analysis, and use of metrics to monitor the effectiveness of assurance and safety processes and drive continuous improvement.

### 7.4.4  Implementing Continuous Improvement

* **Regular Internal Assessments**:
  + Don’t wait for periodic benchmarks led by SMA—initiate internal audits and self-assessments, using **NASA-STD-8739.8** as guidance.
  + Track compliance and improvement at both the Project and Center levels.
* **Closing Recurring Compliance Gaps**:
  + Identify recurring or systemic compliance gaps during benchmarks and work with the SMA organization to implement Agency-level adjustments that resolve these issues effectively and prevent reoccurrence.
* **Increase Workforce Proficiency**:
  + Ensure your Center’s assurance and safety workforce is well-trained on **NASA-STD-8739.8**. Provide training on newly identified gaps or updates to standards.
  + Consider planning the team's professional development journey through the **SMA Technical Excellence Program (STEP) [294](#_tabs-<p></p>)** at Levels 2, 3, and 4.

### 7.4.5  Expected Outcomes of Benchmarking

By actively supporting benchmarking efforts:

1. **Improved Compliance**:
   * Each Center strengthens its alignment with **NASA-STD-8739.8**, improving mission and safety outcomes.
2. **Agency-Wide Consistency**:
   * Benchmarks drive consistency across all NASA Centers by identifying gaps and promoting knowledge sharing.
3. **Enhanced Software Safety**:
   * Strengthened software safety practices reduce risks for all safety-critical and mission-critical software systems.
4. **Continuous Process Improvement**:
   * Benchmarks foster a culture of self-assessment and continuous improvement in software assurance.

### 7.4.6  Conclusion

Software Assurance personnel play a critical role in benchmarking activities by preparing evidence, participating in reviews, and ensuring corrective actions are implemented. By aligning with **NASA-STD-8739.8**, each Center can demonstrate the maturity of its software assurance and safety processes while driving continual improvements. These efforts ultimately promote consistent compliance, enhanced safety, and mission success across NASA programs.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-098 - Agency Process Asset Library](/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) |
