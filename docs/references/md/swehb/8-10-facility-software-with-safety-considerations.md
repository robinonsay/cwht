# 8.10 - Facility Software with Safety Considerations

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695728. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations

8.10 - Facility Software with Safety Considerations

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695728)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695728&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Facility Life Cycle](#tabs-2)
* [3. Maturity Schedules](#tabs-3)
* [4. SW Engineering Responsibilities](#tabs-4)
* [5. SA Responsibilities](#tabs-5)
* [6. Safety Critical SWE Tasks](#tabs-6)
* [7. Entry/Exit Criteria](#tabs-7)
* [8. Resources](#tabs-8)

# 1. Introduction

Facility software safety exists to ensure the safe and continuous operation of software associated with ground-based facilities. Facility software may be comprised of embedded software systems, user applications/interfaces, programmable logic devices (PLDs), etc. Essentially, it is all the types of software required to make the hardware operate as expected.

**NPR 8820.2** [692](#_tabs-<p>8</p>) provides the minimum requirements for planning, approving, and acquiring all NASA Facility Projects. The role and expectations of the Safety and Mission Assurance (SMA) organization throughout the life cycle of these Facility Projects are established in **NPR 8715.1** [693](#_tabs-<p>8</p>). Since some Facility projects include the construction or modification of systems, the project needs to manage the systems in accordance with **NPR 7120.5** [082](#_tabs-<p>8</p>) or **NPR 7120.8** [269](#_tabs-<p>8</p>)  (depending on the type of system being developed.)

This Facility Software topic focuses on how software, specifically safety critical software, is integrated into Facility Projects and Software Assurance’s role in these projects. Whether the software is new or modified, Software Engineering and Software Assurance will continue to follow **NPR 7150.2** [083](#_tabs-<p>8</p>) and **NASA-STD-8739.8** [278](#_tabs-<p>8</p>) as well as the guidance in this Handbook for these projects as well as those levied by **NPR 8820.2** and **NPR 7120.5/NPR 7120.8**. The information in this topic attempts to connect the **NPR 7150.2** requirements to these higher-level requirements.

The information is divided into several tabs as follows:

* Tab 1 – Introduction
* Tab 2 – Facility Life Cycle and milestones with a mapping to Software/Systems Engineering milestones
* Tab 3 – Software Engineering and Software Assurance work product Maturity Schedules for Facility Milestones
* Tab 4 – SW Engineering Responsibilities during Facility Projects
* Tab 5 – SA and Software Safety Responsibilities during Facility Projects
* Tab 6 – SA and Software Safety Tasking for Safety Critical SWEs
* Tab 7 – Entry/Exit Criteria for Facility Milestones
* Tab 8 – Resources

## 1.1    Facility Safety Criticality Indicators

If the Hazard Analysis isn’t available early in the project, there are some initial factors that may give an indication that center facilities and infrastructure may need to be designated as critical, thus requiring SMA involvement. These indicators include:

1. Whether the facility capability is necessary to support development, test, or operation of flight systems and/omissions such that loss of their function would have significant impact on programs, projects, or other development efforts,
2. Whether the facility involves human test subjects,
3. Whether the facility implements high energy capabilities whose failure would be sufficient to cause injury, death, or significant damage.

If the facility meets any of these factors and it has software that commands, controls, or monitors capabilities, then most likely safety critical software is involved invoking the requirements in **NPR 7150.2** and **NASA-STD-8739.8**. Ultimately, the Hazard Analysis will identify any software controls or mitigations that are safety critical requiring the implementation of the **NPR 7150.2** and **NASA-STD-8739.8** safety requirements.

To put this into context, some examples of a facility with safety critical software are Laser facilities, Wind Tunnel facilities, mission operations centers, and the [Vertical Motion Simulator (VMS) at NASA Ames](https://www.nasa.gov/ames/aviationsystems/vms/).

## 1.2. Best Practices

1. **Hazard Verification Tracking Log** - All hazards controlled or mitigated by software must be tracked to closure. They must be traced from the Preliminary Hazard Analysis/Hazard Analysis (PHA/HA) to requirements to verification and validation to ensure all software controls and mitigations are verified or validated.  It is best practice to use a Hazard Verification Tracking Log (HVTL) to perform this tracking.
2. **Software Requirements Writing** - Software requirements must be approved by all project stakeholders (e.g., project manager, operators, test lead).  Projects may not use Symbolic Logic Diagrams (SLDs) as a substitute for requirements to save money and time.  While technical project members may be able to read and interpret SLDs, non-technical members like operators are not able to read and interpret then.  Thus, software requirements should be written using English phrasing or natural language to ensure all project stakeholders understand the requirements.
3. **PHA/HA Author Involvement in Change Management Process** - Software changes must be assessed against hazard controls and mitigations.  Include the PHA/HA author in the software change management process when evaluating the proposed modifications.  The PHA/HA author should assess all software changes impacts to hazard software controls and mitigations.
4. **Perform a Software Safety Analysis** - Correct identification and handling of software failures is essential for safety critical software.  A Software Safety Analysis helps identify all possible software failures commonly used. Therefore, it is recommended that a Software Safety Analysis be performed. A Software Safety Analysis may include a Failure Modes and Effects Analysis (FMEA), Fault Tree Analysis (FTA), and/or Failure Modes, Effects, and Criticality Analysis (FMECA).

## 1.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 2. Facility Project Life Cycle

The Facility Project life cycle comprises the project formulation phases (including planning and development), final design, implementation (including construction, commissioning, and activation), M&O, decommissioning, and disposal/demolition. Figure 1 below illustrates the full facility project life cycle with a mapping to the equivalent system and software engineering milestones.

Due to the timing of Construction of Facilities (CoF) program funding, some or all of the **NPR 7120.5** [082](#_tabs-<p>8</p>)/**NPR 7120.8** [269](#_tabs-<p>8</p>) life cycle milestones may not be funded until the start of Phase C. Software may receive limited funding to support the CoF milestones, but typically it won’t be enough to support the development of mature software work products.

By the end of Phase B (90% Design Review), the software engineering and software assurance should have:

1. Reviewed and analyzed the system Hazard Analysis to determine if there are any software-related hazards.
2. Determined the Software Classifications and Safety Criticality of the Computer Software Configuration Items (CSCIs).
3. Developed the Software Management/Development Plan and the Software Assurance Plan.

## 2.1   Facility Milestone Reviews Descriptions

Facility projects will be assigned a Chief SMA/Safety Officer (CSO) (a.k.a. Center Institutional Safety Discipline Lead) to monitor and ensure compliance with the Agency, Center, and regulatory policies and requirements (See **NPR 8715.1** [693](#_tabs-<p>8</p>)). Typically, the CSO will participate in and represent Software Assurance and Software Safety at the Facility Project milestone reviews. However, SA and Software Safety should plan to support or participate in any presentations given at these reviews. The Facility Project Manager (FPM) will establish which reviews will be held and document them in a project plan or schedule. “Depending on the size of the project, NASA will typically have between two and four weeks to review each package and return comments prior to the milestone review meeting.” [692](#_tabs-<p>8</p>)

The typical facility project milestones are:

* **Facilities Utilization Review Board (FURB)** – The FURB directs the utilization of real property at the Center and communicates that direction to all Center stakeholders and includes affected Capability Portfolio Managers (CPMs). The FURB approves which properties are to be submitted to the NASA HQ Facilities and Real Property Division (FRED). (See **NPR 8800.15F** [694](#_tabs-<p>8</p>))
* **Facility & Systems Requirements Review (FSRR)** – The FSRR evaluates whether the project functional and performance requirements are properly formulated and correlated with center and operating organization needs, goals, and objectives. Project requirements are baselined by the conclusion of the FSRR. The FSRR also assesses the credibility of the project’s estimated budget and schedule.
* **30-Percent Design Review** – The 30% Design Review for a center critical facility is the first design review that confirms the project requirements are validated. The review criteria demonstrates that the preliminary design meets all system requirements with acceptable risk and within the cost and schedule constraints and establishes the basis for proceeding with the detailed design.
* **60-Percent Design Review** – The 60% Design Review validates if the project as designed is achievable to construct within the NASA-specified budget. Preliminary/initial designs and completed analyses are deliverables for this milestone.
  + Note: The symbolic logic diagrams and ladder logic, if applicable, should be ready for review and included in the software architectural design documents.
* **90-Percent Design Review** – The 90% Design Review should complete the validation of the final design package of drawings, specifications, calculations and analysis, schedules, and commissioning plans. The period between 90-percent and 100-percent should be to address minor spelling corrections, small adjustments to drawings and specifications and for final coordination activities.
* **Independent Safety Reviews (ISR)** – Throughout the life cycle of a facility project, the FPM will request independent reviews from the Center Institutional Safety Discipline Leads. These reviews will include any proposed facility project configuration changes that have a potential to impact project fire protection, life safety, or health systems and equipment. Some of these reviews are:
  + **Integrated System Safety Review (ISSR)** – The ISSR assesses the overall safety of the facility and its planned operation, confirms the facility supports intended operational characteristics, ensures that hazard controls have been validated, and confirms that plans reflect a systematic approach to demonstrate the full operational capability. The ISSR is held before facility Integrated System Acceptance Test (ISAT) to ensure that appropriate safety measures are in place to support the test.
  + **Human Occupancy Review Board (HORB)** – This is one final review to attest that the facility is safe and ready for human occupancy. It typically occurs after ORR, but before going operational. SA will support this review but has no formal role on this board.
* **Operational Readiness Review (ORR)** – The final NASA review of a facility immediately prior to placement into its intended operation. For projects with software systems, the ORR examines the actual system characteristics and the procedures used in the system or product's operation and ensures that all system and support (flight and ground) hardware, software, personnel, and procedures are ready for operations and that user documentation accurately reflects the deployed state of the system. (**NPR 7120.5**)

Note: Institutional Safety Discipline Leads. They are Subject-Matter-Experts (SMEs) for the safety discipline. These individuals are assigned to ensure facilities, systems, and activities are safe and conform to Agency, Center, and regulatory policy and requirements. The roles and responsibilities for these individuals are specified in **NPR 8715.1, NASA Safety and Health Programs.**

## 2.2   System/Software Milestones

There are some system milestones that should be included in the list of Facility Project milestone reviews when software is involved regardless of criticality. Tailoring of the **NPR 7120.5** [082](#_tabs-<p>8</p>) and **NPR 7120.8** [269](#_tabs-<p>8</p>) milestone reviews for inclusion in the schedule is expected, but at a minimum, the following should be added:

* **Test Readiness Review (TRR)** – The TRR ensures that the test article (hardware/software), test facility, support personnel, and test procedures are ready for testing and data acquisition, reduction, and control. (See **NPR 7123.1** [041](#_tabs-<p>8</p>)) Multiple TRRs may be held to ensure the software, system, and facility are ready for the next testing phase. This is illustrated in the next section (see [Table 1](#tabs-3)).
* **Systems Integration Review (SIR)** – The SIR evaluates the readiness of the project to start flight system assembly, test, and launch operations. V&V Planning, integration plans, and test plans are reviewed. Test articles (hardware/software), test facilities, support personnel, and test procedures are ready for testing and data acquisition, reduction, and control. (**NPR 7120.5**) The SIR is typically held before the facility Integrated System Acceptance Test (ISAT) to ensure that appropriate safety measures are in place to support the test.

For safety critical software, the full set of system software life cycle milestone reviews are expected to be held unless the Technical Authority approves them being tailored out. At a minimum, these additional milestone reviews should be held:

* **Software/System Acceptance Review (SAR)** – The SAR verifies the completeness of the specific end item with respect to the expected maturity level and assesses compliance with stakeholder expectations. The SAR examines the system, its end items and documentation, and test data and analyses that support verification. It also ensures that the system has sufficient technical maturity to authorize its shipment to the designated operational facility or launch site. (**NPR 7120.5**)
* **Flight Readiness Review (FRR)** – If the facility software will be used for flight, a FRR must be held. The FRR examines tests, demonstrations, analyses, and audits that determine the system's readiness for a safe and successful flight/launch and subsequent flight operations. It also ensures that all flight and ground hardware, software, personnel, and procedures are operationally ready. (**NPR 7120.5**)

For descriptions of the other System/Software Engineering milestones, see Topic [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria).

## 2.3   Software Peer Reviews

Although not a milestone, some software peer reviews are quite important and need to be included in the project schedule. Besides the source code, there are several analysis products (i.e., static analysis, cyclomatic complexity) that need to be generated and discussed at the Code Review of safety critical software. Thus, the Code Review is included in the Maturity Schedules (See [Table 1 and Table 2](#tabs-3) in the Maturity Schedules tab).

# 3. Document Maturity Schedules

Click on [Download](/download/attachments/102695728/Table%201%20and%20Table%202.docx?version=1&modificationDate=1750897309000&api=v2) to obtain a usable copy of the tables on this page. 

## 3.1   Software Engineering Life Cycle Documentation Maturity Schedule

Table 1 summarizes the anticipated timetable for when the software life cycle documentation, specified by **NPR 7150.2D** [083](#_tabs-<p>8</p>), will be provided by engineering and the associated maturity level at the various Facility Project milestone reviews. Software engineering is not expected to produce any products for the Facilities Utilization Review Board (FURB), so it is not included in the table below. Table 1 represents the work products to be reviewed for a particular milestone and their maturity at the review’s exit (i.e., Exit / Success Criteria.)

The maturity schedule for all other system and software milestones may be found in Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews).

**Table 1: NPR 7150.2 Software Life Cycle Documentation Maturity Table for Facility Project Milestones**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Documentation** | **FSRR** | **30% Review** | **60% Review** | **90% Review** | **Code Review\*** | **TRR\*\*** | **SIR\*\* (w/ SVT TRR)** | **ISSR (w/** **ISAT TRR)** | **ORR** |
| Software Development Plan (SDP) | P | B | U | F |  |  |  |  |  |
| * + NPR 7150.2 Software Requirements Mapping Matrix | P | B | U | F |  |  |  |  |  |
| * + Software Schedule | P | U | B | U |  |  |  |  |  |
| * + Software Cost Estimate | P | U | B | U |  |  |  |  |  |
| * + Software Classification and Criticality Assessment | P | B | U | F |  |  |  |  |  |
| Software Configuration Management Plan (SCMP) | P | P | B | F |  |  |  |  |  |
| Software Verification and Validation Plan / Test Plans | P | B | U | U |  | U | U | U/F |  |
| * + Unit Software Test Plan |  |  |  |  |  | B |  |  |  |
| * + SVT Software Test Plan |  |  |  |  |  | P | B |  |  |
| * + Integrated Systems Acceptance Test (ISAT) Software Test Plan |  |  |  |  |  |  | P | B |  |
| Software Protection Plan | P | B | U | F |  |  |  |  |  |
| Unit Software Test Procedures |  |  |  | P |  | B |  |  |  |
| SVT Software Test Procedures |  |  |  |  |  | P | B |  | F |
| ISAT Software Test Procedures |  |  |  |  |  |  | P | B | F |
| Unit Software Test Reports |  |  |  |  |  |  | B/F |  |  |
| SVT Software Test Reports |  |  |  |  |  |  |  | B | F |
| ISAT Software Test Reports |  |  |  |  |  |  |  | P | B/F |
| Risk Management Plan | P | B | U | F |  |  |  |  |  |
| Software Requirements Specification (SRS) |  | P | B | U | U | U |  |  | F |
| Requirements on OTS Software |  | P | B | U |  |  |  |  |  |
| Bi-Directional Requirements Traceability |  |  |  |  |  |  |  |  |  |
| * + Higher-level requirements to the SRS requirements |  | P | B | U |  |  |  |  | F |
| * + SRS requirements to the system hazards |  | P | B | U |  | U | U | U | F |
| * + SRS requirements to the software design components |  | P | U | B |  |  |  |  | F |
| * + Software design components to the software code |  |  |  |  | P | B | U | U | F |
| * + SRS requirements to the software verification(s) |  |  |  | P |  | B | U | U | F |
| * + - SRS requirements to SVT test procedure |  |  |  |  |  |  | B |  |  |
| * + - SRS requirements to ISAT test procedure |  |  |  |  |  |  |  | B |  |
| * + SRS requirements to the software non-conformances | P | U | U | U |  | U | U | U | F |
| Software Data Dictionary (Control System I/O and Device Listing) |  | P | P | B |  | F |  |  |  |
| Software Design Description (Architectural Design) |  |  | B | U |  | F |  |  |  |
| Software Design Description (Detailed Design) |  |  | P | B |  | F |  |  |  |
| Interface Control Document |  |  | P | B |  | F |  |  |  |
| Coding Standards / Guidelines |  | B |  |  |  |  |  |  |  |
| Software Code |  | P | U | U | U | B | U | U | F |
| Software User's Manual |  |  |  |  |  |  |  |  | B |
| Records of Continuous Risk Management | P | U | U | U |  | U | U | U | U |
| Measurement Analysis Results (SW Metrics) |  | B | U | U |  | U | U | U | F |
| Operational Concepts (part of "Mission Operations Concept") | P | U | B | F |  |  |  |  |  |
| Acceptance Criteria and Conditions |  |  | P | B | U | U | U | U |  |
| Software Safety and Hazard Analysis | P | P | B | U |  | U | U | U | F |
| * + Software Safety Analysis (included in FMEA) | P | P | B | U | U | U | U | U/F |  |
| * + Analysis of Preliminary Hazard Analysis Reports and software controls and mitigations (FHA / Hazard Reports / Hazard Analysis Tracking Index) | P | B | U | U | U | U |  |  |  |
| * + List of all software safety-critical components identified | P | B | U | U | U | U | U | U | F |
| Version Description Document (VDD) |  |  |  | P | P | P | P | U | B/F |
| Software Cyclomatic Complexity Assessment and Analysis |  |  |  | P | P | B | U | U | F |
| Code Coverage Analysis |  |  |  | P | P | B | U | U | F |
| Static Analysis |  |  |  | P | P | B | U | U | F |
| Key: | P == Preliminary: Most content is there but has not been baselined yet. B == Baseline: Product reviewed with an action plan to complete. U == Updated: Updated as required. F == Final: Product is finalized and no additional modifications are expected. Signatures obtained, if applicable. \* == System Milestone to include in Facility Projects \*\* == Software Peer Review | | | | | | | | |

## 3.2   Software Assurance and Software Safety Work Product Maturity Schedule

Table 2 lists the major products with their sub-products and other details that Software Assurance and Software Safety typically develops during the software project life cycle. The development of these products will depend on the delivery of the associated software engineering products/documentation. If the engineering product is not delivered, the SA product/sub-product will not be generated.

Table 2 summarizes the anticipated timetable for developing the software assurance products. It provides the life cycle phase(s) where the product is typically developed and reviewed along with the associated maturity level at the various software reviews (milestone and peer). Table 2 represents the work products maturity at the review’s exit (i.e., Exit / Success Criteria.) Software Assurance is not expected to produce any products for the Facilities Utilization Review Board (FURB), so it is not included in the table below.

See Topics [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) for additional details and maturity schedules. The maturity schedule for all other system and software milestones may be found in Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews).

**Table 2: SASS Work Products and Schedule**

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **SASS Product**       Sub-Product               Sub-Product Details | **FSRR** | **30% Review** | **60% Review** | **90% Review** | **Code Review\*** | **TRR\*\*** | **SIR\*\* (w/ SVT TRR)** | **ISSR (w/ ISAT TRR)** | **ORR** |
| 1 | [Software Assurance Plan](https://swehb.nasa.gov/display/SWEHBVD/8.51+-+Software+Assurance+Plan) | P | B | U | U | U | U | U | U | U/F |
| Software Safety Plan (included in SA Plan) | P | B | U | U |  |  |  |  |  |
| Software Assurance Schedule | P | B | U | U | U | U | U | U | U/F |
| Software Assurance Cost Estimate | P | B | U |  |  |  |  |  |  |
| Software Safety Schedule | P | B | U |  |  |  |  |  |  |
| Software Safety Cost Estimate | P | B | U |  |  |  |  |  |  |
| NASA-STD-8739.8 SASS Requirements Mapping Matrix | P | B | U | U | U | U | U | U | U/F |
| Software Classification and Criticality Determination | P | B | U | U | U | U | U | U | U/F |
| 2 | [Software Requirements Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.54+-+Software+Requirements+Analysis) |  | P | B | U | U | U | U | U | F |
| 3 | [Software Safety and Hazard Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.58+-+Software+Safety+and+Hazard+Analysis) (Performed by Software Engineering) | P | P | B | U | U | U | U | U | F |
| 4 | [Software Design Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.55+-+Software+Design+Analysis) (optional) |  | D | P | B | U | U | U | U | F |
| 5 | [Source Code Quality Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.56+-+Source+Code+Quality+Analysis) (optional) |  |  |  |  | P | B | U | U | U/F |
| Analysis showing uncovered software code percentage |  |  |  |  | P | B | U | U | U/F |
| Software static code assessments |  |  |  |  | P | B | U | U | U/F |
| Analysis showing software code coverage percentage for safety-critical code |  |  |  |  | P | B | U | U | U/F |
| Analysis showing software code complexity for safety-critical code |  |  |  |  | P | B | U | U | U/F |
| Software static code analysis for cybersecurity vulnerabilities and weaknesses |  |  |  |  | P | B | U | U | U/F |
| Software static code analysis showing that the source code follows the defined secure coding practices. |  |  |  |  | P | B | U | U | U/F |
| 6 | [Testing Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.57+-+Testing+Analysis) |  |  | X | X | X | X | X | X | X |
| Software Test Plan Analysis |  |  | P | B | U | U | U | U | F |
| Software Test Procedures Analysis |  |  |  |  | D | B | U | U | U/F |
| Software Test Results Analysis |  |  |  |  | P | P | P | P | B/F |
| Test Witnessing and Signatures |  |  |  |  | X | X | X | X | X |
| 7 | [SA Status Reports](https://swehb.nasa.gov/display/SWEHBVD/8.52+-+Software+Assurance+Status+Reports) | X | X | X | X | X | X | X | X | X |
| List of SA Non-conformances, risks, issues, concerns (Non-conformances == SA Findings, Discrepancies, PRs, Defects) | D | U | U | U | U | U | U | U | U |
| Results of any Analysis done in current phase | X | X | X | X | X | X | X | X | X |
| Verification Activities Analysis | X | X | X | X | X | X | X | X | X |
| Software Assurance Measurements & Analysis | X | X | X | X | X | X | X | X | X |
| Results of Assessments Done Since Last Report | X | X | X | X | X | X | X | X | X |
| Assessment of all the products in Table 1 | A | A | A | A | A | A | A | A | A |
| Assessment of SA Plan | D | P | B | U | U | U | U | U | B/F |
| Assessment of SA Compliance w/ NASA-STD-8739.8 | D | U | U | U | U | U | U | U | B/F |
| Assessment of Software Engineering Plans | P | B | U | U | U | U | U | U | B/F |
| Assessment of SW Engineering Compliance w/ NPR 7150.2 | D | U | U | U | U | U | U | U | B/F |
| Assessments of Hazard Analyses and Reports | P | B | U | U | U | U | U | U | F |
| Assessments of Software Reviews results | D | U | U | U | U | U | U | U | B/F |
| Assessments of Accuracy of Severity-Level Application to Non-Conformances | A | A | A | A | A | A | A | A | A |
| Assessments of Joint NASA/developer Audit Results | A | A | A | A | A | A | A | A | A |
| Results of Audits Done Since Last Report | A | A | A | A | A | A | A | A | A |
| Assessments of Technical Interchange Meetings results | D | U | U | U | U | U | U | U | B/F |
| Assessments of Trade Studies and Source Data Results | P | B | U | U |  |  |  |  |  |
| Project milestone reviews including participation | X | X | X | X | X | X | X | X | X |
| Training Status for Project’s SA Personnel | X | X | X | X | X | X | X | X |  |
| Results of Software Peer Reviews including participation | X | X | X | X | X | X | X | X | X |
| 8 | [Audit Reports](https://swehb.nasa.gov/display/SWEHBVD/8.59+-+Audit+Reports) | A | A | A | A | A | A | A | A | A |
| Peer Review Process Audit Report | A | A | A | A | A | A | A | A | A |
| Risk Management Process Audit Report | A | A | A | A | A | A | A | A | A |
| Software Assurance Process Audit Report | A | A | A | A | A | A | A | A | A |
| SW Development Processes and Practices Audit Report | A | A | A | A | A | A | A | A | A |
| Standards and Processes Audit Report | A | A | A | A | A | A | A | A | A |
| Software Configuration Management Baseline and Process/Procedure Audit Report | A | A | A | A | A | A | A | A | A |
| Software Configuration Management Procedure Audit Report | A | A | A | A | A | A | A | A | A |
| 9 | Objective Evidence | X | X | X | X | X | X | X | X | X |
| Records showing NASA-STD-8739.8B Confirmation tasks were done | X | X | X | X | X | X | X | X | X |
| Software control activities | X | X | X | X | X | X | X | X | X |
| Approvals/sign-offs on deliveries |  |  |  |  |  |  |  |  | F |
| SA Peer Review records | X | X | X | X | X | X | X | X | X |
| Key: | D == Draft: Product is in outline form with some content; Still has a lot of TBDs (To Be Determined). P == Preliminary: Most content is there but has not been baselined yet. B == Baseline: Product reviewed with an action plan to complete. U == Updated: Updated as required. F == Final: Product is finalized and no additional modifications are expected. Signatures obtained, if applicable. A == Anytime: Product may be generated at any time. X == All Phases: Activity or product applies to all phases of the life cycle. The product will be generated at the time of this review. \* == System Milestone to include in Facility Projects \*\* == Software Peer Review | | | | | | | | | |

## 3.3   Definitions & Terms:

* **Unit Test (UT)** – Prior to installation into the operational environment, the software system must be tested. This testing provides the initial opportunity to compile and load the software system configuration and software system for debugging and testing. This testing should be conducted in the development or test environment. Comprehensive testing should be conducted to prove that the software system is ready for installation in the operational environment. This is also known as Bench Top Testing (BTT).
* **System Verification Test (SVT)** – After the software system installation is complete, the System Verification Test (SVT) provides a period for the software development organization to check out, test, and tune the software system in the operational environment in preparation for the Integrated System Acceptance Test. A full execution of the verification test procedures is expected during this test.
* **Integrated Systems Acceptance Test (ISAT)** – A series of acceptance tests to a new or modified testing facility that incorporates a test article to check out all the operational systems and confirm design requirements.

# 4.  Software Engineering Responsibilities

The Facility Project Manager is required to work with project stakeholders including Software Engineering to define the scope of the project. When working with Facility Software with safety considerations, software engineering should treat the facility software in the same manner as with any other software project that invokes to **NPR 7150.2**[083](#_tabs-<p>8</p>). In addition to implementing **NPR 7150.2**, the software engineering organization is also responsible for:

1. Ensuring the requirements in **NPR 7150.2** and **NASA-STD-8739.8**[278](#_tabs-<p>8</p>) are implemented including all safety critical requirements.
   1. For each Facility Project with software, the Facility Project Manager or software lead must complete a Requirements Mapping Matrix (a.k.a. Compliance Matrix) for all the “shall” statements in **NPR 7150.2**. The requirements may be tailored as with any other **NPR 7150.2** project. Software Assurance must create the equivalent NASA-STD-8739.8 Requirements Mapping Matrix. Any intended non-compliances must be explained and receive approval. See [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) and Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan)
2. Participating in the Facility Project milestone reviews.
3. Developing the software assurance analysis (e.g., FMEA, Hazard Analysis, test, etc.).

# 5.  Software Assurance and Software Safety Responsibilities

The Facility Project Manager is required to work with project stakeholders including S&MA to define the scope of the project.

When working with Facility Software with safety considerations, the responsibilities of software assurance and software safety personnel are to:

1. Ensure that the proper software engineering and software assurance requirements are included in the facility activities and contract paperwork.
2. Perform the Software Assurance and Software Safety activities as specified in **NASA-STD-8739.8**[278](#_tabs-<p>8</p>).
   1. Determine and implement the appropriate safety-critical requirements contained in the **NASA Software Engineering Requirements,** **NPR 7150.2**[083](#_tabs-<p>8</p>), and the **Software Assurance and Software Safety Standard, NASA-STD-8739.8**.
      1. The SA Tasking Checklist Tool identifies each of the SA Tasks that need to be performed for safety critical software. (See Topic [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool).) They are also listed in Section 4.0 of this topic.
3. Ensure that the appropriate hazard analysis includes any facility software considerations and software controls.
4. Review and analyze the appropriate hazard analysis to identify any software hazards. To do this:
   1. Use the identified hazards to determine if any of the software is safety-critical.
      1. Use the **Software Assurance and Software Safety Standard, NASA-STD-8739.8**, to determine if the software meets any of the safety critical criteria.
      2. Identify the software elements/components that contain the safety critical code. This information will be used to create and build the Critical Items List (CIL).
   2. Determine the risk of the software hazards in terms of severity and probability.
   3. Recommend controls that will eliminate/mitigate the hazard or reduce the risk of the software hazard.
   4. Communicate the risks of the software hazards to the appropriate authority.
5. Ensure that designated facilities/systems software and other associated documentation are under the appropriate level of configuration management (CM).
   1. Document the CM process and maintain software and associated documentation under it.
6. Identify the appropriate software risk mitigations for the software safety-critical elements.
7. Ensure standard operating procedures are documented and maintained for use by operating personnel.
   1. This includes ensuring comprehensive training and documentation are available for the operating personnel.
   2. The documentation should include detailed procedures, troubleshooting guides, and emergency protocols to ensure the team is well-prepared to handle any situation. A User Manual with instructions and applicable information about the operation of each feature may fulfill this expectation.
8. Ensure facility personnel and facility software assurance personnel review any software changes that affect safety or operations. Ensure any changes in operating procedures are communicated to all facility personnel.
9. Participate in the Facility Project milestone reviews.

See also Topic [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan), [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification), [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management),  [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks), [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)

# 6. Safety Critical SWEs and Associated SASS Task

The table below contains the list of Safety-related Software Assurance and Software Safety (SASS) Tasks and associated SWE requirements from **NASA-STD-8739.8**[278](#_tabs-<p>8</p>) that must be performed for Safety Critical software.

Note: The Safety Critical designations of these SASS tasks are the same as those in Topic [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool). They were reviewed and endorsed by the NASA Office of Safety and Mission Assurance (OSMA) Software Assurance Technical Fellow.

| **SWE #** | **NPR 7150.2  Requirement** | **NASA-STD-8739.8   Software Assurance and Software Safety Tasks** |
| --- | --- | --- |
| 033 | 3.1.2 The project manager shall assess options for software acquisition versus development. | 2. Confirm the flow down of applicable software engineering, software assurance, and software safety requirements on all acquisition activities. (NPR 7150.2 and NASA-STD-8739.8). |
| 013 | 3.1.3 The project manager shall develop, maintain, and execute software plans, including security plans, that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring. | 1. Confirm that all plans, including security plans, are in place and have expected content for the life cycle events, with proper tailoring for the classification of the software.  2. Develop and maintain a Software Assurance Plan following the content defined in NASA-HDBK-2203 for a software assurance plan, including software safety. |
| 024 | 3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.   1. 1. Corrective actions are taken, recorded, and managed to closure.    2. Changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals are taken, recorded, and managed. | 1. Assess plans for compliance with NPR 7150.2 requirements, NASA-STD-8739.8, including changes to commitments.  2. Confirm that closure of corrective actions associated with the performance of software activities against the software plans, including closure rationale.  3. Confirm changes to commitments are recorded and managed. |
| 036 | 3.1.6 The project manager shall establish and maintain the software processes, software documentation plans, list of developed electronic products, deliverables, and list of tasks for the software development that are required for the project’s software developers, as well as the action required (e.g., approval, review) of the Government upon receipt of each of the deliverables. | 1. Confirm the following are approved, implemented, and updated per requirements:      a. Software processes, including software assurance,           software safety, and IV&V processes,      b. Software documentation plans,      c. List of developed electronic products, deliverables, and      d. List of tasks required or needed for the project’s           software development.      2. Confirm that any required government actions are established and performed upon receipt of deliverables (e.g., approvals, reviews). |
| 039 | 3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:   1. 1. Monitor product integration.    2. Review the verification activities to ensure adequacy.    3. Review trade studies and source data.    4. Audit the software development processes and practices.    5. Participate in software reviews and technical interchange meetings. | 8. Confirm that the project manager provides responses to software assurance and software safety submitted issues, findings, and risks and that the project manager tracks software assurance and software safety issues, findings, and risks to closure. |
| 139 | 3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an “X” in Appendix C consistent with their software classification. | 1. Assess that the project's software requirements, products, procedures, and processes are compliant with the NPR 7150.2 requirements per the software classification and safety criticality for software. |
| 121 | 3.1.12 Where approved, the project manager shall document and reflect the tailored requirement in the plans or procedures controlling the development, acquisition, and deployment of the affected software. | 1. Confirm that any requirement tailoring in the Requirements Mapping Matrix has the required approvals.  2. Develop a tailoring matrix of software assurance and software safety requirements. |
| 125 | 3.1.13 Each project manager with software components shall maintain a requirements mapping matrix or multiple requirements mapping matrices against requirements in this NPR, including those delegated to other parties or accomplished by contract vehicles or Space Act Agreements. | 1. Confirm that the project maintains a requirements mapping matrix (matrices) for all requirements in NPR 7150.2.      2. Maintain the requirements mapping matrix (matrices) for requirements in NASA-STD-8739.8. |
| 015 | 3.2.1 To better estimate the cost of development, the project manager shall establish, document, and maintain:   1. 1. Two cost estimate models and associated cost parameters for all Class A and B software projects that have an estimated project cost of $2 million or more.    2. One software cost estimate model and associated cost parameter(s) for all Class A and Class B software projects that have an estimated project cost of less than $2 million.    3. One software cost estimate model and associated cost parameter(s) for all Class C and Class D software projects.    4. One software cost estimate model and associated cost parameter(s) for all Class F software projects. | 1. Confirm that the required number of software cost estimates are complete and include software assurance cost estimate(s) for the project, including a cost estimate associated with handling safety-critical software and safety-critical data. |
| 151 | 3.2.2 The project manager’s software cost estimate(s) shall satisfy the following conditions:   a. Covers the entire software life cycle. b. Is based on selected project attributes (e.g., programmatic assumptions/constraints, assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products). c. Is based on the cost implications of the technology to be used and the required maturation of that technology. d. Incorporates risk and uncertainty, including end state risk and threat assessments for cybersecurity. e. Includes the cost of the required software assurance support. f. Includes other direct costs. | 1. Assess the project's software cost estimate(s) to determine if the stated criteria listed in "a" through "f" are satisfied. |
| 174 | 3.2.3 The project manager shall submit software planning parameters, including size and effort estimates, milestones, and characteristics, to the Center measurement repository at the conclusion of major milestones. | 2. Confirm that all software assurance and software safety software estimates and planning parameters are submitted to an organizational repository. |
| 016 | 3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. Reflects the critical dependencies for software development activities.    4. Identifies and accounts for dependencies with other projects and cross-program dependencies. | 2. Develop a software assurance schedule, including software assurance products, audits, reporting, and reviews. |
| 020 | 3.5.1 The project manager shall classify each system and subsystem containing software in accordance with the highest applicable software classification definitions for Classes A, B, C, D, E, and F software in Appendix D. | 1. Perform a software classification or concur with the engineering software classification of software per the descriptions in NPR 7150.2. |
| 176 | 3.5.2 The project manager shall maintain records of each software classification determination, each software Requirements Mapping Matrix, and the results of each software independent classification assessments for the life of the project. | 1. Confirm that records of the software Requirements Mapping Matrix and each software classification are maintained and updated for the life of the project. |
| 022 | 3.6.1 The project manager shall plan and implement software assurance, software safety, and IV&V (if required) per NASA-STD-8739.8, Software Assurance and Software Safety Standard. | 1. Perform software assurance, software safety, and IV&V (if required) according to the software assurance and software safety standard requirements in NASA-STD-8739.8, Software Assurance and Software Safety Standard, and the Project’s software assurance plan. |
| 205 | 3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8. | 1. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.    2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.  3. Assess that hazard analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.    4. Confirm that the traceability between software requirements and hazards with software contributions exists.    5. Develop and maintain a software safety analysis throughout the software development life cycle. |
| 023 | 3.7.2 If a project has safety-critical software, the project manager shall implement the safety-critical software requirements contained in NASA-STD-8739.8. | 1. Confirm that the identified safety-critical software components and data have implemented the safety-critical software assurance requirements listed in this standard. |
| 134 | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:   a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. k. The software provides error handling. l. The software can place the system into a safe state. | 1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l."  2. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone.    3. Confirm that the values of the safety-critical loaded data, uplinked data, rules, and scripts that affect hazardous system behavior have been tested.      4. Analyze the software design to ensure the following:    a. Use of partitioning or isolation methods in the           design and code,    b. That the design logically isolates the safety-critical           design elements and data from those that are           non-safety-critical.      5. Participate in software reviews affecting safety-critical software products.    6. Ensure the SWE-134 implementation supports and is consistent with the system hazard analysis. |
| 219 | 3.7.4 If a project has safety-critical software, the project manager shall ensure that there is 100 percent code test coverage using the Modified Condition/Decision Coverage (MC/DC) criterion for all identified safety-critical software components. | 1. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component. |
| 220 | 3.7.5 If a project has safety-critical software, the project manager shall ensure all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. Any exceedance shall be reviewed and waived with rationale by the project manager or technical approval authority. | 1. Perform or analyze Cyclomatic Complexity metrics on all identified safety-critical software components.    2. Confirm that all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. If not, assure that software developers provide a technically acceptable risk assessment, accepted by the proper technical authority, explaining why the cyclomatic complexity value needs to be higher than 15 and why the software component cannot be structured to be lower than 15 or why the cost and risk of reducing the complexity to below 15 are not justified by the risk inherent in modifying the software component. |
| 052 | 3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between the following software elements:   |  |  |  |  | | --- | --- | --- | --- | | Bi-directional Traceability | Class A, B, and C | Class D | Class F | | Higher-level requirements to the software requirements | X |  | X | | Software requirements to the system hazards | X | X |  | | Software requirements to the software design components | X |  |  | | Software design components to the software code | X |  |  | | Software requirements to the software verification(s) | X | X | X | | Software requirements to the software non-conformances | X | X | X | | 2. Confirm that the software traceability includes traceability to any hazard that includes software. |
| 051 | 4.1.3 The project manager shall perform software requirements analysis based on flowed down and derived requirements from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design. | 1. Perform a software assurance analysis on the detailed software requirements to analyze the software requirement sources and identify any incorrect, missing, or incomplete requirements. |
| 184 | 4.1.4 The project manager shall include software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software in the software requirements documentation. | 1. Analyze and confirm that the software requirements documentation contains the software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and the software. |
| 058 | 4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. | 4. Confirm that the software design implements all of the required safety-critical functions and requirements. |
| 135 | 4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to, at a minimum, detect defects, software security, code coverage, and software complexity. | 2. Confirm the static analysis tool(s) are used with checkers to identify security and coding errors and defects.      5. Per SWE-219 for safety-critical software, verify code coverage and approved waivers.    6. Per SWE-220 for safety-critical software, verify cyclomatic complexity and approved waivers. |
| 062 | 4.4.5 The project manager shall unit test the software code. | 1. Confirm that the project successfully executes the required unit tests, particularly those testing safety-critical functions. |
| 065a | 4.5.2 The project manager shall establish and maintain:   a. Software test plan(s). b. Software test procedure(s). c. Software test(s), including any code specifically written to perform test procedures. d. Software test report(s). | 2. Confirm that the software test plan addresses the verification of safety-critical software, specifically the off-nominal scenarios. |
| 065b | 4.5.2 The project manager shall establish and maintain:   a. Software test plan(s). b. Software test procedure(s). c. Software test(s), including any code specifically written to perform test procedures. d. Software test report(s). | 2. Analyze the software test procedures for the following:     a. Coverage of the software requirements.    b. Acceptance or pass/fail criteria,     c. The inclusion of operational and off-nominal conditions,         including boundary conditions,     d. Requirements coverage and hazards per SWE-066 and         SWE-192, respectively.    e. Requirements coverage for cybersecurity per SWE-157         and SWE-210. |
| 066 | 4.5.3 The project manager shall test the software against its requirements. | 2. Perform test witnessing for safety-critical software.      3. Confirm that any newly identified software contributions to hazards, events, or conditions found during testing are in the system safety data package. |
| 068 | 4.5.5 The project manager shall evaluate test results and record the evaluation. | 3. Confirm that test results are sufficient verification artifacts for the hazard reports. |
| 071 | 4.5.7 The project manager shall update the software test and verification plan(s) and procedure(s) to be consistent with software requirements. | 1. Analyze that software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal scenarios. |
| 191 | 4.5.11 The project manager shall plan and conduct software regression testing to demonstrate that defects have not been introduced into previously integrated or tested software and have not produced a security vulnerability. | 1. Confirm that the project plans regression testing and that the regression testing is adequate and includes retesting of all safety-critical code components. |
| 192 | 4.5.12 The project manager shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique. | 1. Through testing, confirm that the project verifies the software requirements which trace to a hazardous event, cause, or mitigation techniques. |
| 080 | 5.1.3 The project manager shall track and evaluate changes to software products. | 1. Analyze proposed software and hardware changes to software products for impacts, particularly safety and security. |
| 081 | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. | 2. Assess that the software safety-critical items are configuration-managed, including hazard reports and safety analysis. |
| 087 | 5.3.2 The project manager shall perform and report the results of software peer reviews or software inspections for:   a. Software requirements. b. Software plans, including cybersecurity. c. Any design items that the project identified for software peer review or software inspections according to the software development plans. d. Software code as defined in the software and or project plans. e. Software test procedures. | 4. Confirm that the source code satisfies the conditions in the NPR 7150.2 requirement SWE-134, "a" through "l," based upon the software functionality for the applicable safety-critical requirements at each code inspection/review. |

# 7. Facility Milestone Entry/Exit Criteria

This section addresses the unique requirements for the facility milestone review entry/exit criteria. The entry/exit criteria for the system/software milestones are discussed in Topic [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria).

## 7.1 Facility & Systems Requirements Review (FSRR)

The FSRR evaluates whether the project functional and performance requirements are properly formulated and correlated with center and operating organization needs, goals, and objectives. Project requirements are baselined by the conclusion of the FSRR. The FSRR also assesses the credibility of the project’s estimated budget and schedule.

The center critical facility development project IRB shall conduct a Facility & Systems Requirements Review per **NPR 8820.2, Facility Project Requirements**[692](#_tabs-<p>8</p>), and the criteria listed in Table 3 below.

**Table 3: Facility and System Requirements Review Criteria**

| Entrance Criteria | Exit/Success Criteria |
| --- | --- |
| 1. The operator organization has provided an operations concept and user requirements set and current hazard analyses for existing facility and systems. 2. The facility development project has provided a complete set of requirements for the facility. 3. The facility development project has provided safety analysis products:    1. Preliminary hazard list for new work 4. The facility development project has provided other System engineering products (as applicable) for facility construction, hardware, software, and human system elements.    1. Preliminary engineering assessment of requirements, including a summary of key trade studies and results.    2. Risk assessment and mitigations.    3. Initial document tree or model structure.    4. Preliminary verification and validation method identified for each requirement.    5. Initial Human Rating Certification Package (as applicable). 5. Prepare and provide the work products and documentation specified in[Table 1 and Table 2](#tabs-3) for this review. | 1. The top-level requirements are agreed upon (by developer and operator organizations), finalized, stated clearly. 2. Facility and system requirements comply with corresponding Critical Facility functional and performance requirements. 3. Facility and system requirements are achievable and sufficiently mature to support design activities. 4. Major risks have been identified and technically assessed, and viable mitigation strategies have been defined. 5. The project has complied with applicable government, NASA and implementing Center requirements, standards, processes, and procedures. 6. TBD and TBR items are clearly identified with acceptable plans and schedule for their disposition. 7. The software work products and documentation for this review are at the maturity level listed in [Table 1](#tabs-3). 8. The software assurance work products for this review are at the maturity level listed in [Table 2](#tabs-3). |

## 7.2 30-Percent Design Review

The 30-Percent Design Review for a center critical facility encompasses and expands upon the traditional facility development 30-Percent Design Review milestone as defined in **NPR 8820.2, Facility Project Requirements**. The expanded review criteria demonstrate that the preliminary design meets all system requirements with acceptable risk and within the cost and schedule constraints and establishes the basis for proceeding with detailed design.

The center critical facility development project IRB shall conduct a 30-Percent Design Review per **NPR 8820.2, Facility Project Requirements**, and the criteria listed in the table below.

**Table 4: 30% Review Criteria**

| Entrance Criteria | Exit/Success Criteria |
| --- | --- |
| 1. The facility development project has provided facility construction design documentation required per NPR 8820.2. 2. The facility development project has provided a preliminary design that meets requirements, including:    1. Subsystem hardware and software design specifications with supporting trade studies and data    2. Engineering drawing tree    3. Interface control documents (ICDs) 3. The facility development project has provided safety analysis products:    1. Updated hazard list    2. Preliminary hazard analysis    3. Energy Trace Barrier Analysis    4. Preliminary FMEA    5. Facility Safety Management Plan    6. List of necessary subsystem and component inspections 4. The facility development project has provided project and technical management products:    1. Updated risk assessment and mitigation    2. Updated schedule    3. Updated project cost estimate    4. Updated trending information on the closure of review actions (RFA, RID, and/or Action Items).    5. Plans to respond to regulatory requirements (e.g., Environmental Impact Statement), as required.    6. For new software development, Software Classification and development plan. 5. Prepare and provide the work products and documentation specified in [Table 1 and Table 2](#tabs-3) for this review. | 1. The preliminary design is expected to meet the requirements at an acceptable level of risk.  The operator organization has reviewed and concurred with this design solution. 2. Project cost and schedule are credible and within constraints. Adequate resources are available to complete development and commissioning within budget, schedule, and known risks. 3. The project risks are understood and have been credibly assessed, and plans, a process, and resources exist to effectively manage them. 4. Safety and mission assurance designs and products meet requirements, are at the appropriate maturity level, and indicate that the project safety/reliability residual risks will be at an acceptable level. 5. Technical trade studies are mostly complete to sufficient detail and remaining trade studies are identified, plans exist for their closure, and potential impacts are understood. 6. Preliminary subsystem analysis has been completed and summarized, highlighting performance and design margin challenges. Where appropriate, modeling, and analytical results are available. 7. The project complies with applicable government, NASA and Center requirements, standards, processes, and procedures. 8. Heritage and benchmark designs have been suitably assessed for applicability and appropriateness. 9. Plans and processes for new software development and testing are appropriate and technically sound. 10. TBD and TBR items are clearly identified with acceptable plans and schedule for their disposition. 11. The software work products and documentation for this review are at the maturity level listed in [Table 1](#tabs-3). 12. The software assurance work products for this review are at the maturity level listed in [Table 2](#tabs-3). |

## 7.3 60-Percent Design Review

The center critical facility development project IRB shall conduct a 60-Percent Design Review per **NPR 8820.2, Facility Project Requirements**, and the criteria listed in the table below.

**Table 5: 60% Design Review Criteria**

| Entrance Criteria | Exit/Success Criteria |
| --- | --- |
| 1. The facility development project has provided design documentation required for a 60% design review as specified in NPR 8820.2. 2. The facility development project has provided an updated preliminary design that meets requirements, including:    1. Update Subsystem hardware and software design specifications with supporting trade studies and data    2. Update Engineering drawing tree    3. Updated Interface control documents (ICDs) 3. The facility development project has provided safety analysis products:    1. Updated hazard list    2. Updated facility and system hazard analysis    3. Updated FMEA    4. Critical Items List    5. Updated Facility Safety Management Plan    6. Updated list of necessary subsystem and component inspections 4. The facility development project has provided project and technical management products:    1. Updated trending information on the closure of review actions (RFA, RID and/or Action Items).    2. Preliminary operational limits and constraints.    3. For new software development, updated Software Classification and development plan.    4. Updated risk assessment and mitigation.    5. Updated schedule    6. Updated cost estimate    7. Reliability analyses and assessments. 5. Preliminary Systems and subsystem certification plans and requirements (as needed). 6. Prepare and provide the work products and documentation specified in [Table 1 and Table 2](#tabs-3) for this review. | 1. The FPM shall ensure that the following minimum deliverables for this 60-percent submission are identified within the A/E SOW:    1. A drawing package with a cover sheet, including a drawing index, initial versions of drawings and equipment schedules for all required disciplines. Although the drawings will be in varying states of maturity, the set should be complete enough to validate the construction cost estimate. The drawings should reflect adequate M&O clearances around all equipment and systems.    2. First draft of construction specifications, including all required sections for each discipline that are edited to reflect the project requirements.    3. Completed design analyses and supporting engineering calculations.    4. A second draft of the construction phasing plan and the commissioning plan.    5. First draft of the construction schedule identifying key milestones and utility tie-in requirements.    6. Identification of any constructability issues.    7. A comprehensive construction engineering estimate and AFPCE in accordance with Section 3.5.7.2.f. 2. The software work products and documentation for this review are at the maturity level listed in [Table 1](#tabs-3). 3. The software assurance work products for this review are at the maturity level listed in [Table 2](#tabs-3). |

## 7.4 90-Percent Design Review

The 90-percent design review encompasses and expands upon the traditional facility development 90% design review milestone as defined in **NPR 8820.2, Facility Project Requirements**. The expanded review criteria demonstrate that the maturity of the design is appropriate to support proceeding with construction, assembly, integration, and test. A construction permit will only be issued after successful completion of the 90-percent design review.

The center critical facility development project IRB shall conduct a 90-Percent Design Review per **NPR 8820.2, Facility Project Requirements**, and the criteria listed in the table below.

**Table 6: 90% Design Review Criteria**

| Entrance Criteria | Exit/Success Criteria |
| --- | --- |
| 1. The facility development project has provided design documentation required for a 90% design review as specified in NPR 8820.2. 2. The facility development project has provided safety analysis products:    1. Updated hazard list    2. Updated facility and system hazard analysis    3. Updated FMEA    4. Subsystem-level and preliminary operations safety analyses    5. Updated Critical Items List 3. The facility development project has provided project and technical management products.    1. Updated trending information on the closure of review actions (RFA, RID and/or Action Items).    2. Defined operational limits and constraints.    3. Acceptance plans    4. Preliminary checkout and activation plan.    5. Updated risk assessment and mitigation.    6. Updated schedule    7. Updated cost estimate    8. Updated reliability analyses and assessments. 4. Systems and subsystem certification plans and requirements (as needed). 5. Prepare and provide the work products and documentation specified in [Table 1 and Table 2](#tabs-3) for this review. | 1. The detailed design is expected to meet the requirements. The operator organization has reviewed and concurred with this design solution. 2. The project cost and schedule estimates are credible and within project constraints. Adequate margins and resources exist to complete the development within budget, schedule, and known risks. 3. High confidence exists in the design baseline, and adequate documentation exists to allow proceeding with construction, integration, and test. 4. Identified fabrication, construction, and assembly methods are sufficient to meet requirements. 5. The test approach is comprehensive, and the plan for system assembly, integration, test, and operations is sufficient to proceed with construction. 6. Safety and mission assurance have been adequately addressed in system and operational designs. Safety/reliability residual risks will be at an acceptable level. 7. The project complies with applicable government, NASA and Center requirements, standards, processes, and procedures. 8. Engineering test units, life test units, and/or modeling and simulations have been developed and tested per plan. 9. The operational concept has been considered in test planning. 10. The software work products and documentation for this review are at the maturity level listed in [Table 1](#tabs-3). 11. The software assurance work products for this review are at the maturity level listed in [Table 2](#tabs-3). |

## 7.5 Independent Safety Reviews (ISRs)

### 7.5.1.   Integrated System Safety Review (ISSR)

The ISSR assesses the overall safety of the facility and its planned operation, confirms the facility supports intended operational characteristics, ensures that hazard controls have been validated, and confirms that plans reflect a systematic approach to demonstrate the full operational capability. The ISSR is held before facility Integrated System Test to ensure that appropriate safety measures are in place to support the test.

The center critical facility development project IRB shall conduct an Integrated System Safety Review per the criteria listed in the table below.

**Table 7: Integrated System Safety Review Criteria**

| Entrance Criteria | Exit/Success Criteria |
| --- | --- |
| 1. The facility development project has provided final project and technical products:    1. Facility / system requirements and design    2. List and assessment of critical functions and components    3. Analysis of primary load paths    4. Comparison of as-built vs. design, summarized by subsystem (Redlines, Non-Compliance Reports)    5. Description and status of unmodified systems, specifying interaction and effect of modified and unmodified systems on one another.    6. Summary of previous review findings with associated closures and list of open items 2. The facility development project has provided documentation of subsystem-level verification and validation tests and results:    1. Sequence to prepare for ISAT    2. Test objectives, envelopes, and constraints    3. Off-nominal response requirements verification    4. Requirements verification capture process and results    5. Anomaly resolution process 3. The facility development project has provided Integrated System Test Plan materials that define:    1. Test objectives, envelopes, and constraints    2. Redlines, margins, assumptions, model validation    3. Standard operating procedures    4. Emergency procedures    5. Training requirements    6. Test-specific hardware/software    7. Anomaly resolution process    8. ISAT specific requirements verification 4. The facility development project has provided completed safety analyses that have been reviewed by the Office of Safety and Mission Assurance, including:    1. FMEA, OHA, HAZOP    2. Facility, System and software hazard analyses and controls    3. Procedural hazards and controls    4. Hazard control verification 5. Prepare and provide the work products and documentation specified in [Table 1 and Table 2](#tabs-3) for this review. | 1. Safety analyses are complete and correct. 2. Hazard controls are adequate and their operation has been verified. 3. Contingency conditions and responses have been defined and included in operator training, including:    1. Operational redline values    2. Emergency shutdown procedures    3. Contingency procedures 4. Personnel are adequately trained and properly equipped to operate the facility / system and appropriately respond to anomalies and emergencies. 5. Systems, processes, and procedures are in place to support testing. 6. Test plans and procedures adequately address the intended facility range of operation. 7. Hazard mitigations have been validated; associated verification plans are acceptable. 8. Hazard residual risks have been identified and accepted by management. 9. The software work products and documentation for this review are at the maturity level listed in [Table 1](#tabs-3). 10. The software assurance work products for this review are at the maturity level listed in [Table 2](#tabs-3). |

## 7.6 Operational Readiness Review (ORR)

Transition from the facility development phase to the facility operations phase is marked by successful completion of an Operational Readiness Review (ORR). The ORR verifies the completeness of the facility and system development and test efforts, accuracy and completeness of associated documentation, compliance to stakeholder expectations, and technical maturity to authorize its transfer to the operating organization.

The center critical facility development project IRB shall conduct an Operational Readiness Review per the criteria listed in the table below.

**Table 8: Operational Readiness Review Criteria**

| Entrance Criteria | Exit/Success Criteria |
| --- | --- |
| 1. The facility development project has provided key facility documentation to the operator organization and to reviewers:    1. As-built facility, hardware and software documentation.    2. Commissioning test results.    3. Documentation that the system complies with the established acceptance criteria.    4. Documentation that the system will perform properly in the expected operational environment.    5. Applicable operating certification documents.    6. Required checkout and operational plans and procedures.    7. Updated risks and mitigations 2. The facility operations organization confirms that all operational supporting and enabling products necessary to support operations (e.g., facilities, equipment, documents, software tools, databases) necessary for nominal and contingency operations have been tested and delivered/installed. 3. The facility development project has successfully completed all planned commissioning testing. 4. The facility development project has reviewed and resolved all test failures and anomalies from verification and validation testing. Results/mitigations/workarounds have been incorporated into operational products. 5. The facility development project and the facility operations organization both agree that all hazard mitigation have been verified and hazard reports are closed. 6. Prepare and provide the work products and documentation specified in [Table 1 and Table 2](#tabs-3) for this review. | 1. Required tests and analyses are complete and indicate that the system will perform properly in the expected operational environment. 2. Risks are known and manageable. 3. The system meets established acceptance criteria. 4. The facility complies with applicable government (including OSHA and EPA), NASA and Center requirements, standards, processes, and procedures. 5. Adequate provisions (i.e., safety related materials and critical spare parts) are in hand and effective. 6. The technical data package and other required delivery documentation is complete and reflects the delivered system. 7. Safe operating limits are well-defined, appropriate, and ensure that that permissible stress limits will not be exceeded; reliable controls are in place to prevent exceeding these safe operating limits. 8. Adequate measures have been taken to ensure the safety of the facility and its operators over the design range of the facility or device. 9. Operational procedures are documented, clear, and complete. 10. Operations personnel are properly trained and, where necessary, certified per formal certification requirements. 11. Applicable lessons learned for organizational improvement and system operations are captured. 12. Agreements with contractor organizations are complete and correct. 13. The software work products and documentation for this review are at the maturity level listed in [Table 1](#tabs-3). 14. The software assurance work products for this review are at the maturity level listed in [Table 2](#tabs-3). |

# 8. Resources

## 8.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-692)

  [Facility Project Requirements (FPR) (Updated with Administrative edits w/Change 1)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8820&s=2G "Click to open in new window")

  NPR 8820.2 Rev I, Effective Date: September 04, 2024, Expiration Date: September 04, 2029
* (SWEREF-693)

  [NASA Safety and Health Programs](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_8715_001B_&page_name=main&search_term=8715%2E1 "Click to open in new window")

  NPR 8715.1B, Office of Safety and Mission Assurance, Effective Date: February 01, 2021, Expiration Date: February 01, 2026
   See Chapter 14. Facility Safety Management
* (SWEREF-694)

  [Real Estate Management Program (Updated with Change 2)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8800&s=15F "Click to open in new window")

  NPR 8800.15F, Office of Strategic Infrastructure, Effective Date: October 08, 2024, Expiration Date: October 08, 2029

## 8.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 8.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks), * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

## 8.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>8</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only).

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 8.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
