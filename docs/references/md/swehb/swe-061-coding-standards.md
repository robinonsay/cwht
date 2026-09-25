# SWE-061 - Coding Standards

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695445. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards

SWE-061 - Coding Standards

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695445)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695445&showCommentArea=true&showComments=true#addcomment)

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

4.4.3 The project manager shall select, define, and adhere to software coding methods, standards, and criteria.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-061 History

SWE-061 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.3.2 The project shall ensure that software coding methods, standards, and/or criteria are adhered to and verified. |
| Difference between A and B | Added requirement to select coding methods, standards, and/or criteria. |
| B | 4.4.3 The project manager shall select, adhere to, and verify software coding methods, standards, and/or criteria. |
| Difference between B and C | Removed the requirement to verify. |
| C | 4.4.3 The project manager shall select and adhere to software coding methods, standards, and criteria. |
| Difference between C and D | Added the word 'define' |
| D | 4.4.3 The project manager shall select, define, and adhere to software coding methods, standards, and criteria. |

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
| * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |

# 2. Rationale

To ensure safety, security, reliability, quality, maintainability, readability, and testability of the NASA code products.

Software coding methods, standards, and criteria form the foundation of a consistent, maintainable, and reliable software development process. Establishing and enforcing these principles ensures code quality, promotes collaboration, supports regulatory compliance, and minimizes risks during software development and maintenance lifecycle phases.

Below are detailed reasons that justify the rationale for this requirement:

---

### **1. Ensuring Code Consistency**

* **Rationale:** A consistent coding style across the project minimizes ambiguity for both current developers and future maintainers of the software.
  + Coding methods provide a unified approach to structuring, testing, and documenting code, simplifying understanding for all team members, including newcomers.
  + Standards eliminate variability in code implementation styles, which reduces errors introduced by differing personal preferences in programming.
  + Example: Using consistent naming conventions, indentation, and formatting improves code readability and reduces the time required for collaboration, reviews, and debugging.

---

### **2. Improving Software Quality**

* **Rationale:** Adhering to predefined coding standards ensures adherence to industry best practices and helps deliver high-quality software.
  + Standards encourage the use of proven, reliable programming constructs, reducing the likelihood of introducing unsafe or error-prone practices.
  + Code quality criteria ensure that artifacts meet requirements for performance, maintainability, scalability, modularity, and security.
  + Example: Standards like MISRA-C for safety-critical C programs enforce rules that prevent usage of potentially unsafe language features (e.g., uninitialized variables or undefined behaviors).

---

### **3. Facilitating Collaboration and Integration**

* **Rationale:** On large or distributed teams, coding standards ensure that multiple developers can contribute to the same project effectively.
  + Common methods improve communication between developers, software testers, and software assurance personnel by presenting uniform code conventions.
  + Standardized interfaces between modules improve interoperability and simplify integration and reuse of code across systems and subsystems.
  + Example: A team working on different components of an embedded control system will need to follow consistent interface definition methods to enable seamless integration when modules are combined.

---

### **4. Supporting Standards Compliance and Certification**

* **Rationale:** Many NASA systems and mission-critical software projects operate in regulatory environments that require adherence to software standards to ensure safety and reliability.
  + Examples include compliance with **NASA-STD-8739.8 (Software Assurance Standard)**, **ISO 26262 (Functional Safety)**, or other mission-specific software safety standards.
  + Well-defined coding standards provide traceability and verifiability during audits or third-party certification processes, ensuring software readiness for flight or deployment.

---

### **5. Enhancing Code Maintainability**

* **Rationale:** Standardized code is easier to maintain, debug, refactor, and extend over the long term.
  + Projects often have turnover in personnel over their lifespans, requiring new team members to quickly understand the existing codebase. Well-structured code reduces the learning curve.
  + Code that adheres to clear criteria is easier to update when requirements change or when bug fixes are needed in the post-deployment phase.
  + Example: Modular code with documented interfaces allows a developer to make improvements without needing to understand the entire system.

---

### **6. Supporting Automation and Tooling**

* **Rationale:** Consistently styled code facilitates automated checks and refactoring using static analysis tools and linters.
  + Many tools validate source code against coding standards, enabling automated enforcement of rules for quality, security, and maintainability.
  + Adherence to methods like modular design and encapsulation improves the effectiveness of automated testing and code generation tools.
  + Example: Static analysis tools such as **SonarQube** or **Coverity** can help identify coding vulnerabilities, unmaintained legacy constructs, or unsafe practices when the code conforms to specific standards.

---

### **7. Reducing Project Risks**

* **Rationale:** Ensuring adherence to coding standards minimizes risks related to software errors, rework, security vulnerabilities, and system failures.
  + Poorly written software increases the risk of defects or unpredictable behavior in the system, especially for safety-critical or mission-critical software.
  + Enforcing strict criteria reduces the probability of errors introduced by ambiguous or non-standard implementation approaches.
  + Example: Enforcing checks for buffer overflows and memory leaks in coding rules mitigates potential risks in embedded systems used for space missions.

---

### **8. Supporting Reuse of Software Components**

* **Rationale:** Standardization allows software components to be reused across multiple projects and missions.
  + Reusable code saves time and cost for future development efforts while ensuring similar reliability and quality as the original implementation.
  + Example: NASA has a history of reusing flight software components designed for earlier missions (e.g., Mars rovers) in new missions, enabled by adherence to strict coding methods and modular software design.

---

### **9. Reducing Defect Rates Early in Development Cycle**

* **Rationale:** Coding standards help developers detect and mitigate issues in earlier phases.
  + When well-defined criteria and methods are followed, errors such as undefined behaviors, type mismatches, or memory management issues are reduced during the coding phase.
  + Example: Enforcing standards like redundant error handling for file I/O operations mitigates defects that might otherwise be discovered only during rigorous testing or production use.

---

### **10. Meeting Safety and Security Requirements**

* **Rationale:** Many NASA systems involve safety-critical and mission-critical components where any malfunction can lead to catastrophic system failures or the loss of mission objectives.
  + Secure and safety-focused coding criteria address vulnerabilities like memory corruption, race conditions, or invalid accesses that could compromise the integrity of the system.
  + Example: Requiring input validation and sanitization for all external inputs prevents buffer overflows and security exploits.

---

### **Examples of Coding Standards and Guidance**

To implement and enforce this requirement, the project manager should select appropriate coding methods, standards, and criteria such as:

