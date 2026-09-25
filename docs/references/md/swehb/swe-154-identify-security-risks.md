# SWE-154 - Identify Security Risks

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695510. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks

SWE-154 - Identify Security Risks

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695510)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695510&showCommentArea=true&showComments=true#addcomment)

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

3.11.3 The project manager shall identify cybersecurity risks, along with their mitigations, in flight and ground software systems and plan the mitigations for these systems.

## 1.1 Notes

Project Protection Plans describe the program’s approach for planning and implementing the requirements for information, physical, personnel, industrial, and counterintelligence/counterterrorism security, and for security awareness/education requirements in accordance with NPR 1600.1, NASA Security Program Procedural Requirements, NPD 1600.2, the NASA Security Policy, NPD 2810.1, and NPR 2810.1. Include provisions in the plan to protect personnel, facilities, mission-essential infrastructure, and critical program information from potential threats and vulnerabilities that may be identified during the threat and vulnerability assessment process.

## 1.2 History

Click here to view the history of this requirement: SWE-154 History

SWE-154 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 3.16.2 The project manager shall ensure that security risks in space flight software systems are identified and security risk mitigations are planned for these systems in the Project Protection Plan. |
| Difference between B and C | Changed focus of responsibility to identify risks - "ensure" was removed;  Changed security to cybersecurity;  Removed the requirement for a Project Protection Plan. |
| C | 3.11.3 The project manager shall identify cybersecurity risks, along with their mitigations, in flight and ground software systems and plan the mitigations for these systems. |
| Difference between C and D | No change |
| D | 3.11.3 The project manager shall identify cybersecurity risks, along with their mitigations, in flight and ground software systems and plan the mitigations for these systems. |

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

Software systems have the potential to provide an entry point for actors to abuse or exploit the asset in an unexpected manner.  Identifying the threats and risks as well as the planned mitigations for them early in the project life cycle helps to increase the overall security and enhance the reliability of the system.

The rationale for Requirement 3.11.3 lies in the critical importance of ensuring the security, reliability, and resilience of both flight and ground software systems that support NASA missions. These systems often play essential roles in mission success, whether through the direct operation of spacecraft, processing of mission data, or the secure transmission of commands and telemetry. Cybersecurity risks threaten not only the systems themselves but also the mission’s objectives, public safety, and NASA's reputation. Thus, implementing processes for **identifying cybersecurity risks and planning mitigations** is essential for ensuring operational integrity.

### **1. Protect NASA Missions from Evolving Cybersecurity Threats**

* **Rationale**: Flight and ground software systems are increasingly exposed to evolving cybersecurity threats, including attacks targeting data integrity, communication systems, and remote access interfaces. Threat vectors may arise from external actors (e.g., adversaries targeting NASA infrastructure) or internal oversights (e.g., software vulnerabilities).
* **Why Mitigations are Essential**: Unaddressed cybersecurity risks could lead to:
  + **Data corruption**: Loss or compromise of scientific or operational data.
  + **Operational interference**: Unauthorized access or command injection, leading to spacecraft misbehavior or mission failure.
  + **System compromise**: Breaches in Earth-based systems (e.g., ground stations) leading to cascading vulnerabilities in flight software.

By identifying and mitigating these risks proactively, Requirement 3.11.3 ensures the secure execution of missions while fostering trust in NASA's critical systems.

### **2. Holistic Approach to Flight and Ground Software Security**

* **Rationale**: Flight and ground systems are interconnected and interdependent, meaning cybersecurity risks in one domain can propagate to the other. For example:

  + **Flight software vulnerabilities** could be exploited through communication interfaces originating at ground stations.
  + **Ground system vulnerabilities** could enable attackers to gain unauthorized access to spacecraft, leading to control manipulation or denial-of-service attacks.
* **Why Mitigations are Essential**: By planning mitigations for both flight and ground systems, Requirement 3.11.3 ensures a **holistic defense** that addresses the complete lifecycle of risks across NASA's operational infrastructure. This integration prevents siloed cybersecurity practices and ensures comprehensive protection.

### **3. Alignment with Mission-Critical Cyber Resilience**

* **Rationale**: Many NASA mission systems exist in challenging and constrained environments with limited capacity for real-time troubleshooting (e.g., software aboard long-duration spacecraft, lunar surface operations). Cybersecurity issues in these environments can have irreversible consequences due to system isolation and inability to apply immediate patches or mitigations.
* **Why Mitigations are Essential**: Effective **planning of mitigations** during the software lifecycle ensures systems can:
  + **Detect and respond to cybersecurity threats autonomously**.
  + Operate in "degraded states" that maintain mission objectives even when risks materialize.
  + Protect long-duration or time-critical missions from cascading failures triggered by exploitation of vulnerabilities.

### **4. Compliance with NASA Standards and Policies**

* **Rationale**: NASA has established cybersecurity-related policies, standards, and directives (e.g., NASA-STD-1006, NPR 7120.5E) to address system protection. These directives specify the identification of risks and integration of mitigations across mission-critical systems.

  + The **SPACE SYSTEM PROTECTION STANDARD (NASA-STD-1006)** outlines protection strategies for both software and hardware.
  + NPR 7120.5E mandates the development of **Threat Summaries** and **Project Protection Plans (PPP)** for all flight programs and projects.
* **Why Mitigations are Essential**: Requirement 3.11.3 ensures the necessary integration of software cybersecurity risks and mitigations into these policies, enabling projects to meet agency-wide standards for cybersecurity and mission assurance.

### **5. Addressing Risks in Third-Party Software (COTS, GOTS, OSS, MOTS, and Reused Components)**

* **Rationale**: Third-party software often introduces unique challenges to cybersecurity due to limited visibility, control over source code, or reliance on external dependencies. COTS, OSS, GOTS, MOTS, and reused software can contain unpatched vulnerabilities or outdated security mechanisms that expose systems to attack.
* **Why Mitigations are Essential**:

  + Proactively evaluating risks ensures that vulnerabilities stemming from third-party software are identified and mitigated before integration.
  + Planning for regular **updates, patches, and testing** safeguards critical systems from reliance on insecure external components.

### **6. Prevention of Financial and Reputational Damage**

