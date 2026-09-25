# 5.21 - Software Requirements Analysis Report Minimum Content

> NASA Software Engineering Handbook (SWEHB Ver D), page id 140641581. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content

**Documenting and Reporting of Analysis Results**.

When the requirements are analyzed, the Software Requirements Analysis work product is generated to document results capturing the findings and corrective actions that need to be addressed to improve the overall requirements set. It should include a detailed report of the requirements analysis results. Analysis results should also be reported in a high-level summary and conveyed as part of weekly or monthly SA Status Reports. The high-level summary should provide an overall evaluation of the analysis, any issues/concerns, and any associated risks. If a time-critical issue is uncovered, it should be reported to management immediately so that the affected organization may begin addressing it at once.

When a project has safety-critical software, analysis results should be shared with the Software Safety personnel. The results of analysis conducted by Software Assurance personnel and those done by Software Safety personnel may be combined into one analysis report, if desired.

## **4.1 High-Level Analysis Content for SA Status Report**

Any requirements analysis performed since the last SA Status Report or project management meeting should be reported to project management and the rest of the Software Assurance team. When a project has safety-critical software, any analysis done by Software Assurance should be shared with the Software Safety personnel.

When reporting the results of an analysis in a SA Status Report, the following defines the minimum recommended contents:

* Identification of what was analyzed: Mission/Project/Application
* Period/Timeframe/Phase analysis performed during
* Summary of analysis techniques used
* Overall assessment of design, based on analysis
* Major findings and associated risk
* Current status of findings: open/closed; projection for closure timeframe

## **4.2 Detailed Content for Analysis Product:**

The detailed results of all software requirements analysis activities are captured in the Software Requirements Analysis product along with the types of analysis techniques used to provide information on the robustness of the analysis done. The techniques/methods used provide information on those that produced the most useful results . This document is placed under configuration management and delivered to the project management team as the Software Assurance record for the activity. When a project has safety-critical software, this product should be shared with the Software Safety personnel.

When reporting the detailed results of the software requirements analysis, the following defines the minimum recommended content:

* Identification of what was analyzed: Mission/Project/Application
* Person(s) or group/role performing the analysis
* Period/Timeframe/Phase analysis performed
* Documents used in analysis (e.g., versions of the system and software requirements, interfaces document, Concept of Operations)
* A high-level scope and description of the techniques/methodologies used in the analysis
  + Use the list of possible analysis techniques/methodologies listed in Tab 2 as a starting point.
  + For each technique/methodology on the list, state why/or why not it was used.
  + List any additional techniques/methodologies used that were not included in the Tab 2 list.
* Summary of results found using each technique/methodology
  + How many findings resulted from each technique/methodology?
  + Difficulty/Ease of technique/methodology used
  + The general assessment of the technique/methodology
  + High-Level Summary of the findings
* Results, major findings, and associated risk:
  + Overall assessment of the quality/completeness of the requirements, based on the analysis
  + Either list each result, finding, or corrective action or summarize them and list the links to the detailed findings.
  + Assessment of the overall risk involved with the findings.
* Documentation should include types of findings:
  + Missing requirements
  + Requirements that need rewriting: because they are incomplete, incorrect, unclear, not testable/verifiable, etc.
  + Requirement with safety concerns
  + Requirements with security concerns (e.g., access control, vulnerabilities, weaknesses, etc.)
  + Incompatibilities in interfaces not clearly defined
  + Issues in traceability (Child with no parent, parent with no children, etc.)
  + Requirements with unnecessary functions
  + Requirements are not detailed enough to provide the information needed to develop a detailed design that can be implemented in the code
  + Hazards and safety-related software controls, constraints, features not included in the requirements
  + Any other requirements issues discovered during the analyses
* Minor findings
* Current status of findings: open/closed; projection for closure timeframe
  + Include counts for those discovered by SA and Software Safety
  + Include overall counts from the Project’s problem/issue tracking system.
