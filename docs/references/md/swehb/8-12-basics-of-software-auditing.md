# 8.12 - Basics of Software Auditing

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695731. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing

8.12 - Basics of Software Auditing

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695731)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695731&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Planning](#tabs-2)
* [3. Conducting](#tabs-3)
* [4. Follow-up and Close-out](#tabs-4)
* [5. Audit Checklists](#tabs-5)
* [6. CMMI Practice content](#tabs-6)
* [7. Tools and Examples](#tabs-7)
* [8. Resources](#tabs-8)

# 1. Purpose

The use of this topic is to provide the basics of assessing software engineering project processes and products for compliance with an established set of criteria.  The information is useful to anyone needing to provide an independent assessment of compliance with a set of defined processes, standards, requirements, etc.

## 1.1 Basic Principles

There are a few basic principles that apply to audits, regardless of audit type or purpose.  These principles ensure objectivity in the audit conduct and outcome as well as provide the basis for an efficient audit.

|  |  |
| --- | --- |
| **Principle** | **Description** |
| Auditors are qualified | Auditors need to have knowledge of or experience with audit processes and necessary backgrounds in the audit subject matter, such as software engineering or software assurance. Qualification can be through training, on-the-job experience, a mentor-mentee relationship, or simply by including a variety of these skills on the audit team. |
| An audit is against agreed-to requirements/criteria | To get the best objective results, define the audit criteria before the project starts (i.e., the process requirements, standards, development plans, etc. to be used for the audit). The team being audited knows they are expected to follow these criteria so the audit team simply looks for evidence of that compliance. |
| Conclusions are based on the evidence | Audit results are based on and backed up by the collected evidence only. |
| The audit focuses on the project records, not the personnel | An audit is designed to assess compliance, not personalities or behavior; therefore, the auditors focus on the records, the interviews, and observations to determine the results. |

## 1.2 Basic Objectives

Audits provide management with information about the project team, the project processes and help identify best practices and areas of improvement.

Audits are useful to assess:

* Adequacy of project plans, processes, systems
* Compliance with those plans, processes, systems
* Effectiveness of those plans, processes, systems, and internal project controls on those processes
* Product fitness for use/compliance to specifications
* Areas for improvement

The results of audits allow project management to make adjustments and corrections to ensure high-quality products are being produced and delivered and that the team is functioning efficiently and effectively. Trending audit results over time allows management to identify systemic issues and areas of risk while monitoring the effect of process and product improvements.

## 1.3 Process Audits Schedule

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

# 2. Planning

The Lead Auditor manages the planning process with the audit team, once the team is identified (see Team Selection below).  This activity results in an audit plan or at least a summary of the planned audit activities that can be included in the audit notification.

If audits are not one-time or triggered by a change in governing documents, establish an overall audit plan that captures the following:

* **Audit planning** – Align audit schedules with Project activities for maximum effectiveness and efficiency; for example, a process planning audit is much more effective during the project planning phases, and a software configuration management audit is difficult if the primary configuration manager is unavailable.
* **Audit schedule** – Establish a schedule that ensures full and periodic coverage of governing documents within a specified timeframe for a single project or all projects within the auditor’s areas of responsibility. For example, establish a schedule to audit all areas of a project’s software development plan over a year so that at the end of the year, all areas of the software development plan have been audited. Other triggers for audits include project milestones, changes in governing documents (e.g., a new version of an applicable standard is released and the project has a specified timeframe by which to comply), major staffing changes, identification of a major defect. Section 1.3 shows when audits may be done in preparation for project reviews.
* **Audit criteria/checklists** – Use existing checklists or create a library of checklists to ensure full coverage of the governing documents and audit objectives for the audits on the schedule. Maintain checklists as the governing documents change; i.e., update the checklists with new revisions of their source documents. Audit checklists can take many forms, are captured in the audit records, and can be included by reference in the audit plan. See Checklist examples in the [Tools and Examples](#tabs-7) tab of this topic.
* **Audit methods** – Determine and document the techniques to be used for the scheduled audits. Interviews, observing work in progress, remote record reviews, and onsite record reviews are all valid methods for an audit, and more than one method is typically used for each audit.
* **Audit report generation and delivery** – Work with the project to determine the list of audit report recipients and how the report will be delivered (email, posted to a shared repository, printed copy delivered to the project, etc.). Capture this information in the audit plan.
* **Audit templates** – Many outputs from an audit can be generated using templates to ensure completeness and consistency. Items that lend themselves to templates include the audit notification letter, in-brief, out-brief, and the audit report. Reference any templates to be used in the audit plan.
* **Records to capture and retain** – Identify in the audit plan the records to be captured as a record of the audit. Records include:
  + Audit notification letter/email
  + Audit plan
  + Completed audit checklists
  + Audit report
  + Audit notes, including those from the in-brief and out-brief along with records of attendees and personnel interviewed
  + Audit Findings/Opportunities for Improvement (OFIs)/Observations
  + Any project evidence collected before, during, or after the audit (to close out open items)
  + Corrective action plans and closure evidence to address audit findings
* **Records repository and retention guidance** – Capture in the audit plan the location for the audit records and any applicable retention policies that apply.
* **Follow-up activities and timeframes** – Audits are not typically over once the onsite work is complete. Audit reports need to be delivered in a timely fashion. Findings need to be tracked to closure within a specified timeframe. Summary reports need to be delivered to auditor management. Capture these activities and their associated timeframes in the audit plan.
* **Global Items to review in preparation for all audits:**
  + Findings from the previous process audit
  + Process being audited
    - Has the process changed since the last process audit?
    - Are there any inconsistencies in the process (compared to other processes)?
    - Are there any ambiguous steps?
    - Is key content from the CMMI Practices present (\*see table below)
    - Are the expectations (standards) for work products in the process identified? Note: this is important because these will be used to audit the work products.
    - Are the outputs from each step (when applicable) clear?
    - Were there any process findings in the previous audit?
  + Relevant Work Instructions
  + Project Tailoring

* **Global Questions (consider using in all audits):** 
  + How does each individual being interviewed know the role(s) to which he/she is assigned (i.e., where are the roles and individuals assigned documented)?
  + Do the individuals being interviewed for the audit have sufficient resources (e.g., tools, software, equipment) to perform their work?
  + What training has the individuals being interviewed had that is relevant to the work they perform (e.g., process training, tool training, method training)?
  + How is senior management involved in the activities described in the process?
  + Was the process tailored? If so, where is the tailoring described?
  + Are there any relevant organization or project-specific work instructions?
  + Do the individuals being interviewed know how to submit information to the organization (e.g., lessons learned, best practices, process changes/improvements) and how to review the information made available by the organization?

## 2.1 Audit Scope

For every audit, establish the scope of the audit to focus the audit team and to allow the project to understand the impact the audit will have on their work. Review results from any previous audits of the organization or project to be audited to help establish the scope and focus areas to be included. Key items to consider from past audits include:

* Major non-conformances addressed as a result of the last audit
* Trends of results across a series of audits
* Lingering Findings or Observations from past audits
* Areas that narrowly passed a previous audit
* Areas not assessed during the previous audit

Capture the audit scope in the audit plan, including:

* **The audit purpose** – the objective(s) of this particular audit; e.g., to assess a project’s compliance with their configuration management plan
* **The audit criteria** – the governing document(s) that will be used as the measuring stick for the audit; e.g., the project’s software development plan and related work instructions
* **The project, processes, and products to be assessed** – the specific project and project processes and artifacts to be audited
* **The project personnel/roles to be audited** – the list of personnel, typically by role, who will need to be available for the audit

The audit scope will also be conveyed to the project in the audit notification, so completeness and clarity are important to establish a clear understanding between the audit team and the project or organization being audited.

## 2.2 Audit Notification

It is important to set expectations for an audit. The audit team provides the project or organization to be audited with an audit notification letter (email) ahead of the audit. A best practice is to provide this notification 2 weeks to 30 days ahead of the audit, depending on the agreements with the project and program/project plans. The audit notification includes key pieces of information for both the audit team and the project to be audited. Recommended content includes:

* **Audit purpose and scope** – See Audit Scope in this topic for more information
* **Schedule / Agenda** – Based on experience or using a known estimation method/tool and data for a similar scope and a similarly experienced audit team, generate an agenda to fit the audit timeframe, so both the audit team and project understand the audit timeline. The project can use this information to plan the resources needed to support the audit. Be prepared to adjust onsite if interviews run longer than planned, interviews lead down a new risk trail or access to records is interrupted or slowed, etc. Know that once the audit notification letter is received by the project, be prepared to iterate on the dates and agenda to ensure the project can fully support the audit. When establishing the agenda, include time for:
  + Audit team to prep and wrap-up daily
  + Audit team to prepare the out brief
  + Meals and breaks
  + Re-visits if findings/concerns are addressed while onsite
* **Audit Team/Roles** – List by name and role and whether attending in person (preferred) or remotely
* **Auditees/Roles** – List by name, if known, but this will likely be a list of the project roles needed to support the audit with enough detail to allow the project to identify the personnel needed to support the audit and the timeframes that personnel will be involved in the audit
* **Governing Documents** – List by name and version the documents serving as the basis of the audit criteria; e.g., software development plans, standards
* **Onsite logistics needed from the project** (see Audit Logistics in this topic) – Provide a list of items the audit team will need while onsite to efficiently conduct the audit. Consider the following items:
  + MS Teams / Webex / Teleconference, if needed
  + Location (e.g., conference room, audit team meeting room)
  + Projector and screen
  + Access to facilities (e.g., NASA Center grounds, buildings, rooms, site maps)
  + Access to the Internet, printer, etc.
  + Records/materials and/or repository access needed from the project (e.g., arrangements for accessing project artifacts behind firewalls)
  + Escort assignments, if necessary

## 2.3 Audit Logistics

It is important to establish logistical items for the audit.  Consider:

* **Travel** – If the audit occurs at a location different than the location of the audit team, as soon as the audit timeframe is agreed upon with the project, any required travel should be planned.  This ensures the entire audit team is onsite and ready for the audit to occur.
* **Repository for audit records** – It is important to capture the evidence from the audit in a known repository accessible to the audit team and management.  These records serve as the official record of the audit as well as provide information for planning future audits. For example, identify a folder in a general audit repository to hold the items such as the audit plan, audit notification letter/email, records of attendees and personnel interviewed, completed audit checklists, audit notes, audit results, audit reports, audit results responses from the project, etc.)
* **Method for tracking results of this audit to closure** – If not captured in an overall audit plan, identify and document a method for working audit Findings to closure.  This could be as simple as a spreadsheet or an existing tool such as JIRA, Confluence, or SharePoint could be used.
* **Confidentiality** – Remember to consider confidentiality requirements when establishing the method for recording and tracking audit results to closure (e.g., select a tool that has provisions for access permissions and restrictions). The audit records and results may be sensitive (e.g., CUI, Secret, Proprietary) and should not be disclosed to non-interested parties. Steps need to be taken to protect them.

## 2.4 Audit Communication

For an audit to be successful, communication between the audit team, the project, and management before, during, and after the audit is key.  Consider the following as key communication items:

* **Audit Authorization** – Get the appropriate authority to authorize the audit in written form so a record of this authorization can be captured in the audit records.  This could be software assurance management, a contracting officer for audits of contracted development, or some other designated, pre-determined authority.  In some cases, the audit team may need to sign confidentiality agreements.
* **Audit notification** – Send the audit notification (see Audit Notification in this topic) to the project via email, in-person delivery, or another appropriate method and within the pre-determined timeline.
* **Dates and logistics** – Iterate with the project being audited on audit dates (see Audit Notification in this topic) and logistics (See Audit Logistics in this topic) until everyone agrees.  Iterations could be via email, in person, or by phone, to capture any decisions made for the audit records.

## 2.5 Audit Team Selection

When establishing an audit team, work with appropriate management to obtain the personnel and other resources needed to conduct the audit.  Keep in mind the goals of independence and objectivity while obtaining personnel with the appropriate skill sets and knowledge to efficiently conduct the audit and capture the notes and evidence needed to support the audit conclusions.

 Suggested considerations include:

* **Expertise in the audit criteria / governing documents** – Most of the audit team needs to be familiar with the audit criteria or governing documents used as the basis for the audit.  The audit team can do some familiarization as part of audit preparation, but familiarity with the relevant standards, process documents, development plans, etc. from other roles these personnel hold is even better because it gives them good, practical knowledge to use when interviews open new paths to explore during the audit. One specific area of expertise that auditors on the team should be familiar with is the Capability Maturity Model Integration (CMMI)® practices so that they can identify process issues as the audit is performed.
* **Experience or training in performing audits** – The Lead Auditor, at a minimum, should be an experienced auditor.  This helps ensure a consistent process across audits and can be an asset for keeping the team on track during the audit, especially when a portion of the team is there for their technical background.  A mix of experienced auditors and newly trained auditors can be used to help newer auditors gain valuable experience.
* **Involvement in the work being audited or any other potential conflict of interest** – Audit team members must not be involved in any of the work being audited or have any other ties to the work that would make their participation in the audit appear to be a conflict of interest. These connections to the work being audited can taint or invalidate the audit results (think about the concept of someone checking their work) and reduce or even eliminate true objectivity and independence which are key concepts when performing an audit.
* **Skills for the role they will fulfill** – The audit team has a few key roles that need to be fulfilled, and each role has its own set of skills needed for success.  These key roles include:
  + **Lead Auditor** – Person who leads the team, manages the overall audit work, interfaces with the project during planning, leads the onsite audit, and interfaces with the project to ensure audit results are tracked to closure.
  + **Facilitator** – Person who ensures the team remains on track and scheduled during the audit.  This person could have roles as a time-keeper or as the person who keeps order and prevents the team from straying too far off the main audit focus.
  + **Documentarian/Recorder** – Person who captures the interview notes, observation notes, attendance, evidence (actual or references), and other records during the audit to ensure all the information needed to back up the audit conclusions is collected and captured in the audit records.
  + **Technical expert** – Person(s) with experience in the focus of the audit.  Technical expertise could be configuration management, test/verification, risk management, etc.  Technical expertise could also be guidance, navigation, and control (GN&C), ground systems, flight operations, etc. to help the audit team identify areas of risk.
  + **General auditor** – Person(s) with audit experience or trainees who are not technical experts but may have some familiarity with the governing documents.

**Note**: Auditors on the team should be familiar with the Capability Maturity Model Integration (CMMI)® practices so that they may identify process issues as the audit is performed.

When establishing an audit team, other decisions that need to be made include:

* **Team size/number of auditors** – An audit team should not overwhelm the project being audited, so 10 auditors for a project team of 4 or 5 developers might be a mismatch.  On the other hand, a single auditor to fill the standard roles of Lead Auditor, Facilitator, Documentarian/Recorder, and technical expert is inefficient and ineffective.  The person asking the questions cannot take notes and keep the discussion on track without slowing down the audit progress.  Team size is often based on the necessary technical or process expertise in addition to the standard roles, so a minimum team size might be 3 or 4 to conduct an audit efficiently.
* **Lead auditor and other roles** – Determine what roles are key for each particular audit and the number of technical experts needed and identify audit team members to fill those roles.   Be sure any necessary training, such as basic auditing for technical experts or review of the governing documents/audit criteria for the entire team, is completed well ahead of the audit.
* **Auditor participation method** – Identify who will audit in person and who will be remote, if applicable.  For a multi-day, offsite audit, it may be sufficient for a technical expert to participate by teleconference for a 2-hour audit session where their expertise is needed.  The Lead Auditor should be onsite for the audit as should the Documentarian/Recorder, but where good teleconference facilities exist, it may be acceptable for the Documentarian/Recorder to participate remotely.

## 2.6 Audit Checklists

Having tools in place to support audits is key to consistent, well-planned, complete, and accurately documented audits.   One key tool is the audit checklist.

When establishing audit checklists or audit criteria, start with the governing documents. Using those governing documents, generate questions as the basis for collecting evidence by which compliance will be assessed/measured.  Potential sources, not an exhaustive list, for checklist questions include:

* NASA standards
* NASA Procedural Requirements (NPRs)
* An existing baseline checklist created from an entire governing document (tailor such checklists to focus on the specific audit area of interest)
* Requirements specifications
* Project processes and procedures
* Software Development Plans (SDPs) / Software Management Plans (SMPs)
* Past audit results and corrective action plans, if available
* Process best known practices (i.e., CMMI® practices, IEEE standards, etc.)
* Known areas of concern (based on project performance, management reviews, project reviews, etc.)

Some general concepts and questions to keep in mind when creating checklists include:

* Does the person performing the task have access to and understand the work procedures for their tasks?
* Are the procedures being used by the project up to date?
* Does the person performing the task have the right training, skills, experience?
* Is the work being performed efficiently and effectively?
* Does the person have the right tools, environment, infrastructure, etc. to do the task?
* Are the work products verified, approved, controlled as required?
* Are defects reported and tracked to closure?
* Are the appropriate records/task evidence being captured?

Questions should have the following characteristics:

* Answers should be known and expected based on pre-audit work and the auditors’ knowledge of the project based on project documentation, familiarity with the team’s processes and work products, review of project artifacts/work products, etc.
* Questions should focus on the work, not the individuals.
* Questions should be open-ended and context-free, for example, “What procedures do you follow when performing your work?” is a better audit question than “Do you follow work instruction ABC when you do your work?” Another example is “Describe how process ‘X’ is done,” where ‘X’ could be the change management process, peer review process, software build process, etc.

A checklist or set of audit criteria often takes the form of a spreadsheet for ease of capturing notes, evidence references, and audit conclusions all in one place. A spreadsheet can include the following columns:

* Questions – often answerable by yes/no or in the form of “show us evidence that…”
* Pass / Fail slots per question
* Action slots per question – e.g., to capture follow up work by the project or audit team to close a possible Finding or provide additional evidence
* A place to capture evidence viewed to assess compliance per question
* A place to capture the rationale for the pass / fail results per question
* The priority of questions/topics (H/M/L – in case the audit team needs to reduce or adjust scope in real-time)

Links to the Audit Checklists available in this Handbook have been compiled in the Audit Checklist tab of this topic.  Click here to see the [List of Audit Checklists](#tabs-5) in the Audit Checklist tab.

# 3. Conducting the Audit

With the planning complete and the audit tools in place, it is time to conduct the actual audit.  There are several steps to an audit, including pre-audit preparation, audit activities, and post-audit close-out work.  The following sections describe each step and offer guidance for success.

## 3.1 Audit Team Preparation

Before the audit team arrives for the audit, the following preparation is completed:

* **Review governing process documentation** – If not performed as part of checklist generation, obtain and review governing process documentation.  Process documentation may be Project, Contract, Agency, or Center-specific, and the audit team needs to be familiar with the specific governing documents for this audit.  Familiarity with the entire governing document, not just the area(s) under audit, is important as process areas can influence each other, and audit discussions can flow into those related areas. Having the background knowledge of the governing documentation, including work-level process instructions, helps put discussions with project personnel into context as well as provides a basis for understanding personnel responses to questions.
* **Audit plan and checklist review** – It is important for the entire audit team to be familiar with the audit focus, the questions to be asked, the activities to be witnessed, the audit team member roles, etc. The audit team lead ensures this review is completed, and everyone understands their role in the audit and the purpose of each item in the checklist.
* **Prior audit results review** – If not performed as part of checklist generation, the audit team reviews the results of any relevant prior audits for this project.  Part of the audit could include follow-up on the root cause and corrective action for any prior Findings or systemic issues and a few spot checks on any specific areas of concern.
* **Pre-audit assessment** – Some elements of the audit can be completed before the audit begins.  If the audit team has or can obtain access to project repositories and records, the team carries out document reviews to assess checklist items that can be completed without involving the project.  This provides a basis for tailoring checklist questions to focus on areas this pre-audit assessment identifies as potential compliance concerns.  For example, compliance with a process requirement indicating that all problem reports will include specific fields and signatures can be checked by sampling project problem reports. Any concerns found during this review can be used to tailor checklist questions to determine if the project is aware of the concerns and what is being done to address them.

## 3.2 In-brief

It is important for the audit team and the project to have a common understanding of the audit plans.  Initially, this was conveyed in the audit notification (see Audit Notification in this guidance), but on the first day of the audit, the ground rules should be repeated to ensure everyone is on board and has the same interpretation of the audit plan.  This is also the time for the audit team and project to ask and have answered any general questions related to the audit.

The Lead Auditor typically runs this meeting on day 1 of the audit.  The in-brief can be short (15-30 minutes) and focused, but covers the following information:

* **Audit team introductions** – Introduce the audit team, including any audit team members who are participating remotely.
* **Project team introductions** – While the entire project team may not attend the in-brief, key players such as the project manager and team leads should be invited to gain an understanding of the audit.  At the project’s discretion, other key auditees may choose to attend the in-brief.
* **Audit scope review** – Review the audit focus/scope, including any changes in the pre-delivered schedule and/or agenda.
* **Audit method review**, as needed – If the audit will include more than just personnel interviews, it is a good idea to review those audit activities during the in-brief.  Include a brief description of any planned document reviews, interviews, observations.   Remember to inform the group that auditing is a sampling technique, not an exhaustive review of all work products and interviews with every project team member.
* **Project team participation** – State expectations of the project team, if not covered elsewhere.  The goal should be to minimize the team’s time away from their project work while providing sufficient time to collect information for the audit.  Review the overall audit agenda and indicate when specific project roles are requested to participate.
* **Closing expectations and activities** – State for the group the expectations for the out brief (see Outbrief in this guidance) and post-audit activities/timeframes (see Follow-Up and Close-out in this guidance).  The out brief will occur on the final day of the audit and is typically attended by the same key personnel who attended the in-brief.  They will want to know any preliminary results as well as any timeframes for the final audit report and anticipated response by the project.
* **Audit logistics** – Both the Lead Auditor and project manager cover this material.  The Lead Auditor confirms any logistics such as Webex, teleconference, Internet / Wi-Fi access, room assignment(s), etc. previously provided by the project.  The project manager reviews building logistics (e.g., emergency evacuation instructions, restrooms, etc.), lunch possibilities, etc.

It is important to have a record of the in-brief, so the audit team captures the in-brief presentation(s), in-brief attendees with their roles, and notes from any discussion.  Typically, this information is captured in the official audit record by the audit team Documentarian/Recorder.

## 3.3 Interviews/process observations/meeting observations

Once the in-brief is concluded, the core audit work begins.  The team follows the agenda and checklist, adjusting as needed based on where the audit discussion takes the team.  The Lead Auditor or audit Facilitator ensures the audit team remains as close to schedule as possible while allowing sufficient time for an investigative and informative discussion.

For a full perspective on process compliance, interviews include project personnel at all project levels – managers, leads, engineers.  The Documentarian/Recorder captures the names and roles of auditees in the official audit notes.  Consider confidentiality in choosing people who will be interviewed together.  The audit team should not interview workers in the same interview as their supervisors to help ensure that interviewees remain honest about what they do.

For each interview session, the Lead Auditor:

* Introduces the audit team and their roles
* States the interview purpose
* Informs the auditee(s) how the session will be conducted (e.g., notes will be taken, the focus is on the process, not the auditee, etc.)
* Tries to put the interviewee at ease
* Asks general introductory questions
* Asks planned open-ended questions & follow-up questions as appropriate
* Thanks the interviewee for their time

A few key concepts help keep the interview focused:

* Follow the prepared checklist
* Keep language-neutral – avoid leading the auditee answers or giving the impression that “all is well” or “all is bad”
* The auditee should do most of the talking
* Don’t provide feedback during interviews, observations, etc. – just collect evidence; feedback can be provided during out brief
* The auditee should not select record samples but could direct the auditor to a repository where the auditor selects the sample

These concepts help the audit team identify issues and concerns:

* View evidence: “if it’s not written down, it never happened.”
* Follow the evidence until satisfied or a dead end or a time constraint is reached – remember the need is to sample enough evidence to assess compliance
* Look for trends in the interviews, collected evidence, etc.
* Look for process escapes

When interviews are not sufficient or are not appropriate to gather the required evidence, witness project activities to confirm employees are familiar with processes, procedures, policies, and their related roles and responsibilities.

## 3.4 Audit Records

While the Documentarian/Recorder captures the official audit record, the entire audit team takes their notes to ensure the official audit record is complete and accurate.  Note that comparisons occur in the daily audit team meetings (see Daily audit team meeting in this guidance), and any discrepancies in evidence references can be cleared up with the project before the audit concludes.   The Documentarian/Recorder captures the following evidence for the audit record:

* **Objective criteria / Records assessed** - Capture record identification and location (document name, document id, date, repository, URL, etc.) to uniquely identify the records assessed during the audit
* **Who said what during interviews** – Capture (for corroborating evidence) along with the interview notes, each auditee’s name and project role as well as the date/time of each interview
* **Date/time/location/event** - For observed meetings, processes, and witnessed activities, along with the notes identifying the process being assessed and what was observed/witnessed, capture the date, time, location, and event name or description.  Include audit team members participating as well as any project personnel and their roles.

## 3.5 Process-specific Questions

* Focus questions on the following:
  + Applicable findings from the last similar process audit
  + key steps of the process (not entry criteria, exit criteria, or content that is present in every SOP such as submitting/reviewing lessons learned)
  + Content in the process that is confusing or unclear
  + Project’s tailoring of a process
  + Work products based on the standards/guidance that is identified in the process

## 3.6 Daily audit team meeting

At the start of each audit day or the end of the day or both the audit team meets alone to plan and prepare.

At the beginning of each day, the audit team reviews the plan for the day and discusses any adjustments needed to remain on track.  Any adjustments are communicated as soon as possible to the project manager to minimize the impact on the project team’s work.

At the end of each day, the audit team reviews and compares notes to ensure the audit record is complete and accurate and makes any clear pass/fail decisions based on the evidence collected.  The team also comes to a consensus where possible on findings, observations, etc.   Collectively, the team:

* Looks for trends in the interviews, collected evidence, etc.
* Looks for multiple interviewees making the same statement
* Identifies if multiple auditors heard the same thing

This information is captured in the Documentarian’s/Recorder's audit record.

The team discusses any open questions and determines if a follow-up is needed and where that might occur in the audit schedule.  If the team realizes they are off schedule, re-planning can occur to ensure the highest risk or most critical items are assessed during the audit.

To ensure the out-brief presentation is sufficiently prepared, the audit team uses these daily meetings to collect content for the presentation.  This content is adjusted daily as appropriate until the presentation is finalized and becomes part of the audit record.

## 3.7 Out brief / Closing Meeting

The last official activity during the audit is an out brief presentation (Audit Summary Report) from the audit team.  The project will want results, but the audit team may need some time to process the collected evidence.   During the daily team meetings (see Daily audit team meeting in this guidance), the audit team should have been collecting content for this out-brief to provide the project with as much information as possible before the official audit report is generated.  Neither the audit team nor the project wants any surprises when that report is delivered, so the out brief is a preview of the report content.

The out-brief presentation is not required to be lengthy, but includes the following information:

* **Audit Overview** – Repeat a summary of the audit in-brief content (see In-brief section of this guidance), noting any deviations made during the audit.
* **Audit Evaluation Summary** – Overall evaluation of audit subject, based on audit observations/results. Capture and share any overall impressions, observations, etc. for the project, both good and bad.  This could include best practices identified by the audit team, project team cooperation and openness, concerns about missing or frequently changing project documentation, etc.  This is not a list of official findings and observations but is a general set of information for the project.
* **Findings, Observations, OFIs, and associated Risks** – If available, provide any identified Findings, Observations, OFIs from this audit.  Full details may not yet be available, so sharing at a high level is acceptable, but make it clear to the project that the audit report will contain the official results. Even at a high level, these concerns should be written because the project is likely to begin to push back even before the final report is delivered.  The audit team needs to be prepared for some discussion at this point in the out brief. If there are risks associated with findings and observations identified, be sure to include them.   
  Often with fairly large audits, the audit team holds preliminary findings meeting with the project to ensure that the audit team has understood what they heard. This may also give the auditees a chance to provide some evidence that was overlooked during the interviews.
* **Status of Actions, Next Steps, and Due Dates** – Include in the presentation the next steps and actions for this audit with due dates and assignments.  Typical items include:
  + Audit report generation and delivery – the audit team, typically delivered the official set of audit results to the project 2 weeks to 30 days after the audit ends.
  + Timeframe for audit report response – the due date for the project to respond to the audit report with their feedback and/or plan to address any Findings; this could be 30 days after the project receives the official audit report.
  + Additional evidence due from the project – if during the audit the project agreed to provide additional evidence (screenshots, copies of records not accessible to the audit team, etc.), list those items, the audit team point-of-contact (typically, the Lead Auditor), and relevant due dates .

As with the In-brief, it is important to have a record of the Out-brief, so the audit team captures the presentation, attendees with their roles, and notes from any discussion.  Typically, this information is captured in the official audit record by the audit team Documentarian/Recorder.

See Topic [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) in this Handbook for the Minimum Recommended Content for the Audit Report Summary.

# 4. Follow-Up and Close-out

To conclude the audit, there are follow-up and close-out steps that occur.  The official results are generated in an audit report, Findings are tracked to closure, project trends are captured for potential future audits, and the audit process is reviewed and updated as necessary.

## 4.1 Generate and Deliver Audit Report

Just as they were at the Out-brief, the project is anxious to receive the final audit results, so the first order of business for the audit team is to generate and deliver the audit report, which contains the official audit results to which the project will respond.

The audit report summarizes the audit and provides the official results.  Typical audit report content includes:

* **Confidentiality Statement** – Depending on the nature and ownership of the material assessed during the audit, any project contracts in place, etc. the audit report may be restricted to specific audiences or require a statement of confidentiality regarding the results it contains.  The Lead auditor makes this determination and ensures the audit report contains the necessary statements and access restrictions.  
  If the audit team assessed several companies within a project, there might be company-confidential processes or information involved. Also, in the case of multiple companies, the audit team may not want to put company-specific audit results out publicly where they can be used for comparisons.
* **Purpose, Scope, Schedule, and Governing Documents** – These sections of the report reflect the audit plan and serve as the official record of what was audited, for what purpose, and the audit timeframe.  The audit notification (see Audit Notification in this guidance) is a good source for this information, but be sure the audit report content reflects any adjustments made during the audit.
* **Personnel** – List the auditors, auditees, other attendees as captured in the Documentarian/Recorder record of the audit.  Depending on the audit report audience, it may be necessary only to capture key personnel and not every person who participated in the audit.  The Documentarian/Recorder notes from the audit will include the full list of participants, so the audit report may include only key participants.
* **Governing documents** -  List by name and version the documents serving as the basis of the audit criteria, e.g., software development plans, standards.
* **Assumptions, qualifications** – Audits are sampling activities, so it is important to identify any assumptions and qualifications made when generating Findings and Observations.  Assumptions could include the number of samples taken given the full number of records available, the time available to conduct an interview or witness an activity, the availability of key personnel during the audit, etc.  These caveats impact the audit results, and so are important to list in the report.
* **Overall Summary** – Provide a statement or paragraph regarding the overall compliance of the project with the governing documents, or specific sections thereof, used for this audit.
* **Results** – List in clear statements, the Findings, Observations, Opportunities for Improvement (OFI) in that order with major Findings first.  List the relevant governing document requirement with each Finding, preferably the full text and reference to its location in the governing document.  Stick to the facts – what was heard, seen, collected, or not able to be seen, heard, or collected (i.e., no objective evidence could be found).  A good set of working definitions for audit results are listed below.
  + **Major Finding**– major non-conformance or non-compliance with requirement or process or collection of minor non-conformances that indicate systemic issue (see also ISO 1021-1:2015E and AS9101TMF); a major or total breakdown of a process; not meeting a requirement
  + **Minor Finding** – minor non-conformance or partial non-compliance (see also ISO 1021-1:2015E and AS9101TMF); isolated or single part of a requirement not being met; roll up minor Findings into a single Finding; e.g., not in compliance with configuration management (CM) control vs. a long list of minor CM Findings
  + **Observation** – positive and negative observations that are not non-conformances or a potential non-compliance outside the scope of the current audit; positive observations are observations that contribute to quality; negative observations are observations that detract from the quality and if not addressed could be non-compliances in the future. This should include important observations such as any systemic issues, Best Practices, and areas of concern.
  + **OFI** – a recommendation that would improve compliance to a higher level of quality or to a suggested best practice.
* **Status of Actions, Next Steps, and Due Dates** – List any actions and next steps relevant to the delivery of the audit report with appropriate due dates.  Consider the following:

+ The date for a formal review of the audit report with the project
+ Dates Corrective Actions are due to the project for the findings
+ Dates for any follow-up meetings planned, perhaps to review Corrective Action status

See Topic [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) in this Handbook for the complete set of Minimum Recommended Content for the Audit Reports.

When planning to deliver the audit report, confirm the distribution with audit management and the project team.  Consider recipients from the following groups, depending on any access, confidentiality, and viewing restrictions associated with the report:

* Project distribution
* Audit team distribution
* Management distribution

## 4.2 Track Findings to Closure

After the audit report is delivered, the audit team continues to have closure responsibilities such as those listed below.

* Review corrective action (CA) plans or responses from the project following an agreed-upon timeframe with the project.  Two weeks to 30 days is a reasonable timeframe depending on the project’s schedule and when they can reasonably implement the solutions, once approved.
  + Review CA plans for expected content:
    - Problem/Issue/Finding statement
    - Root Cause investigation plan, including “where else does this need to be applied” and a due date
    - Short term correction plan and a due date
    - Long term CA plan  (plan to avoid recurrence) and a due date
  + Assess any provided rationale for why corrective action is not needed, e.g.:
    - The project provided more evidence
    - Project clarified an audit team misunderstanding
  + Assess timeliness of CA plans, coverage of the associated Findings,  and recurrence prevention plan
  + Work any concerns with the project; this responsibility lies with the Lead Auditor and project manager
* Once the project has implemented the CA plans, review the results to assess how well those plans addressed the relevant audit Findings.  This includes a review of any revised documents, an assessment of revised process implementation, and perhaps a follow-up audit.
* When Findings are satisfactorily closed, the Lead Auditor notifies the project and audit team management in writing and captures the written notifications in the official audit records, including the rationale for closure of each Finding.

## 4.3 Track Observations and OFIs

While audit Findings are required to be addressed by the project, NASA does not always require Observations and OFIs to receive a formal response from the project given that these items are not non-compliances, but suggestions for improvement that could prevent non-compliance in the future.   If a project responds to Observations and OFIs, the audit team is responsible for reviewing those responses and following up as appropriate.  Follow-up could be simple feedback that the response is acceptable, or it could be to enter notations in the audit record that the Observation or OFI is a candidate for a future follow-up audit.  The audit team determines how to respond to the project for Observations and OFIs.

## 4.4 Track items for future audits

As noted in several places in this guidance, an audit can generate items to be assessed in future audits.  Capturing these items in an official audit repository ensures they are available for planning future audits and not lost over time. Consider the following:

* Project trends identified during an audit might need to be re-assessed in a future audit.
* Corrective actions for Findings might be acceptable in the short term, but those processes become potential candidates for future audits to ensure those corrective action plans remain in place.
* Observations and OFIs provide candidate material for future audits to ensure those items are not trending negatively.  This includes areas that narrowly passed a previous audit
* Trends observed across a series of audits are good future audit material.
* Regular interaction with a project can identify possible audit material, including processes that seem to be followed loosely, work products that seem to have repeated issues, and process escapes.

## 4.5 Identify and Adjust the Audit Process

As with any process, continuous assessment and improvement of the audit process are necessary to focus and efficiently use available resources.   During each audit, the audit team learns lessons about what works with each project and each type of audit conducted.  Those lessons are captured and when the overall audit schedule permits, the team reviews those lessons learned and makes appropriate adjustments to the audit process using all the appropriate checks and balances, peer reviews and inspections, and management approvals necessary to maintain an effective and efficient process.

# 5. Audit Checklists

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

## 5.2 Other Audit Checklists

-- Under construction

# 6. CMMI Practice content

The tables below identify critical Capability Maturity Model Integration (CMMI)® Practice content that should be captured to some extent in the identified audits.  As part of the audit preparation, verify this content is present during the audit review.  If it is not present or is vague/unclear, inconsistent, incomplete, then identify improvement opportunities.

|  |  |  |
| --- | --- | --- |
| **Process Management SOP** | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | Is Senior Management involved in identifying and communicating policies concerning the organization’s process/performance improvement (e.g., activities that shall be performed, organizational processes that have been developed, who they apply to in the organization)? | GOV 2.1 |
| 2 | Does Senior Management provide process/performance improvement goals and objectives to the EPG periodically (based on organization/business objectives)? | GOV 3.2 |
| 3 | Is it clear how process assets are maintained so that they are consistent and easily accessible? Are there standards for the different types of process assets? | PAD 3.1, 3.5 |
| 4 | Is Senior Management involved in identifying their information needs for all activities performed in the organization – for projects and support functions (e.g., status meeting items to be covered, measures to be collected)? | GOV 2.3 |
| 5 | When does an analysis need to be performed for acquiring/developing a process asset? Is it clear how it should be performed (e.g., using the formal decision process)? | PAD 2.2 |
| 6 | Is a process architecture (process model) developed?  Are the required components of a process architecture defined? | PAD 3.2 |
| 7 | Are tailoring guidelines and criteria established and where are they documented? | PAD 3.4 |
| 8 | Is tailoring monitored?  When/how is it monitored? | PAD 3.4 |
| 9 | Are measurement standards (list of required measures, description of each measure, to whom the measure pertains) developed, and are they clear? How often are they revisited and is senior management involved? | PAD 3.7, GOV 3.1 |
| 10 | Are process improvement objectives defined and traced to business objectives? | PCM 3.1 |
| 11 | Are critical processes identified for business and performance objectives? | PCM 3.2 |
| 12 | How is a deployment of process assets planned?  Does the planning include training, version description, project’s adoption of assets, etc.? | PCM 3.4, 3.5 |
| 13 | How is the effectiveness of deployed improvements determined as they relate to the process improvement objectives? | PCM 3.6 |
| 14 | How are audit trends and tailoring used by the EPG? | PCM 3.3, II 2.2/3.2 |
| 15 | Is the quality of measurement data reviewed periodically? | MPM 3.3 |
| 16 | How does the EPG and Senior Management review aggregated measures and identify corrective actions? How does Senior Management communicate the results of this review to the organization? | MPM 3.5, 3.6; GOV 3.1 |
| 17 | Is senior management involved in the process management activities? In providing resources? In reviewing status? In providing training (e.g., CMMI Training, process definition training)? | GOV 2.2, 2.3, 2.4 |
| 18 | Is Senior Management involved in reviewing aggregated measures, identifying corrective actions, and communicating performance results to the organization? | GOV 3.1 |

|  |  |  |
| --- | --- | --- |
| **Organization Training SOP** | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | Are organization training needs evaluated periodically and documented? How are projects and support functions involved? How is Senior Management involved? | OT 2.1, 3.1, 3.2, GOV 3.2 |
| 2 | Do organization training needs to address relevant processes and work environment standards (e.g., tools, methods)? | II 2.1 |
| 3 | Is training planned and communicated to the organization? | OT 3.3 |
| 4 | Are training records maintained so that quick searches by name and/or course can be conducted? | OT 2.2, 3.4 |
| 5 | Are there different methods for determining the training effectiveness of the organization’s training program? | OT 3.5 |
| 6 | Is senior management involved in the organization's training activities? In providing resources? In reviewing status? In providing training (e.g., instructors, HR)? | GOV 2.2, 2.3, 2.4 |

|  |  |  |
| --- | --- | --- |
| **Formal Decision SOP**  1.       This is a support process that should be executed by the project or organization as needed (following the guidelines set in the SOP); many times, projects are making decisions but not documenting them well or taking credit for the decisions they have captured.  Look for instances when this has occurred and encourage projects to think about how to take credit for the decisions they are making.  2.       Auditors should consider conducting this audit across the Organization once a year sampling from projects who have conducted a formal decision or using a formal decision performed at the Organization level (e.g., the decision on a tool to be used by all projects).  If there are no projects in the organization that has completed a formal decision in a year, notify the EPG. | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | Are the rules/guidelines identified for when the process should be followed? | DAR 2.1 |
| 2 | Are there multiple options for documenting the results of a formal decision?  This is a good practice to encourage projects to use the process |  |
| 3 | Is an approval authority for select decisions documented? | DAR 3.1 |

|  |  |  |
| --- | --- | --- |
| **Causal Analysis & Resolution SOP**  1.       This is a support process that should be executed by the project or organization as needed; many times, projects are conducting a root cause analysis but not documenting them well or taking credit for those that have been done.  Look for instances when this has occurred and encourage projects to think about times when performing a root cause analysis would add value.  2.       Auditors should consider conducting this audit across the Organization once a year sampling from projects who have conducted a root cause analysis using the CAR SOP.  If there are no projects in the organization that has completed a root cause analysis in a year, notify the EPG. | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | Are examples of positive and negative outcomes that should be considered identified (e.g., test results, measurement results, audit results)? | CAR 2.1 |
| 2 | Are forums that might lend themselves to the execution of a root cause analysis identified (e.g., sprint retrospectives, team status meeting)? |  |
| 3 | Are methods to be used in performing a root cause analysis described? | CAR 2.2, 3.1 |
| 4 | Are different methods of documenting an outcome, the root cause analysis, actions proposed and selected, etc. provided?  Note: this is a good practice to encourage projects to execute the process. |  |
| 5 | Is it clear how actions to address root causes are different from actions taken to address the issue that led to the root cause analysis? | CAR 3.2, 3.3 |
| 6 | Does an action proposal for a root cause include how the effectiveness of the action can be determined?  Note: this is a good practice so that the project considers ahead of time how effectiveness will be measured once the action is taken. | CAR 3.2, 3.5 |

|  |  |  |
| --- | --- | --- |
| **Peer Review SOP**  1.       This is a support process that should be executed by the project or organization as needed.  2.       It may be useful to perform the Peer Review Audit across the organization sampling peer reviews from each project. | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | How are peer reviews performed?  Are there different methods for performing a peer review and are they described? | PR 2.1 |
| 2 | How are peer review results analyzed? | PR 3.1 |
| 3 | How is peer review data analyzed? | PR 3.1 |

|  |  |  |
| --- | --- | --- |
| **Planning SOP** | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | Are estimates generated to include size and effort? How is historical data used for generating estimates? | EST 2.2, 2.3, |
| 2 | Are estimation methods to be used in generating estimates described (e.g., wideband delphi, agile, using historical data)? | EST 3.1 |
| 3 | Are resources (tools, people) planned? | II 2.1 |
| 4 | Is project-specific training planned? | PLAN 2.2 |
| 5 | Is a schedule developed?  Does it include resources and dependencies? | PLAN 2.3, 3.3 |
| 6 | Is there planning for delivery and post-delivery? | PLAN 2.5 |
| 7 | Is tailoring of the organization processes performed and is it clear how this should be performed and documented? | PLAN 3.1 |
| 8 | Are specific performance objectives and associated measures identified for a project?  Is there project information that should be included for each measure? | MPM 2.1, 2.2 |
| 9 | Is senior management involved in planning (e.g., reviewing and approving the plan)? | GOV 2.1 |
| 10 | Are there requirements for the update of a plan (for a project that spans multiple years)? | PLAN 2.7 |
| 11 | Is there an approach (either at the organization level or the project level as specified) for addressing risks?  Does the approach include a description of risk categories, risk parameters, and a strategy for addressing and reporting risks? | RSK 3.1, 3.2, 3.3 |
| 12 | Is there an approach (either at the organization level or the project level as specified) for addressing opportunities? Does the approach include a description of opportunity categories, opportunity parameters, and a strategy for addressing and reporting opportunities? | RSK 3.1, 3.2, 3.3 |
| 13 | Are risks and opportunities identified and evaluated based on the approach? | RSK 2.1, 3.1, 3.2, 3.4 |
| 14 | Is a CM Plan (or equivalent) developed?  Does it include the items to be configuration managed, the tools and how they will be used, the baselines that will be performed (how, when), a description of how changes to items will be addressed, and the CM audits that will be performed? | CM 2.1-2.6 |

|  |  |  |
| --- | --- | --- |
| **Project Management SOP** | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | Are effort and cost monitored? Is it clear how it should be monitored? | MC 2.1 |
| 3 | Are resources (tools, people) monitored | II 2.1, MC 2.1 |
| 4 | Is project-specific training monitored to completion? | II 2.1, MC 2.1 |
| 5 | Is a schedule monitored and updated? | MC 2.1, 3.2 |
| 6 | Are the delivery and post-delivery activities monitored? | MC 2.3 |
| 7 | Is tailoring of the organization processes updated when process changes are deployed? | PLAN 3.1 |
| 8 | Are measures collected and analyzed following the measure descriptions? | MPM 2.3-2.6 |
| 9 | Are the project team and support functions involved in monitoring the project? How are they involved? | MC 2.1, 2.2, 3.1, 3.4 |
| 10 | Is senior management involved in monitoring the project? In reviewing status? In reviewing measures? In providing resources? In providing training? | GOV 2.2, 2.3, 3.1 |
| 11 | Are issues identified and tracked to closure? | MC 2.4, 3.4 |
| 12 | Are risks and opportunities monitored and updated? | RSK 2.1, 3.4, 3.5 |
| 13 | Are items to be configuration managed controlled and baselined correctly (following the plan)? Are changes to items addressed appropriately (following the plan)? | CM 2.2, 2.3, 2.4, 2.5 |

|  |  |  |
| --- | --- | --- |
| **Requirements SOP** | | |
| **ID** | **Item Description** | **CMMI Practice ID** |
| 1 | Are requirements documented? | RDM 3.1 |
| 2 | Does the team review and commit to the requirements? | RDM 2.4 |
| 3 | Are customers and/or end-users involved in defining/prioritizing requirements? | RDM 2.2, 2.3 |
| 4 | Is there an approach to addressing changes to requirements? How are impacted work products identified and updated? | RDM 2.6, 3.1 |
| 5 | Are an operational concept and selected scenarios described? | RDM 3.2 |

# 7. Tools and Examples

NOTE: Download these examples to get a usable copy. The thumbnails below only give a partial preview of what the example looks like.

## 7.1 Sample audit notification letter

Click the link to download: [Offsite Software Audit Notification Letter\_Sample Template.docx](#)

## 7.2 Sample checklist

Click the link to download: [SSO\_ISO 27001 Audit Checklist.xlsx](#)

The thumbnail below only gives a partial preview of what the example looks like. Download the spreadsheet to get a usable copy.

## 7.3 Sample In-brief

Click the link to download: [Audit In-Brief Sample Template.pptx](#)

## 7.4 Sample out-brief

Click the link to download: [Audit Outbrief Sample Template.pptx](#)

## 7.5 Sample audit report

Click the link to download: [Audit Report\_Sample Template.docx](#)

## 7.6 Sample tracking sheet, if tool not used

Click the link to download: [Audit Results Tracking Sheet\_Sample.xlsx](#)

The thumbnail below only gives a partial preview of what the example looks like. Download the spreadsheet to get a usable copy.

# 8. Resources

## 8.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-050)

  [STEP Level 2 NASA Software Auditor Skills course,](https://satern.nasa.gov/ "Click to open in new window")

  SMA-SA-WBT-203 SATERN. System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
   User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
* (SWEREF-218)

  [IEEE Computer Society, "IEEE Standard for Software Quality Assurance Plans", IEEE 730-2002, 2002.](http://standards.ieee.org/findstds/standard/730-2002.html "Click to open in new window")

   IEEE 730-2002, 2002.  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-219)

  [IEEE Standard for Software Reviews and Audits](https://ieeexplore.ieee.org/document/4601584 "Click to open in new window")

  IEEE Std 1028, 2008. IEEE Computer Society, NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-291)

  [ISO/IEC 17021-1:2015 Conformity assessment](https://www.iso.org/standard/61651.html "Click to open in new window")

  ISO/IEC 17021-1:2015 contains principles and requirements for the competence, consistency and impartiality of bodies providing audit and certification of all types of management systems. ISO 17021-1:2015(E) – Conformity assessment – Requirements for bodies providing audit and certification of management systems (accessible through the NASA Standards website (https://standards.nasa.gov) than searching the HIS Engineering Workbench)
* (SWEREF-340)

  [CMMI Model Viewer](https://cmmiinstitute.com/products/cmmi/cmmi-v2-products "Click to open in new window")

  CMMI online Model Viewer gives you complete access and control over the full complement of CMMI V2.0 content. CMMI Process Quality Assurance (PQA) information available in CMMI model. CMMI Institute account needed to access this material.
* (SWEREF-371)

  [AS9101 Rev. F - Quality Management Systems - Audit Requirements for Aviation,
  Space, and Defense Organizations](https://ewb.ihs.com/#/document/HUOKSFAAAAAAAAAA?qid=637152147083078308&sr=re-1-10&kbid=4%7C27707&docid=943279500#h07e92142 "Click to open in new window")

  Aerospace Standard 9101 Rev F, Quality Management Systems

## 8.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-045 - Project Participation in Audits](/spaces/SWEHBVD/pages/102695419/SWE-045+-+Project+Participation+in+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-209 - Benchmarking Software Assurance and Software Safety Capabilities](/spaces/SWEHBVD/pages/102695329/SWE-209+-+Benchmarking+Software+Assurance+and+Software+Safety+Capabilities)        * [PAT-036 - Architecture and Design Process Audit](/spaces/SITE/pages/198770701/PAT-036+-+Architecture+and+Design+Process+Audit) * [PAT-037 - Configuration Management Process Audit](/spaces/SITE/pages/198770725/PAT-037+-+Configuration+Management+Process+Audit) * [PAT-038 - Implementation Process Audit](/spaces/SITE/pages/198770739/PAT-038+-+Implementation+Process+Audit) * [PAT-039 - Operations, Maintenance, & Retirement Process Audit](/spaces/SITE/pages/198770753/PAT-039+-+Operations+Maintenance+Retirement+Process+Audit) * [PAT-040 - Project Management Process Audit](/spaces/SITE/pages/198770755/PAT-040+-+Project+Management+Process+Audit) * [PAT-041 - Project Planning Process Audit](/spaces/SITE/pages/198770757/PAT-041+-+Project+Planning+Process+Audit) * [PAT-042 - Requirements Development and Mgmt Audit](/spaces/SITE/pages/198770759/PAT-042+-+Requirements+Development+and+Mgmt+Audit) * [PAT-043 - Software Defects & Tracking Process Audit](/spaces/SITE/pages/198770761/PAT-043+-+Software+Defects+Tracking+Process+Audit) * [PAT-044 - Software Hazard Development Process Audit](/spaces/SITE/pages/198770763/PAT-044+-+Software+Hazard+Development+Process+Audit) * [PAT-045 - Software Peer Review Inspection Report Audit](/spaces/SITE/pages/198770772/PAT-045+-+Software+Peer+Review+Inspection+Report+Audit) * [PAT-046 - Test Verification and Validation Process Audit](/spaces/SITE/pages/198770767/PAT-046+-+Test+Verification+and+Validation+Process+Audit) |

## 8.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>8</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement)      * [Software Quality Assurance](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Software+Quality+Assurance) |

## 8.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