* **Rationale**: Cybersecurity failures in NASA systems can result in significant financial losses due to delays in mission timelines, equipment failures, or required remediation efforts. Additionally, the public and international community expect NASA systems to function securely and responsibly. A cybersecurity incident could erode trust, damage NASA’s reputation, and risk sensitive data vital to national and global interests.
* **Why Mitigations are Essential**: Proper planning ensures risks are addressed efficiently, avoiding costly and reputationally damaging outcomes. It also helps demonstrate NASA’s leadership in aerospace cybersecurity.

### **7. Enablement of Continuous Risk Management**

* **Rationale**: Cybersecurity is not a "once-and-done" concern; software systems require lifecycle-level risk management as new vulnerabilities and threats emerge. Requirement 3.11.3 enforces ongoing evaluations and anticipatory planning.
* **Why Mitigations are Essential**:

  + Establishing proactive mitigation planning ensures systems can adapt to emerging threats after deployment.
  + Continuous updates, monitoring, and re-assessment preserve system security for long-duration missions and complex ground operations.

### **8. Protecting NASA's Unique Operating Environment**

* **Rationale**: NASA mission systems often operate in unique contexts—spacecraft are remote, autonomous, and resource-constrained, while ground systems are network-connected and rely on global infrastructure. Flight systems may experience hardware redundancy limits, long communication delays, and power constraints.
* **Why Mitigations are Essential**:

  + Secure flight software is critical for maintaining system integrity in extreme and isolated environments.
  + Ground software, as the primary interface to these systems, must be safeguarded to prevent attackers from exploiting the connection to manipulate spacecraft behavior.

### **Key Objectives for Addressing Cybersecurity Risks**

Requirement 3.11.3 supports the following objectives:

1. **Early Risk Identification**: Proactive identification of cybersecurity risks reduces the likelihood of late-stage vulnerabilities threatening mission success.
2. **Integrated Risk Mitigation**: A unified approach to handling risks in both flight and ground systems ensures comprehensive risk management.
3. **Alignment with NASA Policies**: By conforming to NASA’s cybersecurity directives, the requirement ensures accountability and standardized processes.
4. **Cost and Time Savings**: Early planning reduces the cost and time spent on reactive security fixes or post-deployment incidents.
5. **Resilience in Adverse Environments**: Mitigation plans provide robustness and continuity for missions operating in isolated or resource-constrained settings.

### **Conclusion**

Requirement 3.11.3 ensures that NASA projects are prepared to address and mitigate cybersecurity risks for both flight and ground software systems. By proactively identifying risks, aligning mitigations with NASA policies, and implementing a lifecycle-centric strategy, Requirement 3.11.3 protects mission systems while enabling their successful operation in complex and potentially hostile environments.

This focused approach safeguards NASA missions from evolving cybersecurity threats, ensures compliance with institutional standards, reduces financial impact and reputational risk, and protects mission-critical operations in space and on Earth.

See also Topic [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations).

# 3. Guidance

## 3.1 Threat Assessment

#### **Overview**:

For flight and ground software systems, it is essential to identify and address cybersecurity risks proactively. Threat assessments ensure that systems are designed with security in mind from the very start, reducing the probability of vulnerabilities being exploited in later stages of the software lifecycle or mission operations. The **project manager** and **software engineering team** play a collaborative role in supporting the program manager, Information System Security Officer (ISSO), and other Agency stakeholders in developing a comprehensive **Threat Summary** and identifying mitigation strategies to be captured in the **Project Protection Plan (PPP)**.

Threat assessments focus on identifying:

* Software defects or weaknesses with security implications.
* Risks introduced by third-party or reused components.
* Vulnerabilities related to the development process, operations, or deployment environments.

#### **Key Actions for Software Engineering**:

1. **Collaborate with the ISSO and Agency Threat Teams**:

   * Provide the ISSO and relevant teams with necessary input, including:
     + **Lists of software elements**: Operating systems, software tools, third-party libraries (e.g., COTS, OSS, GOTS, MOTS, reused software components).
     + **Software security strategies and processes** employed (e.g., use of static analysis tools, automated vulnerability scans, secure development frameworks).
   * Support the Threat Summary process by ensuring detailed documentation of potential software defects and vulnerabilities, focusing on those with **security ramifications** (e.g., design flaws, code errors, improper configurations).
2. **Ensure Comprehensive Threat Categorization**:

   * Leverage multiple sources to identify and categorize potential software-specific security threats:

     + **NIST FIPS 199 Assessment Results**: Identify critical information and categorize software assets based on confidentiality, integrity, and availability.
     + **System Security Plan (SSP)**: Integrate SSP-derived threats for the flight and ground segments into software-level assessments.
     + **Risk Assessments**: Utilize risk reports provided by the ISSO and program-level teams.
     + **CCSDS Guidance**: Leverage documents from the Consultative Committee for Space Data Systems to understand industry-defined security threats, including operator/user, software, and external agent risks.
   * Consider risks introduced by:

     + **Users or administrators** installing unauthorized or poorly vetted software.
     + **Misconfigurations** by system operators leading to weakened security controls.
     + **Programming errors** resulting in systemic vulnerabilities or instabilities.
     + **Exploitation by external threat agents**, including injection attacks or unauthorized system modifications.
3. **Incorporate Threat Findings into the Project Protection Plan (PPP)**:

   * Draft **threat summaries** and integrate them into the **Project Protection Plan** as early as the **formulation phase** (pre-SDR/MDR).
   * Verify that:
     + Software defects with security implications are included in threat assessments.
     + Mitigation measures are clearly outlined in the PPP and traceable to specific risks.

#### **Best Practices**:

* **Timeframe Considerations and Planning**:

  + Begin threat assessments early (pre-SDR/MDR) and update them iteratively at milestones such as Preliminary Design Review (PDR), Critical Design Review (CDR), and System Integration Review (SIR). This mitigates late-stage security risks and avoids costly rework.
  + Recognize that threat assessments and mitigation strategies will evolve throughout the mission lifecycle, including during **Operational Readiness Reviews (ORR)** and **Mission Readiness Reviews (MRR/FRR)**.
* **Secure Development and Deployment Techniques**:

  + Plan for **built-in mitigations** including:
    - Adoption of secure coding standards.
    - Proactive usage of vulnerability testing, static code analysis, and penetration testing.
    - Implementation of encryption schemes to safeguard data at rest and in transit.

#### **Sources of Input**:

