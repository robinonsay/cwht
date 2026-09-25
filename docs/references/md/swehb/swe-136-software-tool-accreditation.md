# SWE-136 - Software Tool Accreditation

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695495. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation

SWE-136 - Software Tool Accreditation

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695495)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695495&showCommentArea=true&showComments=true#addcomment)

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

4.4.8 The project manager shall validate and accredit the software tool(s) required to develop or maintain software.

## 1.1 Notes

All software development tools contain some number of software defects. Validation and accreditation of the critical software development and maintenance tools ensure that the tools being used during the software development life cycle do not generate or insert errors in the software executable components. Software tool accreditation is the certification that a software tool is acceptable for use for a specific purpose. Accreditation is conferred by the organization best positioned to make the judgment that the software tool in question is acceptable. The likelihood that work products will function properly is enhanced, and the risk of error is reduced if the tools used in the development and maintenance processes have been validated and accredited themselves.

## 1.2 History

Click here to view the history of this requirement: SWE-136 History

SWE-136 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.3.7 The project shall validate and accredit software tool(s) required to develop or maintain software. |
| Difference between A and B | No change |
| B | 4.4.8 The project manager shall validate and accredit software tool(s) required to develop or maintain software. |
| Difference between B and C | No change |
| C | 4.4.8 The project manager shall validate and accredit the software tool(s) required to develop or maintain software. |
| Difference between C and D | No change |
| D | 4.4.8 The project manager shall validate and accredit the software tool(s) required to develop or maintain software. |

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

Software development tools contain software defects.  Commercial software development tools do have software errors.  Validation and accreditation of the critical software development and maintenance tools ensure that the tools being used during the software development life cycle do not generate or insert errors in the software executable components.  This requirement reduces the risk in the software development and maintenance areas of the software life cycle by assessing the tools against defined validation and accreditation criteria.  The likelihood that work products will function properly is enhanced and the risk of error is reduced if the tools used in the development and maintenance processes have been validated and accredited themselves. This is particularly important for flight software (Classes A and B) which must work correctly with its first use if critical mishaps are to be avoided.

The validation and accreditation of software tools are essential practices in software development and maintenance, especially for critical, high-assurance software systems such as those in NASA projects. This requirement ensures that all tools used in the software lifecycle reliably perform their intended functions, do not introduce undetected errors, and support the overall quality, safety, and correctness of the software being developed or maintained.

---

### **Key Rationale for Validating and Accrediting Software Tools**

#### **1. Preventing Errors and Defects Introduced by Tools**

* **Rationale**: Software development and maintenance tools, including compilers, static analysis tools, requirement management tools, and configuration management systems, play a crucial role in creating, managing, and verifying software systems. However, if these tools contain defects, misconfigurations, or compatibility issues, they can introduce errors into the process, resulting in potentially faulty software.
* **Example**: A compiler with a bug in its optimization routine could unintentionally alter critical sections of the software, causing incorrect behavior in the final build despite correctly written source code.
* **Why Validation is Needed**: By validating tools, the project ensures that they function as expected and do not introduce errors or inconsistencies into the software.

---

#### **2. Ensuring Tool Capability Matches Project Requirements**

* **Rationale**: Not all tools are appropriate for every project. Tools must meet the specific needs of the project in terms of functionality, scale, performance, and compatibility. For example, a requirements management tool must support traceability to all stages of the software lifecycle.
* **Example**: An inadequate tool may fail to manage complex configurations, resulting in difficulty replicating builds or verifying changes. A static analysis tool designed for lower-assurance software may not support the code analysis depth required for safety-critical software.
* **Why Accreditation is Needed**: Accreditation ensures that project leadership explicitly approves the suitability of a tool for use in the project, considering project-specific requirements, risks, and constraints.

---

#### **3. Managing Risks in Safety- and Mission-Critical Systems**

* **Rationale**: NASA projects often involve safety-critical or mission-critical software. In such projects, unvalidated or unaccredited tools could compromise software reliability and safety, leading to potential mission failure, loss of hardware, or threats to human life.
* **Example**: Malfunctioning or unvalidated verification tools could generate false positives or false negatives, leading the team to overlook critical defects or expend resources on non-issues.
* **Why Validation is Needed**: Validating tools ensures that they are capable of meeting the high-assurance demands of safety-oriented projects and generating accurate, reliable results.

---

#### **4. Supporting Compliance with Standards and Regulations**

* **Rationale**: Many NASA projects and associated software products are subject to compliance with stringent industry, agency, or program-specific standards (e.g., NASA-STD-8739.8, DO-178C for aviation-related software). Validated tools are often a prerequisite for compliance with these standards, as they help ensure that the resulting software meets safety, quality, and technical requirements.
* **Example**: Certifications like DO-178C for airborne systems demand that software development and verification be performed using tools accredited for their specific roles in the lifecycle to ensure compliance.
* **Why Accreditation is Needed**: Formal accreditation provides evidence of tool compliance with the standards or frameworks relevant to the project.

---

#### **5. Ensuring Tool Interoperability and Integration**

* **Rationale**: Most software projects use multiple tools for development, testing, configuration management, requirements tracing, and deployment. Ensuring interoperability and seamless integration between these tools is crucial for efficiency and to avoid introducing system errors due to tool mismatches or incompatible workflows.
* **Example**: If the version of a modeling tool used to generate code does not match the downstream build tools, regressions may go unnoticed, introducing subtle defects that affect overall software behavior.
* **Why Validation is Needed**: Validating tools confirms that all tools work together as intended and supports the establishment of reliable toolchains for the project.

