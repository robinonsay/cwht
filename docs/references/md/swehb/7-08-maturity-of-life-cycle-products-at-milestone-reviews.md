# 7.08 - Maturity of Life Cycle Products at Milestone Reviews

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695638. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews

7.08 - Maturity of Life Cycle Products at Milestone Reviews

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695638)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695638&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction and Chart](#tabs-1)
* [2. Resources](#tabs-2)
* [3. Lessons Learned](#tabs-3)

# 1. Introduction and Chart

This chart summarizes current guidance approved by the NASA Office of the Chief Engineer (OCE) for software engineering life cycle products and their maturity level at the various software project life cycle reviews.   This chart serves as guidance only and NASA Center procedures should take precedence for projects at those Centers.

The chart was constructed using the software engineering products from NPR 7150.2 [083](#_tabs-<p>2</p>), NASA-STD-8739.8 [278](#_tabs-<p>2</p>), the project life cycle reviews from NPR 7123.1[041](#_tabs-<p>2</p>), previous work from the NASA Software Working Group to map products to life cycle reviews, and additional information gathered from these NPRs, NPR 7120.5 [082](#_tabs-<p>2</p>), and individual NASA Center procedures.

The following maturity definitions from NPR 7120.5 are used in this table:

a. "Preliminary" is the documentation of information as it stabilizes but before it goes under configuration control. It is the initial development leading to a baseline.  
Some products will remain in a preliminary state for multiple life cycle reviews. The initial preliminary version is likely to be updated at subsequent life cycle reviews but remains preliminary until baseline.  
b. "Baseline" indicates putting the product under configuration control to track, approve, and communicate changes to the team and any relevant stakeholders. The expectation on products labeled "baseline" is that they will be at least final drafts going into the designated life cycle review and baselined coming out of the life cycle review. Updates to baselined documents require the same formal approval process as the original baseline.  
c. "Update" is applied to products that are expected to evolve as the formulation and implementation processes evolve. Only expected updates are indicated.  
However, any document may be updated, as needed. Updates to baselined documents require the same formal approval process as the original baseline.

**NPR 7150.2 and NASA-STD-8739.8 include life cycle products that are not included in the chart and life cycle reviews that are also not represented in the chart.**

Links are provided where "Minimum Content" document topics are available. 

| 7150.2 Software Life Cycle Products | MCR | SRR | SwRR | MDR | SDR | PDR | CDR | SIR | TRR | SAR | ORR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Software Development Plan (SDP) / Software Management Plan (SMP) - [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) |  | **P** | **B** | **U** | **U** | **U** | **U** |  |  |  | **F** |
| NPR 7150.2 Requirements Mapping Matrix/table - [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) |  | **P** | **B** | **U** | **U** | **U** | **U** |  |  |  | **F** |
| Software Schedule | **D** | **P** | **B** | **U** | **U** | **U** | **U** |  |  |  | **F** |
| Software Cost Estimate | **D** | **P** | **B** | **U** | **U** | **U** | **U** |  |  |  | **F** |
| Software Configuration Management Plan (SCMP) - [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) |  | **P** | **P** | **P** | **B** | **U** | **U** |  |  |  | **F** |
| Software Test Plans - [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) |  |  |  |  |  | **P** | **B** | **U** | **U** |  | **F** |
| Software Test Procedures - [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) |  |  |  |  |  |  | **D** | **P** | **B** | **U** | **F** |
| Software Test Reports - [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) |  |  |  |  |  |  |  |  |  | **B** | **F** |
| Software Maintenance Plan - [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) |  |  |  |  |  |  | **D** | **P** | **P** | **B** | **F** |
| Software Requirements Specification (SRS) - [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) |  | **P** | **B** | **U** | **U** | **U** | **U** |  | **U** |  | **F** |
| Requirements on OTS s/w |  | **P** | **B** | **U** | **U** | **U** | **U** |  |  |  | **F** |
| Bi-directional Requirements Traceability matrix - [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) |  | **P** | **B** |  |  | **U** | **U** |  | **U** | **U** | **F** |
| Software Data Dictionary - [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) |  |  | **P** | **P** | **P** | **B** | **U** |  |  |  | **F** |
| Software Design Description (Architectural Design) - [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) |  |  |  | **P** | **P** | **B** | **U** |  | **U** |  | **F** |
| Software Design Description (Detailed Design) - [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) |  |  |  |  |  | **P** | **B** |  | **U** |  | **F** |
| Interface Design Description - [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) |  |  |  | **P** | **P** | **P** | **B** |  | **U** |  | **F** |
| Software Coding Standards/Guidelines |  |  | **B** |  |  | **U** | **U** |  |  |  |  |
| Source Code |  |  |  |  |  |  |  | **B** | **U** |  | **F** |
| Version Description Document (VDD) - [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) |  |  |  |  |  |  |  | **P** | **P** | **B** | **F** |
| Software User's Manual (SUM) - [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) |  |  |  |  |  |  |  |  |  | **B** | **F** |
| Records of Continuous Risk Management | **P** | **U** | **U** | **U** | **U** | **U** | **U** |  | **U** | **U** | **U** |
| Measurement Analysis Results - [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) |  |  | **P** | **P** | **P** | **X** | **X** | **X** | **X** | **X** | **X** |
| Software Volatility measures |  |  | **X** | **X** | **X** | **X** | **X** |  |  |  |  |
| Operational Concepts (part of "Mission Operations Concept" or separate) |  | **P** | **P** | **U** | **U** | **B** | **U** |  |  |  | **F** |
| Record of trade-off criteria & assessment (make/buy decision) |  |  |  |  |  | **X** | **X** |  |  |  |  |
| Acceptance Criteria and Conditions |  |  | **B** |  |  |  |  |  | **B** |  |  |

| Software Assurance and Software Safety (from NASA-STD-8739.8) Products | MCR | SRR | SwRR | MDR | SDR | PDR | CDR | SIR | TRR | SAR | ORR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Software Assurance and Software Safety Plan(s) - [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |  | **D** | **D** | **P** | **B** | **U** | **U** |  |  |  | **F** |
| Software Assurance and Software Safety Cost Estimates | **D** | **P** | **P** | **P** | **B** | **U** | **U** |  |  |  |  |
| NASA-STD-8739.8 Requirements Mapping Matrix (RMM) |  | **D** | **D** | **P** | **B** | **U** | **U** |  |  |  | **F** |
| Safety-Critical Software Determination |  | **P** | **B** | **U** | **U** | **U** | **U** |  |  |  | **F** |
| Software Classification Determination |  | **P** | **B** | **U** | **U** | **U** | **U** |  |  |  | **F** |
| Software Assurance schedule |  | **P** | **P** | **P** | **B** | **U** | **U** |  |  |  |  |
| IV&V Project Execution Plan (if required) - [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |  | **P** | **P** | **P** | **P** | **B** | **U** | **U** | **U** | **U** | **F** |
| IV&V Project risk assessment  (if required) | **P** | **B** | **U** | **U** | **U** | **U** | **U** | **U** | **U** |  |  |
| Software Assurance Product Acceptance Criteria and Conditions |  |  | **P** | **P** | **B** | **U** | **F** |  |  |  |  |
| Software Assurance Requirements Analysis - [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) |  | **P** | **B** | **U** | **U** | **U** | **U** | **U** | **U** | **U** | **F** |
| Software Assurance and Software Safety hazard analysis - [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |  |  | **D** | **P** | **P** | **B** | **U** | **U** | **U** | **U** | **F** |
| Software Assurance safety analysis - [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |  | **D** | **D** | **P** | **P** | **B** | **U** | **U** | **U** | **U** | **F** |
| Software Assurance design analysis - [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) |  |  |  | **P** | **P** | **P** | **B** |  |  |  | **F** |
| Software source code quality analysis - [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) |  |  |  |  |  |  |  | **B** | **U** |  | **F** |
| Software Assurance Testing/Verification Activities Analysis - [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |  |  |  |  |  |  |  | **P** | **B** | **U** | **F** |
| Software Static Code Analysis |  |  |  |  |  |  |  | **P** | **B** |  | **F** |
| Analysis showing software code coverage percentage for safety-critical code |  |  |  |  |  |  |  | **P** | **B** | **U** | **F** |
| Analysis showing software Cyclomatic Complexity for safety-critical code |  |  |  |  |  |  |  | **P** | **B** |  | **F** |
| Security vulnerabilities and security weaknesses analysis |  |  |  |  |  |  |  |  | **B** | **U** | **F** |
| SA analysis of software volatility measures |  |  | **X** | **U** | **U** | **U** | **U** |  |  |  |  |
| **Ongoing activities** | MCR | SRR | SwRR | MDR | SDR | PDR | CDR | SIR | TRR | SAR | ORR |
| Software Process Root Cause Analysis results |  |  | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** |
| Software risks, findings, or known issues |  |  | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** |
| Evaluation of software changes |  |  | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** |
| Software Assurance status reports, including Software Assurance metric analysis - [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) |  | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** |
| Participation in Software Peer reviews |  | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** |
| Software Assurance process Audits and Assessments - See Schedules in Topic [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |  | **PPS** | **PPS** | **PPS** |  | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** |
| Software test witnessing |  |  |  |  |  |  |  | **PPS** | **PPS** | **PPS** | **PPS** |
| Software Assurance participation in milestone product reviews | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** | **PPS** |

Legends

**Maturity Types**

**F** = Final,  **D** = Draft,  **P** = Preliminary,  **B** = Baseline,  **U** = Updated/Updated as required,  **X** = assume complete (final),   
**PPS** = Per Project Schedule or Software Assurance Schedule as appropriate

**Review Types**

|  |  |  |
| --- | --- | --- |
| **MCR** = Mission Concept Review, | **SRR** = System Requirements Review | **SwRR** = Software Requirements Review |
| **MDR** = Mission Definition Review | **SDR** = System Definition Review | **PDR** = Preliminary Design Review |
| **CDR** = Critical Design Review | **SIR** = System Integration Review | **TRR** = Test Readiness Review |
| **SAR** = System Acceptance Review | **ORR** = Operational Readiness Review |  |

See also [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking), [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria), [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis),

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the  [Additional Guidance tab](#tabs-2)  in the Resources tab.

# 2. References

## 2.1 References

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

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking)        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) * [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) * [A.09 Software Risk Management](/spaces/SWEHBVD/pages/133235385/A.09+Software+Risk+Management) * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) |

# 3. Lessons Learned

### 3.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 3.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
