# SWE-146 - Auto-generated Source Code

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695503. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code

SWE-146 - Auto-generated Source Code

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695503)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695503&showCommentArea=true&showComments=true#addcomment)

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

3.8.1 The project manager shall define the approach to the automatic generation of software source code including: 

a. Validation and verification of auto-generation tools.  
b. Configuration management of the auto-generation tools and associated data.  
c. Description of the limits and the allowable scope for the use of the auto-generated software.  
d. Verification and validation of auto-generated source code using the same software standards and processes as hand-generated code.  
e. Monitoring the actual use of auto-generated source code compared to the planned use.  
f. Policies and procedures for making manual changes to auto-generated source code.  
g. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-146 History

SWE-146 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 3.8.1 The project manager shall define the approach to the automatic generation of software source code including:   1. 1. Validation and verification of auto-generation tools.    2. Configuration management of the auto-generations tools and associated data.    3. Identification of the allowable scope for the use of auto-generated software.    4. Verification and validation of auto-generated source code.    5. Monitoring the actual use of auto-generated source code compared to the planned use.    6. Policies and procedures for making manual changes to auto-generated source code.    7. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools. |
| Difference between B and C | In item c, changed "Identification" to "Description".  Also, added requirement to include the limits of the auto-generated software.  In item d., made the requirement more specific by adding "using the same software standards and processes as hand-generated code". |
| C | 3.8.1 The project manager shall define the approach to the automatic generation of software source code including:   1. 1. Validation and verification of auto-generation tools.    2. Configuration management of the auto-generation tools and associated data.    3. Description of the limits and the allowable scope for the use of the auto-generated software.    4. Verification and validation of auto-generated source code using the same software standards and processes as hand-generated code.    5. Monitoring the actual use of auto-generated source code compared to the planned use.    6. Policies and procedures for making manual changes to auto-generated source code.    7. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools. |
| Difference between C and D | No change |
| D | 3.8.1 The project manager shall define the approach to the automatic generation of software source code including:   a. Validation and verification of auto-generation tools. b. Configuration management of the auto-generation tools and associated data. c. Description of the limits and the allowable scope for the use of the auto-generated software. d. Verification and validation of auto-generated source code using the same software standards and processes as hand-generated code. e. Monitoring the actual use of auto-generated source code compared to the planned use. f. Policies and procedures for making manual changes to auto-generated source code. g. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |

# 2. Rationale

Defining the approach to be used for the automatic generation of software source code allows projects to review and verify their plans for the use and management of auto-generated software before implementation to ensure the development approach and the resulting software will meet the expectations and goals of the project without introducing unacceptable levels of risk.

The rationale for this requirement is rooted in the growing use of **automatically generated software** to accelerate development, improve consistency, reduce manual coding errors, and meet the demands of complex and safety-critical systems within NASA projects. While auto-generation tools offer significant advantages, improper use or insufficient oversight poses risks, particularly in safety-critical systems. Addressing these risks with strong processes, policies, and tools validation ensures mission success, software reliability, and compliance with standards. Below is a detailed explanation of the rationale for this requirement:

## 2.1 Ensuring Safety and Integrity of Critical Systems

* Auto-generated code is often used in **safety-critical systems**, such as spacecraft systems, launch vehicle controllers, and flight software. These systems require rigorous validation to ensure that even small errors do not result in catastrophic mission failures or life-threatening situations.
* Without proper safeguards, errors can propagate through auto-generation tools and compromise safety-critical operations.
* **Rationale**: Defining an approach to validating, managing, and monitoring auto-generated code ensures the software meets safety-critical requirements and reduces risks of unseen defects.

## 2.2 Preventing Propagation of Errors from Misconfigured Tools

* Auto-generation tools rely heavily on proper configuration and accurate input data. Misconfigured tools or invalid inputs can result in **systematic errors**, with many instances of incorrect code being produced across a project.
* For example, incorrect assumptions during the tool setup can introduce a defect into multiple parts of the software, magnifying potential risks.
* **Rationale**: Verifying and validating auto-generation tools (and their configurations) reduces the risk of systematic errors cascading into the final software systems.

## 2.3 Equal Standards for Auto-Generated and Hand-Coded Software

* Auto-generated code and hand-written code may both contribute to mission-critical functionality. Applying different or weaker standards to auto-generated code could create vulnerabilities, reducing reliability and trustworthiness.
* **Rationale**: Ensuring that auto-generated code is verified and validated with **the same standards and processes as hand-generated code** promotes consistency and ensures compliance with NASA’s software engineering and assurance standards (e.g., NPR 7150.2, NASA-STD-8739.8).

## 2.4 Configuration Management Across the Software Lifecycle

* Auto-generation tools produce outputs based on specific inputs (e.g., requirements models, design specifications). Improper configuration management for inputs, tools, outputs, or edits made to auto-generated code can result in misalignment, untracked changes, or defects that escape detection.
* **Rationale**: Applying robust configuration management ensures traceability, accountability, and repeatability for auto-generated code, mitigating risks of untracked changes or unintended consequences.

## 2.5 Establishing Limits and Scope for Auto-Generated Software

* Auto-generation tools are highly effective for specific functionalities (e.g., embedded systems, repetitive logic, or simple algorithms) but may not be suitable for complex, non-standard, or highly adaptive aspects of a system. Over-reliance on auto-generation without defining limits can introduce risks where human intervention is necessary.
* **Rationale**: Defining the allowable scope and limits of auto-generated software ensures that the tools are applied appropriately and effectively, reducing the risk of misuse and mismatches in critical areas of functionality.

## 2.6 Addressing Risks of Manual Changes to Auto-Generated Code

* Manual edits to auto-generated code can inadvertently create **new errors** or inconsistencies, especially when they bypass validation and verification processes. Such changes create a disconnect between the auto-generation tool's intended outputs and source code integrity.
* **Rationale**: Establishing policies for managing manual modifications to auto-generated code ensures that changes are controlled, tracked, tested, and aligned with system requirements.

## 2.7 Monitoring Planned vs. Actual Tool Usage

* Auto-generation tools are often integrated into specific phases of the software lifecycle. Without monitoring tool usage, discrepancies between planned and actual tool use can result in gaps where manual coding is improperly introduced or tools are applied in unintended ways.
* **Rationale**: Monitoring helps ensure tools are used as designed and any deviations are documented, evaluated, and risk-mitigated.

