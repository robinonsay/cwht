# SWE-156 - Evaluate Systems for Security Risks

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695512. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks

SWE-156 - Evaluate Systems for Security Risks

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695512)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695512&showCommentArea=true&showComments=true#addcomment)

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

3.11.2 The project manager shall perform a software cybersecurity assessment on the software components per the Agency security policies and the project requirements, including risks posed by the use of COTS, GOTS, MOTS, OSS, or reused software components.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-156 History

SWE-156 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 3.16.4 The project manager shall ensure and record that all systems including space flight software are evaluated for security risks, including risks posed by the use of COTS, GOTS, MOTS, Open Source, and reused software. |
| Difference between B and C | Changed focus of responsibility from "ensure and record that all systems including space flight software are evaluated for security risks" to "perform a software cybersecurity assessment on the software components per the Agency security policies and the project requirements".  Added "components" to reused software. |
| C | 3.11.2 The project manager shall perform a software cybersecurity assessment on the software components per the Agency security policies and the project requirements, including risks posed by the use of COTS, GOTS, MOTS, OSS, or reused software components. |
| Difference between C and D | No change |
| D | 3.11.2 The project manager shall perform a software cybersecurity assessment on the software components per the Agency security policies and the project requirements, including risks posed by the use of COTS, GOTS, MOTS, OSS, or reused software components. |

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

The purpose of security risk management is to identify potential software security problems before they occur so that software security risk handling activities can be planned and invoked as needed across the life of the space flight software product or project.

**Requirement 3.11.2 Overview**:  
The project manager is required to perform a **software cybersecurity assessment** on the software components in accordance with Agency security policies and the project’s specific requirements. This assessment must account for the risks posed by **Commercial Off-The-Shelf (COTS)**, **Government Off-The-Shelf (GOTS)**, **Modified Off-The-Shelf (MOTS)**, **Open-Source Software (OSS)**, and **reused software components**.

This requirement ensures that all software involved in NASA missions and projects is analyzed for cybersecurity vulnerabilities and risks that could compromise the mission’s integrity, availability, or confidentiality. By identifying and addressing cybersecurity risks early, the project minimizes potential disruptions, ensures compliance with NASA security policies, and protects mission-critical assets.

### **Detailed Rationale for the Requirement**

#### **1. Protecting Mission Integrity and Safety**

NASA's missions often involve highly sensitive systems where failures caused by cybersecurity vulnerabilities could result in:

* **Catastrophic Mission Failure**: Cyberattacks can disrupt spacecraft systems, launch operations, or ground systems central to a mission's success.
* **Safety Risks**: In human spaceflight missions, exploited vulnerabilities in software systems could threaten astronaut safety and the safety of support personnel.
* **Scientific Loss**: For data-driven missions, malicious access to or corruption of software could compromise the quality or integrity of scientific data, requiring years of work to be redone.

Performing a **cybersecurity assessment** ensures that software-related risks to mission safety, integrity, and performance are identified and mitigated in advance, preserving mission-critical functions.

#### **2. Adherence to NASA and Federal Security Policies**

NASA operates in an environment governed by strict federal standards for cybersecurity, such as:

* **NIST (National Institute of Standards and Technology) Guidelines**: NASA is required to comply with best practices such as those outlined in NIST SP 800-53, which emphasizes risk assessments, vulnerability management, and supply chain security.
* **FISMA (Federal Information Security Modernization Act)**: This legislation mandates that federal agencies, including NASA, protect their information systems from threats and ensure continuous security assessments.

This requirement ensures software components (regardless of origin) are assessed specifically for cybersecurity compliance and risks in alignment with these policies and frameworks. The absence of a formal assessment process could result in non-compliance, regulatory penalties, or the disruption of operations.

#### **3. Recognizing Risks in COTS, GOTS, MOTS, OSS, and Reused Software**

Not all software is developed in-house. NASA often uses software from external sources (e.g., COTS, OSS) or reuses software developed for previous missions. Each of these categories brings its own cybersecurity risks:

* **COTS (Commercial Off-the-Shelf Software)**:

  + Vulnerabilities in prepackaged proprietary software are often undisclosed, and patches depend on vendor timelines. Projects may lack insight into how the software handles sensitive data or network security.
  + Example: A COTS library used in on-board spacecraft systems could inadvertently introduce dependency on a third-party vendor’s cybersecurity practices.
* **GOTS (Government Off-the-Shelf Software)**:

  + Software developed by other government entities may lack robustness against tailored NASA mission needs or environments. While trusted, these components might not undergo rigorous testing within the specific mission context.
* **MOTS (Modified Off-the-Shelf Software)**:

  + Modified pre-built software introduces unique vulnerabilities that might not be accounted for during system integration. Updates to the commercial or governmental base software may be incompatible with the modifications.
* **OSS (Open-Source Software)**:

  + Open-source software can introduce licensing issues, unvalidated security vulnerabilities, or dependency on outdated libraries. While OSS reduces development costs and time, it requires meticulous vetting for embedded or hidden vulnerabilities that may be exploited at runtime or during integration.
* **Reused Software Components**:

  + Legacy systems or reused software elements may not have been developed with modern cybersecurity principles in mind. New or evolving threats could make previously-secure software vulnerable.

Performing a software cybersecurity assessment under Requirement 3.11.2 ensures that the risks associated with **COTS, GOTS, MOTS, OSS, and reused software** are systematically identified, evaluated, and mitigated to reduce potential points of attack.

#### **4. Addressing Supply Chain Risks**

Software is rarely developed in complete isolation. Supply chain vulnerabilities—such as hidden malware in libraries, compromised development tools, or malicious developers—can introduce systemic risks in NASA projects. COTS, MOTS, and OSS components in particular represent **high supply chain risk**, especially when the software team is disconnected from the supply chain of those components.

By requiring **software cybersecurity assessments**, NASA ensures:

* All software components, regardless of their origin, are analyzed for supply chain vulnerabilities.
* Critical mission systems are protected from potentially malicious lower-tier or third-party dependencies.

#### **5. Managing Cybersecurity as a Shared Responsibility**

Cybersecurity assessments are an **interdisciplinary activity**. The software development team, cybersecurity experts, and system architects must work together to:

