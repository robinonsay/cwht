# SWE-206 - Auto-Generation Software Inputs

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695540. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs

SWE-206 - Auto-Generation Software Inputs

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695540)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695540&showCommentArea=true&showComments=true#addcomment)

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

3.8.2 The project manager shall require the software developers and custom software suppliers to provide NASA with electronic access to the models, simulations, and associated data used as inputs for auto-generation of software.

## 1.1 Notes

The term electronic access includes access to the data from NASA facilities.

## 1.2 History

Click here to view the history of this requirement: SWE-206 History

SWE-206 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.8.2 The project manager shall require the software developers and suppliers to provide NASA with electronic access to the models, simulations, and associated data used as inputs for auto-generation of software. |
| Difference between C and D | clarified that this applies to custom software suppliers. |
| D | 3.8.2 The project manager shall require the software developers and custom software suppliers to provide NASA with electronic access to the models, simulations, and associated data used as inputs for auto-generation of software. |

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

NASA requires electronic access to models and simulation data used as input auto-generation of software developed by either suppliers or software developers to facilitate cases where inputs or models may require changes to produce the desired code results.  This access also accommodates the longer-term needs for performing maintenance, assessing operation or system errors, and addressing hardware and software workarounds.

**Requirement 3.8.2** mandates that software developers and custom software suppliers provide NASA with **electronic access** to the models, simulations, and associated data that serve as inputs for auto-generation of software. This requirement ensures transparency, traceability, and accountability in the software development process, particularly for systems relying on auto-generated code. Below is a detailed rationale for this requirement:

---

### **1. Ensuring Traceability**

* **Why?** Auto-generated software introduces an abstraction layer where the source code is derived from input models and data through code generation tools. To validate the correctness, accuracy, and reliability of the generated code, traceability between requirements, models, and outputs must be established.
* **How This Helps**:
  + Providing NASA with access to the models and simulations ensures traceability between the requirements, functional designs, and ultimately, the generated code.
  + Access allows NASA to verify that the inputs (e.g., models, configurations, scripts) align with project requirements and safety standards.
* **Example**: In a flight control system, access to the input models ensures the outputs are traceable to the initial system design and requirements, enabling verification that the generated code meets performance and reliability standards.

---

### **2. Supporting Independent Validation and Verification (IV&V)**

* **Why?** NASA employs **Independent Validation and Verification (IV&V)** to identify potential defects, risks, and inconsistencies in software systems. Direct access to the models, simulations, and associated data is critical for IV&V teams to analyze and confirm the correctness of outputs derived via auto-generation tools.
* **How This Helps**:
  + Enables IV&V to evaluate the underlying assumptions, logic, and constraints built into the models, ensuring the auto-generated software is robust and reliable.
  + Supports the identification of systemic errors that may originate from incorrect models or incompatible simulation data.
* **Example**: Access to system behavior models ensures IV&V can detect edge-case issues or subtle dependencies, such as timing mismatches or incomplete boundary conditions, which might not be immediately apparent in the generated source code.

---

### **3. Ensuring Compliance with NASA Standards**

* **Why?** Models and simulations used for auto-generation must comply with NASA’s safety, reliability, and quality standards. Gaining electronic access ensures visibility into whether these inputs adhere to NASA-approved guidelines.
* **How This Helps**:
  + NASA can assess whether the models comply with specific software engineering and assurance standards, such as **NPR 7150.2** and **NASA-STD-8739.8**.
  + Enables audits of supplier processes to confirm adherence to contractual agreements and regulatory requirements.
* **Example**: Ensuring inputs meet defined safety-critical standards for embedded systems such as flight software can prevent systemic errors propagated through auto-generated code.

---

### **4. Preventing Black Box Dependencies**

* **Why?** Without access to the models and data used for auto-generation, NASA risks relying on software outputs that could effectively become a **black box**—outputs that cannot be reproduced, analyzed, or audited independently.
* **How This Helps**:
  + Providing electronic access breaks down black box dependencies, ensuring that NASA has insight into how the software is generated and can reproduce the process as needed.
  + Supports mitigation of risks where the supplier's auto-generation process may have hidden assumptions or errors.
* **Example**: In reusable projects or future missions, NASA can access these models and reuse or adapt them, saving development time rather than starting from scratch.

---

### **5. Facilitating Transparency and Oversight**

* **Why?** Clear visibility into models and associated inputs increases trust and transparency between NASA and its contractors or suppliers. It reinforces the agency’s ability to oversee and audit critical systems, reducing the risk of costly or catastrophic errors.
* **How This Helps**:
  + Enables active oversight of inputs and simulations, reducing risks of errors propagating through the development lifecycle.
  + Builds supplier accountability by requiring them to share critical inputs that NASA can review as part of project deliverables.
* **Example**: During project evaluations or reviews, NASA can confirm supplier-generated inputs accurately reflect project requirements and constraints by directly examining model designs.

---

### **6. Increasing Reproducibility for Future Use**

* **Why?** Software lifecycles often extend beyond the initial project. Gaining access to the inputs ensures that NASA can reproduce auto-generated code even if tools, suppliers, or personnel change during long-term missions or future projects.
* **How This Helps**:
  + Models and simulation data provide a starting point for reproducibility, allowing NASA to regenerate software outputs later if tools or requirements need to be updated.
  + Eliminates risks tied to vendor turnover or discontinued proprietary tools.
* **Example**: In a multi-phase project spanning decades, access to models ensures NASA can regenerate and adapt software code when new system hardware or configurations are introduced.

---

### **7. Diagnosing and Resolving Issues from Inputs**

* **Why?** Errors in auto-generated code often stem from upstream issues in the models, simulations, or input data. NASA needs access to these artifacts to diagnose problems that originate early in the development pipeline.
* **How This Helps**:
  + Direct access to models and simulations saves time during error investigations by enabling root cause analysis.
  + Ensures changes to models or simulations can be immediately reflected in updated auto-generated software.
* **Example**: If a spacecraft's telemetry system has runtime issues due to incorrect logic in the auto-generated code, NASA can examine the model used during code generation to identify the problem and generate fixes.

---

### **8. Mitigating Risks of Proprietary Tool Lock-In**

* **Why?** Suppliers often use proprietary tools to generate code, leaving NASA dependent on these tools for future modifications or updates. Access to models mitigates this risk by reducing dependency on proprietary generation processes.
* **How This Helps**:
  + NASA retains control over the critical artifacts (models/simulations) used to generate the software, allowing alternate approaches if tools or supplier relationships change.
  + Enables migration to NASA-preferred tools for long-term management.
* **Example**: During a transition from one supplier to another, models and associated data provide continuity without needing to duplicate effort or adapt to new generation tools.

---

### **9. Meeting Safety and Reliability Goals**

