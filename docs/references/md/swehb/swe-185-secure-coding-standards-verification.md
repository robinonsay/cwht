# SWE-185 - Secure Coding Standards Verification

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695521. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification

SWE-185 - Secure Coding Standards Verification

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695521)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695521&showCommentArea=true&showComments=true#addcomment)

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

3.11.7 The project manager shall verify that the software code meets the project’s secure coding standard by using the results from static analysis tool(s).

## 1.1 Notes

If a static analysis tool will not work with the selected coding standard, other methods are acceptable, including manual inspection.

## 1.2 History

Click here to view the history of this requirement: SWE-185 History

SWE-185 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.11.9 The project manager shall verify that the software code meets the project’s secure coding standard by using the results from static analysis tool(s). |
| Difference between C and D | No change  A note was added under this SWE for clarification. |
| D | 3.11.7 The project manager shall verify that the software code meets the project’s secure coding standard by using the results from static analysis tool(s). |

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

The use of uniform software coding methods, standards, and/or criteria ensures uniform coding practices, reduces errors through safe language subsets, and improves code readability. Verification that these practices have been adhered to reduces the risk of software malfunction for the project during its operations and maintenance phases. Assuring the adherence of the developed software to the coding standards provides the greatest benefit when followed from software development inception to completion. Coding standards are selected at the start of the software development effort. Verification activities of the software work products include reviews, such as peer reviews and inspections (see [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures)), and assessments of how the coding standards are used to develop the software work products. The use of automated tools for assessing adherence to standards at appropriate reviews, or even on a batch mode run overnight, will assist the project team in adherence and verification.

This requirement exists to **ensure the integrity, security, and conformance of software code** to secure coding standards as part of NASA’s approach to software assurance. By leveraging **static analysis tools**, projects can identify, track, and resolve vulnerabilities and non-conformances early in the software development lifecycle, reducing operational risks and ensuring compliance with security expectations.

Below is the detailed rationale for each aspect of this requirement:

---

### **1. Early Detection of Vulnerabilities**

#### **Why It Matters:**

* Static analysis tools analyze source code **automatically and comprehensively**, uncovering vulnerabilities that may not be easily detectable during manual reviews or dynamic testing.
* Early identification of security issues like **buffer overflows**, **memory leaks**, or **input validation weaknesses** allows for cost-effective fixes and minimizes downstream risks during integration or operational phases.

#### **Supporting Argument:**

For example:

* Detecting a potential **SQL injection vulnerability** in a database query module during development avoids catastrophic failure later when the system is in operation.
* Early mitigation of common coding flaws, such as improper error handling or insecure API usage, reduces the likelihood of system exploits by malicious actors.

---

### **2. Adherence to Secure Coding Standards**

#### **Why It Matters:**

* Secure coding standards (e.g., SEI CERT, MISRA, OWASP) establish best practices for safe development in various programming languages and environments. These standards offer guidance on avoiding known weaknesses, such as hardcoded secrets, race conditions, or improper memory management.
* Verifying code compliance ensures that all team members are consistently applying these best practices across the software project.

#### **Supporting Argument:**

Without enforcing the use of a secure coding standard:

* Teams may inadvertently introduce security flaws, such as unsafe pointer operations in C/C++ or improper permissions handling in Python/Java.
* Static analysis ensures that non-conformance to project-secure coding standards is flagged and can be addressed systematically.

---

### **3. Objective, Repeatable, and Scalable Assessment**

#### **Why It Matters:**

* Static analysis tools provide **objective and repeatable assessments** of source code. This is critical in ensuring that the verification process is not prone to human error, bias, or subjectivity.
* Larger codebases and complex systems make manual reviews unfeasible, while static analysis tools scale efficiently as the project grows.

#### **Supporting Argument:**

For instance:

* Reviewing thousands (or millions) of lines of code manually for compliance with secure coding standards is impractical for large NASA projects.
* Automated static analysis tools (e.g., SonarQube, Fortify, Coverity) can quickly scan the entire codebase and generate detailed reports, pointing to specific lines of code that violate secure coding guidelines.

---

### **4. Increased Reliability and Mission Assurance**

#### **Why It Matters:**

* Many critical issues in scientific, aeronautical, and space missions stem from software flaws. Verifying code compliance ensures that vulnerabilities, bugs, or unexpected behaviors are proactively addressed.
* Secure code minimizes risks such as:
  + **Operational failures** caused by unhandled edge cases or resource exhaustion.
  + **System compromise** via cyberattacks targeting unprotected entry points in software.
  + **Data corruption or loss**, particularly in systems handling telemetry, navigation, or sensitive mission-related information.

#### **Supporting Argument:**

* A secure and conformant codebase increases the reliability of mission-critical systems, ensuring they behave as expected across conditions.
* For NASA, this is particularly important given the cost of failure—not just in financial terms, but also in terms of mission success, national security, and human safety.

---

### **5. Compliance with Industry and NASA Standards**

#### **Why It Matters:**

* This requirement aligns with both internal **NASA policies** (e.g., NPR 7150.2, NASA-STD-8739.8) and **industry best practices**, such as the use of **static analysis tools** for consistent enforcement of coding standards.
* Many security certifications (e.g., for safety-critical systems) mandate the use of static analysis tools to ensure compliance with secure coding standards.

#### **Supporting Argument:**

* NASA’s adherence to policies regarding software safety (per NPR 7150.2) requires that code is analyzed and verified against secure coding guidelines.
* Alignment with industry standards (e.g., CERT, MISRA) and cybersecurity frameworks (e.g., NIST SP 800-53, ISO/IEC 27001) ensures systems are "built for security" and reduces risk across the software supply chain.

---

### **6. Quality Assurance Through Objective Evidence**

#### **Why It Matters:**

* Static analysis tools produce **detailed, auditable evidence** to verify code compliance with cybersecurity guidelines. This enhances transparency, ensures accountability, and allows for corrective actions.
* Results from these tools serve as a foundation for project managers to measure compliance, track resolution of vulnerabilities, and demonstrate adherence to secure coding practices to NASA oversight entities.

#### **Supporting Argument:**

* Objective evidence strengthens project reviews, audits, and IV&V assessments, ensuring that the software product is secure and meets all contractual, regulatory, and mission requirements.
* Using consistent metrics (e.g., percentage of resolved non-conformances) allows the project manager to track progress over time.

---

### **7. Establishing a Culture of Secure Software Development**

#### **Why It Matters:**

