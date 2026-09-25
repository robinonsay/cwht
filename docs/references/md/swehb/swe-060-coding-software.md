# SWE-060 - Coding Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695444. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software

SWE-060 - Coding Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695444)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695444&showCommentArea=true&showComments=true#addcomment)

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

4.4.2 The project manager shall implement the software design into software code.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-060 History

SWE-060 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.3.1 The project shall implement the software design into software code. |
| Difference between A and B | No change |
| B | 4.4.2 The project manager shall implement the software design into software code. |
| Difference between B and C | No change |
| C | 4.4.2 The project manager shall implement the software design into software code. |
| Difference between C and D | No change |
| D | 4.4.2 The project manager shall implement the software design into software code. |

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

This requirement begins the implementation section of the NPR 7150.2. It acknowledges that the project has the primary responsibility for producing the software code. The NPR notes that the "software implementation consists of implementing the requirements and design into code, data, and documentation. Software implementation also consists of the following coding methods and standards. Unit testing is also a part of software implementation." Other guidance areas in this Handbook cover the requirements for data, documentation, methods, standards, and unit testing (see the table in the guidance section for this requirement).

This requirement is essential to ensure that the transition from software design to implementation is deliberate, controlled, and aligned with project objectives and standards. Here’s the rationale:

1. **Design-to-Code Traceability:**

   * Implementing software design into code ensures that the developed software is aligned with the approved architecture and design specifications. This traceability minimizes the likelihood of deviations that could lead to defects or missed requirements.
2. **Controlled Execution:**

   * Assigning this responsibility to the project manager ensures oversight and accountability during the critical phase of transforming design into executable code. The project manager ensures that development adheres to schedule, resource plans, and quality standards.
3. **Consistency and Integrity:**

   * A structured implementation ensures that the overall design, functional requirements, and system constraints are consistently translated into the codebase, preserving the project’s integrity.
4. **Risk Mitigation for Errors and Flaws:**

   * Mistakes in implementation can introduce significant risks to mission success. Connecting the design process directly to the coding effort, under proper oversight, helps promptly identify and address potential gaps or inconsistencies.
5. **Compliance with Standards:**

   * A direct implementation process focused on adhering to the design ensures compliance with software development standards, such as NASA’s stringent guidelines for safety-critical systems.
6. **Alignment with Larger Lifecycle Goals:**

   * This requirement supports the software lifecycle by ensuring that the implementation phase builds a stable foundation for downstream tasks, such as testing and integration, reducing costly rework during later stages.
7. **Efficient Resource Management:**

   * Proper oversight and adherence to design constraints prevent unnecessary redesign or rework, helping optimize the use of time, budget, and personnel.
8. **Supports Software Assurance Objectives:**

   * Direct implementation of the design facilitates software assurance activities, such as automated checks and manual reviews, by maintaining clear design-code alignment.

In essence, this requirement ensures that the software development process is rigorous, traceable, and aligned with design standards, maintaining project integrity and reducing risks to mission success. It emphasizes the crucial link between the theoretical (design) and practical (code) aspects of software development, enabling efficient and quality-driven project execution.

See also [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design).

# 3. Guidance

## 3.1 Coding Standards

Adhering to established software coding standards ensures consistency, reduces errors, and improves code quality. Coding standards promote uniform practices within development teams, simplify code reviews, and enhance collaboration (see SWE-061 - Coding Standards). For outsourced development, specifying and enforcing coding standards ensures the supplier’s code meets NASA-STD-8739.8 Software Assurance and Safety requirements.

Key takeaways:

* Coding standards reduce ambiguity in team or collaborative environments, resulting in faster reviews and fewer oversight errors.
* For external contractors, agreed-upon standards ensure alignment with NASA's quality and safety guidelines.
* Refer to SWE-185 for secure coding verification.

---

## 3.2 Accredited Tools

Utilizing accredited development tools is critical to ensuring software’s reliability, traceability, and compliance with standards (see SWE-136 - Software Tool Accreditation). Development processes must evaluate and accredit tools when used in new environments or combinations.

