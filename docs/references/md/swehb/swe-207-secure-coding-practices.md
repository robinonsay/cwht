# SWE-207 - Secure Coding Practices

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695541. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices

SWE-207 - Secure Coding Practices

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695541)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695541&showCommentArea=true&showComments=true#addcomment)

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

3.11.6 The project manager shall identify, record, and implement secure coding practices.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-207 History

SWE-207 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.11.8 The project manager shall identify, record, and implement secure coding practices. |
| Difference between C and D | No change |
| D | 3.11.6 The project manager shall identify, record, and implement secure coding practices. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |

# 2. Rationale

Secure coding practices should be identified, recorded, and implemented to include all life cycle phases of the project.  Unsafe coding practices result in costly vulnerabilities in application software that leads to the theft of sensitive data.   Some secure practices include but not limited to the strict language adherence and use of automated tools to identify problems either at compile time or run time; language-specific guidance, domain-specific guidance, local standards for code organization and commenting, and standard file header format are often specified as well.

Secure coding practices are essential for minimizing software vulnerabilities, ensuring resilience against cyber threats, and safeguarding the critical assets of a project. The importance of formally **identifying, recording, and implementing secure coding practices** stems from the increasing reliance on software in NASA’s missions and its role in supporting critical tasks, sensitive data handling, and overall system integrity.

The rationale for this requirement is supported by its alignment with proactive, industry-standard cybersecurity practices, NASA’s mission-critical objectives, and the necessity to address risks throughout the software lifecycle.

---

### **1. Protecting Mission-Critical Systems**

NASA projects often control or manage systems that are critical to mission success, human safety, or the functionality of high-value assets. Implementing secure coding practices ensures that:

* Mission-critical systems remain robust and free from vulnerabilities that could disrupt operations, compromise data, or lead to costly failures.
* Fault-tolerant, resilient code is created to prevent single points of failure that could have cascading impacts during mission execution.
* Critical systems are resistant to external adversaries and accidental failures introduced through poor coding practices.

---

### **2. Mitigating Growing Cybersecurity Threats**

The evolving and increasingly sophisticated cybersecurity threat landscape necessitates a robust software defense through secure coding. Key considerations include:

* **Targeted Cyberattacks**: Space systems are exposed to deliberate attacks, such as unauthorized access, data interception, malware injection, and command spoofing.
* **Supply Chain Risks**: Software reused or developed using third-party libraries or components may introduce vulnerabilities. Secure coding helps mitigate these risks by ensuring external code meets NASA-defined standards.
* **Emerging Operational Risks**: Software vulnerabilities left unaddressed may be difficult or impossible to mitigate once deployed, especially in space environments where direct remediation is costly or nonviable.

---

### **3. Preventing Common Software Vulnerabilities**

Use of secure coding practices effectively addresses common vulnerabilities identified by organizations like **MITRE (Common Weakness Enumeration (CWE))**, NASA, and **NIST**, such as:

* **Inadequate Input Validation**: Failure to validate inputs can lead to injection attacks (e.g., SQL injection, command injection).
* **Buffer Overflow Risks**: Poor memory handling can result in runtime crashes or opportunities for adversarial control of a system.
* **Insecure Communication**: Unencrypted or improperly transmitted data can be intercepted or modified.
* **Use of Hardcoded Credentials**: Embedding sensitive information like passwords into code can lead to unauthorized access.

By explicitly requiring the implementation of secure coding practices, NASA minimizes the occurrence of such vulnerabilities early in the software development lifecycle.

---

### **4. Enhancing Development Efficiency and Quality**

Recording and implementing secure coding practices provide substantial gains in both software quality and team efficiency:

* **Proactive Mitigation Saves Time and Cost**: Vulnerabilities discovered late in the development cycle or during operations are exponentially more expensive to correct than addressing them early.
  + According to research, **fixing a security defect during the implementation phase** can cost 6–30 times more than addressing it during design/code phases.
* **Standardized Practices Improve Code Quality**: Secure coding practices contribute to producing cleaner, more maintainable, and robust code, reducing the likelihood of introducing defects or vulnerabilities during maintenance or future iterations.

---

### **5. Ensuring Compliance With Standards and Best Practices**

NASA projects must adhere to internal cybersecurity standards as well as federal mandates, including those from:

* **CWE and NIST Secure Coding Guidelines**: These organizations provide industry-standard lists of coding weaknesses and secure implementation practices.
* **NASA Cybersecurity Frameworks**: Ensures compliance with NASA's own coding standards and guidelines, which align with agency-wide security protocols.

This requirement ensures that all project teams and stakeholders maintain compliance with these mandatory frameworks.

---

### **6. Recording Practices to Preserve Institutional Knowledge**

Formal documentation of secure coding practices ensures continuity, consistency, and repeatability across projects. Recording secure coding practices provides:

* **Reusable Guidance**:
  + New team members or contractors can quickly adopt secure coding standards without requiring extensive onboarding or training.
* **Consistency Across Teams**:
  + Projects can maintain coding discipline even across geographically diverse teams or subcontracted development groups.
* **Historical Traceability**:
  + Stored records create a referenceable audit trail for code decisions, helping troubleshoot and investigate issues post-deployment.

---

### **7. Supporting Long-Term Sustainability**

NASA missions often involve long-term operations (e.g., satellite missions extending 10+ years). Secure coding practices play a major role in ensuring software sustainability:

* **Preserving Code Safety Over Time**: Well-documented and secure code ensures that future developers can maintain, debug, or modify systems without introducing vulnerabilities.
* **Reducing Costly Failures in Legacy Systems**: Long-term sustainability mitigates risks associated with introducing vulnerabilities during updates, which would be especially critical in systems beyond Earth where patches may have limited or delayed application (e.g., Mars rovers, deep space probes).

---

### **8. Enabling Verification and Validation (V&V)**

Secure coding practices streamline and strengthen the **Verification and Validation (V&V)** process:

* Coding practices provide the foundation for **Static and Dynamic Code Analysis Tools**, which rely on properly defined practices such as input validation, proper error handling, and boundary testing.
* They enable the Software Assurance (SA) team to more effectively evaluate software products, ensuring that cybersecurity mitigations are planned and tested systematically.

---

### **9. Meeting NASA’s Unique Development Environment**

