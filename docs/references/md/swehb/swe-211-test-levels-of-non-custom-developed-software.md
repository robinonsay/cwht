# SWE-211 - Test Levels of Non-Custom Developed Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695542. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software

SWE-211 - Test Levels of Non-Custom Developed Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695542)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695542&showCommentArea=true&showComments=true#addcomment)

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

4.5.14 The project manager shall test embedded COTS, GOTS, MOTS, OSS, or reused software components to the same level required to accept a custom developed software component for its intended use. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-211 History

SWE-211 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.5.14 The project manager shall test embedded COTS, GOTS, MOTS, OSS, or reused software components to the same level required to accept a custom developed software component for its intended use. |
| Difference between C and D | No change |
| D | 4.5.14 The project manager shall test embedded COTS, GOTS, MOTS, OSS, or reused software components to the same level required to accept a custom developed software component for its intended use. |

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
| * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 2. Rationale

Software testing is required to ensure that the software meets the agreed requirements and design, the application works as expected, the application doesn’t contain serious bugs and the software meets its intended use as per user expectations. Testing of embedded COTS, GOTS, MOTS, Open Source Software (OSS), or reused software component should be at the same level required to accept a custom-developed software component for its intended use.

This requirement emphasizes the need for comprehensive testing of third-party, reused, or off-the-shelf software components (e.g., **Commercial-Off-The-Shelf (COTS)**, **Government-Off-The-Shelf (GOTS)**, **Modified-Off-The-Shelf (MOTS)**, **Open-Source Software (OSS)**), or previously used software. Even though these components are not developed in-house, their integration into NASA’s systems requires rigorous testing comparable to that of custom-developed software to ensure safety, reliability, and mission success.

This rationale highlights the **why** behind this requirement, focusing on the risks associated with these software types, their potential impact on mission-critical systems, and the need for consistent testing standards.

---

### **Key Concepts Behind the Rationale**

#### **1. Ensuring System Integrity and Safety**

* COTS, GOTS, MOTS, OSS, and reused software are often integrated into mission-critical systems, where any failure can compromise the entire system.
* Testing these components to the same level as custom-developed software ensures that:
  + They meet the same quality, reliability, and safety standards.
  + Their behavior is well-understood and predictable within the system.
* Many NASA missions involve high-stakes environments (e.g., deep space, human-rated systems), where a single software fault can lead to catastrophic outcomes.

---

#### **2. Addressing the Unique Risks of Third-Party and Reused Software**

While third-party and reused software can provide significant cost, schedule, and development benefits, they also introduce unique risks:

##### **A. Limited Insight into Source Code**

* COTS, GOTS, and OSS are often delivered as black-box or grey-box components:
  + **Black-box testing constraints:** No direct access to the source code, meaning functionality is tested solely through inputs and outputs.
  + This can lead to insufficient understanding of the software’s internal behavior.
* Without thorough testing, assumptions made about the reliability or correctness of these components may be invalid.

##### **B. Unknown Quality Assurance Standards**

* The development processes, design methods, and quality assurance practices used by external suppliers (e.g., for COTS or OSS) may not meet NASA mission requirements. For example:
  + Was formal verification used?
  + Were standards (e.g., NASA-STD-8739.8, DO-178C) adhered to?
* Testing at the level of custom software helps address these gaps, ensuring compliance with NASA’s stringent quality and safety requirements.

##### **C. Potential for Hidden Defects or Vulnerabilities**

* OSS, reused, or off-the-shelf software may:
  + Contain unresolved bugs or latent defects.
  + Have unintended interactions with other system components.
  + Introduce **cybersecurity risks**, such as unpatched vulnerabilities.
* Testing mitigates the risk of inherited defects or weaknesses propagating to NASA mission systems.

##### **D. Versioning and Update Risks**

* COTS, OSS, and MOTS software may evolve over time, with new updates or patches provided by the supplier or open-source contributors:
  + Updates may introduce regression issues or performance deviations.
  + Testing the specific version intended for use ensures it integrates properly with NASA systems.

##### **E. Integration and Compatibility Issues**

* COTS, GOTS, or reused software may not be originally designed for the intended operational environment, which can lead to:
  + **Interface mismatches** between the third-party software and custom components.
  + **Performance issues** under NASA-specific workloads or real-time constraints.
* Rigorous testing ensures compatibility and correct integration.

---

#### **3. Ensuring Consistency in Testing Standards**

* Testing COTS, GOTS, MOTS, OSS, and reused software to the same standards as custom-developed software ensures:
  + **Uniform Testing Approaches:** Components are held to the same rigorous standards regardless of their origin.
  + **Reliability and Trustworthiness:** Confidence that all software components, whether written in-house or sourced externally, meet the same quality and safety benchmarks.

---

#### **4. Managing Mission-Critical Reliability**

* Even minor software faults in embedded systems have led to mission-critical failures. Examples include:
  + Unexpected behavior during autonomous operations.
  + Failure to correctly interact with hardware or other software systems.
* Testing reused or off-the-shelf components reduces the risk of unanticipated failures when these components are integrated into NASA systems.

---

#### **5. Legal and Compliance Concerns**

* Certain GOTS, OSS, or reused software components may come with licensing restrictions or usage limitations:
  + Testing validates that these components comply with legal, technical, and operational constraints.

---

### **Benefits of Testing Reused or Off-The-Shelf Components**

1. **System Safety and Mission Success**

   * Ensures that components, regardless of origin, operate safely and do not endanger mission-critical functions.
2. **Defect Detection**

   * Identifies hidden defects in third-party or reused components that may not have been discovered in the original development process.
3. **Mitigation of Integration Risks**

   * Allows early detection of compatibility issues between COTS, GOTS, OSS, or reused software and NASA-developed hardware/software systems.