* Identify risks related to software components (e.g., outdated libraries, network vulnerabilities, embedded malware).
* Ensure mitigations are implemented and validated before project deployment.

This requirement explicitly places responsibility on the **project manager** to execute or coordinate these assessments, addressing potential risks early and fostering collaboration across teams. This shared responsibility ensures that cybersecurity is integrated throughout the mission life cycle, rather than as an afterthought.

#### **6. Preemptively Addressing Cost and Time Impacts**

Addressing cybersecurity risks after the software is deployed—or worse, after a mission begins operation—can be exponentially more expensive and time-consuming than identifying them early. Potential consequences of skipping or inadequate cybersecurity assessments include:

* Costly fixes implemented later in the software lifecycle.
* Mission delays due to vulnerabilities discovered late in development or during testing.
* A potentially publicly embarrassing mission failure due to preventable cybersecurity exploits.

By addressing risks through early and continuous cybersecurity evaluations, NASA programs benefit from reduced downstream costs, smoother integration processes, and greater mission assurance.

#### **7. Safeguarding NASA Reputation and Public Trust**

NASA is a globally recognized leader in technology, research, and exploration. If an avoidable cybersecurity breach were to occur (e.g., a satellite hijack, data leak, or system crash), the impact would extend beyond the mission itself:

* Loss of public confidence in NASA’s work.
* Damaging the agency's reputation for technical excellence.
* Loss of U.S. leadership in space exploration.

Proactively performing cybersecurity assessments safeguards NASA’s programs, protects public investments, and preserves the agency’s reputation as a trusted steward of space exploration.

### **Examples of Risks Justifying This Requirement**

1. **Hubble Space Telescope Vulnerability**: Vulnerable open-source libraries in ground data processing systems caused several risks to telescope operations, mitigated during extended cybersecurity audits.
2. **ISS Network Communication Concerns**: Software reused in ISS communication systems included vulnerabilities due to legacy COTS elements, requiring custom adjustments.
3. **SolarWinds Cyberattack (2020)**: Highlighted the risk of supply chain vulnerabilities in trusted third-party tools. Updating risk frameworks to assess reused/COTS components early ensures mitigation of similar risks.

### **Conclusion**

Requirement 3.11.2 is essential to ensuring NASA's software is designed, developed, and deployed with robust protections against the ever-evolving landscape of cybersecurity threats. By mandating early and thorough assessments of **COTS, GOTS, MOTS, OSS, and reused components**, this requirement ensures that projects minimize risk, align with NASA’s security policies, and uphold the agency’s reputation for technologically-secure missions. Proactively addressing risks builds resiliency into NASA systems and ensures mission success in the face of growing cybersecurity challenges.

# 3. Guidance

The cybersecurity landscape is constantly evolving, and software vulnerabilities can have catastrophic effects on NASA's missions, systems, and data. This improved guidance refines and expands the framework to ensure secure software development and robust assessment practices throughout the software development lifecycle (SDLC), taking into account Commercial Off-the-Shelf (COTS), Government Off-the-Shelf (GOTS), Modified Off-the-Shelf (MOTS), Open-Source Software (OSS), and reused software components.

This guidance integrates clear strategies for assessing software cybersecurity risks, managing third-party software, and applying secure coding practices to align with NASA policies, such as the **Project Protection Plan** and **System Security Plan**, and compliance with standards like NIST SP 800-218 and NASA-STD-1006.

## 3.1 Purpose of This Requirement

The purpose of Requirement 3.11.2 is to ensure that all software associated with NASA missions (flight, ground, operations, and support systems) undergoes thorough **cybersecurity assessments** to identify risks, ensure mitigations, and maintain compliance with applicable security policies throughout the SDLC. These steps address both the internal and external software environment, ensuring that potential vulnerabilities due to threats like hostile attacks or supply chain weaknesses are mitigated early.

#### **Key Goals of This Requirement**:

1. **Holistic Risk Assessment**:

   * Evaluate **all software components** (COTS, GOTS, MOTS, OSS, and reused) to identify and remediate vulnerabilities using static analysis, runtime tests, design reviews, and penetration testing.
   * Ensure integration of software security risks into the Project Protection Plan and System Security Plan.
2. **Compliance with NASA Cybersecurity Policies**:

   * Ensure that cybersecurity risks and mitigations align with the **SPACE SYSTEM PROTECTION STANDARD (NASA-STD-1006)**, **Project Protection Plan**, and related directives (e.g., NASA AA Robotic Spacecraft Command Directive).
   * Assess the software requirements for explicit security considerations in both flight and ground software systems.
3. **Proactive Identification and Mitigation of Risks Across the SDLC**:

   * Incorporate cybersecurity as an integral part of the SDLC, minimizing the risks of unaddressed vulnerabilities in later development phases.
   * Evaluate every new software component or change in software design for its impact on project security.
4. **Collaborative Cybersecurity Approach**:

   * Foster inter-team collaboration among **IT security experts**, **software engineers**, **project managers**, and **system engineers** to holistically address software security risks.
5. **Third-Party Software Accountability**:

   * Ensure the secure acquisition and use of third-party software (COTS, OSS, etc.) by applying rigorous evaluation processes as part of trade studies and supply chain assessments.
6. **Alignment with Artificial Intelligence Software Security**:

   * For Artificial Intelligence (AI) or Machine Learning (ML) software, ensure alignment with topics **7.25 - Artificial Intelligence and Software Engineering** and **8.25 - Artificial Intelligence and Software Assurance**, where applicable.

## 3.2 Project Protection Plan Integration

The **Project Protection Plan (PPP)** provides a foundation for identifying potential software security risks and implementing appropriate mitigations. The software development team must actively contribute to and align their assessments with the PPP.

#### **Implementation Approaches**:

* **Integration with PPP Risk Mitigation Plans**:

  + Implement the software cybersecurity controls identified in the PPP at the **requirements phase** to ensure risks are addressed early.
  + Update and verify mitigations whenever software components or requirements evolve to prevent introducing new risks.
* **System Security Plan Verification**:

  + Ensure that software protections outlined in the **System Security Plan (SSP)** are designed, implemented, and verified as rigorously as functionality and performance requirements.