* **Why?** For safety-critical systems, like flight control software or embedded systems, the integrity of the models and data driving auto-generation directly impacts mission success. Errors or deviations in input models can result in catastrophic outcomes if not detected.
* **How This Helps**:
  + Electronic access ensures that models and simulations meet high-level safety requirements and support rigorous testing for reliability.
  + Reinforces fault tolerance by ensuring generated outputs account for all operational conditions outlined in the models.
* **Example**: Data used to auto-generate software for a spacecraft's descent mechanism must accurately reflect mission safety parameters, ensuring the generated code accounts for environmental extremes or hardware constraints.

---

### **10. Supporting Multi-Organizational Collaboration**

* **Why?** NASA often collaborates across multiple organizations, teams, and suppliers. Providing direct access to inputs helps align work products and ensures consistent interpretation of requirements.
* **How This Helps**:
  + Shared access to models enables better coordination among diverse teams, including developers, assurance teams, and suppliers.
  + Reduces misinterpretations between requirements and generated outputs, improving the efficiency of multi-stage projects.
* **Example**: During a multi-agency space exploration mission, models can be shared among teams to ensure consistent software generation across international contributions.

---

### **Conclusion: Value to NASA**

**This requirement is essential for maintaining traceability, transparency, and control over critical software development processes.** Providing NASA electronic access to models, simulations, and associated data ensures:

1. **Traceable and reproducible software** aligned with project requirements.
2. **Safety-critical validation** for inputs driving generated code.
3. The ability to diagnose, update, and adapt systems well beyond the initial implementation.
4. Flexibility in tool use and supplier transitions, reducing vendor lock-in risks.
5. Enhanced collaboration across organizations and teams.

This access ultimately supports NASA’s goals of developing **reliable**, **safe**, and **traceable software systems** critical to mission success.

# 3. Guidance

## 3.1 Auto-generated Software

Auto-generated software is created by translating system behavior models into software code using a **code generation tool**. While this approach offers benefits such as reducing human error, increasing development consistency, and shortening timelines, it also introduces unique complexities and risks. Projects must carefully document, manage, and validate the approach to ensure the resulting software meets the technical, functional, and safety requirements defined by the system’s objectives.

**Key Consideration:**  
Users must ensure not only that the generated code accurately reflects the model, but also that:

* The **code generator** is properly **configured** and used correctly.
* Any **target environment adaptations** (e.g., platform-specific configurations) are accurate and complete.
* The generated code meets **high-level safety, quality, and reliability** requirements.
* Generated code integrates seamlessly with **legacy code** or manually written code, where applicable.
* Models and code outputs are reproducible, traceable, and maintainable.

### **Importance of Capturing an Approach**

It is essential to document the approach for **auto-generated software** development to:

1. **Mitigate Risks**: Understand and address potential issues that arise from code generation tools, input models, or downstream modifications.
2. **Ensure Consistency**: Define repeatable and well-documented procedures for developing and validating auto-generated code.
3. **Support Verification and Validation (V&V)**: Ensure the process verifies the correctness of both tools and outputs at every stage (refer to **SWE-146** for detailed guidance).
4. **Facilitate Audits and Reviews**: Provide a reference for stakeholders to evaluate compliance with safety-critical and mission-critical requirements.
5. **Prepare for Tool Limitations**: Account for situations where the tool may fail to address edge cases or extraordinary conditions.

The documented approach is typically included in project-level artifacts such as the **Software Development Plan (SDP)**, and related documentation such as:

* **Configuration Management Plans** (to manage models, scripts, and tool versions).
* **Verification and Validation Plans** (to detail how tools and generated outputs will be verified).

### **Core Elements of the Approach to Auto-Generated Software**

The following considerations capture critical aspects of managing auto-generated software and should be included in the engineering approach:

#### **1. Code Generation Tool Validation and Configuration**

**Guidance**:

* Validate all **code generation tools** to ensure they correctly translate models and data into reliable, compliant software.
* Confirm that each version of the tool is functional and certified for use in the project. Follow standard practices such as **SWE-136 - Software Tool Accreditation**, which defines accreditation procedures for software tools.
* Account for updates to the tools or configurations during the project lifecycle, as new versions may introduce regressions or incompatibilities.

**Why It’s Important**:

* Defective or improperly configured generation tools may propagate errors across all auto-generated code, negatively impacting safety-critical systems.

**Documentation**:

* Include validation reports, tool configuration settings, and usage protocols in the project’s software documentation.

#### **2. Configuration Management of Auto-Generation Inputs and Outputs**

**Guidance**:

* Place all **input models**, generation tools, and configurations under configuration control (e.g., design diagrams, initialization scripts, or environment data).
* Treat the inputs as primary artifacts (models, configurations) and the **generated source code** as "disposable" unless manually modified.
* Track associated reference models and validation test cases used to confirm tool performance.

**Why It’s Important**:

* Configuration control ensures that the workflow is reproducible, version-controlled, and traceable over the life of the project, even when revisions are required.

**Documentation**:

* Define a procedure in the **Configuration Management Plan (CMP)** for managing auto-generation artifacts, including inputs, intermediate outputs, and any downstream edits.

#### **3. Definition and Rationale for the Scope of Auto-Generated Software**

**Guidance**:

* Clearly define **where** auto-generation will be used, and document justification for its application. In most projects, not all code will be auto-generated, so understanding and communicating this boundary is vital.
* Base scoping decisions on the system architecture, safety-criticality, expected complexity, and cost-benefit analysis.

**Why It’s Important**:

* Ensures that auto-generation is applied to areas where it provides measurable benefits (e.g., productivity, repeatability) while avoiding risks in areas where manual coding is safer or more practical.

**Documentation**:

* Include this rationale in the **Software Development Plan (SDP)** to communicate scoping decisions to all stakeholders.

#### **4. Verification and Validation of Generated Code**

**Guidance**:

* Treat auto-generated code with the same level of scrutiny as hand-written code. Include the following in the V&V strategy:
  + **Static Analysis**: Ensure code complies with applicable coding standards and safety requirements.
  + **Requirements-Based Testing**: Verify that the generated code fulfills specific software requirements.
  + **Dynamic Testing**: Execute runtime tests for functionality, reliability, and performance.
  + **Failure Scenarios and Edge Case Analysis**: Test for unanticipated inputs or conditions.
* Verify that the generated code operates correctly in the intended environment and satisfies safety-critical requirements.

**Why It’s Important**:

* Since code generators are typically **not qualified**, there is no guarantee that their outputs are error-free. Comprehensive V&V provides assurance that the generated code is suitable for its intended function.

**Documentation**:

* Include test plans, results, and traceability matrices in the **Verification and Validation Plan**.

#### **5. Monitoring Planned vs. Actual Use of Auto-Generated Code**

**Guidance**:

* Track how much of the project’s software is auto-generated compared to the planned scope. Note any deviations to:
  + Monitor project progress and evaluate the need for adjustments.
  + Provide insights for future projects regarding tool utilization and efficiency.