* **MISRA-C/C++:** For safety-critical systems in C or C++.
* **Effective C++ practices:** Focused on object-oriented programming reliability.
* **Pylint and PEP8:** For Python projects.
* **NASA-STD-8739.8:** Software assurance and safety as per NASA's standards.
* **Center-Specific Standards:** Localized standards from Goddard, JPL, or other NASA centers tailored to specific domains or projects.

---

### **Conclusion**

This requirement ensures that the project manager formally selects, defines, and enforces best practices and standards for the software development process. Doing so ensures that the software meets its intended requirements with high reliability, safety, and maintainability. By fostering consistency, improving quality, reducing risks, and supporting compliance, adherence to coding methods, standards, and criteria is essential to the success of NASA’s software-intensive missions.

# 3. Guidance

NASA programs and projects have multi-year life cycle times. Often the software personnel who develop the original software work products move on to other projects. These developers are then backfilled on the team by other developers for the remainder of the development, operations, maintenance, and disposal phases of the life cycle. This personnel turnover process may occur several times during the project's life cycle. The use of uniform software coding methods, standards, and/or criteria ensures uniform coding practices, reduces errors through safe language subsets, and improves code readability. Verification that these practices have been adhered to reduces the risk of software malfunction for the project during its operations and maintenance phases.

See also [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software),

There are five key benefits of using coding standards:

1. Understanding, maintainability, and readability of the code.
2. Consistent code quality — no matter who writes the code.
3. Software security from the start.
4. Reduced development costs.
5. Testability of the code.

Coding standards help prevent or reduce unsafe coding practices such as defect-prone coding styles, security issues from specific coding sequences, and numerous coding errors, mistakes, and misunderstandings.

**NESC report on Alternative Software Programming for Human Spaceflight**

"Coding standards are the ‘materials and manufacturing standards’ for implemented software...  
Human-rated certification and mission-critical software both require applying a recognized coding standard, one that is supported by automated analysis tools, for all software required to be certified for human spaceflight and mission-critical applications. Manual verification is all but impossible.

The reduction in effort by simply adhering to a coding standard that can be tested through automation is the one certification process that truly has no other efficient verification method. ... As security becomes an issue, security coding standards should also be applied.”

