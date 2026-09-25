# 8.59 - Audit Reports

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695745. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports

8.59 - Audit Reports

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695745)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695745&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Audits](#tabs-2)
* [3. Audit Metrics](#tabs-3)
* [4. Audit Schedules](#tabs-4)
* [5. Audit & Assessment Checklists](#tabs-5)
* [6. Small Project Audits](#tabs-6)
* [7. Audit Report Contents](#tabs-7)
* [8. Resources](#tabs-8)

Return to [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products)

# 1.  Introduction

A main software assurance objective is to provide a level of confidence that the software produced is error free and performs in its intended manner. Thus, the software assurance personnel are involved in projects throughout the entire software development life cycle monitoring the development activities, ensuring that the correct standards, processes, and procedures are being followed, and evaluating the product quality as it is being developed. Audits are a common tool used to assess the quality of the software products and the level of compliance with the process requirements.

The Audit Reports topic focuses on the many aspects of software auditing and how to report the results. Since audits and auditing are discussed in many areas of this Handbook, some audit topics will provide links to other areas of the Handbook where the information is already located. For example, Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) contains an extensive description of the basic process of planning and conducting an audit, along with reporting the results.

The information in this topic is divided into several tabs as follows:

* Tab 1 – Introduction.
* Tab 2 – Audit requirements and recommendations in the Software Assurance and Software Safety Standard (NASA-STD-8739.8).
* Tab 3 – Audit Metrics that are typically collected or associated with audits and their use.
* Tab 4 – Audit Schedules discusses when to conduct process/procedure audits
* Tab 5 – Audit and Assessment Checklists provides a list of the available Process Asset Templates (PATs) that may be used for process audits and SWE work product assessments.
* Tab 6 – Small Project Audits gives tips to small projects to minimize cost
* Tab 7 – Audit Report Contents discusses the communication of the audit results.
* Tab 8 – Resources for this topic.

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

See also [SWE-022 - Software Assurance](/pages/viewpage.action?pageId=16780799) for Audit Reports listed in SA Work Products.

# 2. Audits

Auditing is one tool used by the software assurance and software safety personnel to determine whether projects are following and in compliance with governing requirements and standards along with project processes and procedures. Thus, the Software Assurance and Software Safety (SASS) Standard (NASA-STD-8739.8) lists requirements for many types of audits and required tasks that could be performed by auditing (e.g., compliance assessments).

When conducting audits, there are two basic types – Formal and Informal. Formal audits are discussed in Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing). Informal have less rigor and more leeway on how they are conducted.

* Formal Audits – Formal audits involve carefully selected areas, outcomes, and samples. Some characteristics are:
  + Audit team typically includes members from external organizations
  + Audits focus on comprehensive process/procedure audits, typically reviewing the organization
  + Results are reported to upper management or corporate executives
  + Audits are against organizational or industry standards
  + Findings may result in corporate repercussions such as the loss of a certification or contract
  + Audits use formal/structured reporting and documentation
  + Audit Planning is formal and structured; coordination and communication are very formal and well documented
* Informal Audits – Informal audits are generally much smaller and may be performed on an ad hoc basis. Some characteristics are:
  + Audit team members are primarily from internal teams
  + Audits often check one process/procedure at a time, typically looking at the project
  + Results are reported to project management
  + Audits are against project processes/ procedures/ standards
  + Findings may be resolved by the project
  + Reporting and documentation are more informal (e.g., SA Status Reports)
  + Audit Planning is coordinated and communicated informally

There are three basic audit perspectives – targeted, generic, and those that satisfy other requirements. The targeted audits focus on one specific process, product, or activity (e.g., software configuration management audits). Generic audits are more general in nature and may call for audits of standards, processes, procedures, and practices. Those audits may require multiple audits, spanning the life cycle to ensure all aspects are met (e.g., software development audits). A third perspective of audits is comprised of those requirements in the SASS Standard listed as “confirm” or “assess” that can be easily satisfied by performing an audit (e.g., SASS tasking for SWE-139 which calls for assessing compliance to NPR 7150.2). All three audit perspectives should be considered when planning the schedule of audits for a project. All project audits should be planned in conjunction with the activities that are occurring in that time period and need to be coordinated with the project schedule. For example, it does not make sense to plan an audit to evaluate the test procedures during the planning phase when they have not been developed yet.

As mentioned previously in the Introduction, there are many good resources on planning, conducting, and closing out an audit in Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing).  As part of the planning for an audit, checklists should be generated or used. To make this easier, there are many checklists available in this Handbook as well as in Center asset libraries, which can be accessed from the NASA Engineering Network (NEN) Software Community of Practice (CoP) Software Processes Across NASA (SPAN) [197](#_tabs-<p>8</p>) site. Once on the Software Engineering CoP, select the “Process Assets (SPAN)” option to access the NASA SPAN [197](#_tabs-<p>8</p>) site. A list of audit checklists can be found in this Handbook in Topics [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) and [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists). As part of the audit preparation, checklists should be reviewed as they may need to be modified to fit specific tailored, approved processes that are in place for the project.

After the audit is conducted, a key part of any audit involves the post audit activities and actions. Any type of non-conformance, including findings, issues, defects, or errors found during an audit is recorded in a tracking system and these non-conformances are tracked to closure by the audit team. An analysis or assessment of the non-conformances should be performed and compared with previous or similar audit results to determine if there are systemic or consistent problems, which might require a closer look.

Most of the audits that Software Assurance will perform are of the informal nature and targeted to software particular process, procedure, activity, or product. Table 1 below lists the required Software Assurance and Software Safety Standard (SASS) audits along with the associated SWE requirement number. Table 2 lists some of the SASS Tasks where an audit might be one way to satisfy the requirement but is not the only method that could be used.

**Table 1: Audit Requirements in the Software Assurance and Software Safety Standard (NASA-STD-8739.8 [278](#_tabs-<p>8</p>)):**

|  |  |  |
| --- | --- | --- |
| **SWE #** | **NPR 7150.2  Requirement** [083](#_tabs-<p>8</p>) | **NASA-STD-8739.8   Software Assurance and Software Safety Tasks** [278](#_tabs-<p>8</p>) |
| 084 | 5.1.7 The project manager shall perform software configuration audits to determine the correct version of the software configuration items and verify that they conform to the records that define them. | 1. Confirm that the project manager performed software configuration audits to determine the correct version of the software configuration items and verify that the results of the audit conform to the records that define them. |
| 077 | 4.6.3 The project manager shall complete and deliver the software product to the customer with appropriate records, including as-built records, to support the operations and maintenance phase of the software’s life cycle. | 1. Confirm that the correct version of the products is delivered, including as-built documentation and project records.      2. Perform audits for all deliveries per the configuration management processes to verify that all products are being delivered and are the correct versions. |
| 045 | 5.1.9 The project manager shall participate in any joint NASA/developer audits. | 1. Participate in or assess the results from any joint NASA/developer audits. Track any findings to closure. |
| 088 | 5.3.3 The project manager shall, for each planned software peer review or software inspection:  a. Use a checklist or formal reading technique (e.g., perspective-based reading) to evaluate the work products. b. Use established readiness and completion criteria. c. Track actions identified in the reviews until they are resolved. d. Identify the required participants. | 3. Perform audits on the peer-review process. |
| 086 | 5.2.1 The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans. | 2. Perform audits on the risk management process for the software activities. |
| 039 | 3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:   1. 1. Monitor product integration.    2. Review the verification activities to ensure adequacy.    3. Review trade studies and source data.    4. Audit the software development processes and practices.    5. Participate in software reviews and technical interchange meetings. | 5. Perform audits on software development processes and practices at least once every two years.  6. Develop and provide status reports.  7. Develop and maintain a list of all software assurance review discrepancies, risks, issues, findings, and concerns. |
| 195 | 4.6.5 The project manager shall maintain the software using standards and processes per the applicable software classification throughout the maintenance phase. | 1. Perform audits on the standards and processes used throughout maintenance based on the software classification. |
| 085 | 5.1.8 The project manager shall establish and implement procedures for the storage, handling, delivery, release, and maintenance of deliverable software products. | 2. Perform audits on the project to ensure that the project follows defined procedures for deliverable software products. |
| 032 | 3.9.2 The project manager shall acquire, develop, and maintain software from an organization with a non-expired CMMI-DEV rating as measured by a CMMI Institute Certified Lead Appraiser as follows:   1. 1. For Class A software: CMMI-DEV Maturity Level 3 Rating or higher for software.    2. For Class B software (except Class B software on NASA Class D payloads, as defined in NPR 8705.4): CMMI-DEV Maturity Level 2 Rating or higher for software. | 3. Perform audits on the software development and software assurance processes. |

**Table 2: Requirements in NASA-STD-8739.8 that might be satisfied with the use of an audit:**

|  |  |  |
| --- | --- | --- |
| SWE | NPR 7150.2 Requirement | Software Assurance and Software Safety Tasks |
| 139 | 3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an “X” in Appendix C consistent with their software classification. | 1. Assess that the project's software requirements, products, procedures, and processes are compliant with the NPR 7150.2 requirements per the software classification and safety criticality for software. |
| 079 | 5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project. | 1. Assess that a software configuration management plan has been developed and complies with the requirements in NPR 7150.2 and Center/project guidance. |
| 016 | 3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. Reflects the critical dependencies for software development activities.    4. Identifies and accounts for dependencies with other projects and cross-program dependencies. | 1. Assess that the software schedule satisfies the conditions in the requirement. |
| 024 | 3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.   1. 1. Corrective actions are taken, recorded, and managed to closure.    2. Changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals are taken, recorded, and managed. | 1. Assess plans for compliance with NPR 7150.2 requirements, NASA-STD-8739.8, including changes to commitments. |
| 013 | 3.1.3 The project manager shall develop, maintain, and execute software plans, including security plans, that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring. | 1. Confirm that all plans, including security plans, are in place and have expected content for the life cycle events, with proper tailoring for the classification of the software.  2. Develop and maintain a Software Assurance Plan following the content defined in NASA-HDBK-2203 for a software assurance plan, including software safety. |

Note: This is not a complete list but is meant to provide some examples.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 3. Audit Metrics

Audit metrics may be collected and reported on at the organization or project-level. Those collected at the organization-level may be the result of organization-level audits or the roll-up of the audit data from individual projects to see how the organization is performing as a whole. The audit metrics collected at the project-level are specific to the project and should be able to provide insight into the health and status of the project.

Note: Projects include any projects where NASA may be performing audits (NASA in-house, contracted, or external commercial projects where NASA is providing some evaluation). Ideally, software assurance for external commercial projects should follow these practices also.

The audit metrics that are tracked and reported on will depend on the specific metrics chosen by the audit team. The Audit Team may be from a project, an independent 3rd party auditors for commercial ventures, or organization. The audit team must select or develop the audit metrics that best reflect the goals of audit to be performed. Organizations or projects may have a pre-defined set of metrics making the selection process straight forward. Typically, only a few audit metrics are selected, as the most important things to come out of an audit are the findings and observations themselves.

Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) provides a list of potential metrics including audit metrics that could be selected for specific requirements and are sorted by the type of metrics they support (e.g., Peer Review Process Audits, Compliance Audits). This is not an exhaustive list and may not cover all of the possible audit metrics that need to be collected and reported.

When selecting metrics, the audit team may want to look at the data from different aspects. Selecting a few high-level metrics will provide overall status information. Some of these should be chosen to give the management team a quick view of the “state of the project,” or the “state of the Software Assurance work” being done. A couple of examples high-level audit metrics are:

* # of audits performed vs. # of audits planned
* # of Open vs. Closed Audit Non-Conformances over time

Selecting a few low-level metrics will attest to the quality of the work that was performed. The lower-level metrics should be chosen to give the management team insight into how well the projects and organizations are following the NASA requirements and standards as well as their organizational and project processes and procedures. A couple of examples of low-level requirements are:

* # of Non-Conformances identified in the CM Plan
* # of audit Non-Conformances per peer review audit

Some metrics examples that could be chosen:

## 3.1 Audits of Software Assurance:

* # of audits performed versus # of audits planned
* # of Peer Review Audits planned vs. # of Peer Review Audits performed
* # of Compliance Audits planned vs. # of Compliance Audits performed
* Trends on non-conformances from audits (Open, Closed, life cycle Phase)
* Time required to close audit Non-Conformances
* Preparation time each audit participant spent preparing for audit

## 3.2 Peer Review Process Audit Metrics:

* # of audit Non-Conformances per Peer Review Audit
* # of audit Observations per Peer Review Audit
* # of Peer Review Audits planned vs. # of Peer Review Audits performed
* Trends on non-conformances from audits (Open, Closed, Life cycle Phase)
* Time required to close Peer Review Audit Non-Conformances
* Preparation time each audit participant spent preparing for audit

## 3.3 Compliance Audit Metrics:

* # of Compliance Audits planned vs. # of Compliance Audits performed
* # of Open vs. Closed Audit Non-Conformances over time
* Trends of # of Non-Conformances from audits over time (Include counts from process and standards audits and work product audits.)
* # of Non-Conformances identified in plans (e.g., SMPs, SDPs, CM Plans, SA Plans, Safety Plans, Test Plans)
* # of Non-Conformances identified in the software Configuration Management Plan
  + Trends of # Open vs. # Closed over time
* # of Configuration Management Audits conducted by the project – Planned vs. Actual
* # of Non-Conformances per audit (including findings from process and compliance audits, process maturity)
* # of process Non-Conformances (e.g., activities not performed) identified vs. # accepted by the project
  + Trends of # Open vs. # Closed over time"
* # of process Non-Conformances in the Risk Management process identified

## 3.4 Project health and status based on Audit metrics:

* # of process Non-Conformances (e.g., activities not performed) identified vs. # accepted by the project
* # of Compliance Audits planned vs. # of Compliance Audits performed
* # of Open vs. Closed Audit Non-Conformances over time
* Trends of # of Non-Conformances from audits over time (Include counts from process and standards audits and work product audits.)

## 3.5 SA value in Peer Reviews:

* How many non-conformances have been found in each peer review? # of non-conformances found in each peer review
* # of non-conformances found by SA
* # of non-conformances accepted by the project
* Trend of open non-conformances vs closed non-conformances over time (SA analysis of trends could show project problems if # of closed non-conformances continue to lag further and further behind # of open non-conformances

## 3.6 Observations of Project status based on Audit metrics:

* # of process Non-Conformances (e.g., activities not performed) identified by SA vs. # accepted by the project
* # of Compliance Audits planned vs. # of Compliance Audits performed
* # of Open vs. Closed Audit Non-Conformances over time
* Trends of # of Non-Conformances from audits over time (Include counts from process and standards audits and work product audits.)

## 3.7 Safety issues and non-conformances:

* # of safety related-requirements issues (over time, open, closed)
* # of safety-related non-conformances identified by life cycle phase (over time, open, closed)

## 3.8 Display Data With Charts

Simple charts are a good way to show the data for discussion when reporting status. Some simple examples are below:

## 3.9  Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 4. Audit and Assessment Schedules

Software Assurance is required to perform audits on software development and software assurances processes along with performing assessments on the software work products. A schedule establishes when audits and assessments will be performed within a specified timeframe for a single project, all projects, or a program. The software development processes and practices are required to be audited at least once every two years, which means auditing a project to ensure that the project follows defined processes and procedures for deliverable software products. Assessments should be performed on each work product that the development team produces. Audits and assessments may be triggered by project milestones, changes in governing documents (e.g., a new version of an applicable standard is released, and the project has a specified timeframe by which to comply), major staffing changes, or identification of a major defect. Auditors may choose to conduct the audits all at once or throughout the life cycle as it is being executed. For example, create a schedule to audit all areas of a project’s software development plan over a year so that at the end of the year, all areas of the software development plan have been audited. It is recommended that the work product assessments be performed as the work products are being completed or baselined.

The tables below provides the recommended schedule for Software Assurance to use when conducting the software engineering process/procedure audits and work product assessments prescribed in NPR 7150.2 and NASA-STD-8739.8. The green blocks represent the recommended milestone where it is optimal to conduct the audit or assessment. If the audit or assessment cannot be conducted during the recommended time frame, the yellow blocks indicate a good secondary time frame.

## 4.1 Software Assurance Process Audits Schedule

This schedule may be used to help plan for Process Compliance Audits in phases A through D in your project.

| **Audits /  **Systems Engineering** Phase** | **Pre-**Phase** A** | **Phase A** | | | | **Phase B** | **Phase C** | | | **Phase D** | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **SA Process Compliance Audits** | MCR | SRR | SwRR | MDR | SDR | PDR | CDR | SIR | TRR | SAR | ORR |
| Software Project Planning |  |  |  |  |  |  |  |  |  |  |  |
| Software Project Management |  |  |  |  |  |  |  |  |  |  |  |
| Software Configuration Management \* |  |  |  |  |  | Implementation Audit |  |  | FCA | Implementation Audit | PCA |
| Software Requirements \* |  |  |  |  |  |  |  |  |  |  |  |
| Software Design |  |  |  |  |  | Architecture Audit | Detailed  Design Audit |  |  |  |  |
| Software Implementation or Coding |  |  |  |  |  |  |  |  |  |  |  |
| Software Testing \* |  |  |  |  |  |  |  |  |  |  |  |
| Software Hazard Development |  |  |  |  |  |  |  |  |  |  |  |
| Software Defects Tracking \* |  |  |  |  |  |  |  |  |  |  |  |
| Risk Management |  |  |  |  |  |  | Implementation Audit |  |  |  |  |
| Software Peer Reviews & Inspections |  |  |  |  |  |  |  |  |  |  |  |
| Software Operations Maintenance & Retirement |  |  |  |  |  |  |  |  |  |  |  |
| Number of Audits per Milestone: | 0 | 0 | 1 | 1 | 0 | 4 | 3 | 1 | 2 | 2 | 1 |

Legend: 

|  |  |
| --- | --- |
| Primary recommended time period for SA audit |  |
| Secondary recommended time period for SA audit |  |

\*Minimum audits to be performed

## 4.2 Software Assurance Process Assessment Schedule

This schedule may be used to help plan for Software Engineering Work Product Assessments in phases A through D in your project. 

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Assessments / Systems Engineering Phase** | **Pre-Phase A** | **Phase A** | | | | **Phase B** | **Phase C** | | | **Phase D** | |
| **Software Assurance Work Product Assessments** | **MCR** | **SRR** | **SwRR** | **MDR** | **SDR** | **PDR** | **CDR** | **SIR** | **TRR** | **SAR** | **ORR** |
| Architecture and Detailed Design Assessment |  |  |  |  |  | **S** | **P** |  |  |  |  |
| Interface Design Description Assessment |  |  |  |  |  | **S** | **P** |  |  |  |  |
| IVV Project Execution Plan Assessment |  | **S** |  | **P** | **S** |  |  |  |  |  |  |
| Risk Management Plan Assessment |  | **P** |  | **S** |  |  |  |  |  |  |  |
| Software Assurance Plan Assessment |  |  |  | **S** | **P** |  |  |  |  |  |  |
| Software Assurance Reqts Mapping Matrix Assessment |  | **P** | **P** | **S** |  |  |  |  |  |  |  |
| Software Change Request Problem Report Assessment |  |  |  |  | **S** | **P** | **S** |  |  |  |  |
| Software Configuration Management Plan Assessment |  |  |  | **S** | **P** | **S** |  |  |  |  |  |
| Software Data Dictionary Assessment |  |  |  |  |  | **S** | **P** |  |  |  |  |
| Software Development Management Plan Assessment |  |  | **P** | **S** |  |  |  |  |  |  |  |
| Software Engineering Reqts Mapping Matrix Assessment |  | **P** | **P** | **S** |  |  |  |  |  |  |  |
| Software Maintenance Plan Assessment |  |  |  |  |  |  |  |  |  | **P** | **S** |
| Software Requirements Specification Assessment |  |  | **P** | **S** |  |  |  |  |  |  |  |
| Software Test Plan Assessment |  |  |  |  |  |  | **P** | **S** |  |  |  |
| Software Test Procedures Assessment |  |  |  |  |  |  |  | **S** | **P** |  |  |
| Software Test Report Assessment |  |  |  |  |  |  |  |  |  | **P** | **S** |
| Software Training Plan Assessment |  | **P** |  | **S** |  |  |  |  |  |  |  |
| Software User Manual Assessment |  |  |  |  |  |  |  |  | **S** | **P** | **S** |
| Software Version Description Assessment |  |  |  |  |  |  |  |  | **S** | **P** | **S** |
| Number of Assessments per Milestone: | 0 | 4 | 4 | 1 | 2 | 2 | 5 | 0 | 1 | 4 | 0 |

### Legend:

|  |  |
| --- | --- |
| Primary recommended time period for SA audit | **P** |
| Secondary recommended time period for SA audit | **S** |

## 4.3 Minimum Required Audits

There are 4 process/procedure area audits that must be performed:

1. Software Configuration Management – This includes:
   1. Performing audits for all deliveries per the configuration management processes to verify that all products are being delivered and are the correct versions.
   2. Performing an audit against the configuration management procedures to confirm that the project follows the established procedures.
   3. Confirming that the project manager performed software configuration audits to determine the correct version of the software configuration items and verify that the results of the audit conform to the records that define them.
2. Software Requirements
3. Software Testing
4. Software Defects Tracking

Software Engineering Work Product audits should be conducted in-phase with the appropriate milestone review.

All other audits are at the discretion of the project but should be performed. The project’s Requirements Mapping Matrix should reflect which audits are being tailored.

Note: No audits are required for Class E software unless audits are used to assess whether a requirement has been implemented.

# 5. Audit & Assessment Checklists

## 5.1 Audit Checklists for SWE Requirement Compliance

Click on a link to download a usable copy of the template. (AudCK)

**Audit Checklists Process Asset Templates - Full Details**

* (PAT-036 - )

  [PAT-036 Software Architecture and Design Process Audit](https://swehb.nasa.gov/download/attachments/198770701/PAT-036%20-%20Architecture%20and%20Design%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Architecture and Design. SWE-027, SWE-052, SWE-057, SWE-058, SWE-087, SWE-088, SWE-089, SWE-134, SWE-143, SWE-157, Topic 8.12, Topic 8.59, AudCK, DesAn, SATask,
* (PAT-037 - )

  [PAT-037 - Configuration Management Process Audit](https://swehb.nasa.gov/download/attachments/198770725/PAT-037%20-%20Configuration%20Management%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Configuration Management Process. This PAT replaces PAT-001 - FCA and PAT-002 - PCA. SWE-063, SWE-065, SWE-077, SWE-079, SWE-080, SWE-081, SWE-082, SWE-083, SWE-084, SWE-085, SWE-187, SWE-193, Topic 8.12, Topic 8.59, CM, A.08, AudCK, ChgMgmt, CM, RelDel, SATask,
* (PAT-038 - )

  [PAT-038 - Implementation Process Audit](https://swehb.nasa.gov/download/attachments/198770739/PAT-038%20-%20Implementation%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Implementation Process. SWE-023, SWE-027, SWE-042, SWE-052, SWE-060, SWE-061, SWE-062, SWE-065, SWE-080, SWE-087, SWE-088, SWE-089, SWE-134, SWE-135, SWE-136, SWE-156, SWE-157, SWE-159, SWE-186, SWE-190, SWE-207, SWE-219, SWE-220, Topic 8.12, Topic 8.59, AudCK, Impl, SATask,
* (PAT-039 - )

  [PAT-039 - Operations, Maintenance, & Retirement Process Audit](https://swehb.nasa.gov/download/attachments/198770753/PAT-039%20-%20Operations%2C%20Maintenance%2C%20%26%20Retirement%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Operations, Maintenance, & Retirement Process. SWE-013, SWE-032, SWE-075, SWE-087, SWE-088, SWE-089, SWE-195, SWE-196, Topic 8.12, Topic 8.59, AudCK, MaOps, Plng, SATask,
* (PAT-040 - )

  [PAT-040 - Project Management Process Audit](https://swehb.nasa.gov/download/attachments/198770755/PAT-040%20-%20Project%20Management%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Project Management Process. SWE-013, SWE-017, SWE-018, SWE-022, SWE-027, SWE-032, SWE-036, SWE-037, SWE-039, SWE-040, SWE-045, SWE-054, SWE-075, SWE-080, SWE-086, SWE-087, SWE-088, SWE-089, SWE-090, SWE-093, SWE-094, SWE-125, SWE-139, SWE-141, SWE-146, SWE-148, SWE-154, SWE-156, SWE-176, SWE-178, SWE-179, SWE-189, SWE-191, SWE-194, SWE-195, SWE-199, SWE-200, SWE-201, SWE-202, SWE-203, SWE-204, SWE-205, SWE-206, Topic 8.12, Topic 8.59, AudCK, Plng, SATask,
* (PAT-041 - )

  [PAT-041 - Project Planning Process Audit](https://swehb.nasa.gov/download/attachments/198770757/PAT-041%20-%20Project%20Planning%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Project Planning Process. SWE-013, SWE-015, SWE-016, SWE-017, SWE-020, SWE-024, SWE-027, SWE-032, SWE-033, SWE-034, SWE-036, SWE-037, SWE-061, SWE-075, SWE-079, SWE-080, SWE-087, SWE-088, SWE-089, SWE-090, SWE-121, SWE-131, SWE-147, SWE-151, SWE-154, SWE-174, SWE-191, SWE-202, SWE-205, SWE-207, Topic 8.12, Topic 8.59, AudCK, Plng, SATask,
* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management. SWE-027, SWE-033, SWE-050, SWE-051, SWE-052, SWE-053, SWE-054, SWE-080, SWE-087, SWE-088, SWE-089, SWE-134, SWE-157, SWE-184, SWE-194, SWE-200, SWE-205, SWE-210, Topic 5.09, Topic 8.12, Topic 8.59, AudCK, ChgMgmt, ReqAn, SATask,
* (PAT-043 - )

  [PAT-043 - Software Defects & Tracking Process Audit](https://swehb.nasa.gov/download/attachments/198770761/PAT-043%20-%20Software%20Defects%20%26%20Tracking%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Defects & Tracking Process. SWE-018, SWE-024, SWE-039, SWE-045, SWE-062, SWE-065, SWE-068, SWE-088, SWE-191, SWE-194, SWE-201, SWE-202, SWE-203, SWE-204, Topic 8.12, Topic 8.59, AudCK, ChgMgmt, SATask,
* (PAT-044 - )

  [PAT-044 - Software Hazard Development Process Audit](https://swehb.nasa.gov/download/attachments/198770763/PAT-044%20-%20Software%20Hazard%20Development%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Hazard Development Process. SWE-023, SWE-052, SWE-065, SWE-066, SWE-068, SWE-071, SWE-081, SWE-087, SWE-134, SWE-184, SWE-192, SWE-193, SWE-205, SWE-219, SWE-220, Topic 8.12, Topic 8.59, AudCK, Haz, SATask, SftySp,
* (PAT-045 - )

  [PAT-045 - Software Peer Review Inspection Report Audit](https://swehb.nasa.gov/download/attachments/198770772/PAT-045%20-%20Software%20Peer%20Review%20Inspection%20Report%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Peer Review Inspection Report Process. SWE-039, SWE-087, SWE-088, SWE-089, SWE-134, SWE-143, Topic 8.12, Topic 8.59, AudCK, PRvw, SATask,
* (PAT-046 - )

  [PAT-046 - Test Verification and Validation Process Audit](https://swehb.nasa.gov/download/attachments/198770767/PAT-046%20-%20Test%20Verification%20and%20Validation%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Test Verification and Validation Process. SWE-023, SWE-027, SWE-052, SWE-055, SWE-062, SWE-065, SWE-066, SWE-068, SWE-070, SWE-071, SWE-073, SWE-080, SWE-087, SWE-088, SWE-089, SWE-134, SWE-159, SWE-186, SWE-187, SWE-189, SWE-190, SWE-191, SWE-192, SWE-193, SWE-194, SWE-211, SWE-219, Topic 8.12, Topic 8.59, AudCK, SATask, TstAn, TstDoc,

## 5.2 Assessment Checklists for SWE Work Products

Click on a link to download a usable copy of the template. (AsmtCK)

**Assessment Checklists Process Asset Templates - Full Details**

* (PAT-047 - )

  [PAT-047 - Architecture and Detailed Design Assessment](https://swehb.nasa.gov/download/attachments/198770765/PAT-047%20-%20Architecture%20and%20Detailed%20Design%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Architecture and Detailed Design in the Software Design Description document. Based on the minimum recommended content for a Software Design Description. SWE-039, SWE-052, SWE-057, SWE-058, SWE-087, SWE-143, Topic 7.08, Topic 8.59, AsmtCK, DesAn, PRvw, SATask,
* (PAT-048 - )

  [PAT-048 - Interface Design Description Assessment](https://swehb.nasa.gov/download/attachments/198770866/PAT-048%20-%20Interface%20Design%20Description%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Interface Design Description document. Based on the minimum recommended content for an Interface Design Description. SWE-039, SWE-057, SWE-058, SWE-087, SWE-143, Topic 7.08, Topic 8.59, AsmtCK, DesAn, PRvw, SATask,
* (PAT-049 - )

  [PAT-049 - IVV Project Execution Plan Assessment](https://swehb.nasa.gov/download/attachments/198770869/PAT-049%20-%20IVV%20Project%20Execution%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the IV&V Project Execution Plan document. Based on the minimum recommended content for an IV&V Project Execution Plan. SWE-022, SWE-039, SWE-087, SWE-131, SWE-141, SWE-178, SWE-179, Topic 7.08, Topic 8.59, AsmtCK, PRvw, Plng, SATask,
* (PAT-050 - )

  [PAT-050 - Risk Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770872/PAT-050%20-%20Risk%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Risk Management Plan. Based on the content requirements established by NPR 8000.4C. SWE-039, SWE-086, SWE-087, SWE-154, SWE-156, SWE-179, Topic 7.08, Topic 7.19, Topic 8.59, AsmtCK, PRvw, Plng, RskMgmt, SATask,
* (PAT-051 - )

  [PAT-051 - Software Assurance Plan Assessment](https://swehb.nasa.gov/download/attachments/198770874/PAT-051%20-%20Software%20Assurance%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Assurance Plan. Based on the minimum recommended content for a Software Assurance Plan. SWE-013, SWE-016, SWE-017, SWE-022, SWE-036, SWE-039, SWE-087, SWE-121, SWE-174, SWE-176, Topic 7.08, Topic 8.59, AsmtCK, PRvw, Plng, SATask,
* (PAT-052 - )

  [PAT-052 - Software Assurance Reqts Mapping Matrix Assessment](https://swehb.nasa.gov/download/attachments/198770876/PAT-052%20-%20Software%20Assurance%20Reqts%20Mapping%20Matrix%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Assurance Requirements Mapping Matrix. Based on the minimum recommended content for a Software Assurance Requirements Mapping Matrix. SWE-039, SWE-121, SWE-125, SWE-126, SWE-152, SWE-176, SWE-212, Topic 7.08, Topic 8.59, AsmtCK, PRvw, Plng, SATask,
* (PAT-053 - )

  [PAT-053 - Software Change Request Problem Report Assessment](https://swehb.nasa.gov/download/attachments/198770878/PAT-053%20-%20Software%20Change%20Request%20Problem%20Report%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Change Request - Problem Report. Based on the minimum recommended content for a Software Change Request - Problem Report. SWE-039, SWE-086, Topic 7.08, Topic 8.59, AsmtCK, ChgMgmt, PRvw, SATask,
* (PAT-054 - )

  [PAT-054 - Software Configuration Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770880/PAT-054%20-%20Software%20Configuration%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Configuration Management Plan. Based on the minimum recommended content for a Software Configuration Management Plan. SWE-039, SWE-079, SWE-082, SWE-085, SWE-087, SWE-146, Topic 7.08, Topic 8.59, AsmtCK, ChgMgmt, CM, PRvw, Plng, SATask,
* (PAT-055 - )

  [PAT-055 - Software Data Dictionary Assessment](https://swehb.nasa.gov/download/attachments/198770882/PAT-055%20-%20Software%20Data%20Dictionary%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Data Dictionary. Based on the minimum recommended content for a Software Data Dictionary. SWE-039, SWE-050, SWE-057, SWE-058, SWE-087, Topic 7.08, Topic 8.59, AsmtCK, DesAn, PRvw, SATask,
* (PAT-056 - )

  [PAT-056 - Software Development Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770884/PAT-056%20-%20Software%20Development%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Development - Management Plan. Based on the minimum recommended content for a Software Development - Management Plan. SWE-005, SWE-006, SWE-013, SWE-015, SWE-016, SWE-017, SWE-018, SWE-020, SWE-023, SWE-024, SWE-027, SWE-033, SWE-034, SWE-036, SWE-039, SWE-046, SWE-050, SWE-051, SWE-053, SWE-055, SWE-061, SWE-062, SWE-066, SWE-068, SWE-071, SWE-073, SWE-075, SWE-079, SWE-080, SWE-082, SWE-085, SWE-086, SWE-087, SWE-088, SWE-089, SWE-090, SWE-091, SWE-093, SWE-121, SWE-125, SWE-126, SWE-151, SWE-153, SWE-156, SWE-159, SWE-174, SWE-176, SWE-184, SWE-185, SWE-187, SWE-192, SWE-194, SWE-195, SWE-199, SWE-202, SWE-203, SWE-205, SWE-210, SWE-211, SWE-214, SWE-217, Topic 5.11, Topic 5.14, Topic 7.03, Topic 7.05, Topic 7.08, Topic 8.59, AsmtCK, PRvw, Plng, SATask,
* (PAT-057 - )

  [PAT-057 - Software Engineering Reqts Mapping Matrix Assessment](https://swehb.nasa.gov/download/attachments/198770886/PAT-057%20-%20Software%20Engineering%20Reqts%20Mapping%20Matrix%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Engineering Requirements Mapping Matrix. Based on the minimum recommended content for a Software Engineering Requirements Mapping Matrix. SWE-039, SWE-121, SWE-125, SWE-126, SWE-150, SWE-152, SWE-176, SWE-212, Topic 7.08, Topic 5.09, Topic 8.59, AsmtCK, PRvw, Plng, SATask,
* (PAT-058 - )

  [PAT-058 - Software Maintenance Plan Assessment](https://swehb.nasa.gov/download/attachments/198770888/PAT-058%20-%20Software%20Maintenance%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Maintenance Plan. Based on the minimum recommended content for a Software Maintenance Plan. SWE-036, SWE-039, SWE-075, SWE-085, SWE-087, SWE-136, SWE-195, SWE-196, Topic 7.08, Topic 8.59, AsmtCK, MaOps, PRvw, Plng, SATask,
* (PAT-059 - )

  [PAT-059 - Software Requirements Specification Assessment](https://swehb.nasa.gov/download/attachments/198770890/PAT-059%20-%20Software%20Requirements%20Specification%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Requirements Specification. Based on the minimum recommended content for a Software Requirements Specification. SWE-027, SWE-039, SWE-050, SWE-052, SWE-087, SWE-184, SWE-192, Topic 5.09, Topic 7.08, Topic 8.59, AsmtCK, PRvw, ReqAn, SATask, SRS,
* (PAT-060 - )

  [PAT-060 - Software Test Plan Assessment](https://swehb.nasa.gov/download/attachments/198770892/PAT-060%20-%20Software%20Test%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Test Plan. Based on the minimum recommended content for a Software Test Plan. SWE-039, SWE-065, SWE-071, SWE-087, SWE-191, Topic 7.08, Topic 8.59, AsmtCK, PRvw, SATask, TstAn, TstDoc,
* (PAT-061 - )

  [PAT-061 - Software Test Procedures Assessment](https://swehb.nasa.gov/download/attachments/198770894/PAT-061%20-%20Software%20Test%20Procedures%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Test Procedures document. Based on the minimum recommended content for a Software Test Procedures. SWE-039, SWE-052, SWE-065, SWE-066, SWE-071, SWE-087, SWE-191, SWE-192, SWE-193, SWE-211, Topic 7.08, Topic 8.59, AsmtCK, PRvw, SATask, TstAn, TstDoc,
* (PAT-062 - )

  [PAT-062 - Software Test Report Assessment](https://swehb.nasa.gov/download/attachments/198770896/PAT-062%20-%20Software%20Test%20Report%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Test Report document. Based on the minimum recommended content for a Software Test Report. SWE-039, SWE-052, SWE-065, SWE-068, SWE-073, SWE-087, Topic 7.08, Topic 8.59, AsmtCK, PRvw, SATask, TstAn, TstDoc,
* (PAT-063 - )

  [PAT-063 - Software Training Plan Assessment](https://swehb.nasa.gov/download/attachments/198770898/PAT-063%20-%20Software%20Training%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Training Plan document. Based on the minimum recommended content for a Software Training Plan. SWE-017, SWE-039, SWE-087, SWE-100, SWE-222, Topic 7.08, Topic 8.59, AsmtCK, PRvw, Plng, SATask,
* (PAT-064 - )

  [PAT-064 - Software User Manual Assessment](https://swehb.nasa.gov/download/attachments/198770900/PAT-064%20-%20Software%20User%20Manual%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software User Manual. Based on the minimum recommended content for a Software User Manual. SWE-039, Topic 7.08, Topic 8.59, AsmtCK, PRvw, SATask,
* (PAT-065 - )

  [PAT-065 - Software Version Description Assessment](https://swehb.nasa.gov/download/attachments/198770902/PAT-065%20-%20Software%20Version%20Description%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Version Description Document. Based on the minimum recommended content for a Version Description Document. SWE-039, SWE-063, SWE-087, Topic 7.08, Topic 8.59, AsmtCK, CM, PRvw, RelDel, SATask,

## 5.3 Other Audit and Assessment Checklists

-- Under construction

# 6. Small Project Audits

Projects with small budgets or limited personnel may need to strategically optimize the types and number of audits conducted. Here are some potential solutions on how to do that:

* Limit the number of process audits. At a minimum, perform the minimum require audits that are prescribed by this topic (See the [Audit Schedules](#tabs-4) on Tab 4 - Audit Schedules)
* Instead of maintaining a separate tracking system/database for audit findings, enter the findings in the project’s defect tracking system.
  + The tracking system could be the project’s defect database or as simple as adding an inline comment to a Confluence page that logs change traffic.
* Perform informal audits versus the more rigorous formal audits.
* Audit team may be comprised of one person, but that person should not be the person who performed the activities being audited.

# 7. Audit or Assessment Report Content

Audit results should be reported in a high-level summary and conveyed as part of an outbrief or weekly/monthly SA Status Reports. The high-level summary should provide an overall evaluation of the audit, any associated risks, and thoughts on the health and status of the project or organization audited.

When an audit is conducted, it may be necessary to provide a formal or detailed report of the results to the management team outside of the normal status reporting cycle. This will allow the management team to prioritize and delegate the necessary corrections. If a time-critical issue is uncovered, it should be reported to management immediately so that the affected organization may begin addressing it at once.

Although left to the discretion of the Audit Team, audit reports are comprised of one or more of the following types. Guidance is provided for selecting which type of Audit Report to write:

* Audit Report Summary – An audit summary should be written for all types of audits.

+ For work product compliance assessments/audits, this summary may be included as part of a normal SA Status Report.
+ For Detailed Audit Reports or Formal Audit Report, this summary should be a standalone independent presentation package that may be used for an audit outbrief.

* Detailed Audit Report – It may be necessary to write a detailed audit report depending on who or what is being audited. Any comprehensive audit of an internal project or entity should write this type of report. Examples include Configuration Management audit, process/procedure audit, compliance audit.
* Formal Audit Report – It may be necessary to write a formal audit report depending on who or what is being audited. Any comprehensive audit of an external entity (e.g., contractors, other NASA organizations, commercial crew) should write this type of report. Examples include audits of software development processes and practices that occur at least once every two years, internal CMMI audits, internal ISO audits.

When a project has safety-critical software, audits results should be shared with the Software Safety personnel. The results of audits conducted by Software Assurance personnel and those done by Software Safety personnel may be combined into one report, if desired.

Per SWE-201 – SASS Task 1 and SWE-039 – SASS Task 8, all audit findings and observations are documented in a problem/issue tracking system and tracked to closure. These items are communicated to the affected organization’s personnel and possible solutions discussed.

## 6.1 Minimum Recommended Content for Audit Summary

When reporting the results of an audit for a SA Status Report, the following defines the minimum recommended content:

1. **Identification**– Identify the specific project (Mission/Project/Application), project processes (e.g., Peer Review, change management, PCA/FCA), and artifacts that were audited.
2. **Group Audited** – Identify the group or department (Branch, Division, Project or subset, etc.) being audited. If necessary, include a list of roles that were audited.
3. **Overall** **Summary** – Overall evaluation of audit subject, based on audit observations/results. Capture and share any overall impressions, observations, etc. for the project, both good and bad. Include thoughts on the health and status of the project or organization audited.
4. **Major findings and associated risk** – The detailed reporting should include where the finding was discovered and an estimate of the amount of risk involved with the finding. Major findings are major non-conformance or non-compliance with requirement or process or collection of minor non-conformances that indicate systemic issue; a major or total breakdown of a process; or not meeting a requirement.
5. **Observations** – Positive and negative observations that are not non-conformances or a potential non-compliance outside the scope of the current audit; positive observations are observations that contribute to quality; negative observations are observations that detract from the quality and if not addressed could be non-compliances in the future. This should include important observations such as any systemic issues, Best Practices, and areas of concern.
6. **Opportunities for Improvement (OFI) (Optional)** – Recommendations that would improve compliance to a higher level of quality or to a suggested best practice.
7. **Status of Actions, Next Steps, and Due Dates** – Current status of findings and actions: open/closed; projection for closure timeframe; dates for any follow-up meetings planned. If also writing a Formal or Detailed Audit Report include:
   1. Audit report generation and delivery – the audit team, typically delivered the official set of audit results to the project 2 weeks to 30 days after the audit ends.
   2. Timeframe for audit report response – the due date for the project to respond to the audit report with their feedback and/or plan to address any Findings; this could be 30 days after the project receives the official audit report.
   3. Additional evidence due from the project – if during the audit the project agreed to provide additional evidence (screenshots, copies of records not accessible to the audit team, etc.), list those items, the audit team point-of-contact (typically, the Lead Auditor), and relevant due dates.
8. **Metrics (Optional)** – Include metrics charts showing other details of audit findings.

## 6.2 Minimum Recommended Content for Detailed Audit Report

When reporting the detailed results of an audit, the following defines the minimum recommended content:

1. **Identification**– Identify the specific project (Mission/Project/Application), project processes (e.g., Peer Review, change management, PCA/FCA), and artifacts that were audited.
2. **Auditor Name** – Identify the person or group doing audit(s)
3. **Audit Date(s)** – Period/Timeframe/Phase during which the audit was performed
4. **Governing** **Documents** – Identify the documents or processes used in the audit (e.g., requirements version, etc.)
5. **Group** **Audited** – Identify the group or department (Branch, Division, Project or subset, etc.) being audited. If necessary, include a list of roles that were audited.
6. **Techniques and Methods** – Description of methods and techniques used to perform the audit (Checklists, interviews, comparisons, etc.)
7. **Overall** **Summary** – Overall evaluation of audit subject, based on audit observations/results. Capture and share any overall impressions, observations, etc. for the project, both good and bad. Include thoughts on the health and status of the project or organization audited.
8. **Major findings and associated risk** – The detailed reporting should include where the finding was discovered and an estimate of the amount of risk involved with the finding. Major findings are major non-conformance or non-compliance with requirement or process or collection of minor non-conformances that indicate systemic issue; a major or total breakdown of a process; or not meeting a requirement. List the relevant governing document requirement with each Finding, preferably the full text and reference to its location in the governing document.
9. **Minor findings** – Minor non-conformance or partial non-compliance; isolated or single part of a requirement not being met; roll up minor Findings into a single Finding, e.g., not in compliance with configuration management (CM) control vs. a long list of minor CM Findings. List the relevant governing document requirement with each Finding, preferably the full text and reference to its location in the governing document.
10. **Observations** – Positive and negative observations that are not non-conformances or a potential non-compliance outside the scope of the current audit; positive observations are observations that contribute to quality; negative observations are observations that detract from the quality and if not addressed could be non-compliances in the future. This should include important observations such as any systemic issues, Best Practices, and areas of concern.
11. **Opportunities for Improvement (OFI)** – Recommendations that would improve compliance to a higher level of quality or to a suggested best practice.
12. **Status of Actions, Next Steps, and Due Dates** – Current status of findings and actions: open/closed; projection for closure timeframe; dates for any follow-up meetings planned
13. **Current status of findings**: open/closed; projection for closure timeframe
14. **Metrics (Optional)** – Include metrics charts showing other details of audit findings.

## 6.3 Minimum Recommended Content for a Formal Audit Report

When reporting the detailed results of an audit to an external entity, a more formal report is warranted. The following defines the minimum recommended content:

1. **Confidentiality Statement** – Depending on the nature and ownership of the material assessed during the audit, any project contracts in place, etc. the audit report may be restricted to specific audiences or require a statement of confidentiality regarding the results it contains. The Lead Auditor makes this determination and ensures the audit report contains the necessary statements and access restrictions. If the audit team assessed several companies within a project, there might be company-confidential processes or information involved. Also, in the case of multiple companies, the audit team may not want to put company-specific audit results out publicly where they can be used for comparisons.
2. **Purpose, Scope, Schedule, and Governing Documents** – These sections of the report reflect the audit plan and serve as the official record of what was audited, for what purpose, and the audit timeframe. The audit notification (see Audit Notification in this guidance) is a good source for this information but be sure the audit report content reflects any adjustments made during the audit.
3. **Personnel** – List the auditors, auditees, other attendees as captured in the Documentarian/Recorder record of the audit. Depending on the audit report audience, it may be necessary only to capture key personnel and not every person who participated in the audit.  The Documentarian/Recorder notes from the audit will include the full list of participants, so the audit report may include only key participants.
4. **Governing documents** – List by name and version the documents serving as the basis of the audit criteria, e.g., software development plans, standards.
5. **Assumptions, qualifications** – Audits are sampling activities, so it is important to identify any assumptions and qualifications made when generating Findings and Observations. Assumptions could include the number of samples taken given the full number of records available, the time available to conduct an interview or witness an activity, the availability of key personnel during the audit, etc.  These caveats impact the audit results, and so are important to list in the report.
6. **Overall Summary** – Provide a statement or paragraph regarding the overall compliance of the project with the governing documents, or specific sections thereof, used for this audit.
7. **Results** – List in clear statements, the Findings, Observations, Opportunities for Improvement (OFI) in that order with major Findings first. List the relevant governing document requirement with each Finding, preferably the full text and reference to its location in the governing document.  Stick to the facts – what was heard, seen, collected, or not able to be seen, heard, or collected (i.e., no objective evidence could be found).  A good set of working definitions for audit results are listed below.
8. **Major Findings** – Major non-conformance or non-compliance with requirement or process or collection of minor non-conformances that indicate systemic issue (see also ISO 1021-1:2015E and AS9101TMF); a major or total breakdown of a process; or not meeting a requirement. List the relevant governing document requirement with each Finding, preferably the full text and reference to its location in the governing document.
9. **Minor Findings** – Minor non-conformance or partial non-compliance (see also ISO 1021-1:2015E and AS9101TMF); isolated or single part of a requirement not being met; roll up minor Findings into a single Finding,g., not in compliance with configuration management (CM) control vs. a long list of minor CM Findings. List the relevant governing document requirement with each Finding, preferably the full text and reference to its location in the governing document.
10. **Observations** – Positive and negative observations that are not non-conformances or a potential non-compliance outside the scope of the current audit; positive observations are observations that contribute to quality; negative observations are observations that detract from the quality and if not addressed could be non-compliances in the future. This should include important observations such as any systemic issues, Best Practices, and areas of concern.
11. **Opportunities for Improvement (OFI)** – Recommendations that would improve compliance to a higher level of quality or to a suggested best practice.
12. **Status of Actions, Next Steps, and Due Dates** – List any actions and next steps relevant to the delivery of the audit report with appropriate due dates. Consider the following:
    * The date for a formal review of the audit report with the project.
    * Dates Corrective Actions are due to the project for the findings.
    * Dates for any follow-up meetings planned, perhaps to review Corrective Action status.

# 8. Resources

## 8.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 8.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 8.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-045 - Project Participation in Audits](/spaces/SWEHBVD/pages/102695419/SWE-045+-+Project+Participation+in+Audits) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase)        * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [5.25 - Audit Report Minimum Content](/spaces/SWEHBVD/pages/140641711/5.25+-+Audit+Report+Minimum+Content) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-036 - Architecture and Design Process Audit](/spaces/SITE/pages/198770701/PAT-036+-+Architecture+and+Design+Process+Audit) * [PAT-037 - Configuration Management Process Audit](/spaces/SITE/pages/198770725/PAT-037+-+Configuration+Management+Process+Audit) * [PAT-038 - Implementation Process Audit](/spaces/SITE/pages/198770739/PAT-038+-+Implementation+Process+Audit) * [PAT-039 - Operations, Maintenance, & Retirement Process Audit](/spaces/SITE/pages/198770753/PAT-039+-+Operations+Maintenance+Retirement+Process+Audit) * [PAT-040 - Project Management Process Audit](/spaces/SITE/pages/198770755/PAT-040+-+Project+Management+Process+Audit) * [PAT-041 - Project Planning Process Audit](/spaces/SITE/pages/198770757/PAT-041+-+Project+Planning+Process+Audit) * [PAT-042 - Requirements Development and Mgmt Audit](/spaces/SITE/pages/198770759/PAT-042+-+Requirements+Development+and+Mgmt+Audit) * [PAT-043 - Software Defects & Tracking Process Audit](/spaces/SITE/pages/198770761/PAT-043+-+Software+Defects+Tracking+Process+Audit) * [PAT-044 - Software Hazard Development Process Audit](/spaces/SITE/pages/198770763/PAT-044+-+Software+Hazard+Development+Process+Audit) * [PAT-045 - Software Peer Review Inspection Report Audit](/spaces/SITE/pages/198770772/PAT-045+-+Software+Peer+Review+Inspection+Report+Audit) * [PAT-046 - Test Verification and Validation Process Audit](/spaces/SITE/pages/198770767/PAT-046+-+Test+Verification+and+Validation+Process+Audit) |

## 8.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>8</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Software Quality Assurance](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Software+Quality+Assurance) |

## 8.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
