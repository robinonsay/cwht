# SWE-159 - Verify and Validate Risk Mitigations

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695515. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations

SWE-159 - Verify and Validate Risk Mitigations

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695515)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695515&showCommentArea=true&showComments=true#addcomment)

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

3.11.5 The project manager shall test the software and record test results for the required software cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis.

## 1.1 Notes

Include assessments for security vulnerabilities during Peer Review/Inspections of software requirements and design. Utilize automated security static analysis as well as coding standard static analyses of software code to find potential security vulnerabilities.

## 1.2 History

Click here to view the history of this requirement: SWE-159 History

SWE-159 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 3.16.7 The project manager shall verify and validate the required software security risk mitigations to ensure that security objectives identified in the Project Protection Plan for space flight software are satisfied in their implementation. |
| Difference between B and C | Changed "verify and validate" to "test";  Added requirement to record the test results;  Changed focus of requirement from "security risk mitigations to ensure that security objectives identified in the Project Protection Plan for space flight software are satisfied in their implementation" to "cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis.". |
| C | 3.11.7 The project manager shall test the software and record test results for the required software cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis. |
| Difference between C and D | No change |
| D | 3.11.5 The project manager shall test the software and record test results for the required software cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis. |

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

Mitigations identified to address security risks need to be confirmed as appropriate and adequate.  Software verification and validation (V&V) processes are used to determine whether the software security risk mitigations, as planned and implemented, satisfy their intended use to address security risks in space flight software.  The results of V&V activities serve as a documented assurance that the correct mitigations were identified, implemented, and will reduce to an acceptable level or eliminate known software security risks.

The requirement for thorough software testing and documentation of results for cybersecurity mitigation implementations is essential to ensure the overall safety, security, and success of NASA missions. Below is the rationale for this requirement, highlighting its significance in addressing security vulnerabilities, mitigating risks, and ensuring compliance with NASA standards and best practices.

---

#### **1. Verification of Cybersecurity Mitigations**

Software systems for NASA projects operate in high-risk environments, often involving critical communication pathways and interfaces with both hardware and external systems. Conducting rigorous testing and recording the results ensures that:

* Cybersecurity mitigations identified through security vulnerability and weakness analyses are **fully implemented and effective**.
* Potential introductions of new vulnerabilities during implementation are identified and addressed.
* Mitigation implementations actively counter the specific vulnerabilities and weaknesses they were designed to address.

Without testing, there is no way to confirm that identified cybersecurity risks are adequately mitigated, leaving the project susceptible to potential exploits.

---

#### **2. Assurance of Software Resilience**

Modern mission software systems are increasingly sophisticated and interconnected, making them attractive targets for unauthorized access, malware, or other cybersecurity threats. Testing mitigations offers a proactive means of ensuring that NASA's software:

* Is **resilient to attacks** and can continue functioning securely even under adverse conditions.
* Appropriately responds to malformed inputs, unauthorized access attempts, or attacks designed to exploit system weaknesses.
* Exhibits robust behavior, minimizing the likelihood of mission disruptions, data loss, or system compromises.

This resilience is critical for missions supporting national security, public safety, or significant scientific advancements.

---

#### **3. Compliance with NASA and Federal Requirements**

NASA must meet federal cybersecurity requirements (e.g., NIST guidelines such as the NIST Cybersecurity Framework (CSF) and NIST SP 800-53 for system protections). These frameworks emphasize the need for testing and validation of implemented cybersecurity controls. By requiring projects to test and document mitigation implementations:

* NASA demonstrates adherence to federal cybersecurity standards and regulations.
* The agency ensures that vulnerabilities and weaknesses are addressed in a traceable and auditable manner.
* This reinforces NASA's commitment to maintaining leadership in secure software development practices.

An untested cybersecurity mitigation could indicate non-compliance with these standards, potentially exposing the project, mission, or agency to additional risks, scrutiny, and liability.

---

#### **4. Early Detection of Residual and Emerging Risks**

Testing cybersecurity mitigations allows project teams to:

* Detect and address **residual risks** that persist even after mitigations are implemented.
* Identify any **new risks** or vulnerabilities that emerge as a result of changes or updates during the development cycle.
* Perform iterative testing that reinforces security at every major development stage, ensuring that issues are not discovered too late in the delivery process when mitigation costs are higher.

The requirement to test and record results provides data critical for understanding the evolving risk posture of the project, especially in dynamic mission environments.

---

#### **5. Prevention of Mission Failures and Security Breaches**

Historically, unmitigated or improperly mitigated cybersecurity vulnerabilities in software systems have contributed to significant mission failures, security breaches, and budget overruns. Real-world examples demonstrate the catastrophic impacts of compromised system security:

* Loss of commanding authority: Unauthorized access could lead to malicious command injections, disrupting operational control of spacecraft or systems.
* Loss of sensitive data: Weaknesses in software systems could expose high-value scientific data, intellectual property, or personally identifiable information (PII).
* System downtime: Security weaknesses exploited during operations could result in system failures or an inability to support time-critical missions.

By rigorously testing and documenting mitigation strategies, NASA minimizes the likelihood of these failures, ensuring mission continuity, data protection, and public trust.

---

#### **6. Establishing a Record of Due Diligence**

Documenting test results is a critical aspect of demonstrating due diligence in protecting NASA systems against cybersecurity risks. This requirement ensures that:

* Comprehensive records are maintained of the steps taken to address vulnerabilities and weaknesses.
* Evidence is available in cases where audits, investigations, or post-mission assessments are necessary.
* Projects contribute to the accumulation of institutional knowledge, enabling better practices for future missions.

Without test result documentation, mitigation efforts cannot be validated or verified, making it difficult to review, reproduce, or improve upon previous testing efforts.

---

#### **7. Facilitating Stakeholder Confidence**

Testing and recording results provide transparent, concrete proof that cybersecurity mitigations are effective. This fosters confidence among:

* **NASA leadership** that mission systems are secure and risks are mitigated.
* **External stakeholders** (e.g., international partners, federal agencies) that NASA missions meet rigorous security protocols.
* **Project team members** by promoting accountability and improving project understanding of security requirements.

Confidence in system security is critical to mission success, especially in projects with international or interdisciplinary cooperation.

---

#### **8. Supporting Continuous Improvement**

Testing mitigations and analyzing results contribute to:

* Identifying best practices for cybersecurity implementation.
* Improving the effectiveness of future security efforts by learning from each project's challenges and successes.
* Building a culture of security awareness and fostering continuous improvement across the agency.

Without rigorous testing, it is impossible to refine current practices or prevent recurring problems.

---

### **Summary of Key Benefits**

The mandatory testing and documentation of software cybersecurity mitigation implementations ensures that:

1. Cybersecurity protections are verified as effective.
2. Software systems are resilient to threats and unauthorized access.
3. NASA remains in compliance with federal regulations and internal standards.
4. Emerging risks are identified and addressed early in development.
5. Mission failures due to cybersecurity issues are avoided.
6. A comprehensive, auditable record of security efforts is maintained.
7. Stakeholder confidence in NASA’s technology and practices is bolstered.
8. Continuous improvement in software security is supported agency-wide.

In essence, this requirement reflects NASA's commitment to building and safeguarding software systems that meet the highest standards of security, reliability, and mission assurance. By fulfilling this requirement, project managers securely position their systems to succeed in highly demanding and potentially vulnerable mission environments.

# 3. Guidance

#### **Overview**

Verification and Validation (V&V) activities for software security risk mitigations are vital to ensuring that the identified vulnerabilities and weaknesses are addressed effectively and consistently throughout the software development lifecycle. The improved guidance enhances clarity, strengthens the V&V planning process, and provides actionable steps for project managers to ensure comprehensive testing and validation.

---

## 3.1 Planning V&V for Software Security Risk Mitigations

Project managers must ensure that software security risk mitigations identified in **SWE-154 (Identify Security Risks)** and **SWE-156 (Evaluate Systems for Security Risks)** are tested and validated as part of the project’s planned V&V activities. The **Verification and Validation Plan** must include explicit steps for verifying that security risk mitigations are implemented properly, remain effective, and align with evolving security needs. This plan should evolve across the project lifecycle and include all identified security vulnerabilities and risk mitigations.

Key considerations in planning include leveraging **security analysis artifacts** and integrating **Input from the Information System Security Officer (ISSO)** for targeted and effective V&V activities.

#### **Source Documents to Aid V&V Planning**

When planning V&V for security risk mitigations, the following documents are critical:

1. **System-Level Risk Assessment Report**:

   * Helps identify areas where software interfaces or components are vulnerable to unauthorized access, data interception, or malware.
   * Provides detailed categorization of risks (e.g., high, medium, low) to prioritize mitigation focus.
2. **Plan of Actions and Milestones (POA&M)**:

   * Document outlining actions to resolve, track, and report security weaknesses.
   * Includes timelines for vulnerability remediation based on NASA’s defined standards:
     + **High severity** vulnerabilities must be mitigated within five working days.
     + **Moderate severity** vulnerabilities must be addressed within thirty working days.
     + **Low severity** vulnerabilities must be resolved within sixty working days.
   * Helps V&V teams align test priorities with required mitigation timelines.

#### **Examples of Relevant Information From Source Documents**

* **Specific Vulnerabilities**: Discovered during security impact analysis or monitoring, including system vulnerabilities tied to software components (e.g., exposed APIs, weak encryption schemes, hardcoded credentials).
* **Mitigation Efforts**: Documented corrective efforts targeting security weaknesses in software.
* **System Configuration Goals**: Shared goals for securing software interactions and interfaces (e.g., the use of secure communication protocols, hardened boundary protections).

#### **Key Planning Actions**

* Integrate findings from the risk assessment and POA&M into V&V review checklists, test plans, and software requirements traceability matrices to ensure every identified risk is tracked throughout the lifecycle.
* Identify mission priorities and critical systems through discussions with the owner of the **Project Protection Plan (PPP)**, noting that the PPP may contain Controlled Unclassified Information (CUI). While direct access may be limited, derived requirements and security needs can still inform V&V planning.
* Plan mitigation verification activities as early as possible to minimize cost and risk propagation while remaining flexible to identify and validate new vulnerabilities at each stage of development.

---

## 3.2 V&V Activities

Verification and Validation activities, at a minimum, must cover confirmed testing and validation of software security risk mitigations throughout the lifecycle. Effective V&V approaches include both automated tools and manual techniques. Below is a detailed improvement to existing guidance.

#### **V&V Activities Specific to Software Security Risk Mitigations**