NASA's unique challenges—ranging from space-based operations to highly sensitive data—require a stringent focus on secure software development:

* Remediation options are highly limited once software is deployed in space systems, making upfront secure coding practices essential.
* NASA projects often involve integration with international partners and contractors, requiring strict governance to ensure all contributors meet the same secure coding standards.

---

### **Key Benefits of This Requirement**

Enforcing secure coding practices to ensure this requirement is met provides the following benefits:

1. **Reduced Mission Risks**: Mission operations become less vulnerable to software-based errors or cybersecurity attacks.
2. **Improved Resilience**: Software is more robust against malicious inputs, environmental stress, and operational errors.
3. **Compliance Assurance**: Adherence to federal- and agency-mandated security standards.
4. **Enhanced Code Reusability**: Secure, well-documented code is easier to reuse in future projects without introducing vulnerabilities.
5. **Lower Long-Term Costs**: Reducing the risk of late-stage defect correction or operational failures yields cost savings, especially in challenging operating environments.
6. **Knowledge Preservation**: Documentation ensures that future developers can rely on clear, established guidelines without having to “reinvent the wheel.”

---

**In Summary**:  
The rationale for **Requirement 3.11.6** is grounded in ensuring NASA software remains secure, resilient, mission-critical, and sustainable. By identifying, recording, and implementing secure coding practices, NASA ensures high-quality software that is resistant to vulnerabilities while protecting its missions, assets, and data against evolving cybersecurity threats. This proactive approach saves time, reduces costs, and creates sustainable systems aligned with NASA's long-term goals.

# 3. Guidance

This guidance builds upon the provided secure coding practices by emphasizing clarity, actionable steps, and alignment with NASA standards and best practices used across the industry. Secure coding is a continuous process that spans the **entire lifecycle** of software development, from requirements to operations. The goal of secure coding is to prevent vulnerabilities, mitigate risks, and produce high-quality software that protects NASA’s critical missions.

This enhanced guidance emphasizes **early and consistent implementation of secure coding practices** while ensuring continuous improvement and alignment with NASA’s cybersecurity priorities. Each phase contributes to a cohesive effort to produce software that is resilient, traceable, and safe for mission-critical use.

---

### **Secure Coding Best Practices**

The **Secure Coding Guidelines** encompass principles that must be embedded throughout the **software development lifecycle** (SDLC) to ensure that security considerations are neither overlooked nor addressed belatedly. Below outlines improvements for each development phase:

---

### **3.1 Requirements Phase**

#### **Enhanced Guidance**

1. **Security Requirement Identification**:

   * Ensure security requirements include both functional and non-functional aspects:
     + **Functional:** Input validation rules, data encryption protocols, authentication mechanisms.
     + **Non-Functional:** System resilience, fault tolerance, compliance with NASA security standards.
   * Security requirements should reflect:
     + **NASA Standards** (SWE-050 and NPR 7150.2).
     + Governing frameworks (e.g., NIST 800 series, CWE, OWASP).
     + Project Protection Plan (PPP) for system-level security considerations.
   * Collaborate with stakeholders to ensure **traceability** of security requirements through design, implementation, testing, and operations.
2. **Acquisition Security Requirements**:

   * For Off-The-Shelf (OTS) and Open-Source Software (OSS):
     + Evaluate providers' conformance with secure coding standards.
     + Include clauses or requirements in contracts that enforce secure coding practices for acquisitions.
3. **Risk-Based Security Requirements**:

   * Prioritize security requirements based on risk analysis:
     + Focus on interfaces (APIs, data inputs/outputs) and critical areas such as data storage, authentication protocols, and communication pathways.

---

### **3.2 Architecture Phase**

#### **Enhanced Guidance**

1. **Security by Design**:

   * Ensure all architecture decisions default to secure principles:
     + **Default Deny Policy:** Unauthorized access should be rejected unless explicitly allowed.
     + **Boundary Security:** Define physical and logical boundaries to contain security impacts (e.g., file system sandboxing, network segmentation).
     + Select architectural patterns (e.g., Zero Trust Architecture) appropriate for the system's security needs.
2. **Vulnerability Trade-Offs**:

   * Evaluate potential architecture options using risk analysis:
     + Weigh security vulnerabilities against architectural benefits.
     + For example, a microservices architecture might increase fault isolation but introduces attack surface concerns with API proliferation.
3. **Fault Containment Regions**:

   * Design software modules to localize impacts of security breaches:
     + Ensure critical operations (e.g., command execution, data storage, inter-process communication) use boundaries that prevent propagation of faults across regions.

---

### **3.3 Design Phase**

#### **Enhanced Guidance**

1. **Secure Design Principles**:

   * Embed secure design choices into every layer:
     + **Error Messages:** Avoid needlessly exposing sensitive details (e.g., filenames directories, memory addresses).
     + **Access Control:** Implement least privilege principles—ensure only necessary permissions are granted to users or systems.
     + **Input Validation:** Validate all inputs against predefined rules (e.g., block malicious inputs like SQL injection, Cross-Site Scripting).
   * Review designs for the avoidance of known Common Weaknesses (CWE) via design inspections.
2. **OTS/OSS Software Considerations**:

   * Assess the security posture of selected OTS/OSS software:
     + Are secure coding practices evident in the OTS/OSS documentation?
     + Does the software use outdated or insecure protocols requiring user intervention?
3. **Risk Scenarios**:

   * Incorporate mitigations for realistic attack scenarios:
     + Example: An attacker attempting privilege escalation by exploiting error messages to discover system design flaws.

---

### **3.4 Implementation Phase**

#### **Enhanced Guidance**

1. **Developer Training**:

   * Ensure all development team members are trained in:
     + Secure coding standards (NASA Secure Coding Guidelines, OWASP Top Ten).
     + Awareness of vulnerabilities applicable to the environment (e.g., space systems, embedded systems).
2. **Coding Standards Enforcement**:

   * Utilize linters and secure coding tools to automatically enforce standards during development.
   * Conduct compliance checks with coding guidelines prior to committing code to repositories.
3. **Continuous Vulnerability Monitoring**:

   * Track vulnerabilities throughout implementation and address them promptly.

---

### **3.5 Automated Static Analysis**

#### **Enhanced Guidance**