[476](#_tabs-<p></p>)

### **1. Importance of Coding Standards in NASA Projects**

#### **Longevity of Projects**

NASA programs and projects often span decades across their life cycles, including development, deployment, operation, maintenance, and eventual retirement. During this time:

* **Workforce Turnover:** Original software developers frequently move to other projects, and incoming team members inherit responsibility for the codebase. Consistent coding methods, standards, and criteria ensure continuity and facilitate onboarding for new team members.
* **Reduced Risk:** Uniform coding practices help maintain quality, minimize the introduction of defects, and ensure that software is readable and maintainable well beyond the initial development phases.

#### **Key Benefits of Coding Standards**

Adhering to coding standards provides significant benefits, particularly in NASA's software development context, where safety, reliability, and security are paramount:

1. **Enhanced Readability and Maintainability:** Uniform structure and styles make it easier for teams to collaborate on, understand, and modify the code.
2. **Higher Code Quality:** Consistent practices help avoid defect-prone patterns, reducing the likelihood of runtime issues.
3. **Intrinsic Security:** Coding standards integrate secure practices from the start, helping prevent vulnerabilities such as buffer overflows or unsafe memory usage.
4. **Cost and Time Savings:** Prevention of errors early in the process reduces debugging and troubleshooting effort, lowering overall development costs.
5. **Improved Testability:** Code developed according to standards is easier to test, automate, and verify for critical functionality.

#### **Certification and Critical Software**

For NASA’s human-rated and mission-critical hardware, adherence to a recognized coding standard (e.g., MISRA-C, CERT C) and the use of automated static analysis tools are industry best practices. Manual verification of large-scale systems is impractical, making automated verification against coding standards essential to detect vulnerabilities and ensure compliance.

---

### **2. General Coding Standard Guidance**

#### **Planning for Coding Standards**

* Coding standards should be identified, tailored (if necessary), and adopted **during project initialization** to align the team with expected practices.
* Use existing standards where possible (e.g., MISRA-C, CERT C, or NASA-specific standards), modifying them only to meet specific project requirements.
* Early planning ensures that software artifacts are developed with sufficient foresight for maintainability and compliance.

#### **Key Distinction: Coding Standards vs. Coding Style**

* **Coding Standards:** Define rules and practices to ensure code correctness, safety, reliability, and security.
  + Includes how variables are to be declared, when specific language features (e.g., recursion, global data) should be avoided, and how exceptions are handled.
* **Coding Style:** Concentrates on improving code readability (e.g., indentation, naming conventions, formatting).

#### **Correlation With Defect Prevention**

* Research shows that specific coding rules have been directly tied to defect prevention. Enforcing these rules reduces errors caused by unsafe patterns, ambiguous constructs, and undefined behaviors.
* Example: Avoiding unsafe constructs like `gets()` and enforcing proper use of memory allocation functions helps eliminate predictable runtime errors.

#### **Outsourcing Considerations**

When software development is outsourced, having clear coding standards ensures contractors deliver high-quality code that meets NASA’s requirements. Standards should:

* Be integrated into contracts and work agreements.
* Be paired with compliance verification steps (e.g., regular static analysis checks, peer reviews).

---

### **3. Practical Guidelines for Coding Standards**

#### **Classification of Standards**

Coding standards are commonly classified by:

1. **Language:** Provide specific rules tailored to a chosen programming language (e.g., MISRA-C for C, PEP 8 for Python).
2. **Usage:** Address applicable scenarios such as embedded systems, real-time operations, or distributed systems.
3. **Severity Levels:** Define criticality for rules, such as:
   * *Mandatory:* Must be followed under all situations.
   * *Advisory:* Strongly recommended; deviations require justification.
   * *Permissive:* Optional based on project needs.

#### **Essential Coding Standard Coverage**

Standards should cover the following aspects:

1. **Code Structure:**
   * Organization of projects, including source files, classes, and resources.
   * Limits on module size to improve readability and testability.
2. **Error and Exception Handling:**
   * Rules for handling errors gracefully and consistently.
   * Logging and recovery mechanisms to ensure system reliability during failures.
3. **Use of Libraries:**
   * Safe usage of operating system libraries, runtime environments, and commercial routines.
4. **Global Data Restrictions:**
   * Discourage or prohibit the use of global variables to reduce side effects and promote encapsulation.
5. **Safe Language Subsets:**
   * Avoid constructs prone to undefined behavior, such as unsafe type casting, unsigned/signed comparisons, or floating-point precision assumptions.
6. **Format, Naming, and Comments:**
   * Readability practices, such as consistent indentation and meaningful variable/method names.
   * Sufficient comments to explain *why* code was written a certain way, not just *how* it works.

---

### **4. Tools and Automated Verification**

#### **Role of Automation**

* Automated tools (e.g., static analyzers like Coverity, SonarQube, Klocwork, or Polyspace) are critical for continuously monitoring adherence to coding standards.
* These tools can:
  + Check code nightly for standards compliance.
  + Generate reports identifying violations, which developers must resolve before advancing in the development lifecycle.
  + Verify compliance with industry standards such as ISO/IEC TS 17961 for secure coding.

#### **Recommendations for Automated Analysis**

1. Run nightly automated checks to enforce continuous standards adherence.
2. Combine outputs from coding standard compliance tools and compiler warnings (e.g., using compilers in **pedantic mode** with all warnings enabled).
3. Use mission-specific static checkers to identify project-specific rule violations.

---

### **5. Verification and Assessment**

#### **Verification Activities**

* Incorporate coding standard adherence checks into key software reviews:
  + **Peer Reviews:** Involve designated team members to identify deviations from the standards.
    - Use formal checklists to capture compliance.
  + **Formal Inspections:** Ensure software outputs pass rigorous inspection before reaching the next lifecycle phase.
* Review reports from automated tools as part of the verification process.

#### **Training**

* Provide training to the development team on:
  + Selected coding standards.
  + Proper use of static analysis and logic model checking tools.
  + Security vulnerabilities and how to mitigate them while writing code.

#### **Legacy and Human-Rated Software**

* For software intended for human-rated or safety-critical systems, apply stricter review processes and ensure adherence to the highest levels of secure coding standards to protect against runtime errors and external exploits.

---

### **6. Example Standards and References**

1. **MISRA-C:** Enforces safe C programming practices suitable for safety-critical systems.
2. **CERT-C:** Focuses on secure coding practices to prevent vulnerabilities and exploits.
3. **NASA-STD-8739.8:** Provides guidance and assurance processes for NASA software development.

#### **Documentation of Standards**

* An organization's coding standards can be maintained as a general repository, with project-specific amendments to address unique needs.
* Clear documentation ensures standards are easily understood and uniformly applied.

---

### **7. Conclusion**

This guidance highlights the essential role of coding methods, standards, and criteria in NASA’s software development processes. Their adoption ensures high-quality, secure, reliable, and maintainable software, critical to mission success. In practice:

* Create a clear coding standard at project initiation.
* Validate adherence using systematic reviews and automated tools.
* Train development teams to understand and apply the standards throughout the project lifecycle. By following these principles, NASA projects can mitigate risks, reduce costs, and deliver software engineered for the rigorous demands of space exploration and mission safety.

To assist you in fulfilling this requirement, interpret the text in section 1 as "software coding methods," "software coding standards," and "software coding criteria." Also, interpret the terms "methods" and "criteria" as indicative of the software developer's style.

**Software Certification – Coding, Code, and Coders**

“Code should be checked against the standards with the help of state-of-the-art static source code analyzers. ... Flight code should be checked nightly for compliance with a coding standard and subjected to rigorous analysis with state-of-the-art (static source code analysis tools). The warnings generated by each of these tools are combined with the output of mission-specific checkers that secure compliance with naming conventions, coding style, etc. Also, all warnings, if any (there should be none), from the standard C compiler, used in pedantic mode with all warnings enabled, should be provided to the software developers... (who) are required to close out all reports before a formal code review is initiated. In peer code reviews, an additional source of input is provided by designated peer code reviewers... Separately, key parts of the software design can also be checked for correctness and compliance with higher-level design requirements with the help of logic model checkers.”[477](#_tabs-<p></p>)

**NESC report on Alternative Software Programming for Human Spaceflight**

“The CERT C Secure Coding Standard is composed of 89 rules and 132 recommendations for producing secure code.  It is recommended that compliance with a standard like CERT C be performed by a static analyzer, depending on program size and complexity.  A source code static analysis tool meeting ISO/IEC TS 17961 conformance is recommended.

The following quote from the author of the second edition of the CERT C Coding Standard describes what static analysis for conformance can imply.

While the application of these rules and recommendations does not guarantee the security of a software system, it does tell you ...that the software was developed to a set of industry-standard rules and recommendations developed by the leading experts in the field. ... that ...time and effort went into producing code that is free from the common coding errors that have resulted in numerous vulnerabilities ...over the past two decades ... that the software developers who produced the code have done so with a real knowledge of the types of vulnerabilities that can exist and the exploits that can be used against them, and consequently have developed the software with a real security mindset.”

[476](#_tabs-<p></p>)

See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access), [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification), 

See [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures)), and assessments of how the coding standards are used to develop the software work products.

See also Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

See also [PAT-022 - Programming Practices Checklist](/spaces/SITE/pages/115933208/PAT-022+-+Programming+Practices+Checklist)

## 3.6 Checklists Relevant To Languages

The checklists below contain specific checks and things to be aware of in certain languages:

* [6.5 - Checklist for C Programming Practices](/spaces/SWEHBVD/pages/102695570/6.5+-+Checklist+for+C+Programming+Practices)
* [6.6 - Checklist for C++ Programming Practices](/spaces/SWEHBVD/pages/102695576/6.6+-+Checklist+for+C+Programming+Practices)
* [6.7 - Checklist for Ada Programming Practices](/spaces/SWEHBVD/pages/102695582/6.7+-+Checklist+for+Ada+Programming+Practices)
* [6.8 - Checklist for Fortran Programming Practices](/spaces/SWEHBVD/pages/102695586/6.8+-+Checklist+for+Fortran+Programming+Practices)
* [6.9 - Checklist for Generic (Non-Language-Specific) Programming Practices](/spaces/SWEHBVD/pages/102695593/6.9+-+Checklist+for+Generic+Non-Language-Specific+Programming+Practices)
* [6.10 - Checklist for General Good Programming Practices](/spaces/SWEHBVD/pages/102695600/6.10+-+Checklist+for+General+Good+Programming+Practices)
* [6.11 - Examples of Programming Practices for Exception Handling](/spaces/SWEHBVD/pages/102695607/6.11+-+Examples+of+Programming+Practices+for+Exception+Handling)

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification)        * [6.5 - Checklist for C Programming Practices](/spaces/SWEHBVD/pages/102695570/6.5+-+Checklist+for+C+Programming+Practices) * [6.6 - Checklist for C++ Programming Practices](/spaces/SWEHBVD/pages/102695576/6.6+-+Checklist+for+C+Programming+Practices) * [6.7 - Checklist for Ada Programming Practices](/spaces/SWEHBVD/pages/102695582/6.7+-+Checklist+for+Ada+Programming+Practices) * [6.8 - Checklist for Fortran Programming Practices](/spaces/SWEHBVD/pages/102695586/6.8+-+Checklist+for+Fortran+Programming+Practices) * [6.9 - Checklist for Generic (Non-Language-Specific) Programming Practices](/spaces/SWEHBVD/pages/102695593/6.9+-+Checklist+for+Generic+Non-Language-Specific+Programming+Practices) * [6.10 - Checklist for General Good Programming Practices](/spaces/SWEHBVD/pages/102695600/6.10+-+Checklist+for+General+Good+Programming+Practices) * [6.11 - Examples of Programming Practices for Exception Handling](/spaces/SWEHBVD/pages/102695607/6.11+-+Examples+of+Programming+Practices+for+Exception+Handling) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-022 - Programming Practices Checklist](/spaces/SITE/pages/115933208/PAT-022+-+Programming+Practices+Checklist) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For small projects, the scope, budget, and timeline are typically more constrained than large-scale endeavors. However, adhering to coding methods, standards, and criteria is equally critical to ensure software reliability, maintainability, and security. The following simplified guidance is tailored for small projects to streamline the process while maintaining quality and compliance.