1. **Security Vulnerability Checks During Peer Reviews/Inspections**:

   * Update peer review checklists to include specific cybersecurity checks for:
     + Requirements (e.g., completeness, correctness, inclusion of security measures).
     + Design (e.g., implementation of security controls, boundary protections, encryption standards).
     + Code (e.g., detection of backdoors, static analysis to confirm adherence to secure coding standards).
     + Test procedures (e.g., testing access controls, input sanitization routines, exception handling).
   * Leverage **SWE-087** and **SWE-088** Peer Reviews and Checklists guidance to refine peer review processes for security.
2. **Automated Security Analysis Tools**:

   * Use **static code analysis tools** to detect vulnerabilities at code implementation. This includes:
     + Scanning for insecure coding practices (e.g., hardcoded credentials, buffer overflows, unclosed ports).
     + Checking conformance with coding standards (e.g., MISRA, CERT Secure Coding).
   * Analyze third-party libraries and dependencies for known vulnerabilities.
   * Employ tools for **dynamic analysis** to evaluate runtime security functionality (e.g., penetration testing, fuzz testing).
3. **Repeat Vulnerability Assessments**:

   * Re-assess the software for previously identified vulnerabilities to ensure they have been addressed and verify that new vulnerabilities have not been introduced.
   * Confirm that implemented mitigations are effective through iterative testing, such as **regression testing** based on **SWE-191 guidance**.
   * Emphasize testing in areas that repeatedly demonstrate risk sensitivity or criticality to overall mission objectives.
4. **Manual Security Checks and Techniques**:

   * For specialized software or coding languages lacking automated tooling (e.g., PLDs, FPGA code), conduct manual checks for:
     + Backdoors, hardcoded credentials, or insecure programming practices.
     + Risks in third-party components and libraries (e.g., outdated security patches, supply chain concerns).
     + Compliance with infrastructure security measures (e.g., malware scans, access restrictions).

#### **Examples of Specific Tests and Validation Activities**:

* **Unit Tests**: Validate inputs and outputs, ensuring sanitization of inputs (e.g., rejecting invalid commands).
* **Access Control Tests**: Verify only valid, authorized accounts and interfaces gain access to the software.
* **Boundary Testing**: Test port-blocking, disabled interfaces, and secure communication paths.
* **Fuzz Testing**: Verify secure handling of unexpected or malformed inputs.
* **Stress Testing**: Confirm that security protocols hold under high workloads and adverse conditions.

#### **Focus on Most Critical Systems**

V&V efforts should prioritize **critical systems** that:

* Are directly exposed to external systems/interfaces (e.g., uplinks, command interfaces).
* Are essential to mission success.
* Have been flagged as the most vulnerable based on the system-level risk assessment or PPP.

---

## 3.3 Integration With Project Protection Plans (PPP)

The **Project Protection Plan (PPP)** includes:

* Sensitive information or classified appendices related to the mission’s security posture.
* Software-related security requirements derived from the PPP.

#### **Guidance for V&V Coordination**:

* Consult PPP owners to confirm areas of software that require additional verification efforts.
* Derive specific software security requirements where direct PPP details cannot be shared due to sensitivity.
* Integrate these derived requirements into checklists, test plans, and validation reports to ensure V&V comprehensively addresses mission security objectives.

---

### **Key Recommendations for Effective V&V Planning**

1. **Early Mitigation and Verification**:
   * Implement and verify mitigations as early in the lifecycle as possible to minimize costs and avoid compounding vulnerabilities.
2. **Iterative Testing**:
   * Conduct repeated assessments of mitigations to ensure evolving threats in the project environment are addressed and previous vulnerabilities do not re-emerge.
3. **Document Everything**:
   * Maintain detailed records of all V&V activities, including peer reviews, static analysis, assessment results, and manual evaluations.

---

By systematically incorporating validation, security checks, and iterative assessments throughout the software lifecycle, V&V planning ensures NASA projects meet the highest standards for cybersecurity, mitigate risks effectively, and align with mission-critical objectives.

See also [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks), [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks), [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access), [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing).

For Additional Guidance on Peer Reviews see [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

See also [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis), [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification), [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices), Topic [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software)

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)        * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

Small projects face unique challenges due to limited resources, budget constraints, and personnel availability. Despite these limitations, implementing effective security mitigations is critical to protecting NASA's missions from cybersecurity vulnerabilities. The following refined guidance outlines practical approaches for smaller projects to meet security requirements without sacrificing effectiveness.

---

#### **1. Leverage Free and NASA-Approved Resources**

* Smaller projects can utilize **NASA-approved free software tools** for security scanning and vulnerability mitigation. These tools are vetted and maintained to align with NASA's standards and can be effective replacements for commercial security scanners.
  + Examples may include tools for static code analysis, malware scanning, secure code review, and open-source vulnerability testing frameworks.
* **Office of Chief Information Officer (OCIO) Options**:
  + The OCIO can provide guidance on available free tools, secure frameworks, and techniques for cybersecurity verification and validation.
  + Reach out to OCIO for assistance in identifying tools that are appropriate for small projects and ensuring compliance with security standards.

---

#### **2. Manual Methods for Security Assurance**

* **Adapting Manual Testing**:
  + In situations where automated tools are unavailable, manual methods become more critical. Manual approaches can include:
    - **Code Reviews**: Multiple peer reviewers should inspect the code for security vulnerabilities (e.g., hardcoded credentials, buffer overflows, poorly implemented encryption).
    - **Interface Analysis**: Focus on verifying security measures at interface points such as APIs, communication protocols, or software system integration boundaries.
    - **Supply Chain Risk Inspection**: Examine third-party libraries or components used in the project for outdated patches, known vulnerabilities, or insecure configurations.
    - **Hardening**: Follow manual checklists to secure the software and its environment, addressing access permissions, disabling unused ports, and encrypting sensitive data.

