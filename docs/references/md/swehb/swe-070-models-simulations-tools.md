# SWE-070 - Models Simulations Tools

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695452. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools

SWE-070 - Models, Simulations, Tools

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695452)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695452&showCommentArea=true&showComments=true#addcomment)

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

4.5.6 The project manager shall use validated and accredited software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment.

## 1.1 Notes

Information regarding specific V&V techniques and the analysis of models and simulations can be found in NASA-STD-7009, Standard for Models and Simulations, NASA-HDBK-7009, Handbook for Models and Simulations, or discipline-specific recommended practice guides.

## 1.2 History

Click here to view the history of this requirement: SWE-070 History

SWE-070 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.4.6 The project shall verify, validate, and accredit software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment. |
| Difference between A and B | Changed project's responsibility to verify, validate, and accredit to just use ones that have been validated and accredited. |
| B | 4.5.7 The project manager  shall use validated and accredited software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment. |
| Difference between B and C | No change |
| C | 4.5.6 The project manager shall use validated and accredited software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment. |
| Difference between C and D | No change |
| D | 4.5.6 The project manager shall use validated and accredited software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment. |

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

Performing verification and validation (V&V) to accredit software models, simulations, and analysis tools is important to ensure the credibility of the results produced by those tools. Critical decisions may be made, at least in part, based on the results produced by models, simulations, and analysis tools. Reducing the risk associated with these decisions is one reason to use accredited tools that have been properly verified and validated.

This requirement ensures that all software models, simulations, and analysis tools used in the qualification process for flight software and flight equipment are reliable, accurate, and suitable for their purpose. Validation and accreditation of these tools are essential to confirm that they faithfully represent the systems being tested and produce credible, authoritative results. Adhering to this requirement directly contributes to the safety, reliability, and mission success of NASA operations.

---

### **Key Rationale:**

#### **1. Ensures Accuracy and Credibility of Qualification Results**

* **Flight Software and Flight Equipment Qualification**:
  + The qualification process is critical for proving that systems meet mission requirements and can operate reliably under expected conditions. Using validated and accredited tools ensures that predictions, analyses, and results derived during qualification are accurate, reducing the risk of relying on flawed data.
  + Unvalidated or unaccredited tools could provide inaccurate or incomplete results, potentially leading to the use of non-compliant or unsafe flight software/equipment.

#### **2. Enhances Confidence in Models and Simulations**

* **Validated Tools vs. Assumptions**:
  + Validated models and simulations infuse confidence into the analysis process by demonstrating that the tools replicate real-world system behaviors or physical phenomena accurately.
  + Without validation, tool outputs cannot be trusted, increasing the likelihood of undetected defects or failures during testing or operations.

#### **3. Supports Risk Reduction and Hazard Mitigation**

* **Minimizes Integration Risks**:
  + Flight software is often closely integrated with flight hardware. Misaligned or inaccurate simulation models may result in integration issues, failure to address hazards, or suboptimal system performance. Properly validated tools increase the likelihood of detecting and addressing these issues early in the lifecycle.
  + Accredited tools provide an additional layer of assurance, confirming that the tools meet NASA standards and are appropriate for use in critical environments.

#### **4. Verifies and Validates Mission Readiness**

* **Stress and Boundary Testing**:
  + Tools and simulations are often used to test systems under scenarios that cannot be fully reproduced in physical environments (e.g., extreme space conditions or off-nominal events). Validated tools ensure that boundary and stress testing results are reliable and reflect actual system behavior.
  + For example, thermal, structural, and fault tolerance simulations for spacecraft systems depend on models that provide credible approximations of real-world conditions.

---

### **Why Validation and Accreditation Are Necessary**

1. **Validation:**

   * Validation ensures the tool accurately represents the physical system or software being modeled. It involves comparing the model's outputs to real-world data or experimentation to confirm its functionality and behavior.
   * A validated tool is key to ensuring that simulation-based analyses align with real-world expectations, particularly for mission-critical systems.
2. **Accreditation:**

   * Accreditation is the formal recognition by NASA (or another relevant authority) that a tool is acceptable for its intended purpose. It certifies that the validation evidence meets industry standards and that the tool is appropriate for the specific project, environment, or domain.
   * Accredited tools give stakeholders confidence that the tools have undergone rigorous validation and approval processes, thereby ensuring proper alignment with NASA standards and guidelines (e.g., NASA-STD-8739.8).

---

### **Lessons Learned from NASA and Industry**

* **Failure Due to Invalidation**:

  + Missions have seen failures or delays due to the use of tools that were not formally validated or accredited. For example, inaccurate simulation models can predict incorrect load conditions, leading to faulty design decisions.
  + Lesson Learned: Relying on unvalidated tools introduces **systemic risks**, including errors in software qualification that may propagate into later stages and result in mission failure.
* **Past Successes**:

  + Successful missions such as the **Mars Rover Missions** leveraged validated models and simulations for predictions about landing and surface operations under Mars' specific atmospheric and environmental conditions. The rigor applied in validating these tools contributed to high confidence in mission-critical operations.

---

### **Consequences of Non-Compliance**

If unvalidated or unaccredited tools are used:

1. **Inaccurate Models or Results**:
   * This could lead to incorrect decision-making during qualification testing, allowing systems with latent defects to proceed into operations.
2. **Overly Conservative or Unrealistic Designs**:
   * Erroneous tool outputs could lead to overengineered systems, increasing costs, or underengineered solutions incapable of meeting mission demands.
3. **Increased Risk of Mission Failure**:
   * Flaws undetected due to inaccurate analysis can result in hazardous conditions, mission delays, or total mission failure.
4. **Compliance and Oversight Issues**:
   * A failure to adhere to NASA’s requirements for tool validation and accreditation opens the project to scrutiny during audits, potentially requiring requalification efforts or completely invalidating previous results.

---

### **Supporting NASA Standards and Guidelines**

* **NASA-STD-8739.8 (Software Fault Tolerance)**:
  + Enforces rigorous testing through credible methods, which hinges on using validated tools.
* **NPR 7150.2 (NASA Software Engineering Requirements)**:
  + Addresses the need for thorough software test and validation procedures, including the qualification of flight software.

---

### **Conclusion**

Validated and accredited simulation models and analysis tools offer NASA a means of ensuring that flight software and flight equipment meet the most stringent safety and reliability requirements, essential for mission success. Validation ensures tools produce accurate results, while accreditation ensures those tools have been officially recognized as appropriate for critical qualification processes. By adhering to this requirement, NASA reduces mission risks, protects its investments, ensures compliance with standards, and builds confidence in the qualification of both software and systems.

# 3. Guidance

Models and simulations are essential tools in software engineering, particularly in mission-critical systems such as those at NASA, where they are used for decision-making, system qualification, and predictive analysis. This guidance expands and refines practices for ensuring the correctness and credibility of these tools through proper **validation and verification (V&V)** processes. It also outlines requirements for accrediting models and simulations, including specific considerations for Artificial Intelligence (AI) and Machine Learning (ML) software, ensuring reliable and safe outcomes.