**Why It’s Important**:

* Ensures project teams maintain alignment with the planned use of auto-generation. Allows lessons learned to inform planning and improve future tool applications.

**Documentation**:

* Capture these metrics in periodic project reviews or status reports.

#### **6. Policy for Manual Modifications to Auto-Generated Code**

**Guidance**:

* Create and document policies governing manual edits to generated code. Outline:
  + When manual changes are permitted (e.g., integration with legacy systems).
  + Procedures for documenting, testing, and tracking these changes.
  + How changes will be reconciled with new code generations to avoid lost updates.
* Minimize manual changes to maintain reproducibility.

**Why It’s Important**:

* Manual edits introduce the risk of inconsistencies and make it harder to regenerate code in future cycles. Policies mitigate these risks.

**Documentation**:

* Include policies in the **SDP** and **CMP**, and ensure they are prominently tracked during integration.

#### **7. Supplier and Developer Requirements**

**Guidance**:

* Require suppliers and developers to provide NASA with **electronic access** to all models, simulations, and associated input data facilitating auto-code generation. (See **Requirement 3.8.2**.)

**Why It’s Important**:

* Ensures traceability, reproducibility, and independent validation of the source code and supporting systems. Enables NASA to efficiently manage the codebase over the project lifecycle.

#### **8. Documentation**

The approach to managing auto-generated software should be well-documented and accessible to all relevant project stakeholders in key project documents:

* **Software Development Plan (SDP)**: The primary location for defining the project’s approach to auto-generated software.
* **Configuration Management Plan (CMP)**: Guidance for managing the configuration of tool inputs, outputs, and manually modified portions.
* **Verification and Validation Plan (V&V Plan)**: Strategies for validating generated code and tools.

### **Cross-Referenced Requirements**

* **SWE-146**: Detailed guidance on ensuring auto-generated code is validated and maintained to meet project standards.
* **SWE-136**: Accreditation and validation of software tools used in the auto-generation process.

By capturing, validating, and managing every aspect of auto-generated software, projects can ensure that tools and processes align with NASA’s rigorous safety and quality standards. This structured approach reduces risks, ensures traceability, and enhances project success.

**Generating Code Review Documentation for Auto-Generated Mission-Critical Software**