---

#### **3. Collaboration With Larger Projects**

* **Resource Sharing**:
  + Smaller projects can collaborate with larger projects to gain access to security tools, infrastructure, or expertise. For example:
    - Negotiate access to larger projects’ security infrastructure or tool licenses (e.g., static analysis tools, penetration testing frameworks) with appropriate compensation agreements.
    - Share lessons learned and best practices on identifying and remediating security risks with larger project teams.
  + Larger projects and organizations may be willing to share:
    - Security scanning tools.
    - Training resources for manual cybersecurity validation techniques.
    - Expertise from personnel or external consultants.

---

#### **4. Focus on Critical and Vulnerable Systems**

* Given resource constraints, smaller projects should prioritize their security efforts by identifying and focusing on the **most critical and vulnerable systems** in the software architecture.
  + **Prioritization Process**:
    - Identify the **interfaces**, **high-risk entry points**, and **external-system touchpoints** within the software. Account for areas susceptible to unauthorized access or data manipulation.
    - Highlight mission-critical systems that might compromise operations, safety, or data integrity if exploited.
    - Allocate concentrated efforts on those systems to ensure all mitigations are tested and validated thoroughly.
  + **Interface Security**:
    - Secure all system interfaces, as they are common areas for vulnerabilities. Examples of security strategies at these points include:
      * Input validation to sanitize data from external sources.
      * Allow-list/block-list mechanisms to ensure only authorized communication protocols are allowed.
      * Encryption to ensure secure data transmission across external interfaces.

---

#### **5. Optimize Testing Approach**

* Smaller projects can optimize their testing methodology to make the best use of limited resources:
  + **Iterative Testing**:
    - Prioritize testing early to catch risks in the lifecycle phase where mitigation is least costly.
    - Repeat testing for critical systems and interfaces after small changes, ensuring secure operation continuously.
  + **Fuzz Testing**:
    - Implement fuzz testing to simulate unexpected or malformed inputs, ensuring the software handles adverse conditions gracefully.
  + **Regression Testing**:
    - Use regression tests after major updates to verify that security issues previously identified have been mitigated and that no new vulnerabilities have been introduced.

---

#### **6. Build a Lightweight Security Plan**

* Smaller projects can build a **scaled-down security plan** tailored to their scope and risks:
  + **Key Elements for Small Projects**:
    - Identification of critical systems and interfaces requiring protection.
    - Mitigation strategies prioritized by severity (e.g., high-risk vulnerabilities addressed first).
    - Manual methods for validation of security measures when automated tools are unavailable.
    - Integration of NASA-approved free resources/tools to reduce costs and improve efficiency.
  + Documentation of this plan improves traceability and helps ensure compliance with NASA standards even under resource constraints.

---

#### **7. Engage Expertise**

* Leverage expertise from NASA's cybersecurity teams or OCIO security personnel to gain insights into efficient, scalable approaches for smaller projects.
  + NASA SMEs (Subject Matter Experts) may provide guidance on manual testing techniques, risk prioritization, and interface hardening.
* Engage with shared service centers, mission directorates, and project consultants for advice on cost-effective security measures tailored to the project’s needs and mission scope.

---

### **Summary**

Smaller projects can overcome resource constraints and implement robust security measures by adopting the following principles:

1. Use **NASA-approved free tools** and reach out to OCIO for guidance.
2. Apply effective **manual methods**, such as peer reviews and interface analysis, to compensate for the absence of automated security scanners.
3. **Collaborate** with larger projects to share tools, infrastructure, and expertise.
4. Focus efforts to secure **critical and vulnerable systems**, prioritizing areas such as interfaces and external touchpoints.
5. Optimize testing strategies with iterative, fuzz, and regression testing.
6. Develop a scaled-down yet **comprehensive security plan** tailored to project size and mission scope.
7. Engage NASA experts for additional support and resources.

