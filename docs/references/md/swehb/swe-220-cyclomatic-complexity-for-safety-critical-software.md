# SWE-220 - Cyclomatic Complexity for Safety-Critical Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 105709643. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software

SWE-220 - Cyclomatic Complexity for Safety-Critical Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=105709643)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=105709643&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

3.7.5 If a project has safety-critical software, the project manager shall ensure all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. Any exceedance shall be reviewed and waived with rationale by the project manager or technical approval authority.

## 1.1 Notes

Cyclomatic complexity is a metric used to measure the complexity of a software program. This metric measures independent paths through the source code. The point of the requirement is to minimize risk, minimize testing, and increase reliability associated with safety-critical software code components, thus reducing the chance of software failure during a hazardous event. The software developer should assess all software safety-critical components with a cyclomatic complexity score over 15 for testability, maintainability, and code quality. For more guidance on this requirement, see NASA-HDBK-2203.

## 1.2 History

Click here to view the history of this requirement: SWE-220 History

SWE-220 - Used first in NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | First use of this SWE |
| D | 3.7.5 If a project has safety-critical software, the project manager shall ensure all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. Any exceedance shall be reviewed and waived with rationale by the project manager or technical approval authority. |

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
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |

# 2. Rationale

**To minimize risk, ensure complete software testing, and increase reliability associated with safety-critical software code components,** maintaining a cyclomatic complexity value of 15 or lower for safety-critical software components is critical. Cyclomatic complexity measures the structural intricacy of code by evaluating the number of independent execution paths. Software with higher complexity values is inherently more challenging to understand, test, and maintain, which can jeopardize the reliability and safety of critical systems.

By enforcing a cap at 15, this requirement supports the following key objectives:

* **Improved Testability:**  
  Lower cyclomatic complexity directly enhances testability by simplifying the code structure. With fewer decision paths, it becomes easier to construct comprehensive test cases that cover all possible code execution paths. For safety-critical software, rigorous testing is non-negotiable, as undetected defects or overlooked scenarios could lead to catastrophic failures.
* **Reduced Risk of Failures:**  
  Complex code is inherently more prone to errors, making it difficult to debug, modify, or verify. This increases the chance of introducing new defects, particularly during development or maintenance phases. By limiting complexity, the likelihood of software-related failures is significantly diminished, ensuring a higher standard of safety and reliability.
* **Enhanced Maintainability and Modifiability:**  
  Code with lower complexity is easier to interpret, update, and verify. This is particularly critical in safety-critical systems, where software maintenance or upgrades must be performed efficiently and without introducing new risks. Simpler code fosters safer and quicker updates, especially during mission-critical situations.
* **Alignment with Industry and NASA Standards:**  
  Setting a complexity threshold of 15 aligns with established best practices in software engineering and with safety-critical standards that emphasize simplicity, testability, and maintainability. This requirement reflects NASA's commitment to upholding rigorous quality standards and ensuring reliable performance.

For instances when components exceed the cyclomatic complexity threshold of 15, a structured **review and approval process** ensures that these exceptions are justified and that associated risks are effectively managed. The project manager or a technical approval authority must conduct a thorough review, providing documented rationale for the exceedance. This process ensures transparency and accountability while leveraging appropriate mitigation strategies to reduce risk.

# 3. Guidance

### **3.1 Purpose and Rationale:**

Limiting cyclomatic complexity in safety-critical software components is crucial for reducing risk, improving reliability, and ensuring thorough testing of the software. Cyclomatic complexity measures the number of independent paths in a program's code (where "independent" means having at least one edge unique to that path). Complex code tends to introduce defects, is harder to maintain, and requires more effort to test thoroughly—all of which can compromise the safety and reliability of critical systems during hazardous events.

### **Key Benefits:**

1. **Improved Testability:**

   * Cyclomatic complexity directly correlates with the number of unique test cases needed to achieve full code coverage. Code with lower complexity requires fewer test cases, ensuring higher efficiency and confidence during testing.
   * Complexity values exceeding 15 make it challenging to validate all critical execution paths, increasing the likelihood of undetected defects.
2. **Higher Reliability:**

   * Studies have shown a positive correlation between cyclomatic complexity and the occurrence of software defects. By limiting complexity, the software is less error-prone and more predictable, reducing risks associated with hazardous events.
3. **Enhanced Maintainability:**

   * Code modules with lower complexity are easier to understand, update, and debug. High complexity introduces coupling, making modifications more error-prone and impacting overall code quality. Using modular code design ensures maintainability in safety-critical systems.
4. **Alignment with Standards and Best Practices:**

   * NASA’s requirement aligns with internationally recognized safety standards, such as ISO 26262 and IEC 62304, which mandate low code complexity for secure and reliable systems.

---

### **3.2 What is Cyclomatic Complexity?**

Cyclomatic complexity, introduced by Thomas J. McCabe in 1976, is a software metric that measures the structural complexity of a program. It quantifies the number of independent paths through the program’s control flow graph, calculated as follows:

**Cyclomatic Complexity = E - N + 2**  
Where:

* **E** = number of edges (transitions in the control flow)
* **N** = number of nodes (decision points or processes in the code)

For example:

* Code with no control flow (no conditionals or loops) has a cyclomatic complexity of 1, as there’s only one path.
* A single `IF` statement has two paths (TRUE and FALSE), giving a complexity of 2.
* Nested `IF` statements will increase complexity by adding paths.

**Implications of Cyclomatic Complexity:**

1. **Testing:**  
   Cyclomatic complexity determines the minimum number of test cases needed for adequate coverage. For instance, a function with complexity 15 requires at least 15 test cases to fully test its independent paths.
2. **Defect Correlation:**  
   High complexity correlates with more defects, particularly when program size is controlled. While studies show some variability, functions with higher complexity often have more defects.
3. **Maintainability:**  
   Lower complexity reduces coupling, improves code clarity, and simplifies modifications, all of which are critical for safety-critical software.

### **Recommended Practices:**

1. **During Development:**

   * Developers should monitor cyclomatic complexity and strive to keep it at or below **15** for all safety-critical modules.
   * Overly complex modules should be refactored into smaller, more manageable modules with lower complexity.
2. **Static Analysis Tools:**  
   Utilize modern **static analysis tools** to measure cyclomatic complexity automatically during development and testing. These tools provide valuable insights into code structure and potential improvement areas.
3. **Review and Justification:**  
   If a module exceeds the complexity threshold (16 or higher), the project manager must collaborate with software assurance to perform a **risk assessment**. This review assesses testability, maintainability, and quality implications, and documents rationale for exceeding the limit.

### **Cyclomatic Complexity Levels and Implications:**

| **Complexity Range** | **Meaning** | **Testability** | **Effort & Cost** |
| --- | --- | --- | --- |
| 1-10 | Well-structured code; highly testable | High | Low |
| 10-15 | Manageable complexity for safety-critical systems | Medium to High | Moderate |
| 15-20 | Complex code; requires thorough review | Lower | Higher |
| 20-40 | Very complex; difficult to validate and maintain | Poor | Very High |
| >40 | Excessive complexity; not suitable for safety-critical systems | Very Poor | Extreme |

For safety-critical software, any complexity exceeding **15** should trigger a review process and justification for its necessity.

---

### **Design and Tools Recommendations:**

1. **Modular Design:**  
   Split complex functions into smaller, independent modules with clear and specific responsibilities.
2. **Use Static Analysis Tools:**  
   Static analysis tools can provide cyclomatic complexity values for functions, modules, or classes, offering actionable metrics to maintain code quality and reduce risks.
3. **Adopt Best Practices:**

   * During development, limit cyclomatic complexity to **15** to ensure structuredness, ease of testing, and maintainability.
   * Follow established coding standards and guidelines, such as **NASA’s SWE-023, SWE-134, SWE-135**, and **NIST Structured Testing Methodology**.
4. **Handle Complexity Exceptions:**  
   Justify modules with complexity values exceeding **15** (e.g., through multi-condition logic or state machines) by documenting rationale and performing rigorous risk assessments.

### **References:**

* NASA/TM−20205011566: Cyclomatic Complexity and Basis Path Testing Study
* NESC-RP-20-01515: Guidance for Safety-Critical Software Development
* SWE-023: Software Safety-Critical Requirements
* SWE-134: Safety-Critical Software Design Requirements
* SWE-135: Static Analysis Requirements
* ISO 26262 and IEC 62304: International Standards on Software for Safety-Critical Systems

This revised guidance consolidates the original content into a clearer structure, emphasizing actionable advice, technical relevance, and alignment with NASA’s safety-critical development practices. It balances technical depth with ease of use for developers and engineers.

For Class A software take care to analyze all software affecting safety-critical software  and hazardous functionality including: [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)

See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) and [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements). [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis),

### 3.2.1 Flow graph notation for a program:

Flow Graph notation for a program defines several nodes connected through the edges. Below are Flow diagrams for statements like if-else, While, until, and normal sequence of flow.

Cyclomatic complexity is a software metric used to measure the complexity of a program. These metrics measure independent paths through program source code. An independent path is defined as a path with at least one edge that has not been traversed before in any other path.  It quantitatively measures the number of linearly independent paths through a program's source code. The application of the requirement is to limit the complexity of routines during program development; programmers should count the complexity of the modules they are developing and split them into smaller modules whenever the cyclomatic complexity of the module exceeded 15. The NIST Structured Testing methodology adopted this practice. The figure of 10 had received substantial corroborating evidence.  There are occasional reasons for going beyond the agreed-upon limit. It phrased its recommendation as "For each module, either limit cyclomatic complexity to 15 or provide a written explanation of why the limit was exceeded. For example, if the source code contains no control flow statement, its cyclomatic complexity will be 1, and the source code contains a single path in it. Similarly, if the source code contains one if condition, then cyclomatic complexity is 2 because there will be two paths: true and the other for false.

