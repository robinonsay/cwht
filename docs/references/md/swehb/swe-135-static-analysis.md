# SWE-135 - Static Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695494. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis

SWE-135 - Static Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695494)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695494&showCommentArea=true&showComments=true#addcomment)

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

4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to, at a minimum, detect defects, software security, code coverage, and software complexity.

## 1.1 Notes

Although no maximum cyclomatic complexity score is required for non-safety-critical software, all software projects should regularly collect and maintain complexity metrics and use them to manage risk, either when high-complexity code must be modified, or proactively to improve the overall quality and maintenance of the code base. For safety-critical software, the analysis should take into account the requirements for cyclomatic complexity and code coverage as defined in 3.7.5 and 3.7.4 respectively.

* para 3.7.5 = [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)
* para 3.7.4 = [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)

## 1.2 History

Click here to view the history of this requirement: SWE-135 History

SWE-135 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.3.3 The project shall ensure that results from static analysis tool(s) are used in verifying and validating software code. |
| Difference between A and B | Removed requirement to validate the code. |
| B | 4.4.4 The project manager shall verify the software code by using the results from static analysis tool(s). |
| Difference between B and C | Removed the requirement to verify by changing "verify the software code by using the results from" to "use";   Added the requirement "to analyze the code during the development and testing phases to detect defects, software security, and coding errors." |
| C | 4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to detect defects, software security, and coding errors. |
| Difference between C and D | Requirement modified to analyze code coverage and software complexity along with the other items. |
| D | 4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to, at a minimum, detect defects, software security, code coverage, and software complexity. |

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