## 2.8 Improving Efficiency and Reducing Human Errors

* Auto-generation tools reduce the risk of human errors in repetitive or highly structured tasks, such as generating low-level code (e.g., communication protocols, state machines). However, if not adequately monitored or validated, defects may arise stemming from tool inaccuracies rather than human coding mistakes.
* **Rationale**: Validating auto-generation tools and their output improves efficiency while reducing both tool- and human-related errors.

## 2.9 Lessons Learned from NASA's History

NASA's lessons learned provide several examples of the risks associated with **automated processes in software development**:

* **Mars Climate Orbiter Loss (1999)**: Software failures resulted from undetected mismatches in unit conversions. While this was not an auto-generation issue, it underscores the importance of rigorous validation for tools and processes.
* **Ariane 5 Flight 501 Failure (1996)**: A failure in auto-generated flight control software led to the destruction of the launch vehicle, highlighting the risks of systematic errors in tool-generated code.
* **Lesson Learned**: Proper planning, validation, and monitoring of auto-generation tools prevent systematic errors in software systems.

## 2.10 Supporting Model-Based Engineering (MBE) and Automation Trends

* Advances in **Model-Based Engineering** and software automation increasingly rely on auto-generation tools as part of the workflow. These tools generate source code directly from software models (e.g., Simulink, MATLAB) or design specifications.
* While automation trends can improve development speed and consistency, they also introduce risks if the tools or generated outputs are not rigorously verified.
* **Rationale**: Implementing validation, scope, policies, and configuration management ensures that auto-generation tools align with NASA’s goals for leveraging automation while maintaining safety and reliability.

## 2.11 Breakdown by Requirement Subpoint

#### **a. Validation and Verification of Auto-Generation Tools**

* Prevents systematic errors from faulty tools and ensures tool outputs meet reliability standards.

#### **b. Configuration Management of Tools and Associated Data**

* Ensures traceability and repeatability of tool inputs, configurations, and generated code.

#### **c. Description of Limits and Allowable Scope**

* Defines appropriate use cases for auto-generation tools to avoid misuse or misapplication.

#### **d. Verification of Auto-Generated Code Using Standards**

* Ensures auto-generated code meets the same safety and quality standards as manually written code.

#### **e. Monitoring Planned vs. Actual Tool Usage**

* Provides oversight to ensure adherence to planned tool use and identifies any deviations.

#### **f. Policies for Manual Changes**

* Prevents untracked and unvalidated manual edits that can introduce risks or defects into auto-generated code.

#### **g. Configuration Management of Inputs, Outputs, and Modifications**

* Ensures full traceability and eliminates risks related to untracked changes across the software lifecycle.

## 2.12 Key Takeaways

The rationale for this requirement ensures that auto-generation tools are used responsibly and their outputs are rigorously validated and controlled. By planning and implementing robust practices for validation, scope definition, usage monitoring, configuration management, and manual edits, NASA can:

1. **Maximize efficiencies** while minimizing risks associated with software automation.
2. **Maintain high safety and reliability standards** for mission-critical software.
3. **Preemptively mitigate risks—systematic, human, and tool-related—** introduced by auto-generation processes.

These processes collectively safeguard the integrity of software systems, balancing the benefits of automation with rigorous oversight and control mechanisms.

# 3. Guidance

## 3.1 Auto-Generated Software

**Auto-generated software introduces significant efficiencies but also unique risks. An integrated, well-documented approach ensures that auto-generation tools and their outputs meet NASA’s rigorous safety and quality standards. Projects should actively plan, validate, configure, and monitor auto-generation processes to ensure reliable, safe, and traceable integration into the overall software system.**

**Auto-generated software** is created by translating a model of a system’s behavior into software code using a **code generation tool**. While auto-generation can improve development efficiency and reduce human error, it introduces unique challenges that require careful planning, validation, and management.

It is essential to define and document the approach for creating, maintaining, and using auto-generated software, as potential issues with code generation tools or processes can compromise software quality, reliability, and safety. These risks must be actively managed throughout the software lifecycle.

**"Users not only need to ensure that the code implements the model correctly, but also that the code generator is properly configured, the generated code adheres to safety requirements, adaptations for target platforms are correct, and that the generated code integrates effectively with manually developed or legacy software.”**

The project’s approach to managing auto-generated software includes capturing and addressing the following **key elements**:

### 3.1.1. Validation and Verification of Auto-Generation Tools

* **Why it’s necessary**: The functionality of the code generation tools must be verified and validated to ensure they operate correctly and consistently produce reliable software. This is critical because any defects in the tool can propagate systematic errors into the auto-generated code.
* **What to do**:
  + Validate and verify the tools **before use**, especially for each tool version employed during the project lifecycle.
  + Validation should ensure that tools produce software outputs aligned with functional and safety requirements of the system.
  + Use **SWE-136 (Software Tool Accreditation)** for guidance on accrediting software tools.
  + Repeat validation if the tool is updated or reconfigured during the project.
* **Outcome**: Validation builds trust in the tools and ensures that the auto-generation process does not compromise the software’s integrity.

### 3.1.2. Configuration Management of Auto-Generation Tools and Associated Artifacts

* **Why it’s necessary**: Auto-generated code is derived, meaning the critical artifacts to manage are the input models, configuration data, and generation tools. Proper configuration management ensures traceability and reproducibility of code.
* **What to do**:
  + Place the following under strict configuration management:
    - Input models and data driving the tool.
    - The auto-generation tools and their versions.
    - Initialization or tool configuration scripts.
    - Reference models used to validate tool functionality.
  + Avoid managing **generated source code** unless modifications are made (see Point 7). Treat generated code as a "disposable artifact" tied to the inputs and tools.
* **Outcome**: Proper configuration management prevents inconsistencies and ensures every version of auto-generated code can be reproduced accurately.

### 3.1.3. Defining the Allowable Scope for Auto-Generated Code

* **Why it’s necessary**: Auto-generation tools are not suitable for all parts of a system. Defining the limits of what can be auto-generated helps ensure the appropriate, cost-effective, and safe use of these tools.
* **What to do**:
  + **Document the scope of use**, including safety-critical functionality, complexity considerations, and the separation of manually-created code from auto-generated code.
  + Create a rationale for where and why auto-generation is applied, e.g., for repetitive or deterministic components.
  + Consider the feasibility of using auto-generation in high-safety applications by evaluating the cost-benefit tradeoffs.
