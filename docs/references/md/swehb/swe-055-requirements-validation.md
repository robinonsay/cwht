# SWE-055 - Requirements Validation

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695440. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation

SWE-055 - Requirements Validation

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695440)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695440&showCommentArea=true&showComments=true#addcomment)

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

4.1.7 The project manager shall perform requirements validation to ensure that the software will perform as intended in the customer environment. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-055 History

SWE-055 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.1.2.3 The project shall perform requirements validation to ensure that the software will perform as intended in the customer environment. |
| Difference between A and B | No change |
| B | 4.1.3.3 The project manager shall perform requirements validation to ensure that the software will perform as intended in the customer environment. |
| Difference between B and C | No change |
| C | 4.1.7 The project manager shall perform requirements validation to ensure that the software will perform as intended in the customer environment. |
| Difference between C and D | No change |
| D | 4.1.7 The project manager shall perform requirements validation to ensure that the software will perform as intended in the customer environment. |

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
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Rationale

Validation is the process performed throughout the software lifecycle to ensure that the product will meet end-user/customer or stakeholder expectations. Validation ensures that a software product meets the requirements and expectations of the end user and stakeholder(s).  The difference between “verification” and “validation” is that **validation ensures that the “right product is built”** according to the user/stakeholder, while **verification ensures that the “product is built right”**.

Validation is performed for the following reasons:

* To clarify and document customer expectations.
* To gain additional understanding of requirement intent or rationale
* To gain confidence that the requirements are realistic and can be fulfilled for the intended use
* To ensure that the development effort is “on-track” during the software lifecycle
* To reduce costs (i.e., get it right the first time).
* To ensure customer satisfaction with the end product.

Requirements validation is fundamental to ensuring the software meets the customer’s needs, functions as expected, and operates successfully in its intended environment. By validating requirements, the project manager can confirm that the software aligns with mission objectives, operational constraints, and stakeholder expectations, including end-user needs. This process eliminates costly errors stemming from misunderstood, incomplete, or incorrect requirements and reduces the risk of operational failures once the software is deployed.

---

### **Key Supporting Points for the Rationale**

#### **1. Ensures Alignment with Customer Needs**

* **Why It’s Important:**  
  Requirements validation checks whether the stated requirements accurately reflect the customer's needs and whether the software satisfies them under real-world operating conditions. Misaligned or misunderstood requirements can compromise mission objectives and customer satisfaction.
* **Example:**  
  If a ground control system must operate in low-bandwidth environments, validating this requirement during early reviews ensures the software design will account for communication constraints. Without validation, the software could fail to function under such constraints.

---

#### **2. Prevents Defects Early in the Lifecycle**

* **Why It’s Important:**  
  Requirements validation identifies errors, omissions, or ambiguities in customer requirements before development begins, when corrections are cheaper and easier to implement. Validating requirements early prevents these errors from propagating through the software lifecycle, which could lead to costly design changes, schedule overruns, or system defects.
* **Example:**  
  Misinterpreting a requirement for object tracking accuracy during validation could lead to extensive rework later when testing reveals that the software fails to meet operational tolerances.

---

#### **3. Guarantees Operational Compatibility with the Intended Environment**

* **Why It’s Important:**  
  Software often operates under specific hardware configurations, environmental conditions, or constraints (e.g., bandwidth limitations, extreme temperatures, power usage, latency). Requirements validation ensures the software is designed with these constraints in mind, avoiding incompatibilities that could lead to system failures during deployment.
* **Example:**  
  Consider a mission-critical spacecraft software system designed for operation under high radiation. Requirements validation involves confirming all operational tolerances (e.g., computation error rates) match real-world radiation levels to avoid hardware or software malfunctions in the space environment.

---

#### **4. Reduces Risk of Mission Failure**

* **Why It’s Important:**  
  For NASA projects, any failure in mission-critical software can result in loss of mission objectives, scientific data, assets, or human safety. Requirements validation reduces these risks by ensuring the software performs as intended under all operational scenarios, including edge cases.
* **Example:**  
  The Mars Polar Lander mission failed partly because the software requirements did not specify handling premature engine shutoff caused by vibrations during landing. Validating the requirements against anticipated landing conditions might have flagged this omission, preventing mission failure.

---

#### **5. Ensures Requirements Are Testable and Measurable**

* **Why It’s Important:**  
  An important aspect of requirements validation is ensuring that requirements are clear, testable, and measurable. This helps teams confirm that the software meets the stated requirements during various lifecycle phases (e.g., design, testing, and validation). Without testable requirements, it becomes nearly impossible to verify software functionality accurately against customer needs.
* **Example:**  
  A requirement like "The software shall process data quickly" is vague and untestable. Validation ensures the requirement is rewritten as "The software shall process 1 GB of satellite data within 10 seconds under normal conditions," making testing feasible and measurable.

---

#### **6. Mitigates Risks to Safety-Critical and Security-Critical Systems**

* **Why It’s Important:**  
  Requirements validation ensures no gaps exist in addressing safety-critical and security-critical functions. For example, hazard controls, intrusion detection, and operational safeguards must be validated to ensure the software does not inadvertently introduce risks to personnel, equipment, or data.
* **Example:**  
  Safety-critical validation may confirm that requirements adequately address emergency shutdown scenarios in case of hardware faults. Similarly, requirements validation may include testing for alignment with security protocols in NASA’s operational environment.

---

#### **7. Promotes Collaboration Between Stakeholders**

* **Why It’s Important:**  
  Requirements validation fosters collaboration among customers, system engineers, software engineers, and testers. Ensuring all stakeholders have a shared understanding of the requirements minimizes miscommunication and increases alignment across teams.
* **Example:**  
  During validation, customers may clarify nuanced operational needs that were initially misunderstood. For instance, they might specify that "real-time data processing" means updates within milliseconds instead of seconds, prompting necessary updates to the software design requirements.

---

#### **8. Prevents Wasted Resources on Unnecessary Features**

* **Why It’s Important:**  
  Validation helps avoid efforts spent on superfluous or incorrect features by confirming which requirements are truly necessary for the software’s success.
* **Example:**  
  A project may initially list software features that align poorly with the customer environment or add complexity without corresponding benefits. Validation identifies such issues early, enabling teams to adjust scope and resources accordingly.

---

#### **9. Adheres to NASA Standards and Project Guidelines**

* **Why It’s Important:**  
  NASA directives mandate rigorous requirements validation to comply with safety, reliability, and performance standards. Requirement 4.1.7 ensures software functionality aligns with the customer environment and satisfies agency guidelines, such as NPR 7150.2.
* **Example:**  
  Validation ensures that requirements for telemetry data processing align with NPR 7150.2 standards for data precision, reducing the risk of inconsistencies in development and mission operations.

---

### **Benefits of Enforcing This Requirement**

1. **Improved Software Quality:**  
   Validation ensures the software operates as intended and avoids defects linked to misunderstood requirements.
2. **Reduced Development Costs:**  
   Catching requirement issues early reduces costly downstream fixes and minimizes resource allocation toward handling misaligned functionality.
3. **Enhanced Mission Success Rates:**  
   Validating requirements ensures robust functioning under real-world conditions, reducing risks of operational failure that could jeopardize mission objectives.
4. **Increased Stakeholder Confidence:**  
   Customers and end-users are assured the software will meet their needs and function reliably in the environment for which it was designed.

---

### **Summary**

Requirement 4.1.7 is critical to ensuring the software performs as intended in the customer environment, aligning with stakeholder needs, operational conditions, and NASA's rigorous safety and reliability standards. Requirements validation minimizes the risk of defects, operational failures, and miscommunications while reducing costs and improving mission success rates. By adhering to this process, project managers can ensure the delivered software meets expectations, protects resources, and supports the organization’s high standards for safety, quality, and performance.

# 3. Guidance

Validation is a process performed throughout the software lifecycle to ensure that the product will meet end-user/customer or stakeholder expectations. Validation ensures that a software product meets the requirements and expectations of the end user and stakeholder(s) in their target environment.  The difference between “verification” and “validation” is that **validation ensures that the “right product is built”** according to the user/stakeholder, while v**erification ensures that the “product is built right”**.