1. **Tool Selection and Configuration**:

   * Select tools that align with project security priorities:
     + Use tools capable of detecting common weaknesses with integration into CI/CD pipelines.
     + Configure tools to provide detailed reporting (e.g., CWE categorization, severity levels).
2. **Resolving False Positives/Negatives**:

   * Establish processes to triage tool findings:
     + Use multiple tools to cross-check results and reduce false negatives.
     + Apply manual analysis to validate whether results are false positives.
3. **Early and Incremental Use**:

   * Integrate static analysis early and perform regular scans as code evolves to enforce secure practices continuously.

---

### **3.6 Manual Static Analysis**

#### **Enhanced Guidance**

1. **Incremental Reviews**:

   * Perform smaller code reviews throughout the lifecycle:
     + Focus on specific areas, such as user authentication, encryption, or memory management.
     + Ensure assumptions between disconnected pieces of code are validated during integration reviews.
2. **Specialized Review Checklists**:

   * Create detailed review guides targeting security issues:
     + Secure coding violations (e.g., hardcoded credentials, unresolved buffer overflows).
     + Business logic validation.
     + Compliance with NASA standards.

---

### **3.7 Build Phase**

#### **Enhanced Guidance**

1. **Elimination of Compiler Warnings**:
   * Strictly enforce policies to fix all compiler warnings, converting them to errors where possible.
2. **Cryptographic Hash Verification**:
   * Generate unique hashes for releases to ensure discarded builds cannot be altered.
   * Store hashes in versions tracked via Software Bill of Materials (SBOM).
3. **Code Signing Certificates**:
   * Sign all builds used in deployments (including mobile applications).

---

### **3.8 Automated Dynamic Analysis**

#### **Enhanced Guidance**

1. **Dynamic Tools Triage**:

   * Select tools capable of assessing runtime behaviors aligned with NASA mission environments (e.g., embedded systems, space operations).
   * Use memory checking tools to identify vulnerabilities.
2. **Combination Testing**:

   * Mix automated validation tools (e.g., penetration testing frameworks) and manual dynamic reviews.

---

### **3.9 Manual Dynamic Analysis**

#### **Enhanced Guidance**

1. **Simulation of Attacks**:
   * Manually test denial-of-service and unauthorized access scenarios to evaluate system resilience.

---

### **3.10 Testing Phase**

#### **Enhanced Guidance**

1. **Cyber Resilient Testing**:
   * Prioritize test coverage for security requirements and known attack vectors.
   * Use fuzz testing to simulate malformed inputs over time.
2. **Regression Testing**:
   * Re-test security mitigations following system changes during updates.

---

### **3.11 Operations/System Configuration Phase**

#### **Enhanced Guidance**

1. **Monitoring and Maintenance**:
   * Continuously monitor systems for emerging vulnerabilities and apply patches promptly.
2. **Configuration Hardening**:
   * Apply least privilege principles in deployment environments.

---

## 3.12 Guideline for a roadmap to Cyber Resilient Software

#### **Phase 1 - Basic Security**

* Apps run in separate processes
* Processes run with non-root (administrative) service accounts
* Operating Systems (OS) hardening and compiler security settings are used
* Cryptographic integrity checks on executables
* Security audit logs
* Enforced file system access controls

#### **Phase 2 - Secure response and recovery**

* Security lockdown mode
* Secure system recovery
* •    Secure backups (including configuration files)
* Secure software updates

#### **Phase 3 - Role Based Access Control (RBAC) and intrusion detection**

* Authenticate commands from all sources
* Multiple levels of authorization (e.g., administer, operator)
* Secure boot
* Algorithmic intrusion detection

#### **Phase 4 - Zero trust, mandatory access control**

* Zero trust message bus
* SELinux mandatory access kernel calls

#### **Phase 5 - Advanced Security**

* AI/ML intrusion detection
* Memory safe programming language
* Secure microkernel of operating system

## 3.13 Maintenance Of The Software

Having a plan for executing updates, running maintenance tasks (compacting logs, rotating files…), and managing software patches as they are provided by vendors or the team must be in place for the operations modes of the software.  This plan must contain guidance on fixing vulnerabilities in the software itself as well as disclosure mechanisms to any customers.  These plans can be updated as situations change, but measurements of risk should be taken into account (i.e., weigh the risk of updating software right before a major mission milestone with limited testing time).  An operations plan for when a security incidence response is necessary to provide personnel a plan for analyzing the code/program, discussing with any IT security operations centers, and containing the impact from the security vulnerability.

## 3.14 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software)        * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

See also [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements),

See [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software)  and [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks).

See also [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design),

See also [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations),

## 3.15 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

Secure coding is particularly important in small projects, which often face resource constraints (time, personnel, and tools) but still require robust defenses against cybersecurity vulnerabilities. For smaller projects, adopting scaled-down yet effective secure coding practices ensures compliance with NASA standards while optimizing team efforts and resources. The following guidance is tailored to **small projects** to ensure these principles are practical, actionable, and efficient.

---

### **Why Secure Coding Matters for Small Projects**

* **Risk Amplification**: Even small vulnerabilities can have cascading effects, especially in systems integrated with larger NASA missions.
* **High Impact with Simple Measures**: Small teams can make significant progress with basic secure coding principles, avoiding costly rework or mission delays later.
* **Streamlined Processes**: Secure coding practices can be simplified using lightweight tools and workflows while maintaining compliance with NASA standards.

---

### **Key Steps for Small Projects**

#### **1. Identify Secure Coding Needs Early**

Small projects benefit greatly from early integration of secure coding principles into their workflows.

* **Define Security Requirements**:
  + Identify critical areas where security matters most. For example:
    - Sensitive data handling (e.g., telemetry, authentication inputs).
    - Code designed to interact with larger systems or interfaces (e.g., APIs, files).
  + Derive requirements using sources like:
    - NASA Secure Coding Practices document.
    - Project Protection Plans (PPP).
    - Off-The-Shelf (OTS) and Open-Source Software (OSS) Security Policies.
    - Known threats from **NIST’s CWE** and OWASP catalogs.
  + Document requirements early in a simple format (e.g., a bulleted checklist) for traceability throughout development.
* **Scope Security Efforts Based on Risk**:
  + Evaluate the system's impact and prioritize high-risk areas (e.g., public-facing interfaces and authentication protocols).