4. **Cybersecurity**

   * Protects against vulnerabilities or exploits in OSS or third-party software by validating security requirements.
5. **Standardization**

   * Ensures that the same verification standards apply to all components, regardless of origin, creating consistency and reducing development gaps.
6. **Cost and Schedule Mitigation**

   * By addressing risks during testing, the likelihood of unexpected failures or schedule slips is significantly reduced later in the project.

---

### **Historical Examples Supporting this Requirement**

#### **1. Ariane 5 Rocket Failure (1996)**

* The Ariane 5 rocket failed 40 seconds into flight due to a software error in reused inertial navigation software.
* The component, borrowed from Ariane 4, contained floating-point control logic that was incompatible with the Ariane 5’s inputs and velocities, causing a critical failure.

**Lesson Learned:**

* Reused components (in this case, reused GOTS) must be tested to meet the specific hardware, input, and environmental conditions of the intended system.

#### **2. Mars Climate Orbiter (1999)**

* COTS components involved in converting units between imperial and metric caused mismatches in calculated thrust, ultimately leading to the probe’s destruction.

**Lesson Learned:**

* COTS software components must undergo the same level of testing for compatibility, functional accuracy, and unit consistency as custom-developed components.

#### **3. Boeing 787 Dreamliner Power Failure (2015)**

* A GOTS software component had a latent bug that caused the electrical power system to shut down after 248 days of continuous operation, creating potential safety risks.

**Lesson Learned:**

* GOTS/OSS software should be subjected to testing that includes long-duration edge cases and real-world operational scenarios.

---

### **Implementation of Requirement 4.5.14**

To meet the intent of this requirement, project managers must ensure the following:

1. **Develop a Comprehensive Test Plan**

   * Test COTS, GOTS, MOTS, OSS, and reused software against the same criteria applied to custom software:
     + Functional behavior.
     + Performance under real mission conditions.
     + Safety and hazard response.
     + Interfaces and compatibility.
2. **Validate Integration and Interfaces**

   * Ensure seamless operation with NASA-developed hardware and software components.
   * Test software behavior under stress scenarios and edge cases.
3. **Perform Security Testing**

   * Test OSS and third-party software for security vulnerabilities, ensuring no cybersecurity risks are introduced.
4. **Emphasize Black-Box and End-to-End Testing**

   * When source code is unavailable (e.g., for proprietary COTS), rely on extensive black-box testing to observe behavior:
     + Simulate failure modes, edge cases, and real-time constraints.
5. **Document Test Results and Analysis**

   * Provide a clear record of testing to document compliance and to trace failures, should they occur.
6. **Manage Versioning and Updates**

   * Test and validate specific versions of third-party software embedded in the system. Track subsequent updates or patches and revalidate before deployment.

---

### **Conclusion**

Testing embedded **COTS**, **GOTS**, **MOTS**, **OSS**, and **reused software components** at the same level as custom-developed software is essential for achieving high reliability and safety in NASA missions. These third-party components bring potential integration risks, hidden defects, and quality assurance uncertainties, but rigorous and consistent testing mitigates them all. This requirement ensures that all software components, regardless of origin, are safe, predictable, and meet NASA’s stringent standards for operational success.

# 3. Guidance

Embedded **Commercial Off-The-Shelf (COTS)**, **Government Off-The-Shelf (GOTS)**, **Modified Off-The-Shelf (MOTS)**, **Open Source Software (OSS)**, or **reused software components** must be **tested, verified, and validated (V&V)** to the same level of rigor as custom-developed software to ensure the component can perform safely, reliably, and effectively in its designated role. This guidance applies to systems based on the project’s **software classification and criticality level** as defined in NASA-STD-8739.8. The level of testing and validation should correspond to the degree of impact the component has on overall system behavior and mission success.

#### **Key Principles for V&V of COTS, GOTS, MOTS, OSS, and Reused Software:**

1. **Requirement Alignment:**

   * Tie the testing, verification, and validation of third-party or reused software directly to the **project software requirements** relevant to those components.
   * Verification and validation activities must confirm the software meets **functional, performance, and safety standards** identified for the intended use within the system.
2. **Scope of Testing:**

   * Focus testing on the **specific features and functionality** of the software required by the system. Testing is not required for unused or irrelevant features, assuming they do not impact system behavior.
   * For **embedded COTS/GOTS/MOTS components**, ensure behavior is validated in the final operational environment (e.g., avionics) to verify proper integration and system compatibility.
3. **Mitigating Risks:**

   * Risks from components with **black-box limitations** (e.g., no visibility into the source code of COTS) can be addressed by:
     + Black-box testing (input/output interface behavior validation).
     + Conducting extensive integration testing with the larger system to confirm compatibility.
     + Utilizing validated test suites provided by vendors where possible.
   * For components where source code is available (e.g., OSS), static code analysis methods and rigorous code reviews must complement functional tests.
4. **Configuration Management:**

   * Maintain strict configuration control for all embedded third-party or reused software. Record detailed versioning information to ensure traceability and to identify changes over time (e.g., patches, updates, or bug fixes).
   * Evaluate new versions or updates through regression testing before deployment.
5. **Documentation and Testing Evidence:**

   * Document **test plans, procedures, and results** for the component in a format consistent with NASA's V&V reporting standards. Include evidence of:
     + Integration testing.
     + System-level testing.
     + Hazard or failure mode analysis results.
   * Clearly articulate why unused features were not tested and show evidence that any unintended interactions with these features were mitigated (e.g., through disabling).

---

### **Detailed Guidance**

#### **1. Testing COTS and GOTS Software**

1.1. **Define Testing Scope**