1. **NPR 2810.1**: Security requirements for software acquisition, development, and modification.
2. **System Security Plan (SSP)**: Define threats and risks at the system level and use as input for software-specific assessments.
3. **NASA Software Security Website**: Accessible via the NEN (NASA Engineering Network).
4. **Consultative Committee for Space Data Systems (CCSDS)**: Documents detailing space system security threats.

## 3.2 Project Protection Plan (PPP)

#### **Overview**:

The **Project Protection Plan (PPP)** serves as the formalized outcome of the threat assessment and mitigation planning process. It is a classified document that details the finalized threats, susceptibility analysis, vulnerabilities, and associated mitigations for the entire system, including flight and ground software systems. The PPP supports system survivability and mission resilience.

#### **Key Actions for Software Engineering**:

1. **Align Software Risks with PPP Development**:

   * Integrate identified **software-specific risks** from the Threat Summary into the PPP. This involves reviewing key threats and ensuring traceability to:
     + Risk categories defined in the NASA Risk Matrix (e.g., likelihood vs. impact).
     + Mitigation strategies addressing known vulnerabilities and defects.
2. **Iterate Protection Measures Across the System Lifecycle**:

   * Collaborate with the mission’s **System Protection Working Group (SPWG)** to refine mitigations over time:
     + **Before launch**: Update the PPP iteratively as part of key decision points (SDR, PDR, CDR, ORR, FRR).
     + **Post-launch**: Ensure **annual updates** of the PPP to keep pace with evolving threats and system changes.
3. **Incorporate Risk-Mitigating Strategies**:

   * Map software-specific mitigation plans for any identified risks into the PPP. Recommendations may include:
     + Static code analysis to detect known vulnerabilities.
     + Secure input/output handling processes to prevent injection or buffer overflow attacks.
     + Configuration reviews to eliminate security weaknesses from operator setup errors.
     + Penetration testing to probe for exploitable code pathways or interface flaws.
4. **Classified PPP Maintenance**:

   * Understand the classified nature of PPP documents (typically at the **Secret level**). Ensure that software engineering personnel involved in PPP-related activities have proper security clearances or are read in during critical reviews.

#### **Additional Guidance**:

* **Threat and Vulnerability Analysis**:

  + Fuse identified **protection threats** with system susceptibilities to identify actionable vulnerabilities.
  + Use the formula **Threat × Susceptibility = Vulnerability** as a guiding principle in determining risk priorities.
* **Model-Based Risk Mitigation**:

  + Utilize threat models available on the NASA Engineering Network (NEN) or through the **Mission Resilience and Protection Community of Practice**.

### **Summary of Key Deliverables**

| **Key Deliverable** | **Purpose** |
| --- | --- |
| **Threat Summary** | Captures recognized risks and their related vulnerabilities early in the lifecycle. |
| **Project Protection Plan (PPP)** | Describes systemwide mitigations for software and hardware risks, updated periodically to reflect evolving threats. |
| **System Security Plan (SSP)** | Documents threats, vulnerabilities, and risks associated with the larger system architecture that affect software components. |

### **Implementation Notes for SWE Compliance**:

* **SWE-156 (Evaluate Systems for Security Risks)**: Verify that software vulnerabilities are included in the system-level evaluation.
* **SWE-157 (Unauthorized Access Mitigation)**: Ensure that mitigations account for access control and authentication.
* **SWE-159 (Risk Mitigation Validation)**: Confirm that implemented countermeasures are tested and validated.
* **SWE-191 (Regression Testing of Software)**: Ensure cybersecurity mitigations do not introduce regressions into existing software.