---

### **1. Start Simple: Use Existing Standards and Tools**

#### **Leverage Established Standards**

* Avoid creating custom coding standards for small projects unless absolutely necessary. Instead, adopt readily available and well-documented standards such as:
  + **MISRA-C** for C-based safety-critical systems.
  + **PEP 8** for Python projects.
  + **CERT C** for secure coding practices across critical C programs.
  + NASA’s **STD-8739.8** for software assurance and safety-critical requirements (if applicable).

#### **Use Tools for Automation**

* Simplify verification by relying on free or affordable static analysis tools designed for the selected coding language:
  + **For C/C++:** Use tools like **Cppcheck**, **Clang-Tidy**, or **SonarQube Community Edition**.
  + **For Python:** Use tools like **Pylint** and **Bandit**.
  + **For Java:** Use tools like **Checkstyle** or **SpotBugs**.
* These tools:
  + Automatically enforce adherence to coding standards.
  + Highlight potential bugs, code smells, and security vulnerabilities.

---

### **2. Tailor Standards to Small Project Needs**

#### **Focus on Essential Rules**

* Small projects do not always require the strict enforcement of hundreds of coding rules. Instead, focus on a small subset of essential rules that address:
  + Code maintainability and readability.
  + Safe memory management.
  + Error handling and logging practices.
  + Security practices to prevent common vulnerabilities.

#### **Keep It Lightweight**

* Publish a one- or two-page **coding standard document** with guidelines relevant to the project’s scope. Key contents may include:
  + Naming conventions (e.g., camelCase for variables, PascalCase for classes).
  + Module size restrictions (e.g., limit a function to 50 lines of code).
  + Rules for global variables and memory use (e.g., "do not use uninitialized variables").
  + Error-handling protocols (e.g., "all exceptions must be logged").
  + Testability practices (e.g., "every function must have corresponding unit tests").

---

### **3. Planning and Integration**

#### **Set Expectations Early**

* Define and adopt coding methods, standards, and criteria at the **start of the project** to align the team on expectations.
* For small teams or solo developers:
  + Use a shared document repository (e.g., GitHub, GitLab, or Bitbucket) to store the coding standard and ensure visibility.
  + Include a coding practice checklist as part of project planning.

#### **Low Overhead for Compliance**

* For small teams, perform **lightweight peer reviews** to verify adherence during regular team meetings or at each milestone.
* Use Continuous Integration (CI) to automatically check standards compliance during builds (e.g., GitHub Actions, GitLab CI with integrated linters).

---

### **4. Ensure Traceability to Project Goals**

#### **Align With Project Requirements**

* Even in small projects, each coding standard or criterion should link directly to project goals, such as:
  + Meeting mission-critical objectives (e.g., for experimental hardware or prototypes).
  + Ensuring security and accuracy for sensitive data handling.
  + Reducing the likelihood of defects in the operational environment.

#### **Traceability Practices**

* Keep the design and code tightly aligned with requirements:
  + Use a simple **traceability matrix** to map requirements → design → code modules.
  + For teams with minimal resources, consider using a spreadsheet for this purpose.

---

### **5. Efficient Verification and Testing**

#### **Static Code Analysis**

* Run static code analysis tools regularly during development (e.g., once per day during active coding). They can identify:
  + Violations of naming and formatting conventions.
  + Memory leaks, null pointer dereferences, or use of unsafe library functions.
  + Security vulnerabilities, such as missing input sanitization.

#### **Peer Reviews (Lightweight)**

* Regular peer reviews ensure that coding standards are being followed while avoiding an onerous process for small teams:
  + Use a simple **coding standard checklist** during each review.
  + Focus on detecting issues early, such as inconsistent formatting, poor module design, or unsafe practices.
  + Example Checklist Items:
    - Did this code adhere to the error-handling guidelines?
    - Are variables named appropriately and consistently styled?
    - Are complex or risky operations (e.g., recursion, dynamic memory allocation) justified and clearly documented?

---

### **6. Security Considerations for Small Projects**

#### **Adopt Secure Coding Practices**

* Even small systems are vulnerable to attacks and bugs if secure coding practices are not implemented:
  + Avoid using unsafe functions like `gets()` in C.
  + Sanitize all inputs to prevent injection attacks and data corruption.
  + Implement proper error logging while taking care not to expose sensitive data via logs.

#### **Use Minimal Tooling**

* Security practices do not have to be resource-intensive:
  + Use tools like **Bandit** for Python or **Flawfinder** for C/C++ to scan for common vulnerabilities.
  + Follow simple recommendations from CERT C or OWASP for web-related projects.