---

#### **2. Identify and Record Secure Coding Practices**

Small projects should formalize their chosen secure coding practices:

* Borrow from the "NASA Secure Coding Best Practices" document and industry standards like **CERT Secure Coding**, **CWE**, and **OWASP**. Focus primarily on the practices most relevant to the small project, such as:
  + **Input validation:** Validate user inputs rigorously to prevent injection attacks.
  + **Error handling:** Ensure error messages don’t reveal sensitive system details.
  + **Secure authentication:** Store passwords securely and employ secure protocols (e.g., HTTPS).
  + **Memory safety:** Avoid buffer overflows and improper memory access.
  + **Default deny policies:** Ensure unauthorized actions and access are rejected unless explicitly permitted.
* Keep it simple:
  + Record these in a centralized location (e.g., a shared document or project wiki).

---

#### **3. Simplify Development with Lightweight Processes**

Small projects can integrate secure coding practices into regular workflows without overwhelming the development team:

* **Peer Code Reviews**:
  + Adopt low-effort manual code reviews focused on security. Example questions for reviewers:
    - Are there hardcoded credentials in the code?
    - Are all inputs validated (e.g., sanitized against known bad patterns)?
    - Is sensitive information (e.g., logs) being exposed unnecessarily?
  + Use review checklists with 5–7 key items specific to secure coding (e.g., memory safety, secure error handling).
* **Automated Checks**:
  + Run lightweight **static analysis tools** (e.g., SonarQube, cppcheck, or NASA-approved tools) to detect common errors without requiring heavy setup or maintenance.
  + For small projects with limited budgets or computational resources, use **open-source tools** for vulnerability scanning and secure coding compliance.

---

#### **4. Leverage OTS/OSS Secure Software**

Small projects often rely heavily on OTS (Off-The-Shelf) and OSS (Open-Source Software) for cost and efficiency.

* **Select Trusted Sources**:
  + Only use publicly vetted and widely supported libraries with clear security documentation.
  + Check for known vulnerabilities in OTS/OSS components (e.g., via NIST’s National Vulnerability Database (NVD)).
* **Patch and Update Regularly**:
  + Monitor dependencies for updates or security patches and apply them promptly.
  + Use dependency management tools (e.g., npm audit for JavaScript, pip-audit for Python) to track vulnerabilities automatically.

---

#### **5. Scale Testing and Validation**

Testing can be streamlined for small projects:

* **Testing Focus Areas**:
  + Test interfaces and critical functionalities that are most at risk (e.g., input handling, user authentication).
  + Skip low-risk areas (where vulnerabilities are unlikely to impact security) to minimize testing overhead.
* **Static Analysis**:
  + Run static analysis tools like **CodeQL** on small codebases regularly.
* **Dynamic Analysis**:
  + Focus manual security testing on areas of operational importance.
  + Simple practices such as manually trying to bypass access controls or inject malicious inputs can reveal critical vulnerabilities.

---

#### **6. Use Resource-Constrained Development Guidance**

Small projects can mitigate resource limitations by adopting efficient tools, automation, and simple policies:

* **Minimal Overhead Automation**:
  + Automate security scans in CI/CD pipelines (even lightweight setups like GitHub Actions for basic security checks).
* **Small Team Collaboration**:
  + Assign a "security lead" to champion secure coding practices and help other developers identify issues.
  + Hold short security-oriented design discussions before significant development milestones.
* **Limit Scope to What Matters**:
  + Focus security efforts on system entry points (e.g., input validation, exposed APIs), sensitive data, and external interfaces.

---

### **Examples of Secure Coding Practices for Small Projects**

* **Error Handling**:
  + Avoid exposing sensitive system details in error messages.
  + Use generic error messages such as “Error: Unauthorized access” rather than disclosing internal details (e.g., file paths or memory addresses).
* **Input Validation**:
  + Reject invalid inputs immediately and verify data formats (e.g., sanitization against SQL injection or XSS attacks).
  + Use well-established validation libraries from OSS ecosystems when applicable.
* **Memory Management**:
  + Avoid unsafe memory operations like manual pointer manipulations in languages like C/C++.
  + Use modern languages or libraries that enforce safe memory management (e.g., Python, Rust).
* **Authentication**:
  + Never store passwords as plain text; use hashing protocols such as **bcrypt** or **PBKDF2**.
  + Enforce HTTPS for all communication, even during small-scale local testing setups.

---

### **Small Project Tool Recommendations**

Small projects can use lightweight tools and libraries suited for secure development:

* **Static Analysis**:
  + Tools like **SonarQube**, **cppcheck**, or **Bandit (Python)** for quick identification of vulnerabilities.
* **Dynamic Analysis**:
  + **OWASP Zap** for quick penetration testing.
* **Dependency Tools**:
  + **npm audit**, **pip-audit**, or **Snyk** for OSS vulnerability monitoring.
* **Error Handling**:
  + Libraries like **loguru** (Python) that centralize logging and enforce best practices.
* **Secure Authentication**:
  + Implement libraries like **OAuth** for secure user authentication.

---

### **Practical Steps for Small Teams**

* **Record Practices**: Maintain a simple document (e.g., Google Doc) or project wiki outlining secure coding requirements for future reference by all developers and stakeholders.
* **Focus Reviews on High-Risk Areas**: Prioritize reviews and testing on areas like input handling, APIs, and authentication mechanisms.
* **Integrate Lightweight Tools**: Use free or open-source tools that are easy to set up and don’t require extensive overhead.
* **Incremental Development**: Address secure coding practices step-by-step for each deliverable rather than attempting full-scale implementation at once.

---

### **Conclusion**