Project Protection Plans [362](#_tabs-<p></p>)  are classified as documents (Secret).  NASA has developed a process to incrementally lower classification levels of relevant threat information to Secret and worked with project management teams to obtain clearances for their personnel at that level.  Program/Project managers can also be read in at the Secret level for short periods to review Project Protection Plans.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions)        * [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

For small projects, where resources (time, personnel, budget) are often limited, meeting cybersecurity requirements presents unique challenges. The following guidance tailors Requirement 3.11.3 to the needs of small projects by focusing on **streamlined processes, practical tools, and scalable methods** to identify and mitigate cybersecurity risks effectively.

### **Key Considerations for Small Projects**

1. **Resource Constraints**: Small projects may have fewer human and financial resources to allocate but must still follow cybersecurity best practices.
2. **Leverage Existing Tools and Frameworks**: Use low-cost, freely available, or lightweight tools to perform essential cybersecurity activities.
3. **Leverage Existing Documentation and Resources**: Borrow from existing threat libraries, templates, and checklists used in other NASA projects to save time. Consult ISSOs and reuse components from existing NASA initiatives where applicable.
4. **Identify Mission-Critical Risks First**: Concentrate efforts on the most significant and mission-critical risks, rather than attempting to address every possible vulnerability at once.

### **1. Simplified Threat Assessment**

The first step in the process is to perform a basic **threat assessment** for both flight and ground software systems. Small projects can make this step manageable by following a streamlined approach:

#### **Actionable Steps**:

1. **Build a Software Inventory**:  
   Identify all software components, including:

   * Operating systems.
   * Tools, libraries (COTS, GOTS, OSS, MOTS, reused software).
   * Third-party services and hardware interfaces.

   For each software component, document:

   * Its function in the system.
   * Its environment (offline, networked, connected to spacecraft, etc.).
   * Its criticality to mission success (high, medium, low).

   Tools for inventorying include:

   * A simple spreadsheet or checklist for small-scale documentation.
   * Use of a Software Bill of Materials (SBOM).
2. **Identify Threats Using Predefined Templates**:  
   Leverage existing threat models (e.g., NASA Engineering Network (NEN) resources or [NIST SP 800-30](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf)) to identify typical risks to small mission systems. Key categories:

   * Unauthorized access or command injection.
   * System misconfigurations (e.g., setup errors by operators or administrators).
   * Vulnerabilities in reused software (COTS/OSS libraries).
   * Denial of service (DoS) targeting ground-to-flight communication.
   * Data corruption or exposure during transmission (e.g., unencrypted telemetry).

   Example Tool:

   * **OWASP Threat Modeling Tool**: Offers a lightweight way to identify threats for smaller systems.
3. **Collaborate with the Information System Security Officer (ISSO)**:  
   Reach out to the project's designated ISSO or cybersecurity expert for assistance with validating identified risks. Provide basic system details, including the software inventory and associated functions.

   *Tip*: Small projects can rely heavily on the **ISSO's expertise** to guide the threat assessment.

### **2. Planning Mitigations for Software Risks**

Mitigations for risks identified in the threat assessment must be both practical and cost-effective. Small projects can prioritize the most impactful solutions and focus on building cybersecurity safeguards into the project.

#### **Actionable Steps**:

1. **Focus on High-Impact Threats**:  
   Rank each identified threat by:

   * Likelihood: How likely it is for the vulnerability to be exploited?
   * Impact: What is the consequence of exploitation (e.g., loss of mission-critical data)?

   Use a simple risk matrix (NASA Risk Matrix Standard) to prioritize risks.
2. **Leverage Low-Cost, Scalable Mitigation Techniques**:

   * **Use Automated Static Analysis Tools**:

     + Examples: SonarQube (Free Community Edition), Checkmarx, or GitHub’s built-in vulnerability scanning tools (dependabot).

     Static analysis tools can identify coding errors that lead to security vulnerabilities, such as:

     + Buffer overflows.
     + Insecure input/output handling.
     + Hardcoded credentials.
   * **Enforce Secure Configuration Practices**:

     + Apply default security features in operating systems and platforms (e.g., file permissions, access controls).
     + Verify configuration of networked components (e.g., secure firewall settings, encrypted connections).
   * **Simplify Secure Coding**:

     + Apply lightweight secure coding principles appropriate for small teams (e.g., CERT Secure Coding Standards).
     + Establish coding rules that every developer follows (e.g., input validation, error handling).
   * **Focus on Reliable Third-Party Software**:

     + Evaluate COTS, OSS, and reused software components for known vulnerabilities. Use:
       - OWASP Dependency-Check.
       - Tools like NPM Audit (for JavaScript libraries) or PyPI tools for Python libraries.
     + Select components with active community or vendor support for timely updates.
   * **Build-in Simple Encryption Schemes**:

     + Encrypt data at rest and in transit to protect sensitive information and telemetry.

### **3. Tailoring Project Protection Plans (PPP) for Small Projects**

Although the Project Protection Plan (PPP) is a required deliverable, small projects can balance compliance and practicality by simplifying its creation and focusing on high-priority threats.

#### **Actionable Steps**:

1. **Develop a Lightweight Threat Summary**:

   * Identify the top risks for the project using the process described in the threat assessment section.
   * Simplify categories to those most relevant to the project (e.g., software vulnerabilities, network risks, operational errors).
   * Use resources like predefined templates from NASA's **Mission Resilience and Protection Community of Practice** accessible on the NEN.
2. **Collaborate on PPP Refinement**:

   * Work closely with the system security team and SPWG (System Protection Working Group) to refine the PPP iteratively.
   * Use milestone reviews (e.g., SDR/PDR/CDR) to update and finalize the security impact of the software risks.
3. **Document the Essentials Only**:

   * Include only the relevant software risks and mitigations in your portion of the PPP. Avoid over-documenting risks that are unlikely to affect the mission.
4. **Revisit PPP Annually Post-Launch**:

   * Post-launch updates should focus on emerging cybersecurity threats, vulnerabilities, or updates for third-party software.

### **4. Essential Reviews and Validation**

Even for small projects, verifying that mitigations are effective is critical.

#### **Actionable Steps**:

1. **Perform Minimal Validation for Mitigations**:

   * Static and dynamic testing to ensure basic security controls (e.g., input validation, error handling, access control) are implemented successfully.
   * Regression testing to ensure mitigations do not unintentionally break other functionality (NASA SWE-191).
2. **Work Within Limited Personnel**:

   * If the team lacks dedicated cybersecurity personnel, rely on straightforward tools such as:
     + NASA’s Cybersecurity Best Practices (via NEN).
     + Free cybersecurity testing tools (e.g., Nessus Essentials, OWASP ZAP).
   * Seek help from the ISSO when advanced tools/testing expertise is needed.
3. **Review Key Artifacts** Before Key Milestones:

   * Ensure cybersecurity risks and their mitigations are recorded and validated by the time of:
     + Preliminary Design Review (PDR).
     + Critical Design Review (CDR).

### **5. Example Metrics for Monitoring Progress**

Tracking progress helps ensure that cybersecurity remains a focus as small projects advance. Metrics can be simple but informative:

* **Total risks identified vs. mitigated**: Number of open, closed, and unresolved cybersecurity risks.
* **Mitigation effectiveness**: Number of risks remediated after mitigation testing.
* **Risks by severity**: Count of high, medium, and low risks over time.
* **Risk trends pre- and post-deployment**: Measure new risks identified after system launch.

### **Summary of Scaled Execution for Small Projects**

| **Step** | **Key Activities** |
| --- | --- |
| **Threat Assessment** | Inventory software, use standard models, prioritize risks, and collaborate with ISSO. |
| **Plan Mitigations** | Focus on high-impact threats, use simple tools (e.g., static analyzers), and enforce secure configurations. |
| **Tailor PPP** | Address only critical risks, use templates, and avoid over-documentation. |
| **Validation and Reviews** | Perform lightweight testing, use ISSO expertise, and review at milestone events. |
| **Track Progress** | Use simple metrics to monitor open vs. closed risks and severity trends. |

---

By using this tailored approach, small projects can meet the requirements of 3.11.3 in a practical, efficient manner, ensuring cybersecurity risks are managed effectively without overburdening limited resources. This guidance emphasizes simplicity, leveraging existing support resources, and focusing on mission-critical risks.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-060)

  [Mission Resilience and Protection Community of Practice,](https://nen.nasa.gov/web/sap "Click to open in new window")

  NASA Engineering Network. Accessed September, 2016. Formerly Space Asset Protection,
   The NASA Engineering Network (NEN) is accessible only to NASA users.
* (SWEREF-064)

  [Engineering Principles for Information Technology Security (A Baseline for Achieving Security),](https://csrc.nist.gov/publications/detail/sp/800-27/rev-a/archive/2004-06-21 "Click to open in new window")

  NIST SP 800-27, Revision A.
* (SWEREF-065)

  [Security Considerations in the System Development Life Cycle,](http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-64r2.pdf "Click to open in new window")

  NIST SP 800-64 Revision 2.
* (SWEREF-081)

  [NASA Security Program Procedural Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1600&s=1A "Click to open in new window")

  NPR 1600.1A, Office of Protective Services, Effective Date: August 12, 2013, Expiration Date: December 12, 2021
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-087)

  [NASA Security Policy (Revalidated on 4/2/2015 w/Change 1)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1600&s=2E "Click to open in new window")

  NPD 1600.2E, Office of Protective Services, Effective Date: April 28, 2004, Expiration Date: May 28, 2022
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-361)

  [SPACE SYSTEM PROTECTION STANDARD](https://standards.nasa.gov/standard/NASA/NASA-STD-1006 "Click to open in new window")

   NASA-STD-1006A, Approved 7/15/2022,  PUBLIC: Upload Publicly Available Standard
  https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/2022-07-15-NASA-STD-1006A-Approved.pdf
* (SWEREF-362)

  [Project Protection Plan (PPP) Template,](https://nen.nasa.gov/documents/777837/6986400/MRPP+Project+Protection+Plan+%28PPP%29+Template+2023-01-23.docx/888e52c0-e1bb-4d8d-b7fb-6c1ff9ba726a?t=1674492071311 "Click to open in new window")

  Mission Resilience and Protection key document,  Available in NEN, Mission Resilience and Protection Community of Practice. Formerly "Space Asset Protection", Updated Jan 23, 2023
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-470)

  [NASA Space Flight Program and Project Management Handbook,](https://www.nasa.gov/offices/oce/home/feature_proj_prog_handbook.html "Click to open in new window")

  NASA/SP-2014-3705, NASA, September, 2014.
* (SWEREF-472)

  [Report Concerning Space Data System Standards, (Revised) Security Threats Against Space Missions,](https://public.ccsds.org/Pubs/350x1g2.pdf "Click to open in new window")

  Green Book, Issue 2, CCSDS 350.1-G-2, Consultative Committee for Space Data Systems (CCSDS), December 2015. From site: https://public.ccsds.org/publications/greenbooks.aspx.
* (SWEREF-473)

  [Threats to United States Space Capabilities.](http://fas.org/spp/eprint/article05.html "Click to open in new window")

  Wilson, Tom, Space Commission Staff Member. Prepared for the Commission to Assess United States National Security Space Management and Organization.Retrieved 12:15 PM August 5, 2015 from http://fas.org/spp/eprint/article05.html.
* (SWEREF-589)

  [Verify That Test Equipment Cannot be Interrupted by Extraneous Computer Processes](https://llis.nasa.gov/lesson/8501 "Click to open in new window")

  Public Lessons Learned Entry: 8501.
* (SWEREF-590)

  [International Space Station (ISS) Program/Computer Hardware-Software/Downlink Encryption.](https://llis.nasa.gov/lesson/1148 "Click to open in new window")

  Public Lessons Learned Entry: 1148.
* (SWEREF-591)

  [Computer Hardware-Software/International Space Station/Uplink Encryption.](https://llis.nasa.gov/lesson/1133 "Click to open in new window")

  Public Lessons Learned Entry: 1133.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA Lessons Learned along with their relevance to Requirement 3.11.3. These lessons emphasize principles applicable to mitigating software cybersecurity risks and ensuring robust security strategies for both flight and ground systems. Additional explanations are provided to tie each lesson to its application in software security practices.

### **Lesson 1: Verify That Test Equipment Cannot Be Interrupted by Extraneous Computer Processes**

**Lesson Number**: 8501  
**Summary**:  
Many test facility computers use general-purpose systems configured for multiple roles beyond testing, such as running office functions. Extraneous processes (e.g., code updates, file backups, email downloads, security scans) can interrupt test executions without operator knowledge, especially if these systems are connected to institutional networks. Such interruptions can lead to significant test time loss or, worse, damage to the test article or support equipment.

**Connection to Requirement 3.11.3**:

* **Risk**: Lack of isolation in test systems can introduce vulnerabilities, allowing extraneous network traffic or unintentionally malicious background tasks to disrupt critical testing activities.
* **Mitigation Insight**:
  + Apply strict **segmentation** and isolation for test equipment networks and software environments to prevent interruptions.
  + Use **dedicated hardware and software** for testing, separate from general-purpose or office networks.
  + Disable or schedule background processes (like updates, backups, or scans) during off-hours when testing is not conducted.
* **Alignment with 3.11.3**:
  + Ensure complete **assessment and mitigation planning** for vulnerabilities in test systems during software development and integration. Interruptions in critical test phases could result in missed opportunities to detect cybersecurity risks before deployment.

**Actionable Recommendations for Software Security**:

* Include **test-system isolation** in the **Project Protection Plan (PPP)** as a mitigation strategy to avoid system interruptions during verification and validation phases.
* Implement **cyber-hardening** measures to ensure that extraneous data flows or background applications cannot interfere with critical ground test operations.
* Enable monitoring to detect processes that may unintentionally disrupt testing.

### **Lesson 2: International Space Station (ISS) Program/Computer Hardware-Software/Downlink Encryption**

**Lesson Number**: 1148  
**Summary**:  
NASA improved ISS communication security by adopting a more robust encryption scheme for downlink transmissions, enhancing the protection of sensitive data shared between the ISS systems and ground stations.

**Connection to Requirement 3.11.3**:

* **Risk**: Insufficient encryption of flight and ground communication channels could lead to unauthorized access, data interception, or manipulation of sensitive mission telemetry and data.
* **Mitigation Insight**:
  + Upgrade to **modern, robust encryption protocols** (e.g., AES-256 or stronger) to protect data integrity and confidentiality during transmission.
  + Periodically reevaluate encryption schemes as technology evolves to ensure continued protection against computational advancements that may render older algorithms outdated or vulnerable.
* **Alignment with 3.11.3**:
  + Identify communication paths between flight and ground systems as critical elements within threat assessments.
  + Plan for encryption schemes within the PPP’s mitigation strategies, leading to secure transmissions.

**Actionable Recommendations for Software Security**:

* Incorporate **end-to-end encryption** into all communication paths between flight and ground software systems.
* Use secure key management strategies (e.g., distribute encryption keys via secure, authenticated channels) to prevent unauthorized access.
* Test and validate encryption schemes as part of the **verification and validation** of all cybersecurity mitigations.
* Regularly review encryption effectiveness and prepare mitigations for evolving threats, including post-quantum cryptographic risks.

### **Lesson 3: Computer Hardware-Software/International Space Station/Uplink Encryption**

**Lesson Number**: 1133  
**Summary**:  
The use of outdated encryption algorithms, such as the Data Encryption Standard (DES), has proven insufficient for protecting the ISS uplink. The vulnerability of DES highlights the need to continuously evolve and upgrade encryption methods as older standards are compromised.

**Connection to Requirement 3.11.3**:

* **Risk**: Over-reliance on deprecated or weak encryption standards exposes uplinks to unauthorized command injection or data tampering. Legacy systems still in operation may be particularly vulnerable.
* **Mitigation Insight**:
  + Engage in **continuous encryption updates** to strengthen resistance against modern attacks.
  + Replace outdated algorithms, like DES, with stronger cryptographic mechanisms, such as Advanced Encryption Standard (AES) or Elliptic Curve Cryptography (ECC).
* **Alignment with 3.11.3**:
  + A key part of identifying risks under Requirement 3.11.3 is ensuring encryption threats (including those stemming from outdated protocols) are captured and mitigated in flight and ground software systems.

**Actionable Recommendations for Software Security**:

* **Modernize legacy encryption protocols** during software upgrades or when mitigating cybersecurity risks. Protect communication channels (e.g., uplinks, command paths) with strong, approved encryption standards.
* Evaluate the **compatibility** of encrypted commands and telemetry with mission-critical hardware and ensure software interfaces can support updated cryptographic libraries.
* Periodically assess the cryptographic strength of the security algorithms through regular **threat modeling and testing**, updating the Project Protection Plan to reflect new mitigations as needed.

### **Additional Lessons Learned Related to Software Security**

#### **Lesson 4: Inadequate Input Validation Can Cause Critical Software Failures**

**Hypothetical Contributor to Small Projects** (Inspired by known recommendations):

* **Risk**: Failure to validate and sanitize inputs from ground systems, interfaces, or external communication channels can leave flight software vulnerable to injection attacks, buffer overflows, or system crashes.
* **Mitigation Insight**:
  + Implement **input validation** in all critical software modules by adopting secure coding principles and frameworks.
  + Use robust **static analysis tools** to detect and prevent uncontrolled data entry points.
* **Alignment with 3.11.3**:
  + Ensure that secure input handling is incorporated into the **development process** and reflected in the protection strategies outlined in the PPP.

### **General Takeaways from Lessons Learned**

1. **Continuous Monitoring and Updates**:

   * Cybersecurity threats constantly evolve; plan for iterative updates to both encryption schemes (Lesson 3) and test environments (Lesson 1).
   * This requires continual contributions from the system's ISSO and updates to the Project Protection Plan even after project deployment.
2. **End-to-End Communication and Data Protection**:

   * Encrypt critical software-driven communication paths to reduce risks associated with data theft or manipulation (Lessons 2 and 3).
3. **Early Risk Identification and Mitigation Planning**:

   * Many high-impact vulnerabilities (e.g., unvalidated inputs, unplanned processes, outdated encryption) can be caught early in the project lifecycle through proactive threat modeling and assessments (aligned with Requirement 3.11.3).
4. **Proactive Implementation of Robust Mitigations**:

   * Ensure software engineering teams adopt secure coding standards, modern cryptographic frameworks, and reliable configuration management practices to safeguard flight and ground systems.

### **Concluding Note: Integration into 3.11.3**

The lessons learned above reinforce the importance of a **holistic approach to software security** where both flight and ground systems are considered during risk assessments and mitigations are planned early. By prioritizing encryption, test process isolation, and continuous monitoring of vulnerabilities, small or large projects can meet Requirement 3.11.3's intent to protect mission-critical assets. Incorporating these lessons into a Project Protection Plan and associated software processes will ensure vulnerabilities are addressed systematically throughout the software development lifecycle.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Include funding for appropriate tools to ensure IT security](https://software.gsfc.nasa.gov/lesson-details/48/). **Lesson Number 48**: The recommendation states: "The project budget should include funding for appropriate tools to ensure IT security."

# 7. Software Assurance

**SWE-154 - Identify Security Risks**

3.11.3 The project manager shall identify cybersecurity risks, along with their mitigations, in flight and ground software systems and plan the mitigations for these systems.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that cybersecurity risks, along with their mitigations, are identified and managed.

Also, Software Assurance may need to review the PPP, SSP, and other products that affect the software system.

## 7.2 Software Assurance Products

**Updated Products:**  
Software Assurance plays a critical role in ensuring that cybersecurity risks are addressed throughout the lifecycle. The following are products that Software Assurance activities should produce, deliver, or assess for this requirement:

#### **Key Software Assurance Products**:

1. **Cybersecurity Risks List:**

   * A consolidated list resulting from assessments across each lifecycle phase.
   * Ensure this list aligns with project risk-management practices under NPR 8000.4 and includes:
     + Risk severity (e.g., high/critical, moderate, low).
     + Status (open, closed, mitigated).
     + Associated mitigations (whether planned or implemented).
2. **Software Risk and Vulnerabilities Assessment Report:**

   * A detailed report documenting identified risks to flight and ground software systems and the corresponding vulnerabilities.
   * Include categories such as:
     + Design flaws (e.g., improper architecture choices leading to security gaps).
     + Implementation errors (e.g., memory safety bugs).
     + Operational risks (e.g., inadvertent misconfigurations).
     + Development process risks (e.g., lack of secure coding standards).
   * Track input data from threat assessments, SBOM analyses, automated tools (e.g., static analysis), and ISSO risk summaries.
3. **Software Cybersecurity Test and Validation Plan:**

   * A test plan that validates mitigations for identified software defects with security ramifications.
   * Include:
     + Correspondence between mitigation strategies and specific test procedures.
     + Identification of test tools (e.g., vulnerability scanning, penetration testing).
     + Verification steps for secure coding guidelines applied to the software implementation.
4. **Mitigation Traceability Matrix:**

   * A matrix linking each identified cybersecurity risk to its mitigation plan, associated validation steps, and test results.
   * Ensure traceability to the **Project Protection Plan (PPP)** and **System Security Plan (SSP)**.
5. **Periodic Status Reports with Cybersecurity Metric Analysis:**

   * Summarize the state of cybersecurity risks and their mitigations across lifecycle phases.
   * Highlight trend metrics (upward, downward, stagnant) and areas requiring heightened attention.

## 7.3 Metrics

Metrics are essential for tracking the identification, management, and mitigation of cybersecurity risks. This section enhances the provided metrics by adding more specific categories and examples tailored to lifecycle assurance needs.

#### **Updated Metrics**:

| **Metric** | **Purpose** |
| --- | --- |
| **# of Risks identified in each lifecycle phase** | Understand risk identification during requirements, design, implementation, and testing phases. |
| **# of Risks by Severity** | Categorize risks by severity level (e.g., red/critical, yellow/moderate, green/low) to prioritize effort. |
| **# of Risks with Mitigation Plans vs. Total # of Risks** | Measure how many identified risks have documented mitigation strategies. |
| **# of Risks trending up over time** | Track emerging risks to evaluate whether additional security assessments or updates are needed. |
| **# of Risks trending down over time** | Assess the effectiveness of mitigation efforts. |
| **# of Cybersecurity Risks identified (Open, Closed, Severity)** | Track cybersecurity-specific vulnerabilities across lifecycle phases. |
| **# of Cybersecurity Risks with Mitigations vs. # of Risks identified** | Ensure mitigation coverage by tracking cybersecurity risks explicitly addressed vs. total risks. |
| **# of Cybersecurity mitigation implementations identified** | Monitor mitigations completed based on security vulnerabilities and weaknesses. |
| **# of Cybersecurity mitigation implementations with associated test procedures vs. total mitigations** | Measure the robustness of mitigation efforts validated by testing activities. |

---

#### **Additional Metrics for Small Projects**:

For small projects, simpler, scaled-down metrics may be appropriate:

1. **# of Critical Risks Addressed**:
   * Focus specifically on high-impact risks and their resolution.
2. **Time-to-Mitigation**:
   * Measure how quickly cybersecurity vulnerabilities are mitigated from identification to implementation.
3. **# of Test Procedures Passed vs. Failed for Security Controls**:
   * Ensure test effectiveness and highlight problematic areas requiring rework.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

#### **Assurance Activities to Support Requirement 3.11.3**:

1. **Assure Cybersecurity Risks Are Identified and Mitigated**:

   * Provide oversight and review to ensure:
     + The cybersecurity risks list is comprehensive and reflects input from threat analyses, static/dynamic code analysis, vulnerability testing outputs, and ISSO reviews.
     + Mitigation strategies are documented and implemented in line with NASA policies.
2. **Coordinate with System Security Personnel**:

   * Collaborate with the ISSO and protection planning teams to review:
     + Threat summaries.
     + System susceptibility analyses.
     + Fused risk models that connect software vulnerabilities with broader system threats.
3. **Include Cybersecurity in Lifecycle Reviews**:

   * Verify that cybersecurity risks and mitigations are included as agenda items in major milestone reviews (e.g., SDR, PDR, CDR, ORR, MRR/FRR).
   * Ensure reviewers validate all mitigation implementations before transitioning to the next lifecycle phase.
4. **Validate Mitigation Effectiveness**:

   * Confirm that software cybersecurity mitigations:
     + Are implemented correctly and address the identified risks.
     + Have been subjected to testing during verification and validation phases (e.g., penetration tests, disaster recovery simulations).
5. **Monitor Metrics Regularly**:

   * Track metrics over time to detect trends:
     + Rising risks may signal insufficient early identification efforts or increasing system complexity requiring additional mitigations.
     + Decreasing risks demonstrate effective mitigation planning and implementation.

#### **Suggested Tools and Practices**:

* **Static Analysis Tools** (e.g., SonarQube, OWASP Dependency-Check):
  + Use to detect common vulnerabilities (e.g., buffer overflows, hardcoded credentials).
* **Dynamic Testing Tools**:
  + Validate mitigations and security measures during runtime (e.g., memory corruption protections, exception handling logic).
* **Simple Risk Tracking Mechanism**:
  + For smaller projects, use spreadsheets or lightweight tools (e.g., Jira, Trello) to track risks and mitigations.

### **Supporting Resources**

1. **NASA Software Assurance Guidance**:

   * SWE-156: Evaluate Systems for Security Risks.
   * SWE-159: Verify and Validate Risk Mitigations.
   * Topic 8.18: Software Assurance Suggested Metrics.
2. **System Security Plan Guidance**:

   * Refer to NPR 2810.1 for definitions of SSP and its input into cybersecurity risk management processes.
3. **NASA Resources**:

   * **Software Security Page on NASA NEN**:
     + Provides templates, tools, and guidance for identifying and mitigating software-related cybersecurity risks.

### **Summary: Practical Software Assurance Steps**

1. **Ensure Comprehensive Risk Assessment**:
   * Validate all cybersecurity risks identified at key lifecycle phases.
2. **Track Mitigations in Real-Time**:
   * Use updated metrics to monitor mitigation progress.
3. **Review and Validate Mitigation Effectiveness**:
   * Test mitigations and ensure they reduce vulnerabilities effectively.
4. **Collaborate to Align Mitigations with Broader System Security Plans**:
   * Leverage ISSO expertise and resources to ensure consistency between software-specific mitigations and system-level requirements.

By following this improved Software Assurance guidance, teams can ensure that cybersecurity risks and mitigations are not only identified and tracked but actively managed in alignment with Requirement 3.11.3. This approach supports mission success, system survivability, and compliance with NASA's directives on system protection.

See also Topic [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide), and [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software)

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions)        * [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence demonstrates compliance with Requirement 3.11.3 and assures that cybersecurity risks have been identified, mitigations have been planned and implemented, and the system is secure. This evidence can be generated and archived at various stages of the project lifecycle.

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

Below are examples of objective evidence grouped by type and relevance to Requirement 3.11.3:

### **1. Documentation**

These artifacts should exist as records of performed activities, analyses, and plans regarding cybersecurity risks.

#### **a. Threat Identification**

* **Threat Summary Document**:

  + Includes identified software cybersecurity risks (e.g., design flaws, vulnerabilities in reused components).
  + Categorizes risks by likelihood, impact, and severity (e.g., high/critical, moderate, low).
  + Example: A documented risk such as "Potential injection vulnerability in command uplink interface due to insufficient input validation."
* **System Security Plan (SSP)**:

  + Outlines threats and risks related to system-level cybersecurity, including flight and ground components.
  + Evidence of how software risks feed into broader system security concerns.
* **Risk Register**:

  + A living risk log that reflects ongoing updates made to identified cybersecurity risks.
  + Includes risk status (open/closed), mitigations planned/implemented, owners, and associated timelines.

#### **b. Risk Mitigation Planning**

* **Project Protection Plan (PPP)**:

  + Includes cybersecurity risks with associated mitigation strategies for flight software, ground software, and communication links.
  + Evidence of security requirements (e.g., encryption, authentication, intrusion detection) planned to address identified vulnerabilities.
  + Example: A mitigation plan for "command uplink vulnerability" includes AES-256 encryption for uplink commands and penetration testing for validation.
* **Mitigation Traceability Matrix**:

  + Links each cybersecurity risk to:
    - Mitigation activities applied.
    - Verification and validation processes.
    - Associated test procedures and results.

#### **c. Communication Path Mitigation**

* **Encryption Strategy Document**:
  + Outlines cryptographic protocols implemented for securing flight-to-ground communication (e.g., AES-256, TLS).
  + Documents key management processes.
  + Example: Evidence of cryptographic protocols replacing outdated DES encryption.

#### **d. Secure Development Processes**

* **Software Development Plan (SDP)**:

  + Evidence of processes enforcing secure coding standards (CERT Secure Coding Standards, MISRA guidelines, etc.).
  + Includes details about static analysis tools used to identify coding flaws.
* **Static and Dynamic Code Analysis Reports**:

  + Automated tool results identifying coding issues, vulnerabilities, or flaws mitigated during development.
  + Example: A static analysis report detailing no unresolved buffer overflow issues.

### **2. Test Artifacts**

Testing activities provide objective evidence that cybersecurity risks have been identified, mitigated, and validated.

#### **a. Security Test Plan**

* Identifies procedures for validating software cybersecurity mitigations.
* Includes tools, test coverage (e.g., penetration testing, vulnerability scanning), test cases, expected results, and criteria for success.

#### **b. Test Results and Reports**

* **Penetration Testing Report**:

  + Evidence of testing performed on software interfaces, communication links, and data pathways against known vulnerabilities.
  + Includes test findings and demonstrated mitigations (e.g., no successful injection attack during testing).
* **Vulnerability Testing Reports**:

  + Test results from tools like **OWASP ZAP, Nessus Essentials**, or **SonarQube**, showing elimination of identified vulnerabilities.
* **End-to-End Encryption Testing**:

  + Evidence of successfully encrypted command/data during transmission and receipt.

#### **c. Validation Evidence**

* **Secure Software Validation Report**:

  + Verifies that mitigations (e.g., secure coding practices, access control mechanisms) have been implemented and function as intended.
  + Includes validation results for flight/ground software cybersecurity measures.
* **Test Procedure Coverage Matrix**:

  + Demonstrates that all cybersecurity mitigations outlined in the mitigation traceability matrix are linked to specific test procedures and verified.

### **3. Metrics and Performance Data**

Metrics track the identification, status, and progress of cybersecurity risk mitigation over time.

#### **Key Metrics**:

1. **Risks Identified by Life Cycle Phase**:

   * Number of cybersecurity risks identified during requirements, design, implementation, validation, and operations.
   * Evidence: Trend charts showing progress in closing cybersecurity risks across lifecycle phases.
2. **Mitigation Coverage**:

   * Ratio of mitigations implemented vs. cybersecurity risks identified.
   * Evidence: A periodic security metrics status report showing 95% of cybersecurity risks mitigated before Final Design Review (FDR).
3. **Test Coverage Metrics**:

   * Number of test procedures created and executed for cybersecurity mitigations vs. mitigations identified.
   * Evidence: A report showing 100% alignment between test cases and mitigations.
4. **Risk Severity Trends**:

   * Evidence of how risks are trending upward or downward over time (e.g., showing reduced critical risks after implementing mitigations).

### **4. Compliance Evidence**

NASA policies and standards provide expectations for performing cybersecurity risk management. Evidence of adherence indicates compliance with requirements.

#### **Compliance Standards**:

1. **NPR 2810.1**: Security of Information and Information Systems.

   * Auditable evidence showing compliance with the cybersecurity requirements outlined in system security plans (SSP).
2. **NPR 7120.5**: Systems Engineering Processes and Requirements.

   * Evidence demonstrating updates to the PPP (preliminary, baseline, and incremental updates).
3. **NASA STD-1006**: Space System Protection Standard.

   * Evidence showing that software risks contribute to system-level threat analysis, mitigations, and survivability planning.

### **5. Collaboration and Review Evidence**

Software Assurance personnel and project teams must collaborate during lifecycle reviews and risk management activities. The following are examples of evidence from collaborative activities:

1. **Review Records**:

   * Minutes from preliminary design reviews (PDR), critical design reviews (CDR), and operational readiness reviews (ORR) showing that cybersecurity risks were discussed and approved as part of the lifecycle process.
2. **ISSOs Collaboration Evidence**:

   * Documented inputs from the Information System Security Officer (ISSO) during threat assessments, test plan development, and verification activities.

### **6. NASA Lessons Learned Application**

Referencing lessons learned provides evidence that the project team incorporated historical knowledge into the cybersecurity risk assessment process:

1. **Lesson Number 8501**:

   * Evidence: Test computer processes were isolated from extraneous institutional network tasks (e.g., operating system updates, email functionality manually disabled during testing).
2. **Lesson Number 1133**:

   * Evidence: Transition from outdated DES encryption to AES-256 for uplink command protection.

### **7. Archivable Objective Evidence Artifacts**

These items demonstrate that Requirement 3.11.3 was actively addressed and help future efforts with traceability and auditability:

1. **Updated Threat Summary**: Includes all identified cybersecurity risks, mitigations, and statuses.
2. **Validated Test Results**: Reports and logs of security measures tested and passed.
3. **Meeting Minutes**: Records showing mitigation plans were discussed and approved during milestone reviews.
4. **Periodic Cybersecurity Status Reports**: Metrics tracking mitigation effectiveness over time (monthly/quarterly updates).

By generating and maintaining these types of objective evidence, teams can document compliance with Requirement 3.11.3, demonstrate accountability, promote secure software development practices, and safeguard mission-critical flight and ground systems.