---

### **7. Practical Example for Small Projects**

Imagine a small team working on a Python project to control a science instrument.

#### **Adopting Standards**

* Use **PEP 8** (Python coding style) for naming conventions and formatting.
* Document the team's additional rules, such as:
  + "Avoid global variables—use parameter passing between functions."
  + "All exceptions must include meaningful error messages and be logged in `errors.log`."
* Enforce standards automatically with **Pylint**.

#### **Verification Process**

* Each developer runs **Pylint** before committing code changes.
* Before a milestone, the team runs automated static analysis tools and conducts a short peer review using a coding standards checklist.

#### **Delivering Results**

* Publish a one-page document summarizing adherence to the standards at the end of development.
* Include key metrics, such as output from static tools (e.g., % compliance with PEP 8).

---

### **8. Final Recommendations for Small Projects**

1. **Start with Simplicity:**

   * Choose one or two widely accepted coding standards and stick to them.
   * Avoid over-complicating by adding unnecessary rules.
2. **Automate Whenever Possible:**

   * Use lightweight tools to automate compliance checks.
   * Schedule these checks regularly through CI pipelines.
3. **Train Developers Quickly:**

   * Provide team members with a short training session or tutorial on the key coding rules.
4. **Document and Enforce:**

   * Maintain a simple coding standard document.
   * Use code reviews and static analysis to ensure compliance.
5. **Keep It Iterative:**

   * Periodically review your coding standards and verification processes to ensure they’re practical for small project constraints.

---

