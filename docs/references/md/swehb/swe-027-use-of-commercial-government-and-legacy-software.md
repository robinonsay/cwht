# SWE-027 - Use of Commercial Government and Legacy Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695410. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software

SWE-027 - Use of Commercial, Government, and Legacy Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695410)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695410&showCommentArea=true&showComments=true#addcomment)

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

3.1.14 The project manager shall satisfy the following conditions when a COTS, GOTS, MOTS, OSS, or reused software component is acquired or used: 

a. The requirements to be met by the software component are identified.

b. The software component includes documentation to fulfill its intended purpose (e.g., usage instructions).

c. Proprietary rights, usage rights, ownership, warranty, licensing rights, transfer rights, and conditions of use (e.g., required copyright, author, and applicable license notices within the software code, or a requirement to redistribute the licensed software only under the same license (e.g., GNU GPL, ver. 3, license)) have been addressed and coordinated with Center Intellectual Property Counsel.

d. Future support for the software product is planned and adequate for project needs.

e. The software component is verified and validated to the same level required to accept a similar developed software component for its intended use.

f. The project has a plan to perform periodic assessments of vendor reported defects to ensure the defects do not impact the selected software components.

## 1.1 Notes

The project responsible for procuring off-the-shelf software is responsible for documenting, prior to procurement, a plan for verifying and validating the software to the same level that would be required for a developed software component. The project ensures that the COTS, GOTS, MOTS, reused, and auto-generated code software components and data meet the applicable requirements in this directive assigned to its software classification as shown in Appendix C.

## 1.2 History

Click here to view the history of this requirement: SWE-027 History

SWE-027 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.3.1 The project shall ensure that when a COTS (Commercial Off the Shelf), GOTS (Government Off the Shelf), MOTS (Modified Off the Shelf), reused, or open source software component is to be acquired or used, the following conditions are satisfied:   1. The requirements that are to be met by the software component are identified. 2. The software component includes documentation to fulfill its intended purpose (e.g., usage instructions). 3. Proprietary, usage, ownership, warranty, licensing rights, and transfer rights have been addressed. 4. Future support for the software product is planned. 5. The software component is verified and validated to the same level of confidence as would be required of the developed software component. |
| Difference between A and B | Removed open source requirement and created SWE-149; Clarified proprietary rights and usage rights need to be addressed; Addresses adequacy of plans to allow for future support; Added requirement f. |
| B | 3.9.2 The project manager shall satisfy the following conditions when a Commercial Off the Shelf (COTS), Government Off the Shelf (GOTS), Modified Off the Shelf (MOTS), or reused software component is to be acquired or used:  a. The requirements to be met by the software component are identified.  b. The software component includes documentation to fulfill its intended purpose (e.g., usage instructions).  c. Proprietary rights, usage rights, ownership, warranty, licensing rights, and transfer rights have been addressed.  d. Future support for the software product is planned and adequate for project needs.  e. The software component is verified and validated to the same level required to accept a similar developed software component for its intended use.  f. The project has a plan to perform periodic assessments of vendor reported defects to ensure the defects do not impact the selected software components. |
| Difference between B and C | Added OSS - which merges SWE-149 into this requirement. |
| C | 3.1.14 The project manager shall satisfy the following conditions when a Commercial Off the Shelf (COTS), Government Off the Shelf (GOTS), Modified Off the Shelf (MOTS), Open Source Software (OSS), or reused software component is acquired or used:   1. 1. The requirements to be met by the software component are identified.    2. The software component includes documentation to fulfill its intended purpose (e.g., usage instructions).    3. Proprietary rights, usage rights, ownership, warranty, licensing rights, and transfer rights have been addressed.    4. Future support for the software product is planned and adequate for project needs.    5. The software component is verified and validated to the same level required to accept a similar developed software component for its intended use.    6. The project has a plan to perform periodic assessments of vendor reported defects to ensure the defects do not impact the selected software components. |
| Difference between C and D | Modified item c. to ensure that the appropriate activities are done and coordinated with the Center IP counsel. |
| D | 3.1.14 The project manager shall satisfy the following conditions when a COTS, GOTS, MOTS, OSS, or reused software component is acquired or used:   a. The requirements to be met by the software component are identified.  b. The software component includes documentation to fulfill its intended purpose (e.g., usage instructions).  c. Proprietary rights, usage rights, ownership, warranty, licensing rights, transfer rights, and conditions of use (e.g., required copyright, author, and applicable license notices within the software code, or a requirement to redistribute the licensed software only under the same license (e.g., GNU GPL, ver. 3, license)) have been addressed and coordinated with Center Intellectual Property Counsel.  d. Future support for the software product is planned and adequate for project needs.  e. The software component is verified and validated to the same level required to accept a similar developed software component for its intended use.  f. The project has a plan to perform periodic assessments of vendor reported defects to ensure the defects do not impact the selected software components. |

## 1.3Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

All software used on a project must meet the project requirements and be tested, verified, and validated, including the incorporated Commercial Off the Shelf (COTS), Government Off the Shelf (GOTS), Modified Off the Shelf (MOTS), Open Source Software (OSS) or reused software components. The project must know that each COTS, GOTS, MOTS, OSS, or reused software component meets NASA requirements; that all of the legal requirements for proprietary rights, usage rights, ownership, warranty, licensing rights, and transfer rights are understood and met by the project’s planned use. That software's future support for the software is planned.  To reduce the risk of failure, the project performs periodic assessments of vendor-reported defects to ensure the defects do not impact the selected software components.

The use of **Commercial Off-The-Shelf (COTS)**, **Government Off-The-Shelf (GOTS)**, **Modified Off-The-Shelf (MOTS)**, **Open-Source Software (OSS)**, or **reused software components** can significantly reduce development time and cost while leveraging existing solutions. However, these software components must meet the same reliability, safety, and mission-critical standards as custom-developed software. This requirement ensures that projects integrate such software components responsibly and verify that they meet NASA’s technical, safety, intellectual property (IP), and lifecycle support needs.

This requirement provides a structured framework for acquiring and integrating pre-existing software components into NASA systems. By addressing requirements, IP and licensing issues, V&V, lifecycle planning, and defect monitoring, NASA ensures that COTS, GOTS, MOTS, OSS, and reused software align with mission needs and meet the same rigorous standards as newly developed software. This approach reduces technical, operational, and legal risks while enabling projects to leverage time and cost advantages provided by pre-existing solutions.

## 2.1 Why 3.1.14 is Critical for NASA Software Projects

NASA software systems often operate in highly regulated, safety-critical, and performance-intensive environments. The use of third-party or pre-existing software components introduces certain risks and challenges that must be mitigated, including:

* Ensuring compliance with project requirements.
* Addressing intellectual property rights and licensing conditions.
* Evaluating the reliability, maintainability, and future supportability of the software.
* Verifying and validating that the software can perform its intended function under NASA’s unique operational demands.

To address these concerns, projects must follow a structured process to evaluate and manage COTS, GOTS, MOTS, OSS, and reused components, ensuring they meet the same standards as newly developed software while preserving IP integrity and managing vendor dependencies.

## 2.2 Breaking Down the Requirements Conditions

#### **a. Identifying Requirements for the Software Component**

To ensure that the COTS, GOTS, MOTS, OSS, or reused software component aligns with the project’s goals, the requirements to be met by the component must be explicitly identified. This step involves:

* Mapping the functional, performance, safety, and security requirements of the component to ensure that it fulfills its intended role.
* Documenting which specific project requirements the component fulfills, and any gaps in coverage or performance.

**Rationale:**  
Defining these requirements ensures the software component fits within the overall system design, minimizing the risk of incompatibility, unmet needs, or costly rework later in the project lifecycle.

#### **b. Documentation for Intended Purpose**

Pre-existing software often comes with vendor-provided or commonly available documentation, such as usage instructions, configuration guides, or integration manuals. This documentation is critical for proper use and lifecycle management.

**Rationale:**

1. Documentation ensures that the project team understands how to configure, deploy, and monitor the component in accordance with its intended purpose.
2. It provides a foundation for troubleshooting, testing, validation, and maintenance activities.

For cases where documentation is incomplete, the project team must assess the risk of using the component versus identifying alternatives or creating its own documentation to fill the gaps.

#### **c. Addressing Intellectual Property Rights and Licensing Terms**

Before integrating the component, the project team must verify and coordinate proprietary rights, usage rights, and licensing conditions with the **Center Intellectual Property (IP) Counsel**. Key licensing details to address include:

* Transfer rights and redistribution conditions (e.g., requirements to redistribute OSS under the same license).
* Ownership and warranty terms.
* Embedding of copyright, author, and license notices where required (e.g., GNU GPL v3 for OSS).

**Rationale:**  
NASA’s software systems are diverse and often shared among multiple agencies, organizations, or public groups. Failing to comply with IP and licensing obligations:

* Risks legal violations, including improper redistribution of software.
* Could prevent the sharing or transferring of NASA software where proprietary terms are restrictive.
* Introduces potential licensing compatibility issues in mixed-use systems (e.g., OSS combined with COTS/GOTS).

#### **d. Ensuring Adequate Future Support**

Projects must ensure that the software will continue to meet needs across the lifecycle through vendor or community-provided support. Future support considerations include:

* Long-term maintenance agreements for COTS/GOTS software.
* Community or developer support for OSS.
* Plans for long-term sustainability if the software becomes obsolete or unsupported.

**Rationale:**  
Without sufficient future support, projects could face issues such as:

* Unpatched vulnerabilities in critical software.
* Loss of support for upgrades, leaving the project with outdated systems.
* Long-term operational risks if vendor contracts expire or OSS communities disband.

Assessing and documenting a plan for future support reduces operational risks in long-duration projects.

#### **e. Verifying and Validating the Software for Its Intended Use**

To minimize risks, the software component must undergo the same level of **verification and validation (V&V)** as a newly developed software component performing the same function. V&V activities include:

* Functional testing to validate requirements fulfillment.
* Security testing to verify robustness against vulnerabilities.
* Stress and reliability testing under mission conditions.

**Rationale:**  
Pre-existing software may not have been developed or validated under the same rigorous standards needed for NASA’s use cases. V&V ensures:

* The component performs as intended within NASA’s system.
* Any deficiencies (e.g., missing functionality, reduced reliability) are identified and addressed before integration.

#### **f. Periodic Assessment of Vendor-Reported Defects**

The project must periodically review defects or vulnerabilities reported by the software vendor (for COTS/GOTS/MOTS) or user communities (for OSS). If critical defects are uncovered:

* Determine whether they impact the project’s use case.
* Take appropriate action to mitigate risks (e.g., applying patches, discontinuing use, implementing workarounds).

**Rationale:**  
In today’s fast-evolving software environment, defect reports, security patches, and upgrades are common. Regular monitoring ensures:

* Project software remains secure, stable, and aligned with current needs.
* Critical defects do not propagate downstream into the project, potentially jeopardizing mission success.

## 2.3 Notes: Verification, Validation, and Software Classification

### 2.3.1 Verification and Validation Plan

Projects must develop a plan for verifying and validating the software **before procurement** to ensure components meet their requirements. This should include:

* V&V activities needed to evaluate functional and non-functional requirements.
* The level of testing and verification corresponding to the **software classification** and safety criticality (Appendix C).

**Rationale:**  
By planning upfront, the project ensures the software is thoroughly assessed and minimizes surprises during integration and testing. For example, Class B safety-critical flight software would require far more rigorous V&V than Class E administrative software.

#### **2.3.2 Software Classification**

The software must be evaluated against NPR 7150.2 requirements according to **software classification** (SWE-020). This ensures classification-specific requirements (e.g., safety-critical software) are properly addressed, even for pre-existing components like COTS, GOTS, or OSS.

# 3. Guidance

Software components that are either acquired off-the-shelf or derived from existing models offer great flexibility in development but come with unique challenges that require careful evaluation and management. This guidance provides an enhanced framework for handling **Commercial Off-The-Shelf (COTS)**, **Government Off-The-Shelf (GOTS)**, **Modified Off-The-Shelf (MOTS)**, **Open Source Software (OSS)**, **reused software**, and **auto-generated code**. These components are considered vital to modern software development at NASA, but each must satisfy stringent requirements to ensure safety, reliability, legal compliance, and long-term lifecycle compatibility.

This enhanced guidance provides a systematic approach to integrating non-hand-generated software components into NASA projects, focusing on requirement identification, licensing compliance, future support, fitness validation, defect management, and lifecycle planning. By adhering to this framework, projects can effectively incorporate COTS, GOTS, MOTS, OSS, reused, or auto-generated software into NASA systems while mitigating legal, operational, and reliability risks.

## 3.1 Identifying Requirements for Non-Hand-Generated Software (Section 3.1)

#### **Key Objectives**

* **Why Requirements Matter**: For software developed externally (COTS, GOTS, MOTS, OSS, reused, or auto-generated), identifying project-specific requirements ensures that the component meets the intended functional, safety, and performance criteria. Requirements provide a foundation for risk evaluation, testing, and verification activities.
* **Risk Management**: Understanding how the integration of externally developed components impacts the software system’s overall risk posture allows projects to anticipate the consequences of adoption, secure mitigation strategies, and avoid critical vulnerabilities.

#### **Steps to Identify Requirements**

1. **Define Objectives**: Fully specify what the component is expected to accomplish, including functional and non-functional requirements.
2. **Alignment with System Needs**: Map the identified requirements back to the overall system design to ensure compatibility.
3. **Testing Scope Based on Requirements**: Testing and validation activities must reference identified requirements to verify behavior and fitness for the intended function.

#### **Importance**

A failure to specify and test against requirements prevents comprehensive evaluation of the component’s functionality and risks introducing unintended behavior in critical systems.

## 3.2 Obtaining Adequate Documentation (Section 3.2)

#### **Key Objectives**

Documentation ensures the project team has a clear understanding of how to integrate, configure, and use the software component. This includes:

* **Usage Instructions**: Ensuring proper functionality within the software ecosystem.
* **Operational Guides**: Enabling teams to install, configure, customize, and maintain the component.

#### **Steps to Obtain Documentation**

1. **Verify Completeness**: Evaluate whether vendor-provided or OSS documentation is sufficient to address the component’s proper usage and integration requirements.
2. **Supplement Missing Documentation**: If existing documentation is incomplete, the project must generate additional materials to bridge gaps, especially for deployed systems.
3. **Ensure Clarity**: For complex components like OSS or MOTS tools, assess whether the documentation is up-to-date and supports non-expert users.

#### **Importance**

Inadequate documentation increases integration risks, user errors, and poor lifecycle support.

## 3.3 Addressing Proprietary Rights and Usage Licenses (Sections 3.3–3.5)

#### **Key Objectives**

* Ensure compliance with legal agreements, ownership rights, and licensing obligations to avoid copyright infringement, violation of software licenses, or conflicts in intellectual property.

#### **Steps to Review Usage and Licensing Rights**

1. **Understand All Rights**: Work with legal advisors and Intellectual Property (IP) Counsel to ensure that proprietary rights, warranties, and restrictions are documented and understood.
2. **Review OSS Licenses**:
   * Carefully evaluate OSS licenses for redistribution requirements, intellectual property claims, and obligations like attribution or reciprocal licensing requirements (e.g., GNU GPL v3).
   * Ensure compatibility with NASA policies and government systems.
3. **Ensure Legal Readiness**: Address legal concerns such as the termination of licenses due to non-compliance or conflicting third-party rights.

#### **Understanding the License Scope**

* **Legal Code Over Language**: Carefully read the full legal code of the license — human-readable summaries may omit critical conditions like jurisdiction-specific terms.
* **Mark Boundaries of the License**: Determine which elements of the software are subject to restrictions and whether additional permissions may be required.

#### **Importance**

Violating license agreements could expose NASA to legal liability or restrict future project use.

## 3.4 Planning Future Support for Non-Hand-Generated Software (Section 3.8)

#### **Key Objectives**

Non-hand-generated software products often have finite lifetimes or external dependencies (e.g., vendor support or OSS community activity). Ensuring future support mitigates risks associated with software obsolescence or discontinuation.

#### **Steps to Plan Future Support**

1. **Supplier Agreements**: Develop supplier agreements to escrow source code or ensure the availability of long-term support plans.
2. **Mitigation Plans**: Include contingencies for supplier loss, software version recalls, or unexpected licensing revocations.
3. **Defect Tracking**: Establish mechanisms to monitor defect reports and rapidly deploy fixes or mitigations for system-critical impact.

#### **Importance**

Without future support planning, projects risk losing access to critical features, security patches, and compatibility over time.

## 3.5 Ensuring Fitness for Use (Section 3.9)

#### **Key Objectives**

Every software component must be validated to confirm its reliability, safety, and security under intended operational conditions.

#### **Steps to Verify Fitness for Use**

1. **Testing Scope**: Test only the features and functions that are actively in use during the project lifecycle — discard or disable unrelated functionality unless verified as safe.
2. **Adaptation V&V**: For MOTS or reused software, ensure verification and validation processes consider modifications made to the original source.
3. **Criticality-Based Effort**: Tailor V&V levels to the software classification (e.g., Class A systems require rigorous safety-critical testing).

#### **Examples**

* Use vendor-provided test suites for critical system matching, such as real-time operating systems (RTOS).
* For OSS, apply NASA’s software environment to verify interoperability and performance against project requirements.

#### **Importance**

Failure to validate components can lead to unexpected system failures, reduced reliability, or safety concerns.

## 3.6 Assessing Vendor-Reported Defects (Section 3.10)

#### **Key Objectives**

Proactively assessing vendor-reported defects helps projects maintain awareness of unresolved issues and prevents risks from propagating into critical systems.

#### **Steps for Defect Assessment**

1. **Set Procedures**: Incorporate vendor defect reports into regular project hazard evaluations.
2. **Analyze Impact**: Assess the extent of defects on safety, reliability, and performance within the project application environment.
3. **Update Risk Plans**: Implement mitigation actions for defects that impact project objectives.

#### **Importance**

Untracked defects can lead to critical failures or vulnerabilities in NASA systems.

## 3.7 Software Reuse and Modification (Section 3.11)

#### **Key Objectives**

Utilizing legacy or heritage code as part of software reuse can reduce costs but requires careful evaluation of risks associated with incomplete documentation or incompatibility.

#### **Steps for Software Reuse**

1. **Evaluate Effort**: Assess the cost and effort required to adapt legacy code for the current application area.
2. **Perform V&V**: Determine whether modifications to reused software meet the confidence levels necessary for project classification and criticality.

#### **Importance**

Software reuse poses risks from unclear requirements or excessive dependence on legacy systems without validation.

## 3.8 Certification by Outside Sources (Section 3.12)

#### **Key Objectives**

Leverage certification data from regulatory entities cautiously, ensuring the software meets NASA's specific requirements even if deemed acceptable elsewhere.

#### **Steps to Incorporate Certifications**

1. **Vendor Evaluation**: Consider the environment of certification (e.g., FAA approval) and verify alignment with NASA’s unique operational conditions.
2. **Engineering Judgment**: Determine acceptable degrees of use when reliance on external certifications applies.

#### **Importance**

Certification outside NASA may not address unique system environments and risks.

## 3.9 Integrating Off-The-Shelf Software (Section 3.13)

#### **Key Objectives**

Different types of OTS software (COTS, GOTS, MOTS, OSS, auto-generated software) require tailored integration guidance based on functionality and criticality.

#### **Steps for Integration**

1. **Checklist Use**: Employ tools and checklists to assess software lifecycle decisions, including acquisition, V&V, and support.
2. **Safety Assessment**: Conduct safety and risk evaluations for complex systems (e.g., launch vehicle control) or portions of software solutions.

#### **Importance**

Standardizing lifecycle evaluations for OTS software ensures proper integration with NASA systems.

## 3.10 Embedded Software

NASA commonly uses embedded software applications written by/for NASA for engineering software solutions. Embedded software is software specific to a particular application as opposed to general-purpose software running on a desktop. Embedded software usually runs on custom computer hardware ("avionics"), often on a single chip.

Care must be taken when using vendor-supplied board support packages (BSPs) and hardware-specific software (drivers), typically supplied with off-the-shelf avionics systems. BSPs and drivers act as the software layer between the avionics hardware and the embedded software applications written by/for NASA. Most central processing unit (CPU) boards have BSPs provided by the board manufacturer or third parties working with the board manufacturer. Driver software is provided for serial ports, universal serial bus (USB) ports, interrupters, modems, printers, and many other hardware devices.

BSPs and drivers are hardware dependent, often developed by third parties on hardware/software development tools that may not be accessible years later. Risk mitigation should include hardware-specific software, such as BSPs, software drivers, etc.