"Users not only need to be sure that the code implements the model, but also that the code generator is correctly used and configured, that the target adaptations are correct, that the generated code meets high-level safety requirements, that it is integrated with legacy code, and so on."[193](#_tabs-<p></p>)

The approach to auto-generated software is typically captured in project documentation such as the Software Development Plan [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan).  Information can also be captured in project documentation relevant to the topic such as configuration management or verification and validation. See also [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code). 

Suppliers and software developers provide electronic access to models and simulation data used as inputs to auto-generation software.

For recommended practices, considerations, and additional guidance related to auto-generated software, see Topic  [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code)..

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For small projects, the application of Requirement 3.1—managing, validating, and documenting auto-generated software—can be simplified to ensure that sufficient rigor is applied without burdening limited resources. Below is tailored guidance to help small projects effectively meet this requirement while keeping processes lightweight and manageable.

### **Overview of Requirement for Small Projects**

**Requirement 3.1** focuses on ensuring that auto-generated software is reliable, traceable, and aligned with project requirements. Small projects can adopt a streamlined approach to manage and validate the auto-generation process without extensive overhead, emphasizing practicality and resource efficiency.

### **Tailored Guidance for Small Projects**

#### **1. Simplify Planning and Management**

* **What to Do**: Document the approach to auto-generated software in an existing project document, such as the **Software Development Plan (SDP)** or a lightweight alternative (e.g., a short appendix or checklist). Include:
  + Tools used for code generation.
  + Scope definition of which components will leverage auto-generation.
  + Basic validation and configuration management details for the tools and inputs.
* **Why It Works for Small Projects**: Consolidating all auto-generation guidance into a single document reduces administrative effort while maintaining a structured plan for managing auto-generated software.

**Simplified Planning Example**:

"The communication protocol code will be auto-generated using Tool X, version 2.1. Functional testing will validate the code against hardware. Models and tool configurations will be version-controlled in GitLab."

#### **2. Focus on Key Inputs Over Outputs**

* **What to Do**: Concentrate configuration management (CM) efforts on **input models, configurations, and scripts** rather than the auto-generated code itself. Treat auto-generated code as a "disposable artifact" that can always be reproduced.
* **Minimum CM for Small Projects**:
  + Put input models and tool settings (configuration files) under version control.
  + Document the version of the generation tool used and any reference models employed for validation.
* **Why It Works for Small Projects**: By controlling inputs instead of outputs, you reduce overhead while ensuring that any generated code can be reproduced reliably.

**CM Example**:

Only the UML design model (input to the code generator) and the code generation configuration script will be version-controlled. Generated source code will not be stored unless manually modified for integration.

#### **3. Validation of Auto-Generation Tools**

* **What to Do**: Instead of performing extensive validation on the auto-generation tool, leverage:
  + The vendor’s tool documentation and existing certifications, if available.
  + A small set of validation tests specifically focused on your project’s needs.
  + Testing of outputs to confirm the tool’s accuracy for your project.
* **Minimum Validation for Small Projects**:
  + Generate a small sample of code for a basic use case.
  + Verify that the generated code behaves correctly in the defined operational environment.
  + If the project updates the tool version during development, repeat this process.
* **Why It Works for Small Projects**: This targeted validation ensures the tool is appropriate for the project and avoids over-investing in tool validation for smaller scopes.

**Tool Validation Example**:

Validate Tool X with a simple subsystem design, ensuring that the generated code compiles and passes functional tests for basic system operations.

#### **4. Clearly Define the Scope of Auto-Generated Software**

* **What to Do**: Identify which parts of the software will be auto-generated vs. manually developed, and include the reasoning for this scope in the SDP or equivalent documentation. For a small project, this might be limited to:
  + Repetitive code (e.g., low-level device drivers, protocols).
  + Non-safety-critical components.
* **Why It Works for Small Projects**: Narrowing the scope ensures that auto-generation is applied only where it offers a clear benefit, keeping processes simple and focused.

**Scope Example**:

Auto-generated code will be used for data serialization and messaging, as these are well-understood, repetitive components. Critical flight logic will be manually developed.

#### **5. Apply Lightweight Verification and Validation (V&V)**

* **What to Do**: Test auto-generated code just as you would hand-coded software, but focus on lightweight V&V strategies:
  + Perform **requirements-based testing** to ensure generated code meets defined functionality.
  + Use static analysis tools or simple checklists to confirm compliance with coding standards.
  + Perform system simulations to evaluate the generated code’s behavior within the overall software.
* **Why It Works for Small Projects**: A practical V&V process allows teams to ensure the generated code is reliable without requiring the exhaustive testing typically applied to larger systems.

**V&V Example:**

The generated communication code will be validated using functional tests in a hardware-in-the-loop setup.

#### **6. Manage Manual Changes to Auto-Generated Code**

* **What to Do**: Minimize manual changes to auto-generated code wherever possible. If modifications are required:
  + Document why the change is necessary.
  + Use a simple tracking mechanism (e.g., comments in the code) to indicate which parts were changed and their purpose.
  + Ensure the changes are version-controlled and tested.
  + Update the generation model or tool configuration to reflect the manual change in future iterations.
* **Why It Works for Small Projects**: This practice prevents loss of manual changes and reduces risks of inconsistency between iterations while keeping management lightweight.

**Manual Changes Process Example**:

Manually edited sections of the generated code will include comments noting the changes. The edited files will be tracked in Git, and corresponding updates will be made to the UML model.

#### **7. Monitor and Adjust Usage of Auto-Generation**

* **What to Do**: Track how auto-generation is used in the project (e.g., planned vs. actual usage). If actual usage deviates significantly from the plan, document and review the reasons.
* **Why It Works for Small Projects**: Keeping track of usage provides feedback for refining auto-generation processes in future projects.

**Monitoring Example**:

The project initially planned to auto-generate both communication code and a GUI configuration library. However, the team's analysis identified that manually developing the GUI interface would save time. This deviation is documented for lesson-learned purposes.

#### **8. Collaborate with Suppliers (If Applicable)**

* **What to Do**: If suppliers or external teams provide auto-generated code, require them to:
  + Provide models, scripts, and reference configurations used in the generation process (see Requirement 3.8.2 for details).
  + Document the validation performed on the generated code.
* **Why It Works for Small Projects**: This ensures that your project has full traceability and can reproduce or modify generated code later if needed.

**Supplier Collaboration Example**:

Supplier-provided generated code will be accompanied by the UML design model, generation scripts, and a validation report.

#### **9. Avoid Excessive Documentation Overhead**

* **What to Do**: Avoid creating separate or redundant documents for auto-generated software. Fold discussions of auto-generation into existing project documents, such as the SDP, CMP, or V&V Plan.
* **Why It Works for Small Projects**: Consolidating documentation reduces administrative burden while ensuring that all requirements for documenting the approach to auto-generated software are still addressed.

**Documentation Example**:

Fold auto-generation details (e.g., tool configuration, scope of use, and test strategy) into a dedicated section of the SDP.

### **Summary for Small Projects**

For small projects, the guidance for Requirement 3.1 can be simplified into these core principles:

1. **Plan and document lightly** but effectively in existing artifacts (e.g., SDP).
2. Focus on **input artifacts** (models and configurations) for configuration control, and treat outputs as disposable.
3. Validate only what is necessary, using simple tests and leveraging vendor resources for tool validation.
4. Define a **clear and narrow scope** for auto-generation.
5. Apply lightweight V&V to the generated code and test it like you would hand-written code.
6. Minimize and track any **manual changes** to maintain consistency and reproducibility.
7. Ensure **supplier collaboration** to retain access to critical inputs and data.

By applying this tailored guidance, small projects can achieve compliance with Requirement 3.1 while keeping processes efficient and manageable.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-193)

  [Generating Code Review Documentation for Auto-Generated Mission-Critical Software,](https://ti.arc.nasa.gov/publications/606/download/ "Click to open in new window")

  Ewen Denney (SGT NASA Ames), Bernd Fischer, July 2009.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

**NASA Lessons Learned** relevant to Requirement **3.1 Auto-Generated Software**, even though they may not explicitly reference auto-generated software. Many documented issues and failures provide indirect but valuable insights into the risks, challenges, and best practices associated with auto-generated code and its development process. Below are curated **NASA Lessons Learned** that highlight aspects of this requirement, including configuration management, validation and verification, dependence on tools, integration with legacy systems, and software quality.

### **1. Lesson ID: 1281 – OrbView-3 Satellite Power System Failure**

#### **Summary**:

The OrbView-3 experienced mission failure due to software errors stemming from improper tool configurations. While not directly related to auto-generated software, the failure underscores the importance of tool validation, configuration management, and ensuring that the output reliably meets system requirements.

#### **Relevance to Requirement 3.1**:

* Demonstrates the need to **validate the correctness** of code generation tools before use.
* Highlights the risks of improperly configured tools leading to unreliable outputs.

#### **Lesson Learned**:

* Validate code generation tools thoroughly and ensure **tool configurations and inputs** meet system needs before relying on their outputs.
* Include input data used to configure the code generation process in the **configuration management plan**, as it is critical for software reproducibility.

### **2. Lesson ID: 2198 – Loss of Mars Climate Orbiter**

#### **Summary**:

The Mars Climate Orbiter was lost in 1999 due to a **software interface error** caused by an improper conversion between metric and imperial units. While this incident did not involve auto-generated code, it emphasizes the risks of **mismatched assumptions within inputs** and outputs of software systems.

#### **Relevance to Requirement 3.1**:

* Highlights the importance of managing **input models and configuration data** for auto-generation tools to ensure consistency and alignment with requirements.
* Suggests rigorous **validation of generated code** against high-level requirements where tools or models operate with assumptions about units, formats, or other parameters.

#### **Lesson Learned**:

* When using auto-generated software, ensure that the **data driving inputs** and any required transformations used by the generation process are consistent with project parameters such as units, protocols, etc.
* Extensive **testing and review** of generated code interfaces and behaviors should be performed before deployment.

### **3. Lesson ID: 1374 – Mars Exploration Rover Spirit and Opportunity Software Patching Issue**

#### **Summary**:

The Mars Rovers experienced issues during updates to operational software. Part of the problem was caused by manual edits to code that conflicted with the existing configuration. This underscores the risks of **modifying generated code** without appropriate procedures, documentation, and version control.

#### **Relevance to Requirement 3.1**:

* Highlights the need for clear **policies for manual modifications** of auto-generated code to ensure consistency and reproducibility.
* Demonstrates the importance of tracking modifications made to generated code and ensuring they are incorporated into future iterations.

#### **Lesson Learned**:

* Projects relying on auto-generated software must:
  + Document and track **manual changes** to generated source code.
  + Plan for updates to input models or tools to regenerate code without losing manual edits.

### **4. Lesson ID: 0589 – Issues with Software Development in the Ares I-X Program**

#### **Summary**:

During the Ares I-X development, significant defects in software were found. These defects arose due to unvalidated processes and improperly managed dependencies between generated outputs and input data models.

#### **Relevance to Requirement 3.1**:

* Demonstrates the importance of validating **inputs to auto-generation tools**, as errors upstream can propagate into the generated software.
* Highlights the need for comprehensive **configuration management** of input models, scripts, and configuration files necessary for code generation.

#### **Lesson Learned**:

* Establish strong configuration control for models, tools, and input data used in auto-generation.
* Treat inputs as critical artifacts and verify their accuracy prior to generating code.

### **5. Lesson ID: 0732 – Galileo Spacecraft High-Gain Antenna Deployment Failure**

#### **Summary**:

The Galileo spacecraft experienced failure of its high-gain antenna because the software driving expected deployment behavior did not account for complex interactions in the physical environment. Software based on oversimplified models and improper data inputs resulted in mismatch between simulation and reality.

#### **Relevance to Requirement 3.1**:

* Reinforces the need to validate the assumptions behind the **models and simulations** used to drive auto-generation.
* Suggests testing auto-generated software under **real-world conditions** to ensure its reliability beyond what is simulated in the model.

#### **Lesson Learned**:

* Carefully validate the **models and simulations** used in code generation to ensure they align with physical environments, operational constraints, and system dynamics.

### **6. Lesson ID: 0792 – Mars Polar Lander Failure**

#### **Summary**:

The Mars Polar Lander failed due to software prematurely shutting down its descent engines. Part of the failure was attributed to oversights in validating logic used by the descent software. Inputs to the automated processes contained insufficient edge-case testing conditions, contributing to the error.

#### **Relevance to Requirement 3.1**:

* Highlights the importance of testing **edge cases and failure scenarios** in auto-generated code to ensure safe operation under all potential conditions.
* Emphasizes the need for rigorous **requirements-based testing** of auto-generated outputs.

#### **Lesson Learned**:

* Ensure **auto-generated code** is comprehensively validated, especially for safety-critical systems. Include edge-case testing and failure modes explicitly in your validation plans.
* Pay close attention to assumptions embedded within input models or scripts used to drive code generation.

### **7. General IV&V Findings – Auto-Code Generators**

#### **Summary**:

NASA’s **Independent Verification and Validation (IV&V) Facility** has identified recurring issues caused by reliance on auto-generation tools in embedded systems software. Common defects included:

* Improper assumptions in input data/models resulting in flawed outputs.
* Mismatched behavior between generated code and user expectations.
* Lack of validation at the tool, input, and output levels.

#### **Relevance to Requirement 3.1**:

* Reinforces the importance of **validation at every level** of the auto-generation process—tools, inputs, and generated code.
* Suggests prioritizing configuration control and ensuring manual edits to generated outputs follow clear guidance.

#### **Lesson Learned**:

* Projects employing auto-generated software must:
  + Validate tools at the initialization phase.
  + Place input data and models under configuration control.
  + Test all outputs with the same rigor as manually written code.

### **Key Lessons Learned for Small Projects:**

For small projects, the following overarching themes emerge from NASA's Lessons Learned database:

1. Validate **auto-generation tools** and ensure their proper configuration to eliminate upstream defects.
2. Treat **input models** as critical artifacts requiring configuration management and validation, as errors in inputs propagate downstream.
3. Implement clear **policies for manual modifications** to generated code to ensure traceability and reproducibility.
4. Focus on **requirements-based testing** and include real-world conditions, edge cases, and failure modes that the models may not fully account for.
5. Document and manage deviations between **planned and actual usage** of auto-generated code for future lessons learned.

### **Conclusion**

NASA’s Lessons Learned emphasize the importance of validation, configuration management, and robust verification processes in projects leveraging auto-generated software. Applying these lessons to Requirement 3.1 ensures that generated software is reliable, safely integrated with legacy systems, and meets mission standards.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-206 - Auto-Generation Software Inputs**

3.8.2 The project manager shall require the software developers and custom software suppliers to provide NASA with electronic access to the models, simulations, and associated data used as inputs for auto-generation of software.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that NASA, engineering, project, software assurance, and IV&V have electronic access to the models, simulations, and associated data used as inputs for auto-generation of software.

## 7.2 Software Assurance Products

Requirement 3.1, which pertains to the management, validation, and traceability of auto-generated software, involves key software assurance (SA) activities, products, and metrics designed to ensure that auto-generated software meets NASA’s safety, quality, and reliability standards. Below is a detailed overview of software assurance products and metrics specifically relevant to this requirement.

The following software assurance products are developed, reviewed, or tracked to assess adherence to this requirement:

#### **1. Tool Evaluation and Accreditation Report**

* **Description**: A report documenting the validation and accreditation of the code generation tool. This includes verifying the tool's ability to correctly translate models into code and its compliance with project-specific requirements.
* **Purpose**: Mitigates risks associated with using unverified or improperly configured tools.
* **Contents**:
  + Certification status of the tool.
  + Results from tool verification tests (e.g., conformance testing, regression testing).
  + Identification of any tool limitations and mitigation strategies.

#### **2. Inputs Validation Report**

* **Description**: A report documenting the validation of the models, configurations, and input data used in the auto-generation process.
* **Purpose**: Ensures inputs are accurate, complete, and aligned with system requirements.
* **Contents**:
  + Validation of models against system/domain requirements.
  + Consistency checks for inputs (e.g., units, formats, boundary conditions).
  + Traceability between high-level requirements and input models.

#### **3. Configuration Management Records**

* **Description**: A set of records tracking all input models, generation scripts, and tool versions used during the auto-generation process.
* **Purpose**: Supports traceability and reproducibility of software by maintaining strict configuration control of all artifacts related to auto-generation.
* **Contents**:
  + Versions of tools, models, and configuration files.
  + Documentation of all changes to inputs or outputs during the development lifecycle.

#### **4. Verification and Validation (V&V) Plan and Results**

* **Description**: A plan outlining the approach for verifying and validating both the generated code and the auto-generation process itself, paired with test results.
* **Purpose**: Confirms that the generated code is free of defects, satisfies requirements, and fulfills safety-critical constraints.
* **Contents**:
  + Test strategies for validating generated code against functional and performance requirements.
  + Plans for testing edge cases and non-nominal conditions.
  + Results of static analyses, dynamic testing, and system integration testing.

#### **5. Generated Code Review Checklists**

* **Description**: Checklists used during reviews of auto-generated code to ensure compliance with standards and requirements.
* **Purpose**: Tracks the consistency of generated code with software assurance standards, project coding guidelines, and traceability requirements.
* **Contents**:
  + Checklist items for compliance with coding standards.
  + Confirmation of alignment between generated code and input models.
  + Validation of proper integration between auto-generated and manual code.

#### **6. Defect Reports**

* **Description**: A record of all defects identified in the auto-generation process, including in the tools, inputs, generated code, and validation outputs.
* **Purpose**: Documents defects, tracks their resolution, and prevents reoccurrences in future versions or iterations.
* **Contents**:
  + Description of the defect.
  + Impact analysis on subsystems and mission objectives.
  + Actions taken for resolution and follow-up testing results.

#### **7. Traceability Matrices**

* **Description**: Matrices that map requirements to input models, generated code, tests, and validation results.
* **Purpose**: Ensures all requirements are fully implemented in the generated code and tested.
* **Contents**:
  + Links between system/software requirements and input models.
  + Traceability from models to output code and V&V results.

#### **8. Risk Assessment Report**

* **Description**: A document highlighting risks associated with using an auto-generation process and the mitigations implemented to address them.
* **Purpose**: Identifies potential risks (e.g., tool failures, input model inaccuracies, misalignment with requirements) and ensures these risks are actively managed.
* **Contents**:
  + Identified risks related to tools, models, and verification gaps.
  + Risk mitigation strategies and contingency plans.

## 7.3 Metrics

### **Software Assurance Metrics**

The following metrics are relevant to tracking and assessing the performance and quality of auto-generated software. These metrics provide insights into the effectiveness of processes and the quality of the resulting software.

#### **1. Requirements-to-Code Traceability Coverage**

* **Definition**: The percentage of software requirements that have direct, traceable links to both the input models and the generated code.
* **Purpose**: Ensures all requirements are translated into functionality within the generated software.
* **Formula**:  
  [ \text{Coverage} = \frac{\text{Number of Requirements with Traceability to Code}}{\text{Total Number of Requirements}} \times 100 ]
* **Acceptance Criteria**: Near 100% traceability coverage.

#### **2. Generated Code Defect Density**

* **Definition**: The number of defects found in the auto-generated code per thousand source lines of code (KSLOC).
* **Purpose**: Assesses the quality of the generated code and helps gauge the effectiveness of the generation process.
* **Formula**:  
  [ \text{Defect Density} = \frac{\text{Number of Defects}}{\text{Generated KSLOC}} ]
* **Acceptance Criteria**: Varies by project, but critical systems typically aim for fewer than 1 defect per KSLOC.

#### **3. Validation Test Coverage**

* **Definition**: The percentage of validation tests successfully passed by the generated code out of the total planned tests.
* **Purpose**: Indicates the reliability and correctness of the generated software under test conditions.
* **Formula**:  
  [ \text{Validation Test Coverage} = \frac{\text{Number of Passed Tests}}{\text{Total Number of Tests}} \times 100 ]
* **Acceptance Criteria**: >95% for non-critical software; ~99%+ for safety-critical software.

#### **4. Configuration Management Compliance Rate**

* **Definition**: The percentage of project artifacts (e.g., models, tools, code, and scripts) under configuration control.
* **Purpose**: Ensures proper management of the artifacts required for traceability and reproducibility throughout the software lifecycle.
* **Formula**:  
  [ \text{Compliance Rate} = \frac{\text{Number of Controlled Artifacts}}{\text{Total Number of Artifacts}} \times 100 ]
* **Acceptance Criteria**: >98% compliance.

#### **5. Tool Change Impact**

* **Definition**: The number of occurrences where a change in the code generation tool significantly impacts the output.
* **Purpose**: Monitors stability and reliability of code generation tools over time.
* **Formula**: Track as a count and assess trends over time.
* **Acceptance Criteria**: Low occurrence count or minimal impact.

#### **6. Manual Code Modification Percentage**

* **Definition**: The percentage of manually modified code in the auto-generated software.
* **Purpose**: Indicates how much manual intervention is needed, which can affect reproducibility and maintainability.
* **Formula**:  
  [ \text{Manual Code Modification Percentage} = \frac{\text{Manually Modified Code Lines}}{\text{Total Generated Code Lines}} \times 100 ]
* **Acceptance Criteria**: Minimize manual changes, as close to 0% as possible.

#### **7. Tool Validation Defect Rate**

* **Definition**: The number of defects found during the validation of the code generation tool divided by the total tests conducted.
* **Purpose**: Measures the quality of the tool and identifies risk areas in its use.
* **Formula**:  
  [ \text{Defect Rate} = \frac{\text{Tool-Related Defects Found}}{\text{Total Validation Tests Conducted}} \times 100 ]
* **Acceptance Criteria**: <1% tool defect rate.

#### **8. Auto-Generated Code Rework Percentage**

* **Definition**: The percentage of generated code requiring rework due to defects or non-conformance identified during testing.
* **Purpose**: Assesses the reliability and correctness of the generation process.
* **Formula**:  
  [ \text{Rework Percentage} = \frac{\text{Reworked Generated Code Lines}}{\text{Total Generated Code Lines}} \times 100 ]
* **Acceptance Criteria**: ~<5%.

---

### Conclusion

The combination of **software assurance products** (e.g., validation reports, V&V results, defect reports) and **metrics** (e.g., traceability coverage, defect density, and validation test coverage) provides critical insights into the quality and reliability of auto-generated software. Together, these products and metrics ensure that the processes and outcomes associated with auto-generated software meet NASA's stringent safety, reliability, and mission-critical standards.

## 7.4 Guidance

The intent of this requirement is to ensure that NASA software development teams and stakeholders have **direct and electronic access** to all artifacts related to the **auto-generation of software**, including source code, models, simulations, data sets, and supporting materials. This electronic access facilitates effective validation, maintenance, reuse, and troubleshooting while reducing costs and technical risks. Below is an improved and expanded software assurance (SA) framework to help ensure compliance with this requirement.

### **Purpose of Electronic Access to Auto-Generated Software**

1. **Validation**: Access to models, simulations, and associated data ensures **traceability and verification** of auto-generated code against requirements and system expectations.
2. **Post-Delivery Activities**: Electronic availability is crucial for conducting continued **testing, porting, and quality assessment** of as-built software work products.
3. **Maintenance and Support**: Facilitates defect resolution, system error investigation, and upgrades. Having access to original auto-generation inputs reduces the effort and complexity of future changes.
4. **Reuse**: Preserving these artifacts enables **future reuse and adaptation** of software for other NASA projects, particularly cost-effective repurposing of auto-generated components.

### **Software Assurance Roles and Activities**

#### **1. Monitoring Data Availability**

Software assurance personnel must verify that all required auto-generated software products and their associated inputs are available in an **electronic, readily accessible format**. These artifacts must be organized, reproducible, and stored in formats suitable for development, testing, and eventual long-term archival.

**Actions**:

* **Collaborate with teams**: Meet with software development managers to confirm processes for accessing auto-generated software data and artifacts.
* **Evaluate completeness**: Ensure that all relevant items (see "What Needs to Be Accessible") are provided by developers or suppliers in the correct electronic format, including input models, data sets, test scripts, and prototype code.
* **Track accessibility issues**: Document any delays or barriers and escalate unresolved matters to the project manager for resolution.

**Opportunities for Improvement**: Regularly conduct audits to ensure ongoing compliance and represent any gaps or challenges in project progress reviews. Software assurance personnel may recommend centralized repositories or frameworks for easier data access.

#### **2. Ensuring Long-Term Access for Maintenance and Reuse**

Post-delivery, assurance personnel are responsible for confirming that all electronic artifacts remain accessible for **maintenance, defect resolution, and system augmentations**. This also includes ensuring NASA has sufficient rights and licenses to reuse auto-generated software components.

**Actions**:

* **Validate archival practices**: Ensure that all data related to auto-generation (models, simulations, scripts, test results) is archived in NASA-approved systems for long-term storage.
* **Assess maintenance preparedness**: Confirm that teams are equipped to retrieve archived materials for defect repairs, upgrades, or workarounds.
* **Reusability evaluation**: Support assessments of whether components and artifacts can be repurposed on future projects, ensuring adequate documentation accompanies each artifact for ease of reuse.

**Opportunities for Improvement**: Recommend standardized formats and metadata practices to ensure long-term portability and accessibility.

#### **3. Verification and Validation of Auto-Generated Software**

SA personnel must ensure that access to models, simulations, and related data is leveraged to thoroughly verify and validate the auto-generated software. Specifically, they must confirm that:

1. The generated code accurately reflects the input models and system requirements.
2. The testing process sufficiently covers edge cases, safety-critical scenarios, and operational environments.

**Actions**:

* **Traceability checks**: Confirm that every requirement is traceable to input models and corresponding generated code.
* **Tool validation**: Ensure the software tools used for auto-generation are properly accredited and validated (refer to NASA SWE-136 Tool Accreditation).
* **Testing compliance**: Verify the adequacy of test scripts derived from auto-generated software, ensuring they align with system-level test plans.

**Opportunities for Improvement**: Standardize tools and methods for tracking traceability, test coverage, and validation outcomes for auto-generated software components.

#### **4. Coordination with Contracting Officers**

Software assurance personnel should proactively engage with project managers and contracting officers to address any **vendor or supplier-related challenges** accessing electronic data, models, and simulations.

**Actions**:

* **Accessibility audits**: Review the availability of all artifacts specified in the supplier agreement, including input data, generated code, and testing materials.
* **Escalate issues**: Initiate discussion with project managers to resolve access difficulties through direct engagement with suppliers or contractors.

**Opportunities for Improvement**: Encourage alignment of contractual obligations around electronic accessibility during initial supplier negotiations and agreements.

### **What Needs to Be Accessible**

The following types of auto-generation artifacts must be tracked and evaluated for completeness and accessibility by software assurance personnel:

1. **Flight and Ground Software Source Code**

   * Generated code for flight and ground systems.
2. **Models and Simulations**

   * Models and simulations used as inputs for code generation and system design validation.
3. **Prototype Software and Architectures**

   * Source code for prototypes and design-related artifacts.
4. **Data Definitions and Data Sets**

   * Data dictionaries, initialization sets, and other elements required for generation.
5. **Generated Ground Support Products**

   * Ground software deliverables, including utilities and processing tools derived from auto-generation.
6. **Build Data**

   * Artifacts describing the compilation and build processes for auto-generated software.
7. **Test Scripts and Test Data**

   * Scripts and test cases derived from the auto-generated software, including their inputs and expected outputs.

Software assurance personnel must confirm accessibility for all these categories, verifying that each is available in electronic form, accurately documented, and well-organized.

### **Metrics to Monitor Compliance and Effectiveness**

1. **Artifact Accessibility Rate**:  
   Percentage of required auto-generation artifacts confirmed to be available electronically:  
   [ \text{Accessibility Rate} = \frac{\text{Number of Accessible Artifacts}}{\text{Total Required Artifacts}} \times 100 ]

   **Acceptance Criteria**: Near 100% artifact accessibility for successful project delivery and post-delivery support.
2. **Artifacts Traced to Requirements**:  
   Percentage of accessible artifacts linked to system or software requirements:  
   [ \text{Traceability Rate} = \frac{\text{Artifacts Linked to Requirements}}{\text{Total Accessible Artifacts}} \times 100 ]

   **Acceptance Criteria**: >95% traceability coverage.
3. **Maintenance Initiation Time**:  
   Time required to retrieve all necessary artifacts for addressing a defect, performing upgrades, or reusing software.

   **Acceptance Criteria**: Minimal retrieval time (e.g., <24 hours from request).
4. **Supplier Artifact Availability Compliance Rate**:  
   Percentage of required vendor-supplied artifacts successfully delivered and accessible:  
   [ \text{Supplier Compliance Rate} = \frac{\text{Supplier-Delivered Artifacts}}{\text{Total Required Supplier Artifacts}} \times 100 ]

   **Acceptance Criteria**: >98% compliance with supplier obligations.
5. **Reusability Assessment Score**:  
   A qualitative score assessing the adequacy of documentation and metadata for future reuse of auto-generated software and components.

   **Acceptance Criteria**: High score indicating ease of reuse without significant rework (e.g., >8/10).

### **Conclusion**

To facilitate long-term use, maintenance, and validation of auto-generated software, software assurance personnel must ensure that all required models, simulations, source code, data sets, and supporting artifacts are **electronically accessible, organized, and well-documented**. Proactive auditing, coordination, and metrics tracking help ensure compliance and maximize the potential for post-delivery benefits such as reuse, manageable maintenance, and cost efficiency.

(See also, [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) )

(See also, [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access))

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) |