* **Outcome**: Clear scoping allows the project team to focus on using auto-generation tools where they bring the greatest benefits, while limiting risks in more complex areas.

### 3.1.4. Verification and Validation of Auto-Generated Code

* **Why it’s necessary**: Since most code generators are not qualified, the correctness of their outputs cannot be taken for granted. Auto-generated software must be verified and validated just like manually-written code.
* **What to do**:
  + Use the same **standards and processes** (e.g., simulation testing, functional testing, static analysis) to validate auto-generated code as applied to manually-written code.
  + Ensure thorough testing, including compliance with high-level functional and safety requirements.
  + Apply guidance from **SWE-027 (Use of Commercial, Government, and Legacy Software)** for validation approaches.
* **Outcome**: The generated code is reliable and conforms to all project requirements, even without tool qualification.

### 3.1.5. Monitoring Planned vs. Actual Use of Auto-Generated Code

* **Why it’s necessary**: Discrepancies between planned and actual use of auto-generation tools can introduce unforeseen risks and misalign resources.
* **What to do**:
  + Record and monitor deviations between planned vs. actual use of auto-generated code.
  + Use this data to assess adherence to development plans and improve future estimation and planning.
* **Outcome**: Maintaining alignment between planned and actual usage ensures the project adheres to its scope, reduces risks, and allows for better planning in future iterations.

### 3.1.6. Policies for Manual Changes to Auto-Generated Code

* **Why it’s necessary**: Manual changes to auto-generated code can create inconsistencies and complicate re-generation of the code. Policies are needed to control and track these changes.
* **What to do**:
  + Establish clear policies for when and how manual modifications to auto-generated code are permitted (e.g., to allow integration with legacy software).
  + Require changes to be tracked in the configuration management system and ensure changes are reflected in the model for future generations.
  + Avoid manual modifications unless absolutely necessary.
* **Outcome**: Procedures for manual edits reduce the risk of lost changes while allowing flexibility when required.

### 3.1.7. Configuration Management of Inputs, Outputs, and Modifications

* **Why it’s necessary**: Full traceability of all inputs, outputs, and intermediate modifications ensures reproducibility and adherence to defined software processes.
* **What to do**: Place the following under configuration control:
  + Input models and configurations.
  + Generated source code outputs, where applicable.
  + Any modifications made to outputs, especially manually-updated code.
  + Set clear policies for managing maturity levels of input models and ensuring generated code meets assigned control levels.
* **Outcome**: Complete configuration management reduces the risk of discrepancies and ensures consistency across the software lifecycle.

### 3.1.8. Documenting the Approach

* **Why it’s necessary**: Capturing all aspects of the auto-generation process ensures consistency and serves as a reference for all stakeholders.
* **What to do**: Include the approach to auto-generation in documents such as:
  + The **Software Development Plan (SDP)**.
  + Configuration management plans detailing tool control.
  + Verification and validation documentation for auto-generated code.
* **Outcome**: A defined process ensures that all team members are aligned and provides long-term traceability for the entire approach.

**Generating Code Review Documentation for Auto-Generated Mission-Critical Software**

“Users not only need to be sure that the code implements the model, but also that the code generator is correctly used and configured, that the target adaptations are correct, that the generated code meets high-level safety requirements, that it is integrated with legacy code, and so on."[193](#_tabs-<p></p>)

When capturing their approach for the creation, maintenance, and use of auto-generated software, the project captures key elements including:

* **Validation and verification of auto-generation tools** - The correct operation of the functionality of the tools used to automatically generate code is to be confirmed before those tools are used.  Tools that do not function correctly only serve to reduce confidence in the quality and functionality of the resulting software source code.  It is important to validate and verify every version of the tools used on the project, especially if updates to the tools are made during the project life cycle (see [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) for recommended approaches).