---

#### **6. Enabling Consistency and Traceability**

* **Rationale**: Consistency in software development processes and artifacts (e.g., source code, version history, analysis reports) depends significantly on reliable tools. Tools must produce consistent, repeatable outputs for given inputs to support accuracy and traceability across the software lifecycle.
* **Example**: A requirements management tool must consistently maintain traceability relationships between system requirements, software requirements, and test cases. An unvalidated tool could corrupt these relationships, undermining traceability.
* **Why Validation is Needed**: By validating tools, the project can ensure that artifacts generated at any point in the lifecycle reflect consistent, repeatable results that support full traceability.

---

#### **7. Safeguarding Against Cybersecurity Threats**

* **Rationale**: Tools used in software development and maintenance may themselves be vulnerable to cybersecurity threats, such as unauthorized access, injection of malicious code, or unintentional propagation of malware. Using unvalidated or outdated tools significantly increases the risk of introducing unintentional vulnerabilities to the product.
* **Example**: A misconfigured or obsolete dependency management tool could download compromised third-party libraries, introducing security vulnerabilities.
* **Why Validation is Needed**: Validation ensures tools are securely configured, patched, and capable of supporting safe supply chain practices in an era of increasing cybersecurity risks.

---

#### **8. Facilitating Early Detection of Deficiencies**

* **Rationale**: Validating tools early in the software lifecycle allows the project team to identify and resolve issues with the tools themselves, reducing the risk of downstream problems, delays, and cost overruns caused by fixing issues late in the lifecycle.
* **Example**: If a code analysis tool produces incomplete results during validation, project management can switch to a more suitable tool before development begins, avoiding rework during testing or deployment.
* **Why Validation is Needed**: Early validation supports proactive risk management, reducing costs and improving schedule efficiency.

---

#### **9. Promoting Confidence in Software Outputs**

* **Rationale**: The use of validated and accredited tools helps improve overall project confidence in the software outputs they produce. Whether it's test reports, source code builds, or verification artifacts, reliable tools produce trustworthy deliverables.
* **Example**: A validated coding standards compliance tool ensures developers can trust that all flagged issues are legitimate while demonstrating compliance to stakeholders.
* **Why Validation is Needed**: When both the tools and their outputs are dependable, stakeholders across the project, including management, reviewers, and customers, have greater confidence in the software product.

---

### **Validation and Accreditation Processes**

Validation and accreditation of tools for software development and maintenance should follow systematic steps:

1. **Tool Selection**: Identify all tools required for development and maintenance and evaluate whether they meet project needs.
2. **Validation**: Test each tool to ensure it operates as intended and produces reliable outputs under expected operating conditions.
   * Verify tool installation and configuration.
   * Test tool outputs for accuracy, consistency, and repeatability.
   * Assess tool behavior under abnormal conditions or edge cases.
3. **Accreditation**: Formally document approval of the tool for use in the project based on validation results.
   * Assess compatibility with standards.
   * Identify risks and establish tool usage guidelines (e.g., what the tool can and cannot do).
4. **Ongoing Monitoring**: Continue to monitor tool performance throughout the project lifecycle, including patching, version updates, and periodic revalidation as necessary.

---

### **Conclusion**

Requirement 4.4.8 ensures that software tools are properly validated and accredited to produce high-assurance software that meets the rigorous demands of NASA missions. By tackling risks such as tool-introduced errors, compatibility issues, security vulnerabilities, and compliance failures, this requirement fundamentally strengthens the software lifecycle. Implementation of this requirement enables reliable development processes, improves stakeholder and mission confidence, and contributes to the success of NASA's high-stakes projects.

# 3. Guidance

This guidance describes the process for selecting, validating, and accrediting software tools for developing and maintaining software. The emphasis is on ensuring that tools are capable, reliable, and suitable for their intended use. Proper validation and accreditation ensure that software tools contribute positively to the development process, do not introduce errors or biases, and comply with the high performance and safety expectations required for NASA projects.

The responsibility for tool validation and accreditation lies with the project manager, and the effort must be supported by technical authorities, software assurance personnel, and the software development team. The following sections expand on the key principles described in the requirement, offering a structured approach to accreditation for a variety of tools and use cases.

---

## 3.1 Validating and Accrediting Tools for Development and Maintenance

#### **What is Validation?**

Validation is the process of ensuring that a software tool performs the intended function without introducing defects into the final product. The goal is to verify that the tool behaves as expected across its intended use cases in the project environment.

* **Validation Process**:
  1. Develop a set of **test cases** representative of the tasks the tool will perform.
  2. Execute test cases using the tool, comparing its outputs to expected results.
  3. Evaluate whether the tool outputs align with established metrics, models, or benchmarks.
  4. Investigate any discrepancies to ensure no hidden biases or errors affect tool performance.
  5. Document evidence of validation, including results, configurations, and context of testing.

Validation is considered successful when the tool demonstrates consistent outputs that meet all requirements under realistic and edge-case scenarios.

---

#### **What is Accreditation?**

Accreditation is the formal certification that a validated software tool is **acceptable for use** to meet a specific project purpose. Accreditation involves assessing the validated tool against specific criteria, such as compliance with project standards, integration with other tools in the development pipeline, and compatibility with the project’s objectives.