The static analysis requirement for NASA software projects increases the quality and safety of code developed for NASA Missions. Using static analysis helps to ensure that code meets the coding standards/criteria established by the project team ([SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards)) and common coding errors are eliminated before system integration and test ([SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)). Studies show that the cost of catching errors dramatically increases from one phase of development to the next by roughly a factor of 10 [136](#_tabs-<p></p>). Eliminating errors during implementation results in cost and time savings during integration and testing, which is a particularly important cost-saving factor for projects using high-fidelity testbeds.

### **Why This Requirement Is Important**

Static analysis tools are essential in NASA's software development processes because they provide an automated, consistent, and early means of identifying potential defects, security vulnerabilities, code coverage gaps, and problematic complexity. This requirement establishes a proactive approach to ensuring the robustness, reliability, and security of mission-critical software systems. Below is the rationale broken down by key factors.

---

### **1. Detecting Defects Early in Development**

* **Catch Issues Early:** Static analysis tools can identify defects at the source code level before the code is executed (i.e., during the development phase). This ensures that issues are caught early in the lifecycle, reducing the cost and burden of fixing defects discovered later in testing or deployment.
  + *Example Defects Detected:* Logic errors, uninitialized variables, off-by-one errors, data type mismatches, unchecked return values.
* **Cost of Early Defect Detection:** Studies show that the earlier a defect is found, the cheaper it is to fix. For instance:
  + Fixing a bug during design or coding costs significantly less than fixing it during testing or after deployment.
  + For NASA, where many software systems are mission-critical or safety-critical, early detection is not just a cost-saving measure but essential to risk mitigation.

---

### **2. Ensuring Software Security**

* **Prevent Vulnerabilities:** Static analysis tools identify coding patterns or practices that may lead to software vulnerabilities, ensuring compliance with secure coding standards (e.g., CERT C, CWE Top 25 vulnerabilities).
  + Commonly flagged issues include:
    - Buffer overflows.
    - Injection vulnerabilities.
    - Use of unsafe functions (e.g., `gets()` in C/C++).
    - Race conditions and data locks in multi-threaded environments.
* **Mitigate Security Risks:** NASA missions are increasingly exposed to cybersecurity threats due to reliance on networked systems and operational environments. Static analysis helps safeguard software against such threats, ensuring that:
  + Systems cannot be exploited maliciously.
  + Safety-critical operations cannot be interrupted.

---

### **3. Managing Software Complexity**

* **Avoid Unnecessary Complexity:** As software systems grow in size and modularity, they also risk becoming unnecessarily complex, creating challenges in comprehension, maintenance, and testing. Static analysis tools measure code complexity (e.g., cyclomatic complexity), which provides insights into areas of the software that may:
  + Be overly intricate, requiring simplification.
  + Increase the likelihood of defects or introduce unnecessary dependencies.
* **Facilitate Maintainability:** By keeping complexity in check, static analysis improves code readability, testability, and maintainability over the long lifecycle of NASA systems. This is essential for projects with frequent personnel transitions or extended periods of maintenance and upgrades.

---

### **4. Measuring Code Coverage**

* **Achieve Adequate Test Coverage:** Static analysis tools can measure coverage, ensuring that all critical paths in the codebase are tested appropriately.
  + Code coverage analysis ensures that:
    - The test suite exercises all branches of conditional logic.
    - Dead code is identified and removed.
    - No critical functionality remains untested.
* **Enhancing Mission Reliability:** For NASA software systems operating in critical environments (e.g., flight control, life support, and deep-space communication systems), comprehensive test coverage directly ties to mission safety and success.

---

### **5. Reducing Human Error**

* **Augment Manual Reviews:** While manual code reviews (peer reviews, inspections) are effective, they are limited in scalability. Static analysis tools provide automated checks that reduce the likelihood of overlooked issues due to human error or fatigue.
  + Automated analysis works across the entire codebase, performing checks consistently for all modules, regardless of size or complexity.
  + Complement manual efforts: Tools provide repeatable, objective outputs that can reinforce or guide manual code inspections.
* **Addressing the Scale of Modern Development:** As modern systems become larger and more modular, static analysis becomes critical to ensuring consistency, making it ideal for projects with distributed development teams.

---

### **6. Ensuring Standards Compliance**

* **Coding Standard Enforcement:** Static analysis tools ensure that developers consistently follow the project’s coding standards, which leads to readable, maintainable, and reliable code.
  + This is especially important for projects using tailored or NASA-specific standards (e.g., MISRA-C for safety-critical software).
  + Automatic identification of violations reduces the overhead of manual enforcement of coding practices.

---

### **7. Supporting the Verification Process**

* **Traceability in Compliance:** Static analysis tools generate detailed reports on compliance with specific project requirements, coding standards, and safety/security goals. These reports serve as objective evidence during key reviews (e.g., Preliminary Design Review [PDR], Critical Design Review [CDR]).
* **Confidence in Deliverables:** By using static analysis throughout development, the project team ensures progressively higher quality and confidence in the software as it moves through each stage of the lifecycle.

---

### **8. Mitigating Risks in NASA’s Unique Context**

NASA’s software systems are unique in their complexity, scale, and criticality:

* **Safety-Critical Systems:** An undetected defect in NASA systems can threaten astronaut safety, spacecraft integrity, or mission success.
* **Long Lifecycle Maintenance:** Software systems supporting space missions often stretch over decades, requiring solutions that prioritize maintainability and robustness.
* **Environmental Challenges:** Space systems operate in unique, harsh environments where redundant safety measures are needed to mitigate risks.

Proactively identifying and addressing issues with static analysis is a key risk mitigation strategy, offering a systematic safeguard for the challenges unique to NASA engineering efforts.

---

### **9. Improving Team Development Practices**

* **Feedback Loops for Developers:** Static analysis tools provide direct feedback to developers during coding, catching issues in real-time or as part of Continuous Integration (CI) pipelines.
  + This iterative feedback helps developers learn from their mistakes, improving their coding practices over time.
* **Building a Culture of Quality:** Regularly using static analysis ensures that quality becomes embedded into team workflows, fostering accountability and collaboration across the team.

---

### **Practical Example of Benefits in NASA Missions**

#### **Mars Pathfinder Example:**

During the Mars Pathfinder project, coding standards and practices played a critical role. However, late-stage tests revealed a priority inversion defect—a concurrency issue that could have been detected earlier with modern static analysis tools. Incorporating static analysis at appropriate stages would have reduced the risk of this occurring.

Had advanced static analysis tools been available:

* Thread-related issues would have been flagged earlier (e.g., race conditions, priority inversions).
* Code complexity contributing to the issue may have been measured and flagged for refactoring.

---

### **Conclusion**

Using static analysis tools during development and testing phases aligns with NASA’s priorities for quality, safety, and mission assurance. These tools enable:

1. Early detection of defects, reducing the overall cost of fixes.
2. Identification of security vulnerabilities, protecting mission-critical systems.
3. Management of software complexity to ensure maintainability over extended mission lifespans.
4. Comprehensive coverage checks to support robust verification and validation efforts.
5. Enforcement of coding standards for consistency and reliability.

The proactive use of static analysis tools ensures that NASA projects maintain the highest levels of reliability and security while staying aligned with mission goals and industry standards. These tools are a cornerstone to building safer, more efficient, and more maintainable software systems.

# 3. Guidance

## 3.1 Modern Static Analysis Tools

#### **Definition**

Static analysis tools analyze code without executing it, enabling the identification of issues early in the software development lifecycle. These tools are critical for verifying adherence to coding standards, detecting vulnerabilities, managing software complexity, and ensuring overall code quality.

#### **Common Issues Detected by Modern Tools**

Modern static analysis tools can identify a variety of software issues, including but not limited to:

* **Reliability Concerns:** Dead code, redundant code, and unused variables.
* **Non-Compliance with Standards:** Violations of industry or project-specific coding standards (e.g., MISRA-C, CERT C, NASA standards).
* **Security Vulnerabilities:** Buffer overflows, injection vulnerabilities, race conditions, and other security gaps.
* **Safety-Critical Issues:** Memory leaks, invalid pointer usage, potential division by zero, or concurrency errors.
* **Maintainability and Complexity:** Excessively long methods, deeply nested loops, or unnecessarily complicated code constructs.

#### **Use in Verifying Project Adherence**

Static analysis tools ensure compliance with defined coding methods, standards, and criteria. They complement manual processes such as peer reviews by automating large-scale and repetitive checks.

#### **False Positives and Tool Configuration**

A common shortcoming of static analysis tools is generating false positives (flagging issues that are not actual defects). This can be mitigated through:

* Careful configuration of tools for the project's needs to filter unnecessary noise.
* Regular review of flagged issues to assess their validity.
* Utilizing tools or settings that rank or categorize issues by severity.

#### **Integration with Peer Reviews**

Static analysis results can be included as part of code inspections and reviews (see SWE-087). This ensures issues flagged by tools are reviewed collaboratively, adding a human layer of validation to the automated results.

#### **Challenges with Tool Availability for Specific Platforms**

In some niche languages or platforms, static analysis tools may not exist or may be inadequate. For such cases:

* **Alternate Methods:** Document manual review and evaluation procedures. These alternate approaches must be included in the compliance matrix for the requirement.
* **Plan Integration:** Address this in the project plan and ensure manual processes supplement the absence of automated analyses.

#### **Critical Code Requirements**

For safety-critical or mission-critical systems, it is *essential* to use "sound and complete" static analyzers. These tools ensure:

* **Soundness:** All potential issues are flagged (no false negatives).
* **Completeness:** Covers all code paths and constructs.
  + While commercial tools can be costly, free tools that provide sound and complete analyses for C and C++ may be used (see NASA Resources Tools Table).

---

## 3.2 Cost of Tools

#### **High Cost of Commercial Tools**

Some advanced static analysis tools, particularly those designed for safety-critical systems, come with significant cost. However, the benefit of identifying complex issues (e.g., concurrency defects, intricate security vulnerabilities) often outweighs the cost when dealing with high-risk, mission-critical software.

#### **Free or Open-Source Tools**

* Projects with budget constraints or less critical software can use free static analysis tools, which are capable of detecting many common issues.
  + Examples:
    - **C/C++:** Clang-Tidy, Cppcheck.
    - **Python:** Pylint, Bandit.
    - **Java:** SpotBugs, Checkstyle.
* Even though free tools may lack robust support or extensive rule sets, their use should be considered a best practice for all software development efforts.

---

## 3.3 Characteristics of Modern Tools

Integrating static analysis tools effectively into a development process requires careful planning. Below are challenges, recommendations, and solutions.

---

#### **3.3.1 The Static Analyzer May Fail to Process Code**

**Challenge:**  
Some static analysis tools may encounter difficulties processing code due to:

* Complex or unusual code constructs.
* Compatibility issues with certain compilers, libraries, or language extensions.

**Guidance:**

1. **Evaluate the Tool on Real Code:**
   * Use a trial period to test the analyzer with your most complex or "tricky" code.
   * Avoid relying on vendor demonstrations—test the tool in your environment to uncover potential limitations.
2. **Technical Support:**
   * Choose a tool with robust technical support, especially for mission-critical projects.
3. **Match Compilers:**
   * Utilize analyzers compatible with the team's compiler (e.g., GCC-based tools for C/C++) to reduce parser mismatches.
4. **Provide Complete Library Access:**
   * Provide the tool access to the same libraries used during compilation.

---

#### **3.3.2 The Static Analyzer May Have Long Run Times**

**Challenge:**  
In-depth static analysis for large codebases may take excessive amounts of time, potentially interrupting the workflow.

**Guidance:**

1. **Configuration for Efficiency:**
   * Adjust precision levels as needed. Run faster, less precise scans daily and more thorough scans before major milestones.
2. **Integrate Incrementally:**
   * Use the tool to analyze smaller components initially and gradually expand to the full codebase.
3. **Schedule Overnight Runs:**
   * For larger scans, configure the tool to run during off-hours (e.g., overnight) to minimize disruption.

---

#### **3.3.3 Too Many Warnings**

**Challenge:**  
Excessive flagged issues can overwhelm the team, making it difficult to distinguish between meaningful issues and noise.

**Guidance:**

1. **Filter Results:**
   * Use filtering capabilities in the tool to prioritize critical issues (e.g., memory safety concerns, race conditions).
   * Rank warnings by severity; focus on high-priority flags first.
2. **Iterative Analysis:**
   * Address earlier warnings first; reanalyze after fixes to eliminate cascading issues.
3. **Use Custom Scripts:**
   * Implement scripts to automate filtering and categorizing results if built-in functionalities are insufficient.

---

## 3.4 Static Analysis and Manual Code Reviews

Static analysis complements manual code reviews by:

* Automating repetitive and large-scale checks (coding standards, best practices).
* Freeing reviewers to focus on higher-level design and architectural concerns.
* Providing consistent verification across large codebases.

**Integration Best Practices:**

1. Include static analysis results in peer review packages.
2. Compare flagged issues with manual review outcomes to assess coverage and identify false positives.
3. Use both approaches iteratively to ensure robust code verification.

See SWE-087 for further details on peer reviews.

---

## 3.5 Availability of Tools

**Static Analysis Tool Availability:**

* Tools exist for widely used programming languages such as C, C++, Ada, Java, and Python.
* NASA's IV&V Program maintains access to an extensive library of static analysis tools and provides fee-for-service support for projects without direct IV&V involvement.

**Resources:**

* Reference the NASA IV&V Program for additional tool recommendations, custom analysis setups, or tool access issues.
* The Tools Table under the Resources tab details available tools per language and use case.

---

### **Conclusion**

Static analysis tools are a cornerstone for ensuring software quality, reliability, and security in NASA systems. By using modern tools effectively and overcoming potential challenges (e.g., false positives, time constraints, compatibility issues), project teams can deliver safer, more maintainable, and compliant software. When integrated with manual reviews and project workflows, static analysis ensures confidence in mission-critical software.

Matching a static analyzer with the development team’s compiler will eliminate many challenges. Even if the tool has a good parser, make sure to give the tool access to the right libraries. Remember that a static analyzer is essentially a fancy compiler that does not produce executable code. Getting the compiling and linking environment right can be challenging if the chosen tool does not use the same parser as the team’s compiler.

With static analysis, there is often a trade between precision and scalability. You can expect to spend time upfront configuring the static analyzer to the particular needs of the project. For example, a quick, but crude, the static analyzer will produce quick feedback within a normal work cycle, and, a slow, but precise, analyzer can be run before a major release. Note that some precise commercial tools are customizable for rapid analysis.

When triaging warnings or errors, it is recommended to first process errors that appear early in the execution and re-run the static analyzer to avoid a lot of unnecessary work. As with compiler errors, fixing an early error might lead to the elimination of many later errors/warnings. This dependency between warnings is why it is recommended to run analysis during the development process; the results are addressed and cascading side effects are less likely to accumulate.

See also Topic [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software)

See also [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) for details on getting access to code for conducting an analysis.

See also [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage),

For Class A software take care to analyze all software affecting safety-critical software  and hazardous functionality including: [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)

[SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures))