Small projects can effectively comply with Requirement 3.11.6 by focusing security efforts on the most critical areas, using lightweight tools, embedding secure coding practices into existing workflows, and balancing resource constraints with risk prioritization. The result is a secure, resilient software product that meets NASA’s standards without overwhelming the team or budget.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-004)

  [Top 10 Secure Coding Practices](https://wiki.sei.cmu.edu/confluence/display/seccode/Top+10+Secure+Coding+Practices "Click to open in new window")

  This site supports the development of secure coding standards for commonly used programming languages such as C, C++, Java, and Perl, and the Android™ platform.  Top ten plus two bonus practices.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-305)

  [Hash Functions](https://csrc.nist.gov/projects/hash-functions "Click to open in new window")

  NIST, Information Technology Laboratory, Computer Security Resource Center,
* (SWEREF-602)

  [CWE-200: Exposure of Sensitive Information to an Unauthorized Actor](https://cwe.mitre.org/data/definitions/200.html "Click to open in new window")

  Common Weaknesses Enumeration, Miter Corporation  CWE is a community-developed list of common software and hardware weakness types that could have security ramifications.
* (SWEREF-604)

  [CWE-209: Generation of Error Message Containing Sensitive Information](https://cwe.mitre.org/data/definitions/209.html "Click to open in new window")

  Common Weaknesses Enumeration, Miter Corporation CWE is a community-developed list of common software and hardware weakness types that could have security ramifications.
* (SWEREF-605)

  [CWE-1295: Debug Messages Revealing Unnecessary Information](https://cwe.mitre.org/data/definitions/1295.html "Click to open in new window")

  Common Weaknesses Enumeration, Miter Corporation CWE is a community-developed list of common software and hardware weakness types that could have security ramifications.
* (SWEREF-664)

  [Software Security](https://nen.nasa.gov/web/coding "Click to open in new window")

  OCE site in NASA Engineering Network, Portal that houses information for software developers to develop code in a secure fashion,  Formerly known as "Secure Coding"
* (SWEREF-665)

  [NATIONAL VULNERABILITY DATABASE](https://nvd.nist.gov/ "Click to open in new window")

  NVD is the U.S. government repository of standards based vulnerability management data represented using the Security Content Automation Protocol (SCAP).
* (SWEREF-666)

  [CVE List](https://cve.mitre.org/cve/ "Click to open in new window")

  CVE® is a dictionary of publicly disclosed cybersecurity vulnerabilities and exposures that is free to search, use, and incorporate into products and services, per the terms of use.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA’s extensive history of software development provides valuable lessons for the implementation of secure coding practices. These lessons highlight the critical importance of embedding security throughout the software development lifecycle to safeguard against vulnerabilities, minimize risks, and ensure mission success.

Below are **key lessons learned** derived from NASA’s **Lessons Learned Information System (LLIS)** and past experiences related to secure coding practices. Each lesson addresses specific challenges, successes, and opportunities relevant to Requirement 3.11.6.

---

### **1. Lesson: Early Identification of Security Vulnerabilities**

#### **Key Takeaway**:

Delaying the identification of vulnerabilities until later stages of development can result in higher remediation costs, operational risks, and compromised mission objectives.

#### **Example**:

A NASA system suffered from **buffer overflow vulnerabilities** that were not detected until integration testing. The issue resulted in unauthorized access to critical software subsystems during a test phase, leading to costly updates late in the lifecycle.

#### **Lesson Learned**:

* **Proactive Integration**: Embed secure coding practices from the **requirements phase** to identify risks early and enforce robust security design principles.
* **Traceability**: Ensure security requirements are traceable through design, implementation, and testing phases to prevent gaps in coverage.

---

### **2. Lesson: Incomplete Input Validation**

#### **Key Takeaway**:

Inadequate input validation has been a recurring issue in NASA-developed software, leading to vulnerabilities such as **injection attacks**, crashes, and unexpected system behavior.

#### **Example**:

During a planetary mission, tests revealed that invalid command inputs crashed specific modules. The software did not sanitize or validate these inputs properly, exposing entry points for potential injection attacks.

#### **Lesson Learned**:

* **Input Sanitization**: Always validate inputs rigorously at every entry point. Ensure data conforms to expected formats, ranges, and types.
* **Guideline Adherence**: Use predefined secure coding guidelines to enforce input validation (e.g., avoid unsanitized user inputs in database commands).

---

### **3. Lesson: Dependency Vulnerabilities in OTS/OSS Software**

#### **Key Takeaway**:

Third-party libraries and tools (Off-The-Shelf (OTS) or Open-Source Software (OSS)) can introduce significant security risks, including supply chain vulnerabilities, insecure protocols, or lack of support for future patches.

#### **Example**:

A commercial software tool used in spacecraft flight systems relied on outdated encryption protocols. Developers assumed the tool adhered to modern standards, but later testing revealed vulnerabilities that exposed sensitive data.

#### **Lesson Learned**:

* **Dependency Management**: Evaluate and document the security policies of any OTS/OSS dependencies. Ensure dependencies are monitored for patches or vulnerabilities.
* **Secure Frameworks**: When possible, use trusted development frameworks that are actively maintained and meet modern security standards.

---

### **4. Lesson: Lack of Secure Error Handling**

#### **Key Takeaway**:

Verbose error messages and improper error-handling strategies have unintentionally exposed sensitive system details to testers and external users.

#### **Example**:

An error handling problem occurred in a NASA mission where exposed error messages provided debugging details, such as **file paths, memory locations, and internal function calls**, to unauthorized users. These details could have been exploited to develop targeted attacks, though no actual breaches occurred.

#### **Lesson Learned**:

* **Minimal Information Exposure**: Use generic error messages (e.g., “Access Denied”) that do not reveal internal details.
* **Log Internally**: Log detailed error information securely for internal troubleshooting but separate this information from what is shown to users.

---

### **5. Lesson: Insufficient Protection for Authentication Mechanisms**

#### **Key Takeaway**:

Hardcoded credentials, improper access control, or weak authentication mechanisms create exploitable vulnerabilities, especially with remote or automated systems.

#### **Example**:

In a past project, hardcoded credentials were included in the source code for testing convenience. These credentials were later pushed to the production environment, creating significant vulnerabilities and requiring emergency patches.

#### **Lesson Learned**:

* **Avoid Hardcoded Secrets**: Store sensitive credentials in secure vaults or use environment variables securely handled by the operating systems.
* **Authentication Best Practices**: Use strong encryption algorithms for passwords (e.g., bcrypt, PBKDF2) and avoid hardcoding any secrets.

---

### **6. Lesson: Deficient Automated and Manual Code Reviews**

#### **Key Takeaway**:

Failing to integrate effective code review processes allowed vulnerabilities to pass undetected into production environments.

#### **Example**:

During a launcher software review, a static code analysis tool identified several warnings regarding **out-of-bounds memory access**. Due to the team’s small size and time constraints, these warnings were dismissed as false positives, leaving unaddressed vulnerabilities that required post-launch remediation.

#### **Lesson Learned**:

* **Combine Tools and Manual Reviews**: Always use a combination of automated static/dynamic analysis tools along with manual peer reviews to validate findings and cover gaps in automated detection.
* **Incremental Reviews**: Perform smaller, incremental code reviews to maintain focus and avoid dismissing issues as technical "debt."

---

### **7. Lesson: Insecure Build and Deployment Practices**

#### **Key Takeaway**:

Neglecting to secure the software build and deployment process can allow unauthorized individuals to modify or replace critical components, jeopardizing the integrity of the system.

#### **Example**:

A NASA system build was performed on an insecure network, leading to uncertainty about whether the build had been tampered with. The issue delayed deployment while additional verification steps were implemented.

#### **Lesson Learned**:

* **Secure Build Environments**: Ensure builds are performed in controlled environments with cryptographic signing and version control.
* **Verification with Hashing**: Use cryptographic hash functions to validate the integrity of built software and track changes.

---

### **8. Lesson: Poor Documentation of Secure Coding Practices**

#### **Key Takeaway**:

Failure to document secure coding practices led to inconsistencies among developers, especially across geographically distributed teams.

#### **Example**:

In one project, misunderstanding of secure data-handling practices resulted in inconsistent implementations, with some modules following encryption policies and others relying on plaintext storage due to communication gaps.

#### **Lesson Learned**:

* **Centralized Documentation**: Maintain a single source of truth for secure coding guidelines that is accessible to everyone on the project.
* **Simple and Modular Guidelines**: Provide concise, implementation-specific secure coding standards for reference during development.

---

### **9. Lesson: Neglecting Runtime Security During Operations**

#### **Key Takeaway**:

Even if software is developed securely, operational vulnerabilities (e.g., misconfigured systems) can expose systems to risks.

#### **Example**:

A previously secure software system was deployed with default configurations that unintentionally allowed unauthorized access to critical endpoint APIs.

#### **Lesson Learned**:

* **Implementation of Secure Defaults**: Configure systems securely before deployment (e.g., least privilege settings, securing APIs, disabling unnecessary services).
* **Ongoing Security Monitoring**: Continually monitor for vulnerabilities and apply patches as needed.

---

### **10. Lesson: Lack of Awareness of Known Vulnerabilities**

#### **Key Takeaway**:

Ignoring known vulnerabilities, such as those documented in systems like CWE (Common Weakness Enumeration), introduces easily preventable flaws into systems.

#### **Example**:

A reused software module had known and documented vulnerabilities in a global vulnerability database (CVE). The team was unaware of these because they didn’t check for updates or patch notices.

#### **Lesson Learned**:

* **Proactive Vulnerability Review**: Actively monitor for known vulnerabilities (CWE, CVE databases) in the system and its dependencies.
* **Patch Management**: Act on vulnerability assessments and apply fixes promptly to minimize system exposure.

---

### **Conclusion:**

NASA has learned that **secure coding practices** must be fully integrated into all phases of small and large projects, including requirement development, design, implementation, testing, and operations. The lessons learned emphasize the importance of **proactive measures**, **continuous monitoring**, and **team-wide commitment** to secure coding principles to ensure the highest level of software quality and mission readiness. By applying these lessons, small projects can avoid common pitfalls and contribute to NASA’s tradition of safe and reliable systems.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-207 - Secure Coding Practices**

3.11.6 The project manager shall identify, record, and implement secure coding practices.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess that the software coding guidelines (e.g., coding standards) includes secure coding practices.

## 7.2 Software Assurance Products

Effective Software Assurance (SA) ensures that secure coding practices are defined, implemented, and verified throughout the software lifecycle. The SA role is to independently assess compliance with secure coding standards and provide assurance that software products meet cybersecurity expectations.

##### **Key SA Products:**

1. **Secure Coding Guidelines Assessment**:

   * Review the project’s documented secure coding guidelines or standards to ensure alignment with best practices (e.g., SEI CERT, MISRA, AUTOSAR).
   * Verify that the selected secure coding standards are tailored to the programming languages, libraries, tools, and specific needs of the project.
2. **Independent Static Code Analysis Results**:

   * SA performs or reviews the results of **independent static code analysis** to assess the compliance of the source code with the defined secure coding practices.
   * Look for key vulnerabilities such as buffer overflows, memory leaks, input validation failures, race conditions, improper error handling, and any exceptions to the secure coding guidelines.
3. **Project-Specific Secure Coding Standards**:

   * Confirm that the software development organization has adopted a secure coding standard appropriate for the programming language(s) used.
   * Assess whether the secure coding standard addresses **safety**, **reliability**, and **security** comprehensively.
4. **Dynamic Analysis Results**:

   * Review dynamic code analysis output (e.g., tools checking runtime behavior, memory management issues, or improper API usage) to ensure secure implementation of code during runtime.
5. **Compliance Verification Reports**:

   * Maintain clear documentation identifying and addressing all gaps or deficiencies found during SA’s review of secure coding practices.
6. **SA Code Spot Checks**:

   * Even when analysis tools are used, occasional **manual spot checks** are critical to verifying that the most critical secure coding guidelines are applied.

## 7.3 Metrics

Metrics help monitor and assess the project's adherence to secure coding practices throughout development.

##### **Key Metrics for Secure Coding Practices**:

1. **Non-Conformances with Secure Coding Standards**:

   * Total number of non-conformances with cybersecurity coding standards:
     + **Open Non-Conformances**: Issues identified but not yet resolved.
     + **Closed Non-Conformances**: Issues that were identified, addressed, and successfully closed.
   * Percentage of closed non-conformances (e.g., "90% closed by [milestone]").
2. **Vulnerability Trends**:

   * Number and severity of vulnerabilities identified in static and dynamic analysis over time.
   * Number of unresolved vulnerabilities or backlogged security fixes.
3. **Tool-Based Coverage Metrics**:

   * Percentage of code analyzed by static and dynamic tools.
   * Number of violations flagged for each type of security flaw (e.g., invalidated inputs, memory safety).
4. **Code Review Metrics**:

   * Number of peer-reviewed lines of code from a security perspective.
   * Number of coding errors corrected during reviews.

## 7.4 Guidance

#### **Objective**: Confirm that the project has implemented secure coding practices and these practices are being followed rigorously throughout software development.

---

##### **1. Verify Secure Coding Guidelines**

1. **Select the Right Guidelines Early**:

   * Confirm that secure coding guidelines were chosen during **project planning**.
   * Example secure coding standards include:
     + **C Language**: SEI CERT C Coding Standard, MISRA C.
     + **C++ Language**: SEI CERT C++, MISRA C++, AUTOSAR C++, JSF AV C++.
     + **Other Languages**: OWASP’s secure coding guidelines for Java, Python, or JavaScript.
2. **Traceability to Requirements**:

   * Ensure that secure coding guidelines align with project security requirements, NASA policies, and system-level protection requirements (e.g., as outlined in the Project Protection Plan).
3. **Continuous Assessment**:

   * Reassess the adequacy of secure coding practices at major milestones to ensure alignment with evolving project requirements and cybersecurity concerns.

---

##### **2. Confirm Secure Coding Practice Implementation**

1. **Review Software Development Plans (SDP)**:

   * Confirm that the SDP documents which secure coding practices have been selected.
   * Verify that teams are aware of these practices and have the tools and training to follow them.
2. **Independent Verification**:

   * Obtain evidence of compliance using standard checkers. Tools like **SonarQube**, **Checkmarx**, or specific compilers with security extensions (e.g., GCC, Clang) can validate adherence.
   * If automatic tools are not available, perform **spot checks** on representative portions of source code to verify manual compliance with selected coding standards.
3. **Secure Configuration Practices**:

   * Ensure secure default configurations are applied to software components (e.g., disabling unnecessary features, enforcing secure protocols by default).

---

##### **3. Perform Independent Code Analysis**

1. **Use Automated Tools**:

   * Run **code analysis tools** against the source code to check for violations of the selected secure coding rules.
     + Examples include **static analysis tools** (e.g., Fortify, Coverity) and **dynamic analysis tools** (e.g., OWASP ZAP for web security testing, Valgrind for memory debugging).
   * Analyze results for critical security issues like input/output validation, resource management, and proper use of APIs.
2. **Manual Spot Checks**:

   * For codebases where automated tools are unavailable (e.g., ladder logic programming for Programmable Logic Controllers), perform manual inspections to ensure adherence to secure coding guidelines.
3. **Review Engineering Outputs**:

   * If engineers are using their own tools for static or dynamic analysis, review the output to assess whether findings have been addressed and resolved.
   * Check if false positives and false negatives in tool outputs are appropriately managed and documented.
4. **Leverage IV&V for Independent Analysis**:

   * Collaborate with the IV&V (Independent Verification & Validation) team, if applicable, to access additional capabilities for detecting vulnerabilities.

---

##### **4. Address Cybersecurity Vulnerabilities**

1. **Check Project Vulnerability Assessment**:

   * Confirm that vulnerability scans (static and dynamic) have been performed by the engineering team.
     + Examples of vulnerabilities include injection attacks, misuse of authentication credentials, and memory management issues.
   * Verify that identified issues have been resolved and documented.
2. **Confirm Testing and Validation of Fixes**:

   * Ensure vulnerabilities are fixed, tested, and documented using traceability matrices or issue-tracking tools.
   * Check that changes made to address vulnerabilities have been retested in subsequent test phases (e.g., regression testing, system integration testing).
3. **Use External References for Verification**:

   * Consult external resources like:
     + **NIST’s National Vulnerability Database (NVD)** for identifying known vulnerabilities.
     + **MITRE’s Common Weakness Enumeration (CWE)** dictionary for common software weaknesses.
     + NASA’s secure coding resources (internal access only).

---

#### **Summary of Responsibilities for Software Assurance (SA)**

* **Assess Compliance**: Ensure coding guidelines include secure practices and verify that these standards are consistently applied.
* **Participate in Analysis**: Independently analyze code with automated tools and complement this with manual inspections where needed.
* **Collaborate Across Teams**: Work with engineering and IV&V to resolve vulnerabilities efficiently.
* **Monitor Metrics**: Track and report metrics to measure security conformance and progress.
* **Encourage Proactive Planning**: Push for early identification of security requirements and selection of secure coding standards.

By systematically adhering to the above guidance, SA can ensure compliance with **Requirement 3.11.6**, reduce security risks, and contribute to the overall mission reliability of NASA projects.

A method of identifying weaknesses and vulnerabilities is to use the National Vulnerability Database [665](#_tabs-<p></p>)  from NIST that is the U.S. government repository of standards-based vulnerability data. Software weaknesses can be identified using Common Weakness Enumeration (CWE) [666](#_tabs-<p></p>)  - a dictionary created by MITRE.

See the secure coding site [664](#_tabs-<p></p>)  for more information (NASA access only).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software)        * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

**Requirement Context**: The requirement emphasizes that secure coding best practices must be **identified, recorded, and implemented** throughout the software development lifecycle to ensure the security, reliability, and integrity of NASA systems.

**Objective evidence** refers to documentation, records, audits, and artifacts that demonstrate compliance with the requirement.

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

The following examples highlight specific and practical forms of objective evidence derived from real-world development processes to meet Requirement 3.11.6.

---

### **1. Secure Coding Guidelines**

#### **Description**:

* Documented **secure coding standards** or guidelines that align with the project’s programming language(s) and system goals.

#### **Examples of Evidence**:

* A project-specific **Secure Coding Standards Document** that specifies rules:
  + Input validation (e.g., reject invalid inputs).
  + Memory safety (e.g., safe handling of pointers in C/C++).
  + Authentication and encryption practices.
  + "Default deny" policy for access control.
* Proof of adoption of industry coding standards, such as:
  + **SEI CERT C** or **CERT C++**.
  + **MISRA C/MISRA C++** guidelines (for embedded systems).
  + **OWASP Secure Coding Practices** (for web-based applications).
  + **AUTOSAR C++** (for automotive-related systems, if relevant).
* Evidence of **tailoring** coding standards from external frameworks to meet project needs and provided requirements.

---

### **2. Software Development Plan (SDP)**

#### **Description**:

* The **SDP** should document how secure coding practices are integrated into the development process.

#### **Examples of Evidence**:

* Sections in the **SDP** detailing:
  + The coding standards selected (e.g., SEI CERT, MISRA).
  + Description of how the coding standards will be applied (e.g., tools/scripts to enforce).
  + Procedures for reviewing, validating, and updating the coding guidelines throughout the project lifecycle.
* **Change Logs** for the SDP showing updates to address secure coding practices or management processes.

---

### **3. Traceability Matrices**

#### **Description**:

* Demonstrates traceability of secure coding-related requirements across **requirements, design, code, and test phases**.

#### **Examples of Evidence**:

* **Requirements Traceability Matrix (RTM)** that explicitly links secure coding practices to:
  + Relevant system security requirements.
  + Design features (e.g., access control, data encryption).
  + Code modules (e.g., input/output validation, memory handling).
  + Test cases (e.g., unit tests for security-critical code paths).
* A specific **Cybersecurity Traceability Supplement**:
  + Mapping vulnerabilities or coding requirements to CWE identifiers (e.g., CWE-78 for OS command injection, CWE-125 for buffer overread).

---

### **4. Static Analysis Reports**

#### **Description**:

* Static code analysis is an essential step in verifying adherence to coding standards and identifying vulnerabilities.

#### **Examples of Evidence**:

* **Automated Reports** generated from tools such as:
  + **SonarQube**
  + **Fortify**
  + **Coverity**
  + **Checkmarx**
* Static analysis **compliance reports** showing:
  + The percentage of code compliant with the selected secure coding standard.
  + Listed defects and their severity (e.g., critical, major, minor).
  + Action items for addressing non-conformances (with status: open/closed).
* **Trend Reports** showing reduced coding violations over successive tool runs.
* **False Positives Documentation** to explain and validate why specific findings are not actual vulnerabilities.

---

### **5. Dynamic Analysis Reports**

#### **Description**:

* Verifies that the software behaves securely during execution.

#### **Examples of Evidence**:

* **Dynamic Scan Results** from tools such as:
  + **Valgrind** (memory analysis).
  + **OWASP ZAP** (to identify runtime security issues in web applications).
  + **KLEE** or **AFL** (fuzz testing for unexpected inputs or boundary cases).
* Reports identifying runtime issues, including:
  + Memory leaks, race conditions, or improper error handling.
  + Filesystem or API misuse vulnerabilities.
* **Authentication Runtime Testing Evidence**:
  + Validation that improper access attempts are denied while authorized access is granted.

---

### **6. Peer Review and Manual Code Inspections**

#### **Description**:

* Manual review of source code by team members or auditors for secure coding adherence.

#### **Examples of Evidence**:

* **Code Review Records** with:
  + Date, participants, and outcomes of the review.
  + Checklist(s) for secure coding (e.g., "Are all inputs validated?")
  + Identified issues found during reviews, along with resolutions and status.
* Evidence of **Secure Coding Spot Checks** during manual inspection on high-risk areas (e.g., authentication modules, input handling methods).

---

### **7. Vulnerability and Risk Tracking Reports**

#### **Description**:

* Evidence demonstrating the identification and mitigation of security vulnerabilities and risks.

#### **Examples of Evidence**:

* Results from vulnerability scans and their resolutions:
  + Using the **NIST National Vulnerability Database (NVD)** to ensure no known vulnerabilities (e.g., CVEs) remain in open-source or third-party components.
  + Mapping detected weaknesses against **Common Weakness Enumerations (CWE)** for resolution.
* **Risk Registers** documenting:
  + Risks related to coding vulnerabilities.
  + Mitigations in place (e.g., input validation mechanisms, encryption of sensitive data).

---

### **8. Test Cases and Results**

#### **Description**:

* Cybersecurity testing ensures all identified vulnerabilities are mitigated during unit, integration, and system testing.

#### **Examples of Evidence**:

* **Test Case Documents**:
  + Testing input validation, output sanitization, and handling of invalid or malicious inputs.
  + Tests for known vulnerabilities (buffer overflows, injection attacks like SQL or command injection).
* **Test Results**:
  + Evidence of successful testing for error handling (e.g., no sensitive data leaked in logs or errors).
  + Regression test reports showing no reintroduction of fixed vulnerabilities.

---

### **9. Secure Build and Deployment Evidence**

#### **Description**:

* Detailed evidence from building and deploying the software in a secure manner.

#### **Examples of Evidence**:

* Logs verifying compiler warnings were eliminated.
* Proof of hash-based integrity verification (e.g., SHA-256 hashes recorded in Software Bill of Materials/Software Authorization Notice).
* Signed builds with digital certificates to confirm origin.
* Scripts for deploying software with disabled insecure features (e.g., disabling development accounts or default passwords).

---

### **10. Audit and Compliance Records**

#### **Description**:

* Documentation of audits and assessments by independent teams to ensure compliance.

#### **Examples of Evidence**:

* Completed Secure Coding **Audits** (showing which rules were violated and how they were addressed).
* **Evaluation Reports**:
  + Software Assurance evaluations of secure coding practices.
  + IV&V evaluations confirming adherence to coding guidelines.
* Records of **third-party assessments** (if applicable) confirming compliance.

---

### **11. Training Records**

#### **Description**:

* Evidence that the development team and stakeholders are trained in secure coding practices.

#### **Examples of Evidence**:

* Training certificates for team members, such as:
  + Secure Coding Practices Training.
  + Specialized certifications (e.g., CSSLP, CEH).
* Training session attendance logs, slides, and materials.
* Agendas and minutes from team workshops and security awareness briefings.

---

### **12. Lessons Learned Documentation**

#### **Description**:

* Post-project reviews documenting lessons related to secure coding practices and process improvement.

#### **Examples of Evidence**:

* Records of issues encountered due to non-compliance with secure coding standards and their resolutions.
* Recommendations for future projects to improve secure coding adherence.

---

### **Conclusion**

Objective evidence for Requirement 3.11.6 spans from **planning documents to implementation artifacts and test results**, all of which demonstrate a systematic approach to secure coding. Collecting and maintaining this evidence is vital for ensuring compliance, improving software quality, and safeguarding against cybersecurity risks in NASA projects.
