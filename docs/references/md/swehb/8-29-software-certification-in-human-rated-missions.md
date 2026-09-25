# 8.29 - Software Certification in Human-Rated Missions

> NASA Software Engineering Handbook (SWEHB Ver D), page id 207290635. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/207290635/8.29+-+Software+Certification+in+Human-Rated+Missions

8.29 - Software Certification in Human-Rated Missions

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/207290635/8.29+-+Software+Certification+in+Human-Rated+Missions#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=207290635)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=207290635&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Compliance Data Needs](#tabs-2)
* [3. Safety Case](#tabs-3)
* [4. Resources](#tabs-4)

# 1. Introduction

This checklist provides comprehensive data and evidence required to certify software for human-rated missions.It ensures compliance with applicable safety standards, regulatory requirements (NASA NPR 7150.2D [083](#_tabs-<p>4</p>) , SSP 50038 [014](#_tabs-<p>4</p>)  , FAA 450.141 Computing systems, NASA-STD-8739.8B [278](#_tabs-<p>4</p>)), mission-critical functionality, and stakeholder acceptance of residual risks, demonstrating that the software is safe, reliable, and mission-ready for crewed spaceflight operations.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-082 - Software Certification in Human-Rated Missions Checklist**

# 2. Key Software Compliance Data Needs

The checklist demands evidence across **12 major domains**.  
Below is a consolidated list of SWEHB artifacts (requirements, design, test, hazard, CM, etc.) that you must supply to satisfy the PAT‑082 checklist.

Each section below cites the corresponding checklist content.

# 1. Requirements & Traceability Evidence

You must provide the following SWEHB artifacts:

• **Software Requirements Specification (SRS)** – system-level, parent, high‑level, low‑level, and safety‑critical requirements  
• **Safety Requirements** (fault tolerance, safe states, redundancy, MWF/MNWF)  
• **Assumptions and safety constraints list**  
• **Requirements Traceability Matrix (RTM)** with full bi-directional trace:  
Hazards ↔ System Req ↔ Software Req ↔ Design ↔ Code ↔ Test ↔ Defects  
• **Hazard ↔ Requirement trace evidence**  
• **Prerequisite command checks requirements**

SWEHB Artifact Mapping:  
– SWE‑050 (Requirements Development)  
– SWE‑055 (Bidirectional Traceability)  
– SWE‑073 (Safety Requirements)  
– SWE‑079 (Hazard Traceability)

# 2. Software Architecture & Design Data

You must provide:

• **Software Architecture Document** (modules, partitions, redundancy, failure containment)  
• **Software Design Specification (SDS)**  
• **Safety‑critical design documentation** (initialization safe states, transitions, state machines)  
• **Interface Control Documents (ICDs)** including:  
– data types, sizes, units, coordinate systems, endianness  
– limits, stale data behavior  
– error value definitions  
• **Data Dictionary**  
• **Command validation design documents**  
• **Fault tolerance architecture and implementation evidence**  
• **Timing diagrams, state-flow models, block diagrams**  
• **Independence of redundant path documentation**  
• **Radiation/single‑event effects mitigation documentation**

SWEHB Mapping:  
– SWE‑057 (Architecture Description)  
– SWE‑061 (Design Documentation)  
– SWE‑086 (Interface Documentation)  
– SWE‑134 (Fault Tolerance Design)  
– SWE‑135 (Redundancy Independence)

# 3. Hazard Analysis and Safety Evidence

You must provide:

• **Hazard Analysis Report (HAR)**  
• **Software Hazard Reports (SHRs)**  
• **Time‑to‑Effect (TTE) analyses**  
• **Mitigation control documentation** (automation, safing, crew override)  
• **FMEA and FTA documentation**  
• **Linkage of hazard controls into software safety requirements**

SWEHB Mapping:  
– SWE‑201/202 (Safety Analyses)  
– SWE‑205 (Hazard Reports)  
– SWE‑206 (FTA/FMEA)

# 4. V&V Test Evidence

Required SWEHB artifacts:

• **Test Plans** (unit, integration, system, end‑to‑end, acceptance)  
• **Test Procedures**  
• **Test Results & Logs** covering:  
– nominal and off‑nominal scenarios  
– safety‑critical functions (abort, inhibit, crew override)  
– reused components (COTS/GOTS/MOTS/OSS)  
– interface testing  
– environmental and timing behaviors  
• **Coverage Analysis Reports**:  
– Statement coverage  
– Decision coverage  
– MC/DC (mandatory for safety‑critical SW)  
• **Static analysis results**  
• **Fault injection test reports**  
• **Integrity check results (CRC, checksum)**  
• **Worst‑case timing analysis**

SWEHB Mapping:  
– SWE‑068/069/070 (Test Planning/Procedures/Results)  
– SWE‑094 (Coverage Analysis)  
– SWE‑187 (Static Analysis)  
– SWE‑189 (Fault Injection)  
– SWE‑190 (Software Timing Verification)

# 5. Configuration Management Evidence

You must provide:

• **Configuration management plan**  
• **Baseline documentation** (release notes, identified flight builds, hashes)  
• **Version Description Document (VDD)**  
• **Configuration audit records**  
• **Change request logs**  
• **Open problem report list**  
• **Checksum comparison results**

SWEHB Mapping:  
– SWE‑079, SWE‑085 (Configuration Management)  
– SWE‑100 (Problem Reporting)  
– SWE‑077 (VDD)

# 6. Cybersecurity & Security Validation

Artifacts required:

• **Security validation reports**  
• **Threat assessment and mitigations**  
• **Penetration testing documentation**  
• **Vulnerability scans and mitigation closure**  
• **Secure coding compliance results**  
• **Static analysis from security tools**

SWEHB Mapping:  
– SWE‑156 (Cybersecurity)  
– SWE‑159 (Secure Coding Practices)

# 7. Defect Management & Residual Risk Evidence

You must provide:

• **Defect report lists** (open/closed categorized by severity)  
• **Defect closure documentation**  
• **Residual risk acceptance forms** signed by stakeholders  
• **TBR/TBD/FWD lists** with disposition  
• **Anomaly logs & resolution data**

SWEHB Mapping:  
– SWE‑100 (Defect Tracking)  
– SWE‑204 (Risk Acceptance Documentation)

# 8. Performance Metrics & Resource Utilization

Artifacts:

• **Latency/timing verification**  
• **CPU/memory utilization reports** (nominal & worst‑case; <80% CPU margin requirement)  
• **Throughput analysis**  
• **Failure detection & recovery documentation** (watchdog, upset recovery)

SWEHB Mapping:  
– SWE‑190 (Worst‑Case Execution Time)  
– SWE‑191 (Resource Margin Verification)

---

# 9. Process Compliance & Team Qualification

Required:

• **Training records** (safety-critical SW, process, standards)  
• **Process compliance evidence** (adherence to NPR 7150.2, 8739.8, coding standards)  
• **Software process audit results**  
• **Operator action analysis (crew procedure timing vs TTE)**

SWEHB Mapping:  
– SWE‑002 (Software Engineering Training)  
– SWE‑027 (Process Compliance Evidence)

# 10. Certification Packages & Regulatory Artifacts

Artifacts include:

• **Software certification package**  
• **Trace matrices** (requirements, hazard, test, defect)  
• **Regulatory compliance statements (FAA, NASA)**  
• **IV&V Certification Reports**  
• **Manual safing data**  
• **Override function validation evidence**  
• **Waivers/deviation packages**

SWEHB Mapping:  
– SWE‑032 (Certification Data Package)  
– SWE‑214 (IV&V Final Report)

# 11. Flight Readiness Review Evidence

Artifacts:

• **Flight-ready VDD**  
• **Final software test summary**  
• **FRR entrance/exit criteria evidence**  
• **Crew user manuals and operational procedures**  
• **Stakeholder risk acceptance forms**

SWEHB Mapping:  
– SWE‑171 (FRR Certification Evidence)

# 12. Structural Quality & Maintainability

Artifacts:

• **Cyclomatic complexity reports**  
• **Maintainability analysis**  
• **Fault‑tolerance validation evidence**  
• **Code quality and standards‑compliance reports**  
• **Architecture quality assessments**

SWEHB Mapping:  
– SWE‑187 (Static Analysis)  
– SWE‑053 (Coding Standards Compliance)

#### **2.1 Table of Key Software Compliance Data Needs**

|  |  |
| --- | --- |
| **Requirements** | * Access to the software requirements or software user stories, software acceptance criteria, software use cases, software functional specifications, software behaviors, software feature descriptions, or software tickets. * Access to the System/Software requirements traceability data * Access to the hazard control software requirements traceability data * Explanation on software safety constraints and assumptions * Access to the software requirements analysis results |
| **Design** | * Access to the software design * Explanation on software fault containment and management approach * Access to the software design analysis results * Access to the Interface Control Documents (ICDs) for software interfaces * Access to the data dictionary data * Data demonstrating prerequisite checks for all hazardous commands * Explanation on how the software design and requirements meet the safety critical requirements * Explanation on how the safety-critical code is modifiable * Demonstrate that the applicable human factors design principles are in place in the software |
| **Development** | * Access to the software operational plans or user’s manual * Explanation of the Fault Tolerance approach used in the design * Access to the source code * Approval data for all AI uses in flight software before deployment. * Demonstrate that the displayed confidence levels are correct for all critical AI decisions and predictions. * Demonstrate that the AI systems used in critical space flight software are managed with transparency to maintain safety, reliability, and accountability. * Access to the software defect reports (open/closed with severity), anomaly logs, residual risk acceptance with stakeholder sign-off * Access to all tailoring/waiver/deviation and TBR/TBD/FWD closure records. * Evidence that the approved software processes were followed during all software development activities * Evidence of closer of peer reviews/inspection findings for requirements, architecture/design, code and test artifacts review * Evidence of qualification and pedigree of reused/third‑party software * Provide an understanding of the certifications process for the software models & simulations used to qualify flight software. * Data showing the Worst‑Case Execution Time (WCET), timing analysis, and scheduling evidence, including partitioning and multicore interference analysis where relevant. |
| **Verification & Validation** | * Access to the software test results * Access to the MC/DC coverage data for safety-critical components * Access to the static and dynamic analysis testing approach and results * Demonstrate the fault injection resilience under worst-case conditions * Demonstrate how the software handles spurious signals and invalid inputs * Provide an understanding of the certifications process for the software test environments used to qualify flight software. * Provide results of a cyclomatic complexity analyses * Provide a list of identified software issues, anomalies, and defects, with clear and traceable justifications for acceptance of any unresolved items. * Provide data showing the operational test results and data confirming system resource margins under nominal and worst-case scenarios, including CPU/memory/throughput margins data * Access to the IV&V reports and findings and an understanding of the IV&V scope |
| **Hazard Analysis** | * Access to the software related hazard analysis reports, fault tree analysis, and FMEA addressing all software hazards and mitigation strategies. * Demonstrate that all AI systems generate warnings and recommendations for anomalies that could lead to hazards * Demonstrate the operator Action Validation * Explanation of the software safing Procedures |
| **Configuration Management** | * Access to the software documentation, * Access to the software change Logs * Access to the software version control, baseline definitions, and audit records for all changes. |
| **Operational Procedures** | * Explanation of the software control Sequences, * Explanation of any software manual safing data and processes |
| **Cybersecurity** | * Demonstrate that the software has encryption, authentication, meets secure coding practices, and has access control * Access to the results showing penetration testing and vulnerability analysis |

#### **2.2 Key Software Compliance Data Needs Rationale**

**Section: Requirements**

| **Item** | **Rationale** |
| --- | --- |
| Access to the software requirements or software user stories, software acceptance criteria, software use cases, software functional specifications, software behaviors, software feature descriptions, or software tickets | Demonstrated the software capability definition and software testing criteria. SWEHB emphasizes complete, correct, validated SRS content as the foundation for safe, verifiable software; early clarity prevents costly downstream defects and safety gaps. |
| Access to the System/Software requirements traceability data | Bi‑directional traceability is required to prove every design, code, and test artifact maps to a validated system need—preventing orphan functionality and ensuring hazards are controlled. |
| Access to the hazard control software requirements traceability data | Hazard controls must trace explicitly from hazard analysis to software requirements and back to verification evidence to avoid missing or partial mitigations. |
| Explanation on software safety constraints and assumptions | Documented constraints and assumptions prevent hidden coupling and incorrect operating expectations—frequent root causes in lessons learned for hazardous behavior. |
| Access to the software requirements analysis results | Structured requirements analysis (ambiguity checks, safety impacts, HSI considerations) provides objective evidence that requirements are testable, feasible, and complete before design. |

**Section: Design**

| **Item** | **Rationale** |
| --- | --- |
| Access to the software design | Architecture/design descriptions enable validation of partitioning, redundancy, timing, and safety mechanisms; undocumented design is a recurring integration‑failure source in SWEHB. |
| Explanation on software fault containment and management approach | A clear FDIR strategy limits fault propagation, preserves redundancy, and supports safe recovery for safety‑critical functions. |
| Access to the software design analysis results | Design reviews/analyses expose interface risks, safety gaps, and performance limits early, reducing costly rework during integration/test. |
| Access to the Interface Control Documents (ICDs) for software interfaces | ICDs prevent interface mismatch failures—one of the most common categories of integration defects called out in SWEHB checklists. |
| Access to the data dictionary data | Data dictionaries provide authoritative definitions and units, preventing misinterpretation and unit conversion defects across teams/tools. (SWEHB practice captured in certification checklist.) |
| Data demonstrating prerequisite checks for all hazardous commands | Prerequisite checks are explicitly required for safety‑critical design to block unsafe command execution unless the system state is validated. |
| Explanation on how the design and requirements meet safety‑critical requirements | Explicit mapping from safety‑critical requirements to design elements verifies that every control is implemented and testable—closing common gaps seen in hazard mitigations. |
| Explanation on how the safety‑critical code is modifiable | Modular, isolated safety‑critical code reduces regression risk during updates and enables focused assurance/maintenance. (Emphasized in SWEHB certification guidance.) |
| Demonstrate applicable human‑factors design principles in the software | HSI evidence (clear displays, alerts, error tolerance) mitigates operator error and automation surprise—frequent contributors to unsafe states in lessons learned and SWEHB checklists. |

**Section: Development**

| **Item** | **Rationale** |
| --- | --- |
| Access to the software operational plans or user’s manual | Operational manuals drive correct crew/operator actions; unclear procedures have historically led to unsafe system states—documented guidance is essential. |
| Explanation of the Fault Tolerance approach used in the design | Development evidence must confirm the implemented redundancy, monitoring, and recovery match the approved design/FDIR strategy. |
| Access to the source code | Assurance/IV&V require code access to assess correctness, safety patterns, and compliance; “code is the design” for verification in SWEHB practice. |
| Approval data for all AI uses in flight software before deployment | The human‑rated certification checklist in SWEHB requires governance of novel tech; AI decisions must be bounded, transparent, and verified before mission use. |
| Demonstrate correct AI confidence levels for critical decisions/predictions | Accurate confidence cues preserve appropriate human trust; misleading confidence can induce hazardous operator actions (SWEHB human‑rated checklist). |
| Demonstrate AI transparency/accountability in critical flight software | Transparency and auditable behavior enable assurance teams to verify AI outputs, edge cases, and failure handling consistent with safety requirements (SWEHB PAT guidance). |
| Access to defect reports, anomaly logs, and residual risk acceptance | Defect trends and residual‑risk approvals provide readiness evidence and ensure risks are visible and accepted prior to flight (SWEHB PAT‑082). |
| Access to tailoring/waiver/deviation and TBR/TBD/FWD closures | Tailoring/waiver records show what SWEHB/NPR expectations were modified and how verification gaps were closed—preventing undocumented process escapes. |
| Evidence that approved processes were followed during development | SWEHB lessons emphasize objective evidence (reviews, audits, checklists) to confirm disciplined execution—avoiding “process‑on‑paper” failures. |
| Evidence of closure of peer review/inspection findings | Peer reviews are high‑value defect prevention in SWEHB; closure evidence ensures findings are resolved, not deferred into flight risk. |
| Evidence of qualification/pedigree of reused/third‑party software | SWEHB certification content calls for assessing provenance, constraints, known defects, and verification completeness to control integration risk. |
| Certification process for models & simulations used to qualify flight software | SWEHB requires validated/accredited models/sims for qualification; unvalidated M&S can mask defects and create false confidence. |
| WCET/timing/scheduling evidence (partitioning & multicore interference) | Deterministic timing & schedulability evidence prevent deadline misses and resource starvation—common latent hazards noted in SWEHB certification checklists. |

**Section: Verification & Validation**

| **Item** | **Rationale** |
| --- | --- |
| Access to the software test results | Test evidence must trace to requirements and hazards to prove correctness and safety under nominal/off‑nominal conditions (SWEHB). |
| Access to MC/DC coverage data for safety‑critical components | For safety‑critical logic, MC/DC helps reveal untested decision paths—improving confidence that critical branches cannot hide defects (SWEHB practice). |
| Static and dynamic analysis approach/results | Static/dynamic analyses expose memory, concurrency, and API defects early, complementing functional tests with deeper correctness checks (SWEHB PAT‑082). |
| Fault‑injection resilience under worst‑case conditions | Fault‑injection validates robustness of error handling and safe‑state transitions under realistic fault scenarios (SWEHB). |
| Handling spurious signals and invalid inputs | Defensive input handling and integrity checks are SWEHB safety‑critical design requirements to prevent unsafe behavior from noise or corruption. |
| Certification of software test environments | Accredited test environments assure fidelity so test results represent flight behavior—preventing false positives/negatives (SWEHB PAT‑082). |
| Cyclomatic complexity analyses results | Complexity correlates with defect likelihood and test effort; tracking supports risk‑based testing and maintainability (SWEHB checklist). |
| Issues/anomalies/defects list with unresolved‑item justifications | Residual issues require documented operational mitigations and rationale to ensure informed risk acceptance before flight (SWEHB). |
| Operational test results & resource margins (CPU/memory/throughput) | Resource margin evidence demonstrates the system sustains mission loads without entering unsafe degraded states (SWEHB). |
| Access to IV&V reports/findings & IV&V scope understanding | Independent assessment adds rigor and identifies latent risks; scope clarity ensures findings are dispositioned (SWEHB/SMA IV&V discussion). |

**Section: Hazard Analysis**

| **Item** | **Rationale** |
| --- | --- |
| Hazard analysis, FTA, FMEA | Hazard analyses formally identify software causes/contributions and define controls; they are the backbone for safety‑critical requirements and tests (SWEHB). |
| AI warnings & recommendations for anomalies | AI components must surface anomaly cues and recommended mitigations in time for operator/software safing to prevent hazard escalation (SWEHB PAT‑082 scope). |
| Operator Action Validation | Operator action validation ensures human‑software interactions are unambiguous and error‑tolerant—reducing unsafe actions under stress (SWEHB checklist). |
| Software safing procedures | Safing procedures must reliably place the system into known safe states on detection of hazardous conditions—captured in SWEHB safety‑critical design items. |

**Section: Configuration Management**

| **Item** | **Rationale** |
| --- | --- |
| Access to the software documentation | CM control of documentation prevents divergence between what is built, tested, and flown—frequent contributors to integration defects (SWEHB PAT‑082). |
| Access to the software change logs | Change history enables traceability and impact assessment for safety‑critical components/interfaces (SWEHB). |
| Version control, baseline definitions, audit records | Version/baseline and audits ensure the exact tested configuration proceeds to flight and prevent unauthorized changes (SWEHB checklist). |

**Section: Operational Procedures**

| **Item** | **Rationale** |
| --- | --- |
| Explanation of the software control sequences | Clear control sequences reduce operator confusion and ensure predictable behavior during time‑critical operations (SWEHB). |
| Explanation of any software manual safing data/processes | Manual safing provides a human‑initiated fallback when automation fails; procedures must be explicit, tested, and accessible (SWEHB). |

**Section: Cybersecurity**

| **Item** | **Rationale** |
| --- | --- |
| Encryption, authentication, secure coding, access control | Security controls protect command authority, data integrity, and system availability—security weaknesses can become safety hazards (SWEHB). |
| Penetration testing and vulnerability analysis results | Pen/vuln testing finds exploitable weaknesses before flight, supporting remediation and risk reduction (SWEHB checklist practice). |

# 3. Example Potential Safety Case for Human-Rated Software Certification

This safety case demonstrates that the software used in this human-rated mission adheres to rigorous safety, quality, and regulatory standards. Based on the evidence provided, the software is flight-ready and capable of supporting critical mission operations while ensuring the safety of the crew and spacecraft under both nominal and adverse conditions.

**1. Requirements and Traceability**

* **Argument:** The software requirements are clearly defined, traceable, and aligned with safety-critical mission needs.
* **Evidence:**
  + Comprehensive Software Requirements Specification (SRS) covering high-level mission-critical systems (e.g., navigation, propulsion, anomaly detection, life support, and abort operations).
  + Verified safety requirements (fault tolerance, redundancy, and safe initialization/termination).
  + Acceptable quality of detailed low-level safety-critical requirements, including specifics like algorithm designs and timing constraints.
  + A completed and validated Requirements Traceability Matrix (RTM) showing bi-directional traceability from requirements through design, code, and test results.
  + Reviewed system-level safety analyses to document "Must Work" (MWF) and "Must Not Work" (MNWF) requirements, prerequisite checks for hazardous commands, and mitigation strategies.

**2. Software Design and Architecture**

* **Argument:** The software architecture is resilient, modular, and designed for fault tolerance and safety-critical operations.
* **Evidence:**

+ Architecture documentation detailing modular fault isolation, redundancy, and resiliency mechanisms.
+ Block diagrams illustrating fault containment, fail-safe control paths, and separation of critical functions.
+ Documentation and analysis of safety-critical subsystems (e.g., propulsion, crew displays, navigation) with clearly defined responsibilities.
+ Verified Interface Control Documents (ICDs), ensuring compatibility between internal software, hardware systems, and external interactions.
+ Safety validation evidence for safeguards like fault containment, error detection, operator validation, integrity checks, and anomaly recovery processes.
+ Independent redundant system designs ensuring physical and logical separation to mitigate single points of failure.
+ Validation of fault-tolerant mechanisms, including cosmic radiation protection in CPU designs.

**3. Hazard Analysis and Safety Evidence**

* **Argument:** All hazards associated with software functionality are identified, analyzed, and mitigated to acceptable levels of risk.
* **Evidence:**

+ A complete Hazard Analysis Report (HAR) identifying software-driving hazards and the mitigation strategies in place.
+ Fault Tree Analysis (FTA) and Failure Mode and Effects Analysis (FMEA) showing robust fault prevention and recovery mechanisms or a completed System Theoretic Process Analysis (STPA) showing robust fault prevention and recovery mechanisms.
+ Time-to-effect (TTE) analyses ensuring hazardous conditions can be addressed by safing systems within operational thresholds.
+ Residual risk documentation showing resolution or acceptance of remaining risks by stakeholders.

**4. Verification and Validation (V&V) Evidence**

* **Argument:** Rigorous testing, validation, and coverage analyses demonstrate software compliance with safety-critical requirements.
* **Evidence:**
  + 100% Statement Coverage.
  + 100% Decision Coverage.
  + 100% Modified Condition/Decision Coverage (MC/DC) for safety-critical components.

+ Unit testing, system integration testing, end-to-end validation, and operational flight simulations confirming that expected functional performance aligns with safety goals.
+ Validation of reused components (COTS, GOTS, OSS, MOTS) to ensure compatibility and reliable integration into human-rated environments.
+ Coverage analysis demonstrating:
+ Static analysis reports showing compliance with coding standards and identification/remediation of software defects.
+ Fault injection testing results validating responses to corrupted data, anomalies during power disruptions, and memory errors.
+ Worst-case response timing analysis confirming safing systems meet TTE requirements under degraded conditions.

**5. Configuration Management and Change Tracking**

* **Argument:** Configuration management processes ensure version control and traceability for all software changes.
* **Evidence:**
  + Documentation showing version-controlled baselines for flight-ready software and data loads, including configuration hashes and release notes.
  + Audit records verifying modifications, regression testing, impact analyses, and stakeholder approvals

**6. Cybersecurity and Security Validation**

* **Argument:** The software architecture incorporates robust cybersecurity measures to mitigate threats in operation environments.
* **Evidence:**
  + Security validation reports demonstrating encryption protocols, authentication mechanisms, access control, and secure coding practices.
  + Penetration testing results validating resilience against cyberattacks and unauthorized system access during pre-launch and flight.
  + Vulnerability analysis reports confirming detection, resolution, and closure of security-related risks.

**7. Defect Management and Residual Risks**

* **Argument:** All software defects have been resolved or mitigated to acceptable levels of residual risk.
* **Evidence:**

+ Defect reports showing all open and closed defects categorized by severity and justifications for acceptance of residual risks.
+ Logs documenting defect resolutions and testing data validating the outcomes of mitigation measures.
+ Residual risk acceptance documentation signed off by stakeholders, with sufficient evidence showing safe system behavior despite unresolved minor risks.

**8. Resource Utilization and Performance Metrics**

* **Argument:** The software demonstrates sufficient resource margins and acceptable performance under normal and worst-case conditions.
* **Evidence:**

+ Validation test results confirming acceptable command execution timing (e.g., abort triggers).
+ Operating analysis showing CPU utilization below 80% even under maximum load conditions.
+ Methods for anomaly detection and recovery to safe states outlined and validated.

**9. Team Training and Software Process Compliance**

* **Argument:** Development teams adhere to validated processes and are properly trained in safety-critical mission standards.
* **Evidence:**
  + Records of team training addressing human-rated software workflows, defect management, and compliance with coding guidelines.
  + Process compliance reports documenting adherence to validated development processes.
  + Operator manuals ensuring deliberate, independent actions are necessary to execute critical safety commands

**10. Certification and Regulatory Compliance**

* **Argument:** The software complies with all applicable standards and safety regulations for human-rated missions.
* **Evidence:**

+ Certification artifacts for compliance with standards like NASA NPR 7150.2D [083](#_tabs-<p>4</p>) ,   
  NASA SSP 50038 [014](#_tabs-<p>4</p>), FAA requirements, and NASA-STD-8739.8B [278](#_tabs-<p>4</p>) .
+ IV&V certification reports confirming operational maturity and compliance with safety standards by independent entities.
+ Regulatory compliance statements from authorities certifying readiness for human-rated missions.
+ Validation of software updates (patched or upgraded) ensuring continued compliance with safety requirements.

**11. Flight Readiness Review (FRR) Certification**

* **Argument:** The software is flight-ready and capable of safely supporting mission operations.
* **Evidence:**

+ Software Version Description Document (VDD) completion demonstrating proper documentation of the deployed software.
+ Final test results confirming readiness during flight operations in all mission environments.
+ FRR exit criteria signed off by stakeholders, certifying acceptance or resolution of all known risks, hazards, defects, and anomalies.

**12. Flight Software Structural Quality**

* **Argument:** The software architecture and implementation are structurally sound and meet all quality standards for safety-critical applications.
* **Evidence:**

+ Cyclomatic complexity analysis showing all safety-critical components meet thresholds (≤ 15).
+ Documentation verifying fault-tolerant mechanisms for error handling, failure recovery, and system operation under degraded conditions.
+ Maintainability analysis supporting modular coding practices for long-term sustainability and easy updates.
+ Code quality reports validating compliance with architecture, standards, security, and testability requirements.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-014)

  [Computer-Based Control System Safety Requirements](https://swehb.nasa.gov/download/attachments/16450414/SSP%2050038-Rev%20C.docx?api=v2 "Click to open in new window")

  SSP 50038, Revision C, NASA International Space Station Program, 1995.
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 4.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 4.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [PAT-082 - Software Certification in Human-Rated Missions Checklist](/spaces/SITE/pages/207290645/PAT-082+-+Software+Certification+in+Human-Rated+Missions+Checklist) |

## 4.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only).

| SPAN Links |
| --- |
|  |

## 4.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
|  |