---

### **1. General Guidance for Models, Simulations, and Analyses**

#### **1.1 Potential Sources of Error**

When using models and simulations, there are multiple pathways through which errors can propagate, resulting in incorrect outputs or unsafe decisions. Specifically:

* **Model Inaccuracy**: A model might inadequately represent the scenario being analyzed due to being overly simplified, outdated, or based on incorrect assumptions.
* **Implementation Errors**: The software implementation of the model might contain bugs or inaccuracies (e.g., in algorithms, numerical computation, or data processing).
* **Operational Misuse**: Users operating the modeling software might misapply it, use incorrect input data, or misinterpret outputs.
* **Hardware and Environment Issues**: The hardware or computational environment might introduce variability or errors, such as floating-point arithmetic discrepancies.

#### **1.2 Mitigation Through V&V**

To mitigate these risks:

* **Validate the Model**: Ensure the model solves the correct problem and represents the real-world scenario adequately for its intended use.
* **Verify the Implementation**: Confirm the model was implemented correctly in software according to its design and specification.
* **Calibrate and Train Users**: Ensure operators are trained to use the model/software, understand its limitations, and interpret the results accurately.
* **Utilize Error-Tolerant Hardware**: Account for hardware reliability and computational limits during V&V.

---

### **2. Guidance for AI-ML Software**

Artificial Intelligence (AI) and Machine Learning (ML) introduce unique challenges. These challenges demand special consideration during model development, V&V, and assurance activities:

* **Relevant Topics for AI Software Assurance**:
  + Refer to **Topic 7.25 - Artificial Intelligence and Software Engineering** and **Topic 8.25 - Artificial Intelligence and Software Assurance** for in-depth treatment on designing, developing, and assuring AI-based software.
* **Key Considerations**:
  1. **Explainability and Transparency**: Ensure that AI model outputs are explainable, documented, and not “black boxes.”
  2. **Training Data Validation**: Validate datasets used to train ML models against biases, representativeness, and completeness.
  3. **Validation of Outputs**: Validate AI software predictions and classifications against ground truth data and real-world operations.
  4. **Safety Impact and Non-Determinism**: Design V&V frameworks tailored to accommodate the inherently probabilistic and non-deterministic nature of AI-based systems.

---

### **3. Accrediting Models and Simulations**

Accrediting a model or simulation is the process of assessing its credibility and approving it for a specific use. V&V activities are fundamental to accreditation.

#### **3.1 Key Information to Document for Accreditation**

When accrediting models and simulations, capture the following essential details:

1. **Purpose and Scope of Use**:
   * Clearly define the question(s) to be answered and the specific aspects of the problem that the model or simulation is intended to address.
2. **Impact on Decision-Making**:
   * Document how the model’s results will drive decisions (e.g., qualification of flight systems, hazard analyses, operational safety).
3. **Consequences of Errors in M&S Outputs**:
   * Identify the potential impact of erroneous results on safety, reliability, or mission success to help prioritize the accuracy, validation effort, and scrutiny required.
4. **Known Constraints and Limitations**:
   * Ensure the accuracy and applicability limitations of the model are documented to avoid misuse (e.g., scenarios that the model cannot capture, computational constraints).

1. The question(s) to be answered and the particular aspects of the problem that the M&S will be used to help address.
2. The decisions that will be made are based on the M&S results.
3. The consequences result from erroneous M&S outputs. [175](#_tabs-<p></p>)
4. Be aware of the constraints/limitations of M&S (i.e., what it can and cannot do).

#### **3.2 NASA Standards for V&V in Modeling**

Use the following standards and best practices:

* **NASA-STD-7009**: Provides detailed guidance for V&V of models and simulations, including numerical error analysis and uncertainty quantification.
* **NPR 7150.2**: Governs software engineering requirements, linking processes to modeling V&V.
* **Additional Resources**: Refer to **Topic 7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009**, which provides cross-references for implementing V&V processes effectively.

#### **3.3 Safety-Critical Software Considerations (Class A Software)**

* Pay special attention to all software that affects **safety-critical functionality** or **hazard mitigation** functions. This includes risks of **inadvertent operator actions (HR-33)**. The model or simulation must demonstrate its ability to predict or account for these risks during testing.

---

### **3.4 Verification of Models and Simulations**

Verification confirms that the model or simulation has been implemented correctly and works as intended. Verification activities for models and simulations include:

1. **Document Verification Techniques**:
   * Specify the methods (e.g., code review, analytical methods, comparison against known data) used to verify the model.
2. **Define Verification Conditions**:
   * Outline the scenarios and conditions under which the model was verified (e.g., boundary constraints, operating environments).
3. **Numerical Accuracy Estimates**:
   * Document the quantifiable error estimates of the computational model's results (e.g., floating-point rounding errors, precision limits).
4. **Collect Evidence of Verification Status**:
   * Provide a clear verification status report that is traceable to documented test cases, standards, and acceptance criteria.

Verification Steps

* Document verification techniques and the conditions under which the verification was conducted.
* Document any numerical error estimates for the results of the computational model.
* Document the verification status.

---

### **3.5 Validation of Models and Simulations**

Validation ensures that the model or simulation accurately reflects real-world behavior for its intended purpose. This involves:

1. **Document Validation Techniques**:
   * Provide evidence of methods used to validate the model, such as:
     + Comparison with experimental data.
     + Statistical analysis of deviations from expected outcomes.
     + Real-world testing under controlled conditions.
2. **Specify Validation Conditions**:
   * Record the scenarios, environments, and assumptions under which validation was conducted.
3. **Include Metrics**:
   * Document measurable validation metrics, error margins, and key performance indicators that demonstrate how successfully the model represents reality.
4. **Compile Validation Results**:
   * Record validation outcomes (e.g., pass/fail determinations, reasoning for failures) alongside the validation datasets and studies conducted.

Validation Steps

* Document techniques are used to validate the models and simulations for their intended use.
* Document the conditions under which the validation was conducted.
* Document any validation metrics and any validation data set used.
* Document any studies conducted.
* Document validation results.

### **3.6 Reporting Requirements**

To understand the accuracy and reliability of a model and improve transparency, NASA projects must comply with the reporting requirements of **NASA-STD-7009**. These include:

#### **3.6.1 Required Documentation**

* **Uncertainty Analysis**:
  + Report sources of uncertainty in the model’s results and quantify their potential effects on outcomes.
* **Credibility Assessment**:
  + Assess and report on the credibility of the results, considering the assumptions, constraints, uncertainties, and validation data used.
* **Error Quantification**:
  + Quantify and document both numerical and conceptual errors that can affect the accuracy of outputs.

#### **3.6.2 Reporting Steps (Per NASA-STD-7009 Sections 4.7 and 4.8)**

1. Assess the credibility of the model’s outputs for their intended use.
2. Provide a comprehensive breakdown of all validation and verification activities, including the results, data, and conclusions.
3. Include recommendations for mitigating identified errors, limitations, or constraints.

---

### **3.7 Practical Considerations for Success**

1. **Iterative V&V**:
   * Continuously verify and validate models during software development and refinement to account for changes.
2. **Engage Experts**:
   * Utilize technical experts to collaborate on validation datasets, boundary condition analysis, and worst-case scenario evaluations.
3. **Traceability**:
   * Ensure traceability between the model, its validation, and the software systems it interacts with, maintaining thorough documentation.

---

Understanding the uncertainties affecting the results

Key points:

1. Simulations/emulations must be kept in sync with hardware/software updates
2. Unidentified coding or logic errors in simulators/emulators used by the programs could lead to flight software errors or incorrect flight software.
3. Projects should verify that their simulators/emulators have been tested and validated against flight or flight-like hardware before use.
4. Projects should independently assess the accuracy of simulator/emulator design and timing controls to verify that program-to-program interfaces are correctly documented and support the hazard-cause risk ranking.

### **Conclusion**

Through proper validation, verification, documentation, and reporting processes, the use of models and simulations in software engineering ensures reliable and credible results necessary for safe and successful NASA operations. By integrating the principles outlined in NASA-STD-7009 and NPR 7150.2, along with the specific considerations for safety-critical and AI-ML software, this guidance ensures that potential risks are mitigated, decision-making is supported by accurate data, and mission objectives are achieved efficiently.

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),        * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