By implementing these strategies, small projects can meet security requirements, mitigate vulnerabilities, and protect mission-critical systems effectively and efficiently.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-064)

  [Engineering Principles for Information Technology Security (A Baseline for Achieving Security),](https://csrc.nist.gov/publications/detail/sp/800-27/rev-a/archive/2004-06-21 "Click to open in new window")

  NIST SP 800-27, Revision A.
* (SWEREF-065)

  [Security Considerations in the System Development Life Cycle,](http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-64r2.pdf "Click to open in new window")

  NIST SP 800-64 Revision 2.
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
* (SWEREF-664)

  [Software Security](https://nen.nasa.gov/web/coding "Click to open in new window")

  OCE site in NASA Engineering Network, Portal that houses information for software developers to develop code in a secure fashion,  Formerly known as "Secure Coding"
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

**NASA lessons learned** related to **software security risk mitigations, V&V (Verification and Validation), and protecting against cybersecurity vulnerabilities**. These lessons, documented in the **NASA Lessons Learned Information System (LLIS)**, provide insights and guidance that can be applied to meet this requirement. Below are examples of relevant lessons, along with their context and how they can inform the implementation of this requirement.

---

### **1. Lesson Learned: Insufficient Validation of Mission Software Security**

* **LLIS Reference**: LLIS-0938
* **Description**: A space mission encountered operational issues due to inadequate testing and validation of software security controls. The project neglected to fully verify the implementation of cybersecurity mitigations, resulting in vulnerabilities that were exploited in testing scenarios, delaying mission readiness.
* **Key Takeaway**:
  + Comprehensive and iterative V&V must be performed to validate that all vulnerabilities identified during risk assessments are fully mitigated.
  + Focus on high-priority risks in critical systems and interfaces, which are often the most vulnerable.
* **Application**:
  + Ensure that all mitigations are tested and validated as part of planned V&V activities, including peer reviews, static and dynamic code analysis, and security-specific regression testing.
  + Test for vulnerabilities early in the lifecycle when they are easier and less costly to address.

---

### **2. Lesson Learned: Lack of Security Focus in Software Peer Reviews**

* **LLIS Reference**: LLIS-0792
* **Description**: Several NASA projects reported that early-stage peer reviews did not adequately focus on cybersecurity, leading to an accumulation of software vulnerabilities. These vulnerabilities were difficult to address during later stages of development, resulting in schedule delays and increased costs. Critical security issues, such as hardcoded credentials and weak encryption, could have been avoided through early review of secure coding practices.
* **Key Takeaway**:
  + Include specific security-related items in the review checklist for all software peer reviews, particularly during requirements, design, and code inspections.
* **Application**:
  + Update project peer review procedures to include checks for security risks, such as input sanitization, secure authentication mechanisms, and system interfaces.
  + Refer to **SWE-087** and **SWE-088**, which provide detailed guidance on enhancing software peer reviews with security considerations.

---

### **3. Lesson Learned: Security Oversights in Interfaces**

* **LLIS Reference**: LLIS-2910
* **Description**: A NASA program found that system interfaces were the most vulnerable points for cyberattacks due to insufficient boundary protections. For example, interfaces did not restrict unauthorized command submissions or validate input data, leading to system-level compromises during testing.
* **Key Takeaway**:
  + Interfaces and external communication pathways are often the most vulnerable areas for systems and should be prioritized during V&V of cybersecurity mitigations.
* **Application**:
  + During planning, identify and focus testing on all system interfaces. Validate against risks such as unauthorized access, data interception, and malformed input commands.
  + Use V&V techniques like "fuzz testing" on interfaces to ensure they handle unexpected or malformed inputs gracefully.

---

### **4. Lesson Learned: Importance of Collaboration for Resource-Restrained Projects**

* **LLIS Reference**: LLIS-3045
* **Description**: Smaller NASA projects struggled to implement robust security practices due to limited resources, including inadequate access to automated tools, expertise, and infrastructure. However, collaborative resource-sharing agreements with larger projects enabled the smaller projects to benefit from advanced security tools and practices.
* **Key Takeaway**:
  + Smaller projects should actively seek collaboration opportunities with larger projects to gain access to security tools, infrastructure, and shared expertise.
* **Application**:
  + Engage with NASA’s **Office of the Chief Information Officer (OCIO)** or other groups to explore resource-sharing options.
  + Identify opportunities to share licenses for automated security scanners or involve personnel from larger projects for security-focused reviews or consultations.

---

### **5. Lesson Learned: Lessons from Real-World Security Incidents**

* **LLIS Reference**: LLIS-0912
* **Description**: Post-incident analyses of cybersecurity breaches during previous missions revealed that root causes often involved insufficient testing of security mitigations against real-world attack scenarios. For example, certain mitigations were designed for nominal conditions, while real-world stressors exposed overlooked vulnerabilities.
* **Key Takeaway**:
  + Projects must ensure that testing scenarios include realistic, mission-relevant conditions, including stress or failure modes, to validate the robustness of security mitigations.
* **Application**:
  + Simulate real-world conditions during V&V testing (e.g., testing cybersecurity under stress, heavy data loads, or unexpected inputs). Use dynamic code analysis for runtime testing under adverse or attack-like scenarios.
  + Repeat vulnerability assessments after applying mitigations to ensure that weaknesses have been fully addressed and no new issues introduced.

---

### **6. Lesson Learned: The Risk of Delaying Cybersecurity Efforts**

* **LLIS Reference**: LLIS-2262
* **Description**: Projects that deferred cybersecurity risk assessments and mitigations to late phases of development encountered a significantly higher cost to remediate issues, as well as schedule delays in addressing critical vulnerabilities.
* **Key Takeaway**:
  + Cybersecurity assessment and mitigation efforts must be addressed as early as possible in the system development process.
* **Application**:
  + Include cybersecurity V&V activities in the plan from the beginning, ensuring that mitigations for identified risks are tested early and throughout the lifecycle.
  + Take advantage of early-phase tools (e.g., NASA-approved free tools, manual inspections) to implement mitigations in low-cost stages.

---

### **7. Lesson Learned: Supply Chain Risks in Third-Party Software**

* **LLIS Reference**: LLIS-2030
* **Description**: A NASA project encountered significant vulnerabilities introduced via third-party components in their software supply chain. Dependency analysis was not performed to check for outdated or unpatched software libraries, resulting in the inclusion of known vulnerabilities in the final system.
* **Key Takeaway**:
  + V&V activities should include careful scrutiny of third-party software, ensuring all components are patched and secure.
* **Application**:
  + Add supply chain security checks to V&V procedures. Ensure third-party libraries are analyzed for security patches and up-to-date.
  + Examine third-party dependencies for compliance with NASA security standards (e.g., SWE-154, SWE-156).

---

### **8. Lesson Learned: Coordination With Project Protection Plans**

* **LLIS Reference**: LLIS-3178
* **Description**: Some projects failed to incorporate security needs identified in the Project Protection Plan (PPP) into their V&V activities due to poor communication with PPP owners. This oversight resulted in gaps between PPP objectives and system implementation.
* **Key Takeaway**:
  + Engage with PPP owners early to ensure that all derived requirements from the PPP (including sensitive or mission-specific security needs) are addressed in V&V planning.
* **Application**:
  + Consult with PPP owners to derive actionable security requirements, incorporate them into checklists and test plans, and validate them during V&V activities.

---

### **Conclusion**

These lessons learned emphasize key principles for effectively meeting **Requirement 3.1** and related NASA requirements:

1. **Test early and iteratively** to minimize costs and avoid late-stage surprises.
2. Focus on **critical systems and interfaces** as they are the most vulnerable.
3. Incorporate **manual and automated testing** techniques to address identified security risks.
4. Account for **supply chain vulnerabilities** and third-party libraries.
5. Collaborate with larger projects and OCIO for resource-sharing opportunities.
6. Maintain alignment with **Project Protection Plans (PPP)** to ensure mission-critical security requirements are tested and validated.

By applying these lessons, project teams can ensure their V&V activities are robust, cost-efficient, and aligned with NASA’s stringent cybersecurity goals.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Run static analysis on code developed for unit test](https://software.gsfc.nasa.gov/lesson-details/217/). **Lesson Number 217**: The recommendation states: "Static analysis tools should be run not only on flight code (or production code in non-flight cases), but also on code developed for unit test. The issues identified for all code should be properly dispositioned and resolved."

# 7. Software Assurance

**SWE-159 - Verify and Validate Risk Mitigations**

3.11.5 The project manager shall test the software and record test results for the required software cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis.

The Software Assurance (SA) process for addressing cybersecurity mitigation requirements and verifying their quality must be comprehensive and tailored to ensure robust testing, accurate reporting, effective mitigation, and continuous improvement throughout the software development lifecycle. Below is the enhanced guidance, along with improved descriptions for products, metrics, and actionable steps.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that testing is complete for the cybersecurity mitigation.

2. Assess the quality of the cybersecurity mitigation implementation testing and the test results.

## 7.2 Software Assurance Products

---

#### **1. Source Code Analysis**

The SA team facilitates both automated and manual analyses of the source code to identify security weaknesses, vulnerabilities, and non-conformances. Key practices include:

* Use software static analysis tools to detect code-level vulnerabilities such as potential buffer overflows, race conditions, or improper input handling.
* Conduct **independent assessments** by running SA-specific static analysis tools to validate findings reported by engineering teams.
* Check for secure coding standards adherence (e.g., NASA Secure Coding Practices, CERT Secure Coding Standards).

#### **2. Verification Activities Analysis**

SA must independently evaluate all project-level verification activities related to cybersecurity requirements, ensuring:

* Testing aligns with requirements for cybersecurity mitigations determined in SWE-154 and SWE-156.
* The verification artifacts provide comprehensive coverage of identified risks and mitigations.

#### **3. Software Assurance Assessment of Cybersecurity Mitigation Testing**

SA evaluates the **quality** and **completeness** of cybersecurity mitigation test procedures and results. This involves:

* Reviewing cybersecurity test reports to ensure findings are thorough, repeatable, and accurate.
* Confirming test procedures systematically address vulnerabilities and weaknesses identified in the system lifecycle.
* Ensuring non-conformances are documented, categorized (severity), and tracked for resolution.

#### **4. Software Test Procedures**

SA reviews test procedures to validate:

* Proper mapping between test cases and detailed cybersecurity requirements.
* Critical security functions (e.g., input validation, encryption mechanisms, access control, detection of unauthorized commands) are covered in the planned tests.

#### **5. Software Test Reports**

SA must ensure test reports include:

* Analysis and outcomes of cybersecurity-specific tests.
* Documentation of resolved vulnerabilities and weaknesses.
* Compliance with NASA standards (e.g., SWE-191 for regression testing, SWE-157 for unauthorized access prevention).

## 7.3 Metrics

#### **Key Metrics to Measure and Evaluate Cybersecurity Testing**

The SA team monitors and reports metrics to evaluate the effectiveness of cyber-risk mitigations while identifying trends and areas requiring improvement. The following metrics are tracked:

**A. Testing Coverage**

1. **Total tests completed vs. number of test results signed off**:
   * Ensures proper validation and approval of test results related to cybersecurity mitigations.
2. **Number of cybersecurity mitigation tests completed vs. total cybersecurity mitigation tests planned**:
   * Tracks the progress and completeness of mitigation testing.
3. **Number of tested detailed software requirements vs. total number of requirements**:
   * Measures how much of the software's security requirements have been tested to date.

**B. Security Vulnerabilities** 4. **Number of cybersecurity vulnerabilities and weaknesses identified**:

* Tracks total vulnerabilities discovered during testing and analysis.

1. **Number of vulnerabilities identified vs. number resolved during implementation**:
   * Evaluates the effectiveness of risk resolution efforts.
2. **Trending of open vs. closed vulnerabilities over time**:
   * Identifies whether vulnerabilities are being resolved in a timely fashion.
3. **Number of vulnerabilities categorized by lifecycle phase**:
   * Highlights lifecycle phases where vulnerabilities are most prevalent (e.g., design phase vs. implementation phase).

**C. Non-Conformance Tracking** 8. **Number of non-conformances identified during cybersecurity testing (open, closed, severity)**:

* Tracks unresolved issues and focuses attention on severe non-conformances.

1. **Trend analysis of cybersecurity non-conformances over time**:
   * Helps evaluate recurring issues or the effectiveness of corrective measures.

**D. Mitigation Verification** 10. **Number of cybersecurity risk mitigations identified vs. mitigations tested**:

* Validates that mitigations are not just identified but tested and verified.

1. **Number of non-conformances identified by lifecycle phase**:

* Helps pinpoint phases where processes can be strengthened.

1. **Number of cybersecurity mitigations with associated test procedures**:

* Confirms proper linkage between mitigations and test cases.

---

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

#### **Confirmation Steps for Quality and Completeness of Cybersecurity Mitigation Testing**

The SA team’s role involves independently verifying the quality of testing and ensuring the results are sufficient to address the required mitigations. Suggested steps include:

**1. Source Code Evaluation**

* **Automated Tools**:
  + Use static code analyzers to assess for security weaknesses and violations of secure coding guidelines (e.g., inadequate error handling, insecure communication protocols).
  + Compare SA-independent analysis results with those conducted by software engineering teams to validate findings.
* **Manual Methods**:
  + For software systems excluding automated tools, perform targeted manual reviews. Focus areas include:
    - Secure initialization of software components.
    - The absence of banned constructs (e.g., hardcoded credentials, inadequate memory access protections).

**2. Static Code Analysis Comparison**

* Establish baseline metrics for static code analysis results.
* Compare these to ongoing analysis findings to ensure improvements in identified vulnerabilities over time.
* Confirm that static analysis findings have been appropriately addressed by the project team.

**3. Peer Review Integration**

* Conduct peer reviews with both Software Assurance and engineering teams:
  + Review known vulnerabilities and weaknesses.
  + Confirm that manual findings align with automated results and that mitigations are planned or implemented.

**4. Vulnerability and Weakness Tracking**

* Confirm that identified vulnerabilities and weaknesses from **NIST National Vulnerability Database (NVD)** and **MITRE Common Weakness Enumeration (CWE)** are logged and analyzed.
* Use SA oversight to verify that all high-priority vulnerabilities are mitigated within NASA’s prescribed remediation timelines.
  + **High severity**: Within 5 working days.
  + **Moderate severity**: Within 30 working days.
  + **Low severity**: Within 60 working days.

**5. Test Procedure Evaluation**

* Verify that cybersecurity mitigation requirements are fully mapped to test procedures.
* Review procedures to confirm that tests cover areas such as:
  + Prevention of unauthorized access to commands or data.
  + Input validation (restricting inputs to expected types and values).
  + Robust handling of malformed commands, boundary conditions, and failure modes.

**6. Review and Validation of Test Results**

* Assess test reports to ensure vulnerabilities are categorized by severity, tracked, and remediated.
* Confirm trending analysis of open vs. closed vulnerabilities, ensuring alignment with NASA’s mitigation goals.

**7. Secure Coding Standards**

* Reference NASA’s **secure coding site** and guidelines for ensuring all code adheres to proven practices for reducing security weaknesses.

---

### **Additional Resources**

* **NIST National Vulnerability Database (NVD)**:
  + Provides data on security vulnerabilities applicable to software components.
* **MITRE Common Weakness Enumeration (CWE)**:
  + Defines software weaknesses and aids in identifying areas of concern during code reviews.
* **Secure Coding Site (NASA Access Only)**:
  + Offers NASA-approved secure coding standards, tools, and best practices.

---

### **Conclusion**

This improved SA guidance ensures that cybersecurity mitigation testing is complete, rigorous, and continually improved throughout the project lifecycle. It integrates automated tools, manual methods, peer reviews, and vulnerability tracking to ensure the highest quality of software security assurance while aligning with NASA's stringent cybersecurity goals. By combining tailored metrics and detailed steps, SA teams can maximize the effectiveness of their oversight and decision-making.

See also [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)        * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence is a critical component for demonstrating compliance with **Requirement 3.11.5: Thorough software testing and documentation of results for cybersecurity mitigation implementations.**

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

Below are examples of **objective evidence** that can be collected, organized, and presented to verify adherence to the requirement.

---

### **Objective Evidence Categories and Examples**

#### **1. Documentation of Identified Security Risks (Initial Inputs)**

Evidence of risk identification activities helps demonstrate that foundational steps have been taken to address cybersecurity vulnerabilities.

* **Risk Assessment Reports**:
  + Security vulnerability assessments (system-wide or software-specific).
  + Cybersecurity risks identified during architecture and interface design reviews.
* **Plan of Action & Milestones (POA&M)**: Document outlining the detailed actions required to mitigate identified risks. Includes:
  + Timeline of mitigation activities.
  + Prioritization of vulnerabilities (high, medium, low severity).
  + Progress tracking of mitigations.

---

#### **2. Software Test Plans and Procedures**

These documents demonstrate that testing was planned and structured to address security mitigations effectively.

* **Software Test Plan (STP)**:
  + Includes specific test cases for validating cybersecurity risk mitigations (e.g., testing boundary protections, input validation, command authentication).
  + Traceability between security requirements (SWE-154, SWE-156, SWE-157) and test cases.
  + Testing methodologies (e.g., static testing, dynamic testing, penetration testing) and tools used.
* **Test Procedures**:
  + Detailed test procedures documenting step-by-step validation methods for cybersecurity mitigations.
  + Procedures for system interfaces, data encryption, authentication protocols, and handling of malformed inputs.

---

#### **3. Static and Dynamic Code Analysis Reports**

Objective evidence demonstrating the identification and correction of code-level vulnerabilities.

* **Automated Analysis Reports**:
  + Results from static code analysis tools, showing vulnerabilities tied to insecure coding practices.
  + Dynamic analysis reports demonstrating runtime behavior and detection of execution vulnerabilities (e.g., race conditions, buffer overflows).
* **Coding Standards Compliance Reports**: Evidence that code adheres to NASA-approved coding standards or secure coding practices (e.g., CERT Secure Coding Standards, NASA Secure Coding Guidelines).

---

#### **4. Peer Review Records**

Peer reviews serve as key checkpoints for detecting vulnerabilities early in the software lifecycle.

* **Peer Review Checklists**:
  + Checklists updated with cybersecurity-related items (e.g., identification of input sanitization risks, misuse of sensitive variables).
* **Peer Review Reports**:
  + Documented review findings and actions taken to address reviewed cybersecurity issues in requirements, design, and code.
  + Evidence of vulnerability resolution discussed during reviews.

---

#### **5. Cybersecurity Test Results**

Objective evidence that security mitigations were tested exhaustively, and vulnerabilities were identified, resolved, and verified.

* **Test Completion Reports**:
  + Documentation showing the successful completion of all tests related to security mitigations.
  + Pass/fail results for each test case.
* **Defect and Resolution Logs**:
  + Log identifying all defects discovered during testing, including security-related defects.
  + Evidence that defects were addressed and resolved, with closure confirmed.
* **Open vs. Closed Vulnerability Trends**:
  + Trends showing successful resolution of vulnerabilities over time (e.g., tracking cybersecurity risks discovered during lifecycle phases and percentage mitigated).

---

#### **6. Cybersecurity Metrics**

Quantitative evidence that measures testing coverage, effectiveness, and risk mitigation success.

* **Key Metrics Examples**:
  + Total number of cybersecurity risks identified vs. resolved.
  + Number of test cases associated with cybersecurity mitigations vs. successfully executed.
  + Number of open vs. closed non-conformances related to cybersecurity testing (tracked by severity: high/medium/low).
  + Testing coverage trends (e.g., completion rates for high-impact systems or critical interfaces).
  + Vulnerabilities identified per lifecycle phase (e.g., design, implementation, testing).

---

#### **7. Regression Testing Reports**

Evidence that previous mitigations remain effective after system updates or changes.

* **Regression Test Results**:
  + Documentation of tests performed following updates, system changes, or bug fixes to ensure mitigations are still intact and no new vulnerabilities were introduced.
* **Verification of Security Controls Stability**:
  + Evidence that existing security controls continue to function as designed across system updates.

---

#### **8. Validation of Manual Methods**

For systems without automated testing tools, documentation of alternative techniques used can serve as objective evidence.

* **Manual Testing Records**:
  + Records showing the extent and scope of manual reviews performed (e.g., code inspections, interface analysis).
  + Evidence that issues identified during manual testing were investigated and remediated.
* **Audit Logs**:
  + Logs tracking manual methods used to verify cybersecurity compliance, including team review meetings, issue tracking, and resolution activities.

---

#### **9. Vulnerability Tracking Tools**

Evidence from tools used to identify and track vulnerabilities throughout the lifecycle.

* **Security Scanning Results**:
  + Documentation from vulnerability scanners showing identified weaknesses (e.g., outdated libraries, insecure configurations) and remediation actions taken.
* **Risk Resolution Logs**:
  + Use of tools (e.g., POA&M tracking tools, Jira, Bugzilla) to identify, categorize, track, and resolve weaknesses associated with cybersecurity mitigations.

---

#### **10. Project Protection Plan (PPP) Alignment**

Evidence showing that testing activities align with security requirements documented in the PPP.

* **PPP-Derived Requirements**:
  + Requirements traced from the PPP to test procedures, ensuring compliance with Controlled Unclassified Information (CUI) standards.
* **PPP Confirmation Records**:
  + Evidence of communication with PPP owners verifying testing coverage and alignment with their security needs.

---

### **Examples of Objective Evidence Artifacts**

1. **Risk Assessments**: Project-specific system-level risk assessment reports.
2. **Traceability Matrices**: Mapping cybersecurity requirements to test cases and executed test results.
3. **Static Code Analysis Logs**: Automated scanner outputs documenting vulnerabilities and corrections.
4. **Dynamic Testing Reports**: Results from penetration tests or simulated attack scenarios verifying system readiness.
5. **Peer Review Meeting Minutes**: Formal review records with documented decisions on resolving vulnerabilities.
6. **Defect Tracker Logs**: Logs showing tracking progress for vulnerabilities and weaknesses identified during the lifecycle.
7. **Test Metrics Dashboards**: Data visualizations showing testing performance trends and remediation status.
8. **Tool Configuration Reports**: Documentation confirming the use of NASA-approved tools for security testing.
9. **Regression Testing Results**: Artifact logs showing stability after fixes or system changes.
10. **Manual Method Worksheets**: Artifacts showing manual reviews and audits performed on systems or components.

---

### **Conclusion**

Objective evidence provides traceable, auditable, and actionable confirmation of compliance with **Requirement 3.11.5**. As NASA places a high priority on cybersecurity, these artifacts and records are essential for assuring vulnerabilities are mitigated, weaknesses are addressed, and systems are secure to meet mission-critical standards. Such evidence supports transparency, accountability, and long-term security assurance.