Board manufacturers provide many BSPs and drivers as binary code only, which could be an issue if the supplier is not available and BSP/driver errors are found. It is recommended that a project using BSPs/drivers maintain a configuration managed version of any BSPs with release dates and notes. Consult with avionics (hardware) engineers on the project to see what actions may be taken to manage the BSPs/drivers.

Consideration should also be given to how BSP/driver software updates are to be handled, if and when they are made available, and how it will become known to the project that updates are available?

Vendor reports and user forums should be monitored from the time hardware, and associated software are purchased through a reasonable time after deployment. Developers should monitor suppliers or user forums for bugs, workarounds, security changes, and other modifications to the software that, if unknown, could derail a NASA project. Consider the following snippet from a user forum:

"Manufacturer Pt. No." motherboard embedded complex electronics contains malware.  
Published: 2010-xx-xx

A "Manufacturer" support forum identifies "manufacturer's product" motherboards that contain harmful code. The embedded complex electronics for server management on some motherboards may contain malicious code. There is no impact on either new servers or non-Windows based servers. No further information is available regarding the malware, malware mitigation, the serial number of motherboards affected, or the source.

|  |  |  |
| --- | --- | --- |
|  | **Example Questions for Assessing COTS. MOTS, OSS, and reuse software for use by or in a System** | |
|  | This is not a complete list. Each Center or Project should add to, remove, or alter the list which applies to their tools. Not all questions apply to all tool types. This checklist helps the thought processes when considering COTS, MOTS, OSS, and reused software or software tools. If the system has safety-critical components that could contribute to a hazard by either providing a false or inaccurate output or developing software with flawed algorithms, paths, execution timing, etc., consider using the example safety checklist below. | |
| Y/N/ NA/ unknown (?) |  |  |
|  | 1. | **What requirements does the intended OTS or OSS or reuse software fulfill for the system?** |
|  | a. | Is it a standalone tool used to produce, develop, or verify software  (or Hardware) for a safety-critical system? |
|  | b. | Is this an embedded product? |
|  | 2. | **Why this COTS, MOTS, OSS, or reuse software product, why this vendor?** |
|  | a. | What is the COTS, MOTS, OSS, or reuse software pedigree? |
|  | b. | Is it a known and respected company? |
|  | c. | What does the market/user community say about it? |
|  | d. | Does the purchasing company/industry have a track record of using this product? |
|  | e. | What is the volatility of the product? Of the vendor? |
|  | f. | The vendor will provide what agreements and services? |
|  | g. | Is escrow of the COTS, MOTS, OSS, or reuse software a viable option? |
|  | h. | What documentation is available from the vendor? |
|  | i. | Are operators/user guides, installation procedures, etc., normally provided? |
|  | j. | Is additional requested documentation available? (perhaps at additional cost) Examples might include requirements, design, tests, problem reports, development and assurance processes, plans, etc. |
|  | 3. | **What training is provided or available?** |
|  | 4. | **Does the vendor share known problems with their clients?** |
|  | a. | Is there a user group? |
|  | b. | Are there a useful means to notify customers of problems (and any solutions/workarounds) found by the company or by another customer? |
|  | c. | Do they share their risk and or safety analyses of new and existing problems/errors? |
|  | 5. | **What plan/agreement is there for if the vendor or product ceases to exist?** |
|  | a. | What if the vendor goes out of business? |
|  | b. | What if another company buys the vendor? |
|  | c. | What if the vendor stops supporting either the product or the version of the product used? |
|  | 6. | **Why not develop it in the house ( this may or may not be obvious)?** |
|  | 7. | **How are those requirements traced throughout the life of the product?** |
|  | 8. | **What performance measures are expected and needed?** |
|  | 9. | **What requirements does it not meet that will need to be fulfilled with developed code?** |
|  | 10. | **Will wrappers and or glueware be needed?** |
|  | 11. | **Will other tools and support software be needed  (e.g., special tools for programming the cots, adaptors for specific interfaces, drivers specific to an operating system or output device, etc.)?** |
|  | 12. | **Does it need to be programmed? Do one or more applications run on the COTS?** |
|  | 13. | **What features does the COTS, MOTS, OSS, or reuse software have that are not used?** |
|  | a. | How are they “turned off,” if that is possible? |
|  | b. | Is a wrapper necessary to assure correct inputs to and/or outputs from the COTS, MOTS, OSS, or reuse software? |
|  | c. | Can the unwanted features be “safe,” prevented from inadvertent functioning? |
|  | d. | Could operators/users/maintenance incorporate the unused features in the future? |
|  | i. | What would be the implications? |
|  | ii. | What would be the controls? |
|  | iii. | What would be the safety ramifications? |
|  | 14. | **How can it verified and validated functionally, performance-wise, stress/fault-tolerant?** |
|  | a. | Outside the intended system? |
|  | b. | With any programming or applications? |
|  | c. | With wrappers and or glueware? |
|  | d. | As part of the incorporating system? |
|  | e. | What performance measures are to be used? |
|  | f. | What tests can be performed to stress the COTS, MOTS, OSS, or reuse software standalone or within the system? |
|  | g. | What fault-tolerant tests can be performed either standalone or within the system, fault injection? |
|  | 15. | **Will it be used in a safety-critical system?** |
|  | a. | Do the functions performed by the COTS, MOTS, OSS, or reuse software meet the SW safety criticality criteria? |
|  | b. | Has a preliminary hazard analysis identified the COTS, MOTS, OSS, or reuse software functions as safety-critical? |
|  | c. | If so, what hazard contributions could it make? |
|  | i. | Think functionally at first. What happens if the function it is to perform fails? |
|  | ii. | Then work through common/generic faults and failure modes. |
|  | d. | How does it fail?; list, test for all the modes. |
|  | e. | Will wrapper code be developed to protect the system from this COTS, MOTS, OSS, or reuse software? |
|  | f. | What potential problems could the unused portions of the COTS, MOTS, OSS, or reuse software cause? |
|  | 16. | **For an Operating System,** |
|  | a. | Is it a reduced or “safe” OS (e.g., Real-Time Operating System VxWorks, Integrity, the D0-178B ARINC 653 version sold only to the aviation, life-critical software market)? |
|  | b. | How are exceptions handled? |
|  | c. | What compilers are needed, what debuggers? |
|  | e. | What is it running on? Is that an approved, recommended platform? |
|  | f. | Is the processing time, scheduler, switching time adequate? |
|  | g. | Will partitioning be needed, how well does it perform partitioning? |
|  | 17. | **Will it be used in a system that must be highly reliable?** |
|  | a. | Is there reliability information from the vendor? |
|  | b. | How will its reliability be measured within the system it is operating in/contributing to? |
|  | c. | Is there company experience of this COTS, MOTS, OSS, or reuse software to be drawn from? Which version of the COTS, MOTS, OSS, or reuse software? |
|  | d. | What are the error/discrepancy metrics that can be collected? |
|  | i. | From the vendor? |
|  | ii. | From use in developing and testing the COTS, MOTS, OSS, or reuse software both within and outside the system? |
|  | e. | Do the system functional FEMAs include the functions to be performed by the COTS, MOTS, OSS, or reuse software? |
|  | i. | Have known potential faults and failures been adequately analyzed and documented? |
|  | 18. | **What happens when versions of the COTS, MOTS, OSS, or reuse software change?** |
|  | a. | Is there an upgrade plan? |
|  | i. | During development? |
|  | ii. | During operations/maintenance? |
|  | iii. | What does the upgrade plan take into consideration? |
|  | b. | Is there a maintenance plan/agreement? |
|  | c. | Is there a support agreement for addressing any errors found? |
|  | d. | Should the COTS, MOTS, OSS, or reuse software be put in escrow? |
|  | e. | Should there be an agreement to have the software revert to the company after so many years? |
|  | f. | Should the company purchase the rights to the COTS, MOTS, OSS, or reuse software code and documentation? |
|  | 19. | **What is the licensing agreement, and what are the limitations?** |
|  | a. | How many seats are there? |
|  | b. | Is vendor support included? |
|  | c. | Can licenses be transferred? |
|  | d. | Does the licensing agreement meet project needs? |
|  | 20. | **For software development  and debugging tools:** |
|  | a. | Which compilers and libraries have been chosen? |
|  | b. | Are there a reduced instruction set and code standards to be followed? |
|  | c. | Is there more than one debug tool to be used? |
|  | i. | What are their false positive and false negative rates? |
|  | d. | Autocode generators: |
|  | ii. | What are their limitations, their known defects? |
|  | iii. | What are their settings and parameters? (Are they easy to use? Do they meet project needs?) |
|  | iv. | Are results usable, repeatable? |
|  | v. | What are the support agreements? |
|  | vi. | Is there verification and validation support? How will they be verified and validated? |
|  | e. | Modeling tools |
|  | f. | Development environment tools |
|  | 21. | **For infrastructure tools (e.g., databases, configuration management, and release tools, verification tools, etc.):** |
|  | a. | Does it meet the requirements? |
|  | b. | Can it grow and expand if needed, or has it been specified for only current needs? |
|  | c. | Will the tool be verifying, creating (e.g., auto code generator), building, assembling, burning in safety-critical software? |
|  | d. | How would the loss of data stored in the tool or accessed by the tool impact the project? |
|  | i. | Could safety data be lost, say, from the tool that stores hazard reports, problem reporting information? |
|  | e. | Are there sufficient and frequent enough back-ups? How and where are those stored? |
|  | f. | How much training is required to use the tools? |
|  | g. | Are there restrictions on and levels of access? |
|  | ii. | How are access levels managed? |
|  | h. | Are any security features needed, either built-in or via access limitations? |

## 3.11 Additional Guidance

Additional guidance can be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights) * [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice)        * [6.3 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SWEHBVC/pages/96174179/6.3+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) * [6.4 - Checklist for Choosing Off-The Shelf Software (OTS)](/spaces/SWEHBVD/pages/102695563/6.4+-+Checklist+for+Choosing+Off-The+Shelf+Software+OTS) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-024 - Checklist for Choosing Off-The Shelf Software](/spaces/SITE/pages/116293728/PAT-024+-+Checklist+for+Choosing+Off-The+Shelf+Software) * [PAT-025 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SITE/pages/116294244/PAT-025+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) |

## 3.12 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

This requirement applies to all projects regardless of size.

Small projects, by definition, may have finite budgets, limited personnel, shorter timelines, and reduced complexity compared to larger NASA projects. Despite these constraints, small projects must still adhere to NPR 7150.2 requirements, but in a **scaled and tailored approach** that is realistic for the available resources. This guidance provides recommendations for simplifying workflows while ensuring critical requirements for safety, mission success, and software quality are met.