* Commonly used tools, such as Simulink and MATLAB, have been extensively tested in NASA projects, but their outputs (e.g., auto-generated code) must be verified against project standards to identify and resolve potential bugs.
* Small projects might use standalone tools, whereas larger projects should rely on Integrated Development Environments (IDEs) to streamline coding, testing, and debugging.

**IDEs typically include:**

1. **Source Code Editor:** Facilitates efficient coding.
2. **Compiler/Interpreter:** Transforms source code into machine-readable code.
3. **Build Automation Tools:** Automates repetitive development tasks.
4. **Debugger:** Identifies and resolves software issues during development.

* Refer to the Process Asset Library (PAL) at your Center for IDE recommendations, and consult SPAN or NEN for a comprehensive list of tools and environments.
* For auto-generated code, see Topic 8.11 and ensure plans are in place for rigorous testing and certification.

---

## 3.3 Executable Code

During this phase, the high-level and detailed design specifications are implemented into executable code, including algorithms, data structures, and interfaces. This is the bridge between software design and functional systems.

**Key considerations:**

* Accurate implementation of algorithms and inter-component communication is essential to maintain system integrity.
* Generated code should be carefully reviewed and validated to prevent defects. The use of accredited tools ensures compliance with standards during compilation.

---

## 3.4 Unit Testing

Regular unit testing and debugging during coding ensure that errors are detected early, minimizing costly fixes during later phases.

Objectives of unit testing:

1. Validate that the unit fulfills its assigned capability.
2. Confirm correct interaction with other units or data.
3. Verify faithful implementation of the design.

**Best practices:**

* Use static analysis tools to uncover vulnerabilities (e.g., dead code, memory leaks, security flaws).
* Perform code walkthroughs and peer inspections to identify potential issues and improve practices (see SWE-062 - Unit Test).
* For safety-critical systems, refer to Topic 8.19 to identify dead/dormant code.

---

## 3.5 Optimizing Code

Code optimization improves performance but must be balanced with other considerations such as stability, maintainability, and portability.

**Recommendations for optimization:**

* Plan for multiple compiler passes to maximize efficiency.
* Focus on practical optimization (e.g., reducing redundancy, streamlining interfaces) and avoid excessive optimization that complicates debugging and maintenance (e.g., inline assembly or superscalar coding).
* Weigh the benefits of optimization against potential risks like compatibility issues or the time required to manage intricate optimizations.

---

## 3.6 C Programming Practices for Safety

Safe development practices for C programs are critical, particularly for systems requiring strict reliability and safety considerations.

**Checklist of key practices:**

1. **Parameter Management:** Limit the number and size of parameters to enhance readability and prevent stack overflow. Pass large data structures by reference, not by value.
2. **Recursive Functions:** Use recursion cautiously; verify finite recursion to avoid stack overflows.
3. **Boundary Checks:** Implement custom boundary-checking functions to prevent out-of-bounds errors with arrays/strings.
4. **Avoid Unreliable Functions:** Replace functions like `gets` with safer custom routines.
5. **Memory Management:** Use `memmove` (instead of `memcpy`) for potential memory overlap and create wrappers for built-in functions to include error handling.
6. **Control Structures:** Use `switch...case` instead of deeply nested `if...else if...` structures for clarity. Always include a default case and define appropriate *break* statements.
7. **Variable Initialization:** Initialize both local and global variables explicitly to prevent unpredictable behaviors.
8. **Pointer Safety:** Validate pointers to ensure references are within scope and avoid using function pointers unless absolutely necessary.
9. **Function Prototypes:** Define prototypes to enable compile-time error detection.
10. **Data Type Safety:** Avoid mixing signed and unsigned variables, and use explicit casting. Be cautious with floating-point comparisons.
11. **Enable Compiler Warnings:** Treat warnings as errors to prompt early fixes.
12. **Concurrency Safety:** Ensure standard library functions in multitasking environments are reentrant and avoid interrupt service routine calls unless necessary.
13. **Code Readability:** Use comments and avoid shorthand operators (`?:`). Define numeric literals via `#define` for better readability and maintainability.
14. **Avoid Assumptions:** Do not assume platform- or compiler-specific features, such as type sizes or reserved words, will always work.

These practices enhance the safety, readability, and reliability of C programs, particularly in mission-critical applications.

---