* **Accreditation Granting Organization**:
  + For most NASA projects, accreditation is conferred by the entity with the expertise and authority to judge the tool’s suitability. This could be:
    - The project team and software technical authority.
    - NASA-approved external organizations (e.g., NIST, ACM).
    - The contractor or software vendor, if their accreditation process is proven reliable.
  + Accreditation should be clearly documented, recorded in the project’s software development or management plan, and kept under configuration control.

---

## 3.1.1 Why Validation and Accreditation Are Necessary

Proper validation and accreditation ensure:

1. **Confidence in Tools**: Tools used to develop safety-critical or mission-critical systems (e.g., flight software, systems with human interaction) perform reliably and do not introduce stability issues or runtime errors.
2. **Detection of Hidden Defects**: Some issues may only arise under specific use cases or environments, making validation necessary to detect hidden defects early.
3. **Interoperability**: Tools interact with other components, configurations, and libraries in the development environment. Validation ensures these interactions comply with system-level requirements and standards.
4. **Minimization of Risk in New/Novel Environments**: In environments where existing tools were never used together before or where the system context is novel, validation ensures tools can be trusted for their functions without introducing unanticipated risks.
5. **Compliance with Standards**: Validating tools helps ensure compliance with industry-specific or NASA mandates (e.g., coding standards, safety certifications, or system rules).

---

## 3.1.2 Tools Subject to Validation and Accreditation

Tools directly involved in the development, maintenance, and testing of software must be validated. These tools include, but are not limited to:

* **Compilers**: Ensure generated binaries execute correctly, including handling safety-critical timing constraints and interactions with libraries.
* **Code Coverage Tools**: Confirm that these tools measure actual code coverage accurately without missing critical areas.
* **Development Environments**: Verify IDEs or frameworks support the necessary configurations and libraries in the target system.
* **Build Tools**: Validate the correctness of build artifacts produced (e.g., version consistency, integration stability).
* **Code-Generation Tools**: Ensure generated code is valid, free of execution-time defects, and correct for its intended design.
* **Math Libraries and Linked Libraries**: Validate the correctness of linked routines used in performance and mission-critical execution.
* **Debuggers**: Confirm debugging capabilities align with the intricacies of mission-critical processors.
* **Other Specialist Tools** (e.g., static analysis tools for code quality, validation tools for timing constraints).

---

## 3.1.3 Exemptions for Indirect Tools

Certain **indirect tools**, such as bug tracking systems, metric reporting tools, or document generation utilities, typically do not require robust validation or formal accreditation. NASA projects may accept these tools as "validated by use" (e.g., demonstrated reliability through long-term practical application in similar domains).

---

## 3.3 Handling Novel or New Environments

NASA projects frequently develop software in scenarios where tools or environments are untested or novel. Appropriate steps for such settings include:

1. **Evaluate Against a Reference Environment**: Compare tools and outputs to an already validated environment/tools when possible.
2. **Custom Validation Processes**:
   * Build representative use cases and outputs for new tools or tool combinations.
   * Simulate the full development and integration process to identify potential issues.
3. **Accreditation of Integrated Systems**: Tools and environments not only need individual validation but may also require integration-level accreditation to ensure seamless cooperation.

---

## 3.4 Accreditation Process Flow

The accreditation process involves the following formal steps (see Figure 3.1 for details):

1. **Identification of Tools**:
   * Create a comprehensive list of tools used in software development and maintenance.
   * Include their roles, interdependencies, and required functionality.
2. **Evaluation of Existing Accreditation**:
   * Check if the tool has prior accreditation from reliable sources.
   * Confirm that prior accreditation applies to the project requirements, environment, and use case.
3. **Validation of Tools as Required**:
   * For tools lacking accreditation or with new/unproven use cases, develop custom validation plans.
   * Use testing, functional demonstrations, simulations, and analysis methods.
4. **Approval and Documentation**:
   * Capture validation steps, results, and acceptance criteria.
   * Ensure the project’s software technical authority accepts and signs off on accreditation.
   * Document accreditation in relevant plans (e.g., software management plan).
5. **Ongoing Monitoring**:
   * Regularly review tools (e.g., during major upgrades, lifecycle phase transitions).
   * Revalidate tools as necessary.
   * Track accreditation status in the project configuration management system.

---

## 3.5 Key Validation and Accreditation Techniques

The following techniques can be employed (adapted from SWE-055 and other practices):

* Functional demonstrations of typical tool use cases.
* Formal and peer reviews of tool behavior and configurations.
* Simulation of test cases within the environment.
* Reviewing artifacts generated by the tool to verify proper operation.
* Static analysis of the tools and their outputs.
* Repeatable and automated stress testing for verifier consistency.

---

### **Conclusion**

By requiring validation and accreditation of critical software tools, this requirement enhances confidence in the software development process, minimizes risks due to tool-induced errors, and helps achieve compliance with NASA’s high standards. For novel or untested configurations, additional care to verify and accredit tool chains ensures consistent results even under unique mission parameters. Formal processes paired with reviews track the tool accreditation status and adapt to evolving project needs, ensuring development remains efficient, scalable, and reliable.

A caveat exists that for many new NASA projects, previous ensembles of accredited development environments and tools just don’t exist. For these cases, projects must develop acceptable methods to assure their supporting environment is correct.

One suggested flow for identifying, validating, accepting, and accrediting new development tools and environments to be used to develop software work products subject to this requirement is shown in Figure 3.1. While it may seem obvious, it is important to review the current and expected development tools (compilers, debuggers, code generation tools, code-coverage tools, and others planned for use) and the development environments and release procedures, to assure that the complete set is identified, understood and included in the accrediting process.

          **Figure 3.1 – Sample Accreditation Process Flow** 

