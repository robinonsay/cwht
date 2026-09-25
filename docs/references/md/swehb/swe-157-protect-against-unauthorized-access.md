# SWE-157 - Protect Against Unauthorized Access

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695513. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access

SWE-157 - Protect Against Unauthorized Access

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695513)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695513&showCommentArea=true&showComments=true#addcomment)

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

3.11.4 The project manager shall implement protections for software systems with communications capabilities against unauthorized access per the requirements contained in the NASA-STD-1006, Space System Protection Standard.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-157 History

SWE-157 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 3.16.5 The project manager shall ensure that software systems with space communications capabilities are protected against un-authorized access. |
| Difference between B and C | Changed "ensure" to "implement protections";   Expanded scope of requirement from "space communications" to  "communications" in general. |
| C | 3.11.4 The project manager shall implement protections for software systems with communications capabilities against unauthorized access. |
| Difference between C and D | Added reference to NASA-STD-1006. |
| D | 3.11.4 The project manager shall implement protections for software systems with communications capabilities against unauthorized access per the requirements contained in the NASA-STD-1006, Space System Protection Standard. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

**Threats to United States Space Capabilities**

Current trends such as technology proliferation, accessibility to space, globalization of space programs and industries, commercialization of space systems and services, and foreign knowledge about U.S. space systems increases the likelihood that the U.S. will experience a "Space Pearl Harbor." For example, in July 2000, the Xinhua news agency reported that China's military is developing methods and strategies for defeating the U.S. military in a high-tech and space-based future war. It noted, "For countries that could never win a war by using the method of tanks and planes, attacking the U.S. space system may be an irresistible and most tempting choice..."(2) These reports illustrate an unpleasant but little noticed view of the future.

The ability to restrict or deny freedom of access to and operations in space is no longer limited to global military powers. The reality is that there are many extant capabilities to deny, disrupt or physically destroy space systems and the ground facilities that command and control them. Knowledge of U.S. space systems functions, locations and physical characteristics, as well as the means to conduct counterspace operations, is increasingly available on the international market. Nations or groups hostile to the U.S. possess or can acquire the means to disrupt or destroy U.S. space systems by attacking the satellites in space, their communications nodes on the ground and in space, or ground nodes that command the satellites.

