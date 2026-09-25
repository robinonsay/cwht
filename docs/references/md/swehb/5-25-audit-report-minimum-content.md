# 5.25 - Audit Report Minimum Content

> NASA Software Engineering Handbook (SWEHB Ver D), page id 140641711. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/140641711/5.25+-+Audit+Report+Minimum+Content

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