* Regular use of static analysis tools reinforces a culture where developers value **secure coding** and understand its importance to mission success.
* Developers receive actionable feedback on code quality and security issues, improving their skills and reducing errors in future projects.

#### **Supporting Argument:**

* Developers can correlate tool results to specific secure coding rules, which raises awareness about common mistakes and improves adherence to secure coding practices.
* This "shift-left" approach integrates security early in development, fostering better coding habits in the long term.

---

### **8. Cost Savings**

#### **Why It Matters:**

* Identifying and fixing defects during the coding phase (via static analysis) is significantly less expensive than addressing issues during testing, system integration, or post-deployment.

#### **Supporting Argument:**

* Studies show that the cost of fixing defects increases exponentially as they progress downstream in the software lifecycle.
* For example, a vulnerability introduced in development might cost 2-10x more to fix during testing and 100x or more to fix after deployment.

---

### **9. Independent and Objective Verification**

#### **Why It Matters:**

* As part of software assurance, project managers must ensure that security measures are implemented independently of developer claims. Static analysis provides **independent verification** that enforces secure coding practices unbiasedly.

#### **Supporting Argument:**

* Without independent verification, there’s a greater risk of missed vulnerabilities due to human error or oversight.
* By requiring static analysis results, project managers avoid reliance solely on manual reviews or engineering team assurances.

---

### **10. Enables Continuous Improvement**

#### **Why It Matters:**

* Static analysis tools generate reports that not only identify violations but also provide **historical trend data**, helping project managers identify recurring issues and institute process improvements.

#### **Supporting Argument:**

* Trend analysis enables the team to focus on weaknesses by identifying code sections or development processes prone to errors.
* Records from historical static analysis results can inform future projects, reducing the recurrence of similar vulnerabilities.

---

### **Conclusion:**

Requiring the project manager to **verify software compliance by using static analysis results** ensures that secure coding practices are **consistently enforced, vulnerabilities are detected early, and high-risk flaws are mitigated proactively**. This requirement aligns with NASA’s commitment to mission assurance, cybersecurity, and system reliability. By leveraging static analysis tools, the project manager balances the need for rigorous, scalable compliance checks with the practical challenges of secure software development.

# 3. Guidance

## 3.1 Verification To Coding Standards

Verification of developed software adherence to coding standards is a critical activity that ensures software quality, maintainability, safety, and security throughout the software lifecycle. It plays a pivotal role in detecting vulnerabilities, improving design consistency, avoiding common coding errors, and ensuring compliance with defined coding principles and project goals. Below is the improved guidance, which strengthens existing practices and addresses gaps to better meet the intent of Requirement 3.1.

---

### **Importance of Verification to Coding Standards**

Verification ensures:

* **Consistency**: Uniform code style and practices across developers and components.
* **Quality**: Reduction in programming errors, vulnerabilities, and non-compliances.
* **Early Detection**: Early identification of coding flaws saves time and cost during later testing phases.
* **Support for Maintenance**: Adherence to coding standards ensures better readability and ease of future modifications.
* **Security**: Reliable implementation of secure and safety-critical coding practices reduces risks of system compromise or mission failure.

---

### **1. Selection of Coding Standards**

#### **Guidance**:

* **Early Selection**: Coding standards should be selected at the **start of the software development lifecycle** during the planning phase.
  + Examples of commonly used coding standards include:
    - **SEI CERT** for secure development in C and C++.
    - **MISRA C/MISRA C++** for embedded and automotive systems requiring safety and reliability.
    - **JSF AV C++** for safety-critical and aerospace-focused systems.
    - **AUTOSAR C++** for adaptive automotive software.
    - **OWASP Secure Coding Practices** for web and server applications.
  + Standards should be chosen based on project requirements, programming language, and domain-specific safety or security needs.

#### **Objective**:

Ensure the selected coding standards meet the **security, maintainability, readability, and performance goals** of the software project.

---

### **2. Continuous Verification Across the Development Lifecycle**

#### **Guidance**:

* **Early and Continuous**: Verification should be performed throughout all phases of development (design, implementation, testing) rather than waiting until the final review.
* **Integration with Development Workflow**:
  + Incorporate static and automated tools into the Continuous Integration/Continuous Deployment (CI/CD) pipeline for **real-time feedback** on adherence.
  + Run tools on nightly builds or batch jobs if automated integration isn’t feasible.
  + Periodically perform manual reviews as a complementary step.

#### **Objective**:

Ensure that coding standards are continuously applied and verified, minimizing non-compliance or vulnerabilities as development progresses.

---

### **3. Automated Tools for Verification**

#### **Guidance**:

* **Static Analysis Tools**:

  + Leverage state-of-the-art tools such as **SonarQube**, **Fortify**, **Coverity**, **Checkmarx**, or others to **mechanically check compliance** with coding standards, detect coding issues, and identify vulnerabilities.
  + Configure tools for **pedantic mode and all warnings enabled** for maximum coverage.
  + Use tools with mission-specific custom checkers to validate compliance with naming conventions, coding style, security rules, and design requirements.
  + Close out **all tool warnings** (there should be none) before initiating formal reviews.
* **Compiler Settings**:

  + Enable **strict mode** during compilation to adhere to coding standards. Examples:
    - GCC: Use flags like `-Wall -Wextra -pedantic`.
    - Clang: Enable `-Weverything`.
  + Record compiler warning reports and resolve all issues before completing reviews.
* **Batch Runs**:

  + For tools not integrated into CI/CD workflows, automated batch runs (e.g., nightly scans or periodic collection of results) should be conducted to keep coding compliance in check.
  + Address flagged items from these batch runs promptly.

#### **Objective**:

Automated verification increases coverage efficiency and reduces the likelihood of errors being missed during manual reviews.

---

### **4. Peer Reviews and Inspections**

#### **Guidance**:

* **Complement Automation**:
  + Automated tools are effective but limited. Human expertise during **peer code reviews** complements tool-based validation, catching nuanced coding standard violations such as incorrect algorithm implementations or ambiguous variable names.
  + Use **review checklists** derived from coding standards and tailored to secure coding practices:
    - Example checklist items:
      * Are all inputs validated and sanitized before processing?
      * Are sensitive data properly encrypted?
      * Are recursion and memory usage safe?
      * Is error handling complete and does not expose sensitive system data?
* **Encourage Collaboration**:
  + Peer reviews should include developers familiar with the coding standard to ensure knowledge-sharing among the team.

#### **Objective**:

Ensure thorough analysis and compliance with coding standards through collaboration and human analysis beyond automated tools.

---

### **5. Training and Competence**

#### **Guidance**:

* **Training for Tools**:

  + Provide training sessions on using automated tools for static code analysis, adhering to programming standards, and interpreting tool outputs.
  + Train developers on resolving errors flagged by tools or compilers.
    - Examples:
      * How to address common issues like buffer overflows flagged by static analysis tools.
      * How to understand CWE mappings for detected vulnerabilities.
* **Coding Standards Training**:

  + Conduct training for development teams on coding standards prior to project kickoff. Training should focus on:
    - Common secure coding mistakes.
    - Best practices for the prescribed coding standards.
    - Integration of coding standards with project workflows.

#### **Objective**:

Equip the development team with the knowledge and tools to implement secure and standard-compliant code.

---

### **6. Limitations of Static Tools and Manual Best Effort**

#### **Guidance**:

* **Impossible to Verify Everything**:
  + Complete application of coding standards across large projects is practically impossible due to tool limitations and human oversight. Teams should aim for **best-effort compliance** by focusing on critical code sections and high-risk security areas.
    - Examples of critical focus:
      * Code handling sensitive data (e.g., authentication, credentials).
      * Code performing low-level memory allocations (e.g., in languages like C/C++).
      * Code that interfaces with external systems (e.g., APIs or network layers).
  + Combine several techniques (static analysis, manual reviews, fuzz testing, etc.) for better coverage.

#### **Objective**:

Provide reasonable assurance while acknowledging the practical limits of tools and manual processes.

---

### **7. Adopting Advanced Techniques**

#### **Guidance**:

* **Dynamic Analysis**:

  + Incorporate dynamic analysis tools such as **Valgrind**, **Memory Analyzer**, or **runtime testing frameworks** to complement static checks by verifying behavior during execution.
  + Ensure dynamic testing covers scenarios such as:
    - Memory safety violations.
    - Input fuzzing to detect edge-case failures.
    - Multi-threading race conditions.
* **Software Fuzzing**:

  + Use fuzzing tools (e.g., **American Fuzzy Lop (AFL)** or **libFuzzer**) to inject random or invalid inputs into software modules and identify security weaknesses.
* **Model Checkers**:

  + For safety-critical systems, adopt model checking techniques to validate logic correctness and compliance with higher-level design constraints.

#### **Objective**:

Adopt additional advanced techniques to cover areas where static analysis tools may fall short.

---

### **8. Metrics and Progress Tracking**

#### **Guidance**:

* **Monitor Compliance Progress**:
  + Develop clear metrics for verifying coding standard compliance, such as:
    - Number of static tool warnings (open/closed).
    - Percentage of peer review findings resolved.
    - Overall code compliance percentages (derived from analysis reports).
* **Historical Trends**:
  + Track trends in compliance rates or recurring vulnerabilities across development cycles to identify and address process-level weaknesses.
  + Use historical metric data to improve future coding guidance and processes.

#### **Objective**:

Establish accountability through measurable indicators of compliance and improvement.

---

### **9. Addressing Non-Conformance**

#### **Guidance**:

* **Resolution Logs**:
  + Maintain logs of non-conformance issues found during analysis or manual reviews and document actions taken to resolve them.
* **Risk-Based Prioritization**:
  + Prioritize resolving non-conformances according to their potential impact on safety, security, or performance.

#### **Objective**:

Ensure complete closure of critical non-conformance issues prior to deployment.

---

### **Conclusion**

Verification to coding standards ensures a systematic approach to implementing software that adheres to security, quality, safety, and maintainability objectives. By combining **automated tools**, **peer reviews**, and **training**, this guidance strengthens development workflows and ensures adherence, even within complex systems or projects. Adopting analysis techniques, leveraging advanced methodologies, and tracking metrics further increase confidence that coding standards are achieved effectively. Teams must employ **best-effort compliance** to ensure robust and reliable software systems, especially for NASA missions.

**Software Certification – Coding, Code, and Coders**

ABSTRACT: "code is mechanically checked against the standards with the help of state of-the-art static source code analyzers..."

Paraphrasing from section 2.2 The Code  
"Code should be checked nightly for compliance with a coding standard and subjected to rigorous analysis with state-of-the-art (static source code analysis tools). The warnings generated by each of these tools are combined with the output of mission-specific checkers that secure compliance with naming conventions, coding style, etc. In addition, all warnings, if any (there should be none), from the standard C compiler, used in pedantic mode with all warnings enabled, should be provided to the software developers... (who) are required to close out all reports before a formal code review is initiated. In peer code reviews, an additional source of input is provided by designated peer code reviewers... Separately, key parts of the software design can be also checked for correctness and compliance with higher-level design requirements with the help of logic model checkers.”

[477](#_tabs-<p></p>)

See also [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training).

See also [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software), [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards), [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis), [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation), [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software), [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access), [PAT-022 - Programming Practices Checklist](/spaces/SITE/pages/115933208/PAT-022+-+Programming+Practices+Checklist),

See [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures)),

See also Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists)

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access)        * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-022 - Programming Practices Checklist](/spaces/SITE/pages/115933208/PAT-022+-+Programming+Practices+Checklist) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For small projects, the guidance for **verification to coding standards** should be practical, scalable, and tailored to the project's limited resources, schedule constraints, and smaller team size. While adhering to coding standards is mandatory, small projects can streamline the process by using lightweight tools, simplified processes, and focused reviews to meet the requirement effectively.

The following guidance is designed specifically for small projects:

---

### **1. Select Lightweight and Practical Coding Standards**

#### **Guidance**:

* **Choose Established Standards**: Select coding standards that suit your project's programming language and scope while being manageable for your team. For small projects, avoid overly complex or domain-specific standards unless mandated by the project requirements.

  + Examples:
    - **SEI CERT C** for C/C++ projects.
    - **MISRA C** for safety-critical or embedded systems (opt for core rules that align with project needs).
    - **OWASP Secure Coding Practices** for small web and server applications.
* **Tailor Standards to the Project**: Avoid excessive customization in coding standards for small projects to ensure they remain simple and can be verified easily.

#### **Why This Matters**:

Simple standards reduce the overhead for small teams and allow efficient adoption without compromising the project's goals.

---

### **2. Automate Verification When Possible**

#### **Guidance**:

* **Select Easy-to-Use Static Analysis Tools**: Use lightweight, user-friendly tools to automatically verify coding standard compliance without requiring complex setups.

  + Examples:
    - **SonarQube Community Edition**: Free, easy-to-configure for small teams.
    - **Cppcheck**: Lightweight static analysis for C/C++.
    - **PMD**: Source code analysis for Java.
    - **PyLint**: Python-specific static analysis tool.
* **Integrate Into Development Workflows**:

  + Run tools manually or integrate them into a simple Continuous Integration (CI) pipeline (e.g., GitHub Actions, GitLab CI/CD) for real-time feedback.
  + Automate nightly runs or batch scans to keep track of violations and issues.
* **Leverage Compiler Warnings**: Enable strict compiler warnings to catch inconsistencies or violations.

  + Examples:
    - For GCC/Clang: Use flags `-Wall -Wextra -pedantic`.
    - For Python: Enable `PyLint` with default rules.

#### **Why This Matters**:

Automation saves time, reduces manual effort for small teams, and ensures adherence to coding standards without adding significant overhead.

---

### **3. Perform Peer Reviews on High-Impact Sections**

#### **Guidance**:

* **Choose Critical Code for Manual Review**: Given limited resources, focus peer reviews on high-risk or high-impact code sections, such as:

  + Authentication modules.
  + Input/output validation functions.
  + Areas responsible for interacting with external systems (e.g., APIs, file handling).
* **Use a Simple Checklist**: Develop a lightweight checklist based on the selected coding standards. Example checklist:

  + Are all inputs sanitized and validated?
  + Are sensitive data (e.g., passwords) encrypted and not hardcoded?
  + Is error-handling implemented correctly without exposing system details?
  + Are loops, memory allocations, or recursion safe?

#### **Why This Matters**:

Manual peer reviews help uncover issues that automated tools can't detect while focusing team effort on areas of the code that pose the highest risk.

---

### **4. Limit Tools and Processes to What’s Necessary**

#### **Guidance**:

* **Avoid Tool Overload**: Small projects should use only one or two essential static analysis tools rather than complex toolchains that may exceed project resources.
* **Keep Verification Lightweight**: Focus on practical reviews and manageable compliance processes. Avoid excessive formal documentation or processes.
* **Batch Verification**: For very small teams, manual script-based checks or occasional use of static analysis tools may suffice where full automation is infeasible.

#### **Why This Matters**:

Small projects typically have constrained resources. Simplifying the verification approach ensures effort is focused on solving problems rather than managing tools or processes.

---

### **5. Train Developers on Coding Standards and Tools**

#### **Guidance**:

* **Conduct Mini-Training Sessions**: Provide a short training workshop or resource (e.g., 1-hour session or coding standard documentation) to familiarize the team with coding standards and analysis tools.
* **Focus Training on Applicable Tools**: Teach developers how to interpret and resolve issues flagged by static analysis tools. Examples:
  + Understanding flagged redundancies (e.g., unused variables).
  + Addressing flagged vulnerabilities (e.g., buffer overflow risks).

#### **Why This Matters**:

Proper training ensures developers can independently adhere to coding standards and effectively address analysis results without extensive oversight, which is vital for small teams.

---

### **6. Plan Verification Activities During Existing Milestones**

#### **Guidance**:

* **Integrate Verification into Routine Reviews**: Combine coding standard verification with existing peer reviews or milestone reviews (e.g., design, unit testing, integration testing). This reduces the need for standalone tasks.
* **Review Coding Standards Early**: Ensure coding standard verification begins early in the software development lifecycle, ideally starting with code implementation reviews.
* **Assign Responsibility**: For very small teams, assign coding verification as part of development tasks or to a dual-role engineer (e.g., developer + verifier).

#### **Why This Matters**:

Aligning verification tasks with existing milestones and multitasking within small teams minimizes scheduling conflicts and resource burdens.

---

### **7. Focus on Managing Risks**

#### **Guidance**:

* **Prioritize Risk Areas**: For small projects with limited resources, focus verification efforts on the code that poses the most significant security or operational risks. Examples:

  + Code managing external input (user data or API integrations).
  + Code responsible for data protection (e.g., encryption, secure communication).
  + Code directly tied to system-critical functionality (e.g., safety checks).
* **Respond to Tool Feedback**: Address critical warnings from tools promptly, while documenting and tracking open issues at lower priorities.

#### **Why This Matters**:

Small projects should aim for **risk-based priorities** rather than exhaustive compliance to ensure critical vulnerabilities are mitigated effectively.

---

### **8. Monitor Progress with Simple Metrics**

#### **Guidance**:

* **Non-Conformance Metrics**: Keep simple metrics to monitor the number of coding violations detected and resolved over time. Examples:

  + Open Violations = Total number of unresolved issues flagged by analysis tools.
  + Closed Violations = Total number of issues resolved across reviews.
  + Compliance Rate = Percentage of code verified against coding standards.
* **Focus on Trends in Key Metrics**: Track critical metrics to see steady improvement in adherence to coding guidelines while minimizing false positives.

#### **Why This Matters**:

Metrics provide small projects with a clear view of progress and compliance without requiring complex tracking systems.

---

### **9. Document Verification Efforts**

#### **Guidance**:

* **Keep Documentation Minimal**: For small projects, log essential verification efforts in simple formats, such as:

  + A coding guideline checklist marked with results during peer code reviews.
  + Verified analysis tool output files stored with comments (e.g., marking resolved issues).
  + A log of closed versus open flagged issues per tool-run date.
* **Capture Evidence for Reviews**: Ensure that verification outputs (tool results, review reports, issue logs) are available during formal project reviews or audits.

#### **Why This Matters**:

Minimal documentation allows small projects to meet accountability requirements without adding excessive effort.

---

### **10. Use the Best Effort Approach**

#### **Guidance**:

* **Prioritize Efforts Based on Constraints**: While exhaustive code compliance verification may be infeasible for small projects, teams should make a **best effort** to verify critical compliance areas (e.g., avoiding known vulnerabilities and risks).
* **Learn and Adapt**: Continuously identify areas where verification can be improved or streamlined for ongoing and future small projects.

#### **Why This Matters**:

A best-effort approach ensures small projects can maximize impact within limited constraints while still meeting coding standards effectively.

---

### **Small Project Example Workflow**

1. **Select Standards**:
   * Choose a lightweight secure coding standard (e.g., SEI CERT C for C projects).
2. **Automate Verification**:
   * Integrate a static code analysis tool into your workflow (e.g., SonarQube or Cppcheck).