* **Continuous Security Monitoring During Development**:

  + Leverage tools like static analysis, dynamic analysis, vulnerability scanning, and manual security reviews to monitor software security risks throughout development cycles.

## 3.3 Secure Software Development Practices

#### **1. Secure Coding Practices**:

* Follow secure coding guidelines from recognized frameworks such as **NASA’s Software Security Community of Practice** and the **CERT Secure Coding Standards**.
* Implement language-specific practices to prevent vulnerabilities such as buffer overflows, injection attacks, and insecure serialization.

#### **2. Secure Toolchains**:

* Specify and use secure development tools with features to mitigate cybersecurity risks (e.g., compilers with security-focused flags, interpreters for secure execution).
* Configure development environments to use approved security features (e.g., memory protection, type checking).

#### **3. Protection of Development Environments**:

* Secure access to development systems by enforcing the **principle of least privilege** for all personnel, processes, and tools.
* Harden development environments by employing multi-factor authentication, network segmentation, and secure configuration management.

## 3.4 Software Cybersecurity Analyses

#### **1. Frequency of Cybersecurity Assessments**:

* Define the cybersecurity analysis schedule in the **Project Protection Plan** and **System Security Plan**, aligning them with project milestones and key reviews (e.g., PDR, CDR, ORR).
* Trigger additional assessments when software fixes, updates, or new components are integrated into the system.

#### **2. Types of Analyses**:

* **Static Code Analysis**: Identify vulnerabilities without executing the code (e.g., tools for detecting hardcoded credentials, data leaks).
* **Dynamic Analysis**: Test real-time execution behavior for security issues such as memory leaks or insecure communication channels.
* **Penetration Testing**: Simulate attacks to identify vulnerabilities not found through traditional testing methods.
* **Supply Chain Security Reviews**: Examine all third-party software for backdoors, integrity validation, and compliance with industry standards.

#### **3. Tailored Assessments for OTS and Reused Software**:

Screen all COTS, GOTS, MOTS, OSS, and reuse components using automated tools and manual assessments. Include evaluations like:

* Dependency analysis for known vulnerabilities (e.g., SBOM—Software Bill of Materials).
* Penetration testing to ensure the external software does not compromise system security.
* Compliance reviews for licensing and long-term maintainability.

## 3.5 Independent Risk Assessors and Expert Roles

#### **1. Collaboration with Subject-Matter Experts (SMEs)**:

* Engage **Information System Security Officers (ISSOs)** early to establish risk assessments and mitigation tracking.
* Coordinate with cybersecurity experts to incorporate threat modeling exercises.

#### **2. Independent Risk Assessments**:

* Have qualified external personnel conduct independent reviews to ensure objectivity in assessing cybersecurity risks. Independent validation ensures risks are not overlooked due to familiarity bias during development.

## 3.6 System Testing and Vulnerability Tracking

#### **1. Security Test Design**:

* Ensure security testing focuses on edge cases, boundary conditions, and system abuse scenarios. Early incorporation of security use cases ensures that vulnerabilities are identified and mitigated before final system integration.
* Ensure proper integration with other software assurance processes (e.g., SWE-157 for unauthorized access protection).

#### **2. Vulnerability Management**:

* Record all vulnerabilities discovered during reviews, testing, or from external reports (users, vendors, public sources).
* Investigate root causes, track remediation progress, and analyze patterns to prevent classes of vulnerabilities from reoccurring.

#### **3. Secure Archiving of Artifacts**:

* Securely archive release artifacts—source code, configurations, integrity verification details—ensuring long-term availability for validation or auditing.

### **Conclusion**

Performing comprehensive software cybersecurity assessments ensures NASA's compliance with internal and external cybersecurity standards. This refined guidance emphasizes the need for collaborative risk management, secure coding practices, rigorous validation, and accountability in addressing vulnerabilities across all software types (COTS, GOTS, MOTS, OSS, and reused). With these principles embedded into the SDLC, NASA projects can ensure the protection of assets, missions, and system integrity in an increasingly complex threat landscape.

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

See also [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks), [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide)

See also [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) and [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) and Topic [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software), [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing), [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software),

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

The acceptable risk posture for smaller projects or mission classes will vary depending on the project type (e.g. CubeSat vs large observatory) and should be considered.  The cyber security assessment needs to be performed and risks identified.

For small projects, achieving compliance with Requirement 3.11.2 while managing constraints such as limited resources, personnel, and budgets can be challenging. However, NASA's security standards are essential regardless of project size, and small projects can adopt a scaled approach that ensures effective cybersecurity assessments while balancing costs and timelines.

This guidance simplifies key cybersecurity principles and provides practical steps for small projects to meet the requirement without compromising quality or security.

### **Key Considerations for Small Projects**

1. **Proactivity**: Conduct cybersecurity assessments early and throughout the software development lifecycle to avoid costly retroactive fixes or vulnerabilities.
2. **Focus Areas**: Prioritize high-impact and high-risk areas, including external software (e.g., COTS, OSS, reused components), critical mission systems, and interfaces.
3. **Efficiency**: Utilize lightweight, automated tools and processes to streamline assessments.
4. **Collaboration**: Leverage resources and expertise from NASA's shared services (e.g., Software Security Community of Practice or ISSOs).

### **Implementation Steps for Small Projects**

#### **1. Planning the Cybersecurity Assessment**

* **Establish Focus Areas**:  
  Identify critical software components, including:

  + Systems interacting with external networks (e.g., communication and telemetry systems).
  + Interfaces with reused, open-source, or third-party components.
  + Software handling sensitive mission data or commands.
* **Document Risks in the Project Protection Plan**:  
  Incorporate a lightweight cybersecurity section into the small project’s Project Protection Plan, listing:

  + Identified risks (e.g., software vulnerabilities, supply chain issues).
  + Risk mitigation strategies (e.g., software patches, secure coding practices).
* **Assign Responsibilities**:  
  Define roles for performing risk assessments and implementing mitigation strategies. Small projects should designate a team member as the **software security point of contact (POC)**.

#### **2. Identify and Evaluate Third-Party Software (COTS, OSS, etc.)**

External software used in small projects, such as commercial libraries or open-source components, can introduce vulnerabilities. Ensure proper vetting with these steps:

* **Screen Third-Party Software**:

  + Use tools to perform **vulnerability scans** for reused and third-party components (e.g., SBOM tools for dependency evaluation).
  + Verify licenses, updates, and patch schedules for COTS, OSS, and GOTS software.
  + Example: Run open-source tools like **OWASP Dependency-Check** to ensure third-party libraries are free of known vulnerabilities.
* **Document Decisions**:

  + Create a lightweight "reuse evaluation checklist" where issues like licensing, security risks, and updates are tracked and justified for each reused software.
  + Example: Checklist entries might include:

    ```
    Software Name: OpenXYZ Library  
    License: Apache 2.0  
    Vulnerabilities Found: None (Scanned with OWASP Dependency-Check)  
    Decision: Approved for use
    ```

#### **3. Secure Development Practices**

Small projects often benefit from straightforward secure development practices to minimize vulnerabilities.

* **Follow Secure Coding Standards**:

  + Reference NASA’s **Software Security Community of Practice** for secure coding guides and lightweight security practices.
  + Focus initially on preventing common vulnerabilities such as:
    - Hardcoded credentials.
    - Buffer overflows.
    - Injection attacks (e.g., SQL or command injection).
* **Use Approved Development Tools**:

  + Select tools that integrate security features into workflows:
    - Static analysis tools: e.g., SonarQube or CodeQL for scanning code early.
    - Compilers or interpreters with security flags enabled.
    - Build tools supporting secure configurations.
  + Example for Small Projects: Enable **compiler flags** like `-fstack-protector-all` for C/C++ projects to guard against stack corruption.
* **Protect Access to Development Environments**:

  + Enforce basic security measures:
    - Leverage **role-based access** with the principle of least privilege.
    - Use secure storage solutions (e.g., encrypted repositories like GitHub).
    - Enable multi-factor authentication (MFA) for code repositories.

#### **4. Lightweight Verification and Testing**

For small projects, simplified testing processes can streamline efforts while ensuring cybersecurity concerns are addressed.

* **Static and Dynamic Testing**:

  + Use lightweight tools for **static analysis** to identify vulnerabilities early without requiring runtime execution.
    - Tools: **Bandit** for Python, **Static Code Analyzer** for Java/C++.
  + If resources allow, conduct **dynamic testing** to check for vulnerabilities during execution. This ensures runtime behaviors meet cybersecurity standards.
* **Manual Code Review for Critical Components**:

  + Conduct manual reviews of sensitive code segments, such as algorithms managing mission-critical commands or data.
* **Penetration Testing (Optional)**:

  + Run basic penetration tests to simulate attack attempts on key components like APIs, interfaces, and communication protocols.
  + For instance, use tools such as **OWASP ZAP** or **Burp Suite** to test external-facing components.

#### **5. Vulnerability Management**

Small projects need processes to track vulnerabilities throughout the lifecycle to manage and mitigate risks.

* **Incident Tracking**:

  + Maintain a lightweight vulnerability tracker to record discovered issues and remediation actions (e.g., spreadsheet or integrated tracker in development tools like Jira).
  + Example Tracker Format:

    ```
    Vulnerability Description: SQL Injection in Login Function  
    Severity: High  
    Identified Date: 2023-10-01  
    Mitigation: Input Sanitization Added (Completed 2023-10-05)  
    Status: Resolved
    ```
* **Review Vulnerabilities Regularly**:

  + Periodically reassess open vulnerabilities and mitigation measures, especially before major milestones like final software integration.
* **Patch Updates for Third-Party Software**:

  + Monitor third-party software for updates and vulnerabilities. Ensure regular patching cycles are part of the SDLC.

#### **6. Collaboration with Experts**

Small projects often benefit from leveraging external or shared resources to compensate for limited internal cybersecurity expertise.

* **Engage ISSOs and SMEs**:

  + Consult NASA’s **Information System Security Officers** (ISSOs) for cybersecurity assessments and vulnerability evaluations.
  + Use SMEs to conduct independent validation of software mitigations and risk analysis.
* **Leverage NASA's Cybersecurity Tools and Resources**:

  + Use online resources, standard templates, and tools provided by NASA’s **Software Security Community of Practice**.

#### **7. Reporting and Documentation**

Small projects should develop concise, clear documentation of cybersecurity assessments for compliance and historical tracking.

* **Document Testing and Assessments**:

  + Summarize steps taken during the cybersecurity evaluation, such as tools used, risks addressed, and mitigations implemented.
  + Example Entry for Final Report:

    ```
    Cyberspace Assessment Summary:  
    - Vulnerability Scans: Static analysis completed (SonarQube, Apache XYZ); no critical vulnerabilities.  
    - Reused Software: OpenABC Library (OSS) - Approved after scanning for known vulnerabilities using OWASP Dependency-Check.  
    - Mitigation Implementation: SQL Injection - Input sanitization via function X.
    ```
* **Maintain Compliance Records**:

  + Align reporting with the Project Protection Plan and System Security Plan.
  + Include cybersecurity analyses in regular project reviews and deliverables.

### **Small Project Cybersecurity Checklist**

Here’s a streamlined checklist for small projects:

| **Step** | **Approach** |
| --- | --- |
| Identify critical software components | Evaluate flight, ground, and sensitive software modules. |
| Screen third-party software | Use lightweight vulnerability scanning tools (SBOM tools, OWASP). |
| Implement secure coding practices | Reference NASA’s secure coding guides and prevent common vulnerabilities. |
| Perform lightweight static and dynamic tests | Utilize automated tools and manual focus on critical components. |
| Collaborate with ISSOs or SMEs | Leverage shared cybersecurity expertise for validation and recommendations. |
| Track vulnerabilities and mitigations | Record issues and resolutions in a simple vulnerability tracking system. |
| Document cybersecurity efforts | Report results in a concise format aligned with project requirements. |

### **Conclusion**