Product behavior validation is a process of evaluating the software product to ensure that the right behaviors are evident in the final product within the target environment (e.g., “Testing, Operations, Maintenance, Training, and Support services”[689](#_tabs-<p></p>)environments.) The right behaviors reflect what the system is supposed to do, what the system is not supposed to do, and what the system is supposed to do under adverse conditions.  Proof of the right behavior is generally accomplished by demonstration or test to show the product exhibits the desired behavior(s).  Requirements validation is performed with the customer and stakeholders throughout the software development lifecycle to confirm that the requirements are feasible, necessary, sufficient, and accurately reflect customer and stakeholder intent and expectation. This will help reduce any rework and misunderstandings to increase the likelihood of delivering a product that meets expectation in the first version of the final product.

Validation activities are not performed in an ad hoc manner but are planned and captured in a validation plan document. The validation plan is typically part of a verification and validation (V&V) plan, a software V&V plan (SVVP), or included in the Software Management/Development Plan ([5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)).

## 3.1 Definition of Validation

NPR 7150.2 defines Validation as:

1. Confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled,[688](#_tabs-<p></p>)
2. Process of providing evidence that the system, software, or hardware and its associated products satisfy requirements allocated to it at the end of each life cycle activity, solve the right problem (e.g., correctly model physical laws, implement business rules, and use the proper system assumptions), and satisfy intended use and user needs,[209](#_tabs-<p></p>)
3. The assurance that a product, service, or system meets the needs of the customer and other identified stakeholders. It often involves acceptance and suitability with external customers,[302](#_tabs-<p></p>) and
4. Process of evaluating a system or component during or at the end of the development process to determine whether it satisfies specified requirements.[209](#_tabs-<p></p>)

Software Validation is the confirmation that the product, as provided (or as it will be provided), fulfills its intended use. In other words, validation ensures that “you built the right thing.”

## 3.2 Requirements Validation Throughout the Life Cycle

Requirements validation is performed by stakeholders throughout the software development life cycle. SWE-055 applies to products from initial requirements development through final product delivery.

* **Requirements Phase/Activity** – Typically, requirements validation starts during the Requirements phase with a stakeholder review of the Software Requirements Specification (SRS). It includes the confirmation that the requirements capture the needs and expectations of the customer and stakeholders through the provision of objective evidence. The reviewed SRS is that objective evidence. The intent of the SRS validation review is to make sure everyone understands and agrees on the documented requirements, and that they are feasible, necessary, and accurately reflect customer and stakeholder intent.

Note: A validation review is a quality control method used to address erroneous interpretations or assumptions regarding the product's intended function or use. Similar to verification, early detection and correction of defects and omissions during validation reduces work by eliminating final product problems.

* **Design Phase/Activity** – Requirements validation continues during the Design phase with the stakeholders reviewing the Software Design Description (SDD) and any Interface Control Documents (ICDs) / Interface Design Descriptions (IDDs). It should provide an indication if the proposed design is feasible and if it satisfies the documented requirements and the stakeholder’s intent. The review of the SDD also provides an opportunity to:
  + Refine existing requirements,
  + Determine if all the requirements have been identified including deriving new requirements,
  + Identify/review/concur with any assumptions, constraints, and limitations, and
  + Provide input on the interfaces (e.g., file I/O) and User Interface.

The SDD validation review is to make sure everyone understands and agrees on the implementation of the documented requirements in the design, and that they accurately reflect stakeholder intent.

* **Test Phase/Activity** (also see [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations)) – Requirements validation also occurs during testing when the design has been transformed into a ready-to-test software product that meets the requirements. Validating the software and associated requirements via test entails:
  + Developing acceptance criteria for the system software and each requirement.
  + Writing, developing, and/or updating the test procedures to be used to validate the software. “Procedures may cover maintenance; set up and support of test and evaluation facilities; training; management and acceptable use of test data."[689](#_tabs-<p></p>)
  + Executing the validation procedures and documenting the results.
  + Identifying “the results that do not meet the established criteria for validation.”[689](#_tabs-<p></p>)
  + Analyzing the validation results that do not meet the established acceptance criteria and determining the corrective action, if any.[689](#_tabs-<p></p>)
  + Recording and communicating “analysis results and corrective actions to affected stakeholders.”[689](#_tabs-<p></p>)

The stakeholders develop and/or update their acceptance [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) to validate the implementation to determine if it meets their requirements, acceptance criteria, and intent. The test results and associated analysis, documented in the acceptance [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) (STR), are the objective evidence that the software product does or does not meet the requirements and customer and stakeholder expectations. If the software is safety critical, Software Assurance must be invited to witness the validation testing.

* **Release Phase** – The final step in validating the requirements is to authorize the release of the software for use and to document how it is to be used in the form of user and operational manuals, training materials, and process documents.

## 3.3 Validation Planning

Requirements validation needs to be planned and documented to establish what software products will be validated and their associated acceptance criteria. Examples of acceptance criteria6 are:

* Specification of test inputs and outputs
* Description of expected results
* Description of acceptable results
* Target service levels and expected results
* Service objectives and measurements
* Customer types and expectations

The plans should also include any processes and techniques that will be used to perform the validation.

It doesn’t matter where it is documented, it just needs to be documented but typically validation plans are in the project’s:

* Verification and Validation (V&V) Plan, Software Test Plan (see Topic [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)), or
* Software Development/Management Plan (see Topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)).

## 3.4 Validation Process

Requirements validation is a process of evaluating the requirements to ensure that the right behaviors have been identified and documented in the work product. The right behaviors adequately describe what the system is supposed to do, what the system is not supposed to do, and what the system is supposed to do under adverse conditions.

The validation process is performed throughout the life cycle regardless of what is being validated. The basic process is illustrated in Figure 1 below. If a product is to be validated, then:

1. Select validation criterion applicable to product
2. Examine product for technical correctness, completeness, and compliance to criterion
3. Note defects, and questions/issues as findings
4. Repeat steps 1 - 4 until all validation criteria are addressed

Figure 1: Basic Validation Process

Validation activities are not to be confused with verification activities as each has a specific goal.  Validation is designed to confirm the right system is being produced while verification is designed to confirm the product is being produced correctly.

## 3.5 Select Life Cycle Products For Validation

The first step in the Validation process is the selection of the software life cycle products that will be validated. Below is a list of the typical work products that will be validated during each phase of the life cycle. During the selection process, review the validation selection, roles, responsibilities, constraints, and methods with the affected stakeholders.

* Requirements Phase – Verify that the requirements are adequate
  + Software Requirements Specifications (SRS) (Also see [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification))
  + Interface Requirements
  + System Requirements
* Design Phase – Ensure the requirements are adequately reflected in the Design and Code.
  + Software Design Descriptions (Also see [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description))
  + Interface Design Descriptions (Also see [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description))
  + Interface Control Documents (ICDs)
* Test Phase – Ensure the requirements are adequately tested.
  + Acceptance Software Test Procedures (Also see [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures))
  + Acceptance Software Test Reports (Also see [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report))
* Release Phase – Make sure the functionality of the software is documented in a manner that the users can understand what the features are supposed to do.
  + Software User Manual / User Guide (Also see [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual))

## 3.6 Validation Techniques & Methods

To perform requirements validation, multiple techniques and methods may be required based on the nature of the system, the environment in which the system will function, or even the phase of the development life cycle.  Validation tests should be clearly outlined and described in the validation plans.  Most validations should be completed through inspection/review, demonstration, or testing and involve the end users and other affected stakeholders. Ideally, the testing should be performed in the target environment of the stakeholder’s system.

These validation techniques and methods may entail some of the following:

* **Conduct Formal reviews:**
  + Structured reviews in which specified steps are taken and roles are assigned to individual reviewers (See Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists))
  + Formal reviews are useful for validating documents, such as software requirements specifications ([5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)), and allow for discussion and eventual agreement on the requirements among stakeholders with varied viewpoints.
    - The Software Requirements Review (SRR) ([7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)) should address both ”getting the right requirements” and "getting the requirements right”.
  + Formal reviews allow for the identification of defects as well as suggested corrections.
  + Ensure requirements meet the intent of the operational concepts to ensure validation covers requirements.
  + Ensure descriptions of how the software will function in the customer’s operational or simulated environment are documented.
  + Use this technique to improve the quality of customer/stakeholder requirements.
  + Use this technique to ensure customer/stakeholder requirements and expectations are correctly captured.
* **Software peer reviews/inspections/walk-throughs:**
  + Relevant stakeholders investigate and review a product, such as requirements to determine if it meets preset criteria, identify product defects, and check for feasibility.
  + Peer reviews, walk-throughs, and inspections are useful for validating documents, such as SRSs, and allow for peer discussion of the technical aspects of the document content.
  + Inspections can be informal or formal with formal inspections being more structured with specific activities, assigned roles, and defined results (metrics, defects, etc.).
  + Inspections typically cover larger volumes of information than formal reviews and only identify the issues; solutions are typically not part of the peer review/inspection process.
  + For Additional Guidance on Peer Reviews see [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).
* **Demonstrate Functionality in Prototypes:**
  + Create a working prototype(s) of the software. This allows the software developers to evaluate the viability of high risk requirements/elements and allows the customer/stakeholders to see the requirements implemented and iterate to get to the desired end-product.
  + Use this technique when budget and time allow, when stakeholders are hands-on, when the development model is an iterative process, etc.
  + Demonstrating specific actions or functions of the code.
  + Use this technique to validate select requirements related to questions such as "can the user do this" or "is this particular feature feasible."
* **Analysis:**
  + A "lightweight" version of simulation may be used for performing analysis without coding. For example, use spreadsheets to decompose and analyze algorithms to develop strategies for implementation without creating a simulation prototype,
  + For time-related aspects of validation, it may be necessary to use a different technique to expedite the analysis. For example, if a system is designed to run at real-time speed, it may not be feasible to execute and collect data for 100 tests/iterations at this rate to perform an analysis. It may be necessary to create a simulator/simulation to execute at X-times real-time in order to perform the analysis, validate the system, and/or troubleshot issues in a timely manner. This technique may also be necessary if the system has restricted or limited access.
  + Use this technique as part of an overall validation strategy or as a precursor step to full simulation.
  + Beta testing of new software applications. This may flush out requirements that were a good idea in theory are not in practice, leading to a refinement or change in the original requirement(s). It may also reveal new or missing requirements.
    - Use this technique when budget and time allow, when stakeholders are hands-on, when stakeholders (primarily user groups) and project schedules are amenable to this type of testing, etc.
* **Paper simulations/prototyping/storyboarding: [304](#_tabs-<p></p>)**
  + Drawing prototypes on paper.
    - This is a low-cost prototyping technique that might be useful in the early stages of high-level requirements development to capture and display visually the ideas and concepts (e.g., user interface) or for projects that don't have the budget for prototyping in software.
    - This is a good technique for developing user interface requirements.
    - Issues with prototyping on paper include storing for future reference and difficulty transforming into executable prototypes.
  + Typically, prototypes simply end up in requirements documents.
  + Commonly used to elicit and validate software user interfaces and interactions.
* **Computer modeling and simulation**
  + The intent of validation is to assure that the final product works within the stakeholder environment, so use of modeling and simulation validation should be minimized.
  + Requirements validation can be supported by modeling various aspects of stakeholders’ needs, e.g., use cases (see below); capabilities decomposition; data flow; control flow; entities’ (objects’) properties and interactions; sequence of events; processes; states, modes, and transitions; and timing aspects.
    - **Use-cases** [304](#_tabs-<p></p>)model a system’s behavior, by identifying actors and their interaction with the system, and depicting a problem and solution from the user's point of view ("who" does "what" using the system). This technique is helpful when the focus of the system is on its user interaction and when it is easy to identify users (both human and other systems) and services or functionality provided to them by the system.
  + Models can be represented using different notations, e.g., graphical notations/languages (e.g., UML/SysML) or mathematical notations.
  + Some models are executable; model execution (simulation) offers additional insight into software behavior and dynamic aspects that a purely descriptive model is not able to provide.
  + There are tools for developing, managing, evolving, and sharing models and simulations, e.g., MagicDraw, MATLAB, and Simulink.
* **Viewpoint-oriented requirements validation**: [304](#_tabs-<p></p>)
  + Identify conflicting requirements based on the viewpoints of various stakeholders.
  + Use this technique when there is a need to identify conflicting requirements based on viewpoints or when it is important to consider requirements from multiple perspectives.
* **Formal methods:**  
  + Mathematically rigorous techniques.
  + Use such techniques to validate formal requirements specifications or to validate key properties of requirements. [181](#_tabs-<p></p>)

* **Development and Review of test cases:**
  + Review test cases individually and as a set to confirm coverage of system scenarios.
  + Review test cases with stakeholders to confirm functional and operational scenarios (as defined by the requirements).
  + Development and review of test cases may help find problems in the requirements since it requires completely thinking through the operation of the application. If the test case is difficult to create, then it’s usually an indicator of a poorly written requirement. The requirement should be written in a manner that the desired test result can be easily obtained.
  + This technique is particularly useful for test-driven software development.

See also [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations), Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009)

### 3.6.1 Security Validation Techniques

There are also validation techniques that are specific to cybersecurity and can be used when identifying security threats and vulnerabilities.  These techniques may be manual, automated, or a combination of both.[689](#_tabs-<p></p>) Some of the techniques are:

* **Simulation and modeling** – “Modeling and simulation (M&S) is the use of models (e.g., physical, mathematical, behavioral, or logical representation of a system, entity, phenomenon, or process) as a basis for simulations to develop data utilized for managerial or technical decision making. In the computer application of modeling and simulation a computer is used to build a mathematical model which contains key parameters of the physical model. The mathematical model represents the physical model in virtual form, and conditions are applied that set up the experiment of interest. The simulation starts – i.e., the computer calculates the results of those conditions on the mathematical model – and outputs results in a format that is either machine- or human-readable, depending upon the implementation.[691](#_tabs-<p></p>)
* **Penetration testing** – Also known as pen testing, is a security exercise where a cyber-security expert attempts to find and exploit vulnerabilities in a computer system. The purpose of this simulated attack is to identify any weak spots in a system’s defenses which attackers could take advantage of.
* **Friendly hacking** – Also known as “Ethical hacking or white-hat hacking, is the practice of intentionally probing computer systems, networks, or applications to identify vulnerabilities and weaknesses. Unlike malicious hacking, friendly hacking is conducted with the permission of the system owner and aims to enhance security by preemptively identifying and addressing potential threats. This proactive approach is crucial in safeguarding sensitive data and maintaining the integrity of digital infrastructures."[690](#_tabs-<p></p>)
* **Fuzzy testing** – Fuzz or fuzzy testing is a class of robustness testing that focuses on providing randomly generated data as (sequences of) input to the system. The data provided are typically, but not limited to, invalid and unexpected input for the purpose of identifying a system’s vulnerability related to boundary values and insufficient validation of input. The latter vulnerability, especially, can lead to security breaches (e.g., Structured Query Language injection attacks, memory leaks). Multiple approaches exist for generating the input values: 1) mutating an initial sample of input randomly or semi-randomly using heuristics or 2) generating the values based on specifications or models of the input. Also see Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).
* **Re-play testing** – Also known as record and replay testing, is a method that uses a tool to automate tests without writing test scripts. It records actions during manual testing and allows them to be replayed later to create automated test scripts.

## 3.7 Roles

When validating products throughout the life cycle, consider inviting personnel serving in the following roles to participate in reviews/inspections/demos because all roles will review the requirements from a different perspective:

| **Sample Roles for Validation Activities** |
| --- |
| Customer |
| Developer |
| Tester |
| Systems Engineer |
| Hardware Engineer |
| Fault Management Engineer |
| Software Assurance and Safety Engineer(s) |
| Requirement/SRS Author |
| Other Reviewers (e.g., subject matter experts)  -       As appropriate, multiple Reviewers may be included, each providing a specialized perspective |

## 3.8 Checklists and Procedures

When available and appropriate, checklists and documented procedures are used for the various techniques selected for requirements validation, to ensure consistency of application of the technique.

| **Sample Checklists and Procedures** |
| --- |
| Peer review/inspection checklists |
| Formal review checklists |
| Analysis procedures |
| Acceptance test procedures |

Samples are included in the Resources section of this guide, but Center procedures take precedence when conducting requirements validation activities at a particular Center.

## 3.9 Requirements Traceability Matrix

A requirements traceability matrix may also be useful to ensure that all requirements are validated.  The matrix could include:

* Links to higher-level requirements that identify/define user needs.
* Traces to the design components, code, and test case(s).
* A place to record validation methods (if not included in the test procedures).
* A place to record or reference the validation results (Results should be recorded in a Test Report,).

## 3.10 Common Issues

Some common issues related to requirements validation include: [012](#_tabs-<p></p>)

* Confusing management of requirements with validation of requirements.
  + Managing requirements will not ensure they are correct.
* When using prototyping to validate requirements:
  + Failing to keep the focus on *what* the software is supposed to do.
  + Allowing the focus to shift to *how* the system will look when it is done.
* Failing to re-validate requirements as they change during the project life cycle.
* Getting stakeholders with different views to agree on a single version of a requirement; interpretation can be troublesome.
* When using visual models to bridge the communication gaps among stakeholders, only translating a limited number of requirements into visual models (often due to time or budgetary constraints).
* Failing to link the text to visual models; both are needed for understanding.
* Failing to use a formal process to track all versions of the requirements as they change during the project.

Additionally, it is important to confirm with stakeholders that their needs and expectations remain adequately and correctly captured by the requirements following the resolution of conflicting, impractical, and/or unrealizable stakeholder requirements.

## 3.11 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.12 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

# 4. Small Projects

Small projects often face constraints in terms of budget, staffing, and time, necessitating a tailored approach to requirements validation. While the rigor of requirements validation may be adjusted based on the software classification (e.g., Class D/E), safety-critical, human-rated, and other mission-critical requirements must still be handled with appropriate care to ensure the software performs as intended in the customer environment. This guidance provides strategies for balancing resource limitations with effective requirements validation methods.

---

### **Approach for Small Projects**

#### **1. Adjust Validation Efforts Based on Software Classification**

For lower-level classifications (Class D/E software):

* **Shared Roles:** Limited resources may result in overlapping roles between developers and stakeholders (e.g., a developer may also act as a stakeholder representative for certain decisions).
* **Combined Processes:** Smaller teams can combine verification and validation processes where feasible. For example, requirements validation could be partially performed during code reviews, integration testing, or system verification stages rather than as a separate activity.

For higher-level classifications (Class A/B/C software):

* Validation processes should adhere to more rigorous methods, reflecting the complexity and criticality of the software.

---

#### **2. Focus on Safety-Critical, Human-Rated, and Other Critical Requirements**

Regardless of software classification, some requirements demand robust validation due to their importance. Small projects must prioritize the following:

* **Safety-Critical Requirements:** These requirements must be validated to ensure they avoid hazards, perform their protective or preventive functions, and operate predictably in both nominal and off-nominal conditions.
* **Human-Rated Requirements:** Validation for requirements affecting human-rated systems must ensure reliable performance under operational conditions, mitigating risks to personnel safety.
* **Other Mission-Critical Requirements:** Requirements directly linked to mission success—such as those affecting data accuracy, real-time performance, or hardware/software integration—should receive heightened validation attention.

**Key Action:** Document these requirements and associated validation methods in the project's software development/management plan to ensure consistency and accountability.

---

#### **3. Leverage Available Resources and Tools**

Small projects can optimize requirements validation by utilizing tools, methods, and resources already available to the team. For example:

* **Testing Frameworks:** Use automated tests where applicable to validate requirements (e.g., confirm performance metrics match operational needs).
* **Simulation/Emulation:** For operational environments (e.g., spacecraft systems or ground control), use lightweight simulations where full system testing is not possible.
* **Requirement Reviews in Team Meetings:** Integrate validation discussions into routine meetings to save time while ensuring alignment.
* **Traceability Matrices:** Maintain a simple spreadsheet or traceability table to confirm requirements are linked to downstream artifacts (design, implementation, testing, etc.).

---

#### **4. Simplify Processes Without Sacrificing Effectiveness**

Small projects can validate requirements without the need for extensive formal reviews or documentation by adopting the following practices:

* **Incremental Validations:** Validate requirements progressively throughout the lifecycle (e.g., during design, coding, testing, and peer reviews). This spreads out the effort and provides frequent checkpoints for alignment.
* **Informal Stakeholder Buy-in:** If formal validation reviews are not feasible, make use of informal stakeholder engagement to confirm requirements satisfy their needs.

**Example:** For a Class D CubeSat project, verify that telemetry requirements are aligned with operational constraints during weekly team meetings and confirm traceability from requirements to test cases as tests are conducted.

---

#### **5. Use Risk-Based Prioritization**

Not all requirements require equal validation effort. Focus validation on areas with the highest risk or potential impact:

* **High-Risk Requirements:** Prioritize validating requirements that:
  + Address safety and reliability.
  + Involve complex integrations (e.g., hardware/software interoperability).
  + Affect critical mission success criteria.
* **Low-Risk Requirements:** For less critical requirements (e.g., minor user interface preferences), validation methods can be less rigorous (e.g., developer testing combined with stakeholder review).

---

#### **6. Document the Validation Process**

Documentation is essential for maintaining traceability and accountability. Even small projects should clearly record:

* **Steps Taken:** List the activities performed to validate each type of requirement (e.g., component tests, stakeholder reviews, simulations).
* **Tools Used:** Identify tools or frameworks leveraged during validation.
* **Results:** Capture the results of validation, including discrepancies found and corrective actions taken.
* **Acceptance:** Include stakeholder sign-off or agreement on validated requirements.

**Key Action:** Summarize the validation effort in the project's software plans. For example:  
*"Requirements affecting CubeSat navigation accuracy were validated using simulation tests and customer feedback on prototype performance. Results showed data errors below the acceptable tolerance of 3%."*

---

#### **7. Ensure Coordination Between Developers and Stakeholders**

In small teams, the close collaboration between software developers, users, and stakeholders enhances the effectiveness of requirements validation. Developers should:

* Regularly engage stakeholders to confirm that requirements are understood and validated in the context of real-world operations.
* Seek end-user feedback on prototypes or early versions of the software to ensure requirements are correctly implemented and will function as intended in the customer environment.

---

### **Examples for Small Projects**

#### **Example 1: Class E CubeSat Software (Telemetry System)**

* **Critical Requirement:** Validate telemetry system performance in low-bandwidth environments.
* **Validation Method:** Perform simulated testing with network emulation tools to confirm data transmission rates align with requirements.
* **Focus Area:** Ensure telemetry data formats and units match the customer's ground station specifications.

#### **Example 2: Class D Instrument Control Software**

* **Critical Requirement:** Validate safety-critical shutdown procedures.
* **Validation Method:** Perform manual verification and end-to-end testing in a prototype environment to confirm compliance with operational safety standards.
* **Focus Area:** Ensure software correctly shuts down the instrument during off-nominal conditions within the specified reaction time.

---

### **Key Summary Points**

1. **Adjust Rigor Based on Classification:** Lower-level classifications (D/E) can simplify validations but must still ensure safety-critical and mission-critical performance requirements are validated thoroughly.
2. **Prioritize Critical Requirements:** Validate safety-critical, human-rated, and mission-critical requirements with appropriately rigorous methods proportional to their impact.
3. **Optimize with Available Resources:** Combine processes (verification + validation), use lightweight tools (e.g., spreadsheets or simulations), and leverage informal stakeholder engagement to conserve resources while maintaining efficacy.
4. **Document Validation Efforts:** Even small projects must document validation processes, tools used, and results to ensure accountability and traceability.
5. **Collaborate Effectively:** Shared roles in small projects allow for streamlined communication between developers, customers, and stakeholders, enhancing validation accuracy.

This guidance helps small projects effectively balance resource limitations with meaningful requirements validation while ensuring software performs as intended in the customer environment.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-012) Checklist for the Contents of Software Requirements Review (SRR),  580-CK-005-02, Software Engineering Division, NASA Goddard Space Flight Center, 2009.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-079) SED Inspections, Peer Reviews, and Walkthroughs,  580-SP-055-02, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2006.
   Updated title from "ISD Inspections, Peer Reviews, and Walkthroughs, 580-SP-055-01" to "SED Inspections, Peer Reviews, and Walkthroughs, 580-SP-055-02" to reflect updated version of document, and to reflect the new name (Software Engineering Division) of the GSFC organization that produced the document.)
  This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-181)

  [Experiences Using Lightweight Formal Methods for Requirements Modeling,](https://ntrs.nasa.gov/api/citations/19980016986/downloads/19980016986.pdf "Click to open in new window")

  Easterbrook, Steve, 1998. NASA-IVV-97-015, October, 16, 1997, Accessed November 2011 from http://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19980016986\_1998065191.pdf.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-209)

  [IEEE Standard for System, Software, and Hardware Verification, and Validation](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8055462 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1012-2016 (Revision of IEEE Std 1012-2012), Published September 29, 2017.  See definition of Software Validation. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards. Non-NASA users may purchase the document from: http://standards.ieee.org/findstds/standard/1012-2012.html
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-302)

  [A Guide to the Project Management Body of Knowledge (PMBOK® Guide) -- Fifth Edition.](http://marketplace.pmi.org/Pages/ProductDetail.aspx?GMProduct=00101095501 "Click to open in new window")

  Project Management Institute (2013).
* (SWEREF-304)

  [Empirical Studies of Requirements Validation Techniques.](http://ieeexplore.ieee.org/document/4909209/ "Click to open in new window")

  Raja, U.A. (February, 2009). IEEE Computer, control and Communication, 2009. 2nd International Conference.  This link may require you to be logged in on your NASA network or to have an account on the NASA START (AGCY NTSS) system (https://standards.nasa.gov ). Once logged in, users can access Standards Organizations, IEEE and then search to get to authorized copies of IEEE standards.
  Retrieved on December 12, 2017.
* (SWEREF-513)

  [Mars Climate Orbiter Mishap Investigation Board - Phase I Report](https://llis.nasa.gov/lesson/641 "Click to open in new window")

  Public Lessons Learned Entry: 641.
* (SWEREF-688)

  [Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Guide to SQuaRE](https://www.iso.org/standard/64764.html "Click to open in new window")

  ISO/IEC 25000:2014, (ISO/IEC/IEEE 12207:2017 Systems and software engineering--Software life cycle processes, 3.1.71) (ISO/IEC/IEEE 15288:2015 Systems and software engineering--System life cycle processes, 4.1.53) (ISO/IEC TS 24748-1:2016 Systems and software engineering--Life cycle management--Part 1: Guide for life cycle management, 2.61
* (SWEREF-689)

  [CMMI Model - Overview](https://cmmiinstitute.com/dashboard "Click to open in new window")

  Capability Maturity Model Integration (CMMI) Model V3.0, ISACA, April 6, 2023,  NASA users can access the CMMI models with a CMMI Institute account at: https://cmmiinstitute.com/dashboard. Non-NASA users may purchase the document from: https://cmmiinstitute.com
* (SWEREF-690)

  [Friendly hacking explained](https://isecjobs.com/insights/friendly-hacking-explained/ "Click to open in new window")

  isecjobs.com, Published 10/30/2024,  Discover the world of ethical hacking, where cybersecurity professionals use their skills to identify and fix vulnerabilities, ensuring systems are secure and resilient against malicious attacks.
* (SWEREF-691)

  [Modeling and simulation](https://en.wikipedia.org/wiki/Modeling_and_simulation "Click to open in new window")

  In Wikipedia, The Free Encyclopedia. (May 3, 2025). Retrieved May 7, 2025 from: https://en.wikipedia.org/wiki/Modeling\_and\_simulation
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Requirement 4.1.7 emphasizes the necessity of performing requirements validation to ensure that the software will perform as intended in the customer environment. Past NASA projects offer valuable insights into the consequences of inadequate validation, as well as the benefits of thorough validation processes.

---

### **1. Mars Climate Orbiter Mishap - Requirements Validation Failure**

* **Lesson Number:** 0641
* **Description:**  
  The Mars Climate Orbiter (MCO) spacecraft was lost due to a failure in requirements validation that could have identified inconsistencies between interface documentation and the requirements. Specifically:
  + Software on the ground provided trajectory data in *English units* (pounds-force seconds), while the existing software interface documentation specified that the data should be in *metric units* (Newton-seconds).
  + This mismatch was not identified during requirements validation, leading to catastrophic trajectory miscalculations and the eventual failure of the mission.
* **Relevance to Requirement 4.1.7:**
  + **Key Takeaway:** Requirements validation must include consistency checks across all documentation, including internal and external interfaces, to prevent unit mismatches or other errors from propagating.
  + Ensure operational environments (e.g., units, hardware/software interactions) are explicitly and thoroughly validated during the requirements phase to detect potential points of failure.

---

### **2. Mars Polar Lander - Communication Failure**

* **Lesson Number:** 0643
* **Description:**  
  The Mars Polar Lander mission failed in part because the software requirements failed to account for the possibility of spurious signals from the spacecraft’s touchdown sensors.
  + During descent, the landing software mistook vibration signals as a confirmation of landing, causing the engines to shut down prematurely.
  + This error could have been identified had the operational environments, including the possibility of false signals during descent, been thoroughly validated against requirements.
* **Relevance to Requirement 4.1.7:**
  + Validation processes must account for both nominal and off-nominal (edge case) operational scenarios.
  + Simulations or other environmental tests should be conducted to ensure software requirements address real-world conditions comprehensively.
  + Safety-critical requirements need extra scrutiny to cover scenarios that might not appear obvious during initial analysis.

---

### **3. Genesis Mission - Requirements to Operational Context Mismatch**

* **Lesson Number:** 1121
* **Description:**  
  The Genesis spacecraft’s mission to collect and return solar particles failed upon sample return due to improperly validated requirements.
  + The spacecraft’s re-entry system depended on a set of switches to detect deceleration and deploy the parachutes. These switches were installed backward because the requirement did not clearly define critical interface and installation details.
  + Without proper validation against operational conditions, the re-entry system misinterpreted the absence of a signal as a normal state, leading to a failure to deploy the parachutes.
* **Relevance to Requirement 4.1.7:**
  + Requirements must explicitly define how components interact and be properly validated in the context of both their physical configuration and their operating environment.
  + Physical interfaces (e.g., hardware/software integration points) need to be tested to validate that the system behaves as intended in real-world conditions.

---

### **4. Hubble Space Telescope - Mirror Aberration**

* **Lesson Number:** 0371
* **Description:**  
  The deployment of the Hubble Space Telescope revealed a flaw in the mirror that prevented it from focusing properly.
  + This issue occurred because the validation processes did not adequately verify the precision alignment requirement for the primary mirror.
  + The tools and measurements used during tests did not catch the error, and the improperly crafted mirror was launched without further validation.
* **Relevance to Requirement 4.1.7:**
  + Validation efforts must include independent assessments and cross-verification of requirements with multiple methods to confirm their implementation.
  + Ensure that the requirements validation process includes thorough physical testing where applicable and avoids over-reliance on specific tools without independent verification.

---

### **5. Space Shuttle Columbia Accident – Validation and Risk Assessment**

* **Lesson Number:** 1122
* **Description:**  
  The Columbia Accident Investigation Board (CAIB) found that organizational gaps in validating and addressing known risks contributed to the loss of the shuttle. One of the contributing factors was a failure to validate assumptions and data related to foam shedding during launch, which was treated as an acceptable risk without adequate validation.
* **Relevance to Requirement 4.1.7:**
  + Requirements validation must include assumptions and risks associated with unusual or low-probability events.
  + Mission-critical and safety-related requirements must undergo rigorous validation, including worst-case scenario testing, to eliminate unwarranted reliance on undocumented assumptions.

---

### **6. Mars Exploration Rovers - Success with Validation Processes**

* **Lesson Number:** 0758
* **Description:**  
  The Mars Exploration Rovers (Spirit and Opportunity) highlighted the benefits of thorough requirements validation. Both missions achieved long-term operational success due to rigorous validation of operational conditions and requirements.
  + The teams conducted extensive simulations for harsh Martian conditions, including atmospheric, thermal, and terrain challenges, and aligned their requirements validation to these operational environments.
* **Relevance to Requirement 4.1.7:**
  + Effective validation considers end-to-end operational contexts, environmental factors, and potential edge cases.
  + Validation is not just about confirming requirements but ensuring they anticipate real-world conditions comprehensively.

---

### **7.** Lessons Learned: In Class D, Fault Protection Becomes the Safety Net—So It Must Be Excellent

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

### **8.** **Lesson Learned (Starliner CFT):** **High‑level requirements invite misinterpretation; safety‑critical behavior must be fully specified and traceable.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Key propulsion/command requirements were high‑level; hazard analyses and safety requirements were not fully decomposed into verifiable software behavior with end‑to‑end traceability.

**Contributing Factors:**

* Ambiguity in expected behaviors (thresholds, timing, reset handling, telemetry fidelity).
* Weak linkage between hazard mitigations and software requirements/tests.

**Impacts:**

* Misinterpretation across teams; gaps persisted into integrated test.
* Incomplete verification evidence for safety‑critical functions.

**Recommended Practices (Aligned to SWE‑050/051/055):**

* Perform **behavioral decomposition**: translate safety requirements into concrete, measurable software requirements (thresholds, timing, state transitions, telemetry).
* Maintain **bidirectional traceability** from hazards → safety requirements → software requirements → test evidence.
* Use **structured requirement reviews** with SA participation and defect tracking.

**Actionable Checks:**

* RTM (Requirements Traceability Matrix) shows full chain from hazards to evidence.
* Safety requirements include quantitative parameters and acceptance criteria.
* Review minutes capture issues and resolutions with SA sign‑off.

### **Lessons Learned Summary**

#### **Failures from Insufficient Requirements Validation:**

1. Mismatches between internal documentation and operational requirements (Mars Climate Orbiter).
2. Failure to account for spurious signals, edge cases, or off-nominal conditions (Mars Polar Lander).
3. Misaligned or incomplete hardware-software interface definitions (Genesis mission).
4. Over-reliance on unvalidated tools or assumptions (Hubble’s mirror; Columbia).

#### **Successes from Robust Validation Processes:**

1. Comprehensive simulations and end-to-end lifecycle validation (Mars Exploration Rovers).

---

### **Key Takeaways from Lessons Learned**

1. **Interface Validation:** Requirements validation must include verifying that software and hardware interfaces are clearly defined, thoroughly tested, and consistent across all documentation.
2. **Cross-Validation of Units and Assumptions:** For systems requiring unit conversions or platform-specific inputs, ensure consistency checks are part of system-level reviews.
3. **Operational Testing:** Validate requirements under both nominal and off-nominal conditions to ensure the software accommodates edge cases in real-world environments.
4. **Independent Validation:** Include independent validation steps where feasible, using external test teams or tools to reduce the risk of overlooking critical requirements.
5. **Risk-Based Prioritization:** Focus rigorous validation efforts on safety-critical, human-rated, and mission-critical requirements, ensuring risks and assumptions are addressed before implementation.

---

By incorporating these lessons and strategies, projects can minimize risks, enhance reliability, and ensure alignment between validated requirements and operational environments, leading to mission success. Requirements validation must remain a critical phase in the software lifecycle, especially for high-stakes NASA projects.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Consider impact on testing when developing requirements in early lifecycle phases](https://software.gsfc.nasa.gov/lesson-details/92/). **Lesson Number 84**: The recommendation states: "Consider impact on testing when developing requirements in early lifecycle phases, and ensure a critical review by operations team members."
* [Operations team/ground system team needs to engage the flight systems development team](https://software.gsfc.nasa.gov/lesson-details/86/). **Lesson Number 86**: The recommendation states: "Operations team/ground system team needs to proactively and persistently engage the flight systems development team to define operating constraints."
* [Validation of the science data earlier in the life cycle](https://software.gsfc.nasa.gov/lesson-details/92/). **Lesson Number 92**: The recommendation states: "Plan for and implement validation of the science data earlier in the life cycle, particularly for externally provided instruments."
* [Operational database needs to reflect operational definitions and approach](https://software.gsfc.nasa.gov/lesson-details/101/). **Lesson Number 101**: The recommendation states: "Scrub the operational database and revise to reflect operational definitions and approach (for example, the operational definitions for R/Y/G limits)."
* [Select data analysis platform for all Instrument Team Facilities](https://software.gsfc.nasa.gov/lesson-details/114/). **Lesson Number 114**: The recommendation states: "Select the data analysis platform for all Instrument Team Facilities (ITFs) early in the life cycle."
* [Early engineering development on an instrument needs support from the scientific community](https://software.gsfc.nasa.gov/lesson-details/115/). **Lesson Number 115**: The recommendation states: "Accompany early engineering development on an instrument with support from the scientific community."
* [Impacts caused by interfaces that are not tested pre-launch](https://software.gsfc.nasa.gov/lesson-details/124/). **Lesson Number 124**: The recommendation states: "Develop mitigations for impacts caused by interfaces that are not tested pre-launch."
* [Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations](https://software.gsfc.nasa.gov/lesson-details/126/). **Lesson Number 126**: The recommendation states: "Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations."
* [Assumptions for both over- and under-allocated RF Link margins](https://software.gsfc.nasa.gov/lesson-details/127/). **Lesson Number 127**: The recommendation states: "Examine and rationalize assumptions for both over- and under-allocated RF Link margins."
* [Critical Data Storage address is useful to the test team](https://software.gsfc.nasa.gov/lesson-details/305/). **Lesson Number 305**: The recommendation states: "The selection of housekeeping telemetry needs input from all customers including the test team. The addition of certain telemetry points can make the customers job easier, maybe even \*significantly\* easier."
* [Perform software prototyping early to increase confidence in selections](https://software.gsfc.nasa.gov/lesson-details/315/). **Lesson Number 315**: The recommendation states: "Identify and pursue early prototyping efforts in order to understand the design space and options, better prior to closing trade studies."
* [Goddard Dynamic Simulator (GDS) Fault Management derived Requirements](https://software.gsfc.nasa.gov/lesson-details/344/).**Lesson Number 344**: The recommendation states: "The Goddard Dynamic Simulator (GDS) team needs to review the GDS requirements when the fault management table is initially defined (as well as when there are changes to the tables), and during the FSW Build Testing phase, at the start of Systems Testing. This review should include working with the Flight Software team at the contents of the Fault Detection and Correction (FDC) tables to determine what telemetry needs to be simulated. This review may result in new GDS requirement(s)."

# 7. Software Assurance

**SWE-055 - Requirements Validation**

4.1.7 The project manager shall perform requirements validation to ensure that the software will perform as intended in the customer environment.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project software testing has shown that software will function as expected in the customer environment.

## 7.2 Software Assurance Products

Software assurance products should comprehensively support software lifecycle activities, providing evidence of engineering rigor, verification, and validation. This section improves readability while highlighting key artifacts needed to demonstrate compliance with requirements and ensure software quality.

**Improved Section:** The following software assurance products are essential to verifying and validating the software lifecycle, ensuring alignment with requirements, design, testing, and customer environment expectations:

1. **Software Requirements Specification (SRS):**

   * Provides the documented baseline of all functional and non-functional requirements.
   * Reviewed to ensure requirements are complete, clear, consistent, testable, and traceable.
2. **Software Design Document (SDD):**

   * Contains the detailed architecture and design plan for the software, ensuring traceability to requirements.
   * Monitored for consistency with the Software Requirements Specification (SRS).
3. **Requirements Traceability Matrix (RTM):**

   * Demonstrates bidirectional traceability:
     + **Requirements to Validation Testcases and Results:** Ensures every requirement is validated through test cases and associated test results.
     + **Requirements to Expected Environment Requirements:** Confirms traceability between software requirements and environmental factors (e.g., hardware constraints, operating conditions, mission-critical limitations).
4. **Software Test Procedures:**

   * Outlines detailed steps and methods for executing software tests.
   * Assessed for completeness and alignment with requirements and the expected environment.
5. **Software Test Reports:**

   * Documents the results of software testing, including:
     + Validation outcomes for each requirement.
     + Evidence of successful execution of test cases under expected conditions.
6. **Test Witnessing Signatures (Reference SWE-066):**

   * Provides documented evidence that testing activities were observed and validated by stakeholders or independent software assurance personnel.
   * Confirms that testing was performed according to procedures and in compliance with project standards and requirements.

---

#### **8.54 Software Requirements Analysis**

**Improved Section:** Software assurance supports the software requirements analysis phase through independent reviews and evaluations to ensure requirements meet project objectives and are validated effectively. Key focus areas include completeness, clarity, consistency, traceability, and testability.

**Key Activities:**

1. **Requirement Identification:**

   * Verify that all functional, non-functional, operational, and environmental requirements are identified and accounted for, including system constraints and safety-critical requirements.
2. **Consistency Analysis:**

   * Ensure requirements are consistent with higher-level system requirements and customer needs.
   * Review for conflicts or ambiguities between requirements.
3. **Testability Assessment:**

   * Confirm each requirement can be validated through corresponding test cases.
4. **Bidirectional Traceability:**

   * Validate that all requirements trace to system-level requirements and downstream artifacts (design, testing, etc.).
5. **Risk Assessment:**

   * Identify risks related to incomplete or ambiguous requirements and present recommended mitigations.
6. **Requirement Change Management:**

   * Confirm that changes to requirements (additions, modifications, deletions) are managed and documented effectively.

**Outputs:**

* Identified, tracked, and resolved requirements issues.
* Documented assurance input for the SRS and RTM reviews.

---

#### **8.55 Software Design Analysis**

**Improved Section:** During software design analysis, software assurance focuses on verifying that the design aligns with the requirements, satisfies operational constraints, and is robust enough to meet mission objectives.

**Key Activities:**

1. **Requirement Compliance Analysis:**

   * Ensure the design addresses functional and non-functional requirements specified in the SRS.
   * Verify that critical requirements (safety, security, performance, etc.) have been integrated into the design.
2. **Architectural Integrity Review:**

   * Assess software architecture for modularity, maintainability, scalability, and fault tolerance.
   * Confirm that safety-critical and human-rated requirements are appropriately addressed in the architecture.
3. **Interfaces and Environment Validation:**

   * Verify the compatibility of software design with hardware, operational environments, and interfacing systems.
4. **Traceability Review:**

   * Verify that the design traces to all requirements and that no requirements are overlooked or partially addressed.
5. **Risk Identification:**

   * Identify and document design risks such as architectural mismatches, potential bottlenecks, or lack of redundancy in critical systems.
6. **Review of Safety-Critical and Mission Functions:**

   * Evaluate how failure scenarios or abnormal conditions are managed in the design.

**Outputs:**

* Assurance input into Software Design Document (SDD) reviews.
* Identified design risks and resolution recommendations.
* Assurance approval of design artifacts based on stakeholder and project compliance.

---

#### **8.57 Testing Analysis**

**Improved Section:** Software assurance ensures that testing is comprehensive, aligned with requirements, and adequately validated. Testing analysis focuses on reviewing test plans, procedures, execution, and results for effectiveness and thoroughness.

**Key Activities:**

1. **Test Coverage Analysis:**

   * Verify that all requirements (functional and non-functional) are covered by test cases, including edge cases and off-nominal scenarios.
2. **Test Procedure Review:**

   * Evaluate test procedures for accuracy, completeness, and alignment with the SRS.
   * Ensure test steps mimic the operational environment and validate the system as intended.
3. **Test Environment Validation:**

   * Confirm that the test environment is representative of the actual operational environment, including hardware, software, and system interfaces.
4. **Test Execution Oversight:**

   * Independently witness key tests (as documented with Test Witnessing Signatures per SWE-066).
   * Ensure adherence to test plans and monitor the proper execution of test cases.
5. **Defect Management:**

   * Review identified issues or failures and ensure corrective actions are planned and implemented.
   * Confirm regression testing for any changes introduced.
6. **Final Assessment of Validation Results:**

   * Analyze test results to confirm all requirements have been successfully validated and the software is ready to perform in the customer environment.

**Outputs:**

* Software test reports with identified assurance findings.
* Metrics tracking (e.g., test completion, traceability coverage, defect resolution).

---

## 7.3 Metrics

**Improved Section:** Metrics provide insight into the quality, consistency, and progress of requirements analysis, design, validation, and testing activities. Software assurance tracks these metrics to identify trends, assess risks, and suggest corrective actions. Key metrics include the following:

1. **Requirements Metrics:**

   * **# of Requirements Issues:** Number of incorrect, missing, or incomplete requirements vs. the number of issues resolved.
   * **# of Software Requirements:** Total count of project, subsystem, application-level requirements, etc.
   * **# of Orphan Requirements:** Number of requirements that do not trace to a parent requirement.
   * **Software Requirements Volatility:** Number of requirements added, deleted, or modified over time; track trends in TBDs and TBCs.
2. **Design and Architecture Metrics:**

   * **# of Architectural Issues Identified vs. Resolved:** Tracks the effectiveness of design reviews and risk mitigation.
3. **Testing and Validation Metrics:**

   * **Traceability Gaps:** Number of requirements without associated test cases.
   * **Validation Coverage:** Number of requirements tested vs. the total number of requirements.
   * **Test Execution Progress:** Number of tests executed vs. tests completed vs. total planned tests.
   * **Environment Testing Coverage:** Number of requirements validated in the customer environment.
4. **Defect Tracking Metrics:**

   * **Rework Metrics:** Number of defects (requirements, design, or testing) generated vs. closed.

**Uses:**

* Metrics are reviewed during milestone reviews (e.g., PDR, CDR, TRR) to assess project health and software quality.
* Identified trends indicate areas needing additional resources or more rigorous validation/verification.

---

This structured and enhanced guidance ensures clarity, actionable insights, and real-world alignment with requirements validation and assurance processes, supporting both quality and compliance with NASA standards.

[8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis)

[8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis)

[8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis)

Test Witnessing Signatures (See [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing))

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

Software assurance personnel play a critical role in ensuring that requirements validation is effective and comprehensive. They are responsible for verifying the adequacy of the project's requirements validation process, identifying risks and gaps, and advocating for rigorous validation methods tailored to the software's classification, operational environment, and criticality. This guidance outlines key actions and best practices that software assurance personnel should follow to support Requirement 4.1.7.

---

### **1. Collaborate in Requirements Validation Activities**

#### **Role of Software Assurance Personnel:**

* Actively participate in requirements validation activities to ensure they are performed consistently and yield accurate results.
* Facilitate coordination between stakeholders, developers, testers, and users to ensure all perspectives are accounted for during validation.
* Ensure traceability between requirements, design, implementation, and testing artifacts to verify operational alignment.

#### **Key Actions:**

* Review validation plans to determine if the methods, resources, and schedules appropriately satisfy the requirement’s intent.
* Confirm that stakeholders (e.g., users, customers, system engineers) are involved in the validation process to guarantee alignment with the operational context.
* Verify that validation outputs are documented for traceability and accountability.

---

### **2. Ensure Adequacy of Requirements Validation Methods**

#### **Role of Software Assurance Personnel:**

* Validate that methods selected for requirements validation are sufficient to demonstrate that the software will perform as intended in the customer environment.

#### **Key Actions:**

* Evaluate the chosen validation methods for each requirement (e.g., inspections, reviews, simulations, prototype testing) for adequacy and rigor.
* Advocate for validation techniques that align with the software classification and criticality:
  + For **Class A/B software**, ensure validation approaches are highly rigorous, leveraging formal methods or simulations of the actual customer environment.
  + For **Class D/E software**, allow simpler methods such as combining verification and validation activities but ensure safety-critical requirements are treated rigorously.
* Confirm that validation scenarios include off-nominal conditions (e.g., error handling, edge cases) and environmental extremes.

#### **Recommended Validation Techniques:**

* **Requirements Reviews:** Ensure requirements are understandable, testable, and aligned with system goals and environmental constraints.
* **Prototyping:** Use prototypes or simulations to validate functional and non-functional requirements.
* **Test Case Reviews:** Confirm that test cases adequately reflect the validated requirements.
* **Traceability Assessments:** Verify that traceability matrices link validated requirements to design, code, and tests.

---

### **3. Focus on Safety-Critical and Mission-Critical Requirements**

#### **Role of Software Assurance Personnel:**

* Provide additional oversight of stringent validation processes for safety-critical, human-rated, and mission-critical requirements to reduce risks of failure in operational environments.

#### **Key Actions:**

* Verify that additional rigor is applied to the validation of requirements related to:
  + Hazard controls and mitigations (safety-critical functions).
  + Security protocols (e.g., intrusion prevention and fault recovery systems).
  + Real-time or mission-critical operational scenarios.
* Confirm documentation of validation methods for these requirements in the Software Development Plan (SDP) or Software Management Plan (SMP).
* Ensure simulations, emulations, or environmental tests adequately mirror the intended operational environment for validation purposes.

---

### **4. Identify and Address Validation Gaps**

#### **Role of Software Assurance Personnel:**

* Act as an independent evaluator by identifying gaps or deficiencies in the requirements validation process and recommending corrective actions.

#### **Key Actions:**

* Perform independent audits or peer reviews of the requirements validation process, ensuring thoroughness and accuracy.
* Check for consistency across:
  + Requirements documentation.
  + Interface definitions (both internal and external).
  + The operational environment specified by the customer.
* Look for mismatches or ambiguities, such as:
  + Unit discrepancies (e.g., metric vs English units).
  + Missing edge cases or test scenarios.
  + Overlooked physical interfaces between software and hardware systems.
* Recommend corrective actions to address identified gaps (e.g., modify test cases, update requirements traceability matrices).

---

### **5. Monitor Validation of Interfaces**

#### **Role of Software Assurance Personnel:**

* Ensure interfaces (software-to-hardware, software-to-software, external system dependencies) are validated as part of the requirements validation process.

#### **Key Actions:**

* Verify interface requirements are defined and validated comprehensively, including:
  + Input/output data formats.
  + Timing constraints.
  + Communication protocols.
* Confirm that interfaces across subsystems, teams, or external contributors align with overall system requirements.
* Advocate for testing of interfaces under realistic operational conditions (e.g., emulated hardware interfacing).

---

### **6. Confirm Validation Outcomes**

#### **Role of Software Assurance Personnel:**

* Ensure that validation results confirm the software will meet its requirements under real-world conditions in the customer environment.

#### **Key Actions:**

* Evaluate validation results to confirm:
  + Every requirement has an associated test result or documented output confirming success.
  + The software meets both functional and non-functional requirements.
  + Resolutions to any validation discrepancies are tracked and closed.
* Cross-reference validated requirements with the operational environment to verify completeness.
* Ensure validation results are communicated to all stakeholders in a transparent and traceable manner (e.g., formally documented reports).

---

### **7. Promote Metrics Collection for Validation Effectiveness**

#### **Role of Software Assurance Personnel:**

* Advocate for the use of metrics to assess the effectiveness of the requirements validation process and to identify improvement opportunities.

#### **Key Actions:**

* Track metrics such as:
  + Percentage of requirements successfully validated on the first attempt.
  + Number of validation discrepancies discovered during system integration.
  + Number of requirements that were accepted but failed during testing due to inadequate validation.
  + Resolution times for any issues identified during validation.
* Monitor trends in validation activities to identify recurring problem areas or areas requiring stricter validation.

---

### **8. Ensure Compliance with NASA Standards**

#### **Role of Software Assurance Personnel:**

* Confirm that requirements validation processes comply with NASA standards, such as NPR 7150.2, and that safety-critical software adheres to NASA-specific constraints.

#### **Key Actions:**

* Review project adherence to NASA policies and directives:
  + Requirements validation must be documented in the Software Development Plan (SDP) or Software Management Plan (SMP).
  + Verify compliance with NASA mandates for safety-critical software (e.g., handling of preventive controls for hazards).
* Assist the project in ensuring that validation steps are auditable and meet NASA expectations.

---

### **9. Advocate for Independent Validation**

#### **Role of Software Assurance Personnel:**

* Recommend independent validation steps where feasible to reduce bias and verify critical requirements.

#### **Key Actions:**

* Encourage independent validation teams or external stakeholders to review high-priority requirements.
* Ensure validation relies on objective testing methods rather than team assumptions or informal processes.

---

### **10. Documenting Software Assurance Activities**

#### **Role of Software Assurance Personnel:**

* Provide comprehensive documentation of assurance activities surrounding requirements validation.

#### **Key Actions:**

* Maintain records of:
  + Validation methods reviewed.
  + Discrepancies identified and recommendations made.
  + Metrics tracked to assess validation effectiveness.
* Ensure validation activities are reported during project milestone reviews (e.g., Preliminary Design Review, Critical Design Review, Test Readiness Review).

---

### **Example Guidance for Different Software Classes**

#### **Class A/B Software (High-Risk Systems)**

* Perform formal requirements validation using simulation and operational testing in realistic environments.
* Use rigorous methods such as model-based validation or independent audits.

#### **Class D/E Software (Lower Risk Systems)**

* Combine verification and validation where feasible due to resource constraints, but treat safety-critical requirements with the highest rigor.
* Use prototypes, stakeholder reviews, or lightweight simulations when full-scale operational validation is impractical.

---

### **Key Software Assurance Deliverables**

1. **Requirements Validation Audit Report:** Documents discrepancies, risks, and recommendations for improvement.
2. **Validation Coverage Metrics:** Summarizes the completeness and robustness of requirements validation activities.
3. **Validation Process Review Record:** Confirms compliance with NASA standards and tracks validation results.
4. **Discrepancy Resolution Logs:** Lists corrective actions for requirements validation gaps.

By employing this guidance, software assurance personnel can ensure that requirements validation is effective, comprehensive, and tailored to the project's classification and criticality—ultimately enabling the software to perform as intended in the customer environment.

Software validation is a process performed throughout the software lifecycle to confirm that the software product, as provided (or as it will be provided), fulfills its intended use in its intended environment, and meets the requirements and expectations of the end user/customer and stakeholder(s).  In other words, validation ensures that “you built the right thing.”  Examples of validation methods and techniques include but are not limited to:  formal reviews, prototype demonstrations, functional demonstrations, peer reviews/inspections/walk-throughs, acceptance testing against mathematical models, analyses, and testing in the target environment. See also [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations).

**Requirements validation** is a process performed throughout the software life cycle to ensure that the requirements and resulting end product meet customer and stakeholder expectations. This includes ensuring that the requirements are defined for development, designed and implemented into the system, and tested in the target environment. Requirements validation begins during the requirements phase of the life cycle to check for errors and misinterpretations, as they may increase cost and cause excessive rework when detected later in the development process.

Various types of checks are performed throughout the requirements validation process to ensure the requirements documented in the Software Requirements Specification ([5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)) are valid. These checks include:

* Completeness checks
* Consistency checks
* Validity checks
* Realism checks
* Ambiguity checks
* Verifiability/Testability checks

The output of requirements validation during each life phase is the list of issues/problems and agreed-on actions that need to be resolved for the designated work product (see Tab 3 – 3.5 Select Life Cycle Products for Validation). The list of issues/problems indicates something was detected during the requirement validation process that requires further action. The list of agreed upon issues/problems should state the corrective action to be taken to fix the issue/problem. Typically, these issues/problems will be detected by the project’s stakeholders as they are primarily the ones performing the validation.

### 7.4.1 Requirements Validation Throughout the Life Cycle

All requirements must be validated and followed throughout the development life cycle. SWE-055 applies to products from initial requirements development through final product delivery.

* **Requirements Phase** – During this phase, the requirements should be reviewed to ensure they adequately reflect the stakeholder requirements and meet their expectations. Requirements categories to be reviewed should include, but are not limited to:
  + System requirements (note that systems-level validation procedures are described in NPR 7123.1, **NASA Systems Engineering Processes and Requirements** [041](#_tabs-<p></p>), with guidelines in NASA SP-2016-6105 Rev2, **NASA Systems Engineering Handbook** [273](#_tabs-<p></p>)).
  + Software requirements, which includes:
    - Functional requirements.
    - Data requirements.
    - Subsystem requirements.
    - Safety requirements.
    - Security requirements.
    - Performance and timing requirements.
    - Environmental requirements.
    - Integration requirements.
    - COTS, MOTS, GOTS, and reused software requirements.  
      To assess the SRS content, see [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification).
  + Interface requirements.
* **Design Phase** – During this phase, the design documentation is reviewed for feasibility and to ensure the requirements are adequately reflected in the design and are ready for implementation. The design documents to be reviewed may include:
  + Software Design Descriptions – To assess the SDD content, see [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description).
  + Interface Design Descriptions – To assess the IDD content, see [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description).
  + Interface Control Documents (ICDs)
* **Test Phase** – During the test phase, ensure the requirements are adequately tested and documented. Software Assurance must review all verification and validation test documentation. If the software is safety-critical, Software Assurance should witness enough of the validation testing to be confident that the tester is executing the test procedures as written, the software is adequately tested, and that the software will perform as expected.  
    
  The validation test documents to be reviewed include;
  + Acceptance Software Test Procedures – To assess the Acceptance Software Test Procedures content, see [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures).
  + Acceptance Software Test Report – To assess the Acceptance Software Test Report content, see [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report).
* **Release Phase** – As part of the software release process, some form of a Software Users Manual / User Guide (or similar training material) should be created/updated with description of the features/requirements implemented. Ensure the functionality of the software is documented in a manner that the users can understand what the features are supposed to do.
  + To assess the Software Users Manual content, see [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual).

### 7.4.2 Validation Planning

The project must plan and document the requirements validation activities to establish:

* Software products will be validated and their associated acceptance criteria.
* Processes and techniques that will be used to perform the validation.

Software Assurance should include any validation plans, processes, and methods/techniques in their Software Assurance Plan ([5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content)).

It doesn’t matter where software engineering’s validation plans are documented just as long as they are documented, but typically validation plans  are in the project’s Verification and Validation (V&V) Plan, Software Test Plan (see Topic [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)), or Software Development/Management Plan (see Topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)).

### 7.4.3 Validation Techniques & Methods

To perform complete requirements validation, multiple techniques and methods may be required based on the nature of the system, the environment in which the system will function, or even the phase of the development life cycle. Validation tests should be clearly outlined and described in the validation plans.  Most validations should be completed through inspection/review, demonstration, or testing where all involve the end users and other affected stakeholders. Ideally, the testing should be performed in the target environment of the stakeholder’s system.

Sample validation techniques or methods include, but are not limited to:

* **Formal reviews:**
  + Structured reviews in which specified steps are taken and roles are assigned to individual reviewers. (See Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists))
  + Formal reviews are useful for validating documents, such as software requirements specifications ([5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)), and allow for discussion and eventual agreement on the requirements among stakeholders with varied viewpoints.
    - The Software Requirements Review (SRR) ([7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria)) should address both ”getting the right requirements” and "getting the requirements right”.
  + Formal reviews allow for the identification of defects as well as suggested corrections.
  + Ensure requirements meet the intent of the operational concepts to ensure validation covers requirements.
  + Ensure descriptions of how the software will function in the customer’s operational or simulated environment are documented.
  + Use this technique to improve the quality of customer/stakeholder requirements.
  + Use this technique to ensure customer/stakeholder requirements and expectations are correctly captured.
* **Software peer reviews/inspections/walk-throughs:**
  + Relevant stakeholders investigate and review a product, such as requirements to determine if it meets preset criteria, identify product defects, and check for feasibility.
  + Peer reviews, walk-throughs, and inspections are useful for validating documents, such as SRSs, and allow for peer discussion of the technical aspects of the document content.
  + Inspections can be informal or formal with formal inspections being more structured with specific activities, assigned roles, and defined results (metrics, defects, etc.).
  + Inspections typically cover larger volumes of information than formal reviews and only identify the issues; solutions are typically not part of the peer review/inspection process.
  + For Additional Guidance on Peer Reviews see [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).
* **Demonstrate Functionality in Prototypes:**
  + Create a working prototype(s) of the software. This allows the software developers to evaluate the viability of high-risk requirements/elements and allows the customer/stakeholders to see the requirements implemented and iterate to get to the desired end-product.
  + Use this technique when budget and time allow, when stakeholders are hands-on, when the development model is an iterative process, etc.
  + Demonstrating specific actions or functions of the code.
  + Use this technique to validate select requirements related to questions such as "can the user do this" or "is this particular feature feasible."
* **Analysis:**
  + A "lightweight" version of simulation may be used for performing analysis without coding. For example, use spreadsheets to decompose and analyze algorithms to develop strategies for implementation without creating a simulation prototype.
  + For time-related aspects of validation, it may be necessary to use a different technique to expedite the analysis. For example, if a system is designed to run at real-time speed, it may not be feasible to execute and collect data for 100 tests/iterations at this rate to perform an analysis. It may be necessary to create a simulator/simulation to execute at X-times real-time in order to perform the analysis, validate the system, and/or troubleshot issues in a timely manner. This technique may also be necessary if the system has restricted or limited access .
  + Use this technique as part of an overall validation strategy or as a precursor step to full simulation.
  + Beta testing of new software applications. This may flush out requirements that were a good idea in theory are not in practice, leading to a refinement or change in the original requirement(s). It may also reveal new or missing requirements.
    - Use this technique when budget and time allow, when stakeholders are hands-on. when stakeholders (primarily user groups) and project schedules are amenable to this type of testing, etc.
* **Paper simulations/prototyping/storyboarding**: [304](#_tabs-<p></p>)
  + Drawing prototypes on paper.
    - This is a low-cost prototyping technique that might be useful in the early stages of high-level requirements development to capture and display visually the ideas and concepts (e.g., user interface) or for projects that don't have the budget for prototyping in software.
    - This is a good technique for developing user interface requirements.
    - Issues with prototyping on paper include storing for future reference and difficulty transforming into executable prototypes.
  + Typically, prototypes simply end up in requirements documents.
  + Commonly used to elicit and validate software user interfaces and interactions.
* **Computer modeling and simulation:**
  + The intent of validation is to assure that the final product works within the stakeholder environment, so use of modeling and simulation validation should be minimized.
  + Requirements validation can be supported by modeling various aspects of stakeholders’ needs, e.g., use cases (see below); capabilities decomposition; data flow; control flow; entities’ (objects’) properties and interactions; sequence of events; processes; states, modes, and transitions; and timing aspects.
    - **Use-cases** [304](#_tabs-<p></p>) model a system’s behavior, by identifying actors and their interaction with the system, and depicting a problem and solution from the user's point of view ("who" does "what" using the system). This technique is helpful when the focus of the system is on its user interaction and when it is easy to identify users (both human and other systems) and services or functionality provided to them by the system.
  + Models can be represented using different notations, e.g., graphical notations/languages (e.g., UML/SysML) or mathematical notations.
  + Some models are executable; model execution (simulation) offers additional insight into software behavior and dynamic aspects that a purely descriptive model is not able to provide.
  + There are tools for developing, managing, evolving, and sharing models and simulations, e.g., MagicDraw, MATLAB, and Simulink.
* **Viewpoint-oriented requirements validation**: [304](#_tabs-<p></p>)
  + Identify conflicting requirements based on the viewpoints of various stakeholders.
  + Use this technique when there is a need to identify conflicting requirements based on viewpoints or when it is important to consider requirements from multiple perspectives.
* **Formal methods:**
  + Mathematically rigorous techniques.
  + Use this technique to validate formal requirements specifications or to validate key properties of requirements. [181](#_tabs-<p></p>)

* **Development and Review of test cases:**
  + Review test cases individually and as a set to confirm coverage of system scenarios [209](#_tabs-<p></p>).
  + Review test cases with stakeholders to confirm functional and operational scenarios (as defined by the requirements).
  + Development and review of test cases may help find problems in the requirements since it requires completely thinking through the operation of the application. If the test case is difficult to create, then it’s usually an indicator of a poorly written requirement. The requirement should be written in a manner that the desired test result can be easily obtained.
    - This technique is particularly useful for test-driven software development.
* **Security Validation Techniques** – Some of the following techniques can be used when identifying security threats and vulnerabilities. These techniques may be manual, automated, or a combination of both.[689](#_tabs-<p></p>)
  + Simulation and modeling
  + Penetration testing
  + Friendly hacking
  + Fuzzy testing
  + Re-play testing

### 7.4.4 Requirements Traceability Matrix

The requirements traceability matrix may also be useful to ensure that all requirements are validated. The matrix should include:

* Links to higher-level requirements that identify/define user needs.
* Traces to the design components, code, and test case(s).
* A place to record validation methods (if not included in the test procedures).
* A place to record or reference the validation results (Results should be recorded in a Test Report,)

See also [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations), Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009)

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

To demonstrate compliance with Requirement 4.1.7 and provide objective evidence of requirements validation, the project must present clearly documented artifacts, analysis outputs, and test results. These artifacts serve as proof that the requirements have been reviewed, analyzed, validated, and traced throughout the software lifecycle, including alignment with operational needs, customer expectations, and environmental constraints.

---

### **Categories of Objective Evidence**

Objective evidence for Requirement 4.1.7 falls into several categories:

#### **1. Requirements Validation Documentation**

Artifacts that confirm requirements have been systematically validated in accordance with the customer environment and operational conditions.

**Examples:**

* **Requirements Validation Plan:**

  + A documented plan outlining the methods, tools, schedules, and personnel involved in requirements validation.
  + Includes strategies for validating safety-critical, human-rated, and mission-critical requirements.
* **Requirements Review Records:**

  + Meeting minutes, annotated requirements documentation, or worksheets from requirements validation reviews.
  + Stakeholder approvals confirming that requirements satisfy their needs and can function in the operational environment.
* **Validation Criteria:**

  + Documentation of criteria used to determine whether requirements meet operational and environmental specifications.
  + Example: Criteria for real-time performance in low-bandwidth environments or extreme temperature conditions.

---

#### **2. Requirements Traceability**

Documentation that demonstrates traceability of requirements as they progress through validation, design, implementation, and testing activities.

**Examples:**

* **Requirements Traceability Matrix (RTM):**

  + Shows bidirectional traceability:
    - **Requirements → Design Elements:** Each requirement is linked to corresponding design components.
    - **Requirements → Test Cases:** Ensures every requirement is validated via associated test cases and test procedures.
    - **Requirements → Expected Environment Requirements:** Confirms that requirements are fully aligned with environmental constraints and hardware/software interfaces.
* **Traceability Reports:**

  + Outputs showing gaps or discrepancies resolved during traceability analysis (e.g., an orphaned requirement without validation test coverage).

---

#### **3. Validation Test Artifacts**

Test-related documentation that demonstrates requirements have been validated through testing, reviews, simulations, or prototypes.

**Examples:**

* **Test Procedures:**

  + Documented procedures detailing how tests validate specific requirements (e.g., performance, safety, security, or compatibility).
  + Includes operational environment simulation details (e.g., hardware/software integration tests).
* **Test Cases:**

  + Specific test cases traceable to validated requirements.
  + Test cases must cover edge cases, nominal and off-nominal conditions, and expected environmental constraints.
* **Test Results/Reports:**

  + Summary of executed test cases showing which requirements were validated successfully and which required rework.
  + Includes screenshots, logs, or metrics recorded during testing.
  + Example: A test report confirming telemetry data transmission matches environmental constraints (e.g., performance under low bandwidth).
* **Simulation Results:**

  + Outputs from environment simulations (e.g., hardware emulation or stress testing) that validate requirements in operational contexts.

---

#### **4. Independent Verification and Validation (IV&V) Evidence**

Artifacts produced during IV&V activities (if applicable) to confirm requirements validation was conducted independently and rigorously.

**Examples:**

* **IV&V Checklists:**

  + Detailed analysis sheets highlighting validated requirements, associated test cases, and discrepancies identified during IV&V reviews.
* **Independent Validation Reports:**

  + Reports confirming independent validation activities (e.g., Independent Simulation Testing, Independent Requirements Analysis).
  + Example: External testing teams verifying that safety-critical software requirements operate correctly under simulated customer conditions.

---

#### **5. Risk and Issue Resolution Documentation**

Evidence of risk assessments and issue resolutions related to requirements validation.

**Examples:**

* **Risk Logs:**

  + Logs identifying risks discovered during requirements validation (e.g., gaps in test cases or ambiguous interface requirements).
  + Includes risk mitigation plans and corrective actions taken.
* **Discrepancy Resolution Logs:**

  + Records of discrepancies discovered during test validation (e.g., mismatch between requirements and environment constraints) and how these issues were resolved.
  + Example: Corrective actions documenting a resolved mismatch between the units used in ground-based trajectory modeling and flight software requirements (per Mars Climate Orbiter mishap, Lesson #0641).

---

#### **6. Stakeholder Sign-offs**

Stakeholder involvement is essential to validating requirements and confirming they are aligned with mission objectives. Objective evidence includes formal approvals or sign-offs by stakeholders.

**Examples:**

* **Stakeholder Validation Signatures:**

  + Formal sign-offs by end users, customers, and reviewers indicating that requirements meet their mission and operational needs.
* **Requirements Review Results:**

  + Evidence of stakeholder participation during validation reviews, including annotated requirements documents showing stakeholder feedback or suggestions incorporated.

---

#### **7. Metrics and Analysis Reports**

Quantitative data that shows the effectiveness of requirements validation efforts.

**Examples:**

* **Validation Coverage Metrics:**

  + Metrics showing coverage rates for validated requirements (e.g., “100% of detailed requirements have associated test cases successfully executed”).
* **Requirements Volatility Metrics:**

  + Reports on changes made during validation (e.g., "5 requirements modified due to environment constraints identified during validation reviews").
* **Risk Trend Analysis:**

  + Reports showing how risks identified during requirements validation activities were tracked and resolved over time.

---

### **Best Practices for Collecting Objective Evidence**

1. **Centralized Documentation:**

   * Maintain all requirements validation artifacts in a centralized repository accessible to the software assurance team.
2. **Use of Tools and Automation:**

   * Leverage tools such as requirements management software (e.g., IBM DOORS, Jama Connect) to document traceability and validation activities.
3. **Stakeholder Collaboration:**

   * Involve stakeholders throughout validation activities to ensure their objectives and operational concerns are fully addressed.
4. **Comprehensive Testing:**

   * Perform tests under diverse operational scenarios (e.g., hardware interfaces, environmental constraints) and include rigorous validations for mission-critical requirements.
5. **Independent Reviews:**

   * Incorporate independent reviews (IV&V teams, peer reviews) to confirm the adequacy of validation efforts.

---

### **Example Evidence Matrix**

| **Artifact Type** | **Description** | **Purpose** |
| --- | --- | --- |
| Requirements Validation Plan | Defines validation methods, tools, and personnel needed to validate requirements. | Ensures structured and documented validation activities. |
| Traceability Matrix | Connects requirements to test cases, design elements, and environmental constraints. | Demonstrates alignment across lifecycle artifacts. |
| Test Reports | Provides detailed evidence of test execution and validation results for each requirement. | Confirms successful validation in the customer environment. |
| Risk Log | Documentation of risks identified during validation and resolution actions. | Tracks and mitigates validation-related risks. |
| Stakeholder Approval Records | Formal stakeholder sign-offs confirming requirements met operational expectations. | Confirms stakeholder alignment and customer satisfaction. |
| Metrics Reports | Summarizes validation completeness, requirements issues resolved, and testing progress. | Demonstrates validation coverage and project progress. |

---

By providing a combination of these artifacts and practices, the project team can meet Requirement 4.1.7 and substantiate that requirements validation activities are comprehensive, traceable, and aligned with the customer environment to ensure mission success.

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