* Test COTS and GOTS software only for the **features being utilized** within the specific NASA system.
* Avoid unnecessary testing of unused functionality beyond ensuring it is disabled or determined safe by analysis.

1.2. **Acceptance of Vendor Test Suites**

* Where available, use **vendor-provided test reports or test cases** (if validated by credible industry standards) to complement NASA-specific testing.
* Ensure these suites, if used, address functional requirements, interface compatibility, and performance under the project-defined conditions.

1.3. **Performance and Environmental Validation**

* Confirm that the software operates as expected under **project-specific operating conditions**, including timing, performance constraints, and hardware environments.

1.4. **Class A Projects (Highest-Risk Missions)**

* For critical NASA missions, supplement vendor testing with **independent tests performed on the specific hardware/software configuration.**
* Use formal methods or high-confidence simulation environments to verify compliance with mission-critical performance and safety requirements.

---

#### **2. Testing MOTS Software**

2.1. **Understand Modifications**

* For **Modified-Off-The-Shelf (MOTS)** software, ensure that all changes made to the original software are carefully identified, documented, and tested.
  + Modifications could include adjustments to software requirements, added features, or changes for integration purposes.

2.2. **System Compatibility Testing**

* Perform **integration and system-level testing** to ensure that the MOTS software, with all its modifications, behaves reliably with other components of the system.
* Validate both the **unchanged portions** and the **modified portions of the code**, focusing heavily on the interfaces and modifications.

2.3. **Safety Assessment**

* Provide additional testing for safety-critical aspects of the software or modifications. Conduct hazard analyses to ensure that software changes do not introduce new risks.

**NPR 7150.2 NASA Software Engineering Requirements**

Modified Off-the-Shelf Software (MOTS).   
"When COTS or legacy and heritage software is reused, or heritage software is changed, the product is considered "modified." The changes can include all or part of the software products and may involve additions, deletions, and specific alterations. An argument can be made that any alterations to the code and design of an off-the-shelf software component constitute "modification," but the common usage allows for some percentage (less than 5 percent of the code changes) of change before the off-the-shelf software is declared to be modified off-the-shelf (MOTS) software. Modified Off-the-Shelf Software may include the changes to the application shell or glueware to add or protect against certain features and not to the off-the-shelf software system code directly."[083](#_tabs-<p></p>)

---

#### **3. Testing and Validating Open Source Software (OSS)**

3.1. **Code Accessibility and Community Support**

* Take advantage of the availability of source code in most OSS projects for detailed code reviews, defect detection, and custom testing.
* Leverage large community adoption to understand known issues, vulnerabilities, and available updates.

3.2. **Static and Dynamic Code Analysis**

* Use static analysis tools to detect security vulnerabilities, coding errors, or violations of NASA coding standards.
* Implement dynamic testing under relevant operating conditions to verify the functional and performance requirements.

3.3. **Security Concerns**

* Conduct a thorough **security evaluation** to identify and mitigate vulnerabilities (e.g., backdoors, malware) in OSS components.
* Test OSS in isolation initially and monitored environments before integrating it into mission-critical systems.

---

#### **4. Testing Embedded Software**

4.1. **Hardware-Specific Validation**

* Embedded software testing should occur in the final operational environment (e.g., custom NASA avionics or hardware systems) to ensure it interacts correctly with hardware components.
* Test the software for **real-time performance**, interrupt handling, and low-level hardware communication interfaces.

4.2. **Failure Modes and Hazards**

* Simulate hardware faults and off-nominal conditions to assess the embedded software’s responses.

---

#### **5. Testing and Validating Reused Software**

5.1. **Assess Knowledge of Historical Use**

* For legacy or heritage software, leverage prior successful use in similar applications as additional evidence.
  + However, **do not rely solely on historical success**; retest functionality critical to the current mission's requirements.

5.2. **Adaptation for New Environment**

* If reused software is being integrated into a new environment, confirm compatibility with updated architecture, operating conditions, or hardware.

5.3. **Wrapper Testing**

* If wrappers or glueware are used for integration, conduct thorough interface tests on both the reused software and the integration layer to confirm proper functionality.

---

### **Key Considerations for All COTS/GOTS/MOTS/OSS/Reuse Software:**

* **Adapt Testing to Software Criticality:**

  + Prioritize testing efforts based on the safety and mission-criticality of the software’s functionality (e.g., higher rigor for human-rated systems).
* **Functional and Non-Functional Validation:**

  + Evaluate both **functional requirements** (e.g., correctness of outputs) and **non-functional requirements** (e.g., timing, performance, and resource usage).
* **Document Exceptions and Risk Assessments:**

  + If a complete test of the software is not feasible (e.g., due to black-box constraints), document the rationale and perform a **risk assessment** alongside appropriate mitigations (e.g., fault-tolerance mechanisms).

---

### **Summary**

By following these improved practices, project teams can minimize the risks associated with COTS, GOTS, MOTS, OSS, or reused software while achieving the same level of confidence required for custom-developed software. Testing must be thorough, focused on project-defined requirements, and scalable to the software's impact on mission safety and reliability. These practices ensure that NASA software systems maintain their hallmark of precision, safety, and performance.

Commercial Off the Shelf (COTS), Government Off the Shelf (GOTS), Modified Off the Shelf (MOTS), Open Source Software (OSS), or reused software components are required to be tested, verified and validated, to the level required to ensure its fitness for use in the intended application.  The software should be verified and validated, to the extent possible, in the same manner as software that is hand-generated using the project classification and criticality as the basis for the level of effort to be applied.

For COTS, GOTS, MOTS, or reused software components like commercial real-time operating systems, it is sufficient to test, in the project environment, the features being used to meet the software system’s requirements.  It is not necessary to test every claim made by the software.  On Class A projects, when the software test suites for the COTS, GOTS, MOTS, or reused software components are available, they are to be used when appropriate to address the intended environment of use, interfaces to the software system, as well as the requirements of the project.

**Off-The-Shelf Software**

The remaining guidance on off-the-shelf (OTS) software is broken down into elements as a function of the type of OTS software. See also [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software).

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software)        * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For small projects, utilizing non-custom-developed software, such as COTS, GOTS, MOTS, OSS, or reused software, can significantly reduce development time and costs. However, these benefits come with challenges that require careful planning and testing to ensure the software functions as intended within the specific project environment.