Small projects often operate under constrained resources, which makes it important to balance rigor and efficiency in implementing Verification, Validation, and Accreditation (V&V&A) processes. This requirement allows small projects to ease their V&V&A burdens by leveraging models, simulations, and analysis tools that have been previously verified, validated, and accredited by other NASA projects. However, this option requires careful evaluation to ensure the tools remain credible, relevant, and appropriate for the specific use case of the small project. Below is the improved and detailed guidance to support small projects in making informed decisions when utilizing such tools.

---

### **1. Key Considerations When Leveraging Tools Validated by Other Projects**

#### **1.1 Relevance and Applicability of Existing V&V&A**

* **Verify Alignment with Project Needs**:

  + Ensure that the tools were used in a similar manner and for a similar purpose in the prior project. Differences in mission objectives, requirements, system complexity, and operating environments may reduce the relevance of prior V&V&A results.
  + Confirm that the models or simulations were validated against scenarios or data that match your project’s specific use cases.
* **Understand Differences Between Projects**:

  + Compare the system requirements, constraints, and intended use of the tools:
    1. Are the input parameters, operating conditions, and constraints in your project consistent with the prior project’s?
    2. If the requirements or operating conditions differ, assess whether the prior V&V&A covers the required range of scenarios for your project.
* **Check Software Versions and Configurations**:

  + Identify which versions of the models and tools were V&V&A'd in the prior project.
  + Ensure that your project will use the same version or an updated version that retains backward compatibility. Using a new, modified, or untested version may invalidate prior V&V&A results.

---

#### **1.2 V&V Analysis and Documentation**

* **Review V&V Evidence from the Previous Project**:

  + Examine the prior project’s V&V documentation, including test cases, scenarios, and accreditation reports. Ensure these artifacts are available and comprehensible.
  + Verify the credibility of the evidence and confirm the thoroughness of the prior project’s V&V&A activities.
* **Reassess the Results for Your Context**:

  + Evaluate whether the prior project’s V&V results are adequate for your project’s context. Identify gaps or areas where additional testing or validation may be necessary.
  + If uncertainties remain, conduct supplementary V&V activities to fill gaps or address changes in operational requirements.
* **Document Assumptions, Risks, and Limitations**:

  + Record any assumptions about the relevance of the previous project's V&V&A, as well as differences between projects.
  + Document potential risks of relying on these results and include mitigation strategies.
  + Ensure all constraints and limitations of the models and tools are documented and understood by the team.

---

### **2. Maintenance and Management of Tools**

Even when leveraging prior V&V&A'd tools, proper maintenance and management of these tools remain critical to their reliability and effectiveness.

#### **2.1 Configuration Management**

* **Maintain Up-to-Date Models and Tools**:

  + Ensure that the models, simulations, and tools are regularly updated to reflect the latest requirements and design changes.
  + Incorporate all approved changes into configuration-controlled software repositories.
* **Track Tool Configurations**:

  + Maintain accurate records of the specific configurations and settings used for analyses, especially when reusing tools from prior projects.

#### **2.2 Input Integrity**

* **Review and Validate Model Inputs**:
  + Confirm that inputs to the models are accurate, complete, and relevant for the project’s use cases.
  + Ensure input parameters (e.g., operational data, environmental conditions) have been reviewed and validated by domain experts.

---

### **3. Evaluating Models, Simulations, and Test Environments**

When using tools to design, develop, analyze, test, or maintain software systems, the following considerations are essential:

#### **3.1 Tool Use and Scope**

* **Ensure Fidelity of the Models**:

  + Confirm that the level of fidelity and completeness of the models is sufficient to support the intended analyses or tests (e.g., simulations must match real-world operational conditions at the appropriate level of detail).
* **Define Operational Boundaries**:

  + Explicitly define and document the operational parameters, boundaries, and capabilities of the models, simulations, and tools.

#### **3.2 Risk Management**

* **Identify and Address Risks**:
  + Proactively document any risks, concerns, or issues arising from tool limitations, assumptions, or constraints. Feed these risks into the project’s risk management system.
  + Resolve identified risks before critical testing or qualification milestones.

---

### **4. Additional Tool-Specific Steps**

#### **4.1 Purchased Tools and Licenses**

* **Up-to-Date Tools and Licenses**:
  + Ensure all purchased tools are operating under valid and up-to-date licenses.
  + Confirm that the tool deliverables (e.g., results, outputs) meet quality expectations and contractual requirements.

#### **4.2 Operating Tools Within Parameters**

* **Avoid Operation Outside Limits**:
  + Ensure that models, tools, or simulations are only used within their validated bounds, as documented in their user and V&V guides.
  + If you need to operate outside these limits, document the risks and develop mitigation plans.

#### **4.3 Output Validation**

* **Interpret and Verify Results**:
  + Review simulation outputs or test results to ensure they align with expectations or can be appropriately explained.
  + If unexpected results occur, investigate the cause and assess whether adjustments or recalibrations are required.

---

### **5. Reporting and Documentation**

Proper documentation and reporting are critical when using or reusing tools, ensuring that stakeholders have full visibility into the tool’s trustworthiness.

#### **5.1 Limitations and Uncertainties**