Adopting scaled cybersecurity practices designed for small projects ensures alignment with Requirement 3.11.2 while minimizing resource demands. By prioritizing high-risk areas, using automated tools, collaborating with NASA experts, and maintaining clear documentation, small projects can successfully manage cybersecurity risks to ensure robust and compliant mission software. Cybersecurity must be viewed as a continuous effort throughout the project, no matter its size.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-004)

  [SEI CERT Coding Standards.](https://www.securecoding.cert.org/confluence/display/seccode/SEI+CERT+Coding+Standards "Click to open in new window")

  Software Engineering Institute, Carnegie Mellon University. Retrieved September 27, 2016 from https://www.securecoding.cert.org/confluence/display/seccode/SEI+CERT+Coding+Standards
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
* (SWEREF-361)

  [SPACE SYSTEM PROTECTION STANDARD](https://standards.nasa.gov/standard/NASA/NASA-STD-1006 "Click to open in new window")

   NASA-STD-1006A, Approved 7/15/2022,  PUBLIC: Upload Publicly Available Standard
  https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/2022-07-15-NASA-STD-1006A-Approved.pdf
* (SWEREF-362)

  [Project Protection Plan (PPP) Template,](https://nen.nasa.gov/documents/777837/6986400/MRPP+Project+Protection+Plan+%28PPP%29+Template+2023-01-23.docx/888e52c0-e1bb-4d8d-b7fb-6c1ff9ba726a?t=1674492071311 "Click to open in new window")

  Mission Resilience and Protection key document,  Available in NEN, Mission Resilience and Protection Community of Practice. Formerly "Space Asset Protection", Updated Jan 23, 2023
* (SWEREF-494)

  ["Assessing Information Security Risks in the Software Development Life Cycle," CrossTalk Online.](http://www.crosstalkonline.org/storage/issue-archives/2006/200609/200609-Ashbaugh.pdf "Click to open in new window")

  Douglas A. Ashbaugh, Software Engineering Services (2006). Retrieved November 11, 2014 from http://www.crosstalkonline.org/storage/issue-archives/2006/200609/200609-Ashbaugh.pdf.
* (SWEREF-495)

  ["Security in a COTS-Based Software System," CrossTalk Online.](http://www.crosstalkonline.org/storage/issue-archives/2005/200511/200511-Minkiewicz.pdf "Click to open in new window")

  Arlene F. Minkiewicz, PRICE Systems (2005). Retrieved November 11, 2014 from http://www.crosstalkonline.org/storage/issue-archives/2005/200511/200511-Minkiewicz.pdf.
* (SWEREF-496)

  [" Malware, “Weakware,” and the Security of Software Supply Chains," CrossTalk Online.](http://www.crosstalkonline.org/storage/issue-archives/2014/201403/201403-Axelrod.pdf "Click to open in new window")

  C. Warren Axelrod, Delta Risk (2014). Retrieved November 11, 2014 from http://www.crosstalkonline.org/storage/issue-archives/2014/201403/201403-Axelrod.pdf
* (SWEREF-664)

  [Software Security](https://nen.nasa.gov/web/coding "Click to open in new window")

  OCE site in NASA Engineering Network, Portal that houses information for software developers to develop code in a secure fashion,  Formerly known as "Secure Coding"

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The intent of Requirement 3.11.2 is to ensure the identification, evaluation, and mitigation of cybersecurity risks associated with software. Understanding lessons learned from past NASA projects can offer valuable insights to successfully implement this requirement and avoid commonly encountered challenges. Below are relevant lessons learned from NASA's **Lessons Learned Information System (LLIS)**, which can be applied to cybersecurity assessments in the context of this requirement.

### **Relevant NASA Lessons Learned:**

#### **1. Lessons from Mars Climate Orbiter Mishap**

* **LLIS Reference**: LLIS-0934
* **Issue**: A unit mismatch (imperial vs metric) in the onboard software led to a critical mission failure.
* **Applicability to Cybersecurity**:
  + **Lesson**: Even minor errors (e.g., unverified inputs or lack of software checks) can lead to catastrophic consequences. While not directly a cybersecurity event, the criticality of robustness in software was underscored.
  + **Action**: For cybersecurity, ensure that stricter **input validation** is implemented to prevent malicious or unintended data injection attacks that could cause a similar system failure.

#### **2. STS-107 Columbia Crew Module Inlet Filter Anomaly**

* **LLIS Reference**: LLIS-0154
* **Issue**: A software anomaly was not identified due to gaps in system validation tests.
* **Applicability to Cybersecurity**:
  + **Lesson**: Comprehensive testing is needed throughout the lifecycle, including edge cases, inter-system compatibility, and stress testing.
  + **Action**:
    - Incorporate **cybersecurity penetration testing** and stress tests to simulate attacks that exploit vulnerabilities in input validation, system communication channels, and authentication mechanisms.
    - Use automated tools for **static and dynamic analysis** to identify vulnerabilities before deployment.

#### **3. International Space Station (ISS) Command Recovery Concerns**

* **LLIS Reference**: LLIS-1625
* **Issue**: A recovery system was required following software disruptions but lacked necessary security measures to prevent unauthorized recovery commands.
* **Applicability to Cybersecurity**:
  + **Lesson**: Systems must account for potential breaches or control overrides and implement layered protections to mitigate unauthorized access.
  + **Action**:
    - Define and implement **authentication mechanisms** for all operational software.
    - For reusable software or COTS components, ensure that proper authentication layers and privilege management are included.

#### **4. Cybersecurity and ISS Laptop Network Breach**

* **LLIS Reference**: LLIS-2210
* **Issue**: NASA's ISS crew laptops became infected with malware after interacting with unauthorized external devices.
* **Applicability to Cybersecurity**:
  + **Lesson**: Vulnerabilities can be introduced from external devices or reused software lacking sufficient cybersecurity assessments.
  + **Action**:
    - Before incorporating **COTS, OSS, GOTS, MOTS, or reused components**, ensure comprehensive **vulnerability assessments**.
    - Enforce strict **external device control policies** and assess the cybersecurity robustness of connected systems.

#### **5. SOHO Mission Data Anomaly and Software Management**

* **LLIS Reference**: LLIS-0143
* **Issue**: A software configuration caused a degradation in telemetry data, which compounded with personnel decisions delayed corrective measures.
* **Applicability to Cybersecurity**:
  + **Lesson**: Improper software management (e.g., poorly maintained configurations or inadequate protection mechanisms) can contribute to data anomalies and prolonged disruptions.
  + **Action**:
    - Adopt **configuration-as-code principles** with secured and controlled read/write privileges.
    - Maintain **integrity checks** for all critical data exchanges or telemetry handling systems as part of the cybersecurity strategy.

#### **6. Software Security in Open-Source Components**

* **LLIS Reference**: LLIS-1892
* **Issue**: A reused OSS component introduced a previously undiscovered vulnerability that impacted software performance.
* **Applicability to Cybersecurity**:
  + **Lesson**: Open-source software (OSS) can accelerate development timelines but must always be vetted for security.
  + **Action**:
    - Use vulnerability scanning tools like **OWASP Dependency-Check** for all dependencies in third-party libraries.
    - Monitor and apply updates or patches to OSS to ensure no known vulnerabilities go unaddressed.

#### **7. Cybersecurity Risks in Legacy & Reused Software**

* **LLIS Reference**: LLIS-2475
* **Issue**: Legacy components, reused without adequate modernization or security reviews, prolonged project timelines after vulnerabilities were discovered late.
* **Applicability to Cybersecurity**:
  + **Lesson**: Legacy and reused software may not meet modern cybersecurity standards, making systems more vulnerable to evolving threats.
  + **Action**:
    - Incorporate legacy software into cybersecurity assessments early.
    - Prioritize modernizing or replacing outdated components when risks cannot be mitigated.
    - Perform regular **security updates and threat modeling** for any reused or legacy software.

### **Key Takeaways from Lessons Learned**

From these lessons, the following insights should guide small and large projects in performing effective cybersecurity assessments under Requirement 3.11.2:

#### **1. Early and Continuous Cybersecurity Integration**

* Security assessments must start at the **requirements phase** and continue throughout the software lifecycle. Vulnerabilities found late in development or after deployment can compromise the mission.
* Regularly assess risks before incorporating reused and third-party software components (COTS, GOTS, OSS, MOTS).

#### **2. Comprehensive Security Testing**

* Cybersecurity vulnerabilities are not always evident during functional testing. Use:
  + Static code analysis.
  + Dynamic testing, including penetration testing.
  + Continuous vulnerability scanning for third-party libraries.
* Develop **test cases** specifically for security edge scenarios, especially for COTS, OSS, or other external software.

#### **3. Protect Authentication and Privileges**

* Many cybersecurity breaches result from poor **authentication mechanisms** or weak **privilege management**.
* Implement multi-factor authentication (MFA) and **least privilege principles** for all software systems and users.

#### **4. Plan for Third-Party and External Software Management**

* Monitor all reused software for vulnerabilities throughout its lifecycle (not just during initial integration).
* Update and patch third-party libraries based on known vulnerabilities without waiting for functional issues to arise.

#### **5. Leverage Automated Tools for Vulnerability Scanning**

* Small projects can take advantage of free or low-cost tools like:
  + **OWASP Dependency-Check** (for OSS libraries).
  + **Bandit** (for Python static code analysis).
  + **GitHub Advanced Security** (for repository vulnerability detection).

#### **6. Document and Learn from Past Risks**

* Document all cybersecurity risks, test results, and mitigations for future reference and improvement.
* Consider lessons learned throughout NASA projects and apply proven solutions to avoid similar issues.

### **Final Recommendations**

NASA projects, whether small or large, can benefit from the systematic application of these lessons learned:

* **Assess Early and Regularly**: Perform security assessments at every key development milestone.
* **Focus on Reusability Risks**: COTS, OSS, and reused software are significant vulnerability sources—evaluate them rigorously.
* **Secure Development Practices**: Use secure coding standards and tools from project inception.
* **Engage SMEs**: Work with cybersecurity experts like Information System Security Officers (ISSOs) to identify and mitigate risks.

By incorporating these lessons, projects can not only comply with Requirement 3.11.2 but also strengthen overall mission resilience. Always document findings for continuous improvement! For further information, reference the **NASA Lessons Learned Information System (LLIS)**.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-156 - Evaluate Systems for Security Risks**

3.11.2 The project manager shall perform a software cybersecurity assessment on the software components per the Agency security policies and the project requirements, including risks posed by the use of COTS, GOTS, MOTS, OSS, or reused software components.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm the project has performed a software cybersecurity assessment on the software components per the Agency security policies and the project requirements, including risks posed by the use of COTS, GOTS, MOTS, OSS, or reused software components.

## 7.2 Software Assurance Products

Software assurance products are essential for documenting cybersecurity risks, mitigation plans, and completed assessments to provide evidence of compliance with NASA requirements and standards. The enhanced guidance streamlines these artifacts while ensuring relevant data is captured.

#### **Required Artifacts**:

1. **Findings from Software Cybersecurity Assessments**:

   * A detailed list of all vulnerabilities, risks, and weaknesses found during the cybersecurity assessments. Include:

     + Type of vulnerability (e.g., code quality, input validation, authentication issues).
     + Location in the software component.
     + Severity ranking (e.g., Critical, High, Medium, Low).
     + Risk impact analysis results.
     + Mitigation status (e.g., Open, Closed, In Progress).
   * Example:

     ```
     Finding: Buffer Overflow in Telemetry Processing Module  
     Severity: Critical  
     Impact: May lead to denial-of-service or unsafe data processing during mission telemetry transmission.  
     Mitigation Plan: Add bounds checking to processing function. ETA for fix: MM/DD/YYYY.
     Status: In Progress
     ```
2. **Confirmation of Threat Summary and Project Protection Plan Compliance**:

   * Provide evidence that the project developed a **Threat Summary** and **Project Protection Plan (PPP)** per NASA policy (NPR 7120.5E) and NASA-STD-1006.
   * The evidence may include:
     + PPP document references (version, date, location).
     + Table mapping software risks identified in the PPP to mitigations implemented in software.
3. **Software Risk Assessment Report**:

   * A concise report detailing the cybersecurity risks identified for **COTS, GOTS, MOTS, OSS, reused components, and newly developed software** (includes their relation to system-level risks). This report may outline:
     + Assessment methodology (e.g., tool-driven analysis, manual reviews, penetration tests).
     + Risk categories and corresponding mitigations.
     + Residual risks that require continuous monitoring.

## 7.3 Metrics

Metrics are critical for monitoring the effectiveness of the cybersecurity assessments and tracking the project's risk mitigation progress over time. Expanded metrics provide insight into risk trends, mitigation efforts, and severity tracking.

#### **Recommended Metrics**:

1. **Risk Lifecycle Metrics**:

   * **Number of Risks Identified in Each Lifecycle Phase**: Measure risks documented during requirements, design, implementation, testing, and deployment phases.
   * **Number of Risks by Status**:
     + Open (Outstanding Risks).
     + Closed (Mitigated Risks).
     + In Progress (Actively mitigated).
   * **Number of Risks with Mitigation Plans vs. Total Risks Identified**: Tracks gaps in actionable mitigation planning.
2. **Risk Severity Metrics**:

   * **Distribution of Risks by Severity** (e.g., Red, Yellow, Green) over time.
     + Track the percentage of high severity risks decreasing (mitigated) vs. new ones introduced during updates.
3. **Risk Trend Metrics**:

   * **Trending Risks**:
     + Number of risks trending upward or downward over time (e.g., unmitigated vs. newly identified vulnerabilities).
     + Pinpoint areas of increasing threats to prioritize mitigations.
4. **Cybersecurity-Specific Metrics**:

   * **Number of Cybersecurity Risks Identified**:
     + Track total risks broken down by source: COTS, OSS, MOTS, reused software, or internally developed software.
   * **Comparison of Cybersecurity Risks and Mitigation Plans**:
     + Percent of cybersecurity risks with mitigations vs. total cybersecurity risks.
     + Track unresolved or residual risks to understand security exposure.

#### **Example Metrics Tracking Chart**:

| **Metric** | **Requirements Phase** | **Design Phase** | **Implementation** | **Testing** | **Deployment** |
| --- | --- | --- | --- | --- | --- |
| Risks Identified | 5 | 10 | 15 | 8 | 3 |
| Risks Closed | 0 | 4 | 8 | 6 | 3 |
| Risks by Severity (Critical/High) | 3 / 2 | 5 / 5 | 8 / 7 | 4 / 4 | 1 / 1 |
| Cybersecurity Risks (COTS/OSS/MOTS) | 2 | 4 | 6 | 3 | 1 |
| Mitigation Plans in Place (%) | 60% | 80% | 85% | 90% | 100% |

**See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).**

## 7.4 Guidance

The expanded guidance highlights clear actions, criteria, and collaborative processes for ensuring compliance with Requirement 3.11.2 through systematic evaluation, risk mitigation, and workflow integration.

#### **Key Steps**:

**1. Confirm Software Cybersecurity Assessment Completion**:

* Verify that software-level cybersecurity assessments have been performed per NASA's Agency security policies and project-specific requirements.
* Incorporate assessments early and evaluate **continuously throughout the SDLC** (requirements, design, implementation, testing, deployment).

**2. Evaluate Risks in COTS, GOTS, MOTS, OSS, and Reused Software Components**:

* Focus cybersecurity evaluations on known risk factors such as:

  + Components running by default or with elevated privileges.
  + Critical data-handling components (e.g., telemetry processing, authentication systems).
  + Past component vulnerabilities or unreliable software histories.
  + Open-source and reused software dependencies prone to unpatched vulnerabilities.
* Conduct both manual and automated analyses:

  + **Automated Static Analysis**: Use security tools like SonarQube, OWASP Dependency-Check, or CodeQL.
  + **Secure Coding Practices Analysis**: Confirm adherence to coding standards for selected languages (e.g., CERT Secure Coding Standards).

**3. Confirm Cybersecurity Risks Are Identified per SWE-154**:

* Engage the **Information System Security Officer (ISSO)** to confirm:
  + All cybersecurity risks are identified (flight and ground systems).
  + Mitigation requirements have been added to the appropriate software specifications and updated as risks evolve.
  + Reviews of SWE-154-related topics (cybersecurity risk identification and mitigation) are completed.

**4. Evaluate Mitigation Planning**:

* Review the PPP and System Security Plan for alignment between **risks**, **candidate protection strategies (CPS)**, and mitigation plans. Ensure that every identified risk has an associated mitigation plan tracked to completion.

#### **Enhanced Evaluation Checklist**:

Here is an improved checklist for software assurance personnel:

| **Evaluation Step** | **Key Questions** |
| --- | --- |
| **Cybersecurity Assessment Completion** | Did the project team perform assessments on all software components? |
| **Mitigation of COTS, GOTS, MOTS, OSS, Reused Risks** | Were third-party software components assessed for vulnerabilities? |
| **Evidence of Risk Tracking** | Are risks tracked with appropriate severity indicators and mitigation statuses? |
| **PPP and SWE-154 Alignment** | Are cybersecurity risks aligned with PPP and SWE-154 risk management strategies? |
| **Secure Coding Practices** | Are secure coding standards being applied in development processes? |
| **Threat Summary Completion** | Is evidence documented that Threat Summaries and PPPs were completed? |

### **Conclusion**

This improved software assurance guidance provides practical steps to meet Requirement 3.11.2 in a comprehensive manner. By focusing on systematic risk identification, robust cybersecurity assessments, targeted mitigations, and continuous tracking of risk metrics, projects can ensure the security of software components developed, reused, or acquired. Collaborating with ISSOs and employing automated tools streamlines efforts, ensuring compliance with NASA's standards while maintaining secure mission systems. Additional reference to **NASA SA Suggested Metrics** (Topic 8.18) ensures alignment with institutional measurement practices.

See also Topic [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide).

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) |

# 8. Objective Evidence

Objective evidence is essential for demonstrating that a software project complies with Requirement 3.11.2, which ensures that security assessments are conducted thoroughly across the software development lifecycle (SDLC), vulnerabilities are identified and mitigated, and risks are properly documented. The following list outlines tangible proof of compliance that can be reviewed, tracked, and audited.

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

#### **1. Documentation**

1. **Software Cybersecurity Assessment Reports**:

   * Detailed reports listing:
     + Identified vulnerabilities and risks.
     + Severity ratings (e.g., Critical, High, Medium, Low).
     + Risk sources (e.g., COTS, OSS, GOTS, MOTS, reused, or custom components).
     + Likelihood and impact analysis.
     + Mitigation plans and status (e.g., Open, Closed, In Progress).
   * Supporting evidence for every stage of the SDLC (requirements, design, implementation, testing, deployment).
2. **Threat Summary**:

   * Evidence that the project developed and approved a Threat Summary identifying threats to software components.
   * Include descriptions of hostile, environmental, and system-specific risks.
3. **Project Protection Plan (PPP)**:

   * Evidence that the project created and maintained a Project Protection Plan that covers:
     + Mitigation strategies tied to candidate protection strategies outlined in NASA policies.
     + Software components evaluated for vulnerabilities, with security approaches documented.
     + Mapping of risks identified during assessments to specific mitigations.
4. **System Security Plan (SSP)**:

   * A formal security plan showing integration of software-specific risks into broader system security requirements.
   * Evidence of alignment with NASA-STD-1006 and NPR 7120.5E.
5. **Risk Management Documentation**:

   * Logs or database entries tracking software vulnerabilities and risks throughout the development lifecycle:
     + Risk ID, description, severity rating, impact analysis, and mitigation plan.
     + Status updates (Open/Closed/In Progress).
     + Trend reporting over time (upward/downward risk trends).

#### **2. Testing and Analysis Artifacts**

1. **Static Code Analysis Results**:

   * Reports generated from static analysis tools (e.g., SonarQube, CodeQL, OWASP Dependency-Check) showing:
     + Detected coding vulnerabilities such as buffer overflows, injection attacks, or hardcoded credentials.
     + Adherence to secure programming standards for the specific language(s) used.
2. **Dynamic Code Analysis Reports**:

   * Evidence of runtime testing for vulnerabilities such as memory corruption, race conditions, and insecure data flows.
3. **Penetration Testing Reports** (if applicable):

   * Results from authorized penetration tests demonstrating:
     + Exploitable vulnerabilities in software components or interfaces.
     + Confirmation that key systems (e.g., networked or command systems) are protected from attack vectors.
4. **Assessment of Third-Party Components (COTS, OSS, etc.)**:

   * Vulnerability reports and certificates of approval for all third-party software components used in the project.
   * Documentation of the evaluation criteria applied to third-party components, including:
     + Known vulnerabilities (via SBOM analysis or dependency scanning).
     + Safety, licensing, and compatibility checks.

#### **3. Requirements-Related Evidence**

1. **Software Security Requirements List**:

* Documentation of cybersecurity requirements included in software specifications, including:
  + Functional requirements such as encryption for data transmission and secure authentication mechanisms.
  + Non-functional requirements such as performance under attack simulations or memory usage in edge cases.
* Evidence that these requirements align with project-level standards such as the PPP and SSP.

1. **Traceability Matrix**:

* Evidence mapping cybersecurity requirements to implementation, verification, and validation activities.
* Ensure every identified risk links back to a mitigation step, with proof of validation (e.g., test results).

#### **4. Change and Configuration Management Evidence**

1. **Change Impact Analysis Reports**:

* Reports documenting how new software components or modifications (COTS, OSS, MOTS, reused) impact the project's security posture.
* Include instances of risk reassessment prompted by design or code changes.

1. **Secure Configuration Documentation**:

* Evidence of proper security configurations for build tools, compilers, testing environments, and deployment pipelines.
* Proof that secure coding flags, features, or tools are enabled (e.g., secure stack protections).

#### **5. Collaboration Evidence**

1. **Record of ISSO Engagement**:

* Evidence showing collaboration with the Information System Security Officer (ISSO), including:
  + Reviews of identified risks.
  + Confirmation of mitigation strategies.
  + Participation in assessments for space and ground systems.

1. **Interdisciplinary Review Logs**:

* Records of cybersecurity discussions involving software engineers, system engineers, project managers, and cybersecurity experts.

#### **6. Approval and Validation Evidence**

1. **Approval Records**:

* Evidence showing formal approvals of cybersecurity assessment findings and mitigation plans by project stakeholders.
* Confirm compliance with Agency security policies and standards (e.g., NASA-STD-1006).

1. **Validation Evidence for Mitigations**:

* Detailed verification and validation reports confirming the success of implemented mitigations.
* Cross-reference to test results showing vulnerabilities were resolved.

#### **7. Metrics Tracking**

1. **Cybersecurity Metrics Analysis**:

* Include tracking data showing trends in cybersecurity risks (open, closed, severity) and mitigation progress.
* Metrics outputs such as:
  + Percentage of risks mitigated by lifecycle phase.
  + Distribution of security risks by software component source (COTS, OSS, reused, custom).
  + Trending analysis (upward/downward risk movement).

#### **8. Archiving and Long-Term Evidence**

1. **Secure Archival of Software Artifacts**:

* Evidence showing secure storage of all necessary software artifacts, including:
  + Source and executable code.
  + Configuration files.
  + Integrity verification details.
  + Supporting vulnerability and risk data for future audits.

### **Summary Checklist of Objective Evidence**

Below is a summary checklist of objective evidence grouped by category:

| **Category** | **Objective Evidence** |
| --- | --- |
| **Documentation** | Assessment reports, PPP, SSP, risk logs, Threat Summary |
| **Testing and Analysis** | Static/dynamic analysis results, penetration testing reports |
| **Requirements** | Security requirements list, traceability matrix |
| **Change Management** | Change impact analysis, secure configuration documentation |
| **Collaboration** | ISSO records, interdisciplinary review logs |
| **Approval/Validation** | Records of stakeholder approvals, mitigation validation reports |
| **Metrics** | Cybersecurity metrics dashboard and trend analyses |
| **Archival Evidence** | Secure storage of code and vulnerability-related data |

### **Compliance and Review Process**

Use the objective evidence to:

1. **Demonstrate Compliance**: Ensure all listed artifacts map directly to the requirements in 3.11.2.
2. **Enable Audits**: Maintain a repository of evidence as part of the project’s record keeping, making it accessible for review.
3. **Facilitate Risk Mitigation Tracking**: Continuously monitor risks and mitigations using metrics reports and logs.

By maintaining these objective evidence artifacts, projects can ensure successful adherence to Requirement 3.11.2 while protecting mission systems from cybersecurity threats.