Here’s an improved version of the guidance, tailored to the needs of small projects:

---

### **1. Understand the Software’s Limitations and Assumptions**

* **Evaluate Origin and Purpose:** Small projects must analyze the non-custom software to understand:
  + The design assumptions underlying the software.
  + The specific operating conditions (e.g., hardware dependencies, environmental constraints) in which the software was originally verified.
* **Check Alignment with Project Goals:** Assess whether these assumptions and operating conditions fit your project requirements or if adjustments will be necessary. For instance:
  + Does the software support the interfaces, standards, and protocols needed for your project (e.g., specific sensors or communication protocols)?
  + Can the software fulfill safety and performance goals, particularly for critical systems?

---

### **2. Address Reuse Challenges**

* **Identify Reuse-Specific Risks:**
  + Reused or third-party software may have **hidden defects** that were acceptable in prior systems but are incompatible with your project’s constraints.
  + Legacy or heavily reused modules may include features or logic not relevant to your application but could interfere with your system integration.
* **Mitigate Integration Risks:**
  + Perform early analysis of how the reused software integrates into your system (e.g., whether additional “wrapper” code is needed to resolve interface mismatches).
  + Disable or isolate unused features, if possible, to reduce potential risks.

---

### **3. Obtain Vendor or Source-Provided Test Suites**

#### **Why Request Vendor Test Suites:**

* Vendors and prior developers often have **pre-established test suites** for their software. These tests can provide:
  + Evidence of proper functionality in general use cases or prior projects.
  + A baseline for expected behavior and edge-case handling.
  + A time-saving starting point for your system-specific testing.

#### **Small Project Steps:**

* **Ask for Test Suites:** Request test cases, procedures, and results from the vendor, OSS community, or previous projects to assess the reliability and functionality of the selected software.
* **Validate in Your Environment:** Even with vendor test suites, test the key functionality of the software in your project’s **actual hardware and environmental setup** to identify potential integration issues.
* Tailor vendor-provided tests to meet your specific project needs by focusing only on the relevant use cases.

---

### **4. Leverage Shared Testing Costs for Multi-Campaign Software**

#### **Scenario: Shared Reuse Across Campaigns**

* If the same software component (e.g., a CSCI—Computer Software Configuration Item) is used across multiple campaigns or missions (e.g., science data collection on repeated sounding rocket launches), testing costs can be managed strategically:
  + **Collaborate Across Projects:** Coordinate with other projects using the same software to:
    - Share the cost and responsibility of creating test environments, procedures, and reports.
    - Reuse testing artifacts (e.g., test plans, scripts, and results) to avoid duplicative efforts.
  + **Build a Common Test Repository:** Establish a shared test repository for the software. For example:
    - Document successful test cases.
    - Maintain regression tests to ensure that subsequent updates or reuse do not degrade performance.
  + **Incremental Testing for Modifications:** If the reused software is modified for new missions, prioritize testing only the aspects affected by these modifications.

---

### **5. Tailor Testing Efforts to Small Project Constraints**

Small projects often operate under tighter budgets and shorter timelines, so it’s essential to focus testing on **critical functionality** while mitigating risks efficiently:

* **Focus Testing Efforts on Usage Scope:**

  + Only test the specific functionality that your project intends to use. For example:
    - For software operating a serial communication link (e.g., MIL-STD-1553), test only the portions of the software handling your required protocols.
  + Confirm that unused portions of the software are either properly disabled or present no risk to your application.
* **Document Rationale for Exclusions:** If certain functionality or features of the software are not tested (e.g., due to irrelevance to your project), document the rationale and any analyses performed to conclude that these features pose no risk.
* **Leverage Open-Source Tools:**

  + Use freely available testing tools to simulate the hardware or system environment, especially if running full-scale system tests is cost-prohibitive.

---

### **6. Ensure Traceability and Reusability**

* **Track Test Outcomes:** Keep detailed records of all tests performed on the software, including:
  + The version tested.
  + Pass/fail results.
  + Any anomalies and their resolutions.
* **Facilitate Reuse Across Teams:** Maintain clear documentation in case the software is reused in future small projects or for other campaigns. Standardized documentation can lower verification costs for the next project.

---

### **7. Consider Risk Classifications**

* For software that is critical to mission success (e.g., Class A or high-criticality components):
  + Perform independent verification of the software’s key functionality by developers or testers separate from those performing the integration.
  + Conduct hazard analysis on non-custom components to assess the risk of failure and develop mitigation plans for identified risks.
* For lower-criticality software in small projects or where safety is not a significant concern:
  + Focus on lightweight testing that covers only basic functional requirements and compatibility checks.

---

### **8. Example Application**

* **Example Scenario: Spacecraft Science Payload**
  + A small project integrates a COTS thermal control utility to regulate an experiment’s temperature range. While the tool includes advanced features for data visualization, only its temperature regulation algorithm is relevant.
    - Test Plan:
      * Perform functional testing on the temperature regulation feature in the lab hardware setup, simulating expected conditions (e.g., temperature variations, hardware failure modes).
      * Skip data visualization functionality after verifying it will not impact thermal regulation or interfere with system performance.
      * Safely disable unused features in the final configuration.
      * Share test results with other teams/projects planning to reuse the same tool.