* **Limitations of Tools**:

  + Provide a clear report on the limits of the tools and models, including:
    - The scenarios under which the tools are valid.
    - Their fidelity level (e.g., how closely they mimic real-world systems).
  + Include documentation of any operational limitations or boundaries.
* **Trust and Uncertainty Analysis**:

  + Report on the credibility of the results derived from the models, including:
    - Any assumptions made during the process.
    - The level of certainty/trust in outcomes based on V&V documentation.

#### **5.2 Comprehensive Documentation**

* **Provide a History of Use**:
  + Document the history of tools, including their use by prior projects, along with all associated V&V activities, results, and limitations.
* **Results and Issues**:
  + Record results from tool use in the current project, analyzing their accuracy and completeness relative to system requirements.
  + Document any issues, deviations, or risks identified during tool operations and the resolution paths taken.

---

### **6. Summary of Best Practices for Small Projects**

1. **Review Relevance**: Ensure tools and their V&V&A results are relevant and appropriate for your project’s objectives.
2. **Update and Manage**: Maintain configuration control of tools and their updates, validating their inputs and outputs.
3. **Assess Risks**: Identify and mitigate risks associated with tool limitations, assumptions, or differences between projects.
4. **Report Transparently**: Provide clear documentation on the credibility, limitations, and uncertainties of results from reused tools.
5. **Follow Standards**: Align all processes with recognized NASA standards (e.g., NASA-STD-7009, NPR 7150.2).

By carefully considering these factors, small projects can effectively leverage existing V&V&A’d tools while maintaining rigor and reducing unnecessary costs and effort. This approach supports the successful delivery of high-quality software systems within resource constraints.

Key Points