See [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists)

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

Small projects can reduce validation and accreditation efforts by utilizing tools and environments that have been accredited in prior NASA projects or similar domains. This involves reviewing historical project documentation and established resources to identify tools with proven reliability under comparable conditions.

#### **Steps to Identify and Apply Previously Validated Tools:**

1. **Review Project Reports**:

   * Evaluate past projects within the organization to identify tools and environments that were successfully accredited and used for similar tasks or development contexts.
   * Pay special attention to project reports, lessons learned, and validation documentation that highlight how tools performed in actual software development scenarios.
2. **Access Process Asset Libraries (PALs)**:

   * Utilize **Process Asset Libraries** (PALs) to search for documented processes, tools, and accreditation workflows validated by other projects.
   * PALs typically contain reusable resources such as test protocols, accreditation checklists, peer reviews, and tool evaluation records—tailored or adaptable to new environments.
3. **Review Technology Reports**:

   * Evaluate published technology reports and engineering summaries to identify prior use cases of software tools or configurations that align with the project's technical requirements.
   * Look for credible research, benchmarks, and validation results that demonstrate the effectiveness and maturity of tools.
4. **Compliance and Applicability Checks**:

   * Confirm that the tools meet the current project’s specific requirements, constraints, and system architecture.
   * Assess whether the prior accreditation and validation context sufficiently matches the scope of the new project.
   * For safety-critical or mission-critical applications, ensure that the tools align with updated safety standards, coding guidelines, or system constraints.

---

### **2. Adopting New Tools Inspired by Previous Accreditation Lists**

In cases where exact matches are unavailable, small projects can consider adopting comparable toolchains by benchmarking against previously accredited tools. This allows small projects to gain confidence in new tools by capitalizing on historical acceptance workflows.

#### **Suggested Process for Adopting New but Related Tools**:

1. **Compare Tool Capabilities**:

   * Identify tools used in earlier projects and compare their functionalities, performance, and suitability to newer tools available for the current project.
   * Ensure compatibility with the current development environment.
2. **Adapt Accreditation Procedures**:

   * Small projects can adapt accreditation protocols from previous projects to validate newer tools. For example:
     + Use prior test cases and validation benchmarks where applicable.
     + Adopt accreditation frameworks documented in PALs.
3. **Leverage Expert Recommendations**:

   * Seek input from NASA technical authorities, Center software assurance representatives, or external organizations to recommend replacements for tools previously accredited in older systems.
   * Ensure recommendations are documented during the selection process.

---

### **3. Benefits of Utilizing Previously Accredited Tools**

* **Resource Efficiency**: Reduces the effort required to validate and accredit tools from scratch by leveraging prior experience and documentation.
* **Reduced Risk**: Tools with a proven history in similar environments provide confidence in reliability and performance.
* **Accelerated Development**: Speeds up tool adoption and ensures quicker integration into existing development workflows.

---

### **4. Key Considerations for Small Projects**

While using previously accredited tools provides substantial benefits, small projects must ensure that they align these tools with their specific needs and requirements. Critical considerations include:

1. **Relevance to the Current Project**:

   * Verify that the previously accredited tools address current project-specific requirements (e.g., safety-critical features, interoperability with new processors, or compliance with updated guidelines).
2. **Scope and Scale**:

   * Confirm that the tool(s) can handle the scale of the current project, whether it is smaller or more complex than the original accreditation environment.
3. **Lifetime and Maintenance**:

   * Check whether the tool’s accreditation remains valid across the entire lifecycle of the current project, considering potential updates or new version releases.
4. **Backup Accreditation Plans**:

   * Plan for contingencies if previously accredited tools fail to meet expected performance in the new environment. Small projects should allocate minimal resources for testing or reevaluating the tools.

---

### **5. Case Example Workflow**

#### Example Workflow for Adopting Previously Accredited Tools:

* **Step 1**: Review recent NASA project PALs, focusing on tools accredited for similar development tasks (e.g., compilers, testing environments, build tools).
* **Step 2**: Evaluate the current project's requirements and match them to the accreditation scope of the identified tools. Confirm compatibility.
* **Step 3**: Conduct high-level validation using selected reference test cases from previous projects to ensure suitability in the new environment.
* **Step 4**: Document validation steps in the software management plan and track newly identified discrepancies or limitations under configuration management.
* **Step 5**: Use peer reviews to inspect validation activity results and formally accept the tool for use in the development pipeline.

---

### **6. Additional Documentation to Reference**

* Process Asset Libraries (PAL) Reports:
  + Examples: Accreditation history from similar NASA projects, configuration logs, tool evaluation checklists.
* Technology Research Reports:
  + Documented tool maturity evaluations by NASA and industry organizations (e.g., NIST tools).
* Validation and Accreditation Records:
  + Records from prior projects detailing accepted methods to validate and accredit specific tools.

---

### **Conclusion**

Small projects can streamline development efforts by leveraging previously accredited software tools and environments validated on other projects. By accessing project reports, PALs, and technology records, small teams can identify tools with proven performance histories and adapt their accreditation workflows to meet their unique requirements. By balancing cost-effective reuse with tailored validation practices, small projects can ensure reliability without compromising safety, accuracy, or mission goals.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
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
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following **Lessons Learned** from NASA's history emphasize the importance of validating and accrediting software tools. These lessons show how prior experiences have highlighted the criticality of selecting, validating, and accrediting tools to ensure software quality, reliability, and mission success.

---