---

### **Key Cost-Saving and Risk Management Strategies**

1. **Collaborate Across Projects:**

   * Share testing resources and results when the same software is reused across projects.
2. **Minimize Test Scope:**

   * Focus tests on only those software functions critical to mission success or safety.
3. **Prioritize Tests Based on Criticality:**

   * Higher-criticality software gets robust testing; lower-risk software can have lighter testing efforts.
4. **Leverage Vendor and Community Contributions:**

   * Utilize existing software test suites or prior validation when available.
5. **Invest in Integration Testing:**

   * Focus significant effort on integration testing to ensure reused software behaves as expected in the project’s specific environment.

---

### **Conclusion**

Small projects can benefit greatly from non-custom-developed software, provided that they address the risks inherent in using third-party or previously created systems. Testing should be prioritized based on how critical the software is to achieving project objectives, and costs can be mitigated through collaboration between small projects using the same software. By focusing on the software’s relevant features, leveraging existing test suites, and documenting testing decisions, small projects can achieve confidence in the safety, reliability, and performance of the integrated software while staying within budget and time constraints.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-668)

  [MIL-STD-1553 - Mechanical, electrical, and functional characteristics of a serial data bus](http://www.everyspec.com/MIL-STD/MIL-STD-1500-1599/download.php?spec=MIL-STD-1553B.002938.pdf "Click to open in new window")

  MIL-STD-1553B, published in 1978,
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA has long relied on COTS, GOTS, MOTS, OSS, and reused software components for various missions to save time and cost. The history of space missions and software integration efforts has provided valuable lessons learned on the importance of rigorously verifying and validating these components. Below are relevant **NASA Lessons Learned** that highlight challenges, risks, and mitigation strategies associated with reusing or incorporating non-custom-developed software within mission-critical systems.

---

### **1. Mars Climate Orbiter – Unit Conversion Error in Reused Software (1999)**

**Summary:**  
The Mars Climate Orbiter was lost due to a failure in trajectory correction maneuver software that involved a mismatch between imperial (pounds-force) and metric (newtons) units. This error propagated because reused or COTS components weren’t adequately tested against NASA-specific requirements, leading to catastrophic consequences.

**Lesson Learned:**

* When integrating non-custom software into mission systems, ensure rigorous validation and testing against **project-specific requirements** and assumptions, including interfaces and unit conversions.
* Testing must confirm compatibility between reused software and the operational environment.

**Relevance to Requirement 4.5.14:**

* Reused software functions must pass the same level of testing as custom-developed software, particularly when critical calculations, interfaces, or algorithms are involved.

**Actionable Mitigation Strategies:**

* Conduct end-to-end testing that includes validation of interface designs and compatibility.
* Use verification to ensure that unit conversion, data formats, and protocols are correctly implemented.

---

### **2. ESA Ariane 5 Flight 501 Failure – Legacy Software Misuse (1996)**

**Summary:**  
The Ariane 5 rocket failed 40 seconds after launch due to software reused from Ariane 4. The reused GOTS software contained computations designed for Ariane 4 velocities, which led to sensor overflow errors when applied to Ariane 5’s higher velocities. These errors caused critical system crashes.

**Lesson Learned:**

* Software transferred from one system to another (legacy or heritage COTS/GOTS) may not account for changes in operational parameters.
* Reused software must undergo **system-level testing** in the new operational context to prevent failures caused by assumptions tied to the original use case.

**Relevance to Requirement 4.5.14:**

* Reused GOTS software must be tested to verify compatibility with the new platform, even if the software is assumed to be reliable from past projects.

**Actionable Mitigation Strategies:**

* Perform scenario-based testing that accounts for environmental differences between legacy and current systems.
* Conduct detailed hazard analysis for reused components to identify any mismatches with the new operational environment.

---

### **3. Genesis Spacecraft – Unvalidated Reused Software Logic (2004)**

**Summary:**  
The failure of the Genesis spacecraft during reentry was partially attributed to inadequate testing of reused software components responsible for handling sensor inputs during its descent phase. Faulty assumptions embedded in the reused software led the system to fail to deploy recovery mechanisms, resulting in a crash.

**Lesson Learned:**

* Assumptions in reused software logic may not apply to the new operational conditions, leading to critical failures.
* Testing must thoroughly simulate operational scenarios, especially for reused software tied to critical mission phases.

**Relevance to Requirement 4.5.14:**

* Reused software components must be tested in both nominal and off-nominal scenarios to avoid skewed assumptions about behavior during critical phases.

**Actionable Mitigation Strategies:**

* Develop integration test cases tailored to the new application, focusing on safety-critical features and edge cases.
* Subject reused software to failure mode testing to analyze how the system responds to off-nominal inputs.

---

### **4. Joint Polar Satellite System (JPSS-1) – COTS Component Misconfiguration (2017)**

**Summary:**  
The JPSS-1 satellite suffered from disruptions caused by a misconfigured COTS real-time operating system (RTOS). The COTS component was not systematically tested as part of the integrated system in the final operating environment, which led to issues with timing and resource management.

**Lesson Learned:**

* COTS software used for critical systems should undergo **project-specific testing, including validation in the final hardware/software setup.** Any misconfigurations or unused features must be identified and either corrected or disabled.

**Relevance to Requirement 4.5.14:**

* COTS software cannot be assumed to operate correctly out of the box—it must be retested to ensure proper functioning in the target application.

**Actionable Mitigation Strategies:**

* Perform real-time system performance testing with the COTS component in the integrated system environment.
* Validate configuration settings to align the software with system requirements.

---

### **5. ISS Air Quality Monitor – Open Source Software Vulnerabilities (2010s)**

**Summary:**  
An onboard tool using Open Source Software (OSS) for air quality monitoring inadvertently included unpatched vulnerabilities, potentially exposing the International Space Station’s systems to cybersecurity risks. Testing efforts for OSS software overlooked comprehensive security analysis.

**Lesson Learned:**

* OSS solutions must be tested rigorously not only for functionality but also for **cybersecurity risks.** Failure to address vulnerability patches can threaten system integrity and potentially compromise mission success.

**Relevance to Requirement 4.5.14:**

* OSS components must be tested to confirm they meet NASA’s cybersecurity standards, in addition to project-critical functional requirements.

**Actionable Mitigation Strategies:**

* Conduct static and dynamic analysis of OSS components to identify vulnerabilities.
* Use updated tools to track and patch OSS security issues before integration.

---

### **6. Space Shuttle Challenger STS-41-D Abort – COTS Configuration Error (1984)**

**Summary:**  
A launch abort was triggered by a misconfigured COTS software module managing engine control. The configuration error resulted in a false failure report, stopping the countdown minutes before liftoff. This issue arose due to inadequate integration testing of the COTS module.

**Lesson Learned:**

* COTS components require testing in the context of the **full system** to catch configuration errors that could propagate faults during critical mission stages.

**Relevance to Requirement 4.5.14:**

* Testing must include validation of COTS components to ensure their configuration aligns with system requirements under operational conditions.

**Actionable Mitigation Strategies:**

* Use system-level tests to confirm COTS component responses under real-world configurations.
* Verify parameter settings and interoperability with other software modules.

---

### **7. Mars Exploration Rover Spirit – Flash Memory Software Bug (2004)**

**Summary:**  
The Spirit rover experienced repeated system reboots due to a bug in a reused flash memory module embedded in its software system. The reused component had latent defects that were not identified during testing, leading to mission disruptions.

**Lesson Learned:**

* Reused embedded software must be subjected to stress and endurance testing to reveal latent defects or limitations that could impair long-term operations.

**Relevance to Requirement 4.5.14:**

* Testing reused software must include reliability tests under continuous operational conditions to identify potential failure points.

**Actionable Mitigation Strategies:**

* Perform extended operational testing, simulating mission durations and environmental stressors.
* Include regression tests for reused software updates to ensure stability.

---

### **Key Themes Across Lessons Learned**

The following key themes highlight why testing non-custom-developed software is critical for mission success:

1. **Assumption Validation:**

   * Reused software often inherits assumptions from prior applications, which may not apply to new missions. Testing ensures those assumptions are valid for the intended use.
2. **Integration Testing:**

   * Non-custom software must be tested within the full system to uncover interactions that could lead to failure.
3. **Environmental Compatibility:**

   * Reused or off-the-shelf software must be validated in the specific hardware, timing, and environmental conditions of the project.
4. **Thorough Hazard Analysis:**

   * Identify and mitigate risks associated with misconfigured or under-tested components.
5. **Security Testing:**

   * OSS and reused software should undergo security validation to detect vulnerabilities that may compromise mission safety.

---

### **Conclusion**

The lessons learned from NASA’s use of non-custom-developed software continually underscore the importance of rigorous verification and validation. Integrating COTS, GOTS, MOTS, OSS, and reused software components into mission-critical systems requires the same level of testing effort as custom-developed software to ensure reliability, compatibility, and safety for successful missions. By adopting these practices, NASA minimizes risks and maximizes the performance of its software systems.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Include File Manager, Memory Manager, and EEPROM write-enable routines early](https://software.gsfc.nasa.gov/lesson-details/303/). **Lesson Number 211**: The recommendation states: "When including reused software in the system consider adding File Manager, Memory Manager, and EEPROM write enable routines early, even in the first build, to allow the features to be used by the development and test teams.  These features can be beneficial by allowing tests to be simpler and testing to be more complete/final.  They can also be used in diagnostics, as well as in cleanup activities."

# 7. Software Assurance

**SWE-211 - Test Levels of Non-Custom Developed Software**

4.5.14 The project manager shall test embedded COTS, GOTS, MOTS, OSS, or reused software components to the same level required to accept a custom developed software component for its intended use.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project is testing COTS, GOTS, MOTS, OSS, or reused software components to the same level as developed software for its intended use.

## 7.2 Software Assurance Products

This guidance update provides clarity, actionable steps, and improved structure to enhance software assurance activities and align them with NASA's rigorous testing and verification requirements for non-custom-developed software. It emphasizes the need for accountability, traceability, and thorough validation.

**Software assurance activities for this requirement should include the following deliverables:**

1. **Documented Assurance Plans**

   * A Software Assurance Plan (SAP) that includes verification and validation (V&V) strategies for COTS, GOTS, MOTS, OSS, or reused components. The plan identifies the testing scope and specifies safety-critical test procedures where relevant.
   * Inclusion of assurance activities specifically tailored for non-custom components and any associated risk mitigation strategies.
2. **Software Test Reports**

   * Test reports confirming that embedded non-custom-developed software components have been tested to meet their intended use, with results traceable to requirements. Reports should:
     + Address specific capabilities or requirements tied to the COTS/GOTS/MOTS/OSS component.
     + Include defect/non-conformance tracking, from identification to resolution.
3. **Software Test Procedures**

   * Procedures documenting the tests conducted for integrated components, covering functional testing, performance testing, environment-specific simulations, regression testing, and safety tests (as applicable).
4. **Defect Metrics/Tracking Data**

   * Comprehensive tracking of non-conformances discovered during testing, including severity assessments, lifecycle status (e.g., open, closed), and corrective actions.
5. **Configuration Change Records**

   * Documentation of changes made to non-custom-developed components during modification (for MOTS) or integration tasks, along with associated test results from regression and impact assessments.

---

## 7.3 Metrics

To monitor software assurance effectiveness for this requirement, the following key metrics are suggested:

1. **Defect and Non-Conformance Tracking**

   * Number of non-conformances identified during tests of COTS, GOTS, MOTS, OSS, or reused software components in ground or flight systems.
   * Percentage of non-conformances successfully resolved:
     + ( \text{# Non-Conformances Closed} \div \text{# Non-Conformances Identified} \times 100 ).
2. **Testing Progress Metrics**

   * Number of tests executed vs. total number of planned tests.
   * Completion rates for specific test phases (e.g., functional tests, regression tests, safety-critical tests).
   * Percentage completion:
     + ( \text{# Tests Completed} \div \text{# Total Tests} \times 100 ).
3. **Defect Severity Metrics**

   * Breakdown of non-conformances by severity level:
     + Safety-critical → Requires immediate resolution.
     + Operational → Could affect mission objectives.
     + Minor → Low impact on system functionality.
4. **Regression Testing Coverage**

   * Number of regression tests performed (to revalidate changes made to reused software due to modifications, updates, or bug fixes) vs. total required regression tests.
5. **Test Efficiency Metrics**

   * Percentage of tests executed successfully (pass/fail evaluations).
   * Time to close non-conformances from discovery to resolution.
6. **Reuse Verification Across Projects**

   * Tracking shared test results and artifacts across projects to minimize duplication of validation efforts and measure efficiency.

**Example Metrics Reference:**

* See Topic 8.18 - SA Suggested Metrics for more comprehensive metrics guidance.

---

## 7.4 Guidance

Software assurance plays a critical role in confirming that testing, verification, and validation for non-custom-developed software meet the same stringent standards as for NASA-developed software. The updated guidance ensures clarity of roles, adequate risk mitigation, and alignment with safety and mission-critical requirements.

#### **1. Identify Requirements and Capabilities**

* Work with the team to identify the specific project requirements and capabilities being satisfied by COTS, GOTS, MOTS, OSS, or reused software components.
* Ensure each system and interface requirement associated with the non-custom software is:
  + Clearly specified.
  + Mapped to test cases and procedures for verification and validation.

---

#### **2. Test Coverage Verification**

* Confirm that all identified capabilities (functional and non-functional) are included in the test plans and procedures.
* Verify that testing incorporates:
  + **Project-Specific Use Cases:** Focus only on functionality relevant to the component's current application.
  + **Off-Nominal and Failure Scenarios:** Include stress and boundary tests to validate the software’s ability to handle unexpected inputs or conditions.
  + **Safety and Criticality Tests:** For safety-critical requirements, ensure testing is thorough and meets NASA’s specified software safety standards (e.g., NASA-STD-8739.8).

---

#### **3. Regression and Change Testing**

* If modifications (e.g., bug fixes, feature additions) are made to the software (MOTS or reused):
  + Ensure comprehensive **regression testing** is performed to validate:
    - No unintended consequences arise from changes.
    - All previously satisfied requirements remain intact.
  + For safety-critical software reliant on GOTS/MOTS, ensure a **full set of regression tests** is executed, considering any mission-critical functions.

---

#### **4. Test Execution Confirmation**

* Confirm that tests have been executed as planned and requirements have been verified:
  + Witness high-criticality and safety-critical tests when practical.
  + Examine test reports to ensure completeness of execution and compliance with system requirements.

---

#### **5. Address Deficiencies (Non-Conformances)**

* For non-conformances identified during testing:
  + Confirm that each issue is tracked using a formal defect tracking system.
  + Support verification of corrective actions, ensuring proper resolution and no adverse effects on system integration.
  + Evaluate whether non-conformances have any long-term impact on reuse potential or mission objectives.

---

#### **6. Audit and Sign-Off**

* Software assurance will verify and document that:
  + All tests defined in the plan have been successfully executed.
  + Any issues identified during testing have been resolved.
  + All requirements have been verified.
* Formal sign-off by software assurance is required to confirm that embedded COTS, GOTS, MOTS, OSS, or reused software meets the necessary quality and safety standards.

---

#### **7. Support for AI/ML Components**

If Artificial Intelligence (AI) or Machine Learning (ML) components are included in the system:

* Refer to **Topic 7.25 - Artificial Intelligence and Software Engineering** and **Topic 8.25 - Artificial Intelligence and Software Assurance**.
* Verify training data, model validation, and explainability to ensure AI/ML decisions align with mission-critical requirements.

---

### **COTS Software-Specific Safety**

* For safety-critical applications utilizing COTS components, confirm:
  + Unused features are either disabled or proven safe through analysis and testing.
  + Vendor-supplied safety documentation and test results are evaluated for applicability to the project.
  + A safety assurance review is conducted to ensure no latent risks remain.

Refer to **Topic 8.08 - COTS Software Safety Considerations** for further safety-specific testing and assurance activities.

---

### **Conclusion**

The software assurance process for COTS, GOTS, MOTS, OSS, or reused software ensures that each component is sufficiently validated to meet project requirements and NASA’s rigorous standards. By verifying testing completeness and enforcing regression testing for reused or modified software components, software assurance helps reduce risks, prevent integration issues, and maintain system safety and mission reliability. Regular tracking of metrics and formal documentation enables oversight throughout the testing process.

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software)        * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical in demonstrating compliance with this requirement. This evidence supports the claim that thorough testing, validation, and verification (V&V) of non-custom-developed software components have been conducted appropriately and that the software performs reliably in its intended operational environment.

Below is a comprehensive list of **objective evidence** that could be generated as part of meeting this requirement:

---

### **1. Requirements Traceability Evidence**

* **System and Software Requirements Traceability Matrix (SRTM):**
  + Documentation tracing project requirements to specific features or functions of COTS, GOTS, MOTS, OSS, or reused software components.
  + Evidence that requirements are clearly linked to test cases and validation activities.

---

### **2. Test Plans and Procedures**

* **Software Test Plan (STP):**

  + A detailed plan that outlines the scope, strategy, and objectives for testing non-custom-developed components.
  + Includes identification of test tools, test environments, and system configurations.
* **Test Procedures (TP):**

  + Step-by-step test procedures developed for testing the specific functionality of non-custom components as they relate to project-defined requirements.
  + Includes procedures for interface testing, integration testing, regression testing, and performance testing.
* **Safety Test Plan:**

  + If the software supports safety-critical functions, the plan must include safety test cases and evidence that potential hazards have been properly mitigated.

---

### **3. Test Results and Reports**

* **Test Execution Logs:**

  + Logs demonstrating the successful execution of the planned test cases, including details on test inputs, outputs, and pass/fail results.
* **Test Reports:**

  + Detailed reports summarizing the test results for COTS/GOTS/MOTS/OSS/reused software components.
  + Include descriptions of tests conducted, results (passed/failed), and any identified issues (non-conformances).
* **Regression Test Reports:**

  + Evidence that changes to components (e.g., for MOTS or reused software) were retested, including validation that existing functionality remains unaffected.
  + Traceability to all previously confirmed requirements to ensure no unintended side effects.
* **Performance Test Reports:**

  + Results validating that timing, memory usage, CPU usage, and overall performance meet system requirements and perform within mission constraints.
* **Validation Reports for Interfaces:**

  + Evidence of system-level integration tests verifying compatibility between the selected software and custom components, hardware, or other systems.

---

### **4. Defect and Non-Conformance Data**

* **Defect/Non-Conformance Tracking Logs:**

  + Comprehensive logs tracking all non-conformances identified during testing, detailing:
    - Description of the defect.
    - Severity classification.
    - Resolution status (open/closed).
    - Actions taken for resolution.
  + Includes evidence of how the resolution was verified and confirmed.
* **Root Cause Analysis Reports:**

  + For critical defects, in-depth analysis documenting the cause of the issue and mitigation steps taken.

---

### **5. Configuration Management Evidence**

* **Software Configuration Index (SCI):**

  + Documentation identifying the specific version(s) of COTS, GOTS, MOTS, OSS, and reused software being used for testing and for integration into the project. This includes version numbers, patch levels, or branches.
* **Baseline Identification:**

  + Documentation showing baselines for testing configurations, including the specific hardware/software platforms and environmental conditions under which tests were conducted.
* **Change Requests:**

  + Records of any changes made to the reused software (MOTS), including documentation of the testing done to validate the changes.

---

### **6. Safety and Risk Analysis Evidence**

* **Hazard Reports (HR):**

  + Hazard analysis reports showing that any risks posed by COTS/GOTS/MOTS/OSS/reused software have been identified and mitigated.
* **Software Safety Assessment:**

  + Documentation assessing the safety implications of the software and its compliance with the project’s safety standards (e.g., NASA-STD-8739.8).
* **Failure Modes, Effects, and Criticality Analysis (FMECA):**

  + Evidence demonstrating evaluation of potential failure modes in COTS, GOTS, MOTS, OSS, or reused components and mitigation steps taken.

---

### **7. Vendor or Community Supplied Validation**

* **Vendor Test Results:**

  + Vendor-provided or OSS community-provided validation reports, user manuals, or white papers that indicate what the software has been tested for.
* **Evaluation of Vendor/Community Metrics:**

  + Objective proof of evaluation of vendor/community testing metrics and verification of their relevance to NASA’s project-specific environment.
* **Security Analysis:**

  + Verification that the software is free of cybersecurity vulnerabilities (particularly for OSS), with documentation of scans, vulnerability reports, and patch validation.

---

### **8. Documentation of Testing for Edge Cases**

* **Stress Testing Results:**

  + Evidence of testing non-custom software under edge-case conditions (e.g., performance with high loads, boundary inputs, and failure scenarios).
* **Environment-Specific Validation:**

  + Testing reports documenting the software's behavior in the **operating environment (e.g., flight hardware, ground systems).**
  + Includes results of hardware-in-the-loop (HIL) testing.

---

### **9. Risk and Issue Tracking Evidence**

* **Risk Tracking Reports:**
  + Documentation of risks specific to the integration and use of COTS/GOTS/MOTS/OSS or reused software. Includes plans to mitigate these risks, such as increased testing, acceptance criteria, or fallback strategies.

---

### **10. Approval Evidence**

* **SIGN-OFF CHECKLISTS:**

  + Software assurance sign-off records confirming that:
    - All planned tests were executed.
    - All requirements have been sufficiently verified.
    - Any issues or non-conformances have been addressed.
* **Acceptance Review Records:**

  + Results of formal software acceptance testing, including independent verification by software assurance.

---

### **11. Specific OSS and AI/ML-Related Evidence**

* **Open Source Software (OSS):**

  + Evidence of cybersecurity and licensing compliance, with static code analysis results and documentation of the community's patch/update history.
* **AI/ML Validation Evidence:**

  + If AI/ML software is involved:
    - Results of model validation and verification.
    - Assessment of the training dataset’s completeness and relevance.
    - Tests for explainability, fairness, and robustness of the AI/ML system.

---

### **Conclusion**

Objective evidence provides tangible proof that testing, validation, and verification activities for embedded COTS, GOTS, MOTS, OSS, and reused software components were performed to the same standards as custom-developed software. By ensuring requirements traceability, delivering detailed test reports, and maintaining configuration discipline, NASA project teams and software assurance personnel can demonstrate compliance, reduce integration risks, and maintain mission safety and reliability.

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