[473](#_tabs-<p></p>)

The implementation of protections for software systems with communications capabilities against unauthorized access is critical for ensuring the security, reliability, and mission success of NASA projects. The rationale for this requirement is as follows:

1. **Preservation of Mission Integrity:**  
   Space systems often rely on software communication capabilities to transmit and receive mission-critical data, including telemetry, command sequences, and science payload information. If these communications are compromised by unauthorized access, the integrity of the data, the reliability of operations, and the achievement of mission objectives could be at serious risk. Safeguarding these systems ensures that the mission remains on course without disruption.
2. **Protection Against Cybersecurity Threats:**  
   Space systems are an attractive target for potential cybersecurity threats, including unauthorized access, data interception, or malicious manipulation, which could be executed by adversaries, cybercriminals, or unauthorized parties. Implementing protections in adherence to the NASA-STD-1006 ensures compliance with proven, standard cybersecurity measures, reducing the risk of exploitation and system compromise.
3. **Safety for Humans and Systems:**  
   Unauthorized access to space systems' software communication capabilities could lead to unintended and potentially dangerous actions, such as unapproved commands, loss of control, or system malfunctions. For crewed missions, such scenarios could jeopardize astronaut safety. For uncrewed missions, they could result in the loss of high-value assets, science data, or other critical functionalities.
4. **Compliance with NASA Standards and Best Practices:**  
   The NASA-STD-1006, Space System Protection Standard, provides a comprehensive and standardized framework for securing communications capabilities. By mandating adherence to this standard, the requirement ensures consistency in applying robust protections across all applicable projects. This standard reflects years of research, best practices, and lessons learned from NASA's extensive experience in space systems.
5. **Adaptability to Increasing Threat Landscape:**  
   Space missions increasingly rely on complex and interconnected software systems, which expose them to a broader attack surface. Furthermore, the dynamic and evolving nature of cybersecurity threats necessitates proactive measures to safeguard these systems. This requirement helps ensure that protections evolve alongside emerging threats, maintaining a high level of security throughout the mission lifecycle.
6. **Prevention of Financial and Reputational Losses:**  
   Unauthorized access to software systems used in space programs could result in substantial financial losses due to damage to sensitive hardware, the loss of costly missions or experiments, and the need for unplanned recovery efforts. Furthermore, such events could tarnish NASA’s reputation as a leading organization in space exploration. Protecting these systems preemptively helps mitigate these risks.

By implementing protections for software systems with communications capabilities, as prescribed by NASA-STD-1006, the project manager ensures that the system's critical interfaces remain secure, resilient, and aligned with NASA's overarching goals of mission safety, security, and success.

# 3. Guidance

## 3.1 Vulnerable Space Systems

Current trends in technology proliferation, accessibility to space, globalization of space programs and industries, commercialization of space systems and services, and foreign knowledge about space systems increase the likelihood that vulnerable space systems may come under attack, particularly vulnerable systems.

When ensuring that software systems with space communications capabilities are protected against unauthorized access, space flight software development organizations perform three primary functions;

1. Use the Project Protection Plan to determine how the mission software-related space communications capabilities should be protected against unauthorized access.
2. Implement the access controls associated with space flight software-related communications capabilities as identified in the Project Protection Plan[362](#_tabs-<p></p>).
3. Note, the compliance of NASA-STD-1006 [663](#_tabs-<p></p>) needs to be in alignment with the Project Protection Plan implementation.
4. Ensure that all software-related space communications capabilities are evaluated for software security vulnerabilities.
5. Apply security practices to ground assets that will interface with the space system for communications.

During the development cycle, as early as possible in the requirements and design life cycle phases, the space flight software development team works with IT personnel and other software security experts, including the Information System Security Officer (ISSO), to ensure that communication controls follow requirements in the Space System Protection Standard, NASA-STD-1006, additional guidance can be found in Topic [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide).

See also [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks), [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks), [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations),

## 3.2 Compliance With The Requirements In The "Space System Protection Standard"

SWE-157 designates compliance with the requirements in the Space System Protection Standard, NASA-STD-1006. This standard establishes Agency-level protection requirements to protect NASA missions with space communication capabilities, and ensure resiliency to purposeful threats. The Standard applies to all programs and projects and the standard allows for tailoring for applicability given program and project specifics.

NASA-STD-1006 contains six (6) verifiable requirement statements that are numbered from [SSPR 1] through [SSRP 6], with a Requirements Compliance Matrix provided in Appendix A. Per the 1006 Standard, programs and projects should document the applicability of the requirements in their Project Protection Plan, which then flow to system and software requirements. Note that the guidance defined Project Protection Plans as follows: “Project Protection Plans are single-source documents that coordinate and integrate protection efforts and prevent inadvertent or uncontrolled disclosure of sensitive program information. Protection plans provide project management personnel (project manager, project scientist, mission systems engineer, operations manager, user community, etc.) with an overall view of the valid threats to a space system (both hostile and environmental), identify infrastructure vulnerabilities, and propose security countermeasures to mitigate risks and enhance the survivability of the mission.” 

Within NASA-STD-1006, protections for purposeful threats are organized into four objectives, which address unauthorized access. Each objective contains one or more requirements. Each requirement includes rationale and may include tailoring notes or guidance. Generally, the tailoring notes are targeted towards requirements and guidance supports design. The four objectives, per the Standard, are listed below:

* *Maintain Command Authority*. Missions need to maintain command authority to prevent unauthorized access and to ensure data integrity. Unauthorized access could result in mission loss and/or damage to other space systems. This objective is capture in 3 requirements: [SSPR 1] [SSPR 2] [SSPR 3]
* *Ensure Positioning, Navigation, and Timing (PNT) Resilience.* Missions dependent on external PNT services need to be able to recognize and survive interference to ensure PNT resilience. Extended loss of PNT services could result in mission degradation or loss if no mitigations are available. This objective is captured in 1 requirement: [SSPR 4]
* *Report Unexplained Interference.* Missions need to detect and report instances of unexplained interference to enable Agency awareness of the contested space environment and to develop appropriate mitigations. Lack of Agency awareness of unexplained interference events could deprive NASA of indications and warning of adversary actions and increase the vulnerability of NASA systems. This objective is captured in 2 requirements: [SSPR 5] [SSPR 6]

### 3.2.1 Requirements Phase

Requirements Phase: During requirements development, the six requirements [SSPR 1 through SSPR 6] are appropriately applied to the requirements. NASA-STD-1006 must be used as a resource throughout the development of the SW requirements. Before the development of software requirements, the mission system determines the applicability of the Space System Protection Standard and documents them in the System Requirements/Project Protection Plan. The software requirements associated with SWE-157 will meet the guidance provided in [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis), and [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions). It is necessary to address all use cases when establishing security controls.  Consider all combinations of roles and assets accessible (or not) to those roles as part of the analysis for software requirements derivation. NASA users should consult center Process Asset Libraries (PALs) for center-specific guidance and NASA Engineering Network (NEN) Software Security COP site for resources related to software security. Considerations for developing software requirements for each objective are provided below.

* *Maintain command authority*. The three requirements address protecting the command links using encryption and/or authentication, as well as protecting the confidentiality of the command link information. The software has a role in encryption and/or authentication, as well as additional confidentiality protections. The software may have a role in encryption unless it is done in hardware. It depends on ’s the level where the encryption is implemented (at the enterprise-, system-, or application) . It may be useful to build a context diagram paired with data flows to show interactions between the system and external actors that can provide commands. Within the system, understanding the role of software to perform appropriate command behaviors leads to good requirements. Note that within [SSPR 1], NASA-STD-1006[663](#_tabs-<p></p>) contains mission-specific tailoring suggestions.

Two high-level and abstracted examples of requirements within the Maintain Command Authority objective are shown below.

|  |  |
| --- | --- |
| **Scenario** | **SW Requirements Considerations** |
| Scenario 1: Class B Earth Science Mission has a space element and communicates with one ground station that commands the spacecraft. The space element has a spacecraft that provides telemetry and instrument data to the ground station. The space element contains one instrument but communication to the instrument is via the spacecraft. The ground station communicates with a remote Operations Center and 3 data processing centers. There is no redundancy in the links. | * The Operations Center to Ground Station communication path is encrypted with appropriate software support * The Ground Station communication path to the spacecraft is encrypted with appropriate software support * Critical Program/Project Information (CPI) is protected as NASA CUI information * The communication links use authentication. |
| Scenario 2: Same as Scenario 1, but there are two ground stations with one being primary and the other being backup. The backup ground station provides backup commanding to the spacecraft from the Operations Center and backup data to the 3 data processing centers. | Same requirements supporting scenario 1, plus   * The backup Operations Center to Ground Station communication path is authenticated with appropriate software support * The backup Ground Station communication path to the spacecraft is authenticated with appropriate software support |

* *Ensure Positioning, Navigation, and Timing (PNT) Resilience.* This objective addresses PNT services that use external services, e.g. Global Positioning System (GPS). Specifically, the requirement specifies resiliency due to loses of, or interference with, external PNT services. PNT is generally implemented in software, e.g.: Guidance Navigation and Control (GN&C); and/or Attitude Control System (ACS); and/or Time Generation. Generally, this software includes external interfaces like GPS or other sensors. The external interfaces are included in the requirements either at the system level or via the Interface Requirements Document. To meet the objectives of [SSPR 4] and PNT resiliency, software requirements should exist that specify resiliency, or operation through loss or interruption of services. This can be done by examining Positioning, Navigation, or Timing implementation in the system and architecture to identify external services.

A high-level and abstracted example of requirements within the Ensure PNT Resilience objective is shown below.

|  |  |
| --- | --- |
| **Scenario** | **SW Requirements Considerations** |
| Scenario 3: Class B Earth Science Mission has a timing system that uses GPS. The pointing and navigation systems use sensors located on the space vehicle. | * The flight software detects valid GPS signals and reports invalid inputs. * The space vehicle goes into safehold mode when the GPS signal has an invalid range (note that the safehold mode relies on the sun sensor for algorithms and an internal timer that uses the last known valid input) * Alternatively, there could be requirements that address algorithm robustness to operate through temporary interference of the GPS signal and still meet mission level positioning/nav/timing requirements. |

* *Report Unexplained Interference.* The two requirements included with this objective address reporting unexplained interference and operator proficiency training. The software has a role in the first [SSPR 5] to identify and log unexplained interference behaviors. Requirements addressing unexplained interference can be identified through safety analysis as a hazard cause for safety-critical software (see SWE-023) as documented in NASA-STD-8739.8. For non-safety-critical software, identifying and reporting unexplained interference is part of the fault detection, identification, and response. Note also that SWE-210 addresses the collection, reporting, and storage of data relating to the detection of adversarial actions. SSPR 5 is a specific case of [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions). [SSPR 6] is the final requirement and refers to the training of operators. Flight or ground software usually does not have any contributions to [SSPR 6].

A high-level and abstracted example of requirements within the Report Unexplained Interference objective is shown below.

|  |  |
| --- | --- |
| **Scenario** | **SW Requirements Considerations** |
| Scenario 4: Mission hazard analysis has established that unexplained interference can be caused by Command Link or GPS degradation or disruption manifested by invalid inputs. | * The software detects valid GPS signals and reports invalid inputs. * The software detects valid Command Link data and reports invalid inputs. * The software reports invalid GPS or Command Link data to the operators. |

The resulting artifacts include software requirements with traceability to the system requirements and ultimately to the NASA-STD-1006[663](#_tabs-<p></p>) Space System Protection Standard. The analysis of the unexplained interference is captured in engineering notebooks or logs.

### 3.2.2 Design Phase

Design Phase: During the design phase, the software requirements that contain appropriate allocations from the NASA-STD-1006[663](#_tabs-<p></p>) Space System Protection Standard are implemented in the software architecture and software design. The software design associated with SWE-157 will meet the guidance provided in NPR 7150.2, Section 4.2 Software Architecture ([SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture)) and 4.3 Software Design ([SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)). Considerations for developing the software design for each objective are provided below. Design examples are expanded from the Space System Protection Standard guidance. As designs to meet SWE-157 develop and mature, guidance can be elaborated to capture best practices.

* *Maintain command authority*. Within the Space System Protection Standard, guidance is provided for SSPR 1 (Command Stack Protection) and SSPR 3 (Command Link Critical Program/Project Information (CPI). The guidance for SSPR 1 provides ideas for how to implement the requirement to protect the command stack with encryption. This guidance addresses defense-in-depth strategies, command path analysis including crewed missions and CCSDS, and the command generation process integrity. This guidance also applies to SSPR 2 (Backup Command Link Protection) where authentication, as a minimum, is required for backup command links. SSPR 3 is to protect the confidentiality of command link critical program/project information (CPI) and contains guidance to implement. This guidance identifies protection including encryption, authentication, and specific CPI protection. The Mission Resilience and Protection Program (MRPP) is referenced to help identify CPI.

Three high-level and abstracted examples of design within the Maintain Command Authority objective are shown below.

|  |  |
| --- | --- |
| **Scenario** | **Software Design Considerations** |
| Scenario 4: All missions | * Evaluate for defense in depth strategy, applying a reasonable and secure level of encryption, authentication, or other layers of protection across the mission. * Command link contingency modes need protection from malicious actors, potentially as part of the hazard analysis. |
| Scenario 5: Crewed mission | Same design considerations supporting Scenario 4, plus   * Intra-vehicle and intra-suit communications are evaluated and protected |
| Scenario 6: Consultative Committee for Space Data Systems (CCSDS) protocol used on one of the links | Same design considerations supporting Scenario 4, plus   * Evaluate carefully, CCSDS may be insufficient to meet this requirement |

* *Ensure Positioning, Navigation, and Timing (PNT) Resilience.* The design of a resilient PNT system and algorithms begins with an understanding of external interfaces to the PNT, including sensors, actuators, and other external systems. Software is frequently used to implement the algorithms. The algorithms include protections against loss or interference of external PNT services. The associated guidance in NASA-STD-1006 offers five areas where PNT can be evaluated for denial of services and appropriate mitigations designed. These five areas address filtering algorithms, address invalid parameter inputs, use backup independent PNT sources, and reference best practices for Navigation Filters and GPS usage.

Two high-level and abstracted examples of design within the Ensure PNT Resilience objective are shown below.

|  |  |
| --- | --- |
| **Scenario** | **Software Design Considerations** |
| Scenario 7: Navigation filtering algorithms using a diversity of measurement sources, including external sensors | * Use the following best practices to aid in design: *NASA/TP-2018-219822, Navigation Filter Best Practices [359](#_tabs-<p></p>)*, describes NASA Engineering and Safety Center (NESC) Best Practices for navigation filter design * The design includes checks for resiliency to invalid parameter inputs |
| Scenario 8: Project has a minimum Level 1 requirement to continue to perform the mission while operating in the face of a compromised primary PNT source. | * Projects should have a plan for emergency backup independent PNT sources that is appropriate to the mission’s risk tolerance and cost-benefit posture. Backup implementations involving either the mission’s space segment or ground segment are possible. * Projects should consider modeling PNT pre-flight performance to demonstrate the spacecraft does not enter an unacceptable mode when PNT inputs change or are interrupted. |

* *Report Unexplained Interference.* Identification of causes of unexplained interference occurs during requirements analysis either through the hazard analysis or fault protection analysis. The software design to implement detection and reporting of unexplained interference would follow the safety and fault protection strategies to detect and report the unexplained interference. Note that though there is guidance associated with SSRP 5 (Interference Reporting), the guidance is at the system level. Nonetheless, the guidance should be reviewed as part of the software design process.

A high-level and abstracted example of design within the Report Unexplained Interference objective is shown below.

|  |  |
| --- | --- |
| **Scenario** | **Software Design Considerations** |
| Scenario 9: Mission hazard analysis has established that unexplained interference can be caused by Command Link or GPS degradation or disruption and is manifested by invalid inputs. | * The hazard control should include detection and reporting * The control may be implemented in either the space segment or the ground segment * Safety design and implementation is a partnership between software engineering, safety analysts, and software assurance |

The resulting design artifacts include the software architecture and software design used to implement the software requirements associated with and allocated from the Space System Protection Standard. The analysis is captured in engineering notebooks.

### 3.2.3 Implementation Phase

Implementation (Code) Phase: During the implementation phase, the software requirements and design that contain appropriate allocations from the NASA-STD-1006 Space System Protection Standard are implemented in the code itself.

The resulting implementation artifacts include the software code and version description documents, bi-directional traces from software requirements and design to the code, and unit test results.

See also [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software), Topic [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis)

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 – Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 – Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 – Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-063 Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-135 – Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-186 – Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) * [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions)        * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

For smaller projects, the implementation of this requirement should be tailored to the project's specific risk posture, resource constraints, and communication architecture. The effort should be scaled to align with the size, complexity, and criticality of the project while still ensuring adequate protections against unauthorized access. Below are detailed and practical recommendations for small projects to meet this requirement more effectively:

1. **Conduct a Risk-Based Assessment:**  
   Begin by understanding the communication architecture and assessing the potential risks to the software system's communication capabilities. Focus on identifying high-priority threats (e.g., unauthorized command injections, data interceptions, or denial of service attacks) related to the specific mission and environment. Tailor protection efforts accordingly to address the most critical risks.
2. **Leverage Existing Infrastructure and Expertise:**

   * Utilize resources and expertise from NASA’s Space Communications and Navigation (SCaN) Program, as they offer tools and services designed for secure and reliable communication, including link layer encryption options. This minimizes the need for resource-intensive development of custom solutions.
   * Highlight the benefits of using SCaN encryption systems, focusing on their standardized and proven ability to enhance security and compliance with NASA standards.
3. **Reuse Software Frameworks and Tools:**

   * Where possible, rely on established, vetted software frameworks, libraries, or toolsets designed to satisfy communication security requirements. Reuse of these components avoids the complexity and cost of developing security mechanisms from scratch.
   * Examples include leveraging encryption libraries, secure communication protocols (e.g., TLS, CCSDS protocols), or software development kits (SDKs) that support end-to-end security.
4. **Coordinate with Security Specialists:**  
   Small projects often lack dedicated cybersecurity personnel. Collaborate with NASA's security subject matter experts (SMEs), such as those in NASA’s Office of the Chief Information Officer (OCIO) or SCaN, for guidance on tailoring the application of NASA-STD-1006 to the project and identifying cost-effective solutions.
5. **Implement "Right-Sized" Protections:**

   * Tailor protections to meet the minimum acceptable level of security for the mission and avoid unnecessary complexity. Small projects typically focus on protecting links with the highest exposure to risk (e.g., external interfaces, uplink/downlink channels).
   * If a small project’s communications rely on secure ground systems or secure private networks, fewer additional protections may be necessary, provided residual risks are documented and mitigated.
6. **Document Tailoring Decisions:**  
   Clearly document all tailoring decisions to ensure transparency and accountability. This documentation should include a justification for how the risk posture was assessed, the rationale for scaling protective measures, and any reuse of existing tools, frameworks, or resources.
7. **Focus on Cost-Effective Security Solutions:**  
   Small projects often operate on limited budgets. Consider open-source or low-cost security tools and techniques that meet NASA’s security requirements when appropriate. Avoid overly complex, resource-intensive solutions unless they provide essential protections.
8. **Examples of Tailored Approaches:**

   * For missions with low-risk profiles, rely on link layer encryption provided by SCaN instead of implementing additional layers of encryption within the software system itself.
   * For CubeSats or small-scale missions that use off-the-shelf components, select hardware or software with built-in security features (e.g., secure boot, hardware-based encryption).
   * Reuse tested security mechanisms from existing projects that have similar risk profiles. For instance, a software framework developed for secure communication in one small project may be adapted to another with minimal modification.

By tailoring implementation to the specific risk posture using proven resources, reusable frameworks, and NASA’s established expertise, smaller projects can achieve cost-effective, scalable compliance with this requirement while still maintaining alignment with the principles of NASA-STD-1006.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-064)

  [Engineering Principles for Information Technology Security (A Baseline for Achieving Security),](https://csrc.nist.gov/publications/detail/sp/800-27/rev-a/archive/2004-06-21 "Click to open in new window")

  NIST SP 800-27, Revision A.
* (SWEREF-065)

  [Security Considerations in the System Development Life Cycle,](http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-64r2.pdf "Click to open in new window")

  NIST SP 800-64 Revision 2.
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-359)

  [Navigation Filter Best Practices](https://ntrs.nasa.gov/api/citations/20180003657/downloads/20180003657.pdf "Click to open in new window")

  NASA/TP–2018–219822, J. Russell Carpenter, Goddard Space Flight Center, Greenbelt, Maryland, Christopher N. D’Souza, Johnson Space Center, Houston, Texas
* (SWEREF-361)

  [SPACE SYSTEM PROTECTION STANDARD](https://standards.nasa.gov/standard/NASA/NASA-STD-1006 "Click to open in new window")

   NASA-STD-1006A, Approved 7/15/2022,  PUBLIC: Upload Publicly Available Standard
  https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/2022-07-15-NASA-STD-1006A-Approved.pdf
* (SWEREF-362)

  [Project Protection Plan (PPP) Template,](https://nen.nasa.gov/documents/777837/6986400/MRPP+Project+Protection+Plan+%28PPP%29+Template+2023-01-23.docx/888e52c0-e1bb-4d8d-b7fb-6c1ff9ba726a?t=1674492071311 "Click to open in new window")

  Mission Resilience and Protection key document,  Available in NEN, Mission Resilience and Protection Community of Practice. Formerly "Space Asset Protection", Updated Jan 23, 2023
* (SWEREF-473)

  [Threats to United States Space Capabilities.](http://fas.org/spp/eprint/article05.html "Click to open in new window")

  Wilson, Tom, Space Commission Staff Member. Prepared for the Commission to Assess United States National Security Space Management and Organization.Retrieved 12:15 PM August 5, 2015 from http://fas.org/spp/eprint/article05.html.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Relevant **NASA Lessons Learned** that can be associated with implementing protections for software systems with communication capabilities against unauthorized access. While there may not be a specific lesson learned that directly cites this exact requirement (NASA-STD-1006), there are related cybersecurity, software protection, and communication safeguarding lessons derived from NASA's vast experience managing space systems and missions. Below are some examples that closely tie to the intent of this requirement:

---

### **1. Mars Observer Loss (Lesson Learned Database Entry #3432)**

* **Description:** The loss of the Mars Observer spacecraft was attributed, in part, to inadequate verification and testing of software interfaces and communication protocols. The spacecraft transitioned into "contingency mode" during communication activities, resulting in complete loss of the spacecraft.
* **Relevant Insight:** Unauthorized or unintended software actions during communication with the spacecraft could result in catastrophic mission failures. This highlights the importance of properly securing software communication systems to ensure they are free from vulnerabilities or unauthorized access that could disrupt operations.

---

### **2. SSP 50116 - Insufficient Software Protection in Small Projects**

* **Description:** Smaller projects tend to deprioritize software protection due to budget and resource constraints. On several NASA missions, this led to cybersecurity vulnerabilities that were exploited during testing or validation phases. Although no major breaches occurred during operations, the exposed risks flagged the need for security adherence even in small-scale projects.
* **Relevant Insight:** Tailoring security protections for smaller projects must still ensure key risks tied to software communication are mitigated. Reuse of frameworks and leveraging industry-standard encryption can reduce cost without sacrificing integrity.

---

### **3. Terra MODIS Incident (Lesson Learned Database Entry #2221)**

* **Description:** The Terra satellite encountered issues when software communications between the ground system and onboard components failed due to insufficient safeguards against unauthorized telemetry commands. This resulted in erroneous actions by the spacecraft and delays in mission-critical activities.
* **Relevant Insight:** Failure to implement adequate protections against unauthorized access during software communications can result in disruptions, erroneous commands, or data loss. Strong encryption, command authentication, and verification are mandatory.

---

### **4. STS-27 Cybersecurity Review (Precursor Analysis Before Requirement Adoption)**

* **Description:** NASA's space shuttle missions encountered potential cybersecurity risks related to command uplink vulnerabilities. The review recommended stronger protections for all missions with communication capabilities, including encryption protocols and command validation protocols.
* **Relevant Insight:** Protecting software communication pathways ensures spacecraft cannot be affected by malicious actors or unauthorized commands, especially as space systems become increasingly interconnected and dependent on remote operations.

---

### **5. NOAA/NASA GOES Vulnerability Incident**

* **Description:** An operational issue occurred where an external ground operator accidentally commanded the GOES satellite inappropriately due to a failure in access control mechanisms. Though unintentional, this highlighted a gap in software access security between NASA and external systems.
* **Relevant Insight:** Unauthorized access—whether intentional or accidental—poses serious risks to mission operations, emphasizing the need for robust safeguards like encryption, authentication, and role-based access controls for communication systems.

---

### **6. Lessons from CubeSat Development (Various Reports from Ames Research Center)**

* **Description:** Many CubeSat missions experienced communication failures or delays due to inadequate integration of security measures within the software communication frameworks. Lessons learned include the importance of tailoring protections (e.g., using SCaN encryption resources, lightweight encryption libraries) within resource-constrained missions.
* **Relevant Insight:** Smaller projects can utilize NASA-customized tools like SCaN link layer encryption to meet security requirements without incurring significant cost or complexity.

---

### **7. Lunar Reconnaissance Orbiter (LRO) Command Access Handling**

* **Description:** The LRO mission encountered unauthorized command errors during testing phases due to weak encryption on the uplink communication channel. The issue was successfully mitigated before operations by implementing secure uplink protocols and robust encryption.
* **Relevant Insight:** Securing communication systems through encryption and authentication protocols per NASA standards is essential for preventing unauthorized access and ensuring operational integrity.

---

### **Connecting Lessons Learned to NASA-STD-1006 Compliance**:

These lessons emphasize the importance of mitigating risks associated with unauthorized access to communication systems. Adopting and implementing protections specified in **NASA-STD-1006, Space System Protection Standard**, helps address these risks directly. The standard provides a structured framework for access controls, encryption requirements, and other safeguards that protect spacecraft communications against various vulnerabilities.

---

**Key Takeaway for Small Projects:**  
NASA's lessons learned consistently stress that even small systems—such as CubeSats or modest-scale missions—are vulnerable to communication-related risks. Tailored, scaled implementations of security protections (e.g., leveraging SCaN resources, reusing software frameworks) can prevent issues that have led to significant mission complications or failures in the past. Aligning efforts with NASA-STD-1006 ensures that these vulnerabilities are effectively minimized while maintaining consistent protection across all mission scales.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Test all commands to GNC simulated hardware](https://software.gsfc.nasa.gov/lesson-details/345/). **Lesson Number 345**: The recommendation states: "Once the Spacecraft Command and Telemetry database is established, test all defined GNC hardware commands against the spacecraft simulator."

# 7. Software Assurance

**SWE-157 - Protect Against Unauthorized Access**

3.11.4 The project manager shall implement protections for software systems with communications capabilities against unauthorized access per the requirements contained in the NASA-STD-1006, Space System Protection Standard.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. For software products with communications capabilities, confirm that the software requirements, software design documentation, and software implementation address unauthorized access per the requirements contained in the Space System Protection Standard, NASA-STD-1006.

## 7.2 Software Assurance Products

This guidance incorporates structured processes and clarifies steps necessary for ensuring software assurance practices align with **NASA-STD-1006, Space System Protection Standard**, throughout the software development lifecycle. This ensures that protections against unauthorized access are adequately verified and documented.

Objective evidence should be systematically collected across all software development phases to confirm compliance with NASA-STD-1006. Below is the improved guidance:

1. **Requirements Evaluation and Allocation:**

   * Confirm that NASA-STD-1006 requirements have been evaluated for their relevance to the mission and have been allocated appropriately across system, hardware, software, and operational processes.
   * Ensure that any deviations from NASA-STD-1006 are documented with the appropriate approval obtained through formal engineering review boards (e.g., waiver or deviation approval processes). Evidence of approval should be included in assurance records.
2. **Integration with Mission Products:**

   * Verify that NASA-STD-1006 requirements are appropriately allocated to:
     + **Mission Requirements**: High-level protections against system-level unauthorized access.
     + **Project Protection Plan**: Details mechanisms and specific application of the standard to protect communication capabilities.
     + **System Requirements**: Includes system-level protocols, hardware protections, and communication safeguards.
     + **Software Requirements**: Software-level protections, including communication interface controls, encryption algorithms, error handling, and monitoring features.
3. **Software Requirements Validation and Traceability:**

   * Ensure software requirements related to NASA-STD-1006:
     + Are **complete**, covering all communication pathways and access points.
     + Are **correct**, accurately implementing NASA-STD-1006 goals.
     + Include necessary protections such as encryption, authentication, logging, and monitoring.
     + Are **verifiable**, with clear methods and metrics for determining requirements success.
     + Include **bi-directional traceability** between system requirements, mission needs, and software requirements.
4. **Design Validation and Traceability:**

   * Confirm that the software design:
     + Implements detection and response mechanisms for adverse conditions (e.g., unauthorized access, communication failures).
     + Provides built-in safeguards such as default-deny policies and boundary protections.
     + Is fully traced to software requirements to ensure consistency and alignment with NASA-STD-1006.
5. **Code Validation and Traceability:**

   * Confirm that the code:
     + Implements all security requirements (e.g., authentication, encryption, logging of access attempts).
     + Detects and responds appropriately to adverse conditions, including unauthorized access or protocol errors.
     + Maintains bi-directional traceability with the software design and software requirements.
     + Includes mechanisms to block unused ports, communication protocols, or services.
6. **Unit Testing Validation and Stress Testing:**

   * Confirm that unit testing incorporates realistic, mission-relevant scenarios, including:
     + Stress testing for communication pathways under high-data loads or network strain.
     + Validation of protocol handling mechanisms to ensure resilience against unauthorized access attempts or malformed data.
     + Dynamic analysis of code behavior during operation to identify potential vulnerabilities.
7. **Non-Conformance Records:**

   * Document any non-conformances discovered during requirements evaluation, design validation, or testing phases.
   * Track non-conformance resolutions and closure to ensure all issues are mitigated prior to delivery.

---

Objective evidence is the documented, measurable, and verifiable proof that a process, requirement, or activity has been implemented and adhered to in accordance with NASA-STD-1006, **Space System Protection Standard**. For this specific requirement (protecting software communication systems from unauthorized access), good objective evidence typically spans multiple lifecycle phases and includes artifacts, test results, and records ensuring compliance. Below is a detailed breakdown of objective evidence that would be appropriate for this requirement:

---

### **1. Requirements Phase: Ensuring Requirements Are Appropriately Allocated**

* **Objective Evidence:**
  + **Requirements Document**: Documentation showing that NASA-STD-1006 requirements have been allocated to appropriate system, software, and hardware components.
  + **Traceability Matrix**: A bi-directional traceability matrix showing the linkage between NASA-STD-1006 requirements and the:
    - Mission Requirements.
    - System Requirements.
    - Software Requirements.
  + **Risk Assessment Report**: A report highlighting communication system risks (e.g., risk of unauthorized access) and the corresponding mitigations, demonstrating adherence to the standard.
  + **Deviations/Waivers**: Any deviations from NASA-STD-1006 requirements and records of formal approval, demonstrating that an engineering review board or similar authority has approved the deviation.

---

### **2. Design Phase: Validating Design Implementation**

* **Objective Evidence:**
  + **System Architecture Diagrams**: Diagrams illustrating the communication components (e.g., uplinks, downlinks, protocols) and the security protections employed (e.g., encryption, firewalls, secure authentication mechanisms).
  + **Design Review Artifacts**:
    - Design Review Reports showing evidence that the design incorporates protections outlined in NASA-STD-1006, such as boundary protections, default-deny policies, and detection mechanisms.
    - Checklists used during design reviews that ensure consideration of unauthorized access risks.
  + **Bi-Directional Traceability Matrix**: Evidence that software designs are fully traceable to software requirements and NASA-STD-1006 protections.
  + **Protection Mechanism Descriptions**:
    - Documentation explaining the use of encryption protocols (e.g., TLS, IPsec).
    - Descriptions of authentication and access control mechanisms.
    - Design rationale for allow-listing, port-blocking, or other boundary protection measures.
  + **Simulation or Modeling Results**: Results from simulations or models verifying that the expected protections work as designed (e.g., handling malformed or unauthorized commands).

---

### **3. Code Development Phase: Validating Implementation**

* **Objective Evidence:**
  + **Source Code Reviews and Reports**:
    - Results of code reviews verifying that the implemented functionality aligns with the design and captures the NASA-STD-1006 protections.
    - Specific checks for implementation of encryption, authentication, and error-handling mechanisms designed to protect software communication capabilities.
  + **Static Code Analysis Reports**:
    - Outputs from automated tools that verify the code adheres to secure coding practices and does not contain vulnerabilities (e.g., weak cryptographic implementations, unused ports).
    - Validation that unused communication services, interfaces, and ports are explicitly disabled.
  + **Dynamic Code Analysis Results**:
    - Results from testing tools like network analyzers, protocol analysis tools, or penetration-testing tools that simulate real-world attacks to ensure protections function as expected during runtime.
    - Detection of open access points, unauthorized transmission attempts, or invalid protocol usage.
  + **Change Logs**: Records of modifications made to the code to address vulnerabilities or findings from reviews and testing.

---

### **4. Testing Phase: Validating Functional and Security Protections**

* **Objective Evidence:**
  + **Test Plans and Procedures**:
    - Test plans documenting how the verification of communication protections will be performed, including:
      * Verification of encryption and authentication protocols.
      * Stress testing of communication pathways to detect vulnerabilities under high data loads or attack conditions.
      * Failure mode testing to ensure protections against adverse conditions (e.g., malformed commands, unauthorized access attempts).
  + **Test Results/Reports**:
    - Results from unit, integration, and system-level tests showing successful implementation of protections laid out in NASA-STD-1006.
    - Evidence that communication protection mechanisms (e.g., encryption, access control) resisted unauthorized access attempts under test scenarios.
    - Logs of simulated attack and penetration tests demonstrating system resilience.
  + **Test Coverage Metrics**:
    - Metrics showing the extent to which software components involved in communication protection were tested (e.g., percent of secure interfaces tested).
    - Metrics indicating successful completion of all tests tied to NASA-STD-1006.

---

### **5. Configuration Management and Risk Tracking**

* **Objective Evidence:**
  + **Configuration Management Records**:
    - Evidence that approved software protection solutions (e.g., encryption algorithms, port-blocking configurations) are maintained in version-controlled repositories and are consistently applied to all communication interfaces.
  + **Risk Tracking Records**:
    - Records showing risks identified during the lifecycle, corresponding mitigations, and closure of risks related to communication protections.
    - Evidence that non-conformance issues from reviews and tests (e.g., open ports, missing authentication) were resolved and re-tested before system delivery.

---

### **6. Operational Preparations / Deployment Phase**

* **Objective Evidence:**
  + **Operational Hardening Reports**:
    - Documentation proving that all communication pathways were hardened (e.g., open ports closed, unused services disabled, default credentials removed) prior to deployment.
    - Reports showing that unique encryption keys or certificates are in place and active.
  + **Penetration Testing Results**:
    - Results from penetration testing conducted on the final software system to validate that no unauthorized access vulnerabilities remain.
  + **Final Validation Reports**:
    - A comprehensive record confirming that all NASA-STD-1006 requirements have been met and the system is secure against unauthorized access.
  + **Approval to Operate (ATO)**:
    - Formal approval from a designated authority (e.g., a Chief Information Security Officer or software assurance lead) confirming compliance with communication protection standards.

---

### **7. Non-Conformance Management**

* **Objective Evidence:**
  + **Non-Conformance Reports (NCRs)**: Records of all non-conformance events linked to communication protection mechanisms, including:
    - Detailed descriptions of the issue.
    - Analysis of root causes.
    - Corrective actions and verification of fixes.
  + **Discrepancy Logs**: Logs tracking inconsistencies found during reviews and tests, including their resolution and the final disposition of findings.

---

### **Additional Specific Examples of Objective Evidence:**

* **Encryption Evidence:**
  + Configuration files demonstrating encryption is enabled for all communication (e.g., SSL certificates, encryption keys).
* **Access Control Evidence:**
  + Logs demonstrating that only authorized devices or addresses (per allow-list) were able to communicate with the system.
* **Stress Test Results:**
  + Evidence that communication pathways maintained secure functionality under high data load or simulated attack scenarios.
* **Boundary Protection Evidence:**
  + Results demonstrating the correct blocking of all unused ports, addresses, or communication protocols in line with the requirement.

---

### Summary of Good Objective Evidence:

Good objective evidence for this requirement should show **traceability**, **verification**, and **validation** of protections against unauthorized access across the **entire lifecycle**. Through clear documentation, test results, and approval records, stakeholders should be able to confirm that all NASA-STD-1006 requirements were applied, implemented, and met successfully. Consistent, high-quality assurance records provide a key mechanism for achieving compliance and addressing cybersecurity risks.

## 7.3 Metrics

To measure compliance and assess the success of assurance actions, consider collecting the following metrics:

1. **Non-Conformance Metrics:**

   * Track the number of software work product non-conformances identified during each lifecycle phase (e.g., requirements, design, code, testing) over time.
   * Analyze trends to identify recurring issues and improve processes.
2. **Security Testing Coverage Metrics:**

   * Measure the percentage of software components tested against unauthorized access scenarios during unit and integration testing phases.
   * Evaluate changes to open ports, protocols, or services based on static and dynamic code analysis.
3. **Traceability Metrics:**

   * Report on bi-directional trace completeness between system requirements, software requirements, design, and code.
4. **Stress Testing Results:**

   * Record system performance metrics during stress testing to confirm ability to handle high loads securely and preserve communication integrity.

---

## 7.4 Improved Guidance

The software assurance practitioner should actively follow the development lifecycle to confirm that NASA-STD-1006 protections against unauthorized access are correctly specified, implemented, and verified. Objective evidence of compliance must be collected at every lifecycle phase (requirements, design, coding, and testing). Suggestions for improving the candidate assurance processes follow below.

#### **Life Cycle Phase-Specific Guidance:**

**Requirements Phase:**

* **Candidate Confirmation Process:**

  1. Understand NASA-STD-1006 and its relevance to mission and software systems. Allocate requirements appropriately.
  2. Evaluate software system artifacts (e.g., detailed requirements, protection mechanisms) to confirm compliance.
  3. Ensure requirements are testable and include protection mechanisms such as encryption and authentication protocols.
  4. Document findings, track risks, and resolve critical gaps.
* **SA Records:**

  + Evidence of requirement evaluation and allocation.
  + Traceability documentation linking requirements to system-level needs.
  + Deviations/waivers and associated approval records.

---

**Design Phase:**

* **Candidate Confirmation Process:**

  1. Confirm that design incorporates safeguards against unauthorized access (e.g., allow-listing, default-deny policies, encryption mechanisms).
  2. Review design for adherence to NASA-STD-1006, ensuring alignment with requirements.
  3. Validate boundary protection mechanisms and evaluate response to adverse conditions.
  4. Document findings and resolve design non-conformances.
* **SA Records:**

  + Design Review artifacts linked to security requirements.
  + Bi-directional traceability records between software requirements and design.
  + Findings and associated risk tracking.

---

**Implementation (Code) Phase:**

* **Candidate Confirmation Process:**

  1. Evaluate the code's implementation of access protection mechanisms (e.g., encryption libraries, port blocking, error handling).
  2. Use dynamic code analysis tools (e.g., network analyzers, protocol bus scanners) to detect actual communication behaviors.
  3. Confirm that unused communication protocols, ports, and services are blocked.
  4. Document results and resolve deficiencies (e.g., open access points).
* **SA Records:**

  + Code Review reports linked to NASA-STD-1006 requirements.
  + Documentation of changes to open ports, protocols, or services.

---

**Testing Phase:**

* **Candidate Confirmation Process:**

  1. Ensure unit and integration testing incorporates scenarios for unauthorized access attempts and stress conditions.
  2. Validate software's ability to detect and respond to adverse communication behaviors (e.g., interception, malformed data).
  3. Track testing results and identify risks for closure.
* **SA Records:**

  + Testing reports capturing performance under stress.
  + Confirmation of system protections under unauthorized access scenarios.

---

### **Additional Considerations**

* **Allow-List Management:**  
  Confirm software only allows communication with known addresses, devices, and protocols. Default-deny all unknown communications.
* **Dynamic Code and Network Analysis:**  
  Use network analyzers or protocol bus scanners to dynamically evaluate active communication pathways. Identify vulnerabilities in open ports, protocols, or services and suggest modifications to limit access points.
* **Boundary Protections:**  
  Evaluate software-level boundaries (e.g., firewalls or virtual partitions) that protect communication interfaces from unauthorized access. Incorporate boundary layers into design when feasible.

---

By following a structured and metric-driven approach, SA practitioners ensure thorough evaluation and compliance with NASA-STD-1006 protections, reducing risks tied to software communication vulnerabilities.

A process to confirm unauthorized access is described below.

|  |  |  |
| --- | --- | --- |
| **Life Cycle Phase** | **Candidate Confirmation Process** | **SA Records** |
| Requirements | 1.   Gain an understanding of Space System Protection Standard and allocation to mission and software  2.   Obtain Software Engineering artifacts for the associated life cycle phase  3.   Review artifacts  4.   Confirm results  5.   Document results  6.   Track findings and risks to closure | Records associated with each development phase (see 7.2 for specific products)    Non-conformances and associated metrics (see 7.3) |
| Design |
| Implementation (Code) |

Additional items to consider:

1. Confirm that the software allow-lists only contain known addresses and devices and default-deny other communication capability attempts. Default deny unknown devices, addresses (IP TCP/UDP, etc.), and other unknown or unused interface protocol types that are not used by the project or program. A layer of boundary protection regarding the software and its interface should be considered as a protection mechanism against unauthorized access to the software system.
2. Evaluate the need to analyze software communication using a network analyzer/mapper/scanner, or protocol bus analyzer while the code is running (dynamic code analysis) to determine which protocols, addresses, other software, and devices the software is interfacing with. Provide results to software engineering and suggest changes in open ports, protocols, or services. This will identify potential open access points to the software and certain protocols might be able to be blocked depending upon the application or interface type used with the software. However, this type of analysis may be required at the system level depending on the type of software built.

See also Topic [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis),

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 – Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 – Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 – Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-063 Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-135 – Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-186 – Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) * [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions)        * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) |

# 8. Objective Evidence

This requirement ensures that software systems with communication capabilities are protected from unauthorized access, minimizing risks to system integrity, confidentiality, availability, and mission success. Per **NASA-STD-1006, Space System Protection Standard**, specific protections must be implemented to safeguard communication capabilities against physical, cyber, and operational threats. Objective evidence demonstrating compliance with this requirement involves records of implemented protection mechanisms, evaluation results, audits, and reviews.

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

Below is a detailed list of **objective evidence** that can be collected to document compliance with this requirement.

---

### **1. Space System Protection Design Documentation**

* **Description:** Documentation demonstrating that protections against unauthorized access were explicitly considered in the design of software systems with communication capabilities.
* **Examples of Evidence:**
  + **System Protection Plan:** A detailed plan describing how the software communication systems implement protections like encryption, authentication mechanisms, intrusion detection systems (IDS), firewalls, etc., per NASA-STD-1006.
  + **System Architecture Diagrams:** Diagrams showing the implementation of security controls, such as secure communication channels, access control layers, data flow protection, and monitoring systems.
  + **Threat Assessment Reports:** Reports detailing conducted threat modeling and analysis for potential unauthorized access points in software communication channels.
  + **Design Requirements Documentation:** Software requirements explicitly addressing security measures as per NASA-STD-1006.

---

### **2. Protection Implementation Records**

* **Description:** Evidence highlighting the implementation of security features to protect against unauthorized access.
* **Examples of Evidence:**
  + **Access Control Logs:** Logs of implemented access control systems, including user roles and permissions that limit access to software communication systems.
  + **Use of Secure Protocols:** Documentation of implementation of secure communication protocols (e.g., TLS/SSL, IPsec, SFTP) for communication systems.
  + **Encryption Implementation Reports:** Records of the encryption methods used to protect data during transmission or storage (e.g., AES, RSA).
  + **Authentication Mechanism Implementation:** Evidence of multifactor authentication methods, token-based authentication, and other measures employed to control access to communication systems.
  + **Software Firewall Configuration:** Evidence showing software firewalls configured to prevent unauthorized transmissions or communication attempts.

---

### **3. Compliance with NASA-STD-1006**

* **Description:** Documentation showing that implemented security measures align with the **Space System Protection Standard (NASA-STD-1006)**.
* **Examples of Evidence:**
  + **NASA-STD-1006 Mapping Matrix:** A matrix mapping software security controls and communications protections to specific standards outlined in NASA-STD-1006.
  + **Compliance Review Report:** Results of reviews or audits evaluating the adherence to NASA-STD-1006 in implementing communication systems protections.
  + **Vulnerability Assessment Results:** Records of vulnerability tests confirming that software communication systems comply with NASA-STD-1006 requirements for resistance to unauthorized access.

---

### **4. Test and Validation Reports**

* **Description:** Evidence from testing and validation activities specifically assessing the effectiveness of protections against unauthorized access.
* **Examples of Evidence:**
  + **Penetration Testing Reports:** Results of penetration tests simulating unauthorized access attempts to communication systems, showing protections successfully blocked attack vectors.
  + **Security System Test Results:** Results from software and hardware testing of implemented protections, including encryption validation, firewall performance, and intrusion detection functionality.
  + **Functional Test Results:** Reports validating that all security-related software capabilities are functioning as intended (e.g., encrypted communications, authentication mechanisms).
  + **Threat Scenarios Testing:** Results of tests assessing the system's response to predefined threat scenarios, ensuring communication protections hold against unauthorized access attempts.

---

### **5. Risk Assessment Documentation**

* **Description:** Evidence of conducted risk assessments that identified potential risks of unauthorized access and mitigation strategies implemented to address them.
* **Examples of Evidence:**
  + **Risk Assessment Reports:** Reports evaluating security risks specific to software communication systems and identifying mitigation measures aligned with NASA-STD-1006.
  + **Mitigation Plans:** Plans describing implemented strategies for mitigating risks of unauthorized access (e.g., access logging, encryption, IDS deployment).
  + **Residual Risk Analysis:** Documentation showing analysis of any remaining risks post-implementation of protections and concluding they are within acceptable limits.

---

### **6. Security Policy and Procedures**

* **Description:** Evidence of established policies and procedures governing protections against unauthorized access, as required by NASA-STD-1006.
* **Examples of Evidence:**
  + **Software Security Policy:** A project-approved security policy outlining requirements for protecting software communication systems from unauthorized access.
  + **Access Control Procedures:** Procedures defining how user access to communication systems is granted, revoked, or monitored across the lifecycle of the project.
  + **Incident Response Plan (IRP):** Predefined response plan for security breaches and unauthorized access attempts to communication systems.
  + **Data Protection Guidelines:** Procedures illustrating how software communication data (e.g., telemetry, commands) is secured during transmission and at rest.

---

### **7. Logging and Monitoring Records**

* **Description:** Evidence of logging and monitoring systems implemented to identify and respond to unauthorized access attempts.
* **Examples of Evidence:**
  + **Intrusion Detection System (IDS) Logs:** Logs showing detection and alerting of unauthorized or suspicious attempts to access communication systems.
  + **Access Logs:** Logs tracking all authorized and unauthorized access attempts to communication systems.
  + **Security Monitoring Logs:** Records from security monitoring tools (e.g., SIEM systems) confirming active surveillance of communication software activities.
  + **Audit Logs:** Logs of performed audits and reviews for access control and communication security systems.

---

### **8. Software Configuration Management Evidence**

* **Description:** Evidence that software protections were managed and maintained under configuration control to ensure proper implementation and future traceability.
* **Examples of Evidence:**
  + **Configuration Management Plan (CMP):** Plan outlining version tracking of security patches and access control updates for communication systems.
  + **Patch Management Records:** Documentation of security patches applied to software systems with communication capabilities.
  + **Change Logs:** Logs tracking updates to security protections for communication systems.
  + **Baseline Control Records:** Evidence confirming that protection mechanisms for communications systems are part of the baseline and approved configurations.

---

### **9. Third-Party or Independent Assessments**

* **Description:** Records of third-party or independent assessments verifying the effectiveness and compliance of protection mechanisms for software communication systems as per NASA-STD-1006.
* **Examples of Evidence:**
  + **Independent Security Audits:** Reports from third-party auditors or organizations evaluating implemented protections against unauthorized access.
  + **IV&V Security Reports:** Results of Independent Verification and Validation (IV&V) activities assessing adherence to NASA-STD-1006.
  + **Accreditation Reports:** Documentation from accreditation bodies ensuring compliance with required space system protection standards.

---

### **10. Training and Awareness Documentation**

* **Description:** Evidence that relevant personnel are trained on protecting software communication systems against unauthorized access.
* **Examples of Evidence:**
  + **Training Records:** Records of completed training sessions for development teams and users on security mechanisms for software communication systems.
  + **Security Awareness Documentation:** Materials distributed to increase awareness of unauthorized access risks and mitigation strategies related to communication systems.
  + **Training Assessment Results:** Evidence of assessments or evaluations of team members' understanding of these protections.

---

### **Summary Table of Objective Evidence for Requirement 3.11.4**

| **Category** | **Examples of Objective Evidence** |
| --- | --- |
| **Design Documentation** | System Protection Plan, Architecture Diagrams, Threat Assessment Reports, Design Requirements Documentation. |
| **Protection Implementation Records** | Access Control Logs, Encryption Reports, Secure Protocol Documentation, Firewall Configurations. |
| **Compliance with NASA-STD-1006** | Mapping Matrix, Compliance Review Report, Vulnerability Assessment Results. |
| **Test and Validation Evidence** | Penetration Test Results, Security System Test Reports, Functional Testing, Threat Scenarios Testing. |
| **Risk Assessment Documentation** | Risk Assessment Reports, Mitigation Plans, Residual Risk Analysis. |
| **Security Policies and Procedures** | Security Policy, Access Control Procedures, Incident Response Plan, Data Protection Guidelines. |
| **Logging and Monitoring Records** | IDS Logs, Access Logs, Audit Logs, Security Monitoring Records. |
| **Configuration Management Records** | Configuration Management Plan, Patch Management Records, Change Logs, Baseline Control Records. |
| **Third-Party Assessments** | Independent Security Audit, IV&V Security Reports, Accreditation Reports. |
| **Training and Awareness Evidence** | Training Records, Security Awareness Documentation, Training Assessment Results. |

---

### **Conclusion**

Objective evidence for compliance with Requirement 3.11.4 must demonstrate that protections against unauthorized access were designed, implemented, tested, monitored, and maintained, aligning with the guidelines of NASA-STD-1006. This ensures communication systems are safeguarded against vulnerabilities and consistently supported throughout the software lifecycle for secure operations in mission-critical environments.