# 8. Objective Evidence

To comply with this requirement, the project manager must ensure that software developers or custom software suppliers provide actionable electronic access to all models, simulations, and associated data used in the auto-generation process. This ensures NASA has full visibility and control over input data that impacts auto-generated software, allowing for traceability, independent validation, and compliance with NASA standards.

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

Below is a detailed breakdown of types of **objective evidence** that can be gathered to demonstrate compliance with this requirement, including examples for each category.

---

### **Objective Evidence Categories**

---

### **1. Contractual Agreements or Statements of Work (SOWs)**

* **Description:** Documentation that explicitly requires software developers and suppliers to provide NASA with the necessary electronic access to models, simulations, and associated data.
* **Examples of Evidence:**
  + Copies of **contract clauses** or terms requiring delivery of auto-generation inputs (e.g., source models, simulations, or data).
  + **Statement of Work (SOW)** documentation mandating NASA's right to access all input artifacts.
  + **Data Rights Agreements** signed by suppliers, specifying NASA's ownership or sharing rights for the models and simulations.
  + Correspondence (e.g., emails, memos) showing that electronic access requirements were communicated to developers/suppliers and acknowledged.

---

### **2. Delivery Records from Software Developers/Suppliers**

* **Description:** Records confirming that software developers or suppliers provided NASA with the required models, simulations, and associated data.
* **Examples of Evidence:**
  + **Delivery Logs:** Logs or records showing when models, simulations, and data were delivered electronically to NASA (e.g., upload timestamps, file transfer confirmations).
  + **File Directories:** Screenshots or listings of received files, including metadata (e.g., file names, versions, dates) for models/simulations.
  + **Documented File Transfers:** Data transfer protocols (e.g., SFTP logs, secure SharePoint uploads, or NASA’s internal file repository uploads) proving delivery.
  + Deliverable Acceptance Signatures: Signed forms confirming NASA’s receipt and acceptance of inputs.