1. Simulations/emulations must be kept in sync with hardware/software updates
2. Unidentified coding or logic errors in simulators/emulators used by the programs could lead to flight software errors or incorrect flight software.
3. Projects should verify that their simulators/emulators have been tested and validated against flight or flight-like hardware before use.
4. Projects should independently assess the accuracy of simulator/emulator design and timing controls to verify that program-to-program interfaces are correctly documented and support the hazard-cause risk ranking.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-175)

  [Department of Defense Standard Practice Documentation of Verification and Validation and Accreditation (VV&A) For Models and Simulations,](http://www.everyspec.com/MIL-STD/MIL-STD+%283000+-+9999%29/download.php?spec=MIL-STD-3022.028058.pdf "Click to open in new window")

  Department of Defense, MIL-STD-3022, 2008.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-272)

  [NASA Standard for Models and Simulations,](https://standards.nasa.gov/standard/nasa/nasa-std-7009 "Click to open in new window")

  NASA-STD-7009A w/ CHANGE 1: ADMINISTRATIVE/ EDITORIAL CHANGES 2016-12-07
* (SWEREF-623)

  [How to Perform Credible Verification,Validation, and Accreditation for Modeling and Simulation](https://pdfs.semanticscholar.org/c76f/f966a1c00696c39bd476a6e657f7a24f7468.pdf "Click to open in new window")

  Cook, Dr. David A. ; Skinner, Dr. James M.; The AEgis Technologies Group, Inc.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Leveraging past NASA projects and lessons learned, the importance of validation and accreditation is highlighted by several historical challenges and successes. Below are relevant lessons learned from NASA’s expansive history, emphasizing the need for thoroughly validated and accredited tools, models, and simulations.

---

### **1. Mars Climate Orbiter Mishap (1999)**

**Lesson Learned:** Inadequate validation and understanding of models’ assumptions and outputs can lead to mission failure.

* **Context:**

  + The Mars Climate Orbiter failed due to a navigation error caused by a mismatch of measurement units between software systems (imperial vs. metric).
  + The lack of validation and cross-checking of models and their inputs led to discrepancies in the trajectory analysis.
* **Relevance to Requirement 4.5.6:**

  + Software models and tools must be validated against the expected parameters and verified for compatibility across teams, projects, and systems.
  + Accreditation processes should specifically evaluate whether models can reliably operate in mixed-unit or otherwise constrained environments.
  + Ensures inputs and assumptions used in models are consistent, traceable, and validated to avoid misalignment.

---

### **2. Genesis Mission Mishap (2004)**

**Lesson Learned:** Incorrect assumptions in simulations or analysis tools must be identified during V&V, particularly when they influence flight-critical systems.

* **Context:**

  + The Genesis mission returned to Earth with a parachute system that failed to properly deploy, leading to the damage of the payload upon impact.
  + Root cause analysis uncovered that the design was based on simulations and models where the orientation of key sensors was assumed incorrectly.
* **Relevance to Requirement 4.5.6:**

  + Models, simulations, and tools used to design and analyze safety-critical features (e.g., the parachute deployment system) must undergo thorough verification for realistic and mission-specific conditions.
  + Validation activities should ensure that assumptions in the model align with operational reality, and discrepancies must be documented and resolved during the qualification process.

---

### **3. Space Shuttle Challenger Tragedy (1986)**

**Lesson Learned:** Failure to properly document, review, and address simulation limitations can produce catastrophic results.

* **Context:**

  + Constraints and flaws in thermal and structural analysis models failed to predict the effects of low temperatures on the Shuttle's O-ring materials, contributing to the Challenger disaster.
  + While tools were available for thermal analysis, inadequate V&V and an incomplete understanding of operational boundaries failed to uncover the vulnerabilities of the O-rings during launch.
* **Relevance to Requirement 4.5.6:**

  + Models and simulations must be validated for all operational conditions, not just nominal ones. This includes stress testing to identify edge cases and sensitivity analyses to uncover vulnerabilities under varying conditions (like extreme temperatures).
  + Simulation tools must include proper uncertainty and sensitivity analyses and require clear documentation of limitations and decision-making based on their outputs.

---

### **4. Ares I-X Development: Simulating Launch Dynamics**

**Lesson Learned:** Validating simulation models is crucial for predicting complex, interdependent system behaviors.

* **Context:**

  + During the Ares I-X test flight, the accuracy of the models and simulations used to predict flight dynamics was validated and verified through extensive processes that included comparison with wind tunnel results and legacy data from similar systems.
  + The project successfully used accredited tools for aeroacoustic modeling and flight dynamics analysis, ensuring that the launch vehicle would perform safely and reliably.
* **Relevance to Requirement 4.5.6:**

  + Successes in projects like Ares I-X highlight the importance of V&V processes ensuring that simulations provide reliable predictions when modeling highly integrated and dynamic systems.
  + Such rigorous validation builds confidence in the tools’ ability to predict system behaviors under real-world operating conditions.

---

### **5. Mars Science Laboratory (MSL) "Curiosity" Rover (2012)**

**Lesson Learned:** V&V of high-fidelity models is pivotal when complex, multi-step operations depend on simulated system results.

* **Context:**

  + The Entry, Descent, and Landing (EDL) phase of MSL was designed using high-fidelity simulations and models validated against Earth-based tests.
  + Simulations of parachute deployment, atmospheric entry, and “sky crane” operations were extensively validated using real-world test data and accredited against expected conditions on Mars.
  + Successful landing validated the predictive accuracy of the models.
* **Relevance to Requirement 4.5.6:**

  + Critical mission phases that rely on the interplay of multiple systems (e.g., EDL) demand rigorous validation of models and simulations. Accredited tools must be tested for fidelity, accuracy, and alignment with real-world scenarios.
  + Demonstrates how reliance on high-fidelity validated tools reduces mission risk and ensures successful outcomes, even in complex operational environments.

---

### **6. James Webb Space Telescope (JWST) Mirror Deployment**

**Lesson Learned:** Rigorous validation and sensitivity testing of models ensure mission-critical operations perform as designed.

* **Context:**

  + The James Webb Space Telescope’s complex mirror deployment process was painstakingly modeled and simulated to ensure it would work in the low-gravity, cold-space environment.
  + The simulations accounted for material properties, thermal conditions, and mechanical behaviors, all of which were verified against extensive ground testing.
* **Relevance to Requirement 4.5.6:**

  + Models driving safety- and mission-critical deployment operations must undergo exhaustive validation for operational and environmental compatibility.
  + Sensitivity and uncertainty analyses should account for factors like material deformations, temperature variances, and mechanical stresses, ensuring operational success in space.

---

### **7. Software Models for Orbital Maneuvers – International Space Station (ISS)**

**Lesson Learned:** Regular updates and re-verification of reused models are essential to maintain their reliability for ongoing projects.

* **Context:**

  + The ISS implemented models for predicting orbital maneuvers and avoiding potential collisions with orbital debris. Over time, these models required updates to account for changes in debris density and trajectories, as well as updates to station systems.
  + Failure to update, validate, and re-accredit these models could have resulted in inaccurate predictions and potential collisions.
* **Relevance to Requirement 4.5.6:**

  + Models and tools must be continuously updated and re-validated when used in evolving or persistent operational environments like the ISS.
  + This ensures relevance and avoids reliance on outdated models or simulations that no longer adequately predict current operational conditions.

---

### **8.** Lessons Learned: In Class D, Fault Protection Becomes the Safety Net—So It Must Be Excellent

**Problem/Observation:**  
Class D missions accept higher hardware and redundancy risk, which places greater reliance on software‑based fault protection (FP). The Anomaly Review Board (ARB) emphasized that FP must be robust enough to compensate for these elevated risks. For LTB, several FP weaknesses emerged that limited the system’s ability to autonomously protect itself.

**ARB Context:**  
The ARB explicitly stated:  
“On a Class D mission that assumes risk, ensure that the safety net of fault protection can adequately mitigate some of the risks.”

**Contributing Factors:**  
• Incorrect or insufficiently validated FP thresholds.  
• Fault protection logic split across multiple authorities and implementation paths.  
• Sequence‑based safing behaviors and FSW‑based safing behaviors were never tested together end‑to‑end.  
• Missing telemetry limited situational awareness and inhibited on‑orbit diagnosis.  
• Reset behavior and recovery paths were not fully characterized or validated.

**Resulting Impacts:**  
The spacecraft’s ability to safely respond to anomalies was compromised. Fragmented FP design, incomplete testing, and unclear behavior under reset conditions reduced system resilience during off‑nominal events.

**Relevant SWEHB Guidance:**  
Core SWEHB requirements remain applicable even when tailored for Class D:  
• SWE‑057 (Software Architecture) requires the design and documentation of fault management behavior.  
• SWE‑050, SWE‑051, and SWE‑055 require verifiable, traceable FP‑related requirements and logic.  
• SWE‑070 and SWE‑073 require modeling, simulation, and end‑to‑end testing to validate FP behavior under nominal and off‑nominal conditions.

**Lesson Learned:**  
Class D missions rely disproportionately on software fault protection because hardware redundancy is limited. For this reason, FP must be designed, validated, and tested with exceptional rigor. Software fault protection is a mission‑critical system—not an optional enhancement—and must be treated as such from architecture through ATLO and operations.

### **Key Takeaways from Lessons Learned**

1. **Validation of Models is Mission Critical**:

   * All models must reflect real-world scenarios, accounting for variations in environmental, operational, and system-specific conditions.
2. **Traceability to Real Data is Vital**:

   * Models must be validated against actual test results, known data, or experimental outcomes to ensure fidelity.
3. **Document and Understand Limitations**:

   * Limitations of models and simulations must be clearly documented, with measures in place to ensure risks are identified and mitigated.
4. **Reuse Requires Caution**:

   * Reusing previously validated tools necessitates confirming their applicability to the current context, including system, environment, and operational changes.
5. **Continuous V&V for Long-Term Use**:

   * Tools used for extended purposes should undergo periodic re-validation and updates to account for changes in assumptions, inputs, and environments.
6. **Integration Testing Should Be Modeled**:

   * Models must integrate well with other systems, ensuring end-to-end validation of all operational steps and scenarios.

These lessons emphasize the critical importance of NASA’s Requirement 4.5.6 and highlight why validation, verification, and accreditation of models and simulations remain fundamental to mission success.

## 6.2 Other Lessons Learned

* Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009), and NASA-STD-7009[272](#_tabs-<p></p>), includes lessons learned for the verification and validation of models and simulations.
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

  + [Software Requirement Sell-Off Expedience](https://software.gsfc.nasa.gov/lesson-details/177/). **Lesson Number 177**: The recommendation states: "As early as feasible in the program (EPR-CDR time frame) ensure that the project will be provided with all relevant test articles well in advance of the test’s run-for-record (will likely require NASA Program Management buy-in as well). This will allow the time necessary for: review of requirement test coverage, accumulation of all comments (especially if IV&V are supporting the program), and vendor disposition of all comments to project satisfaction. In this manner, when test artifacts from the FQT run-for-record are provided for requirement sell-off, the Flight Software SME will have a high level of confidence in the artifacts provided (knowing how each requirement has been tested) to expedite the sign-off process. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
  + [Going Beyond the Formal Qualification Test (FQT) Scripts: Data Reduction/Automation](https://software.gsfc.nasa.gov/lesson-details/295/).**Lesson Number 295**: The recommendation states: "As early as feasible in the program (pre-FQT time frame), ascertain whether automated testing is planned for Software FQT and ensure that the vendor will provide all relevant test articles well in advance of test run-for-record (will likely require NASA Program Management buy in and support as well). Identify any calls to open up additional views to EGSE, Simulators, raw hex dumps, etc., that may be used to assist with data analysis/processing/reduction in the scripts. Request clarification on how data captured in those views will be used and have snapshots provided (or travel to vendor site) to fully understand verification extent. For automated testing, the Software Systems Engineer should evaluate whether the provider has allocated sufficient time and training to fully understand how the automated testing program will exercise and verify all required functions and behaviors. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."

# 7. Software Assurance

**SWE-070 - Models, Simulations, Tools**

4.5.6 The project manager shall use validated and accredited software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the software models, simulations, and analysis tools used to achieve the qualification of flight software or flight equipment have been validated and accredited.

## 7.2 Software Assurance Products

This guidance supports **Software Assurance (SA)** activities for validating and accrediting software models, simulations, and analysis tools used in the qualification of flight software and flight equipment. It emphasizes the importance of ensuring the reliability, credibility, and safety of these tools, which are critical for mission success and risk reduction. Enhanced clarity, steps, and examples are provided for Software Assurance professionals to ensure compliance with NASA’s standards.

#### **Deliverables to Support this Requirement:**

1. **Validation and Accreditation Report:**
   * Evidence of validation and accreditation (V&V and certification process) for the models, simulations, and analysis tools used in the qualification of flight software and flight equipment.
2. **Verification Results:**
   * Software test reports, test logs, and discrepancy records demonstrating the performance and reliability of models, simulations, and analysis tools.
3. **Compliance Assessment:**
   * Documentation of the use of **NASA-STD-7009**, ensuring the processes adhere to the standard for the accreditation of models and simulations.

## 7.3 Software Assurance Metrics

These metrics focus on monitoring the fidelity, completeness, and accuracy of validation and verification efforts for the models, simulations, and tools.

#### **1.1 Validation/Verification Coverage**

* **Metric:** Percentage of validation/verification activities completed vs. planned.
  + Description: Tracks the proportion of validation and verification tasks that have been successfully performed for each model, simulation, or tool.
  + Formula: [(Completed V&V Activities / Planned V&V Activities) × 100]
  + Purpose: Ensures adequate progress toward completing V&V processes and identifies resource gaps.

#### **1.2 Tool Accuracy and Reliability**

* **Metric:** Frequency of discrepancies/errors discovered during verification.
  + Description: Number of errors or discrepancies identified during tool verification that could impact the qualification process.
  + Example:
    - Minor errors resolved during testing.
    - Severe issues affecting result credibility (e.g., incorrect calculations, inaccurate boundaries).
  + Purpose: Measures the reliability of tools and tracks the effectiveness of the verification process.

#### **1.3 Model Fidelity**

* **Metric:** Level of fidelity of the models/simulations used vs. requirements.
  + Description: Monitors whether the models meet the required fidelity and complexity for the qualification task (e.g., high-fidelity trajectory simulations, environmental condition analysis).
  + Purpose: Ensures models are sufficient to meet qualification requirements and do not compromise testing accuracy.

---

### **2. Accreditation Metrics**

These metrics monitor compliance with accreditation standards and processes for software models, simulations, and tools.

#### **2.1 Accreditation Status**

* **Metric:** Percentage of models, simulations, and tools accredited.
  + Description: Tracks the accreditation progress for all tools used in flight software/equipment qualification.
  + Formula: [(Number of Accredited Tools / Total Tools Used) × 100]
  + Purpose: Confirms that tools meet NASA’s accreditation criteria (e.g., per **NASA-STD-7009**) and are officially approved for use.

#### **2.2 Tools Not Accredited**

* **Metric:** Number of tools not accredited or deemed non-compliant.
  + Description: Identifies tools in the qualification process that lack accreditation or failed to meet accreditation standards.
  + Purpose: Drives corrective action by flagging unvalidated and non-accredited tools, reducing risks tied to incorrect analyses and decisions.

---

### **3. Risk and Non-Conformance Metrics**

These metrics monitor risk levels and track issues that arise from tool use, ensuring mitigation strategies are employed.

#### **3.1 Risk Identification**

* **Metric:** Number of risks identified in models, simulations, and tools.
  + Description: Tracks risks, such as operating models outside their boundaries, invalid inputs, or outdated tools.
  + Purpose: Provides a measure of risk awareness and documentation related to tool limitations.

#### **3.2 Non-Conformance Metrics**

* **Metric:** Count of non-conformances found in models, simulations, tools.
  + Description: Captures the number of:
    - Open non-conformance issues.
    - Closed non-conformance issues.
    - Categorized by severity (Low, Medium, High).
  + Example: Incorrect assumptions, missing calibration, faulty logic.
  + Purpose: Monitors the timely identification and resolution of non-conformance issues.

#### **3.3 Risk Resolution Timeliness**

* **Metric:** Time taken to address tool-related risks or non-conformances.
  + Formula: [(Risk/Open Non-Conformance Discovery Date - Resolution Date)]
  + Purpose: Ensures that identified risks and non-conformance issues are managed efficiently and do not delay project milestones.

---

### **4. Calibration Metrics (If Applicable)**

For tools requiring calibration (e.g., simulators, measurement devices), these metrics track compliance and reliability in their calibration status.

#### **4.1 Calibration Compliance Rate**

* **Metric:** Percentage of tools calibrated before use.
  + Formula: [(Number of Tools Calibrated / Total Number of Applicable Tools) × 100]
  + Purpose: Ensures all tools are calibrated and compliant before qualification testing.

#### **4.2 Out-of-Calibration Instances**

* **Metric:** Number of tools found to be out of calibration during testing.
  + Description: Measures the frequency of tools or models discovered to be miscalibrated or expired, potentially disrupting testing.
  + Purpose: Highlights gaps in calibration practices and promotes preventive measures (e.g., proactive calibration scheduling).

---

### **5. Operational Metrics**

These metrics monitor how well the tools are being used within their limitations and parameters.

#### **5.1 Usage Within Operational Parameters**

* **Metric:** Percentage of tools operated within their validated boundaries or limitations.
  + Formula: [(Number of Tools Operated Within Limits / Total Tools Used) × 100]
  + Purpose: Ensures tools are not used outside their validated scope, reducing the risk of erroneous outputs.

#### **5.2 Anomalous Results**

* **Metric:** Number of unexpected or unexplained outputs from tools.
  + Description: Tracks anomalies generated by tools during flight software/equipment qualification processes.
  + Example: Numerical instabilities, unrealistic boundary behaviors.
  + Purpose: Identifies tool deficiencies and escalates reassessment needs.

---

### **6. Reporting and Documentation Metrics**

These metrics track the completeness and quality of documentation related to the validation, accreditation, and qualification process.

#### **6.1 Documentation Completeness**

* **Metric:** Percentage of required documentation completed for each tool.
  + Formula: [(Completed Documentation Items / Total Documentation Requirements) × 100]
  + Purpose: Ensures that all necessary reports (e.g., validation reports, accreditation certificates, usage limitations documents) are provided.

#### **6.2 Compliance with Standards**

* **Metric:** Percentage of tools/documents compliant with NASA-STD-7009 and NPR 7150.2.
  + Description: Tracks whether tools meet NASA standards for models, simulations, and software engineering.
  + Purpose: Monitors adherence to industry best practices and ensures traceability to certification requirements.

---

### **7. Outcome Metrics**

These metrics measure the overall effectiveness of tool use and their contributions to the qualification process.

#### **7.1 Qualification Success Rate**

* **Metric:** Percentage of flight software/equipment qualification results successfully supported by models and tools.
  + Formula: [(Successful Qualification Results Supported by Tools / Total Qualification Results Supported) × 100]
  + Purpose: Tracks how effectively tools are contributing to mission-critical validation activities.

#### **7.2 Confidence in Results**

* **Metric:** Percentage of confidence in tool-generated outputs based on validation records.
  + Description: Measures analyst/reviewer confidence using factors like error rates, validation accuracy, and test coverage.
  + Example: High-confidence metrics imply tools are highly reliable for use in mission-critical decisions.
  + Purpose: Ensures that tools’ outputs are credible for decision-making.

---

### **Summary of Metrics Usage**

Metrics for this requirement serve multiple purposes:

1. **Monitor Validation and Accreditation Progress**: Confirm that tools meet project-specific quality thresholds for qualification.
2. **Track Risks and Corrective Actions**: Raise awareness of tool-related risks and ensure timely resolutions.
3. **Ensure Compliance**: Validate adherence to NASA standards and ensure use of properly calibrated and configuration-managed tools.
4. **Improve Tool Performance**: Capture data about operational efficiency, fidelity, and reliability.

Using these metrics, Software Assurance professionals can proactively identify gaps, ensure compliance, mitigate risks, and validate the overall quality of tools supporting flight software/equipment qualification processes

1. **Number of Non-Conformances:**
   * Track and categorize the number of non-conformances associated with models, simulations, and tools (e.g., Open, Closed, Severity).
   * Analyze trends to identify systemic issues in tool validation and usage.
2. **Tool Reliability Data:**
   * Provide metrics on defect-detection rates during testing, resolution timeframes, and overall impact on the system.

---

## 7.4 Software Assurance Guidance

#### **Task 1: Validating and Accrediting Software Models, Simulations, and Tools**

Software Assurance (SA) must verify that the project’s software models, simulations, and analysis tools used for qualification have been validated and properly accredited. Accreditation ensures that these tools:

* Have been **reviewed, tested, and certified for their intended use**.
* Are suitable for producing results on which critical decisions (e.g., hazard identification, safety qualification, or mission-critical operations) are based.

##### **Steps for SA to Perform Tool and Model V&V:**

1. **Gather a Comprehensive List:**

   * Obtain a full inventory of models, simulations, and analysis tools being used in the qualification of the flight software or flight equipment.
   * Ensure this inventory includes both physical tools (e.g., compilers, code generation tools) and software tools (e.g., emulators, simulators, linked libraries).
2. **Trace Validation and Accreditation:**

   * Confirm that each tool has undergone **dedicated V&V processes** and that documentation exists describing:
     + How the tool was verified (e.g., analysis methods, test campaigns, boundary tests).
     + The conditions of validation (e.g., real-world scenarios, operating environments).
     + Accreditation approval for the tool’s intended use during the qualification phase.
   * Verify that **NASA-STD-7009** guidelines were followed during the accreditation effort.
3. **Assess Prior Use:**

   * If tools or models have been used on previous NASA projects, confirm their **relevance and applicability** to the current project:
     + Evaluate if the specific versions of these tools were validated for analogous use cases.
     + Assess whether differences in project requirements (e.g., mission-specific constraints, environments) necessitate re-validation or supplemental V&V activities.
4. **Review Test Results and Outcomes for V&V Adequacy:**

   * Validate the **test results** for these tools, specifically reviewing:
     + Non-conformance reports tied to tool behavior.
     + Evidence that failing test cases have been addressed and re-tested successfully.
     + The fidelity and completeness of test scenarios to reflect operational conditions.
5. **Document and Report Results:**

   * Provide evidence of validation and accreditation, including:
     + Reports on the **limitations, updates, and assumptions** associated with each tool.
     + An analysis of the risks associated with tool failure, along with mitigation efforts.

##### **Examples of Tools to Validate and Accredit:**

* **Development and Build Tools:**
  + Compilers, code-coverage tools, coding/debugging environments, and linked libraries.
* **Simulations and Analysis Platforms:**
  + Emulators, trajectory analysis tools, fault injection tools, thermal/environmental simulation models.
* **Test Equipment or Frameworks:**
  + Tools for automated testing, memory analyzers, and hardware-in-loop (HIL) systems.

---

#### **Task 2: Calibration of Tools and Equipment**

For tools (software or physical) that require calibration before use (e.g., simulators, environmental sensors, or measurement devices), SA must confirm they have been properly calibrated.

##### **Steps to Validate Calibration:**

1. **Check Calibration Records:**

   * Verify the **calibration tag** to ensure calibration is current. Tags must indicate:
     + The date of the most recent calibration.
     + The expiration date for calibration and when recalibration is required.
   * Tools or devices found to be **out of calibration** should be flagged immediately, and SA should alert the test director or project manager.
2. **Assess Impact on Testing and Qualification:**

   * Determine whether the calibration error could impact test results or invalidate prior analysis. If so:
     + Require recalibration, followed by re-execution of affected tests or analyses.
     + Recommend delaying qualification milestones until calibration issues are resolved.

---

#### **Special Considerations for Safety-Critical Tools:**

For software tools and models that directly impact system safety:

1. Analyze the potential consequences of **tool errors**:
   * Assess the severity and probability of an incorrect output affecting system safety.
   * Use this analysis to prioritize mitigation measures.
2. Ensure strict oversight to verify that tools are:
   * Operated within their certified boundaries or conditions.
   * Documented properly if used outside known operating limits, with risks added to the project’s **risk management system**.

---

### **Additional Validation Points:**

For all models, simulations, and tools involved in the qualification process, confirm:

1. **Models:**
   * Are kept up to date, **configuration managed**, and evolve alongside project requirements.
   * Faithfully incorporate all system requirements, constraints, and design features.
   * Are testable, properly tested, and include results validation.
2. **General Tools:**
   * Use the latest and properly licensed versions.
   * Align with fidelity requirements sufficient to determine correctness of requirements and functionality.

---

### **Task 3: Monitoring and Mitigating Risks**

1. **Record and Resolve Concerns or Risks:**

   * Any concerns regarding tools, models, or simulations (e.g., assumptions, outdated calibration or versions, boundary limitations) must be documented.
   * Input these risks into the risk management process, paired with mitigation strategies.
2. **Analyze Uncertainty and Output Credibility:**

   * Assess whether tool results:
     + Match expected benchmarks or real-world data.
     + Can be explained and traced back to validated inputs or assumptions.
3. **Report on Tools, Limits, and Outcomes:**

   * Create reports that summarize:
     + The results of V&V activities.
     + Assumptions, constraints, and operating limits of tools.
     + The level of certainty/trust in outputs and an analysis of any risks or deviations.

---

### **Conclusion**

Software Assurance plays a critical role in confirming the reliability of models, simulations, and tools by ensuring their validation, accreditation, and proper application. This guidance emphasizes:

1. Rigorous V&V and calibration.
2. Traceability to standards like **NASA-STD-7009**.
3. Risk-based prioritization for critical tools. Through careful adherence to these practices, SA helps mitigate risks, improve qualification outcomes, and ensure mission success.

Key points:

1. Simulations/emulations must be kept in sync with hardware/software updates
2. Unidentified coding or logic errors in simulators/emulators used by the programs could lead to flight software errors or incorrect flight software.
3. Projects should verify that their simulators/emulators have been tested and validated against fight-or-flight-like hardware before use.
4. Projects should independently assess the accuracy of simulator/emulator design and timing controls to verify that program-to-program interfaces are correctly documented and support the hazard-cause risk ranking.

For auto-generated code see Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code).

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),        * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) |

# 8. Objective Evidence

Objective Evidence

Objective evidence serves to demonstrate compliance with this requirement by documenting that the software models, simulations, and analysis tools used for flight software and equipment qualification have been properly validated, verified, accredited, and used within their approved scope. Below is a detailed list of the types of objective evidence that should be collected and maintained to satisfy this requirement.

---

### **1. Documentation of Validation, Verification, and Accreditation Processes**

* **Validation Reports:**

  + Evidence demonstrating that the software models, simulations, and analysis tools accurately represent the intended real-world system, use cases, or phenomena under expected operational conditions.
  + Includes:
    - Description of validation activities (e.g., test cases, boundary conditions, assumptions).
    - Results of validation metrics and comparisons to actual physical/experimental data.
    - Evidence of repeatability or reproducibility of results.
* **Verification Reports:**

  + Evidence demonstrating that the models, tools, and simulations were properly implemented and function as intended.
  + Includes:
    - Peer review results or code walkthroughs for software modeling implementations.
    - Test results documenting successful execution of functionality against requirements.
    - Error logs for issues found and resolved during verification processes.
* **Accreditation Certificates:**

  + Documentation of formal accreditation indicating that the tools, simulations, and models have been reviewed and have met the necessary criteria for their specific use.
  + Includes:
    - Signed accreditation approvals from project authorities or certification boards.
    - Lists of the specific conditions and scenarios under which the tools are accredited.

---

### **2. Inventory of Validated and Accredited Tools**

* **Tool Inventory:**

  + A comprehensive list of all software models, simulations, and tools used in the qualification process, tracked by:
    - Tool name/version number.
    - Validation and verification status.
    - Accreditation status and approval date.
    - Calibration records (if applicable).
* **Version Control Records:**

  + Evidence that the models, simulations, and tools used during the qualification process are properly configuration managed and are the approved versions.

---

### **3. Testing and Calibration Records**

* **Test Results for Qualification Tools:**

  + Evidence from testing models, simulations, and tools to ensure they meet intended functionality and correctness.
  + Includes:
    - Completed test procedures, test logs, and pass/fail status for the tool certification lifecycle.
    - Stress and edge-case testing to validate the behavior of models under extreme conditions.
* **Tool Calibration Records:**

  + Evidence showing tools were properly calibrated before use, if applicable.
  + Includes:
    - Calibration tags indicating the last calibration date and expiration.
    - Reports on recalibration activities or replacement of tools.

---

### **4. Approval Records**

* **Usage Approval Memo:**

  + Documentation showing the project manager or responsible authority has formally approved the use of the validated and accredited tools for qualification activities.
* **Meeting Minutes or Review Records:**

  + Records from project reviews, audits, or meetings where validation, verification, and accreditation results were presented and accepted.

---

### **5. Risk Management Evidence**

* **Risk Assessments:**

  + Evidence showing the evaluation of risks associated with using models, simulations, and tools for flight software qualification.
  + Includes:
    - Analysis of risks tied to tool limitations, assumptions, or incorrect outputs.
    - Documentation of mitigations applied to reduce risks (e.g., supplemental verification or validation).
* **Limitations Documentation:**

  + Evidence showing that constraints, limitations, or operational boundaries for the tools were identified, documented, and reviewed during system qualification.

---

### **6. Compliance with NASA Standards**

* **Adherence to NASA-STD-7009:**

  + Records demonstrating that the validation, verification, and accreditation processes followed the practices outlined in **NASA-STD-7009, Standard for Models and Simulations**.
  + Includes:
    - Identification of methods used for uncertainty analysis, sensitivity analysis, and numerical accuracy assessments.
    - Traceability to standard guidelines and requirements.
* **Compliance with NPR 7150.2:**

  + Evidence showing that the models, simulations, and tools meet requirements prescribed in **NPR 7150.2** for software engineering processes and assurance.

---

### **7. Operational Evidence**

* **Testing Environment Records:**

  + Evidence showing the tools were used within their specified operational conditions or parameters.
  + Includes:
    - Reports on how the tools were employed in test environments (e.g., trajectory simulations, hardware-in-the-loop testing).
    - Verification that the tools operated within approved limits and did not exceed known boundaries.
* **Output Analysis Reports:**

  + Evidence demonstrating that the outputs/results generated by the models, simulations, or tools were consistent, credible, and explainable.
  + Includes:
    - Comparative analysis reports detailing correlation between simulated results and measured real-world data.
    - Anomalies or discrepancies logged and resolved.

---

### **8. Traceability Evidence**

* **Requirements Traceability Matrix (RTM):**

  + Evidence linking tools to specific system requirements they were used to validate or verify during qualification.
* **Documentation of Input Integrity:**

  + Evidence showing that input data used in the models (e.g., initial conditions, environmental variables, constraints) were accurate, complete, and reviewed for correctness.

---

### **9. Audit and Review Evidence**

* **Independent Audits or Assessments:**

  + Documentation from internal or external auditors confirming the validity and accreditation status of the tools used for qualification testing.
* **Lessons Learned Documentation:**

  + Records illustrating what challenges were encountered and resolved during V&V of models, simulations, or tools.

---

### **10. Reporting Evidence**

* **Reports on Limits, Functionality, and Results:**

  + Comprehensive reporting that summarizes:
    - The scope (intended use, capabilities, constraints) of each tool.
    - Metrics and statistical confidence levels for tool-generated results.
    - Identified risks and mitigation steps.
* **Certification Reports:**

  + Final reports certifying the qualification success driven by simulations, models, and tools, showing how their outputs contributed to decisions, risk reductions, or verifications.

---

### **Summary**

Objective evidence for Requirement 4.5.6 provides a clear, traceable, and documented path from the validation and accreditation of tools to their direct use in the qualification of flight software or flight equipment. Collecting and maintaining this evidence ensures compliance with standards like **NASA-STD-7009** and supports critical decision-making by reducing risks associated with relying on unvalidated or non-accredited tools.

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