### **1. Ensure Validated and Trusted Development Environments**

#### Lesson Learned:

* **Case Title**: Inadequate Validation of Software Development Tools Led to Mission Risks
* **Case Reference**: **LLIS-1623** (*Mars Climate Orbiter Mishap Investigation Board Report, 1999*)
* **Summary**: Inadequate validation and verification of the tools used to develop and test interdependent software systems can lead to catastrophic mission risks. For the Mars Climate Orbiter, conflicting units of measurement were not identified during integration testing, partly because the software tools and associated processes lacked rigorous validation and traceability.
* **Relevance to Requirement**: Software tools must be validated to ensure that they produce outputs that align with expectations, particularly in mission-critical systems. Validation of compilers, testing environments, and configuration tools is essential to avoiding errors that propagate into the final product. This lesson emphasizes the importance of tool validation in detecting subtle errors that tests might otherwise overlook.

---

### **2. Validate All Third-Party or Reused Tools, Libraries, and Code**

#### Lesson Learned:

* **Case Title**: Misuse of Software Library Caused Incorrect Command Interpretation
* **Case Reference**: **LLIS-43201** (*SOHO Mission Software Error, 1998*)
* **Summary**: The Solar and Heliospheric Observatory (SOHO) spacecraft experienced a significant software anomaly after incorrect realignment commands were sent. The issue stemmed from improper interaction between the software and a third-party tool/library used during development. The library was not properly validated for use in the SOHO context, leading to an error that could have been detected during rigorous tool/library accreditation.
* **Relevance to Requirement**: All tools and libraries, whether developed in-house, third-party, or reused, must undergo validation for adequacy in the target environment. Safety and reliability must be verified by validating tools and libraries against specific mission requirements.

---

### **3. Ensure Tool Compatibility with New or Evolving Environments**

#### Lesson Learned:

* **Case Title**: Transition to a New Development Environment Increased Risks
* **Case Reference**: **LLIS-1802** (*X-38 Development Toolchain Integration, 2002*)
* **Summary**: During the development of the X-38 Crew Return Vehicle, integration challenges arose from migrating to a new development toolchain that had not been rigorously validated for use. Incompatibilities between development tools and simulation tools resulted in undetected software flaws until late in the development cycle, causing project delays and increased costs.
* **Relevance to Requirement**: When introducing or integrating new tools (e.g., code generators, simulators), projects must validate that the tools are correctly configured and compatible with other tools in the environment. Early validation and accreditation reduce risks of incompatibilities that can delay development or cause undetected defects.

---

### **4. Avoid Using Tools That Have Not Been Adequately Accredited**

#### Lesson Learned:

* **Case Title**: Incorrect Compiler for Flight Software Caused Launch Failure
* **Case Reference**: **LLIS-2011** (*Ariane 5 Failure, 1996*)
* **Summary**: A critical software failure during the Ariane 5 maiden flight was caused by a design issue embedded in a previously validated system reused without revalidation for the new project. Specifically, the compiler tool was not validated in the new system configuration, and its unchecked behavior resulted in a catastrophic system fault.
* **Relevance to Requirement**: Even when a tool or process has been validated for past missions, it must still undergo validation when applied to new hardware, configurations, or critical environments. Accreditation ensures that reused tools are appropriate for the specific project context.

---

### **5. Accreditation of Tools for Safety and Timing Constraints**

#### Lesson Learned:

* **Case Title**: Timing Constraint Violation in Flight Software
* **Case Reference**: **LLIS-19382** (*Mars Pathfinder Twin Rover Mission, 2000*)
* **Summary**: During the Mars Pathfinder mission, flight software experienced task priority inversion due to a validation gap related to timing constraints. This issue, exacerbated by inadequate tool validation, caused excessive system resets. Although successfully mitigated in-flight, the cost of resolving this defect could have been avoided had proper tool accreditation and validation occurred before deployment.
* **Relevance to Requirement**: Validation should include ensuring that software tools generate outputs that meet timing and performance constraints, particularly for safety-critical systems. Pre-flight testing and accreditation of code generators, timing analysis tools, and compilers can prevent similar issues.

---

### **6. Lessons Learned on the Accreditation Process**

#### Lesson Learned:

* **Case Title**: Tools Without Formal Accreditation Introduced Subtle Errors
* **Case Reference**: **LLIS-19122** (*Software Development on the Genesis Mission, 2004*)
* **Summary**: The Genesis spacecraft suffered a return capsule crash caused by a configuration error. The error stemmed from reliance on a software development tool that lacked formal accreditation and had subtle bugs that led to incorrect software outputs.
* **Relevance to Requirement**: Accreditation provides a formal mechanism for identifying and certifying tools as reliable and fit for purpose. This ensures that potential tool-induced errors are caught and mitigated early, reducing the risk of propagation into mission-critical operations.

---

### **7. Considerations for Small Projects**

#### Lesson Learned:

* **Case Title**: Challenges of Tool Validation in Resource-Constrained Missions
* **Case Reference**: **LLIS-2203** (*Small Satellite Software Projects, 2011*)
* **Summary**: Small-scale projects with limited resources, such as small satellite missions, often overlook tool validation due to time or budget constraints. As a result, errors in unvalidated tools led to late defects during integration and testing, undermining mission reliability.
* **Relevance to Requirement**: Small projects should leverage **Process Asset Libraries (PALs)** and previously accredited tools to save time and resources while still ensuring tool reliability. This approach ensures that even small projects maintain high standards of validation and accreditation.

---