see also [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards),

See also Topic [8.26 - Static Analysis](/spaces/SWEHBVD/pages/187203859/8.26+-+Static+Analysis).

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [8.26 - Static Analysis](/spaces/SWEHBVD/pages/187203859/8.26+-+Static+Analysis) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

Small projects often operate under constraints such as limited budgets, resources, and shorter schedules. However, the use of static analysis tools remains a critical best practice, even in smaller-scale efforts, to ensure high-quality, reliable, and maintainable software. The following guidance tailors approaches for the practical use of static analysis tools in small projects.

---

### **1. Prioritize Simplicity and Focus**

#### **Streamline Static Analysis Scope**

* **Start with Essential Checks:** For small projects where time and resources are limited, focus on detecting critical issues:
  + Security concerns (e.g., buffer overflows, race conditions).
  + Significant coding standard violations.
  + High-complexity or unmaintainable code.
* **Limit Overhead:** Avoid using overly comprehensive scans if not strictly necessary; focus on high-impact checks.

#### **Focus on Critical Areas of the Codebase**

* For small codebases, performing analysis on the entire codebase is feasible. However, if prioritization is needed:
  + Focus on **safety-critical modules** (e.g., logic controlling hazardous operations) or **mission-critical components** first.
  + Review high-risk or high-complexity areas identified during development.

#### **Collaboratively Define Priorities**

* Engage the team to agree on the most relevant static analyses, drawing from project-specific risks (e.g., security for networked software).

---

### **2. Utilize Cost-Effective Tools**

#### **Free and Open-Source Tools**

Small projects can leverage free or open-source static analysis tools that provide robust functionality without the high costs of commercial solutions. Examples include:

* **C/C++:** Clang-Tidy, Cppcheck, GCC’s built-in static analysis.
* **Python:** Pylint, Bandit.
* **Java:** SpotBugs, PMD, Checkstyle.
* **Multi-Language Tools:** SonarQube Community Edition, ESLint (for web or JavaScript projects).

#### **Trial Periods for Commercial Tools**

* Evaluate commercial tools that offer free trial periods. Test them on critical parts of the codebase to assess their benefits before committing to purchase.

#### **NASA Resources**

* Check with NASA’s IV&V Program for access to specialized tools at no additional cost. The IV&V Program supports static analysis for mission-critical projects across a wide variety of languages.