* **Configuration management of auto-generation tools and associated data** - Typically, the software source code is configuration managed, but auto-generated software needs to have its input model and generation tools configuration managed [133](#_tabs-<p></p>).  The code which is entirely generated is a disposable good - the important artifacts are the models.  Any reference models used for confirming the correct functionality of the tool are also recommended for configuration control as are initialization scripts, tool configuration scripts, and any other data needed to run the tool.

* **Identification of the allowable scope for the use of auto-generated** **software** - All of the software in the project is unlikely to be auto-generated software source code; therefore, the scope of the use of auto-generated code should be identified, documented (with rationale), and made available to the project team. Scoping could be established based on safety-criticality, complexity, the ability to segment the auto-generated code from manually-generated code, as well as cost-benefit analyses of auto-generated source code versus manually-developed source code.

* **Verification and validation of auto-generated source code** - Auto-generated software is required to be verified and validated to the level required to ensure its fitness for use in the intended application (See [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) for recommended approaches.).   “Since code generators are typically not qualified, there is no guarantee that their output is correct, and consequently auto-generated code still needs to be fully tested and certified.” [193](#_tabs-<p></p>)

* **Monitoring the extent of use of auto-generated source code compared to the planned use** – Capture the delta between the project’s planned and actual use of auto-generated code as one way to ensure the scope of the auto-generated code is maintained.  This information also allows monitoring of adherence to software development plans and improvement in future estimations of the use of auto-generated source code.

* **Policies and procedures for making manual changes to auto-generated source code** - Typically, auto-generated source code is not modified; it is important that the code can be regenerated (based on updates to the input model) without concerns of losing manual updates to the generated code.  However, if the project expects to manually modify the auto-generated source code at any stage, perhaps to allow integration with other project software, policies and procedures for how and when that code can be manually updated should be planned, documented, and implemented.  Additionally, procedures for tracking those changes and ensuring they are incorporated into the next iteration of the auto-generated source code need to be documented to reduce the risk of losing those changes.
* **Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of auto-generation tools** - The approach should include the project’s guidance for capturing the input (model), output (generated software source code), any modified intermediate output (e.g., the output from a compiler that is modified and then input to an assembler), and any modified auto-generated software (modified after generation).  Include guidance such as at what level of maturity the model is to be configuration controlled and whether the generated source code has and follows its configuration control guidelines or follows the configuration control guidelines for manually-generated code. Typically, source code that is 100 percent generated is not configuration managed because “derived artifacts are 100% redundant, i.e. they don't contain any non-reproducible information.” [133](#_tabs-<p></p>)

For recommended practices, considerations, and additional guidance related to auto-generated software, see Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code)[.](/spaces/SWEHBVC/pages/73106390/8.11+-+Auto-Generated+Code) See also [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs),

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For small projects, the key is to approach **auto-generated software** with simplicity, practicality, and proportional rigor. By focusing validation efforts on tools, maintaining effective configuration management, and applying uniform testing standards to auto-generated code alongside hand-written code, small teams can maximize the benefits of auto-generation while keeping processes manageable and lightweight. Scale processes appropriately to match the complexity and safety-criticality of the software being developed.

For small projects, this requirement —defining an approach to the automatic generation of software source code—can be scaled to suit the size, complexity, and resources of the project while still preserving the integrity of the auto-generation process. Small projects should emphasize efficient and focused implementation of this requirement to ensure reliability without overburdening the project with unnecessary overhead. Here's tailored guidance for a small project:

### 4.1 Start Simple: Scope and Planning

Small projects often have limited resources, so defining a clear scope and plan for auto-generated software is crucial:

* **Define Scope**: Identify which parts of the software can benefit from auto-generation (e.g., repetitive logic, basic control algorithms, or hardware interface code). Avoid using auto-generation tools for highly complex or safety-critical parts unless absolutely necessary.
  + **Example**: Use auto-generation for non-critical portions, such as embedded communication protocols, while keeping core logic hand-coded.
* **Document the Plan**: Define the allowable scope, tools to be used, and any manual modification policies. Document this plan briefly in the **Software Development Plan (SDP)** or a similar lightweight project artifact.

### 4.2 Validate Auto-Generation Tools Cost-Effectively

Validation and verification of the code-generation tools do not need to be as rigorous in small projects, but it must confirm basic functionality:

* **Tool Selection**: Choose a well-established and commercially or open-source validated tool for auto-generation (e.g., tools like Simulink or MATLAB code generators). These tools typically have widespread industry use and come with built-in validations.
* **Basic Validation**:
  + Test the tool with a simple prototype by generating code based on controlled inputs and verifying those outputs against expected behavior.
  + If possible, leverage pre-existing validation results from the tool vendor or other users to avoid unnecessary duplication of effort.
* **Avoid Overhead**: Focus tool validation on functionalities directly relevant to your project.

### 4.3 Configuration Management for Key Inputs

Small projects typically have simple structures and workflows, so configuration management can be streamlined:

* **Focus on Inputs**: Configuration-manage the **input models or artifacts** (e.g., system designs, requirements, or model files) used to drive the auto-generation tool, as these are the most critical elements for reproducibility. Store these in a simple version control system (e.g., Git) that the entire team can access.
  + **Example**: If using a model-based design tool, ensure the model version and associated configuration files are tracked and labeled appropriately.
* **Generated Code**: Treat the auto-generated code as "disposable" and **do not configuration manage it unless manual changes are made**. Instead, document reproducibility (e.g., "Code is generated from Model v2.3 using Tool XYZ version 1.5").

### 4.4 Test Auto-Generated Code Like Hand-Written Code

Even for a small project, verify and validate auto-generated code using the same testing and quality processes applied to hand-written code:

* **Test Inputs and Outputs**: Ensure that the code generation tool correctly translates the input model into source code by comparing the generated code’s behavior to the system requirements.
* **Simplify Testing**: Use automated testing where possible to streamline verification of generated code. For instance:
  + If the auto-generated code controls embedded hardware, test it on the hardware using simulation tools or hardware-in-the-loop testing.
  + Use simple unit tests for the generated code to confirm correctness for smaller code blocks.
* **Safety Considerations**: If the generated code is safety-critical, prioritize tests that address failure conditions, inputs outside expected ranges, and error handling.

### 4.5 Policy for Manual Changes

Manual modifications to auto-generated code are often necessary in small projects to handle integration challenges, but they should be minimized and controlled:

* **Establish Manual Change Rules**:
  + Document precisely when and why manual changes are allowed (e.g., integrating with legacy or hand-written code).
  + Require all manual changes to auto-generated code to be tracked and documented in the project repository, along with the rationale.
* **Regeneration Strategy**: If manual changes are made, include procedures for updating the input model to include the changes so subsequent code generations capture them.

### 4.6 Monitor and Keep It Lightweight

Monitoring the actual use of auto-generated code versus planned use does not need to be elaborate for small projects:

* **Simple Tracking**: Keep an ongoing log (e.g., as part of progress reports) of where auto-generated code is used in the project and whether its use aligns with the plan.
* **Feedback for Improvement**:
  + Evaluate whether auto-generation saved time, reduced errors, or created challenges. Use this information for improving future project estimates.

### 4.7 Scale Configuration Management Based on Complexity

Small projects do not require extensive detailed configuration management workflows:

* **Control Key Elements**: Focus CM efforts on key inputs like models, initialization scripts, and tool configurations.
* **Minimal Outputs Management**: If generated code is modified manually, ensure those changes are under CM tracking (e.g., using a simple file versioning system or tagging modified portions in the repository).
* **Reproducibility**: Clearly document how to regenerate the software if needed (e.g., include exact tool version details and input dependencies).

### 4.8 Keep Documentation Practical

Small projects should avoid excessive documentation overhead:

* **Use Existing Documents**: Integrate auto-generation practices into already planned documents like the SDP, or create a brief appendix or standalone section for capturing these practices.
* **Key Information to Include**:
  + Scope and tools for auto-generation.
  + Validation and testing approach for generated code.
  + Conditions and policies for manual modifications.
  + Configuration management strategy for models, tools, and outputs.

Example Workflow for a Small Project

1. **Scope Definition**:
   * "We will auto-generate code for the embedded communication protocol using Tool ABC, version 2.1. Critical logic will be written manually due to its complexity."
2. **Tool Validation**:
   * "Tool ABC has been validated with sample inputs and outputs; vendor documentation confirms its use for our application."
3. **Configuration Managed Items**:
   * Input model files (stored in Git, version-controlled).
   * Generation tool version and initialization settings.
4. **Verification and Testing**:
   * Unit tests for generated code functionality.
   * Hardware-in-the-loop for testing integration with embedded hardware.
5. **Manual Changes**:
   * "Manual edits limited to integrating generated code with legacy software. Changes tracked in Git with comments connecting modifications to their origin."
6. **Monitoring**:
   * Track the percentage of total project code created via auto-generation and deviations from initial planning. Adjust scope accordingly.

### Key Benefits for Small Projects

1. **Efficiency**: Streamlined validation and testing for auto-generated code save time compared to full-scale hand-written coding efforts.
2. **Simplicity**: Focus configuration management and tracking only on inputs and models while minimizing documentation complexity.
3. **Safety**: Ensures that even small-scale auto-generation processes meet reliability and safety requirements without introducing excessive overhead.
4. **Flexibility**: Small projects gain the flexibility to prioritize critical functions while leveraging automation for simpler, repeatable tasks.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-133)

  [Best Practices for Model-Driven Software Development,](https://www.infoq.com/articles/model-driven-dev-best-practices "Click to open in new window")

  Sven Efftinge, Peter Friese, Jan Köenlein, June 2008.
* (SWEREF-193)

  [Generating Code Review Documentation for Auto-Generated Mission-Critical Software,](https://ti.arc.nasa.gov/publications/606/download/ "Click to open in new window")

  Ewen Denney (SGT NASA Ames), Bernd Fischer, July 2009.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-369)

  [Automatic Code Generation for Instrument Flight Software,](https://trs.jpl.nasa.gov/bitstream/handle/2014/41374/07-4374.pdf?sequence=1&isAllowed=y "Click to open in new window")

  Wagstaff, K., Benowitz, E. Byrne, D.J., Peters, K., Watney, G. (2008), NASA Jet Propulsion Lab (JPL). https://trs.jpl.nasa.gov/handle/2014/41374
* (SWEREF-465)

  [A Verification-Driven Approach to Traceability and Documentation for Auto-Generated Mathematical Software,](http://ti.arc.nasa.gov/publications/623/download "Click to open in new window")

  Ewen Denney, Bernd Fischer, November 2009, accessed on April 21, 2014.
* (SWEREF-533)

  [Computer Software/Configuration Control/Verification and Validation (V&V)](https://llis.nasa.gov/lesson/1023 "Click to open in new window")

  Public Lessons Learned Entry: 1023.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA has documented past challenges and failures associated with software engineering practices, including lessons learned that directly or indirectly highlight the risks and opportunities presented by **auto-generated software**. These lessons emphasize aspects such as tool validation, configuration management, scope definition, manual code modifications, and testing standards—all critical components of Requirement 3.8.1. Below are relevant **NASA lessons learned** that align with this requirement:

### **1. Lesson ID: 2198 – Loss of Mars Climate Orbiter Due to Software Interface Error**

**Summary**:  
The Mars Climate Orbiter was lost in 1999 due to software interface errors caused by a unit mismatch (imperial vs. metric). This failure resulted in the spacecraft deviating from the planned trajectory and being destroyed upon atmospheric entry. While not directly about auto-generated software, the failure illustrates risks associated with **tools, interfaces, and inadequate validation of generated outputs**.

**Relevance to 3.8.1**:

* Highlights the importance of **validation of auto-generation tools** and their outputs to ensure consistency with project requirements (e.g., units, data formats, and safety-critical parameters).
* Emphasizes that generated outputs (including software from tools or models) must meet the same validation and verification standards as hand-coded software.

**Lesson Learned**:

* Auto-generated code, especially for interfaces or embedded systems, must be rigorously tested against requirements, including interface compatibility (e.g., unit conversions, communication protocols).

### **2. Lesson ID: 0732 – Galileo Spacecraft High-Gain Antenna Deployment Failure**

**Summary**:  
The Galileo spacecraft experienced a failure of its high-gain antenna due to unanticipated mechanical interactions. While this incident was primarily mechanical, contributing software controls were sourced from inconsistent inputs and generated outputs that failed to reflect the actual deployment environment.

**Relevance to 3.8.1**:

* Demonstrates the importance of **configuration management** for all inputs and outputs used in auto-generation tools.
* Shows that even "derived outputs," such as auto-generated software, must account for unplanned edge-case conditions.

**Lesson Learned**:

* Configuration management must include **input models** to generation tools, particularly when simulations or models are used to drive safety-critical software components.

### **3. Lesson ID: 1374 – Faulty Software Implementation in the Spirit and Opportunity Rovers**

**Summary**:  
The Mars Exploration Rover mission encountered issues when updating and patching operational software. The problem originated from manual modifications to pre-existing (generated and hand-written) software that were not adequately tracked or tested. These issues created faults during mission operations and caused temporary loss of functionality for one of the rovers.

**Relevance to 3.8.1**:

* Highlights the **risks of manual edits** to auto-generated code without proper configuration control and validation.
* Reinforces the need for policies that govern manual edits to auto-generation outputs, including documenting and testing those changes thoroughly.

**Lesson Learned**:

* For **hybrid auto-generated and manually modified code**, establish robust procedures for tracking, testing, and validating manual changes to avoid introducing defects.

### **4. Lesson ID: 1281 – OrbView-3 Satellite Power System Failure**

**Summary**:  
The OrbView-3 experienced a complete mission failure due to software-related issues, including auto-generated code that was improperly validated against mission-critical safety requirements. Issues arose because the generated code was assumed to be "error-free" based on the tool’s design, and no rigorous testing of outputs was conducted.

**Relevance to 3.8.1**:

* Demonstrates the danger of **assuming correctness of auto-generated code**, leading to insufficient verification and validation processes.
* Emphasizes the need to apply **the same safety standards** to auto-generated code as hand-coded software.

**Lesson Learned**:

* Treat all auto-generated code as requiring **full testing and certification** before deployment, especially when safety-critical systems are involved.

### **5. Lesson ID: 0792 – Mars Polar Lander Loss**

**Summary**:  
The Mars Polar Lander failed upon entry into the Martian atmosphere when a software bug caused premature shutdown of descent engines. Part of the flight software had been derived from models and prototype tools, but the generated outputs were insufficiently tested against edge-case conditions.

**Relevance to 3.8.1**:

* Highlights the importance of **monitoring planned vs. actual use of auto-generated code**, especially for edge cases and unanticipated conditions.
* Demonstrates the need for clear limits on where auto-generation tools are applied (e.g., avoid overly complex or high-risk areas without careful validation).

**Lesson Learned**:

* Clearly define the scope and allowable use of auto-generated software, and ensure thorough testing of generated outputs under all operational conditions.

### **6. Lesson ID: 0330 – Mars Climate Orbiter Metric Conversion Error**

**Summary**:  
The Mars Climate Orbiter incident stemmed from the failure to correctly validate spacecraft control software that had been partially auto-generated from prototype tools. Critical errors related to unit mismatch could have been detected with better oversight of tool usage and generated outputs.

**Relevance to 3.8.1**:

* Emphasizes the importance of **monitoring the extent of use of auto-generated code vs. planned use** to detect unexpected issues (e.g., unit mismatches, data precision problems).
* Suggests that validation of the outputs (such as conversion rules) is as crucial as validating the tools themselves.

**Lesson Learned**:

* Ensure that all auto-generated code undergoes robust **data and unit consistency checks**, especially when controlling safety-critical systems.

### **7. General Observation: Independent Verification and Validation (IV&V) Findings on Code Generators**

**Summary**:  
NASA IV&V has identified numerous cases where auto-generation tools led to defects in embedded systems due to unvalidated configurations, mismatches between models and executable code, and untracked manual edits. IV&V recommends comprehensive validation strategies for both tools and outputs to prevent defects from propagating through project lifecycles.

**Relevance to 3.8.1**:

* Reinforces the importance of **validation and verification of auto-generation tools** and outputs.
* Highlights the need for **configuration management** for all inputs, outputs, and intermediate steps in the generation process.

**Lesson Learned**:

* All inputs to auto-generation tools (models, configurations) must be configuration-controlled, and manual edits to generated code should follow strict tracking protocols to allow for reproducibility and error detection.

### **8. Lesson ID: 0589 – Software Defects in the Ares I-X Program**

**Summary**:  
During the Ares I-X program, late discovery of software defects caused significant delays. Some of these defects were found in auto-generated code, which had not been fully verified against high-level mission requirements. The software relied heavily on the accuracy of input models, which were inadequately configuration-managed during early phases of development.

**Relevance to 3.8.1**:

* Demonstrates the need for **policies and procedures** for managing model inputs and ensuring their traceability during code generation.
* Shows that poorly managed generated code can result in mission-critical issues, even for parts derived from seemingly validated tools.

**Lesson Learned**:

* Ensure models driving code generation are **fully configuration-controlled** and traceable to requirements.

### **9.** **Computer Software/Configuration Control/Verification and Validation (V&V). Lesson Number 1023[533](#_tabs-<p></p>):**

The use of the Matrix X auto code generator for ISS software can lead to serious problems if the generated code and Matrix X itself are not subjected to effective configuration control or the products are not subjected to unit-level V&V. These problems can be exacerbated if the code generated by Matrix X is modified by hand.

### **Key Takeaways from NASA Lessons Learned**

1. **Validation of Tools**: Ensure auto-generation tools are rigorously tested and accredited, and never assume correctness of the output.
2. **Configuration Management**: Place key artifacts such as input models, initialization scripts, and tool version configurations under strict control.
3. **Manual Code Changes**: Establish policies for handling modifications to generated code to prevent defects or loss of reproducibility.
4. **Define Scope**: Limit and clearly define the use of auto-generated software, ensuring it is scoped for safe and appropriate functionality.
5. **Verification and Testing**: Treat generated code as needing full testing, including edge cases and failure scenarios, just like hand-written code.
6. **Monitoring Usage**: Actively monitor the actual use of auto-generated code compared to the planned scope.

### **Conclusion**

NASA’s **lessons learned database** provides significant insight into the challenges and risks posed by auto-generated software. Projects must adopt structured processes to validate tools, manage configurations, verify outputs, and define the scope of auto-generated software to ensure safety, reliability, and mission success. These lessons reinforce the importance of implementing Requirement 3.8.1 to prevent similar issues from recurring in future missions.

6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Establish processes early in development](https://software.gsfc.nasa.gov/lesson-details/331/). **Lesson Number 331**: The recommendation states: "Establish development and testing methodology and process early in the lifecycle."

# 7. Software Assurance

**SWE-146 - Auto-generated Source Code**

3.8.1 The project manager shall define the approach to the automatic generation of software source code including:

a. Validation and verification of auto-generation tools.  
b. Configuration management of the auto-generation tools and associated data.  
c. Description of the limits and the allowable scope for the use of the auto-generated software.  
d. Verification and validation of auto-generated source code using the same software standards and processes as hand-generated code.  
e. Monitoring the actual use of auto-generated source code compared to the planned use.  
f. Policies and procedures for making manual changes to auto-generated source code.  
g. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess that the approach for the auto-generation software source code is defined, and the approach satisfies at least the conditions “a” through “g.”

This revised guidance provides clear, concise, and actionable steps for software assurance activities that address Requirement 3.8.1. The goal is to ensure that auto-generated software is thoroughly planned, monitored, verified, and validated to support safety, reliability, and compliance within the scope of NASA’s projects.

This guidance empowers **Software Assurance** to comprehensively evaluate and oversee the creation, maintenance, and use of auto-generated software in NASA projects. By applying these activities and focusing on validation, configuration, scope, and monitoring adjustments, SA contributes to ensuring safe and high-quality mission-critical software outputs.

## 7.2 Software Assurance Products

#### **SA Review of Project Documentation:**

* **Software Engineering Plans Assessment**:

  + Review the project’s documented approach to auto-generated software, which includes an assessment of the elements listed in **Requirement 3.8.1 (a-g)**:
    - Validation and verification of auto-generation tools.
    - Configuration management of the tools, models, and outputs.
    - Rationale for the allowable scope of auto-generated software.
    - Verification and validation plans for auto-generated code.
    - Monitoring of planned vs. actual usage of auto-generation tools.
    - Policies and procedures for manual modifications of auto-generated code.
    - Configuration management for all related inputs and outputs.
  + Identify and document any issues, risks, or gaps related to these elements in the plan.
* **Software Development/Management Plan (SDP)**:

  + Evaluate the inclusion of the auto-generated software approach in the SDP and ensure it is integrated into lifecycle planning.
  + Verify that the plan aligns with NASA standards for software engineering (e.g., NPR 7150.2, NASA-STD-8739.8).
* **Software Configuration Management Plan (SCMP)**:

  + Ensure the SCMP addresses configuration management of auto-generation inputs (e.g., models), tools, outputs, and any generated code modified manually.
  + Verify guidelines determine when auto-generated outputs require configuration control (e.g., when manual edits are made).

## 7.3 Metrics

Tracking software assurance metrics provides insights into the quality and maturity of auto-generated software and helps identify areas for improvement. The following metrics are relevant to this requirement:

#### **Recommended Metric:**

* **Number of Software Work Product Non-Conformances Identified by Life Cycle Phase Over Time**:
  + Track non-conformances specifically associated with auto-generated software, such as tool-related defects, discrepancies between models and outputs, or improper manual modifications.

#### **See Also:**

* Refer to **Topic 8.18 – SA Suggested Metrics** for additional metrics that may be tailored to the characteristics of the project, such as:
  + Defects in generated source code detected during validation.
  + Percentage of auto-generated source code successfully verified on the first attempt.
  + Tool configuration compliance rate.

Metrics should be gathered and analyzed periodically to monitor the effectiveness of the auto-generation process and inform corrective actions.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

Auto-generated software offers advantages in efficiency and consistency, but it also introduces unique risks. Software assurance (SA) activities must ensure that these risks are identified, mitigated, and addressed throughout the development lifecycle. Below is improved guidance for software assurance practitioners:

Auto-generated software is produced by translating system models or inputs into source code using a **code generator tool**. While this process can reduce human error and save time, issues may arise with the quality of the generated software or the tools used, necessitating careful scrutiny:

* **Key Assurance Principle**: “Users must ensure that the generated code implements the model correctly, the code generator is properly configured, and the final code meets high-level requirements for safety, quality, and integration.”

### Software Assurance Activities for Auto-Generated Software

### 7.4.1. Validation and Verification of Auto-Generation Tools:

* **SA Responsibility**:
  + Verify that the project has validated the code generation tools before they are used to ensure the tools produce correct and compliant outputs.
  + Assess validation practices for every version of the tool used during the lifecycle, ensuring updates or changes to the tool are properly re-validated.
* **Focus Areas**:
  + Look for known issues with the tool (e.g., vendor-reported bugs, limitations in supported functionality).
  + Ensure the project uses **SWE-136 (Software Tool Accreditation)** or equivalent processes for validating critical tools.
* **SA Outcome**:
  + Confidence that the code generation tool produces outputs aligned with project requirements.

### 7.4.2. Configuration Management of Auto-Generation Tools and Associated Data:

* **SA Responsibility**:
  + Confirm that the project’s configuration management plan includes all critical artifacts related to auto-generation:
    - Input models (e.g., design files, state diagrams, initialization scripts).
    - Tool configurations and initialization data.
    - Outputs, especially if intermediate modifications or manual edits occur.
  + Evaluate the traceability of models to generated code.
* **Focus Areas**:
  + Review whether configurations are version-controlled to allow reproducibility at any stage.
* **SA Outcome**:
  + Assured traceability and reproducibility of all generated artifacts.

### 7.4.3. Identification of Allowable Scope:

* **SA Responsibility**:
  + Review the rationale for defining which components will be auto-generated (versus hand-coded).
  + Ensure the project limits auto-generation to components where it is effective and safe (e.g., repetitive, deterministic components rather than highly dynamic or critical systems).
* **Focus Areas**:
  + Ensure the defined scope aligns with the project’s safety classification and risk tolerance.
* **SA Outcome**:
  + Clearly defined and justified areas of auto-generation aligned with project requirements.

### 7.4.4. Verification and Validation of Auto-Generated Code:

* **SA Responsibility**:
  + Ensure that the project verifies auto-generated code with the same rigor as hand-written code.
  + Confirm the use of static analysis, dynamic testing, requirements-based testing, and other methods to validate the generated code.
* **Focus Areas**:
  + Assess whether the generated code meets safety, performance, and functional requirements.
* **SA Outcome**:
  + Verified correctness and readiness of auto-generated code for deployment.

### 7.4.5. Monitoring Planned vs. Actual Use of Auto-Generated Code:

* **SA Responsibility**:
  + Check if the project monitors the extent of auto-generation's use versus its planning in the Software Development Plan (SDP).
* **Focus Areas**:
  + Assess discrepancies in coverage and ensure deviations are risk-assessed and documented.
* **SA Outcome**:
  + A clear record of adherence to, or deviation from, planned auto-generation usage.

### 7.4.6. Policies for Manual Changes:

* **SA Responsibility**:
  + Review the project’s policies and procedures for manually modifying auto-generated code.
  + Evaluate how the project tracks and validates manual changes to ensure no conflicts or unintended behavior.
* **Focus Areas**:
  + Ensure manual edits follow documented rationale and are tested and incorporated into tools or models for future code generations.
* **SA Outcome**:
  + Controlled, documented, and validated changes to generated code.

### 7.4.7. Configuration Management of All Inputs and Outputs:

* **SA Responsibility**:
  + Assess whether the project’s configuration management covers the full lifecycle of auto-generated code:
    - Input models and data.
    - Generation tools.
    - Outputs and any modified artifacts.
* **Focus Areas**:
  + Examine the maturity levels at which artifacts transition to configuration control.
* **SA Outcome**:
  + Comprehensive, lifecycle-spanning configuration control of all critical artifacts.

## 7.5 High-Level SA Assurance Goals for Auto-Generated Software:

* Ensure the **generation tools**, processes, and outputs meet NASA’s safety, reliability, and quality standards.
* Provide independent, objective assessments of associated risks, documenting findings and recommendations.
* Promote traceability, reproducibility, and alignment with project requirements for all generated code and associated artifacts.

### 7.5.1 Where to Document SA Processes:

Software assurance processes for auto-generated software should be detailed in:

* Software Assurance Plans.
* Verification and Validation Plans.
* Software Test Reports.

For recommended practices, considerations, and additional guidance related to auto-generated software, see Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code)[.](/spaces/SWEHBVC/pages/73106390/8.11+-+Auto-Generated+Code)

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

To demonstrate compliance with this requirement, **objective evidence** must be collected to validate the project team’s defined approach and implementation of practices for managing auto-generated software source code. Below is a detailed list of specific types of objective evidence that can be provided for each sub-requirement.

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

 By systematically collecting and maintaining these types of objective evidence, the project can demonstrate compliance with Requirement 3.8.1 while ensuring reliable and high-quality auto-generated software.

### **a. Validation and Verification of Auto-Generation Tools**

* **Description:** Evidence ensuring the tools used for auto-generating source code have been validated to meet their intended purpose and verified for proper functionality during the project.
* **Examples of Evidence:**

  1. **Tool Validation Report:** Documentation of the process used to validate the auto-generation tools, showing they meet all requirements for functionality, reliability, and correctness.
  2. **Test Results for Auto-Generation Tools:** Results from test cases verifying that the tools produce accurate, predictable, and repeatable outputs.
  3. **Verification Checklist for Tools:** Records confirming that all tool functionalities were reviewed and verified as working correctly.
  4. **Independent Tool Assessment Report:** Review of the tool by an independent party (e.g., IV&V team or external stakeholders) verifying its appropriateness for use.

### **b. Configuration Management of the Auto-Generation Tools and Associated Data**

* **Description:** Evidence confirming that all auto-generation tools and related data (e.g., input data, configuration files) are under strict configuration management to ensure traceability and version control.
* **Examples of Evidence:**

  1. **Configuration Management Plan (CMP):** Plan outlining the processes for managing versions and changes to auto-generation tools and their data.
  2. **Tool Version Logs:** Records tracking versions of the auto-generation tool used throughout the project.
  3. **Change Requests (CRs):** Documents describing approved changes to tools, input data, or supporting files.
  4. **Tool Repository Access Logs:** Access logs showing tracking of who accessed or modified the tools/data.

### **c. Description of the Limits and Allowable Scope for Auto-Generated Software**

* **Description:** Documentation detailing where and how auto-generated software is used, as well as limitations or constraints for its usage.
* **Examples of Evidence:**

  1. **Scope Document for Auto-Generated Code:** A document outlining the types of code that may be generated (e.g., device drivers, mathematical calculations) and areas where auto-generation is restricted or not appropriate.
  2. **Tool Usage Guidelines:** Documentation describing allowable use cases and criteria for using auto-generated code in the project.
  3. **Decision Memo:** Written rationale for the decision to use auto-generated code in specific parts of the project.
  4. **Risk Analysis:** Assessment of risks associated with using auto-generated code in specific contexts.

### **d. Verification and Validation of Auto-Generated Source Code**

* **Description:** Evidence that auto-generated code has been tested, validated, and verified using the same standards and quality control processes as hand-written code.
* **Examples of Evidence:**

  1. **Test Plans and Procedures for Auto-Generated Code:** Plans detailing how the auto-generated code will be validated (e.g., test cases, test environments, expected results).
  2. **Test Results and Reports:** Evidence that the auto-generated code has passed all required tests, including logic checks, path coverage, and behavioral tests.
  3. **Code Review Records:** Reports from peer or independent reviews of the auto-generated code, showing adherence to software development standards.
  4. **Regression Testing Results:** Confirmation that auto-generated code does not introduce new defects or break existing functionality.

### **e. Monitoring Actual Use vs. Planned Use of Auto-Generated Code**

* **Description:** Evidence documenting whether the actual usage of auto-generated code aligns with the project's planned use and scope.
* **Examples of Evidence:**

  1. **Planned vs. Actual Usage Report:** A report comparing the planned use of auto-generated code (from design documentation or plans) with actual implementation details.
  2. **Scope Change Log:** Records documenting approved deviations from the planned auto-generation scope and justifications for those changes.
  3. **Metrics Report:** Metrics showing the percentage of code that was auto-generated vs. hand-written.
  4. **Usage Analysis Memo:** Documentation from project meetings or reviews highlighting usage trends for auto-generated code.

### **f. Policies and Procedures for Manual Changes to Auto-Generated Code**

* **Description:** Evidence of formal policies and procedures governing situations where auto-generated code is modified manually.
* **Examples of Evidence:**

  1. **Manual Code Change Policy Document:** A formal policy outlining the process for identifying, documenting, approving, and implementing manual changes to auto-generated code.
  2. **Code Modification Logs:** Records documenting every manual change to auto-generated code, including justifications for the changes and the individuals responsible for implementing them.
  3. **Approval Records for Changes:** Sign-off records from the project manager or technical authority for each manual code modification.
  4. **Test Plans for Modified Code:** Evidence that manual changes were subjected to rigorous verification and testing.

### **g. Configuration Management of Input, Output, and Modifications**

* **Description:** Evidence confirming that inputs, outputs, and modifications related to auto-generation tools are systematically controlled within a configuration management process.
* **Examples of Evidence:**

  1. **Configuration Management Plan (CMP):** Plan detailing how input models, configuration files, tool outputs (source code), and modifications are tracked and controlled.
  2. **Version Control Logs:** Auditable logs of input models (e.g., UML diagrams, templates), auto-generated outputs, and any manual changes, with timestamps and justifications for changes.
  3. **Change Request Records:** Approved change requests associated with inputs (e.g., tool specifications), outputs (e.g., code files), or modifications to code.
  4. **Baseline Tracking Reports:** Reports documenting the baselines for inputs, outputs, and modifications within the configuration management system.
  5. **Tool Input and Output Validation Records:** Evidence of validation activities performed on the input data and tool-generated output, ensuring correctness and consistency.

## 8.1 Summary Table of Objective Evidence

| **Sub-Requirement** | **Examples of Objective Evidence** |
| --- | --- |
| **a. Validation and verification of auto-generation tools.** | Tool Validation Report, Test Results, Verification Checklist, Independent Tool Assessment Report. |
| **b. Configuration management of tools and associated data.** | Configuration Management Plan, Tool Version Logs, Change Requests, Repository Access Logs. |
| **c. Description of limits and allowable scope.** | Scope Document, Tool Usage Guidelines, Decision Memo, Risk Analysis. |
| **d. Verification and validation of auto-generated code.** | Test Plans, Test Results, Code Review Records, Regression Testing Results. |
| **e. Monitoring actual vs. planned use of auto-generated code.** | Planned vs. Actual Usage Report, Scope Change Log, Metrics Report, Usage Analysis Memo. |
| **f. Policies for manual changes to auto-generated code.** | Manual Code Change Policy, Code Modification Logs, Approval Records, Test Plans for Modified Code. |
| **g. Configuration management of inputs, outputs, modifications.** | Configuration Management Plan, Version Control Logs, Change Request Records, Baseline Tracking Reports, Validation Records. |

---

## 8.2 Best Practices for Collecting Objective Evidence

1. **Use Centralized Tools:** Utilize configuration management tools (e.g., Git, Subversion, or ClearCase) and project tracking systems for version control and traceability.
2. **Maintain Audit Trails:** Preserve logs and documentation for all aspects of the auto-generation process, ensuring traceability and justification for all changes.
3. **Regular Reviews:** Conduct periodic reviews of auto-generation processes and evidence to verify alignment with defined procedures.
4. **Involve All Stakeholders:** Engage the tool developers, users, and independent reviewers to ensure comprehensive validation and process adherence.