### **8. Human Oversight in the Accreditation Process**

#### Lesson Learned:

* **Case Title**: Over-Reliance on Automated Tools Without Human Oversight
* **Case Reference**: **LLIS-1403** (*Failure of Automated Code Analysis Tools, 2006*)
* **Summary**: During the testing of automated static analysis tools, assumptions about the tool's accuracy resulted in oversight of manually reviewing results. The automated tools failed to detect certain defects due to edge cases, which led to significant debugging efforts late in the development lifecycle.
* **Relevance to Requirement**: Validation of tools must include human review and oversight. Even when tools are accredited, regular monitoring and manual analysis ensure that edge cases or unique scenarios are accounted for.

---

### **Summary of Relevant Lessons Learned**

| **Key Takeaway** | **Lessons Reference** |
| --- | --- |
| Validate reused tools under new conditions. | LLIS-2011 (Ariane 5) |
| Use prior PALs to identify accredited tools. | LLIS-2203 (Small Projects) |
| Validate safety-critical timing constraints. | LLIS-19382 (Mars Pathfinder) |
| Consider human oversight in validation. | LLIS-1403 (Automated Tools) |
| Understand tool/library interactions. | LLIS-43201 (SOHO Error) |
| Transition to new tool environments carefully. | LLIS-1802 (X-38 Development Toolchain) |