3. **Perform Peer Reviews**:
   * Focus on high-risk sections of code during peer reviews using an easy checklist.
4. **Log Compliance Metrics**:
   * Maintain simple logs of coding warnings and resolutions.
5. **Train the Team**:
   * Provide short training on coding standards and tool usage.
6. **Iterate on Results**:
   * Address flagged issues promptly and prioritize the most critical violations.

---

### **Conclusion**

This streamlined approach to coding standard verification aligns with small project constraints while ensuring compliance with Requirement 3.1. By leveraging lightweight tools, targeted verification activities, focused reviews, and minimal documentation, small projects can achieve secure and quality software delivery without overstretching their resources.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-476)

  [NESC report on Alternative Software Programming for Human Spaceflight,](http://slideplayer.com/slide/12119033/ "Click to open in new window")

  Michael Aguilar, NASA Engineering and Safety Center, October 21, 2014.
* (SWEREF-477)

  [Software Certification – Coding, Code, and Coders,](https://pdfs.semanticscholar.org/cc9e/074f90d73ff1d389b85dbafcec30a82a9330.pdf "Click to open in new window")

  Klaus Havelund and Gerard J. Holzmann Laboratory for Reliable Software (LaRS) Jet Propulsion Laboratory, California Institute of Technology 4800 Oak Grove Drive, Pasadena, California, 91109-8099.
* (SWEREF-664)

  [Software Security](https://nen.nasa.gov/web/coding "Click to open in new window")

  OCE site in NASA Engineering Network, Portal that houses information for software developers to develop code in a secure fashion,  Formerly known as "Secure Coding"
* (SWEREF-665)

  [NATIONAL VULNERABILITY DATABASE](https://nvd.nist.gov/ "Click to open in new window")

  NVD is the U.S. government repository of standards based vulnerability management data represented using the Security Content Automation Protocol (SCAP).
* (SWEREF-666)

  [CVE List](https://cve.mitre.org/cve/ "Click to open in new window")

  CVE® is a dictionary of publicly disclosed cybersecurity vulnerabilities and exposures that is free to search, use, and incorporate into products and services, per the terms of use.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA maintains a rich database of lessons learned (available internally via the **NASA Lessons Learned Information System (LLIS)**). Relevant lessons provide insight into the importance of verifying software compliance with coding standards and avoiding issues that could impact safety, security, and mission success. Below are some examples derived from publicly available lessons learned and research in the context of coding standards and verification.

---

### **Lesson 1: Importance of Adherence to Coding Standards**

#### **Lesson Learned**:

* **Case Study**: An embedded system project had difficulty debugging intermittent failures due to inconsistent adherence to coding standards for safe memory handling in C code. Developers implemented system-critical components without following safe memory allocation practices, leading to **buffer overflows** during rapid memory usage cycles.
* **Key Takeaway**:
  + Coding standards such as **SEI CERT C** include rules for safe memory handling (e.g., eliminating the use of `malloc`/`free` without proper error checking). These standards were not enforced, resulting in system crashes and delays in fault resolution.
* **Recommended Practice**:
  + Use **static analysis tools** to verify compliance with memory safety rules and ensure standards are enforced consistently.
* **Relevant Requirements**:
  + Aligns with 3.1 as continuous verification of coding standards could have prevented the issue.

---

### **Lesson 2: Use of Static Analysis Tools to Detect Vulnerabilities**

#### **Lesson Learned**:

* **Case Study**: During the development of mission-critical software for aerospace applications, data corruption occurred due to unhandled edge cases in error handling routines. While dynamic testing identified the issue late, static code analysis tools could have flagged missing error-handling code earlier.
* **Key Takeaway**:
  + Static analysis tools are invaluable for finding vulnerabilities like **race conditions**, **uninitialized variables**, or **error-handling omissions** during development.
* **Recommended Practice**:
  + Integrate static analysis tools in regular CI workflows to flag and resolve errors before final testing.
* **Result**:
  + NASA projects now recommend running **nightly static compliance checks** to prevent similar issues.
* **Relevant Requirements**:
  + Reinforces Requirement 3.1’s emphasis on verifying adherence to coding standards through static analysis.

---

### **Lesson 3: Coding Standards Reduce Security Vulnerabilities**

#### **Lesson Learned**:

* **Case Study**: A NASA program encountered delayed system delivery due to unpatched **security vulnerabilities** in third-party libraries. Developers failed to follow secure coding practices outlined in project coding standards when integrating external libraries, resulting in exposure to **OpenSSL vulnerabilities** that could allow potential exploits.
* **Key Takeaway**:
  + Secure coding standards typically include guidance for validating third-party libraries (e.g., checking for known vulnerabilities and ensuring strong encryption). These practices minimize risks when relying on external code.
* **Recommended Practice**:
  + Projects should enforce secure coding standards using **automated static analysis tools** that flag weaknesses in third-party libraries and ensure compliance.
* **Result**:
  + NASA incorporated stricter coding standard verification processes for third-party libraries, requiring **traceability of vulnerabilities resolution to guidelines like NIST and OWASP**.
* **Relevant Requirements**:
  + Demonstrates how Requirement 3.1 applies in managing third-party software compliance within the development process.

---

### **Lesson 4: Training Is Critical to Coding Standards Compliance**

#### **Lesson Learned**:

* **Case Study**: A NASA software project faced recurring issues due to a lack of developer knowledge about secure coding practices. Newly hired developers struggled to follow pre-established standards and misinterpreted static analysis results, leading to unresolved findings and repeated issues.
* **Key Takeaway**:
  + Knowledge gaps in secure coding standards increase the risk of coding non-conformance and vulnerabilities. Training ensures developers can understand, apply, and resolve issues flagged by static analysis tools.
* **Recommended Practice**:
  + Conduct **secure coding training sessions** and align team practices with coding standards. Include training on correct usage of static and dynamic analysis tools.
* **Result**:
  + Following this lesson, training modules were integrated into NASA’s development lifecycle to ensure coding standard compliance.
* **Relevant Requirements**:
  + Supports training recommendations in Requirement 3.1 and emphasizes building competence for standard compliance.

---

### **Lesson 5: Manual Peer Reviews Complement Automated Tools**

#### **Lesson Learned**:

* **Case Study**: During the early phases of developing a safety-critical application, NASA engineers relied heavily on automated analysis tools to verify compliance with coding standards. While the tools effectively flagged routine issues (e.g., syntax violations, unsafe inputs), critical design flaws (e.g., incorrect algorithm implementation) were overlooked.
* **Key Takeaway**:
  + Automated tools help enforce coding standards but must be supplemented with **manual peer reviews** to identify higher-level flaws that tools may miss.
* **Recommended Practice**:
  + Peer reviews should focus on high-risk code sections (e.g., error handling routines, algorithms controlling safety-critical components) using standardized **checklists** aligned to coding standards.
* **Result**:
  + NASA improved the integration of manual peer reviews alongside automated tools for critical checks and formal code reviews.
* **Relevant Requirements**:
  + Reinforces Requirement 3.1’s emphasis on using both automated tools and manual reviews to verify adherence.

---

### **Lesson 6: Risk of Non-Conformance in Safety-Critical Systems**

#### **Lesson Learned**:

* **Case Study**: A NASA safety-critical system experienced unexpected behavior due to non-conformance with established coding standards for handling real-time constraints in embedded software. These non-conformances were missed during early verification processes due to inadequate static analysis coverage and reliance on undocumented practices.
* **Key Takeaway**:
  + For safety-critical systems, coding standard non-conformance has direct consequences on system reliability and mission success.
* **Recommended Practice**:
  + Use a **priority-based approach** for coding verification, emphasizing compliance in areas tied to safety, performance, and mission-critical features.
* **Result**:
  + NASA implemented stricter thresholds for safety-critical code reviews and enhanced static analysis configurations to improve coverage.
* **Relevant Requirements**:
  + Illustrates how Requirement 3.1 addresses critical verification for safety-sensitive systems.

---

### **Lesson 7: Simplifying Standards for Small Projects**

#### **Lesson Learned**:

* **Case Study**: A small NASA project struggled to comply with complex coding standards due to constraints in team size and expertise. Attempting to follow a heavily customized coding standard consumed excessive time and delayed delivery.
* **Key Takeaway**:
  + Simplified coding standards tailored to small project needs reduce overhead and improve compliance efficiency.
* **Recommended Practice**:
  + Focus on lightweight standards that address core issues (security, maintainability) while avoiding unnecessary complexity in verification processes. Use one or two static tools effectively.
* **Result**:
  + Small NASA projects now emphasize streamlining coding standards and verification processes to suit team size and system scope.
* **Relevant Requirements**:
  + Highlights tailored automation and minimalistic verification methods for Requirement 3.1 in small projects.

---

### **Leveraging Lessons Learned for Project Success**

#### **Key Recommendations**:

1. **Enforce Compliance with Tool-Aided Analysis**: Use static analysis tools to reduce human error and automate adherence checks.
2. **Complement Automation with Manual Review**: Conduct peer reviews to address critical flaws and nuances missed by tools.
3. **Prioritize Safety and Security Compliance**: Focus verification efforts on critical code areas before broadening coverage.
4. **Train Developers**: Educate teams on coding standards and introduce tool-specific training early.
5. **Tailor Processes for Small Projects**: Simplify coding standards and verification processes to fit project constraints.

---

### **Conclusion**

These NASA lessons highlight why verification to coding standards is vital for ensuring software reliability, security, and mission assurance. By addressing coding non-conformance risks, leveraging automated tools, training developers, and combining automated tools with manual reviews, Requirement 3.1 provides a clear framework for mitigating software risks and optimizing project success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Run static analysis on code developed for unit test](https://software.gsfc.nasa.gov/lesson-details/217/).**Lesson Number 217**: The recommendation states: "Static analysis tools should be run not only on flight code (or production code in non-flight cases), but also on code developed for unit test. The issues identified for all code should be properly dispositioned and resolved."

# 7. Software Assurance

**SWE-185 - Secure Coding Standards Verification**

3.11.7 The project manager shall verify that the software code meets the project’s secure coding standard by using the results from static analysis tool(s).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Analyze the engineering data or perform independent static code analysis to verify that the code meets the project’s secure coding standard requirements.

## 7.2 Software Assurance Products

### **Source Code Analysis**

#### **Updated Elements**

Software Assurance (SA) activities should go beyond superficial analysis and produce thorough, actionable products that demonstrate adherence to secure coding practices. Below is the enhanced guidance for SA products associated with secure coding compliance.

---

#### **1. Analysis of Engineering Results**

* SA is responsible for independently confirming that secure coding practices were implemented correctly in the software. This includes:
  + Verifying that **static code analysis results** demonstrate compliance with chosen coding standards.
  + Identifying errors, warnings, and anomalies in these results, then confirming their resolution.
  + Reviewing **peer review outcomes** as part of the verification process for compliance with the selected coding standards (e.g., SEI CERT, MISRA C).
* Document cases of **non-conformance**, including reasons for deviation, analysis of risks, and mitigation plans.

---

#### **2. Independent Static Code Analysis**

* SA should perform **independent static code analysis**:
  + **Verify Secure Coding Standard Compliance**:
    - Confirm alignment with the project's selected secure coding guidelines (e.g., MISRA C for embedded systems, SEI CERT C/C++ for safety/security-critical systems, or JSF AV C++ for aerospace).
    - Ensure all flagged code violations align with risk-based priorities (e.g., vulnerabilities affecting mission-critical functionality are addressed first).
  + **Assess Vulnerabilities and Weaknesses**:
    - Use the static analysis tool to focus not only on compliance but also on identifying potential cybersecurity vulnerabilities (e.g., buffer overflows, race conditions, injection flaws).
  + **Risk Evaluation**:
    - For non-conformance, SA will identify risks, assess severity, and provide regular feedback on associated impacts to the engineering team and management.

---

#### **3. Identification of Risks or Issues**

SA will capture and document a comprehensive risk evaluation with the following:

* The **severity** and **likelihood** of vulnerabilities/issues identified in the software.
* The **status** of vulnerabilities: categorized into Open, Mitigated, Closed (with resolutions evaluated independently).
* Suggestions for any **tool misconfigurations** that may be limiting the static analysis output.
* Any discrepancies between secure coding standards and coding implementation.

---

#### **4. Documentation Products**

* **Secure Coding Standards Document**: Ensure a central repository or artifact exists for the coding standards selected by the project. Include additional tailoring or supplemental rules as required for specific project contexts.
* **Analysis Reports**:
  + SA will maintain:
    - **Detailed Static Code Analysis Reports**, documenting the tool results prior to resolution and after the resolution of findings.
    - **Trend Analysis**: Tracking the reduction or recurrence of coding violations over time.
  + Review findings to identify recurring pain points in adherence (e.g., insufficient input sanitization routines, overuse of unsafe functions like `strcpy` or `malloc`).

## 7.3 Metrics

Metrics provide quantitative insights into how effectively coding standards are being enforced, tracked, and remediated. Below is an improved set of metrics to enhance process transparency and focus on actionable outcomes:

#### **1. Code Non-Conformance Metrics**

* **# of Non-Conformances Identified by Life Cycle Phase**:

  + Breakdown of violations identified per phase (e.g., design, implementation, testing).
  + Helps detect process-level deficiencies (e.g., recurring coding errors in the design vs. late identification during implementation).
* **# of Non-Conformances Raised by SA**:

  + Compare Non-Conformances raised by SA with the total raised (e.g., by both SA and engineering teams). SA may find gaps missed by engineering.

---

#### **2. Static Code Analysis Metrics**

* **Total Coding Issues**:

  + **# of Total Errors and Warnings** identified by analysis tools over time.
  + Categorized by **severity** (e.g., Critical, Major, Minor).
* **Resolution Rates**:

  + **# of Errors and Warnings Resolved** vs. **# of Total Errors and Warnings Identified**.
  + Track resolution trends and flag areas of poor responsiveness.
* **False Positives Metrics**:

  + Track tool reliability by comparing:
    - **# of Errors Identified as False Positives** vs. Total Errors and Warnings Identified.
    - Examples: Mark security-safe constructs incorrectly flagged due to tool limitations, and document engineering efforts in review logs.
* **Trend Metrics**:

  + Evaluate progress with **trends of Static Code Violations** over time (e.g., Open, Closed, by Severity).

---

#### **3. Security Metrics**

* **Cybersecurity Issues**:
  + **# of Vulnerabilities and Weaknesses Identified** (e.g., CWE categories like buffer overflows, input validation issues) and their resolution status (Open, Closed).
* **Coding Standard Violations**:
  + **# of Violations by Type, Severity, and Resolution**: Focus on errors tied specifically to secure coding rules.
  + Example: Unsafe access of restricted APIs might require both a code rewrite and updated policy.

---

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

#### **1. Confirm and Understand Secure Coding Standards**

* **Confirm Secure Coding Standards**:
  + Verify that the selected standard incorporates secure coding practices relevant to your project’s language, scope, and complexity.
  + Examples:
    - **SEI CERT Guidelines**: Offers extensive rules for memory safety, input validation, and error handling.
    - **MISRA C/C++**: Focus on predictable and safe implementations for embedded systems.
    - Use **language-specific rules** to guide implementation (avoid duplication of efforts across standards).

#### **2. Implement Tight Integration of Static Analysis Tools**

* Select **tools matched to the project’s language and scale**:
  + C/C++: **Cppcheck**, **Coverity**, **Fortify**, **SonarQube**.
  + Python: **PyLint**, **Bandit**.
* **Run Static Analysis Regularly**:
  + Incorporate automated tools into **CI/CD pipelines** (e.g., nightly runs or post-commit scans).
* **Independent Analysis by SA**:
  + Ensure Software Assurance runs independent code scans to confirm results submitted by the development team.

---

#### **3. Address Non-Conformances Fully**

* **Resolve Findings**:
  + Ensure the engineering team addresses **critical findings as a priority**. For unresolved findings, document:
    - Context as to why they were not addressed.
    - Evidence that the issue poses minimal or no risk.
* **Review Engineering Tool Outputs**:
  + Ensure the engineering team has configured static analysis tools to flag relevant coding violations and is resolving issues systematically.

---

#### **4. Beyond Static Analysis: Additional Security Analysis Techniques**

* **Dynamic Execution Analysis**:
  + Test code execution under real-world conditions to uncover runtime issues like memory leaks or race conditions.
  + Example tools: Valgrind, Helgrind.
* **Attack-based Testing**:
  + Leverage fuzzing techniques to validate input handling against unexpected inputs or threats.
  + Tools: American Fuzzy Lop (AFL), libFuzzer.
* **Boundary Analysis in Testing**:
  + Adopt boundary-based security checks (input constraints) on all identified external interfaces in code modules.

---

#### **5. Provide Feedback Loops**

* **Iterate Process Improvements**:
  + Evaluate static analysis reports for patterns of recurring issues, missed standards, or tool configuration gaps. Use this feedback to improve engineering practices and standards documentation.

---

### **Conclusion**

This revamped software assurance guidance focuses on producing actionable, risk-driven outcomes that foster adherence to secure coding standards. By providing independent verification, ensuring thorough analysis, and creating a feedback loop between SA and engineering teams, projects can proactively identify and address weaknesses. These efforts enhance quality, safety, and security, ensuring mission success. The inclusion of meaningful metrics further enhances progress tracking and accountability.

A method of identifying weaknesses and vulnerabilities is to use the National Vulnerability Database [665](#_tabs-<p></p>) from NIST that is the U.S. government repository of standards-based vulnerability data. Software weaknesses can be identified using Common Weakness Enumeration (CWE) [666](#_tabs-<p></p>) - a dictionary created by MITRE.

See the secure coding site [664](#_tabs-<p></p>) for more information (NASA access only).

See also [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software)

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access)        * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-022 - Programming Practices Checklist](/spaces/SITE/pages/115933208/PAT-022+-+Programming+Practices+Checklist) |

# 8. Objective Evidence

Objective evidence serves as formal proof that the software project adheres to coding standards, allowing projects to demonstrate compliance during reviews, audits, and inspections.

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

Below are examples of recommended objective evidence that align with Requirement 3.1's focus on secure coding verification and static analysis.

---

### **1. Coding Standards Documentation**

#### **Objective Evidence**:

* **Approved Coding Standards**:
  + A documented coding standard tailored to the project (e.g., SEI CERT C, MISRA C/C++, OWASP Secure Coding Practices) signed off during the **planning phase**.
  + Ensure the document includes:
    - Chosen rules and guidelines specific to the programming language or system domain.
    - Security principles (e.g., secure data handling, memory safety).
    - Specific rule exceptions (if applicable) and rationale for deviations.

#### **Purpose**:

Demonstrates the team's adherence to an approved coding standard as the foundation of secure development practices.

---

### **2. Static Code Analysis Reports**

#### **Objective Evidence**:

* **Initial Analysis Reports**:

  + Raw output from the static analysis tool(s) used to evaluate source code (e.g., SonarQube, Coverity, Fortify, Cppcheck).
  + The report should include:
    - Total errors, warnings, and non-conformances identified.
    - Categorization by severity (Critical, Major, Minor).
    - Specific rule violations (e.g., memory leaks, unsafe function calls, insufficient error handling).
* **Post-Resolution Reports**:

  + Follow-up analysis reports after the team has resolved flagged issues and re-run the analysis tool.
  + Evidence of improvement, such as reduced non-conformances or closure of critical issues.

#### **Purpose**:

Provides quantitative evidence that coding standard violations were identified, prioritized, and resolved systematically.

---

### **3. SA Independent Analysis Results**

#### **Objective Evidence**:

* **Independent Static Code Analysis Results**:
  + Reports generated by Software Assurance (SA), independent of the development team, using static analysis tools or manual review.
  + The results should:
    - Verify compliance to the secure coding guidelines.
    - Include findings that align (or contrast) with those from engineering analysis.
    - Document SA recommendations for resolving non-conformances.

#### **Purpose**:

Allows SA to validate development claims while providing an additional layer of compliance assurance.

---

### **4. Peer Review Checklists and Logs**

#### **Objective Evidence**:

* **Peer Review Artifacts**:
  + Completed review checklists used to evaluate code compliance with the secure coding standard during manual code reviews.
  + Logs should include:
    - Checklist items such as memory safety, input validation, error handling routines, or naming conventions.
    - Issues flagged during the review, resolutions discussed, and closure details.
    - Signatures of reviewers verifying the review's completion.

#### **Purpose**:

Demonstrates stakeholder involvement in manual verification of secure coding practices.

---

### **5. Compliance Tracking Logs**

#### **Objective Evidence**:

* **Non-Conformance Resolution Tracker**:
  + A tracker documenting all identified non-conformances (e.g., coding standard violations, security vulnerabilities). The tracker should include:
    - Non-conformance description (e.g., unsafe code construct, unhandled inputs).
    - Severity classification (Critical, High, Medium, Low).
    - Resolution status (Open, In Progress, Closed).
    - Resolution details (e.g., changes made, updated code location).
    - Associated responsible party and completion date.
  + Trend Analysis:
    - Historical data showing improvement over time (e.g., reduction of non-conformances across development phases).

#### **Purpose**:

Evidence that violations are being systematically tracked and mitigated over time with clear accountability.

---

### **6. Tool Configuration Files and Settings**

#### **Objective Evidence**:

* **Tool Configuration Documentation**:
  + Documentation of the static analysis tool setup, including:
    - Rules selected from coding standards.
    - Exclusion rules (if applicable) and their rationale.
    - Thresholds for severity levels.
    - Integration details with the CI/CD pipeline.
  + Examples:
    - A configuration file (e.g., `.yml`, `.json`) showing coding standards mapped into the static analysis tool.
    - Documentation confirming how specific rules (e.g., SEI CERT C buffer overflow checks) are enforced in the tool.

#### **Purpose**:

Proves that the tools have been properly configured to reliably assess the chosen coding standards.

---

### **7. Descriptions of Handled False Positives**

#### **Objective Evidence**:

* **False Positive Review Reports**:
  + List of issues flagged by the static analysis tool that were deemed false positives after engineering and/or SA review.
  + Documentation should include:
    - Tool rule violated (e.g., "unsafe function usage").
    - Justification for false positive classification.
    - Supporting evidence (e.g., alternate mechanism ensuring safety).
    - Sign-off by reviewers.

#### **Purpose**:

Ensures repeatability and accountability for handling false positives to improve process reliability.

---

### **8. Metrics Reports and Trend Analysis**

#### **Objective Evidence**:

* **Static Code Analysis Metrics**:
  + Reports defining progress in resolving coding violations over time, categorized by:
    - Severity category (Critical, Major, Minor).
    - Type of violation (e.g., memory safety, naming conventions, unvalidated inputs).
    - Resolution rates (e.g., percentage of resolved issues per cycle).
* **Trend Analysis**:
  + Visual charts showing trends over time:
    - Reduction in open violations.
    - Increased resolution rates.
    - Fewer recurring violations across development iterations.

#### **Purpose**:

Provides high-level quantitative evidence of compliance progress and refinement of coding practices.

---

### **9. Training Records**

#### **Objective Evidence**:

* **Training Attendance Documents**:
  + Records of developer and SA team members completing training on:
    - Secure coding practices.
    - Usage of static analysis tools.
  + Include sign-off sheets, training materials, or post-training quizzes as evidence of participation and understanding.
* **Training Outcomes Reports**:
  + Documentation showing how training participants applied their learning, such as fewer coding violations or more effective tool usage.

#### **Purpose**:

Proves that project teams are adequately trained to implement and verify secure coding practices.

---

### **10. Cybersecurity Vulnerability Assessment Report**

#### **Objective Evidence**:

* **Vulnerability Scan Results**:
  + Reports generated by specialized tools assessing cybersecurity vulnerabilities (e.g., Bandit for Python or Fortify for C/C++).
  + Includes:
    - Identified vulnerabilities and their severity classification.
    - Evidence of vulnerability resolution (e.g., code changes, retested scans).
    - Residual risks (if not fully mitigated) justified with an accompanying rationale.

#### **Purpose**:

Ensures robust consideration of cybersecurity risks and their mitigation during coding standard enforcement.

---

### **11. Audit and Compliance Summary Reports**

#### **Objective Evidence**:

* **Audit Records**:
  + Reporting on coding standard compliance conducted by SA teams during internal audits or reviews.
  + Evidence should include:
    - Findings from the audits categorized by risk.
    - Actions required to close gaps.
    - Evidence of closure for identified gaps (e.g., updated coding guidelines, fixed non-conformances).

#### **Purpose**:

Documents independent reviews of adherence to coding standards to validate compliance.

---

### **12. Configuration Management and Version Control Logs**

#### **Objective Evidence**:

* **Source Code Repository Logs**:
  + Histories showing evidence of fixes for flagged coding violations.
  + Documentation of configuration/version updates for coding standards or static analysis tools.

#### **Purpose**:

Provides traceability for changes made in response to coding standard verification activities.

---

### **Conclusion**

The objective evidence listed above ensures comprehensive documentation and verification of secure coding practices. By combining static analysis reports, manual review artifacts, metrics, training logs, and security vulnerability scans, development teams can demonstrate compliance effectively and transparently, supporting both project and mission assurance goals. Objective evidence aligned to Requirement 3.1 provides reviewers and stakeholders confidence in the project's adherence to coding standards and overall software reliability.