---

### **3. Minimize Overhead with Automation**

#### **Integrate Static Analysis into CI/CD Pipelines**

* Deploy lightweight static analysis scans as part of Continuous Integration (CI) tools (e.g., Jenkins, GitHub Actions, GitLab).
* Automate checks to run during nightly builds or with each commit to catch issues early without adding significant manual effort.

#### **Leverage Defaults to Start**

* Configure the static analysis tool to use its default rule sets, which often cover common coding issues and security vulnerabilities.
  + Fine-tune the configuration later to reduce false positives and tailor rules to the project’s unique requirements.

#### **Batch Analysis for Small Teams**

* For very small teams that cannot afford continuous scans, schedule static code analysis at critical project milestones, such as:
  + Feature-complete milestones.
  + Before integration testing.
  + Before final delivery.

---

### **4. Manage Findings Efficiently**

#### **Triage and Categorize Results**

* Expect some false positives, even from the most well-configured tools. Prioritize findings for review in the following order:
  1. Critical security vulnerabilities.
  2. Safety-related issues.
  3. Violations impacting maintainability and readability.
  4. Non-critical or cosmetic warnings.
* Assign findings to responsible team members for resolution, or document justifications for exceptions when fixes are not feasible.

#### **Limit Warnings to What Matters**

* Filter results based on severity, focusing on “High” or “Critical” findings.
* Suppress minor warnings to avoid overwhelming the team, but ensure that suppressions are documented to maintain traceability.

---

### **5. Keep Coding Standards Simple**

#### **Adopt a Practical Approach to Standards**

* Choose a small, essential subset of coding standards most relevant to the project. For example:
  + Enforce rules for **naming conventions**, **code formatting**, and **error handling**.
  + Adopt secure coding standards suitable for your language (e.g., CERT C for C/C++, PEP 8 for Python).
* Implement these standards into the static analysis tool configuration early so they are consistently enforced.

#### **Train the Team**

* Provide a brief overview or checklist of relevant coding standards to all developers.
  + Even short, informal sessions on coding best practices and common issues flagged by static analyzers can improve code quality significantly.
  + Consider sharing the tool’s “quick fixes” feature (for tools that automate corrections, such as fixing indentation or unused imports).

---

### **6. Align With Manual Processes**

#### **Combine Static Analysis With Peer Reviews**

* Static analysis results can complement code inspection or peer reviews (SWE-087). Share tool findings with reviewers to highlight areas needing further scrutiny.
  + Example: Use static analysis to identify high-complexity modules and prioritize manual review of those modules.

#### **Focus on Reusability and Maintainability**

* For small projects, code maintainability is particularly important due to limited resources:
  + Static analysis ensures code is consistently written, which minimizes confusion during later updates or reuse.
  + This reduces technical debt and facilitates easier handoffs.

---

### **7. Plan for Tool Limitations**

#### **Identify Risks When Tools Are Unavailable**

* If no suitable static analysis tool exists for your programming language or platform:
  + Document this in the project’s compliance matrix and provide an alternate plan (e.g., enhanced manual code reviews or tailored testing processes).
  + Use manual alternative checklists to verify critical aspects, such as adherence to coding standards and identification of potential vulnerabilities.

#### **Focus on Safety-Critical Aspects**

* If manual reviews are the alternate process, place extra emphasis on:
  + Functions affecting safety-critical systems.
  + Code interacting with hazardous functionality (see HR-33, Inadvertent Operator Action).

---

### **8. Small Project Example Use Case**

#### **Scenario**: Small Project for Ground-Based Data Processing Software

* **Codebase Size:** ~5,000 lines of Python code.
* **Team Size:** 3 developers.
* **Constraints:** Budget limitations, tight 6-month delivery schedule.

#### **Implementation Steps:**

1. **Select a Tool:**
   * Use free tools like Pylint and Bandit for Python.
2. **Run Simple, Automated Checks:**
   * Integrate static analysis runs into the team's GitHub Actions CI pipeline.
   * Static analysis checks run with every pull request, providing immediate feedback on coding standards and security vulnerabilities.
3. **Focused Training:**
   * Teach developers how to interpret common issues flagged by Pylint and address them.
   * Introduce the PEP 8 standard for Python as a team-wide coding practice.
4. **Milestone Checks:**
   * Conduct triaged reviews of static analysis results during key sprints (e.g., after major module completion).
5. **Document Code Quality:**
   * Use filtered tool reports as part of milestone documentation.
   * Track resolved issues versus remaining warnings to show progress.

---

### **9. Benefits of Tailored Static Analysis for Small Projects**

* **Improves Code Reliability:** Even lightweight tools reduce the risk of introducing defects.
* **Minimizes Rework Costs:** Early defect detection avoids costly repairs later in the process.
* **Encourages Consistency:** Enforces coding standards efficiently for small teams with limited manual review capacity.
* **Supports Compliance:** Provides low-resource methods to demonstrate compliance with NASA coding and assurance requirements.
* **Prepares for Growth:** Lays a solid foundation for scaling the codebase or integrating with larger systems.

---

This guidance ensures small projects achieve the benefits of static analysis within their constraints, improving software quality while maintaining practicality and cost-effectiveness. By strategically applying tools and focusing on critical areas, small teams can develop robust and maintainable systems without overburdening their limited resources.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-123)

  [Software Static Code Analysis Lessons Learned,](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.638.6456&rep=rep1&type=pdf "Click to open in new window")

  Andy German, Qinetiq Ltd. (2003). " CrossTalk Online.
* (SWEREF-136)

  [Software Engineering Economics,](https://www.amazon.com/Software-Engineering-Economics-Barry-Boehm/dp/0138221227 "Click to open in new window")

  Boehm, Barry. Englewood Cliffs, NJ:Prentice-Hall, 1981.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-241)

  [List of tools for static code analysis.](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis "Click to open in new window")

  Wikipedia, The Free Encyclopedia.