---

### **3. Evidence of Electronic Access for NASA Teams**

* **Description:** Evidence that NASA personnel have direct, electronic access to models, simulations, and associated data (either live access or downloadable repositories).
* **Examples of Evidence:**
  + **Access Credentials:** Records of NASA user accounts with access to developer or supplier repositories storing source models and simulations.
  + **Access Logs:** System logs showing NASA’s access to deliverables in supplier-provided tools or repositories (e.g., model-based design tools, databases).
  + **Shared Repositories:** Screenshots of cloud-based shared drives (e.g., Google Drive, SharePoint, AWS, or GitHub) demonstrating where deliverables are stored and accessed electronically by NASA.
  + **Data Hosting Agreements:** MOUs or contracts specifying that suppliers host data in environments accessible to NASA.

---

### **4. Artifact Details and Metadata**

* **Description:** Documentation of specific details about the models, simulations, and data provided by developers/suppliers, including file descriptions, formats, and traceability to the project requirements.
* **Examples of Evidence:**
  + **Artifact Inventory List:** A complete list of input artifacts (e.g., UML diagrams, finite-state machine models, XML configurations) provided for auto-generation, including:
    - Artifact name.
    - Description/purpose.
    - File size and format (e.g., MATLAB Simulink, SCADE models, or SysML diagrams).
    - Version numbers.
  + **Data Dictionaries:** Documentation providing definitions for any associated data used in simulations or auto-generation (e.g., parameters, constants).
  + **Change Logs:** Logs showing updates or revisions to input artifacts provided to NASA, with version control information.