Small projects can successfully meet NPR 7150.2 guidelines by adopting a **risk-based, tailored approach** that prioritizes critical requirements and uses streamlined processes. By focusing resources on safety, mission success, and compliance essentials, while leveraging tools like off-the-shelf software and automation, small projects can deliver innovative, cost-effective results without sacrificing quality or compliance.

## 4.1 Key Principles for Small Projects

### 4.1.1 Prioritize Risk-Based Requirements Compliance

While all requirements must be considered, small projects should focus efforts on **high-priority requirements** that directly impact:

* **Mission success** (e.g., functional correctness, software reliability);
* **Safety** (e.g., requirements for safety-criticality);
* **Cybersecurity** (e.g., protecting sensitive or mission-critical data).

Tailoring lower-priority requirements can reduce the burden on small projects without compromising the overall integrity of the system.

### 4.1.2 Take Advantage of Tailoring Opportunities

Tailoring is a formal process of modifying, scaling down, or omitting specific requirements based on the classification and safety criticality of the software. For small projects:

* **Start with SWE-140:** Examine which requirements apply to your software class using NPR 7150.2, **Appendix C**.
* **Document Tailoring Rationale:** Clearly justify the tailoring decisions in the **Compliance Matrix**, including how risks are mitigated.
* **Technical Authority Approvals:** Obtain approval for all tailoring decisions from the appropriate Engineering Technical Authority (ETA), Safety and Mission Assurance Technical Authority (SMA TA), or other relevant authorities.

### 4.1.3 Streamlined Compliance Matrix for Small Projects

Small projects can simplify the compliance matrix by:

* **Identifying "Critical Entries":** Highlight the most essential requirements directly tied to mission success, safety, and cybersecurity. Focus resources on fulfilling these entries.
* **Grouping Waivers/Deviations:** Consolidate tailoring, waivers, and deviations into the compliance matrix to streamline review and approvals.
* **Reducing Overlap:** Use existing Center-wide compliance resources (e.g., templates, reusable processes) to avoid duplicative work.

### 4.1.4 Software Design and Development Strategy

For small projects, adopt lightweight and efficient processes to meet requirements:

1. **Agile Methods:** Small teams can use agile development practices with frequent incremental deliveries to maintain focus on essential features and requirements.
2. **Risk-Driven Testing:** Tailor testing efforts to prioritize high-risk areas of the software. For example:
   * Classify safety-critical portions for rigorous testing.
   * Reduce testing effort for non-safety-critical features through sampling or targeted tests.
3. **Automation to Save Effort:** Automate repetitive tasks such as testing, code analysis, and build/deployment processes to free up limited resources.

### 4.1.5 Leverage Existing Software (COTS, GOTS, MOTS, OSS, or Reused Software)

Small projects can reduce time and cost by incorporating **non-hand-generated software** wherever appropriate. However, such software must be carefully evaluated, including:

* Ensuring it meets project-specific requirements.
* Verifying legal and licensing rights, especially for Open Source Software (OSS) or Modified Off-The-Shelf (MOTS).
* Applying validation and verification (V&V) practices to confirm its functionality and fitness for intended use.

When possible:

* **Leverage Vendor Support or Built-in Testing Tools:** For COTS software, use vendor-provided test suites or documentation to reduce the burden of developing custom verification processes.
* **Reuse Proven Code:** Prioritize heritage software from previous NASA projects with a record of successful use.

### 4.1.6 Documentation Simplification

Small projects often struggle with resource-intensive documentation requirements. To address this:

* Use **scaled-down templates** provided by NASA Centers or prior small projects.
* Focus on "just enough documentation" — ensure key artifacts like the Software Development Plan (SDP), Software Management Plan (SMP), and Compliance Matrix are complete, but minimize non-essential documentation.
* For iterative or agile practices, align documentation updates with sprint cycles or incremental software deliveries, avoiding extensive upfront documentation.

### 4.1.7 Develop Plans for Long-Term Software Support

Even for small projects, planning for **software maintenance and support** is critical, particularly for key software dependencies like COTS, GOTS, or OSS. Key actions include:

* Ensuring vendor agreements include long-term support or source code escrow (where applicable).
* Identifying risks of software obsolescence and documenting mitigation steps.
* Periodically assessing defects reported by the software vendor, OSS community, or developers, ensuring they do not affect system quality.

For truly short-term projects, plan for **transition or decommissioning** to ensure external dependencies do not leave residual risks for NASA’s infrastructure.

## **4.2 Process Guidance for Small Projects**

The following framework outlines practical steps for small teams to meet NPR 7150.2 compliance while managing constraints.

### Step 1: Software Classification

Classify the software according to **SWE-020** to determine safety-criticality and overall impact:

* Low-risk non-mission-critical software (e.g., Class D, E, or F) will often allow for significant tailoring.
* High-risk mission-critical systems (e.g., Class A or B) will require minimal tailoring due to stricter requirements.

### Step 2: Develop a Compliance Matrix

Populate the compliance matrix referencing:

* Applicable NPR 7150.2 requirements (Appendix C).
* Tailored requirements (including approved waivers and deviations).
* Supporting documents and evidence for each completed requirement.

### Step 3: Focus Testing and V&V Efforts

Balance testing effort based on criticality:

* Perform **functional verification** for all active features and system requirements.
* For off-the-shelf or reused software components, test only the portions being used in the system, rather than testing unrelated features.
* Focus cybersecurity testing on areas where data sensitivity or system access requires it, simplifying efforts for low-risk environments.

### Step 4: Risk-Mitigation Planning

Even small projects must plan for risks. Address:

1. **Safety Hazards**: Mitigate risks of unintended safety-critical system failures.
2. **Software Vulnerabilities**: Assess OSS and legacy system code for known vulnerabilities.
3. **Undefined Support**: Identify alternatives in case third-party software becomes unavailable.

### Step 5: Leverage Center Resources

Take advantage of tools, templates, and expertise:

1. **Compliance Templates**: Use pre-built matrices or documents to save time.
2. **Engineering Expertise**: Leverage shared Center resources like real-time operating system (RTOS) guidelines or safety review tools.
3. **Open Collaboration Platforms**: Utilize internal NASA communities to share small-project best practices.

### Step 6: Use Iterative Development and Documentation Techniques

If aligned with project needs, lightweight methodologies like Agile allow small projects to:

* Deliver functional software early.
* Break down requirements into manageable parts for shorter, focused development cycles.
* Incorporate iterative review and testing without needing fully completed documentation upfront.

## 4.3 Key Focus Areas for Small Projects

To summarize, small projects should:

1. **Tailor Wisely**: Reduce requirements where justified but fully document and approve tailoring.
2. **Focus Resources on Mission-Critical Functions**: Always prioritize functionality that impacts safety, performance, or mission success.
3. **Complete Core Documentation**: Avoid over-documenting but maintain compliance with expectations for the SDP, SMP, and Compliance Matrix.
4. **Plan for Long-Term Sustainability**: Even small projects need to consider system maintainability and end-of-life planning.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-040)

  [NASA Study on Flight Software Complexity (Final Report),](http://www.nasa.gov/offices/oce/documents/FSWC_study.html "Click to open in new window")

  Commissioned by the NASA Office of Chief Engineer, Technical Excellence Program, Adam West, Program Manager, and edited by Daniel L. Dvorak, Systems and Software Division, Jet Propulsion Laboratory, 2009.
* (SWEREF-121)

  [AIAA Guide for Managing the Use of Commercial off the Shelf (COTS) Software Components for Mission-Critical Systems(G-118-2006e).](https://netforum.aiaa.org/eweb/DynamicPage.aspx?Action=Add&ObjectKeyFrom=1A83491A-9853-4C87-86A4-F7D95601C2E2&WebCode=ProdDetailAdd&DoNotSave=yes&ParentObject=CentralizedOrderEntry&ParentDataObject=Invoice%20Detail&ivd_formkey=69202792-63d7-4ba2-bf4e-a0da41270555&ivd_cst_key=00000000-0000-0000-0000-000000000000&ivd_prc_prd_key=4FBFBBC1-5790-436A-B966-4C6CB206B320 "Click to open in new window")
* (SWEREF-125)

  [Open-source vs. proprietary software bugs: Which get squashed fastest?"](https://www.cnet.com/news/open-source-vs-proprietary-software-bugs-which-get-squashed-fastest/ "Click to open in new window")

  Asay, Matt. CNET, September 27, 2007
* (SWEREF-129)

  [COTS Foundations: Essential Background and Terminology.](http://www.ippa.org/IPPC2/PROCEEDINGS/Article_5_Baron.pdf "Click to open in new window")

  Baron, Sally J. F. (September, 2006). International Public Procurement Conference Proceedings.
* (SWEREF-130)

  [Change-out: A system of systems approach to COTS management.](http://ieeexplore.ieee.org/document/4127316/ "Click to open in new window")

  Baron, Sally J. F., Ph.D. Management Consulting. IEEE Xplore, Sixth International IEEE Conference on Commercial-off-the-Shelf (COTS)-Based Software Systems (ICCBSS'07), 0-7695-2785-X/07.
* (SWEREF-143)

  [Decision Point: Will Using a COTS Component Help or Hinder Your DO-178B Certification Effort?](http://www.crosstalkonline.org/storage/issue-archives/2003/200311/200311-0-Issue.pdf "Click to open in new window")

  Budden, Timothy J. AVISTA. CrossTalk - Journal of Defense Software Engineering, November 2003. See page 18.
* (SWEREF-148)

  [The Commandments of COTS: Still in Search of the Promised Land.](http://siteresources.worldbank.org/PSGLP/Resources/TheCommandmentsofCOTS.pdf "Click to open in new window")

  Carney, D.J., Oberndorf, P.A. (May, 1997). Carnegie Mellon Software Engineering Institute, Carnegie Mellon University.
* (SWEREF-154)

  [Added Sources of Costs in Maintaining COTS-Intensive Systems,](http://www.crosstalkonline.org/storage/issue-archives/2007/200706/200706-Clark.pdf "Click to open in new window")

  Clark, Drs. Brad and Betsy. Software Metrics, Inc. (June, 2007). CrossTalk - Journal of Defense Software Engineering.
* (SWEREF-167)

  [COTS Software Integration Cost Modeling Study.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.143.1227&rep=rep1&type=pdf "Click to open in new window")

  June 1997.University of Southern California, Center for Software Engineering.
* (SWEREF-185)

  [Working Effectively with Legacy Code,](http://ptgmedia.pearsoncmg.com/images/9780131177055/samplepages/0131177052.pdf "Click to open in new window")

  Feathers, Michael C. (2004). Prentice Hall.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-242)

  [COTS: Commercial Off-The-Shelf or Custom Off-The-Shelf?](http://www.crosstalkonline.org/storage/issue-archives/2007/200706/200706-Livingston.pdf "Click to open in new window")

  Livingston, Jr. P.E., Wiley F. (June, 2007). Software Technology Support Center (STSC), Hill AFB.
* (SWEREF-249)

  [Sick of COTs Acronyms?](http://www.pennwellblogs.com/mae/2008/01/sick-of-cots-acronyms-yet.html "Click to open in new window")

  McHale, John, Exec. Ed. (January, 2008). Military & Aerospace Electronics magazine.  Title no longer available.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-369)

  [Automatic Code Generation for Instrument Flight Software,](https://trs.jpl.nasa.gov/bitstream/handle/2014/41374/07-4374.pdf?sequence=1&isAllowed=y "Click to open in new window")

  Wagstaff, K., Benowitz, E. Byrne, D.J., Peters, K., Watney, G. (2008), NASA Jet Propulsion Lab (JPL). https://trs.jpl.nasa.gov/handle/2014/41374
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022  See page 9.
* (SWEREF-424)

  [Lessons Learned Study Final Report: For the Exploration Systems Mission Directorate,](https://llis.nasa.gov/lesson/1838 "Click to open in new window")

  NASA Langley Research Center (LaRC), August 20, 2004. Lessons Learned Reference. (See pages 45-56)
* (SWEREF-425)

  ["International Space Station Lessons Learned As Applied to Exploration,"](http://nen.nasa.gov/llis_lib/pdf/1022932main_ISSLessonsLearnedJuly2009.pdf "Click to open in new window")

  International Space Station, Multilateral Coordination Board, NASA Kennedy Space Center (KSC), July 22, 2009. Lessons Learned Reference.
* (SWEREF-426)

  ["Commercial Item Acquisition: Considerations and Lessons Learned,"](http://www.acq.osd.mil/dpap/Docs/cotsreport.pdf "Click to open in new window")

  Office of the Secretary of Defense, June 26, 2000. Lessons Learned Reference.
* (SWEREF-462)

  [Ohloh/Black Duck Open HUB.](http://www.ohloh.net/ "Click to open in new window")

  © 2014 Black Duck Software, Inc.
* (SWEREF-550)

  [ADEOS-II NASA Ground Network (NGN) Development and Early Operations -- Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned](https://llis.nasa.gov/lesson/1346 "Click to open in new window")

  Public Lessons Learned Entry: 1346.
* (SWEREF-551)

  [Lessons Learned From Flights of ?Off the Shelf? Aviation Navigation Units on the Space Shuttle, GPS](https://llis.nasa.gov/lesson/1370 "Click to open in new window")

  Public Lessons Learned Entry: 1370.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
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

## 5.3 Process Asset Templates

**SWE-027 Process Asset Templates**

Click on a link to download a usable copy of the template.

* (PAT-024 - )

  [PAT-024 - Checklist for Choosing Off-The Shelf Software](https://swehb.nasa.gov/download/attachments/116293728/Checklist%20for%20Choosing%20Off-The-Shelf%20%28OTS%29%20Software.docx?api=v2 "Click to open in new window")

  Topic 6.4, Also in SWE-027 and categories: Commercial and Legacy Software, and Coding Practices.
* (PAT-025 - )

  [PAT-025 - Checklist for Choosing a Real Time Operating System (RTOS)](https://swehb.nasa.gov/download/attachments/116294244/Checklist%20for%20Choosing%20a%20Real%20Time%20Operating%20System%20%28RTOS%29%202022%200617.docx?api=v2 "Click to open in new window")

  SWE-027, tab 3.1, Also in Topic 6.3.
* (PAT-036 - )

  [PAT-036 Software Architecture and Design Process Audit](https://swehb.nasa.gov/download/attachments/198770701/PAT-036%20-%20Architecture%20and%20Design%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Architecture and Design.
* (PAT-038 - )

  [PAT-038 - Implementation Process Audit](https://swehb.nasa.gov/download/attachments/198770739/PAT-038%20-%20Implementation%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Implementation Process.
* (PAT-040 - )

  [PAT-040 - Project Management Process Audit](https://swehb.nasa.gov/download/attachments/198770755/PAT-040%20-%20Project%20Management%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Project Management Process.
* (PAT-041 - )

  [PAT-041 - Project Planning Process Audit](https://swehb.nasa.gov/download/attachments/198770757/PAT-041%20-%20Project%20Planning%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Project Planning Process.
* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management.
* (PAT-046 - )

  [PAT-046 - Test Verification and Validation Process Audit](https://swehb.nasa.gov/download/attachments/198770767/PAT-046%20-%20Test%20Verification%20and%20Validation%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Test Verification and Validation Process.
* (PAT-056 - )

  [PAT-056 - Software Development Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770884/PAT-056%20-%20Software%20Development%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Development - Management Plan. Based on the minimum recommended content for a Software Development - Management Plan.
* (PAT-059 - )

  [PAT-059 - Software Requirements Specification Assessment](https://swehb.nasa.gov/download/attachments/198770890/PAT-059%20-%20Software%20Requirements%20Specification%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Requirements Specification. Based on the minimum recommended content for a Software Requirements Specification.

**Coding Practices Process Asset Templates**

Click on a link to download a usable copy of the template. (CodePrac)      6/27/2025 - 4 items

**Coding Practices Process Asset Templates**

* (PAT-017 - )

  [PAT-017 - C Code Inspection Checklist](https://swehb.nasa.gov/download/attachments/114328366/C%20Code%20Inspection%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.6, Also found in Peer Review category.
* (PAT-022 - )

  [PAT-022 - Programming Practices Checklist,](https://swehb.nasa.gov/download/attachments/115933208/Programming%20Practices%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.56 - Source Code Quality Analysis, tab 2.2,
* (PAT-024 - )

  [PAT-024 - Checklist for Choosing Off-The Shelf Software](https://swehb.nasa.gov/download/attachments/116293728/Checklist%20for%20Choosing%20Off-The-Shelf%20%28OTS%29%20Software.docx?api=v2 "Click to open in new window")

  Topic 6.4, Also in SWE-027 and categories: Commercial and Legacy Software, and Coding Practices.
* (PAT-025 - )

  [PAT-025 - Checklist for Choosing a Real Time Operating System (RTOS)](https://swehb.nasa.gov/download/attachments/116294244/Checklist%20for%20Choosing%20a%20Real%20Time%20Operating%20System%20%28RTOS%29%202022%200617.docx?api=v2 "Click to open in new window")

  SWE-027, tab 3.1, Also in Topic 6.3.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains the following lessons learned related to the user of commercial, government, and legacy software:

* **Misalignment with Commercial Vendor Software Capabilities**

**Incident:**  
Misaligned expectations for vendor simulation, interface details, and heritage design significantly delayed testing and integration activities. COVID‑related limitations reduced the required face‑to‑face interaction needed to align on software behaviors.

**Lesson Learned:**

* + **Deep Early Integration:** NASA personnel must work side‑by‑side with commercial partners early to align on simulation capabilities, interface assumptions, and development processes.
  + **Contractual Clarity:** Software deliverables and testbed capabilities must be unambiguously specified in contracts.

**Implication:**  
Weak alignment with vendor software ecosystems causes delays, rework, and verification gaps that can push missions off launch schedules.

* ### **Class D Encourages COTS Usage, but COTS Requires More Software Assurance—Not Less**

  **Problem/Observation:**  
  Class D missions often rely on Commercial Off‑the‑Shelf (COTS) hardware and software to reduce cost and schedule. However, the LTB mission demonstrated that increased COTS dependence can actually elevate software risk if not paired with sufficient Software Assurance (SA) rigor. The Anomaly Review Board (ARB) identified multiple gaps stemming from limited understanding and verification of COTS behaviors.

  **Contributing Factors:**  
  • Limited or incomplete vendor documentation restricted insight into internal behaviors and interfaces.  
  • Incorrect assumptions were made about EPS behavioral characteristics under fault or reset conditions.  
  • The radio experienced misconfiguration after resets, preventing commands from being received.  
  • I²C interface issues were inherited from Janus without adequate re‑characterization or validation.

  **Resulting Impacts:**  
  These COTS‑related issues introduced unanticipated system behavior, reduced controllability, and increased operational risk. Several anomalies could not be fully analyzed or resolved due to limited observability into COTS internals.

  **Relevant SWEHB Guidance:**  
  The SWEHB maintains specific expectations for COTS and GOTS integration:  
  • SWE‑027 sets requirements for evaluation, characterization, verification, and integration of COTS/GOTS components.  
  • COTS introduces unique risks due to opaque or proprietary behaviors; tailoring cannot reduce required system‑level verification, insight, and test rigor.

  **Lesson Learned:**  
  COTS may reduce development effort, but it does **not** reduce the need for verification, characterization, and assurance. In fact, opaque or insufficiently documented behaviors require **more** testing, not less. Mission class does not change this principle: any “cheap box” must still be systematically evaluated, verified, and integrated to ensure it performs reliably in the mission environment.
* **MER Spirit Flash Memory Anomaly (2004).  Lesson Number 1483[557](#_tabs-<p></p>):**  "Shortly after the commencement of science activities on Mars, the Mars Exploration Rover (MER) lost the ability to execute any task that requested memory from the flight computer. The cause was incorrect configuration parameters in two operating system software modules that control files' storage in system memory and flash memory. Seven recommendations cover enforcing design guidelines for COTS software, verifying assumptions about software behavior, maintaining a list of lower priority action items, testing flight software internal functions, creating a comprehensive suite of tests and automated analysis tools, providing downlinked data on system resources, and avoiding the problematic file system and complex directory structure."

**Recommendations:**

* + "Enforce the project-specific design guidelines for COTS software, as well as for NASA-developed software. Assure that the flight software development team reviews the basic logic and functions of commercial off-the-shelf (COTS) software, including the vendor's briefings and participation.
  + "Verify assumptions regarding the expected behavior of software modules. Do not use a module without detailed peer review and ensure that all design and test issues are addressed.
  + "Where the software development schedule forestalls completion of lower priority action items, maintain a list of incomplete items that require resolution before final configuration of the flight software.
  + "Place a high priority on completing tests to verify the execution of flight software internal functions.
  + "Early in the software development process, create a comprehensive suite of tests and automated analysis tools.
  + "Ensure that reporting flight computer-related resource usage is included.
  + "Ensure that the flight software downlinks data on system resources (such as the free system memory) so that the actual and expected behavior of the system can be compared.
  + "For future missions, implement a more robust version of the dosFsLib module, and/or use a different type of file system and a less complex directory structure.".

* **Lessons Learned From Flights of Off the Shelf Aviation Navigation Units on the Space Shuttle, GPS. Lesson Number 1370**[551](#_tabs-<p></p>): "The Shuttle Program selected off-the-shelf GPS and EGI units that met the requirements of the original customers. It was assumed that off-the-shelf units with proven design and performance would reduce acquisition costs and require minimal adaptation and minimal testing. However, the time, budget, and resources needed to test and resolve firmware issues exceeded initial projections."

* **ADEOS-II NASA Ground Network (NGN) Development and Early Operations – Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned. Lesson Number 1346**[550](#_tabs-<p></p>): "The purpose of the Standard Autonomous File Server (SAFS) is to provide automated management of large data files without interfering with the assets involved in the acquisition of the data. It operates as a stand-alone solution, monitoring itself and providing an automated fail-over processing level to enhance reliability. The successful integration of COTS products into the SAFS system has been key to its becoming accepted as a NASA standard resource for file distribution, and leading to its nomination for NASA's Software of the Year Award in 1999."  
    
  **Lessons Learned:**  
  "Match COTS tools to project requirements. Deciding to use a COTS product as the basis of system software design is potentially risky. The potential benefits include quicker delivery, less cost, and more reliability in the final product. The following lessons were learned in the definition phase of the SAFS/CSAFS development.  
  + "Use COTS products and re-use previously developed internal products.
  + "Create a prioritized list of desired COTS features.
  + "Talk with local experts having experience in similar areas.
  + "Conduct frequent peer and design reviews.
  + "Obtain demonstration [evaluation] versions of COTS products.
  + "Obtain customer references from vendors.
  + "Select a product appropriately sized for your application.
  + "Choose a product closely aligned with your project's requirements.
  + "Select a vendor whose size will permit a working relationship.
  + "Use vendor tutorials, documentation, and vendor contacts during the COTS evaluation period."  
      
    "Test and prototype COTS products in the lab. The COTS evaluation prototyping and test phase allow problems to be identified as the system design matures. These problems can be mitigated (often with the help and cooperation of the COTS vendor) well before the field-testing phase, at which time it may be too costly or impossible to retrofit a solution. The following lessons were learned in the prototyping and test phase of the SAFS/CSAFS development:
  + "Prototype your system's hardware and software in a lab setting as similar to the field environment as possible.  
    - "Simulate how the product will work on various customer platforms.
    - "Model the field operations.
    - "Develop in stages with ongoing integration and testing."
  + "Pass pertinent information on to your customers.
  + "Accommodate your customers, where possible, by building in alternative options.
  + "Don't approve all requests for additional options by customers or new projects that come online.
  + "Select the best COTS components for product performance, even if they are from multiple vendors.
  + "Consider the expansion capability of any COTS product.
  + "Determine if the vendor's support is adequate for your requirements.  
      
    "Install, operate, and maintain the COTS field and lab components. The following lessons were learned in the installation and operation phase of the SAFS/CSAFS development:
  + "Personally perform on-site installations whenever possible.
  + "Have support/maintenance contracts for hardware and software through development, deployment, and first year of operation.
  + "Create visual representations of system interactions where possible.
  + "Obtain feedback from end-users.
  + "Maintain the prototype system after deployment.
  + "Select COTS products with the ability to do internal logging."

* **Lesson Learned (Starliner CFT):** **COTS reduces development effort but increases assurance obligations; opaque behaviors demand more testing, not less.**

  **Project Context:**  
  Derived from Starliner CFT Investigation.

  **Problem/Observation:**  
  Limited vendor documentation and opaque subsystem behaviors hindered observability, characterization, and anomaly resolution for COTS avionics/propulsion interfaces.

  **Contributing Factors:**

  + Insufficient insight into vendor design decisions and internal states.
  + Inadequate mission‑representative testing of reset behaviors, interface edge cases, and configuration persistence.

  **Impacts:**

  + Misconfiguration and behavior drift after resets; reduced command capability.
  + Unverified assumptions about electrical power system (EPS) behavior and interface timing.

  **Recommended Practices (Aligned to SWE‑027):**

  + Plan **deep characterization tests** (reset, boot sequences, timing/latency, configuration persistence, error modes).
  + Negotiate contract terms for **engineering insight** (logs, telemetry, design notes, failure reports).
  + Maintain a **COTS hazard log** mapping opaque behaviors to system mitigations and verification evidence.

  **Actionable Checks:**

  + COTS characterization test matrices cover reset, timing, interface robustness.
  + Supplier data access clauses are present and exercised.
  + Hazard log entries include explicit verification/validation artifacts.
* **Lessons Learned Study Final Report for the Exploration Systems Mission Directorate, Langley Research Center; August 20, 2004. Lessons Learned Number 1838**[424](#_tabs-<p></p>): "There has been an increasing interest in utilizing commercially available hardware and software as portions of space flight systems and their supporting infrastructure. Experience has shown that this is a very satisfactory approach for some items and a major mistake for others. In general, COTS [products] should not be used as part of any critical systems [but see the recommendation later in this Lesson Learned] because of the generally lower level of engineering and product assurance used in their manufacture and test. In those situations where COTS [software] has been applied to flight systems, such as the laptop computers utilized as control interfaces on [International Space Station] (ISS), the cost of modifying and testing the hardware/software to meet flight requirements has far exceeded expectations, potentially defeating the reason for selecting COTS products in the first place. In other cases, such as the [Checkout Launch Control System] (CLCS) project at JSC, the cost of maintaining the commercial software had not been adequately analyzed and drove the project's recurring costs outside the acceptable range.

**Recommendation:** Ensure that candidate COTS products are thoroughly analyzed for technical deficiencies and life cycle cost implications before levying them on the program.

* + - COTS systems can reduce system costs, but only if all of their characteristics are considered beforehand and included in the planned application. (Standards)
    - COTS systems that look good on paper may not scale well to NASA's needs for legitimate reasons. These include sustaining engineering/update cycle/recertification costs, scaling effects, dependence on third party services and products. We need to ensure that a life cycle cost has been considered correctly. (Headquarters - CLCS)

**LLSW01 — Heritage Software Reuse and Testing *(full content above)***

* **Context/Background: Legacy flight software reuse assumed minimal testing; defects emerged late.**
* **Lesson Learned: Treat heritage software as if new—perform full requirements validation, interface verification, regression testing, environmental qualification.**
* **Evidence/Observation: PPE planned legacy reuse; issues remained open at pause; assumptions delayed defect discovery.**
* **Cause(s): Belief prior flight obviates testing; lack of reuse standards.**
* **Recommendation/Corrective Action: Establish project level reuse standards specifying test scope, verification criteria, acceptance gates.**
* **Implementation Guidance: Embed reuse criteria in plans (SWE013), trace reused functionality to req/design/tests (SWE052/059/064/072), determine safety impacts (SWE133/134).**
* **Success Criteria/Verification: Reuse plan; executed test campaigns; bidirectional traceability; IV&V closure; defect rates comparable to new development.**
* **Applicability/Scope: All mission/safety critical software; heritage and third party components.**
* **Related: SWE027, SWE013, SWE050, SWE052/059/064/072, SWE133/134.**

**LLSW02 — Heritage Knowledge vs. Heritage Code**

* **Context/Background: Teams treated legacy code as “plug‑and‑play,” underestimating adaptation effort and verification for new architectures.**
* **Lesson Learned: Leverage heritage experience, not code blindly; plan/budget as new development; invite IV&V early to requirements TIMs and merges to surface gaps sooner.**
* **Evidence/Observation: Late requirement updates and delivery slips affected dependent systems; earlier IV&V would have found gaps.**
* **Cause(s): Underscoped changes; late IV&V engagement.**
* **Recommendation/Corrective Action: Require early IV&V engagement (SWE141/131), define reuse criteria (LLSW01), enforce full traceability (SWE050/052/072).**
* **Implementation Guidance: Add IV&V coordination to contracts/schedules; include IV&V in requirements reviews; maintain authoritative baselines.**
* **Success Criteria/Verification: Fewer late requirement changes; on‑schedule deliveries; reduced rework/nonconformances.**
* **Applicability/Scope: Any reuse effort across new mission contexts.**
* **Related: SWE141, SWE131, SWE050, SWE052.**

**LLSW11 — COTS/Reuse Policy for Safety‑Critical Systems *(full content above)*   Context/Background: Teams struggled to apply NPRs to COTS/reuse; safety controls missing in COTS; insight difficult.**

* **Lesson Learned: Create program‑specific COTS/reuse policy clarifying applicability of NPR****2/standards to CBCS, including safety control expectations.**
* **Evidence/Observation: Reliability/availability/upgrade issues with COTS critical items; provider resistance to design insights.**
* **Cause(s): Undefined requirements/expectations; lack of upfront safety control provisions.**
* **Recommendation/Corrective Action: Update Agency NPRs/standards (or tailor) for COTS in human‑rated contexts; perform early feasibility against safety controls.**
* **Implementation Guidance: SWE027, SWE133/134, SWE158.**
* **Success Criteria/Verification: Documented COTS policies; hazard controls traceable to requirements; successful verification closeouts.**
* **Applicability/Scope: Safety‑critical CBCS, avionics, integrated systems.**
* **Related: SWE027, SWE133, SWE134, SWE158.**

## 6.2 Other Lessons Learned

* **The following information comes from the NASA Study on Flight Software Complexity listed in the reference section of this document[040](#_tabs-<p></p>):**

"In 2007, a relatively new organization in DoD (the Software Engineering and System Assurance Deputy Directorate) reported their findings on software issues based on approximately 40 program reviews in the preceding 2½ years (Baldwin 2007). They found several software systemic issues that were significant contributors to poor program execution." Among the seven listed were the following on Commercial Off The Shelf (COTS):

* + - "Immature architectures, COTS integration, interoperability."

"Later, in partnership with the NDIA, they identified the seven top software issues that follow, drawn from a perspective of acquisition and oversight." Among the seven listed were the following on COTS:

* + - "Inadequate attention is given to total life cycle issues for COTS/NDI impacts on life cycle cost and risk."

"In partnership with the NDIA, they made seven corresponding top software recommendations." Among the seven listed were the following on COTS:

* + - "Improve and expand guidelines for addressing total life cycle COTS/NDI issues."
* **The following information is from Commercial Item Acquisition: Considerations and Lessons Learned July 14, 2000, Office of the Secretary of Defense[426](#_tabs-<p></p>):**

This document is designed to assist DoD acquisition and supported commercial items. According to the introductory cover letter, "it provides an overview of the considerations inherent in such acquisitions and summarizes lessons learned from a wide variety of programs." Although it's written with the DoD acquirer in mind, it can provide useful information and assist you as we move down this increasingly significant path.

* **International Space Station Lessons Learned as Applied to Exploration, KSC, July 22, 2009[425](#_tabs-<p></p>):**(23-Lesson): Use Commercial Off-the-Shelf Products Where Possible.
  + An effective strategy in the ISS program was to simplify designs by utilizing commercial off-the-shelf (COTS) hardware and software products for non-safety, non-critical applications.
  + Application to Exploration: The use of COTS products should be encouraged whenever practical in exploration programs.
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

  + [Ensure heritage software meets all requirements before reuse](https://software.gsfc.nasa.gov/lesson-details/57/). **Lesson Number 57**: The recommendation states: "Ensure heritage software meets all requirements before reuse, or evaluate the impact on areas where the heritage and reused requirements differ."
  + [When inheriting FSW from a previous mission, evaluate the differences between the missions' requirements and/or design](https://software.gsfc.nasa.gov/lesson-details/71/). **Lesson Number 71**: The recommendation states: "When inheriting FSW from a previous mission, evaluate the differences between the missions' requirements and/or design."
  + [Evaluate new software along the full range of operational scenarios](https://software.gsfc.nasa.gov/lesson-details/91/). **Lesson Number 91**: The recommendation states: "Evaluate new software along the full range of operational scenarios."
  + [Use Common Ground Systems over mission life-cycles](https://software.gsfc.nasa.gov/lesson-details/103/). **Lesson Number 103**: The recommendation states: "Use Common Ground Systems over mission life-cycles as much as possible."
  + [Consider innovative and "outside-the-box" approaches to risks and challenges](https://software.gsfc.nasa.gov/lesson-details/153/). **Lesson Number 153**: The recommendation states: "Consider innovative and "outside-the-box" approaches to risks and challenges."
  + [AWS services availability](https://software.gsfc.nasa.gov/lesson-details/176/). **Lesson Number 176**: The recommendation states: "Ensure that AWS services of interest are available in the AWS region you selected."
  + [Software Requirement Sell-Off Expedience](https://software.gsfc.nasa.gov/lesson-details/177/). **Lesson Number 177**: The recommendation states: "As early as feasible in the program (EPR-CDR time frame) ensure that the project will be provided with all relevant test articles well in advance of the test’s run-for-record (will likely require NASA Program Management buy-in as well). This will allow the time necessary for: review of requirement test coverage, accumulation of all comments (especially if IV&V are supporting the program), and vendor disposition of all comments to project satisfaction. In this manner, when test artifacts from the FQT run-for-record are provided for requirement sell-off, the Flight Software SME will have a high level of confidence in the artifacts provided (knowing how each requirement has been tested) to expedite the sign-off process. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
  + [Near Space Network (NSN) Cloud transition challenges](https://software.gsfc.nasa.gov/lesson-details/300/). **Lesson Number 300**: The recommendation states: "When considering a transition to Cloud platform/services, keep these in mind: A delivered cloud service capability may not be as robust as needed for operations. Don't take on a Cloud instance if you don't have to; use the Cloud as a giant Network-attached storage and just pay data egress. Hire a Cloud expert even before inheriting the Cloud Concepts. Write requirements for the Cloud up front; everything should have a requirement, no matter if it needs to be built or already works; never let your management agree to accepting an operational component of the ground segment without having agreed upon requirements. A proper communication between the Project leadership and the Ground Segment Manager and PDLs is crucial. Near Space Network (NSN) services have “hidden” fees, so make sure you have a good understanding of all cost implications upfront."
  + [Include File Manager, Memory Manager, and EEPROM write-enable routines early](https://software.gsfc.nasa.gov/lesson-details/303/). **Lesson Number 303**: The recommendation states: "When including reused software in the system consider adding File Manager, Memory Manager, and EEPROM write enable routines early, even in the first build, to allow the features to be used by the development and test teams.  These features can be beneficial by allowing tests to be simpler and testing to be more complete/final.  They can also be used in diagnostics, as well as in cleanup activities."
  + [When using commercial BSP for VxWorks don't forget to include yearly maintenance fees](https://software.gsfc.nasa.gov/lesson-details/304/). **Lesson Number 304**: The recommendation states: "When costing a mission that has software licenses, these fees must be accounted for the duration of the mission, including post launch (through Phase E)."

# 7. Software Assurance

**SWE-027 - Use of Commercial, Government, and Legacy Software**

3.1.14 The project manager shall satisfy the following conditions when a COTS, GOTS, MOTS, OSS, or reused software component is acquired or used:

a. The requirements to be met by the software component are identified.

b. The software component includes documentation to fulfill its intended purpose (e.g., usage instructions).

c. Proprietary rights, usage rights, ownership, warranty, licensing rights, transfer rights, and conditions of use (e.g., required copyright, author, and applicable license notices within the software code, or a requirement to redistribute the licensed software only under the same license (e.g., GNU GPL, ver. 3, license)) have been addressed and coordinated with Center Intellectual Property Counsel.

d. Future support for the software product is planned and adequate for project needs.

e. The software component is verified and validated to the same level required to accept a similar developed software component for its intended use.

f. The project has a plan to perform periodic assessments of vendor reported defects to ensure the defects do not impact the selected software components.

This requirement ensures all *Commercial Off-The-Shelf (COTS)*, *Government Off-The-Shelf (GOTS)*, *Modified Off-The-Shelf (MOTS)*, *Open Source Software (OSS)*, and reused software components meet a defined set of criteria before integration into the project. This includes addressing requirements identification, documentation, usage rights, future support, verification and validation (V&V), and defect tracking.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the conditions listed in "a" through "f" are complete for any COTS, GOTS, MOTS, OSS, or reused software that is acquired or used.

## 7.2 Software Assurance Products

### 7.2.1 COTS/GOTS/MOTS/OSS/Reused Software Requirements Assessment Report

**Purpose**: Identifies and validates the software requirements specific to COTS, GOTS, MOTS, OSS, or reused software, ensuring they can meet project needs.  
**Contents**:

* List of project requirements specifically related to the selected software component (e.g., features, functions, capabilities).
* Traceability from project-level requirements to the capabilities provided by the software component.
* Risk analysis for any gaps in requirements or limitations discovered (e.g., missing features or undocumented behaviors).
* Reference to test plans for verifying defined capabilities.

### 7.2.2 Software Documentation Review Checklist

**Purpose**: Verifies that the selected COTS, GOTS, MOTS, OSS, or reused software components include adequate documentation to fulfill their intended purpose.  
**Contents**:

* Checklist of required documentation types, including:
  + User and operational instructions.
  + Licensing and usage agreements.
  + API references, interface control documents (ICD), and developer guides.
  + Maintenance and future support documents (if available).
* Results of the checklist review, identifying gaps or inconsistencies in the provided documentation.

### 7.2.3 Rights and Licensing Compliance Report

**Purpose**: Documents verification of proprietary rights, licensing rights, warranties, and other related legal or ownership agreements for the software.  
**Contents**:

* Licensing agreement details:
  + Terms and conditions (e.g., GNU GPL restrictions, redistribution requirements).
  + Ownership and intellectual property rights.
  + Transfer rights (if applicable).
* Documentation of coordination with the **Center Intellectual Property Counsel**.
* Identified risks or unresolved issues with licensing compliance.

### 7.2.4 Software Support Plan Assessment Report

**Purpose**: Verifies that future support for the software product is adequate for long-term project needs and identifies gaps in preparedness.  
**Contents**:

* Summary of support plans provided by the vendor or open-source community.
* Assessment of version update frequency and compatibility.
* Risk analysis for unsupported components.
* Mitigation plans for dependencies on outdated software.

### 7.2.5 Software Verification and Validation (V&V) Test Report

**Purpose**: Confirms that the software component has been verified and validated to the same rigor required for a similar in-house or newly-developed software component.  
**Contents**:

* Description of the V&V process, including test procedures and test cases.
* Results of functional, integration, and performance testing.
* Risk analysis for unverified functionality or deficiencies in vendor-provided verification data.

### 7.2.6 Vendor Reported Defects Assessment Plan and Log

**Purpose**: Tracks and assesses the periodic evaluation of vendor-reported defects in the selected software component.  
**Contents**:

* A log of vendor-reported defects, categorized by severity and relevance to the project.
* Plan for periodic reviews of defect reports throughout the software lifecycle.
* Risk analysis for unresolved or critical defects and their potential impact on mission requirements.

## 7.3 Metrics

Metrics help monitor compliance and identify trends related to the acquisition and usage of third-party software components.

### Key Metrics

1. **# of Requirements for COTS, GOTS, MOTS, OSS, or Reused Software Components:**

   * Tracks project-specific requirements linked to third-party software.
   * Indicator of how well requirements traceability is established.
2. **# of Third-Party Software Components Verified and Validated:**

   * Tracks progress on V&V completion for each software component.
   * Ensures all components are scrutinized to the same level as in-house development.
3. **# of Vendor Defects Reported vs. Assessed Defects Over Time:**

   * Tracks new and recurring defects reported by vendors and their assessments.
   * Helps identify trends in the software’s reliability and potential risks.
4. **# of COTS, GOTS, MOTS, OSS Components with Adequate Support Plans:**

   * Monitors whether components have clear future support plans (e.g., patches, updates).
   * Assesses preparedness for addressing obsolete or unsupported software.
5. **% of Components with Licensing Issues Resolved:**

   * Tracks resolution of intellectual property, licensing, or usage rights issues for the software.
   * Helps ensure compliance with legal or licensing obligations.

## 7.4 Guidance

### 7.4.1 Software Assurance Actions for Compliance:

1. **Assess Requirements Identification:**

   * Confirm that all relevant requirements for the software component’s functionality, features, safety, and performance are explicitly documented in the **Software Requirements Specification (SRS)** or other project documentation.
   * Verify that missing or poorly defined requirements are identified as risks.
2. **Review Software Documentation:**

   * Assess if vendor-provided documentation (e.g., user guides, API references, and operational procedures) is sufficient.
   * Identify gaps in documentation that could hinder integration or use.
3. **Address Licensing and Proprietary Rights:**

   * Verify that licensing rights, usage agreements, ownership, and other legal aspects are documented and approved.
   * Ensure Intellectual Property Counsel is engaged to address any potential issues.
4. **Verify Future Support Plans:**

   * Confirm the availability of vendor or community support.
   * Ensure that plans account for version updates, maintenance patches, and defect reporting mechanisms.
5. **Perform Verification and Validation to Required Levels:**

   * Assess whether the software component is verified and validated through testing to the same level as newly developed software.
   * Include functional tests, integration tests, and other assurance activities.
6. **Plan for Vendor Defect Management:**

   * Ensure the project has implementation plans for periodic assessments of vendor-reported defects.
   * Track defects and document risks tied to known issues.
7. **Address Safety Considerations for Safety-Critical Components:**

   * If the software component is identified as **safety-critical**, confirm it meets additional safety assurance standards:
     + Contributions to hazards and controls for safety-critical functions are identified, tracked, and verified.
     + Discrepancies in safety-critical software and workarounds are dispositioned with Software Assurance approval.
8. **Evaluate Risks with Heritage Reviews or Trade Studies:**

   * Verify that risk analyses, trade studies, and heritage assessments are conducted for impacts to safety, quality, security, or reliability.

By following this structured approach, Software Assurance personnel can effectively assess and ensure compliance with the requirements for acquiring or using third-party software components under this requirement.

### 7.4.2 Example COTS Safety Checklist

|  |  |
| --- | --- |
| This is not a complete list. Each Center or Project should add to, remove, or alter the list which applies to their tools. Not all questions apply to all COTS, MOTS, GOTS, OSS, or reuse software or tool types. This checklist helps the thought processes when considering if software tools or programs (embedded or standalone) could contribute to a hazard by either providing a false or inaccurate output or developing software with flawed algorithms, paths, execution timing, etc. | |
| 1. Were any risk analyses or trade-off analyses performed? | |
|  | a.    Where and how are the COTS, MOTS, GOTS, OSS, or reuse software planned to be used? |
|  | b.    What features will not be used, and how can they be prevented from inadvertent access? |
|  | c.     What changes to the rest of the system are needed to incorporate the COTS, MOTS, GOTS, OSS, or reuse software? |
|  | d.     Where are the results of the trade study documented, and are they being maintained? |
| 2. How adequately does the SW Management Plan address the COTS, MOTS, GOTS, OSS, or reuse software in its system(s), or is there a standalone COTS, MOTS, GOTS, OSS, or reuse software management plan? | |
|  | a.   Does the plan address how version changes and problem fixes to the COTS, MOTS, GOTS, OSS, or reuse software will be handled during development? |
|  | i.    What is the decision-making process for what upgrades will be made and when they will be made? |
|  | ii.   How does it address version control for the COTS, MOTS, GOTS, OSS, or reuse software and any wrappers or glueware? |
|  | iii.   If there are multiple COTS, MOTS, GOTS, OSS, or reuse software that interacts, how are upgrades coordinated? |
|  | iv.   What retesting and additional analyses will take place to assure smooth incorporation? |
|  | b.   How will COTS, MOTS, GOTS, OSS, or reuse software be included in the Data Acceptance package and version description documents? |
|  | c.   What Software Classification is assigned to the COTS, MOTS, GOTS, OSS, or reuse software or the SW System in which the COTS, MOTS, GOTS, OSS, or reuse software is used? |
|  | d.   Does SA agree with the Software Classification? With the Safety Assessment? |
|  | e.   Is the plan complete for the appropriate level(s) of SW Classification? |
|  | f.    How will risks be captured and managed? |
|  | g.   Does it cover the issues listed above? |
|  | h.   Does the plan make sense? |
| 3. Other SW or system plans will need to be reviewed to assure that they address the COTS, MOTS, GOTS, OSS, or reuse software: | |
|  | a.   Has the software maintenance plan been reviewed? |
|  | i.    How will COTS, MOTS, GOTS, OSS, or reuse software be upgraded or replaced once in operation |
|  | ii.   What trigger points will be used to determine the need/benefits vs. potential instability caused by upgrades or replacement of COTS, MOTS, GOTS, OSS, or reuse software? |
|  | b.   Have retirement plans been reviewed? |
|  | c.   Have safety plans been reviewed? |
|  | d.   Have assurance plans (which address all that is listed here and possibly more)been reviewed? |
| 4. A review of the requirements the COTS, MOTS, GOTS, OSS, or reuse software is supposed to be fulfilling: | |
|  | a.   Functional requirements, |
|  | b.   Interface requirements, |
|  | c.   Performance requirements |
|  | d.   Wrapper software requirements |
|  | e.   Has the functionality of the COTS, MOTS, GOTS, OSS, or reuse software not to be used identified, and how will it be prevented from being used? |
|  | f.    How are the requirements fulfilled by COTS, MOTS, GOTS, OSS, or reuse software being traced from beginning to delivery and beyond? |
|  | g.    Have realistic and complete operational and failure scenarios been written? |
| 5. Participation in the design reviews of how the COTS, MOTS, GOTS, OSS, or reuse software is to be architected into the system, or at least the PDR and CDR of the systems should address the COTS, MOTS, GOTS, OSS, or reuse software. | |
|  | a. Does it meet the requirements placed on it? |
|  | b. Has the risk analyses been performed? |
|  | c. Have the safety analyses been performed and presented to the appropriate phase? |
| 6. Safety: How will Hazard analyses be run on the COTS, MOTS, GOTS, OSS, or reuse software or systems with COTS, MOTS, GOTS, OSS, or reuse software? | |
|  | a. By its functions, or just as inputs and outputs through a wrapper? |
|  | b. What if it is an OS, are the safety personnel aware of how to cover OS in an HA? |
|  | c. Possible hazard causes and effects on safety-critical systems? |
|  | d. Its applications, glueware, and or wrappers? |
|  | e. How to mitigate possible hazards that a COTS, MOTS, GOTS, OSS, or reuse software could trigger? |
| 7. Review of verification and validation plans, procedures, results, | |
|  | a. How will it be tested? |
|  | i. White box testing? |
|  | ii. In situ testing? |
|  | iii. Can it be tested standalone to ensure it meets the needs it is intended for? |
|  | b.   How are upgrades to the COTS, MOTS, GOTS, OSS, or reuse software verified and validated? |
|  | c.   What are the plans and procedures? |
|  | d.    Proof that it does not utilize undesired features? |
|  | e.   Are any safety controls and mitigations tested sufficiently? |
|  | f.    When best to participate in testing to assure the COTS, MOTS, GOTS, OSS, or reuse software are working properly and have been incorporated properly? |
| 8. Reliability | |
|  | a.   What are the performance measures? |
|  | i.    Expected? |
|  | ii.   Measured? |
|  | iii.   What are the issues with crashes, input, or memory overloads? |
|  | b.   How does it fail? |
|  | i.    What are the conditions that lead to failure or fault? |
|  | ii.    What are the operational limits? |
|  | iii.    What are the impacts of those failures or faults? |
|  | iv.    Are there any predictors that can measure and lead to the prevention of a failure? |
|  | v.    What protections need to be provided? |
|  | 1. In the operations? |
|  | 2. In the glueware/wrappers? |
|  | c.   How does the COTS, MOTS, GOTS, OSS, or reuse software provide notifications of faults and failures? |
|  | d.   How does it get reset? |
|  | e.   What measurements should be taken, and when, to understand the reliability of the COTS, MOTS, GOTS, OSS, or reuse software? |
|  | i. During integration and incorporation into the system (interface problems, trouble with support SW, etc.)? |
|  | ii. During systems checkout and testing? |
|  | iii. During operations? |
| 9. Metrics should be determined to assure performance and quality within the system or as a standalone tool. | |
| 10.    SW Assurance of any associated developed software needs to carry the same SW Classification and safety assessment and thus the appropriate normal software engineering and assurance: | |
|  | a.   glueware |
|  | b.   wrappers |
|  | c.   applications |
|  | d.   Interfaces |
|  | i.     human |
|  | ii.   other systems/software |
|  | iii.   Hardware including Programmable Logic Devices |
| 11. Lessons learned of problems, changes, adaptations, usage, programmability, etc.: | |
|  | a.    Including its applications, glueware, and or wrappers? |
|  | b.    Provide information and evidence if the COTS, MOTS, GOTS, OSS, or reuse software product(s) worked, and provide documentation of both problems and solutions. |

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality), [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

## 7.5 Additional Guidance

Additional guidance can be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights) * [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice)        * [6.3 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SWEHBVC/pages/96174179/6.3+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) * [6.4 - Checklist for Choosing Off-The Shelf Software (OTS)](/spaces/SWEHBVD/pages/102695563/6.4+-+Checklist+for+Choosing+Off-The+Shelf+Software+OTS) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-024 - Checklist for Choosing Off-The Shelf Software](/spaces/SITE/pages/116293728/PAT-024+-+Checklist+for+Choosing+Off-The+Shelf+Software) * [PAT-025 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SITE/pages/116294244/PAT-025+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) |

# 8. Objective Evidence

Objective evidence substantiates the claims and activities performed to ensure compliance with the requirements for **COTS, GOTS, MOTS, OSS, or reused software**.

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

## 8.1 Objective Evidence to Be Collected

### 8.1.1 Identified Software Requirements:

* Software requirements for COTS, GOTS, MOTS, OSS, or reused software, including project-specific functionality, safety, and performance requirements.
* Requirements defined in the Software Requirements Specification (SRS), linking software features to project requirements.

### 8.1.2 Software Documentation:

* Documentation provided by the vendor or open-source community, including:
  + User guides, API references, installation instructions.
  + Licensing agreements and usage terms.
  + Maintenance plans and support documentation (if available).

### 8.1.3 Verification and Validation Evidence:

* Test plans, procedures, and reports showing the selected software was verified and validated for its intended use.
* Evidence that testing met the same standards as an equivalent developed software component.

### 8.1.4 Rights and Licensing Evidence:

* Signed agreements, records, or approvals from the Center Intellectual Property Counsel regarding proprietary rights, usage terms, and warranties.

### 8.1.5 Vendor Reported Defects Review:

* Data or logs showing periodic reviews of vendor-reported defects and assessments of their impact.
* Documentation of identified risks and mitigation steps.