By incorporating these improvements, the updated guidance emphasizes actionable steps, streamlines instructional content, and supports NASA’s focus on safety, reliability, and quality across its software engineering practices.

Once the software development team has completed the software architecture and the software detailed design, the exacting task of turning the design into code begins. The use and adherence to the project's software coding standards will enhance the resulting code and reduce coding errors (see [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards)). In a team environment or group collaboration, coding standards ensure uniform coding practices; it reduces oversight errors and the time spent in code reviews. When NASA software development work is outsourced to a supplier, the agreement on a set of coding standards ensures that the contractor's code meets all quality guidelines mandated by NASA-STD-8739.8, Software Assurance, and Software Safety Standard. [278](#_tabs-<p></p>)

See also [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification),

See also Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code).

See also [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test).

See also Topic [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software),

See also [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access), [PAT-032 - Considerations When Using Interrupts](/spaces/SITE/pages/123600994/PAT-032+-+Considerations+When+Using+Interrupts),

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [PAT-032 - Considerations When Using Interrupts](/spaces/SITE/pages/123600994/PAT-032+-+Considerations+When+Using+Interrupts) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For small software projects, the transition from design to implementation should remain systematic and efficient while adhering to the requirements for high-quality, maintainable, and reliable code. Below is tailored guidance and best practices for small projects:

---

#### **1. Simplify and Use Lightweight Processes**

* **Streamline Documentation:** Use lightweight design documentation tools, such as flowcharts, UML diagrams, or whiteboard sketches, to ensure effective communication of software design without unnecessary complexity.
* **Iterative Approach:** Implement the design incrementally using agile or iterative methods, allowing for quick feedback and adjustments during development cycles.

---

#### **2. Focus on Coding Standards**

* **Adopt Clear Coding Standards:** Ensure that even for small teams, all developers follow uniform coding standards (see SWE-061 - Coding Standards). This promotes consistency across the codebase and simplifies future maintenance.
* **Start with Existing Best Practices:** Utilize pre-existing coding standards and secure coding guidelines from repositories such as NASA’s Process Asset Library (PAL) or Software Processes Across NASA (SPAN), if applicable.

---

#### **3. Define Accountability and Collaboration**

* **Small Team Accountability:** Assign a specific team member or the project manager to oversee implementation, ensuring the design is faithfully transformed into code.
* **Frequent Team Check-Ins:** For small teams, frequent communication (e.g., weekly standups) is critical to ensure the design principles are being followed during implementation.

---

#### **4. Balance Tool Selection**

* **Use Lightweight Development Tools:** For small projects, choose simple, lightweight IDEs or text editors (e.g., VS Code, Eclipse) and accredited development tools that meet basic requirements without adding overhead (see SWE-136 for tool accreditation).
* **Leverage Automated Tools:** Use tools that fit smaller workloads, such as static code analyzers (e.g., SonarQube for small teams) to identify errors and enforce coding standards without heavy tooling.

---

#### **5. Prototype or Focus on Minimal Viable Product (MVP)**

* **Reduce Unnecessary Complexity:** For small projects, focus on implementing the core functionality of the design first. Avoid over-engineering by implementing essential features first and layering in additional functionality later.

---

#### **6. Test as You Code**

* **Regular Unit Testing:** For small projects, carry out unit testing early and often. Use lightweight test frameworks (e.g., JUnit, Pytest) for small-scale verification.
* **Static Analysis and Debugging:** Incorporate static analysis tools and peer reviews into the workflow to catch bugs early. This approach avoids expensive troubleshooting in later phases.

---

#### **7. Risk Management and Design Iteration**

* **Start Small, Adapt as Needed:** If constraints (e.g., budget, timeline, workforce) force design modifications, iterate on the design rapidly and document changes clearly to maintain traceability.
* **Identify and Manage Risks:** For small projects, focus on high-impact design elements and critical failure points when managing risks during the implementation phase.

---

#### **8. Post-Implementation Practices**

* **Code Reviews:** Even in small projects, involve the team in collaborative code walkthroughs for quality assurance.
* **Maintainable Code:** Ensure the code developed is simple, properly commented, and aligned with the approved design for easier handoffs and maintenance.

---

#### **Summary for Small Projects**