Several studies have investigated the correlation between cyclomatic complexity numbers with the frequency of defects occurring in a function or method. Studies have found a positive correlation between cyclomatic complexity and defects: functions and methods with the highest complexity also tend to contain the most defects. However, international safety standards like **ISO 26262** [376](#_tabs-<p></p>)  and **IEC 62304** [375](#_tabs-<p></p>)  mandate coding guidelines that enforce low code complexity.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

# 4. Small Projects

Effective software engineering guidance for **small projects** should focus on scalability, simplicity, efficiency, and tailored application of key principles that still ensure quality, reliability, and compliance with organizational standards like NASA's. Small projects typically have fewer resources and shorter timelines, so the guidance should avoid unnecessary complexity while still enforcing critical practices. Below is practical, streamlined guidance for small software projects:

### **4.1 General Principles for Small Projects**

1. **Simplify Processes**: Prioritize lightweight versions of formal processes. Small projects should aim for efficiency in planning, tracking, and reviewing, while still meeting critical requirements.
2. **Focus on Risk Management**: Evaluate and address key risks early, particularly those tied to safety-critical requirements, testing, and software reliability.
3. **Prioritize Documentation**: Create concise and essential documents. Avoid excessive or overly detailed documentation that might overwhelm small teams or divert attention from implementation and testing.
4. **Automation and Repeatable Processes**: Use static analysis tools, automated testing frameworks, and configuration management systems to reduce manual effort.
5. **Rapid Iterations and Incremental Development**: Adopt iterative methods like Agile or similar lightweight processes to deliver functional software in short cycles, allowing for early user feedback.
6. **Scalable Assurance Practices**: Implement scaled-down versions of software assurance and safety practices that match project size and complexity while remaining compliant with required standards.

### **4.2 Small Project Software Engineering Practices**

### 4.2.1 Requirements Definition

* **Keep Requirements Simple and Prioritized**: Focus on essential functionality and safety-critical features. Avoid scope creep by clearly defining goals upfront and regularly reviewing requirements.
* **Safety-Critical Focus**: Identify all safety-critical functions early and ensure requirements explicitly address these, even for smaller systems.

### 4.2.2 Software Design

* **Modular Design**: Use simple, modular architecture to minimize the complexity of the software system. Modular code is easier to develop, test, and maintain.
* **Limit Cyclomatic Complexity**: Even for small projects, adhere to the cyclomatic complexity threshold (e.g., ≤15 for safety-critical software). Refactor complex code into smaller, testable units.
* **Reuse Approved Code**: Leverage reusable software components or libraries to save development time and ensure adherence to established quality standards.

### 4.2.3 Development Practices

* **Coding Standards**: Enforce consistent coding practices using lightweight coding standards (e.g., NASA's SWE-134 for safety-critical software requirements). Focus on readability, maintainability, and simplicity.
* **Static Analysis Tools**: Incorporate static analysis tools into the development process to identify defects early and ensure adherence to coding standards.
* **Version Control**: Use version control systems (e.g., Git) to track development progress, changes, and facilitate collaboration.

### 4.2.4 Testing and Validation

* **Automated Testing**: For small projects with limited testing resources, use automated testing tools to efficiently generate and execute unit tests, regression tests, and test coverage assessments.
* **Risk-Based Testing**: Prioritize testing on critical functionality (e.g., safety-critical components). Focus on areas that, if defective, could cause mission failure, equipment damage, or safety hazards.
* **Cyclomatic Complexity Coverage**: Ensure all independent code paths (determined by cyclomatic complexity) are validated through unit and system tests.

### 4.2.5 Software Assurance

* **Adapt Software Assurance Activities**: Scale software assurance plans proportional to the size and complexity of the project. For example:
  + Conduct lightweight peer code reviews for small teams instead of formal review boards.
  + Focus assurance resources primarily on critical functions and interfaces.
* **Independent Verification & Validation (IV&V)**: If required by project size or scope, ensure IV&V is aligned with project risks and critical areas (NASA-STD-8739.8 may not fully apply to small efforts, but critical components should still be verified).

### 4.2.6 Documentation

* **Concise Documentation**: Limit documentation to essential items, such as:
  + Requirements Traceability Matrix (RTM) for tracking compliance to requirements.
  + Lightweight safety-critical software test plans.
  + Finalized implementation guidelines and code quality reports.
* **Reusable Templates**: Use standardized and reusable templates tailored for small projects to reduce the burden of generating original documentation.

### 4.2.7 Risk Management

* **Identify Key Risks Early**: Even small projects should assess technical risks, schedule risks, and resource availability. Focus on mitigating risks tied to safety-critical functionality and reliability.
* **Failure Mode Analysis**: Conduct lightweight failure modes and effects analysis (FMEA) to ensure safety-critical components are proactively reviewed and mitigated for potential failures.

### 4.2.8 Project Management

* **Simplified Governance**: Scale project management tools and tracking techniques (e.g., use spreadsheets instead of enterprise-level tools). For small teams, simple tracking methods can be effective.
* **Cross-Functional Teams**: Use small, multi-skilled teams to streamline communication and reduce unnecessary hierarchies.
* **Time and Scope Management**: Clearly define and control project scope. Ensure teams deliver within deadlines by setting achievable milestones and avoiding scope increases.

### 4.2.9 Configuration Management

* **Lightweight CM Systems**: Small projects can benefit from simpler configuration management tools, such as Git repositories, for version tracking and change control.
* **Monitoring Key Artifacts**: Focus configuration control efforts on requirements documentation, source code, and test results for critical components.

### 4.2.10 Tools and Resources for Small Projects

* **Static Analysis Tools**: For cyclomatic complexity and defect identification (e.g., SonarQube, Coverity, or similar lightweight tools).
* **Project Management Tools**: Use simple tools like Trello, Asana, or spreadsheets to manage tasks and schedules effectively.
* **Automated Testing Frameworks**: Adopt tools like JUnit, PyTest, or other automated testing frameworks suited for the project language.
* **Version Control Systems**: Git and GitHub (or similar tools) are versatile and scalable for small projects.
* **Reusable NASA Standards**: Refer to streamlined versions of **NASA-STD-8739.8** and **NASA Software Engineering Handbook** for scalable practices.

### 4.2.12 Key Considerations for Small Projects

1. **Balance Simplicity and Quality**: Keep processes streamlined but ensure compliance with essential standards for reliability and safety.
2. **Focus on Risk Areas**: Prioritize safety-critical software functions and areas that could cause significant project impact.
3. **Make Everything Scalable**: Avoid heavyweight processes or tools that would overwhelm small teams. Lean tools and methodologies can achieve the same results with less overhead.

By tailoring software engineering practices to the size and scope of the project, small teams can maximize efficiency while still delivering high-quality, reliable, and safe software systems.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-375)

  [IEC 62304](https://en.m.wikipedia.org/wiki/IEC_62304# "Click to open in new window")

  IEC 62304:2006, Medical device software — Software life cycle processes A copy of this standard is available from https://www.iso.org/standard/38421.html
* (SWEREF-376)

  [ISO 26262](https://en.m.wikipedia.org/wiki/ISO_26262 "Click to open in new window")

  ISO 26262-1:2011, Road vehicles — Functional safety — Part 1: Vocabulary A copy of this standard is available from: https://www.iso.org/standard/43464.html
* (SWEREF-377)

  [Cyclomatic Complexity and Basis Path Testing Study](https://ntrs.nasa.gov/api/citations/20205011566/downloads/20205011566.pdf "Click to open in new window")

  NASA/TM?20205011566, NESC-RP-20-01515

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

NASA lessons learned associated with cyclomatic complexity and related software assurance practices for safety-critical software. Many of these lessons stem from failures or issues encountered in past projects, where high software complexity, inadequate testing, or lack of proper risk management contributed to mission risks or failures. Below are key examples of NASA lessons learned relevant to **Requirement 3.7.5** (Cyclomatic Complexity management in safety-critical software):

---

### **Relevant NASA Lessons Learned**

#### **1. Lesson ID: 0839 – Mars Polar Lander Loss**

**Summary:**  
The loss of the Mars Polar Lander in 1999 was partially attributed to software design and testing issues, specifically insufficient testing of software handling "edge cases." The system relied on a complex decision-making process in the software, which was not fully validated under real-world scenarios.

**Relevance to Cyclomatic Complexity Requirement:**

* Complex software decisions and branching logic (high cyclomatic complexity) increase the chance of untested paths leading to mission failure.
* This highlights the importance of ensuring testability through proper code structure and maintaining low cyclomatic complexity in safety-critical systems.

**Lesson Learned:**

* Avoid overly complex logic in safety-critical software where possible. Lower complexity improves test coverage and reliability. If complexity cannot be avoided, ensure exhaustive testing of all paths.

---

#### **2. Lesson ID: 1281 – OrbView-3 Satellite Power System Failure**

**Summary:**  
The OrbView-3 satellite suffered a mission failure due to inadequate testing of software interfaces in a safety-critical subsystem. The software complexity contributed to incomplete identification and validation of all critical failure modes during testing.

**Relevance to Cyclomatic Complexity Requirement:**

* High complexity in safety-critical software components creates challenges for identifying all failure modes, increasing the likelihood of defects and untested scenarios.

**Lesson Learned:**

* Controlling cyclomatic complexity ensures that comprehensive testing of all paths in safety-critical software is feasible within project constraints.

---

#### **3. Lesson ID: 2197 – Juno Spacecraft Software Challenges**

**Summary:**  
The Juno spacecraft encountered significant software-related challenges during its post-launch operations phase. Complex software logic contributed to difficulties in diagnosing and resolving anomalies in real time.

**Relevance to Cyclomatic Complexity Requirement:**

* Higher cyclomatic complexity reduces maintainability and makes real-time debugging and anomaly resolution more challenging, especially during mission-critical phases.

**Lesson Learned:**

* Reducing cyclomatic complexity improves software clarity, maintainability, and ease of debugging during critical operations.

---

#### **4. Lesson ID: 0379 – Mars Climate Orbiter Metric Conversion Failure**

**Summary:**  
The Mars Climate Orbiter was lost due to a simple software error involving unit mismatches (metric vs. imperial). The system's complexity, combined with inadequate validation processes, contributed to the failure.

**Relevance to Cyclomatic Complexity Requirement:**

* While this failure was due to a conversion error, it underscored the importance of structured, easily testable software. High complexity exacerbates the difficulty of identifying "simple" errors in safety-critical systems.

**Lesson Learned:**

* Maintaining lower cyclomatic complexity in safety-critical components ensures better error identification and traceability during testing and validation.

---

#### **5. Lesson ID: 2433 – Software Design Defects in Launch Vehicle Systems**

**Summary:**  
Software defects in launch vehicle control systems were identified during extensive testing phases. The defects were linked to high cyclomatic complexity in certain safety-critical components, which made thorough validation challenging.

**Relevance to Cyclomatic Complexity Requirement:**

* Safety-critical software components with high cyclomatic complexity hinder comprehensive test coverage of all logical paths, increasing defect exposure.

**Lesson Learned:**

* Enforce complexity thresholds to ensure all independent paths can be reasonably tested, particularly in high-consequence systems such as launch vehicle systems.

---

#### **6. General Observation: Software Complexity and Defect Correlation**

**Summary:**  
Several NASA projects have identified a consistent pattern where higher cyclomatic complexity in software modules correlates with increased defects, reduced reliability, and higher costs for maintenance and testing.

**Relevance to Cyclomatic Complexity Requirement:**

* High cyclomatic complexity not only introduces defects but also increases testing costs, impacts reliability, and poses risks during mission-critical operations.

**Lesson Learned:**

* Cyclomatic complexity thresholds (like limiting to ≤15 in safety-critical components) are effective for minimizing risks and managing costs.
* NASA studies also support modular design practices to further reduce complexity.

---

### **General Lessons**

NASA's lessons learned database frequently highlights common themes related to controlling software complexity in critical systems:

1. **Test Coverage Sufficiency**: High complexity often leads to gaps in test coverage, particularly for rare or edge-case execution paths.
2. **Safety Assurance**: Complexity exacerbates risks in safety-critical systems, making hazard analysis and assurance reviews more challenging.
3. **Maintainability and Debugging**: Systems with high complexity create significant challenges during real-time debugging or anomaly resolution in operational environments.
4. **Cost and Schedule Risks**: High complexity drives up testing and maintenance costs and increases schedule pressure during validation phases.

---

### **How These Lessons Inform Requirement 3.7.5**

The overarching takeaway from NASA's lessons learned is that controlling cyclomatic complexity is essential for ensuring the safety, reliability, and affordability of software development in high-consequence systems. Limiting complexity to **15 or lower** for safety-critical components directly addresses the following:

* **Risk Reduction**: Lower complexity minimizes the chance of defects and untested paths.
* **Testability**: Improves the ability to thoroughly validate all independent execution paths.
* **Maintainability**: Simplifies updates and real-time debugging during mission operations.
* **Safety Assurance**: Facilitates hazard analysis and assessment for critical software functions.

---

### **References**

* NASA Lessons Learned Database (<https://llis.nasa.gov/>).
* NPR 7150.2 and NASA-STD-8739.8 Standards.
* NASA/TM−20205011566: Cyclomatic Complexity Study.
* Historical project analyses (e.g., Mars Climate Orbiter, Mars Polar Lander).

---

These lessons reinforce the importance of adhering to cyclomatic complexity thresholds in safety-critical software components as outlined in **Requirement 3.7.5**. The insights are actionable for improving project designs, testing strategies, and risk assessments.

# 7. Software Assurance

**SWE-220 - Cyclomatic Complexity for Safety-Critical Software**

3.7.5 If a project has safety-critical software, the project manager shall ensure all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. Any exceedance shall be reviewed and waived with rationale by the project manager or technical approval authority.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Perform or analyze Cyclomatic Complexity metrics on all identified safety-critical software components.

2. Confirm that all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. If not, assure that software developers provide a technically acceptable risk assessment, accepted by the proper technical authority, explaining why the cyclomatic complexity value needs to be higher than 15 and why the software component cannot be structured to be lower than 15 or why the cost and risk of reducing the complexity to below 15 are not justified by the risk inherent in modifying the software component.

## 7.2 Software Assurance Products.

### 7.2.1 Purpose and Objective:

This guidance addresses the essential assurance activities required to ensure the quality, reliability, and safety of software used in NASA projects, particularly safety-critical components. The goal is to provide assurance evidence and risk mitigation measures focusing on reducing cyclomatic complexity to enhance testability and maintainability, while minimizing the likelihood of software failure during hazardous events.

For all identified safety-critical software components, it is crucial to adhere to limits on cyclomatic complexity, ensuring compliance with NASA’s standards (NPR 7150.2 and NASA-STD-8739.8). Any deviations from these standards should be documented, reviewed, justified, and managed to ensure risks are understood and adequately mitigated.

### 7.2.2 Software Assurance Deliverables

Software assurance deliverables are required to provide confidence in the software’s compliance with assigned safety-critical standards while identifying and mitigating risks. The deliverables include the following:

1. **Software Assurance Status Reports**:

   * Periodic project status summaries documenting progress in meeting assurance requirements, with an emphasis on compliance for safety-critical components.
   * Highlight any unresolved issues, risks, and outstanding concerns related to cyclomatic complexity.
2. **Software Hazard Reports**:

   * A detailed analysis of hazards tied to software components, focusing on safety-critical areas.
   * Include mitigations or changes required to address hazards identified during the development lifecycle, especially in complex areas of code.
3. **Software Design Analysis**:

   * Perform structured reviews of software designs, focusing on architectural decisions that affect complexity, modularity, testability, and maintainability.
   * Identify design improvements for reducing complexity and coupling.
4. **Source Code Quality Analysis**:

   * Analysis of the source code's adherence to coding standards, focusing on metrics such as cyclomatic complexity, readability, modularity, and maintainability.
5. **Software Complexity Data**:

   * Evidence of all safety-critical components’ cyclomatic complexity values.
   * Provide detailed breakdowns highlighting areas that exceed the complexity threshold and propose steps for reducing complexity or managing risks appropriately.
6. **Software Assurance Risk Assessments**:

   * Assess risks associated with software components that do not meet cyclomatic complexity requirements.
   * Include technical rationale provided by developers justifying the exceedance and its acceptance or mitigation by technical authorities.
7. **Mapping Matrices**:

   * NPR 7150.2 and NASA-STD-8739.8 requirements mapping matrices signed by Engineering and SMA technical authorities for each development organization.

## 7.3 Metrics

The following metric must be monitored throughout the software assurance process:

* **Cyclomatic Complexity Value**: Report the cyclomatic complexity number for all identified safety-critical software components. Ensure it remains at or below **15** or provide justification for exceedances.

## 7.4 Guidance

### 7.4.1 Cyclomatic Complexity in Safety-Critical Software

Cyclomatic complexity is a software metric used to measure the number of independent paths through a program's source code. It provides a quantitative assessment of program structure and is closely tied to testability, defect rates, maintainability, and risk. NASA-STD-8739.8B outlines that all safety-critical software components should ideally have a cyclomatic complexity **≤15** as part of best practices for minimizing software-related risks.

### 7.4.2 Actions to Meet Compliance

1. **Measure Cyclomatic Complexity**:

   * Conduct cyclomatic complexity analysis for all safety-critical software components using static analysis tools.
   * Work closely with Engineering and, if applicable, Independent Verification & Validation (IV&V) teams to obtain accurate complexity values based on source code.
   * Document complexity values for use in assurance status reporting.
2. **Ensure Compliance**:

   * Confirm that all safety-critical software components adhere to the complexity threshold (≤15).
   * Components with complexity values exceeding 15 must be reviewed and justified via a **risk assessment** document, approved by the appropriate technical authority.
3. **Risk Assessment for Exceedance**:  
   If complexity values exceed the threshold:

   * Provide rationale explaining why the components cannot feasibly be restructured to reduce complexity.
   * Include analysis of risks associated with testing, maintainability, and defect propagation for the complex code.
   * Justify the decision to accept the complexity level based on cost, technical feasibility, or mission-critical constraints.
4. **Refactor Where Possible**:

   * Encourage developers to split large, complex modules into smaller, simpler functions or methods.
   * Ensure modular design principles are used to minimize coupling.
5. **Static Analysis Tools**:

   * Utilize tools (e.g., SonarQube, Coverity) to automatically calculate cyclomatic complexity at the code level.
   * Ensure regular monitoring and reporting of complexity values as part of continuous assurance activities.

### 7.4.3 Impacts of Cyclomatic Complexity

**Limiting Complexity During Development**:

* Helps programmers structure their code to optimize ease of testing and maintainability. Using modular design also ensures code reliability.

**Correlation with Defects**:

* Studies have shown a positive correlation between cyclomatic complexity and program defects. Higher complexity results in more testing complexity and hidden defects during development.

**Code Maintainability**:

* Lower complexity makes code easier to update, understand, and test. Highly coupled, complex code introduces risks and delays in mission-critical software updates.

**Testing Complexity**:

* Cyclomatic complexity directly determines how many test cases are needed for full coverage. For example, a complexity of 15 implies 15 independent execution paths, each requiring validation.

#### **Guidance for Exceedances**:

* Components with higher complexity (e.g., 16+) should undergo analysis to determine whether the complexity can be reduced. If not, provide a **technically acceptable rationale**, ensuring risks are identified and mitigated. Refer to NASA/TM−20205011566 for further analysis techniques.

### 7.4.4 Reference Standards and Resources

Ensure adherence to the following standards and tools:

* **NASA-STD-8739.8**: Software Assurance and Software Safety Standards.
* **NPR 7150.2**: NASA Software Engineering Requirements.
* **SWE-023**: Software Safety-Critical Requirements.
* **SWE-134**: Safety-Critical Software Design Requirements.
* NASA/TM−20205011566: Cyclomatic Complexity Study.
* **Static Analysis Tools**: SonarQube, Coverity, etc.

By applying this refined software assurance guidance, teams can effectively manage cyclomatic complexity, reduce risks, and ensure compliance with NASA safety-critical software standards.

### 7.4.5 What is Cyclomatic Complexity?

Cyclomatic complexity is a software metric used to measure the complexity of a program. These metrics measure independent paths through program source code. An independent path is defined as a path with at least one edge that has not been traversed before in any other path. Cyclomatic complexity can be calculated concerning functions, modules, methods, or classes within a program.

Thomas J. McCabe developed this metric in 1976, and it is based on a control flow representation of the program. Control flow depicts a program as a graph that consists of Nodes and Edges.

In the graph, nodes represent processing tasks while edges represent control flow between the nodes.

## Flow graph notation for a program:

Flow Graph notation for a program defines several nodes connected through the edges. Below are Flow diagrams for statements like if-else, While, until, and normal sequence of flow.

Cyclomatic complexity is a software metric used to measure the complexity of a program. These metrics measure independent paths through program source code. An independent path is defined as a path with at least one edge that has not been traversed before in any other path.  It quantitatively measures the number of linearly independent paths through a program's source code. The application of the requirement is to limit the complexity of routines during program development; programmers should count the complexity of the modules they are developing and split them into smaller modules whenever the cyclomatic complexity of the module exceeded 15. The NIST Structured Testing methodology adopted this practice. The figure of 10 had received substantial corroborating evidence.  There are occasional reasons for going beyond the agreed-upon limit. It phrased its recommendation as "For each module, either limit cyclomatic complexity to 15 or provide a written explanation of why the limit was exceeded. For example, if the source code contains no control flow statement, its cyclomatic complexity will be 1, and the source code contains a single path in it. Similarly, if the source code contains one if condition, then cyclomatic complexity is 2 because there will be two paths: true and the other for false.

Several studies have investigated the correlation between cyclomatic complexity numbers with the frequency of defects occurring in a function or method. Studies have found a positive correlation between cyclomatic complexity and defects: functions and methods with the highest complexity also tend to contain the most defects. However, international safety standards like **ISO 26262** [376](#_tabs-<p></p>)  and **IEC 62304** [375](#_tabs-<p></p>)  mandate coding guidelines that enforce low code complexity. See also [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements). 

**Use of Cyclomatic Complexity:**

* Limit code complexity.
* Determine the number of test cases required.
* Determining the independent path executions has thus proven to be very helpful for Developers and Testers.
* It can make sure that every path has been tested at least once.
* This helps to focus more on uncovered paths.
* Code coverage can be improved.
* The risk associated with the program can be evaluated.
* These metrics being used earlier in the program help in reducing the risks.

Higher numbers of cyclomatic complexity are bad, and lower cyclomatic complexity numbers are good. That's because code with high complexity is difficult to test. And it's likely to result in errors. So, code with low complexity is easier to test. And it's less likely to produce errors.

The following table gives an overview of the complex number and its corresponding meaning:

| **Complexity Number** | **Meaning** |
| --- | --- |
| 1-10 | Structured and well-written code High Testability Cost and Effort are less |
| 10-20 | Complex Code Medium Testability Cost and effort are Medium |
| 20-40 | Very complex Code Low Testability Cost and Effort are high |
| >40 | Not at all testable Very high Cost and Effort |

For safety-critical code, anything over 15 should be assessed for testability, maintainability, and code quality.

If the software safety-critical components have a cyclomatic complexity value of 16 or higher, then work with engineering to provide a risk assessment showing why the cyclomatic complexity value needs to be higher than ten and why the software component cannot be structured to be 15 or lower.

Additional information can be found in NASA/TM−20205011566, NESC-RP-20-01515, Cyclomatic Complexity, and Basis Path Testing Study [377](#_tabs-<p></p>).  

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) |

# 8. Objective Evidence

This requirement ensures that the cyclomatic complexity (a quantitative measure of code complexity based on decision paths) is managed for safety-critical software, making it easier to test, verify, and maintain software while minimizing risks. If a software component has higher complexity (exceeding 15), the project must provide a rationale or risk assessment and obtain approval for a waiver.

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

By ensuring that this evidence is clearly documented, reviewed, and approved, the project demonstrates compliance with this requirement, ensuring that safety-critical software complexity is manageable, testable, and does not pose unmitigated risks. This also provides a strong basis for explaining deviations and their acceptable handling.

Here is a detailed list of objective evidence that can be provided to demonstrate compliance with this requirement:

## 8.1 Categories of Objective Evidence

### 8.1.1 Cyclomatic Complexity Analysis Reports

* A report generated from an automated software analysis tool (e.g., Lattix, VectorCAST, Understand, LCOV, or static analysis tools like SonarQube) verifies the cyclomatic complexity values of all identified **safety-critical software components**.

##### **Must Include**:

* The cyclomatic complexity value for each safety-critical software component.
* Identification of any components exceeding the complexity threshold of 15.
* Documentation of methods used to measure complexity.

##### **Examples of Evidence**:

* **Cyclomatic Complexity Summary (Tool Output)**:

  | **Component** | **Cyclomatic Complexity Value** | **Threshold Met?** |
  | --- | --- | --- |
  | Safety\_Init.cpp | 12 | Yes |
  | FaultMonitor.cpp | 10 | Yes |
  | NavigationControl.cpp | 18 | No (Requires Waiver) |
* **Analysis Report Narrative**:

  + "Safety-critical components were assessed using 'Understand' static analysis tool. Out of 50 components analyzed:
    - 47 components met the complexity requirement.
    - 3 components exceeded a complexity score of 15, and waivers will be reviewed (see attached waiver documents)."

### 8.1.2 Source Code and Complexity Reduction Evidence

* If initial cyclomatic complexity exceeded 15 for specific safety-critical components but was later reduced through code simplification or refactoring, objective evidence must demonstrate the actions taken to meet the allowable threshold.

##### **Must Include**:

* Before-and-after complexity comparisons for refactored modules.
* Documentation of code refactoring tasks/changes performed to lower complexity.

##### **Examples of Evidence**:

* **Code Simplification Logs**:
  + "NavigationControl.cpp complexity reduced from 18 to 14 by restructuring nested decision logic into modular functions (commit ID: `a7bc234`). Attached are refactored code reviews and updated complexity reports."
* **Change Request (CR) Records**:
  + Change requests or tickets summarizing the plans, actions, and results for reducing cyclomatic complexity.
    - Example: "Refactored propulsion software module to separate fault-detection logic into a separate module, reducing `PropulsionMonitor.cpp` complexity from 20 to 11."

### 8.1.3 Requirements Traceability Matrix (RTM)

* A traceability matrix mapping safety-critical software components to their cyclomatic complexity evaluations ensures compliance with the requirement. It provides a clear link between the requirements, code components, and corresponding analysis.

##### **Must Include**:

* Software requirements for complexity thresholds.
* Mapping of all safety-critical software components to their complexity scores.
* Status indication of mitigation measures or waivers for components exceeding the threshold.

##### **Examples of Evidence**:

* **RTM Example Excerpt**:

  | **Requirement ID** | **Safety-Critical Component** | **Complexity Value** | **Action Taken** | **Waiver Required** |
  | --- | --- | --- | --- | --- |
  | SC-REQ-105 | FaultMonitor.cpp | 10 | N/A | No |
  | SC-REQ-140 | EmergencyShutdown.cpp | 16 | Waiver Approved | Yes |
  | SC-REQ-190 | PropulsionControl.cpp | 12 | N/A | No |

### 8.1.4 Waivers and Rationale for Exceeded Cyclomatic Complexity

* Any exceedance of the cyclomatic complexity threshold (i.e., value > 15) must be formally reviewed and approved by the project manager or technical approval authority. Objective evidence includes the waiver documentation and the accompanying rationale.

##### **Must Include**:

* **Detailed Waiver Justification** for exceeding cyclomatic complexity, addressing:
  + Why the high complexity is necessary and unavoidable for the component.
  + An explanation of why refactoring or redesign is not feasible or justifiable.
  + A **Risk Assessment**, describing the functional and safety-critical impact of leaving the high complexity unmitigated.
* **Approval Signatures**: Formal approval of the waiver by the project manager and/or technical approval authority.

##### **Examples of Evidence**:

* **Waiver Documentation Example**:
  + **Component**: `EmergencyShutdown.cpp`
  + **Cyclomatic Complexity**: 16
  + **Rationale for Exceedance**: "The component manages interdependent safety-critical paths and decision trees that cannot be further modularized without compromising real-time constraints. Additionally, fault injection tests demonstrate reliable error recovery and system fail-safes."
  + **Risk Mitigation**: "Increased testing (including fault injection and boundary condition handling) to validate components with complexity exceeding 15."
  + **Approval**: Project Manager and SMA signed off on waiver under document ref. WVR-XYZ-2024.

### 8.1.5 Risk Assessment Reports for High-Complexity Components

* When a component's complexity exceeds 15, a risk assessment must be performed to ensure sufficient safeguards are in place to mitigate potential challenges in testing, maintaining, and verifying the software.

##### **Must Include**:

* Analysis of risks posed by high complexity, such as:
  + Increased difficulty in testing all possible decision paths.
  + Potential for undetected faults to arise due to untested branches.
* Mitigation plans, such as:
  + Adding redundancy or safety monitoring tests.
  + Independent Verification & Validation (IV&V) on high-complexity software.

##### **Examples of Evidence**:

* **Risk Assessment Report Example**:
  + "Component `NavigationControl.cpp` complexity of 18 increases the difficulty of ensuring full path coverage during validation. Additional IV&V testing was conducted, with performance results confirming no unbounded decision outcomes under nominal or off-nominal conditions."

### 8.1.6 Independent Verification and Validation (IV&V) Assessment Reports

* If complexity thresholds are exceeded, an IV&V review provides confidence that safety-critical software undergoes rigorous testing and validation. Objective evidence shows the IV&V team assessed adherence to requirements in light of elevated complexity.

##### **Must Include**:

* Reports from independent review teams verifying:
  + Coverage of code paths in high-complexity components.
  + Safety-critical functions operate reliably despite increased complexity.
* Recommendations provided by IV&V and actions taken to address concerns.

##### **Examples of Evidence**:

* **IV&V Assessment Summary**:
  + "The IV&V team completed its review of `PropulsionControl.cpp` (complexity: 16) and confirmed that mitigation measures (modularized test coverage and additional validation through boundary-condition testing) sufficiently reduce risks."

## 8.2 Summary of Objective Evidence

| **Category** | **Examples of Evidence** |
| --- | --- |
| **Cyclomatic Complexity Reports** | Tool-generated complexity values for each safety-critical software component (with breakdowns by function, line, branches). |
| **Code and Refactoring Evidence** | Before-and-after complexity values showing code refactoring tasks lowered complexity where possible. |
| **Traceability Matrix** | Mapping of components to their complexity and corresponding actions (e.g., tests, mitigations, waivers). |
| **Waiver Documentation** | Formal waiver requests and signed rationale for components exceeding complexity threshold. |
| **Risk Assessment** | Analysis of the risks posed by high complexity and mitigation efforts such as additional testing or redundancy. |
| **IV&V Review Reports** | Independent validation of high-complexity components to ensure safety and reliability. |