By integrating lessons from these cases, NASA projects can ensure that tools used in software development and maintenance are rigorously validated and appropriately accredited for their intended purpose. Adhering to this requirement reduces the likelihood of tool-induced errors and ensures mission success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Consolidate tools and automate workflows where possible](https://software.gsfc.nasa.gov/lesson-details/333/). **Lesson Number 333**: The recommendation states: "Consolidate tools and automate workflows where possible."

# 7. Software Assurance

**SWE-136 - Software Tool Accreditation**

4.4.8 The project manager shall validate and accredit the software tool(s) required to develop or maintain software.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the software tool(s) needed to create and maintain software is validated and accredited.

## 7.2 Software Assurance Products

For this requirement, software assurance plays a vital role in verifying that all tools used in the software development and maintenance lifecycle are appropriately validated and accredited to ensure their reliability, reduce risks, and prevent tool-related errors. The following **Products** should be produced as part of the software assurance process:

1. **Validated and Accredited Criteria for Tools**:

   * A documented set of criteria used to evaluate whether software tools meet the required standards for validation and accreditation. This includes safety, reliability, performance, and compatibility criteria.
   * Criteria should include requirements for tool configuration management, software defect tracking, testability, and confirmation of tool performance within the scope of the project's requirements.
2. **Validated and Accredited Results for Tools**:

   * Records showing that tools have been validated and accredited for their intended use in the project. This should include:
     + Validation test plans, test cases, and results.
     + Accreditation decision artifacts reflecting organizational acceptance.
     + Evidence of tool performance across safety-critical or mission-critical use cases.
   * Any tool discrepancies, limitations, or warnings should also be documented along with the corresponding mitigation actions.

---

## 7.3 Metrics

To monitor the effectiveness of validation and accreditation activities and ensure the reliability of tools, the following metrics should be collected and reported:

1. **Number of Non-Conformances (Open vs. Closed)**:

   * Track non-conformances found in software work products as well as tools, including:
     + **Flight Code**: Errors found in code intended for flight systems.
     + **Ground Code**: Issues encountered in ground support software.
     + **Tools**: Problems identified during tool validation or operation.
     + **COTS Products**: Non-conformances related to commercial off-the-shelf components.
   * Monitor the progress of closing non-conformances and ensuring corrective actions are complete.
2. \*\*Additional Metrics from **[SA Suggested Metrics Topic 8.18]**:

   * Percentage of tools validated prior to major project milestones.
   * Number and recurrence of tool-related errors or defects observed during software development lifecycle phases.
   * Cycle time or effort required to validate and accredit software tools.

---

## 7.4 Software Assurance Guidance

To fulfill this requirement, software assurance must confirm that any critical software tools used for the development, analysis, testing, or maintenance of software have been explicitly validated and accredited. Tools that are validated and accredited help ensure they do not introduce errors or biases into the software being developed, enhancing the likelihood of producing functional and reliable work products.

---

### **Steps for Confirming Tool Validation and Accreditation**

#### **1. Identify the Tools Used in the Project**

* Obtain a complete and comprehensive list of all tools used in software development and maintenance.
* This includes tools such as:
  + Compilers, debuggers, unit-test tools, memory-check tools, and static/dynamic analysis tools.
  + Configuration management tools, code-coverage tools, IDEs, and code generation tools.
  + Linked or third-party libraries (e.g., math libraries).
  + Simulators and build tools.
* Ensure this list is maintained under version control in the project’s configuration management system.

---

#### **2. Verify Validation Status of Tools**

* Confirm whether the tools in use have already been validated and accredited by the project or an external organization. Look for existing evidence of validation, such as:
  + Validation test results from prior projects that used the tool.
  + Records in the **Process Asset Library (PAL)** or other organizational repositories.
* **For Third-Party Tools**: Verify whether the tool has been approved or certified by recognized agencies (e.g., NIST, ACM) or if it comes with vendor certification documentation.

---

#### **3. Determine Safety Implications of Tools**

* Review whether the tools being used impact the safety of the system or product:
  + Evaluate the severity of harm caused by the tool producing incorrect results.
  + Analyze the likelihood of such errors occurring.
  + Prioritize strict validation and accreditation for safety-critical systems.
* Refer to **SWE-020** (Classification of Software) and **SWE-023** (Safety-Critical Requirements) to assess tool impact on mission safety and determine required mitigations.

---

#### **4. Verify Compliance with Validation Criteria**

For tools requiring validation:

* Confirm that inputs to the tool are accurate, complete, and conform to the tool's intended use parameters.
* Check whether all outputs produced by the tool:
  + Match expectations based on predefined reference outputs.
  + Are documented and explained for traceability (e.g., discrepancies must be noted and reconciled).
* Assess whether the tool is being operated within its defined limitations. Examples:
  + Using supported versions of the tool.
  + Adhering to the tool's input/output size constraints.

---

#### **5. Conduct Validation and Accreditation**

* For tools not previously validated, software assurance must support the creation of validation plans with the software development team. Activities should include:
  + Testing tools against diverse test cases that reflect operational conditions.
  + Performing functional demonstrations and use-case simulations.
  + Examining edge cases or scenarios with high risk to expose tool limitations.
* Accreditation decisions should be thoroughly documented, detailing:
  + The validation process followed.
  + Scope of tool usage approved for the project.
* Confirm with the Technical Authority that the accreditation process has been executed and tools approved.

---

### **Additional Software Assurance Considerations for Tools**

Software Assurance should confirm that tools are maintained, monitored, and used correctly during operation. Key considerations include:

* **Tool Maintenance**:

  + Ensure tools and their configurations are version-controlled.
  + Keep tools up-to-date with necessary patches or new versions.
  + Verify that tools with licenses (e.g., COTS tools) remain valid for the project duration.
* **Tool Risks and Known Issues**:

  + Verify that any known limitations or risks related to the tool are identified, documented, and tracked in the project’s risk management system.
  + Mitigation actions for tool discrepancies should be tested and confirmed.
* **Evaluate Trust in Results**:

  + Assure that the results generated by the tool can be traced back to source inputs.
  + Request analysis on the accuracy, reliability, and certainty of tool outputs, especially for safety-critical applications.
  + Escalate concerns or anomalies not easily explained.

---

### **Example Guidance for Tools with Safety Implications**

* For **code-generation tools**, ensure that the generated code is validated (e.g., manually or through testing) for runtime correctness and conformance to functional requirements.
* For **library validation**, ensure that linked code (e.g., math libraries) has been tested for its intended use (e.g., numerical stability, correct handling of precision errors).
* For **built-in analysis tools** (e.g., memory checkers, coverage tools), confirm that the tool settings are configured properly to produce meaningful results and have no adverse runtime impact.

---

## 7.5 Closing the Accreditation Loop

#### Peer Review of Validation Results

* Conduct a peer review of the results from the validation and accreditation process to verify completeness, correctness, and adherence to the requirement. This aligns with the peer review goals of **SWE-087, SWE-088**, and **SWE-089**.
* Peer reviews should focus on ensuring:
  + Discrepancies have been addressed and resolved.
  + Validation confidence is achieved, particularly for critical systems.
  + The validation and accreditation process used is repeatable and robust.

#### Documentation of Evidence

* Final validation and accreditation results should be recorded in the **Software Management Plan (SMP)** or **Software Development Plan (SDP)** for traceability.

---

### **Concluding Guidance**

By adhering to these guidance steps, software assurance can ensure that all tools directly influencing the development and maintenance of software meet the standards required for safety, reliability, and mission-critical performance. This approach ensures that software outputs are not adversely impacted by tool-induced defects, reduces project risk, and supports the overall success of the software development lifecycle.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical to demonstrate compliance with the requirement to validate and accredit software tools. This evidence should provide traceable, verifiable, and auditable proof that software tools were properly validated and accredited for their intended use during the software development and maintenance lifecycle.

---

### **1. Tool Inventory and Usage Documentation**

* **Evidence**: Comprehensive list of all software tools used in the development and maintenance processes.
* **Description**:
  + A documented inventory of tools (e.g., compilers, code generators, debuggers, libraries, version control systems, static/dynamic analyzers, simulators), including:
    - Tool name/identifier and version.
    - Tool vendor or development source.
    - Tool use cases/applications.
    - Tool inputs, outputs, and role(s) in the project.
  + Captured in the **Software Management Plan (SMP)**, **Software Development Plan (SDP)**, or equivalent project document.
* **Purpose**: Provides traceability of all tools used and their potential influence on software products.

---

### **2. Tool Validation and Test Plan**

* **Evidence**: Validation test plans for software tools.
* **Description**:
  + Plans outlining the test procedures and test cases used to validate tools. Specific details may include:
    - Scope, objectives, and expected outcomes of the validation campaign.
    - Tool capabilities being tested (e.g., correctness, performance, limits, configurations).
    - Use-case-specific validation scenarios, including representative and edge cases for software and hardware environments.
    - Detailed workflow of the tool validation process.
  + Referenced in project-specific validation documents or the project’s **Tool Validation Report**.
* **Purpose**: Demonstrates proactive planning and rigorous validation of the tools.

---

### **3. Validation Test Results**

* **Evidence**: Test logs and results from validation activities.
* **Description**:
  + Documentation produced during execution of the validation test plan. Includes:
    - Test reports containing the actual output and comparisons with expected results.
    - Logs showing repeatability and consistency of outputs from the tool across use cases.
    - Evidence of stress, boundary, and exception testing performed.
    - Verification that validated tools do not introduce errors or discrepancies into software outputs.
  + Indexed and stored in the project configuration management system.
* **Purpose**: Verifies the accuracy, reliability, and predictability of the tool’s behavior under realistic and extreme conditions.

---

### **4. Accreditation Records**

* **Evidence**: Formal tool accreditation approval records.
* **Description**:
  + Official documentation certifying that the validated tool is determined to be acceptable for use in the project. Includes:
    - Accreditation authority (e.g., software technical authority, Center software assurance team, or project-level approver).
    - List of project requirements met by the tool, with supporting validation results.
    - Use-case contexts for which the tool is accredited.
    - Version(s) of the tool and environment configuration included under accreditation approval.
  + Captured in project approval records, accreditation memos, or decision artifacts.
* **Purpose**: Demonstrates formal approval of the tool for use and clearly defines its limitations or conditions for usage.

---

### **5. Risk Assessment for Tools**

* **Evidence**: Risk assessment reports for tools with critical or safety implications.
* **Description**:
  + Documentation assessing the impact of tool failure or incorrect operation on the project. Includes:
    - Identification of potential tool failure modes.
    - Severity and likelihood analysis for safety-critical or mission-critical tools.
    - Mitigation plans for risks identified (e.g., additional testing, configuration controls, or redundant validation steps).
  + Typically captured in the project’s **Risk Management Plan** or **Hazard Reports**.
* **Purpose**: Ensures the risks of tool usage are understood and mitigated appropriately.

---

### **6. Configuration Management Evidence**

* **Evidence**: Configuration and version control records for tools in use.
* **Description**:
  + Version-controlled records of tool installations, updates, and configurations. Includes:
    - Tool installation files and change logs.
    - Patch or update history, along with revalidation evidence.
    - Library dependencies or linked resources, with their validated versions.
    - Tool configuration files demonstrating compliance with project standards.
  + Maintained under the project’s **Configuration Management System (CMS)**.
* **Purpose**: Ensures that validated and accredited tools remain consistent, up to date, and reliable throughout the software lifecycle.

---

### **7. Evidence of Third-Party Validation or Certification**

* **Evidence**: Validation results or certification from external organizations or vendors.
* **Description**:
  + Proof that third-party tools (e.g., Commercial Off-The-Shelf (COTS) tools) were validated by their developers or an external standards organization. Includes:
    - Test results or certification (e.g., from NIST, ACM, or ISO).
    - Statements of compatibility or compliance from the vendor or third-party assessor.
    - Warranties from tool developers on specific validated functionalities or use-case ranges.
  + Uploaded to the project repository as supporting evidence for tool accreditation.
* **Purpose**: Reduces the validation burden on the project by leveraging external assurance processes while ensuring tools are appropriate for project use.

---

### **8. Peer Review Records**

* **Evidence**: Peer review artifacts for tool validation and accreditation processes.
* **Description**:
  + Documentation from peer review sessions covering:
    - Validation test plans and test results for tools.
    - Accreditation decisions and rationale, including limitations or concerns.
    - Findings and corrective actions identified during the review process.
  + Peer review forms, inspection checklists, and review minutes linked to the project’s quality assurance activities.
* **Purpose**: Ensures that critical validation and accreditation artifacts are subjected to independent review, increasing trust in the process.

---

### **9. Issue Resolution Records**

* **Evidence**: Records of discrepancies, issues, and resolutions during tool validation.
* **Description**:
  + Documentation of any non-conformances, bugs, or errors found in tools during validation or project use. Includes:
    - Issue logs describing the problem and its impact.
    - Root cause analysis reports indicating the source of the problem.
    - Resolution or mitigation steps taken (e.g., tool reconfiguration, updates, or process changes).
    - Evidence of revalidation or re-accreditation after issue resolution.
  + Captured in the project’s Issue Tracking System or Corrective Action Tracking System.
* **Purpose**: Demonstrates that all tool-related discrepancies were addressed and resolved before deployment.

---

### **10. Traceability of Tools to Work Products**

* **Evidence**: Traceability matrix linking software tools to outputs or artifacts.
* **Description**:
  + A matrix showing how each tool impacts specific project deliverables or artifacts. For example:
    - Compilers linked to flight-ready binary executables.
    - Code generators linked to mission-critical software routines.
    - Test environments linked to validation or verification steps.
  + Includes assurance that all outputs created via tools passed validation for correctness.
* **Purpose**: Ensures traceability of tool influence on work products and provides additional accountability in complex projects.

---

### **11. Software Technical Authority Review Records**

* **Evidence**: Approval and review documents from the software technical authority.
* **Description**:
  + Evidence of final sign-off by the Software Technical Authority or equivalent body. Documents should include:
    - Validation and accreditation results.
    - Tool compliance with applicable safety, reliability, and performance standards.
    - Any deviations from expected outcomes, with acceptable justifications.
  + Stored in the project repository or approval gate review packages.
* **Purpose**: Formalizes the acceptance of validated and accredited tools into the software lifecycle.

---

### Summary of Objective Evidence:

1. Tool Inventory List.
2. Validation Test Plan and Test Results.
3. Accreditation Records.
4. Risk Assessments for Tools.
5. Configuration Management Logs.
6. Third-Party Validation or Certification Evidence.
7. Peer Review Artifacts.
8. Issue Resolution Logs.
9. Tool-to-Work Product Traceability Matrix.
10. Software Technical Authority Approval Records.

By collecting this objective evidence, projects can ensure compliance with the requirement, strengthen the reliability of their software tools, and provide confidence that these tools contribute positively to product quality and safety.

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