* (SWEREF-300)

  [Challenges in Deploying Static Analysis Tools,](https://pdfs.semanticscholar.org/4a55/9d70f538ffda5e581e8dd7a1783541d738f0.pdf "Click to open in new window")

  Piyush, J., Rao, DTV Ramakrishna, Balan, S. (May/June 2011), Crosstalk Online.  Retrieved February 29, 2012 from http://www.crosstalkonline.org/storage/issue-archives/2011/201107/201107-Jain.pdf.
* (SWEREF-428)

  ["Software Static Code Analysis Lessons Learned,"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.638.6456&rep=rep1&type=pdf "Click to open in new window")

  German, A. (November 2003). In CrossTalk The Journal of Defense Software Engineering, Archives. Lessons Learned Reference.
* (SWEREF-464)

  [NASA IV&V Program, Doing Business with IV&V,](http://www.nasa.gov/centers/ivv/business/index.html "Click to open in new window")

  NASA IV&V Program
* (SWEREF-518)

  [Independent Verification and Validation of Embedded Software](https://llis.nasa.gov/lesson/723 "Click to open in new window")

  Public Lessons Learned Entry: 723.
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

This section builds on documented lessons from the NASA Lessons Learned database while incorporating additional insights and best practices accumulated during the application of static analysis to software development projects. These lessons emphasize the effective use of static analysis tools and their integration into the broader software assurance and development lifecycle.

---

### **Key Lessons Learned**

#### **1. Importance of Parallel Coding Analysis**

**Related Lesson**: Independent Verification and Validation of Embedded Software (Lesson Number: 0723)

* **Summary of Lesson**: Parallel coding analysis is a best practice for maximizing the visibility of software development quality. During IV&V implementation phases, static analysis tools were used in conjunction with manual analysis techniques to identify defects earlier in the lifecycle. Incremental code deliveries were continuously monitored and analyzed for quality.
* **Actionable Recommendations**:
  + **Adopt Incremental Analysis:** Perform static analysis incrementally as code is developed, rather than waiting until milestones or major integration phases. This ensures that defects and coding violations are detected as early as possible.
  + **Automate Wherever Feasible:** Use static analysis tools to automate repetitive checks (e.g., syntax errors, rule violations) while reserving manual reviews for higher-order concerns such as architecture and logic validation.
  + **Integrate with Version Control Systems:** Tools should be configured to run as part of the version control system to identify issues introduced between different versions of code.

#### **2. Proper Integration of Static Analysis Tools with Coding Standards**

**Related Lesson**: Static Software Analysis of the NASA Autonomous Flight Termination Software (Lesson Number: 24503)

* **Summary of Lesson**: The success of static analysis as a verification tool depends on its alignment with pre-defined, rigorous coding standards. Moreover, how issues flagged by the tool are triaged, categorized, and resolved must be clearly defined.
* **Actionable Recommendations**:
  + **Harmonize Coding Standards and Tools Capabilities**: Ensure that the selected static analysis tool supports the coding standards specified for the project (e.g., MISRA-C for safety-critical systems, CERT C for secure coding). Adjust tool configurations and filters to focus on these rules.
  + **Establish Issue Management Policies**: Clearly define processes for:
    - Reviewing flagged issues and assessing their criticality.
    - Determining which issues require correction based on impact, risk, and priority.
    - Documenting and justifying any agreed-on exceptions.
  + **Define Reporting Expectations**: Require reports that categorize findings (e.g., severe, warning, informational) to prioritize developer attention to the most impactful issues.

#### **3. Benefits of Continuous Integration with Static Analysis**

**New Lesson Based on Industry Practices**:

* **Summary of Lesson**: Incorporating static analysis as part of the Continuous Integration (CI) pipeline significantly increases its effectiveness. This approach ensures that code is automatically analyzed at every commit or merge, preventing the accumulation of defects.
* **Actionable Recommendations**:
  + Configure static analysis tools to run automatically as part of the CI process (e.g., Jenkins, GitHub Actions, GitLab).
  + Treat failed static analysis checks as build failures and require resolution or justification before merging code into the main branch.
  + Generate detailed logs or reports after every CI-driven static analysis run to improve traceability and developer accountability.

---

### **Additional Lessons Incorporated from Other Projects**

#### **4. Tailored Use of Static Analysis for Risk-Driven Development**

**New Lesson**: Focus analysis efforts on high-risk code areas identified during risk assessment or system design.

* **Context for the Lesson**: Not all code carries equal importance in terms of risk. Safety-critical, mission-critical, or complex algorithmic components often have a higher likelihood of containing significant errors or defects.
* **Actionable Recommendations**:
  + Conduct a risk analysis early in the project to identify modules or functionalities that require heightened analysis (e.g., hazardous operations, communication protocols).
  + Assign heavier scrutiny during static analysis to safety-critical code. Use this knowledge to configure the analysis scope or rules to target these areas more granularly.

#### **5. Avoiding "Alert Fatigue" and Triaging Findings Effectively**

**Related to the Challenges of False Positives in Static Analysis**:

* **Summary of Lesson**: Static analysis tools can easily overwhelm developers with an excessive number of warnings or low-priority findings, leading to alert fatigue. This makes it difficult for teams to focus on addressing critical issues.
* **Actionable Recommendations**:
  + **Triaging Focus**: Classify flagged issues into categories: Critical (must-fix), Warning (fix after prioritization), and Informational (optional fixes or for awareness). Focus resources on resolving Critical issues promptly.
  + **Suppress False Positives**: During initial configuration, enable tool filters to suppress known false positives while documenting the rationale for suppressed categories of issues.
  + **Iterative Analysis**: Fix blocking or high-priority issues first and rerun the analysis to see which downstream issues have automatically resolved.

#### **6. Training and Familiarity with Static Analysis Tools**

**New Lesson**: Projects that neglected proper training for static analysis tools encountered delays and saw inconsistent adherence to tool findings.

* **Actionable Recommendations**:
  + Provide up-front training for developers, quality assurance personnel, and project managers on:
    - How to use the static analysis tool effectively.
    - How to interpret the results of the analysis and understand risk prioritization.
    - How to configure the tool to minimize extraneous warnings.
  + Share common examples of findings and their resolutions to align team expectations.

#### **7. Importance of Documenting Tool Configurations and Exceptions**

**New Lesson on Documentation Practices**:

* **Summary of Lesson**: Projects that failed to document tool configurations and exceptions struggled to maintain consistent analysis results and justify decisions during audits or reviews.
* **Actionable Recommendations**:
  + Clearly document:
    - Tool configurations, including rule sets, filters, and thresholds.
    - Any deviations from the coding standard and the rationale for such deviations.
    - Resolutions and justifications for flagged findings.
  + Share this documentation with IV&V teams to ensure transparency and alignment.

#### **8. Performing Baseline Analysis Early**

**New Industry-Informed Lesson**:

* **Summary of Lesson**: Performing an initial baseline static analysis of the entire codebase early in the project lays the foundation for monitoring changes effectively.
* **Actionable Recommendations**:
  + Run a complete, detailed static analysis as soon as development begins to establish a quality baseline.
  + Use subsequent analyses to focus on incremental code changes, allowing teams to detect regressions in quality over time.

#### **9. Leveraging Static Analysis for Continuous Improvement**

**New Lesson on Team Growth**:

* **Summary of Lesson**: Projects that viewed static analysis as a learning opportunity for the team noticed long-term improvement in software quality.
* **Actionable Recommendations**:
  + Use static analysis results to identify common coding mistakes and provide team feedback.
  + Incorporate insights into training sessions or development guidelines to address recurring patterns, such as poor memory management or insufficient input validation.

---

### **Summary of Lessons Learned**

| **Lesson** | **Key Takeaway** |
| --- | --- |
| Parallel coding analysis is critical | Incremental analysis ensures early detection and avoids the accumulation of defects. |
| Align tools with coding standards | Properly configured tools amplify the value of static analysis as a verification asset. |
| Automate in CI pipelines | Automatic scans catch issues early and prevent their proliferation during builds. |
| Risk-based prioritization of analysis | Focus on high-risk areas such as safety-critical components for deeper scrutiny. |
| Balance precision and alert fatigue | Triage findings to focus on critical issues while managing false positives effectively. |
| Train the team in tool usage | Adequate training fosters effective adoption and consistent analysis outcomes. |
| Document configurations and exceptions | Clearly record decisions on tool settings and issue resolutions for future audits and reviews. |
| Establish quality baselines | Early baseline runs provide a benchmark for identifying defects over time. |
| Promote continuous learning | Use static analysis insights to improve developer practices and prevent repetitive mistakes. |

By applying these lessons, small and large NASA projects can strengthen their static analysis processes, ensuring safer, more reliable, and maintainable code for mission-critical applications.

## 6.2 Other Lessons Learned

The Department of Defense publication *Crosstalk Magazine* contains the following lessons learned related to static analysis tools:

1. **Challenges in Deploying Static Analysis Tools.** [300](#_tabs-<p></p>) For higher quality software and competitive products, many projects are feverishly deploying static analysis tools. Unfortunately, it turns out that many of the deployments are failures. Some have discontinued static analysis tools altogether. Some continue to use them, but find that the results are not as effective as they hoped.   
   Many challenges are facing static analysis tool deployments. Although static analysis tools have some weaknesses, the main challenge stems from people. Whether the tool deployment succeeds or fails depends on the people behind it. What are the challenges facing static analysis tool deployments and how can those challenges be overcome? This paper tries to answer that question based on our deployment of the tools, consultancies with other organizations, and others' experiences.
2. **Software Static Code Analysis Lessons Learned.** [123](#_tabs-<p></p>) The United Kingdom Ministry of Defense has been at the forefront of the use of software static code analysis methodologies, including some of the tools and their application. This article ... discusses what is meant by static analysis, reviews some of the tools, and considers some of the lessons learned from the practical application of software static code analysis when used to evaluate military avionics software [428](#_tabs-<p></p>).
3. The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

   * [Run static analysis on code developed for unit test](https://software.gsfc.nasa.gov/lesson-details/217/). **Lesson Number 217**: The recommendation states: "Static analysis tools should be run not only on flight code (or production code in non-flight cases), but also on code developed for unit test. The issues identified for all code should be properly dispositioned and resolved."
   * [Consolidate tools and automate workflows where possible](https://software.gsfc.nasa.gov/lesson-details/333/). **Lesson Number 333**: The recommendation states: "Consolidate tools and automate workflows where possible."

# 7. Software Assurance

**SWE-135 - Static Analysis**

4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to, at a minimum, detect defects, software security, code coverage, and software complexity.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Analyze the engineering data or perform independent static code analysis to check for code detects defects, software quality objectives, code coverage objectives, software complexity values, and software security objectives.

2. Confirm the static analysis tool(s) are used with checkers to identify security and coding errors and defects.

3. Assess that the project addresses the results from the static analysis tools used by software assurance, software safety, engineering, or the project.

4. Confirm that the software code has been scanned for security defects and confirm the result.

5. Per SWE-219 for safety-critical software, verify code coverage and approved waivers.

6. Per SWE-220 for safety-critical software, verify cyclomatic complexity and approved waivers.

7. Confirm that Software Quality Objectives or software quality threshold levels are defined and set for static code analysis defects, checks, or software security objectives.

## 7.2 Software Assurance Products

### **Capturing and Managing Analysis Results**

#### **Static Code Analysis Results**

* **Corrective Actions Management**:
  + Ensure that all static analysis results are captured as tracked corrective actions within project management or defect-tracking systems (e.g., JIRA, Bugzilla).
  + Assign appropriate metadata to each corrective action, such as:
    - **Severity:** Categorize issues as critical, high, medium, or low.
    - **Category:** Classify issues as security vulnerabilities, coding standard violations, maintainability issues, performance bottlenecks, or dead code.
    - **Life Cycle Phase:** Identify the phase (e.g., development, testing, integration) in which the defect was identified.
    - **Status:** Track issue resolution (e.g., open, under review, closed).

#### **Integration of Results Across Project Phases**

* Review static analysis results provided from different sources, including:
  + Engineering analysis during development.
  + Software assurance independent static analysis.
  + IV&V (Independent Verification and Validation) findings, if applicable.
* Static analysis findings should:
  + Be synchronized among stakeholders and regularly updated for traceability.
  + Include both confirmed issues and documented rationale for false positives or waived items.

---

## 7.3 Metrics:

**Measuring and Monitoring Software Quality**

Effective metrics provide insights into software quality, security, and defect resolution trends. Metrics also guide decision-making and process improvements.

#### **General Metrics**

1. **Tool Usage and Coverage**:
   * Document all static code analysis tools used along with their scope (e.g., coding standards compliance, security checks).
   * Identify programming languages, platform(s), and software components covered in the analysis.
2. **Defect Analysis**:
   * Total number of errors and warnings identified by static analysis tools.
   * Total number of errors and warnings evaluated versus the total identified.
   * Breakdown of findings by type (critical, high, medium, low severity).

#### **Resolution Metrics**

1. **Defect Tracking**:
   * Number of open vs. closed issues over time, broken down by severity.
   * Ratio of identified issues resolved at each severity.
   * Ratio of static code analysis positives (e.g., defects flagged) confirmed as true issues or false positives.
2. **Trend Metrics**:
   * Track errors and warnings identified across project phases to monitor improvement over time.
   * Identify trends by software size (e.g., lines of code [SLOC]) and tool effectiveness.

#### **Cybersecurity-Specific Metrics**

1. **Vulnerability Tracking**:
   * Total number of cybersecurity vulnerabilities and weaknesses identified.
   * Number of cybersecurity vulnerabilities resolved versus remaining by severity.
   * Open versus closed cybersecurity issues tracked over time.
   * Categorization and prioritization of vulnerabilities by type (e.g., injection flaws, buffer overflows, race conditions).
2. **Coding Standard Compliance**:
   * Number of non-conformances related to cybersecurity-specific coding standards, broken down by status (open, closed) and severity.
   * Resolution percentage of cybersecurity-related findings during each phase of the lifecycle.

#### **Safety-Related Metrics**

1. **Critical Issues**:
   * Number of safety-related non-conformances identified and resolved, categorized by lifecycle phase.
   * Trends in resolution of safety-critical errors specific to hazardous operations or impacts on critical system functionality.

---

## 7.4 Guidance: Effective Use of Static Code Analysis Tools

#### **Objective of Software Assurance Analysis**

Analyze static analysis data or perform independent assessments to:

* Detect code defects, such as unused variables, logic errors, or null pointer usage.
* Verify software quality objectives for maintainability, modularity, testability, and fault tolerance.
* Validate software security objectives, including compliance with secure coding standards and identification of vulnerabilities.
* Assess code coverage to verify that all paths, branches, and conditions are tested (if applicable).
* Analyze software complexity (e.g., cyclomatic complexity, module dependencies) and confirm adherence to defined thresholds.

---

#### **Recommendations for Tool Use**

1. **Tool Setup and Configuration**:

   * Confirm that the static analysis tool(s) are configured to:
     + Detect security-related issues.
     + Enforce coding standards selected for the project.
     + Analyze safety-critical functionality for potential risks.
   * Ensure tools include specific checkers aligned with mission-critical software objectives.
2. **Tool Selection and Evaluation**:

   * Evaluate and select static analysis tools based on:
     + Language compatibility (e.g., C, C++, Java, Python).
     + Analysis capabilities (e.g., security-first, safety-critical certifiers, maintainability checkers).
     + Project needs (e.g., lightweight and fast tools for small projects, certifiers for safety-critical systems).
   * Use multiple tools where feasible to cross-check coverage and results.

#### **Handling Static Analysis Results**

1. **Evaluate and Prioritize Results**:
   * Review all flagged findings, confirm false positives, and prioritize real issues by severity level.
   * Critical security vulnerabilities and safety-related issues must be resolved before deployment.
   * Collaborate with the software engineering and development teams to resolve medium and low-level issues as time allows.
2. **Tracking and Visibility**:
   * Ensure identified issues are logged in a project tracking system for visibility and traceability.
   * Document resolution timelines, unaddressed issues, and associated risks or justifications.

---

#### **Specific Safety and Security Considerations**

1. **Safety-Critical Software**
   * For safety-critical software, confirm that all paths are analyzed, and ensure hazardous operations are verified as safe, unsafe, or "potentially unsafe" using safety-focused certifiers.
   * Document all waivers and deviations through formal approvals as per SWE-219 and SWE-220.
2. **Cybersecurity**
   * Confirm that static analysis tools adequately check for memory safety, race conditions, injection flaws, and other cybersecurity issues.
   * If a vulnerability is unresolved (e.g., due to mitigations at runtime), ensure risk justification is documented and approved.

---

#### **Alternate Verification Methods**

* If static analysis tools are unavailable (e.g., for niche languages), alternative verification methods include manual code reviews, peer inspections, and tailored testing processes. These must be clearly documented and approved in the project compliance matrix.

---

#### **Post-Analysis Review**

1. **Resolution Assessment**
   * Software assurance must assess whether the development team has adequately addressed tool-reported issues. Verify:
     + Security vulnerability resolutions are complete and effective.
     + Safety-critical defects are eliminated.
     + Other resolution actions are properly implemented.
2. **Risk Review**
   * Help the project team assess the risks of leaving unresolved issues, especially in time-constrained projects.
   * Recommend mitigation strategies for deferred defects.

---

### **Summary of Guidance**

Software assurance plays a critical role in ensuring the comprehensive and effective use of static analysis tools. By selecting appropriate tools, analyzing the results strategically, and guiding the project team in resolving critical issues, software assurance helps ensure software reliability, safety, and security. This guidance ensures compliance with NASA's software development standards while enabling continuous improvement and maintaining accountability throughout the project lifecycle.

See also [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access), [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification),

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [8.26 - Static Analysis](/spaces/SWEHBVD/pages/187203859/8.26+-+Static+Analysis) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is the documented proof that demonstrates compliance with the requirement. For Requirement 4.4.4, this evidence should confirm the proper use of static analysis tools and the resolution of issues identified through their use. The evidence should be traceable, complete, and sufficient to pass audits and reviews.

---

### **1. Documentation of Static Analysis Tools**

Evidence showing that appropriate static analysis tools were selected, configured, and used during the project:

* **Tool Selection and Configuration Records:**
  + Documentation of the selected static analysis tool(s), including:
    - Tool name and version.
    - Programming languages supported (e.g., C, C++, Python, Java).
    - Rationale for tool selection (e.g., alignment with coding standards, security requirements, or project needs).
    - Any licensing or procurement details.
  + Configuration files from the tool setup (e.g., XML, JSON, or GUI screenshots of the tool’s settings, including checkers and filters enabled).
* **Compatibility Assessment:**
  + Evidence that static analysis tools are compatible with the codebase and align with project needs, including a comparison between project coding standards and tool capabilities.

---

### **2. Static Analysis Results**

Comprehensive records of static analysis results throughout the software development lifecycle:

* **Analysis Logs and Reports:**
  + Raw outputs from static analysis tools (e.g., log files, XML/JSON reports, or dashboards).
  + Summary reports detailing:
    - Total errors, warnings, and information messages detected.
    - Categorization of issues (e.g., security vulnerabilities, maintainability concerns, compliance violations).
    - Breakdown of findings by severity (e.g., critical, high, moderate, low).
  + Screenshots or generated dashboards highlighting major findings over time.
* **Incremental Analysis Results:**
  + Reports from periodic (e.g., weekly or milestone-based) analysis runs, showing trends in findings (e.g., reduction of errors, new warnings introduced).

---

### **3. Corrective Action Records**

Evidence demonstrating that static analysis findings were appropriately addressed:

* **Issue Tracking Records:**
  + A list of all identified static analysis issues, categorized by:
    - Severity (critical, high, moderate, low).
    - Issue type (e.g., memory errors, security concerns, coding standard violations).
    - Resolution status (e.g., addressed, deferred, false positive, under review).
  + Traceability of each issue to its resolution or documented justification for deferral.
* **Defect Resolution Logs:**
  + Step-by-step documentation of the resolution process for critical and high-severity issues.
  + Evidence of collaboration between software assurance, engineering, and IV&V teams on issue prioritization and resolution.
* **Risk Mitigation Justifications:**
  + Documented rationale for deferred issues or waivers, particularly for lower-severity findings or findings with acceptable mitigations. For example:
    - A security vulnerability mitigated through runtime protections.
    - A low-priority defect determined to be unlikely to impact functionality.

---

### **4. Verification of Coding Standards and Security Compliance**

Evidence that the software complies with coding standards and secure coding practices:

* **Coding Standards Verification:**
  + Records confirming static analysis was configured to enforce compliance with coding standards (e.g., MISRA-C, CERT C, PEP 8).
  + Reports detailing coding standard violations and their resolution.
  + Any waivers or exceptions to the coding standard, along with approval documentation.
* **Security Analysis Reports:**
  + Evidence that static analysis tools were configured to flag security vulnerabilities (e.g., buffer overflows, injection flaws, race conditions).
  + Listings of security-related findings and actions taken to address them.
  + Cybersecurity risk assessment documentation based on static analysis results.

---

### **5. Metrics and Trends**

Quantifiable indicators demonstrating compliance and effectiveness of static analysis:

* **Static Code Analysis Metrics:**
  + Total errors, warnings, and informational messages reported by the tool.
  + Number of errors/warnings evaluated versus total reported.
  + Ratio of resolved versus unresolved findings by severity (e.g., “90% closure rate for critical issues”).
  + Weekly or milestone-based trends of identified versus resolved issues.
* **Security-Specific Metrics:**
  + Number of vulnerabilities detected, categorized, and resolved.
  + Open versus closed cybersecurity vulnerabilities over time.
  + The percentage of compliance with relevant secure coding standards.
* **Code Complexity and Maintainability Metrics:**
  + Cyclomatic complexity analysis reports (as per SWE-220).
  + Module dependency analysis or graphs showing modularity and maintainability levels.
* **Code Coverage Metrics:**
  + Reports demonstrating code coverage objectives for static analysis were met, as per SWE-219.

---

### **6. Audit Reports and Compliance Checklists**

Records demonstrating that static analysis is integrated into the software assurance workflow and its results are audited:

* **Project Audit Reports:**
  + Results of internal or external audits verifying compliance with Requirement 4.4.4.
  + Findings from software assurance reviews evaluating static analysis tool usage and effectiveness.
* **Compliance Checklists:**
  + Completed checklists showing adherence to SWE-219 (Code Coverage) and SWE-220 (Cyclomatic Complexity).
  + Evidence that software assurance verified static analysis actions were appropriate and effective.

---

### **7. Peer Review and Independent Assessments**

Records of reviews that include static analysis findings:

* **Code Peer Review Logs:**
  + Documentation that static analysis findings were included in code peer review packages (SWE-087).
  + Peer review feedback on findings and their resolution.
* **Independent Verification and Validation (IV&V) Reports:**
  + Results of IV&V team assessments of static analysis implementation, where applicable.

---

### **8. Tool Evaluation and Training Records**

Evidence that the team selected appropriate tools and was trained to use them effectively:

* **Tool Evaluation Documents:**
  + Records evaluating multiple static analysis tools for compatibility, effectiveness, and cost before final selection.
* **Training Documentation:**
  + Records of training sessions provided to developers and software assurance teams on the use of static analysis tools, interpreting findings, and resolving issues.

---

### **9. Waivers and Exceptions**

Documentation of approved deviations from static analysis or compliance standards:

* **Waivers and Exception Records:**
  + Requests for waivers or exceptions to the use of certain checkers or tools, with the rationale and approval signatures.
  + Waivers for unresolved issues, with documented risk assessments and justification for impact on the project.

---

### **10. Final Certification**

Evidence demonstrating that all required static analysis objectives were met before delivery:

* **Final Analysis Certification Report:**
  + A summary document signed by software assurance, IV&V, and/or the project team certifying:
    - Static analysis coverage of the full codebase.
    - Resolution of all critical and high-severity issues, along with actionable plans for remaining items.
    - Compliance with security and safety standards.

---

### **Examples of Objective Evidence Artifacts**

| **Artifact Type** | **Description** |
| --- | --- |
| Tool Selection Report | Detailed rationale and evaluation showing how the chosen tool aligns with requirements. |
| Static Analysis Raw Reports | Unfiltered logs or output files from tools. |
| Static Analysis Summary Reports | Consolidated summary of findings, categorized by severity and type. |
| Defect Tracking Data | Tool-based tracking of static analysis issues through resolution or deferral. |
| Coding Standards Waivers | Signed waivers explaining deviations from coding standards. |
| Security Assessment Report | Summary of security vulnerabilities identified and actions taken. |
| Metrics Trend Report | Graphs and trends showing defect closure rate, resolution over time, etc. |
| Cyclomatic Complexity Reports | Analysis results showing adherence to complexity thresholds. |
| Peer Review Feedback Forms | Comments and actions from code peer reviews. |
| Audit Review Report | Findings from software assurance audits, verifying proper tool usage and results. |
| Final Verification Checklist | Checklists documenting compliance with SWE-219, SWE-220, and software assurance goals. |

---

### **Conclusion**

Objective evidence ensures that static analysis tools are being used effectively, deficiencies are systematically addressed, and the software meets quality, security, and compliance requirements. By collecting detailed and well-organized evidence, teams can demonstrate compliance with Requirement 4.4.4 and support NASA’s mission-critical standards for software development.

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