---

### **5. Verification and Validation (V&V) of Inputs**

* **Description:** Evidence that NASA has independently validated or verified the models, simulations, and data provided, confirming that all required inputs were delivered and can be used for review or analysis purposes.
* **Examples of Evidence:**
  + **Input Validation Reports:** Documentation ensuring that delivered models are complete, accurate, and meet project standards.
  + **Acceptance Test Logs:** Reports showing that electronic files (models, simulations, etc.) were tested and validated by NASA after delivery.
  + **Input Reviews:** Meeting minutes or review reports from technical evaluations of supplier-provided data ensuring completeness and correctness.

---

### **6. Supplier Acknowledgment of Responsibilities**

* **Description:** Evidence citing supplier acknowledgment of their responsibility to provide NASA with access to auto-generation inputs.
* **Examples of Evidence:**
  + **Kickoff Meeting Minutes or Memos:** Records documenting discussions where suppliers acknowledged their responsibility to provide models, simulations, and data to NASA.
  + Email Communication: Correspondence with suppliers confirming agreement (e.g., "We will provide NASA full access to all inputs for auto-generated code.").
  + Supplier Deliverable Tracker: A joint tracker or tool used to monitor deliverables, including supplier-provided models and associated data.

---

### **7. Configuration Management of Inputs Post-Delivery**