The implementation of software design into code for small projects can be made efficient by using lightweight, iterative development processes. Focus on simplicity, automation, and collaboration to ensure quality while minimizing effort. By emphasizing effective coding practices, using accredited tools, and maintaining traceability to the design, small projects can achieve the same level of reliability and quality as larger projects, scaled appropriately to their scope and resources.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-208)

  [Programming Optimization,](http://www.azillionmonkeys.com/qed/optimize.html "Click to open in new window")

  Hsieh, Paul., 2007. Accessed November 28, 2017 from http://www.azillionmonkeys.com/qed/optimize.html.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-368) Software Version Description Template,  GRC-SW-TPLT-SVD, 2011. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-382)

  [Review Guidelines on Software Languages for Use in Nuclear Power Plant Safety Systems Final Report,](https://www.nrc.gov/docs/ML0634/ML063470583.pdf "Click to open in new window")

  NUREG/CR-6463, H. Hecht, M. Hecht, S. Graff, W Green, D. Lin, S. Koch, A. Tai, D. Wendelboe, SoHar Incorporated, U.S. Nuclear Regulatory Commission
* (SWEREF-417)

  ["The Power of 10: Rules for Developing Safety-Critical Code"](http://spinroot.com/gerard/pdf/Power_of_Ten.pdf "Click to open in new window")

  Holzmann, G.J., NASA Jet Propulsion Laboratory (JPL), 2006.
* (SWEREF-418)

  ["Certifying Auto-generated Flight Code"](https://slideplayer.com/slide/1457415/ "Click to open in new window")

  Denney, E., NASA Ames, 2008. Related: https://ti.arc.nasa.gov/m/profile/edenney/papers/Denney-BigSky-08.pdf

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The transition from design to code is a critical step in software development, especially in the high-stakes environment of NASA projects where failures can have significant consequences. The **NASA Lessons Learned Information System (LLIS)** provides several relevant insights that organizations should consider for implementing software design into code. The following lessons learned highlight the importance of this requirement:

---

### **1. Importance of Design Traceability to Code**

**Lesson: Lack of traceability between system design and code can result in missed requirements and increased defects during integration testing.**

* **Source:** NASA LLIS No. 1778 – **“Mars Climate Orbiter Mishap”**
* **Details:** The Mars Climate Orbiter failed due to a unit conversion error that was not adequately traced from the system-level design into the software. A lack of rigorous processes for design-to-code implementation contributed to the failure, as the discrepancy between metric and imperial units in the design was not caught.
* **Key Guidance:** Project managers must ensure that there is a strong traceability mechanism in place, verifying that every requirement and design element is implemented correctly in the code. Automated tools and manual reviews can assist in this process.

---

### **2. Adherence to Coding Standards**

**Lesson: Failure to use or enforce consistent coding standards can lead to non-optimal code that is difficult to maintain and error-prone.**

* **Source:** NASA LLIS No. 2202 – **“Mars Polar Lander Software Error”**
* **Details:** The Mars Polar Lander mission failed partly due to coding errors introduced in the software implementation phase. Inconsistent coding practices, unchecked use of logic relationships, and inadequate unit tests led to unintended thruster shutdown during the descent phase.
* **Key Guidance:** Establish and rigorously enforce coding standards to ensure consistency, readability, and error prevention early in the implementation phase. This includes secure coding practices, especially for mission-critical systems.

---

### **3. The Role of Reviews and Inspections During Implementation**

**Lesson: Inadequate or inconsistent design and code reviews fail to identify issues in early phases, leading to costly fixes later.**

* **Source:** NASA LLIS No. 1564 – **“Software Development Process Weaknesses”**
* **Details:** During software development for a major NASA mission, insufficient use of formal design and code inspections allowed software defects to propagate through the system. These defects were only discovered late in the lifecycle, requiring extensive rework.
* **Key Guidance:** Project managers should enforce regular peer reviews and inspections during the implementation phase to detect and address discrepancies between the design and code early. This reduces downstream defects and helps maintain project timelines.

---

### **4. Automated Code Generation and Validation**

**Lesson: Auto-generated code can lead to inefficiencies and bugs if not validated against the original design specifications.**

* **Source:** NASA LLIS No. 1984 – **“Flight Software Validation – Lessons Learned”**
* **Details:** A NASA mission experienced significant challenges when relying on auto-generated code from design models. Bugs introduced during code generation were not detected until the integration testing phase, leading to delays and increased costs.
* **Key Guidance:** If using auto-generated code, project managers must implement robust validation processes to ensure fidelity between the design model and the generated code. Validation should include unit testing, static analysis, and compliance checks against the design.

---

### **5. Incremental and Iterative Implementation Practices**

**Lesson: A "big-bang" approach to implementing designs into code leads to longer lead times for error discovery and higher risks.**

* **Source:** NASA LLIS No. 2197 – **“Software Implementation and Testing Lessons from Small Missions”**
* **Details:** Small and agile NASA projects demonstrated success by adopting incremental and iterative approaches to implement code from the design. By breaking the implementation into smaller pieces with regular testing, teams reduced the overall risk and improved defect detection rates.
* **Key Guidance:** Incremental builds and iterative development should be encouraged to allow for faster feedback on implementation quality. This approach ensures realigned focus on critical design elements, reducing integration challenges.

---

### **6. Importance of Early and Accurate Unit Tests**

**Lesson: Lack of well-defined unit testing during implementation can lead to a buildup of defects that are harder to detect later.**

* **Source:** NASA LLIS No. 1241 – **“Challenges in Software Unit Testing”**
* **Details:** Early and rigorous unit testing was identified as a key factor for success in software implementation. Projects that delayed unit tests faced significant challenges during integration and system testing, where the cost to fix errors was much higher.
* **Key Guidance:** Project managers must enforce early and comprehensive unit testing, ensuring that each code module aligns with the design and performs as expected. Unit tests should include both positive and negative test cases with automated and manual validation as necessary.

---

### **7. Alignment of Team Skill Sets to Implementation Needs**

**Lesson: Lack of experience in translating complex designs into efficient and maintainable code can lead to implementation bottlenecks.**

* **Source:** NASA LLIS No. 1665 – **“Software Workforce Competency Lessons Learned”**
* **Details:** In several NASA projects, teams with insufficient experience in the programming language or toolchain faced difficulties in implementing designs correctly. Misinterpretation of design intent led to poorly written, non-performant code.
* **Key Guidance:** Ensure team members possess the appropriate technical expertise and training for implementing the design. If skill gaps are identified, provide training or allocate experienced developers to high-risk implementation tasks.

---

### **8. Configuration Management**

**Lesson: Failure to manage code configuration and changes effectively leads to divergences from the original design.**

* **Source:** NASA LLIS No. 2038 – **“Configuration Management for Software Development”**
* **Details:** In one software project, uncontrolled changes during the coding phase caused mismatches with the baseline design, introducing significant integration problems. A lack of robust configuration management contributed to code that did not meet mission requirements.
* **Key Guidance:** Implement configuration management practices to ensure disciplined control of code changes. Regularly track and validate that all changes align with the approved design.

---

### **Summary of Key Lessons for Requirement 4.4.2**

1. **Traceability:** Establish clear mapping between design and implementation to prevent misalignment.
2. **Coding Standards:** Enforce uniform coding best practices to reduce errors and improve quality.
3. **Validation:** Conduct regular reviews, unit tests, and validation of code against design.
4. **Automation:** Use auto-generation and static analysis tools but validate rigorously.
5. **Incremental Approach:** Implement the design iteratively to reduce risk and improve feedback.
6. **Team Competency:** Ensure the development team is skilled and has the tools necessary for implementation.

By applying these lessons, NASA teams can improve the reliability of their design-to-code implementation process and align with the high standards for mission-critical software systems.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-060 - Coding Software**

4.4.2 The project manager shall implement the software design into software code.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the software code implements the software designs. 

2. Confirm that the code does not contain functionality not defined in the design or requirements.

## 7.2 Software Assurance Products

Software assurance products validate and ensure the quality of the software implementation and its alignment with the design. The following deliverables should cover key assurance activities during implementation:

1. **Software Design Analysis Results:** Confirm that the design adheres to requirements, is feasible for coding, and is structured to minimize implementation risks.

   * Use traceability tools to ensure all elements of the design have been implemented properly in the software.
2. **Software Code Quality Analysis Results:**

   * Report detailing compliance with coding standards, adherence to secure coding practices, and identification of quality risks (e.g., dead code, spaghetti code).
3. **Software Requirements Analysis Results:**

   * Analysis confirming that all design elements align with and fulfill approved software requirements. Identify gaps where design or code is implemented without corresponding requirements or where requirements lack implementation.
4. **Static Code Analysis Results:**

   * Output from automated tools to detect issues such as code complexity, security vulnerabilities, memory leaks, and logical errors that could compromise software functionality.
5. **Code Coverage Metric Data:**

   * Provide evidence that the test routines adequately cover the implemented code, verifying execution of all paths, including corner cases and fault scenarios.

---

## 7.3 Metrics

Metrics help quantify assurance activity success and identify risks during the implementation phase. The following metrics are recommended:

1. **Code Coverage Data:**

   * Percent execution of code tested during unit, integration, or system-level testing, including:
     + Line coverage (all code lines tested).
     + Branch coverage (testing conditional paths, e.g., "if," "else").
     + Path coverage (testing possible execution paths).

   **Target Thresholds:**

   * For safety-critical software, strive for **100% coverage** of all reachable code during testing phases.
2. **Implementation Metrics:**

   * **Planned vs. Completed Units:**
     + Measure the number of units planned for implementation vs. those implemented and tested.
     + Use this ratio to monitor progress against schedule and identify areas where delays or risk accumulation occur.
3. **Traceability Metrics:**

   * Number of design elements traced to requirements: Evaluate whether each design feature maps back to a source requirement and whether each requirement corresponds to implemented software.
4. **Defect Density:**

   * Number of defects per unit size (e.g., lines of code, functional areas) detected during implementation. Lower defect density correlates to higher-quality code.

**Additional Resources:**  
Refer to Topic 8.18 - Software Assurance Suggested Metrics for expanded metric recommendations.

---

## 7.4 Guidance

In the implementation phase of software development, the fidelity between the design and the code being developed must be precise and validated. Software assurance plays a critical role in ensuring compliance and identifying risks during this process.

#### **Key Assurance Activities**

1. **Traceability Validation:**

   * Confirm that **all implemented code traces back to the design** and that **the entire design has been implemented in software**. Traceability tools—such as bi-directional traceability matrices—are critical for verifying alignment.
     + Run tools that identify **orphan code** (code with no corresponding design element) or **orphan design elements** (designs without a corresponding implementation).
2. **Requirement Verification:**

   * Cross-check that **all design elements map back to documented requirements**. If parts of the design have no linked requirements, document gaps and evaluate whether the design must change or whether requirements need to be updated to justify implementation.
3. **Static Code Analysis:**

   * Use automated tools to analyze the generated code, focusing on quality-related metrics like security vulnerabilities, unused code elements, and logical inconsistencies. Static analysis helps ensure compliance with coding standards early in the process, reducing the risk of costly fixes later in the lifecycle.
4. **Design Review Assurance:**

   * Verify that the design itself is implementable using practical coding techniques. Special attention should be paid to high-risk areas such as complex algorithms, inter-module communication, and concurrency.
5. **Code Completeness:**

   * Confirm that all components of the code fulfill their intended functional requirements. Unaddressed gaps in implementation must be flagged for corrective actions.
   * Validate areas prone to incomplete implementation, such as error handling, boundary conditions, and safety-critical modules.

---

## 7.4.1 Checklist: Programming Practices for Safety and Reliability

Extend the coding practices for C programs into broader programming contexts (e.g., Python, C++, Java). The following checklist ensures reliable code implementation across all programming ecosystems:

#### **Safe Programming Practices**

* **Parameter Handling:**

  + Avoid excessive numbers of parameters in functions; pass large structures and arrays by reference instead of by value.
  + Limit recursion depth, ensuring finite recursion to prevent stack overflow.
* **Boundary Checking:**

  + Implement boundary-checking utilities to prevent out-of-bounds errors for arrays and strings.
* **Avoid Non-Safe Library Functions:**

  + Replace unsafe functions such as `gets()` and `memcpy()` with stricter, safer alternatives (`fgets()`, `memmove()`).
* **Structured Control Flow:**

  + Use `switch...case` for complex conditions instead of deeply nested `if...else` constructs. Always include a `default` case with a clear exit path (e.g., `break`).
* **Variable Initialization:**

  + Ensure all automatic and global variables are explicitly initialized before use. Maintain consistent initialization methods for system warm states.
* **Pointer Management:**

  + Strictly validate all pointers to prevent dangling references or memory access outside variable scope.

#### **Code Design Principles**

* Prototype all functions to enable compile-time error checks.
* Minimize ambiguity in interface arguments, avoiding unnecessary use of expressions for routine parameters.
* Enable all compiler warnings and treat them as errors. Warnings often highlight subtle issues that could cause runtime problems.

#### **Concurrency and Multitasking Practices**

* Avoid non-reentrant library functions in multitask environments; ensure task-safe synchronization mechanisms.
* Minimize the use of interrupt service routines within function calls. If unavoidable, use small, reentrant functions.

#### **Readable Code Guidelines**

* Use meaningful variable names instead of placeholders (e.g., `RADIUS_OF_EARTH_IN_KM` instead of ambiguous numerical literals).
* Place all `#include` directives at the top of source code files for clarity.
* Avoid deprecated practices such as mixing signed and unsigned variables without explicit casts, or inappropriate floating-point comparisons.

---

### **Tools and Automation Recommendations**

Software assurance during implementation benefits greatly from the use of modern tools and practices. Recommendations include:

* **Static Analysis Tools:** Use tools like Coverity, SonarQube, or CodeSonar to uncover issues early.
* **Code Reviews:** Peer inspections coupled with auto-generated defect reports enhance code quality.
* **Automated Metrics Dashboards:** Implement dashboards to track metrics such as code coverage, defect density, and traceability progress.

---

### **Summary**

This improved guidance emphasizes traceability, validation, code quality, and safe coding practices to ensure the implementation phase results in software that aligns with its design and requirements. By leveraging automation tools, enforcing coding standards, and adhering to safety practices, project teams can improve reliability and reduce risks during software implementation.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [PAT-032 - Considerations When Using Interrupts](/spaces/SITE/pages/123600994/PAT-032+-+Considerations+When+Using+Interrupts) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical for demonstrating that the software implementation process meets the design intent, complies with coding standards, and aligns with the project's quality and safety requirements. Below is a categorized list of evidence that can support verification and validation activities for this requirement:

---

### **1. Traceability Artifacts**

* **Bidirectional Traceability Matrix (BTM):**

  + A matrix showing that all implemented code traces back to software design elements and that the entire design is reflected in the code.
  + Verifies no "orphan" code (code without corresponding design) or "orphan" design elements (design with no corresponding code).
  + Ensures traceability across requirements, design, and implemented code.
* **Traceability Reports From Tools:**

  + Reports from automated tools (like DOORS, Jama Connect, or Polarion) showing the full traceability lifecycle: from requirements → design → code → tests.

---

### **2. Code Artifacts**

* **Codebase Repository Logs:**

  + Version-controlled logs (e.g., from Git, Bitbucket) showing when, how, and by whom the software code was implemented.
  + Include evidence of code reviews/peer reviews and corresponding approvals for each commit.
* **Design-to-Code Transition Checklist:**

  + A completed checklist documenting that all design elements were addressed during implementation.
  + Includes confirmation of adherence to coding standards and secure coding practices.
* **Self-Documenting Code Practices:**

  + Examples of in-code comments that reference design artifacts (e.g., section numbers, document IDs) to demonstrate that the code corresponds to specific design elements.

---

### **3. Code Quality Assurance Evidence**

* **Static Code Analysis Reports:**

  + Outputs from tools like Coverity, CodeSonar, or SonarQube showing:
    - Compliance with coding standards.
    - Identification and resolution of issues (e.g., unused variables, memory leaks, security vulnerabilities).
  + Includes before-and-after snapshots to demonstrate defect resolution during implementation.
* **Code Coverage Reports:**

  + Reports indicating the percentage of code executed during unit, integration, or system-level tests.
  + Evidence that all implemented code is testable and no unused/unreachable code exists in the system.
* **Coding Standards Compliance Report:**

  + Document showing adherence to approved coding standards (e.g., MISRA C for C/C++ or secure practices for Python/Java).

---

### **4. Software Testing Evidence**

* **Unit Test Reports:**

  + Results showing that each implemented code unit performs as designed.
  + Includes details on the test cases, expected results, actual results, and evidence of bugs resolved during development.
* **Test Procedure Documentation:**

  + Evidence that test cases were designed to verify the fidelity between software design and code implementation.
  + Includes references to specific requirements or design elements covered by the tests.
* **Dynamic Code Analysis Results:**

  + Metrics such as stack usage, memory usage, and runtime performance that confirm implementation meets performance and system constraints defined in the design.

---

### **5. Configuration Management Evidence**

* **Configuration Management Records:**

  + Evidence of proper version control during implementation:
    - Code revisions are linked to specific baseline designs.
    - Change requests and approvals tracked in a configuration management system (e.g., SVN, GitLab, or Jira).
* **Change Impact Analysis Records:**

  + Evidence that any changes to the code during the implementation phase were reviewed and their impacts on design, requirements, or safety were documented and approved.
* **Build Logs and Reports:**

  + Logs of compiled code demonstrating successful builds, no critical warnings/errors, and alignment with the intended design.

---

### **6. Software Reviews and Audits**

* **Code Review Records:**

  + Evidence of systematic code reviews (manual or tool-assisted) to ensure fidelity to the design and compliance with standards.
  + Include documented findings and evidence of resolved issues from peer reviews.
* **Peer Review Checklists:**

  + Completed checklists used during peer reviews to confirm adherence to design and coding standards.
* **Implementation Audit Reports:**

  + Reports from independent audits that confirm the entire implementation process adhered to project plans, coding standards, and traceability requirements.
* **Software Design Review/Inspection Records:**

  + Records of interim design reviews and inspections performed before and during implementation.
  + Ensure no discrepancies between the design and the implemented code.

---

### **7. Design Validation Evidence**

* **Test Matrices:**

  + A matrix mapping all testing activities to design elements and implemented code to confirm that they meet the specified requirements.
* **Prototype or Working Models:**

  + Evidence of functioning prototypes developed during the implementation phase to ensure designs are correctly translated into working software.
* **Automated Code Validation Reports:**

  + Outputs from tools like Simulink or MATLAB (if applicable) documenting a comparison between the design model and the generated code.

---

### **8. Documentation Supporting Key Activities**

* **Implementation Plan:**

  + Documentation outlining the approach taken to translate design into code, including tools, techniques, and personnel assignments.
* **Developer’s Notes/Logbook:**

  + Logs maintained by developers documenting challenges, deviations, or design interpretation decisions during implementation.
* **Safety-Critical Code Analysis:**

  + Evidence of additional reviews/tests conducted for safety-critical portions of the code to ensure compliance with safety standards (e.g., NASA-STD-8739.8).

---

### **9. Metrics Reports**

* **Implementation Progress Metrics:**

  + Data demonstrating the status of implementation, such as the number of planned code units vs. implemented and tested units.
* **Defect Density Metrics:**

  + Reports on the number of defects identified during implementation and their resolution status, categorized by severity.
* **Improvement Metrics:**

  + Evidence of issues raised and resolved during reviews or static/dynamic analysis and how these contributed to code quality improvement.

---

### Summary of Key Objective Evidence:

1. **Traceability Artifacts:** Bi-directional trace matrices and traceability tool outputs.
2. **Code Artifacts:** Version-controlled repository logs and evidence of adherence to coding standards.
3. **Testing Evidence:** Unit and code coverage test results and dynamic code metrics.
4. **Code Quality Analysis Reports:** Evidence from static analysis, defect tracking, and coverage tools.
5. **Configuration Management Records:** Build logs, version histories, and change impact analysis reports.
6. **Review and Audit Documents:** Peer reviews, software design/code inspections, and audit findings.
7. **Documentation and Metrics:** Implementation plans, progress reports, and defect density metrics.

Each of these artifacts demonstrates compliance with Requirement 4.4.2, ensuring that all software implementation activities align with the design, meet quality standards, and are fully traceable to project objectives and requirements.

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