By following these streamlined recommendations, small projects can effectively apply Requirement 4.4.3, ensuring consistency, reliability, and maintainability without unnecessary overhead. These practices support the successful completion of small-scale development efforts while ensuring compliance with NASA standards and best practices.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-006)

  [The Importance of a coding standard and the benefits of adhering to it](http://www.jrtwine.com/Articles/CodingStyles/CStyle1.htm "Click to open in new window")

  Twine, J.R. (2003).
* (SWEREF-007) WBS Checklist Tool,
   NASA Goddard Space Flight Center (GSFC), 2007.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-077)

  ["Guide to the software detailed design and production phase",](http://www.esa.int/TEC/Software_engineering_and_standardisation/TECBUCUXBQE_0.html "Click to open in new window")

  ESA PSS-05-05, Issue 1, Revision 1, ESA Board for Software Standardisation and Control, 1995.  The PSS family of standards was the ESA internal set of standards which was replaced by ECSS. It inluded a software engineering standard and a set of guides. This page contains the cited resource as well as others in the collection.
* (SWEREF-161)

  [Coding Standards and Code Reviews,](http://msdn.microsoft.com/en-us/library/aa291591%28v=vs.71%29.aspx "Click to open in new window")

  MSDN Library, 2003. Accessed May 23, 2011 from http://msdn.microsoft.com/en-us/library/aa291591%28v=vs.71%29.aspx. Checked 6/10/2019, document retired and no longer available, need to find suitable replacement
* (SWEREF-162)

  [Coding Standards in C Sharp,](http://ezinearticles.com/6122965 "Click to open in new window")

  Milan Malkani, 2011. Accessed May 20, 2011 at http://ezinearticles.com/6122965.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-199)

  [MISRA-C:2004 - Guidelines for the Use of the C Language in Critical Systems](http://caxapa.ru/thumbs/468328/misra-c-2004.pdf "Click to open in new window")

   MISRA Consortium, ISBN 0 9524156 2 3 (paperback), ISBN 0 9524156 4 X (PDF), October 2004.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-326) Software Coding Standards Parasoft®.  This document is not available but other development resources may be found at http://www.parasoft.com
* (SWEREF-476)

  [NESC report on Alternative Software Programming for Human Spaceflight,](http://slideplayer.com/slide/12119033/ "Click to open in new window")

  Michael Aguilar, NASA Engineering and Safety Center, October 21, 2014.
* (SWEREF-477)

  [Software Certification – Coding, Code, and Coders,](https://pdfs.semanticscholar.org/cc9e/074f90d73ff1d389b85dbafcec30a82a9330.pdf "Click to open in new window")

  Klaus Havelund and Gerard J. Holzmann Laboratory for Reliable Software (LaRS) Jet Propulsion Laboratory, California Institute of Technology 4800 Oak Grove Drive, Pasadena, California, 91109-8099.
* (SWEREF-510)

  [Mars Pathfinder Flight Software Development Process (1997)](https://llis.nasa.gov/lesson/590 "Click to open in new window")

  Public Lessons Learned Entry: 590.
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-563)

  [Static Software Analysis of the NASA Autonomous Flight Termination Software](https://llis.nasa.gov/lesson/24503 "Click to open in new window")

  Public Lessons Learned Number: 24503, Lesson Date 2018-08-23, Submitting Organization:
  NESC,
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

### **Lessons Learned from NASA’s History with Coding Standards**

The **NASA Lessons Learned database** provides key insights into the importance of coding standards based on prior mission experiences. These lessons underscore the role of coding standards in ensuring maintainability, cost control, and error reduction in projects across the software development lifecycle. The following entries from the database provide critical lessons for implementing coding standards effectively:

#### **1. Software Design for Maintainability**

**Lesson Number 0838**

* **Key Insight:** Software maintenance represents one of the largest cost drivers for NASA systems. Early and consistent planning for maintainability—using appropriate coding standards, styles, and configuration management—can significantly reduce life cycle costs.
* **Implication for Coding Standards:**
  + By establishing consistent coding practices upfront, maintenance efforts (e.g., bug fixes, enhancements) are made simpler and less error-prone.
  + Projects should ensure that coding standards are well-documented and accessible to all developers during the entire lifecycle, from initial development through decommissioning.

---

#### **2. Mars Pathfinder Flight Software Development Process (1997)**

**Lesson Number 0590**

* **Key Insight:** The Mars Pathfinder project demonstrated the benefit of tailoring coding standards to the needs of a specific project. However, this tailoring must balance the need for flexibility against the costs associated with future upgrades and reuse potential.
* **Key Takeaways for Coding Standards:**
  + Developing customized, project-specific coding standards can optimize project success; however:
    - Tailored standards may need to be harmonized or redefined for future upgrades or if the code will be reused in new mission contexts.
  + Consider the balance between tailoring and standardization:
    - If extensive code reuse is anticipated, strive to maintain alignment with broader NASA, industry (e.g., MISRA-C, CERT C), or widely-used standards.

---

#### **3. Static Software Analysis of the NASA Autonomous Flight Termination Software**

**Lesson Number 24503**

* **Key Insights:**
  1. **Specify Detailed Coding Standards:** Coding standards should be explicitly chosen and applied to all relevant software, including both flight software and ground utilities.
  2. **Optimize Static Analysis Tools:** The configuration of static analysis tools should match the established coding standard. This ensures that the tool functions as an effective verification asset.
  3. **Define Issue Resolution Processes:** The project team should define clear processes for reviewing and resolving issues flagged by static analysis. Guidelines should specify:
     + What constitutes a defect.
     + Which issues require mandatory correction.
* **Recommendations for Projects:**
  + Define coding standards early, and configure static analysis tools accordingly to validate compliance systematically.
  + Include fault resolution procedures in the coding standard policy to avoid ambiguity during verification.

---

### **Key Application of Lessons Learned to Small and Large Projects**

These historical lessons emphasize NASA's ongoing focus on the importance of disciplined and consistent coding practices. Regardless of project size, the following actions should be taken to incorporate these lessons effectively:

1. **Adopt Standards Early:**

   * Incorporate coding standards into project planning and allocate resources for training and verification.
   * Small projects should leverage existing, well-established coding standards to reduce the overhead associated with tailoring.
2. **Configure Tools for Compliance:**

   * Make use of static analysis tools that are compatible with the selected coding standards. For instance:
     + **Ground and Flight Software Example:** Configure tools like Klocwork, Coverity, or Polyspace to enforce MISRA-C or CERT C for C language projects.
     + Clearly document which errors or warnings are actionable.
3. **Prioritize Maintainability:**

   * Use consistent coding practices to lower the burden of ongoing maintenance, especially for long-duration projects with multiple personnel transitions.
4. **Reuse and Tailoring:**

   * When tailoring standards, account for potential future reuse of the code. Reuse potential may dictate a higher alignment with established NASA or industry-wide standards rather than significant deviations.
5. **Review Processes:**

   * Formalize coding standard adherence as a criterion for peer reviews, static analysis reports, and milestone inspections to minimize the potential for unforeseen defects.

---

### **Integrating Lessons Learned into Current NASA Projects**

Using the lessons from past projects, the following procedural steps can help integrate coding standards effectively into NASA projects:

1. **Establish Standards and Tools:**

   * Define coding standards in the project's requirements specification document.
   * Select a static analysis tool that aligns well with the chosen coding standard.
2. **Operationalize Lessons:**

   * Clearly define how issues flagged by static tools will be classified, managed, and resolved.
   * Ensure the project schedule includes time for static analysis, issue resolution, and fixing flagged problems prior to formal reviews.
3. **Monitor and Improve Practices:**

   * Use lessons learned repositories as a dynamic input to refine and improve coding standards for future software efforts.

---

### **Examples of Common Lessons to Implement in Practice**

**Lesson/Application:** For projects reusing code from prior missions:

* Take into account compatibility between the original coding standards of the reused software and the new project’s expected standards.

**Lesson/Application:** When adopting static analysis tools:

* Configuration must be customized for the coding standard in use. For example, ensuring the tool can detect unsafe practices specifically disallowed by MISRA-C (e.g., disallowed global variable usage, recursion, or unchecked pointer operations).

**Lesson/Application:** Early identification of coding inconsistencies:

* Schedule periodic (e.g., nightly or weekly) static analysis runs as part of the continuous integration pipeline, allowing the team to identify and resolve issues early.

---

### **Key Takeaways**

Combining insights from the NASA Lessons Learned database with modern practices allows project managers to ensure coding standards are not just a set of rules, but a valuable tool for improving software quality, reducing costs, and ensuring mission success. Leveraging these insights will create a robust foundation for the continued success of NASA’s software systems across their extended life cycles.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Provide template(s) to facilitate developing documentation](https://software.gsfc.nasa.gov/lesson-details/61/). **Lesson Number 61**: The recommendation states: "Use of template(s) and a delivery schedule can help with required documentation."
* [Consistent array indexing philosophy and naming conventions](https://software.gsfc.nasa.gov/lesson-details/76/). **Lesson Number 76**: The recommendation states: "Reach an agreement on a consistent array indexing philosophy, and naming conventions, and ensure it is communicated throughout the project teams (FSW, Systems Engineering and Operations teams)."
* [Engage early with experts from previous missions](https://software.gsfc.nasa.gov/lesson-details/135/). **Lesson Number 135**: The recommendation states: "Engage early with experts from previous missions to understand their data standards."

# 7. Software Assurance

**SWE-061 - Coding Standards**

4.4.3 The project manager shall select, define, and adhere to software coding methods, standards, and criteria.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assure the project manager selected and/or defined software coding methods, standards, and criteria.

2. Analyze that the software code conforms to all required software coding methods, rules, and principles.

## 7.2 Software Assurance Products

#### **Static Analysis of the Source Code**

* Perform static analysis of the source code against the established coding standard. This helps identify:
  + Violations of coding rules (e.g., non-conformance with naming conventions, unsafe use of memory, or uninitialized variables).
  + Potential bugs or vulnerabilities in the code (e.g., buffer overflows, null pointer dereference, or unchecked return values).
  + Security issues in compliance with a **secure coding standard** (e.g., CERT C, CWE Top 25 weaknesses).

#### **Independent Evaluation of Source Code**

* **SA Independent Analysis:** The software assurance team should independently assess the software code for compliance with the project’s coding standard, as well as other coding principles, methods, and rules.
  + Evaluate the effectiveness and coverage of static analysis results provided by the development team.
  + Identify risks or concerns related to deviations from coding standards, such as unexpected complexity, security vulnerabilities, or maintainability issues.
  + Provide actionable feedback to project managers and development teams for improvements.

#### **Key Deliverables for SA Verification of Code Against Coding Standards**

1. **Coding Standard Document Verification:**
   * Ensure coding standards (including secure and safety-critical coding standards, if applicable) are clearly defined and documented for the project.
2. **Static Code Analysis Results:**
   * Verify that static analysis results demonstrate compliance with the coding standard.
     + Use automated tools to validate coding violations (e.g., SonarQube, Coverity, Klocwork).
3. **SA Risk Reports:**
   * Provide reports detailing risks, issues, and recommendations to address coding violations.

---

## 7.3 Metrics

Effective metrics support continuous improvement and provide a quantitative way to track adherence to coding standards and resolution of issues.

#### **Recommended Metrics for Coding Standards**

* **Total Number of Coding Standard Violations Identified:**

  + Open (violations that remain unresolved).
  + Closed (violations resolved during the project phase).
  + Classification by severity level (e.g., critical, major, or minor) and type (e.g., style, security, maintainability, performance-related).
  + Trend tracking across lifecycle phases to identify recurring patterns.
* **Total Number of Non-Conformances:**

  + Track software process **non-conformances** by life cycle phase over time, identifying areas where adherence to coding standards is lacking or requires improvement.
* **Other Metrics:**

  + Percentage of compliance with the coding standard (e.g., % of files/modules that adhere to the rules).
  + Number of identified critical security vulnerabilities and time taken to resolve them.
  + Number of repeated violations (indicating areas needing additional focus or training).

#### **Reference:**

For additional metric-related guidance, see **Topic 8.18: SA Suggested Metrics**.

---

## 7.4 Updated Guidance

#### **Task 1: Understand and Familiarize With Project Coding Standards**

* **Plan Review:**

  + Review the project software development or management plan to determine the coding standards, methods, and principles defined for the project (e.g., safe coding practices, secure coding standards, guidelines for reliability).
  + Verify that the standards are comprehensive and well-suited to the project's requirements (flight software, mission-critical software, ground utilities, etc.).
  + Coding standards could include:
    - Secure coding standards (e.g., CERT C, MISRA-C).
    - Guidelines for safe use of constructs, error handling, and reliability principles.
    - Specific principles for high-assurance embedded or flight software.
* **Analysis of Development and Selection Processes:**

  + During the review of the **software plans (SWE-013)**, ensure that the coding standards align with industry or NASA-specific requirements.
  + Confirm the inclusion of best practices and principles to address project-specific challenges (e.g., mission-critical requirements, safety-critical system requirements).
* **Use of Static Analysis Results:**

  + Analyze results from static analysis tools provided by the development team. Look for patterns of recurring issues that indicate inconsistent use of coding standards or unsafe practices.
  + Examples of issues:
    - Violations of rules governing the use of global variables.
    - Non-compliance with memory usage rules, such as violations of memory allocation/deallocation.
    - Use of unsafe constructs in multithreaded environments (e.g., race conditions, deadlocks).
* **Reporting Issues:**

  + Identify risks or issues from static analysis reports and escalate unresolved violations or critically severe problems to project management.
    - Example risks might include unaddressed buffer overflows, inadequate exception handling, or failure to prevent known vulnerabilities like injection attacks.
  + Provide a summary report to assist project management in understanding project risk and deciding on corrective action priorities.

---

#### **Task 2: Perform Independent Static Code Analysis**

* **Independent Verification:**

  + Software assurance should run independent static analysis tools or use a second configuration to validate the development team’s adherence to coding standards. Ensure that both static analysis use cases are in agreement:
    1. Validation of coding standard compliance.
    2. Detection of potential errors and risks not identified by the development team.
* **Well-defined Issue Review Process:**

  + Develop a process to review results of static code analysis to:
    - Determine the criticality of each issue.
    - Highlight coding violations requiring immediate correction (e.g., issues affecting mission safety, human safety, or system reliability).
    - Separate false positives for meaningful, actionable outputs.
  + Define criteria for closing issues to ensure consistency in the resolution process.
* **Communication and Reporting:**

  + Share detailed results of independent static analysis with project management and relevant stakeholders. Include:
    - Types of coding violations detected and proposed resolutions.
    - Recommendations regarding specific code that may require refactoring or closer oversight.
    - Insights on developer responses to violations and opportunities for improvement in coding practices.
* **Documentation:**

  + Retain all results and verification findings as part of the project record.
  + Document trends and leverage the information to refine coding standards and static analysis rules for future projects.

---

## 7.5 Recommendations for Success

1. **Select Tools Aligned With the Coding Standard:**

   * Ensure static analysis tools support the coding standards used in the project. For example:
     + **MISRA:** Polyspace, Coverity, Klocwork.
     + **CERT C/Secure Coding:** Coverity, Flawfinder.
     + For multi-language projects, select tools that support multiple languages (e.g., SonarQube).
2. **Perform Continuous Verification:**

   * Schedule regular static analysis runs (e.g., nightly or at major development milestones).
   * Independent static analysis by software assurance can be staggered or run in tandem for critical phases.
3. **Integrate SA Into Team Practices:**

   * Engage software assurance early in the project to ensure coding standards are well-defined and practical for the development team.
   * Use regular communication to resolve potential risks collaboratively.
4. **Training and Awareness:**

   * Train developers and assurance personnel on the importance of coding standard adherence, secure coding practices, and related tool usage.
   * Share recurring static analysis trends to help improve the team’s response to coding violations.

By rigorously implementing and independently verifying adherence to coding standards, software assurance ensures that the project minimizes risks, improves maintainability, and upholds NASA’s emphasis on delivering high-quality software systems.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification)        * [6.5 - Checklist for C Programming Practices](/spaces/SWEHBVD/pages/102695570/6.5+-+Checklist+for+C+Programming+Practices) * [6.6 - Checklist for C++ Programming Practices](/spaces/SWEHBVD/pages/102695576/6.6+-+Checklist+for+C+Programming+Practices) * [6.7 - Checklist for Ada Programming Practices](/spaces/SWEHBVD/pages/102695582/6.7+-+Checklist+for+Ada+Programming+Practices) * [6.8 - Checklist for Fortran Programming Practices](/spaces/SWEHBVD/pages/102695586/6.8+-+Checklist+for+Fortran+Programming+Practices) * [6.9 - Checklist for Generic (Non-Language-Specific) Programming Practices](/spaces/SWEHBVD/pages/102695593/6.9+-+Checklist+for+Generic+Non-Language-Specific+Programming+Practices) * [6.10 - Checklist for General Good Programming Practices](/spaces/SWEHBVD/pages/102695600/6.10+-+Checklist+for+General+Good+Programming+Practices) * [6.11 - Examples of Programming Practices for Exception Handling](/spaces/SWEHBVD/pages/102695607/6.11+-+Examples+of+Programming+Practices+for+Exception+Handling) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-022 - Programming Practices Checklist](/spaces/SITE/pages/115933208/PAT-022+-+Programming+Practices+Checklist) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is essential to demonstrate compliance with Requirement 4.4.3 for software coding practices. The evidence should directly show that appropriate coding methods, standards, and criteria were selected, defined, and adhered to throughout the software development lifecycle. Below are examples of good objective evidence that can be collected:

---

### **1. Documentation Evidence**

#### **Coding Standards Document**

* A formal document that details the coding standards adopted for the project.
  + May include references to industry standards (e.g., MISRA-C, CERT C, PEP 8) or project-specific standards.
  + Clearly defines rules for:
    - Code formatting and structure.
    - Error handling and logging conventions.
    - Secure coding practices (e.g., input validation, memory management).
    - Restricted use of unsafe programming constructs.
    - Language-specific guidance (e.g., specific compilers, libraries, or runtime environments).
* Should include guidelines to tailor the standards for project-specific requirements.

#### **Software Development Plan (SDP)**

* Evidence that coding standards were identified and included in the software development process.
* The SDP should outline:
  + How coding standards are enforced (e.g., reviews, static analysis tools).
  + Roles and responsibilities for ensuring compliance.
  + Tools and methods used for verification.

#### **Configuration Management Plan**

* Documents the processes for managing source code to ensure consistency, including:
  + Version control system setup (e.g., Git, SVN).
  + Procedures for maintaining compliance with the coding standard during development.
  + Access restrictions and change control procedures.

#### **Coding Guidelines Training Record**

* Evidence that developers and software assurance personnel were provided training on the coding standards.
  + Training session records, agendas, and attendance logs.
  + Materials used in training, such as presentations and handouts, to confirm the team is aware of the project's coding requirements.

#### **Tailoring Records**

* Documents that explain how the adopted coding standards were customized, modified, or clarified to meet specific project needs.
  + Tailoring justification for exceptions or deviations.
  + Risk analysis and approvals related to tailoring.

---

### **2. Verification and Validation Evidence**

#### **Static Code Analysis Results**

* Reports from static analysis tools showing compliance with the coding standards and identifying any violations.
  + Tools used (e.g., SonarQube, Coverity, Klocwork, Polyspace).
  + Issues flagged, categorized by severity (e.g., critical, major, minor).
  + Trend analysis results showing improvements over time.
  + Metrics such as:
    - Number of violations detected (open/closed breakdown).
    - Severity distribution of violations.
    - Recurrent violations or patterns of non-compliance.

#### **Code Review Records**

* Audit trail of peer reviews or formal code inspections, including:
  + Coding standard checklists used for reviews.
  + Reviewer feedback and comments on code compliance.
  + Records of issues identified during the review.
  + Documentation showing resolution of issues, such as code changes or justification for exceptions.

#### **Verification Reports**

* Written assurances from software assurance personnel confirming adherence to coding standards. These reports should summarize:
  + Results of static analysis and code reviews.
  + Risk or issue logs documenting problems discovered during the review and corrective actions taken.

---

### **3. Implementation and Maintenance Evidence**

#### **Audit Logs**

* Logs from Continuous Integration (CI) or automated builds that routinely validate adherence to coding standards. For example:
  + Output from nightly builds or CI pipelines that integrate static analysis tools.
  + Warnings, errors, and their resolution timelines.

#### **Examples of Standard-Compliant Code**

* Code snippets or repository samples with proper adherence to the coding standards documented in the project.
  + Formatting, naming conventions, module structures, and error-handling routines should reflect the documented guidance.

#### **Deviation Logs**

* Records describing instances where coding standards were intentionally or unintentionally not followed, including:
  + Identified exceptions approved by the project manager.
  + Log of unauthorized deviations with root cause analysis and corrective actions.
  + Evidence that deviations were resolved before deployment.

#### **Test Cases and Results**

* Evidence showing test cases designed to verify code functionality align with coding methods and standards.
  + Examples for confirming error handling, memory management, and boundary condition testing.
  + Traceability matrix linking test cases to code modules and requirements.

---

### **4. Metrics Evidence**

* **Coding Standard Compliance Metrics:**
  + Percentage of code files/modules compliant with the coding standard.
  + Average number of violations per 1,000 lines of code.
  + Percentage of violations fixed over time (tracking continuous improvement).
* **Quality Metrics:**
  + Defect density metric—number of post-release defects per 1,000 lines of code.
  + Percentage of critical defects (severity level) directly attributed to non-compliance with coding standards.
* **Security Metrics:**
  + Number of security vulnerabilities detected by static analysis tools and verified by manual assessment.
  + Time taken to resolve critical vulnerabilities flagged by coding standards compliance tools.

---

### **5. Lessons Learned Evidence**

* Incorporate lessons learned or historical evidence showing how adherence to coding standards contributed to past project success.
* Examples include:
  + Postmortem reports detailing the critical role of coding standards in preventing major defects.
  + Documentation of issues or risks that arose due to non-compliance and how these were resolved using updated standards.

---

### **6. Software Assurance Evidence**

* **Independent Verification by the SA Team:**

  + Reports prepared by the software assurance team confirming:
    - The use of approved coding standards, methods, and criteria.
    - Validation of static analysis results to confirm rules are enforced.
    - Assurance that coding standards have been followed and risks were managed appropriately.
  + Independent audits of the development process for consistency with coding standards.
* **SA Risk Reports:**

  + Risk assessment reports outlining areas of non-compliance.
  + Recommendations provided by SA teams for improvement.

---

### **Summary of Good Objective Evidence**

| **Artifact** | **Purpose** |
| --- | --- |
| Coding Standards Document | Demonstrates the selection and definition of coding standards and methods. |
| Software Development Plan | Outlines the integration of coding standards within development processes. |
| Static Analysis Results | Verifies adherence to coding standards through automated tools. |
| Code Review Record | Documents manual inspections for coding compliance. |
| Deviation Logs | Tracks and justifies deviations from the standard. |
| Metrics Reports | Tracks progress, compliance trends, and violation resolutions. |
| Training Records | Confirms the project team’s understanding of coding standards. |
| SA Verification Report | Independent assurance and risk analysis for compliance and adherence. |

By collecting and maintaining this objective evidence, projects can ensure compliance with coding methods, standards, and criteria, demonstrating their commitment to quality, safety, and maintainability in their software systems.

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