* **Description:** Evidence that delivered models, simulations, and associated data have been brought under NASA’s configuration management (CM) and traceability processes for future use or reference.
* **Examples of Evidence:**
  + **Configuration Management Plan (CMP):** Documentation specifying how delivered artifacts are version-controlled, stored, and traced.
  + **Version Histories:** Logs showing version control for supplier-delivered models/data.
  + **CM Tool Records:** Records of models uploaded into NASA CM systems (e.g., IBM DOORS, Git, or SVN repositories) for future reference and updates.

---

### **8. Compliance Reviews and Audit Reports**

* **Description:** Evidence of compliance reviews or audits confirming that suppliers provided the required inputs for auto-generation and that electronic access for NASA was achieved.
* **Examples of Evidence:**
  + **Audit Reports:** Internal or external audits verifying that all required supplier inputs (models, simulations, data) are accessible to NASA electronically.
  + **Compliance Checklists:** Completed checklists showing supplier adherence to providing auto-generation inputs.
  + **Metrics Reports:** Reports summarizing compliance metrics (e.g., percentage of required models delivered, percentage verified).
  + **Waiver Records:** Documented waivers for any delivered inputs that do not fully meet predefined access requirements, with detailed justification.

---

### **9. Auto-Generation Process Descriptions**

* **Description:** Evidence of how the provided models, simulations, and data fit into the overall auto-generation process, ensuring traceability between inputs and outputs.
* **Examples of Evidence:**
  + **Model-to-Code Mapping Documents:** Documents describing how each model or simulation contributes to specific sections of auto-generated software.
  + **Process Flow Diagrams:** Diagrams showing the flow of inputs (models, data) through auto-generation tools and corresponding output contributions.

---

### **Summary Table of Objective Evidence for Requirement 3.8.2**

| **Category** | **Examples of Objective Evidence** |
| --- | --- |
| **Contractual Documentation** | Contracts, SOWs, Data Rights Agreements, Email Correspondence. |
| **Delivery Records** | Delivery Logs, File Directories, Data Transfer Logs, Acceptance Signatures. |
| **Electronic Access Records** | Access Credentials, Logs of Repository Access, Shared Drive Screenshots, Hosting Agreements. |
| **Artifact Details and Metadata** | Artifact Inventory List, Data Dictionaries, Input Metadata, Change Logs. |
| **Input Validation and Review** | Validation Reports, Acceptance Tests, Review Reports, Test Logs. |
| **Supplier Acknowledgment** | Kickoff Meeting Records, Supplier Deliverable Trackers, Email Confirmations. |
| **Configuration Management Records** | CM Plans, Version Control Records, Artifact Repository Logs. |
| **Compliance Reviews and Audits** | Audit Reports, Compliance Checklists, Metrics, Waiver Justifications. |
| **Process Descriptions** | Model-to-Code Mapping Documents, Auto-Generation Process Flow Diagrams. |

---

### **Best Practices for Compliance**

1. **Establish Expectations Early:** Include the requirement for electronic access to all auto-generation inputs in contracts and project documentation.
2. **Centralized Repositories:** Utilize a shared repository (e.g., SharePoint, GitHub, AWS) that suppliers can directly upload to and NASA can easily access.
3. **Regular Deliverable Reviews:** Ensure that delivered models and simulations are reviewed upon receipt and validated for correctness.
4. **Automated Delivery Tracking:** Leverage tracking systems (e.g., SFTP logs, CM tools) to ensure all required models are received and accessible.

Documentation of these practices and evidence ensures compliance with Requirement 3.8.2, while also promoting traceability, transparency, and effective collaboration between NASA and its software suppliers.
