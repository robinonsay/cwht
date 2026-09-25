# SWE-095 - Report Engineering Discipline Status

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695482. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status

SWE-095 - Report Engineering Discipline Status

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695482)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695482&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

# 1. Requirements

2.1.5.5 The Center Director, or designee, shall report on the status of the Center’s software engineering discipline, as applied to its projects, upon request by the OCE, OSMA, or OCHMO.  

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-095 History

SWE-095 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.4.6 Each NASA Mission Directorate shall establish its own software measurement system to include the minimum reporting requirements in SWE-091. |
| Difference between A and B | Re-write of requirement.  Rev A requirement content merged into SWE-091. Rev B requirement is for SWE to report on the status of the discipline. |
| B | 2.1.3.7 The Center Director or designee shall periodically report on the status of the Center’s software engineering discipline as applied to its projects, to the NASA Office of Chief Engineer and relevant Technical Authorities as requested. |
| Difference between B and C | Removed "periodically" from reporting;  Removed "relevant Technical Authorities" and inserted "OSMA". |
| C | 2.1.5.7 The Center Director, or designee, shall report on the status of the Center’s software engineering discipline, as applied to its projects, upon request by the OCE or OSMA. |
| Difference between C and D | Added OCHMO |
| D | 2.1.5.5 The Center Director, or designee, shall report on the status of the Center’s software engineering discipline, as applied to its projects, upon request by the OCE, OSMA, or OCHMO. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The intent of the requirement is for the Centers to allow the NASA Office of the Chief Engineer (OCE) and relevant Technical Authorities (TA) to assess the status of NASA software improvement initiatives, measurement data, and workforce data, to address internal and external questions asked of the software community, to identify efficiencies in software engineering workflows, to facilitate collaboration between Centers, and to address Agency cost savings studies and questions.

## 2.1 Purpose of the Requirement:

This requirement ensures that key stakeholders within NASA—namely the Office of the Chief Engineer (OCE), Office of Safety and Mission Assurance (OSMA), and Office of the Chief Health and Medical Officer (OCHMO)—have access to an up-to-date status of the software engineering discipline at each Center. This reporting process supports oversight, accountability, and the continuous improvement of software engineering practices across the Agency.

By mandating Center-level reporting, this requirement:

1. **Promotes Organizational Accountability:** Ensures that Centers actively maintain software engineering excellence and are accountable for their compliance with NASA’s software-related policies and directives.
2. **Facilitates Oversight and Risk Management:** Provides a mechanism for higher-level leadership to monitor alignment with safety, mission assurance, and engineering standards, while identifying and mitigating emerging risks.
3. **Supports Process Improvements:** Allows the OCE, OSMA, and OCHMO to assess the effectiveness of the Center’s processes and recommend improvements to meet Agency-wide goals.
4. **Promotes Consistency Across Centers:** Ensures that all Centers are adhering to NASA software engineering frameworks (e.g., **NPR 7150.2** [083](#_tabs-<p></p>)).

## 2.1 Key Rationale for the Requirement

### 1. Ensures Agency-Wide Consistency and Compliance

* Software engineering plays a critical role in NASA’s mission success, with software used in everything from spaceflight systems to science instrumentation and ground support operations. By reporting the status of their software engineering discipline:
  + Centers demonstrate compliance with NASA policies such as **NPR 7150.2: Software Engineering Requirements** and **NPR 7120.5: NASA Space Flight Program and Project Management Requirements**  [082](#_tabs-<p></p>).
  + Agency leadership can identify gaps or inconsistencies in how Centers interpret and implement software engineering practices.
* **Example Scenario:** If one Center applies design and testing processes differently, inconsistencies may lead to integration risks and jeopardize multi-Center collaborations. Regular reporting ensures alignment among Centers and enhances the reliability of software-dependent systems.

### 2. Allows Proactive Risk Identification and Mitigation

* Reporting provides insight into the health of software engineering practices at the Center, including areas where:
  1. Resource gaps exist (e.g., staffing shortages, training issues, tools deficits).
  2. Specific projects face risks tied to software complexity, classification, or safety-criticality.
  3. Tailoring, waivers, or deviations may require additional scrutiny.
* Organizations such as OSMA and OCHMO use these reports to:
  + Verify that processes are in place to control safety-critical risks (e.g., [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)—software assurance, safety, and verification workflows).
  + Address emergent risks, such as cybersecurity threats tied to software vulnerabilities.
* **Example Impact:** For Centers involved in human spaceflight, the status report can highlight areas where safety-critical software assurance practices (such as test coverage for human-rated systems) require reinforcement before an issue compromises crew safety.

### 3. Supports Continuous Improvement of Software Engineering Processes

* Status reports are an opportunity for Centers to:
  + Showcase successes and areas of innovation in software development or assurance practices.
  + Identify persistent challenges that may warrant external assistance, additional resources, or process reengineering.
* The **OCE**, in particular, relies on these reports to maintain an understanding of the Center’s strengths and weaknesses, enabling NASA to:
  + Develop corrective actions across all Centers when systemic challenges are identified.
  + Allocate resources for training, tools, or mentorship programs targeting specific areas of need.
* **Example:** If a report highlights frequent tailoring of critical software requirements, this could prompt the OCE to evaluate whether the requirement itself needs revision to better serve NASA’s mission goals.

### 4. Enhances Transparency and Collaboration Across Offices

* This requirement holds the Center accountable not only to its internal leadership but also to NASA-wide stakeholders responsible for maintaining engineering, safety, and health standards. These offices work together to:
  + Align software engineering best practices with strategic objectives.
  + Ensure that Centers follow consistent criteria when conducting software assurance, risk management, and verification.
  + Identify and resolve cross-functional issues across Centers.
* **Impact:** This communication creates an open and transparent structure where actionable feedback can flow between Centers and headquarters.

### 5. Fosters a Culture of Accountability

* Regular reporting reminds Centers of their responsibility to maintain robust software engineering practices through compliance, process improvement, and allocation of adequate resources. This requirement:
  + Promotes a proactive mindset of self-assessment and adherence to NASA standards.
  + Reinforces that software plays a significant role in supporting mission-critical objectives and mitigating operational vulnerabilities.
* **Real-World Context:** Lessons from past mission mishaps, such as the **Mars Climate Orbiter** and **Mars Polar Lander**, highlight the consequences of failing to manage accountability at the organizational level. Reporting on software discipline serves as a key control mechanism for addressing these challenges early.

### 6. Promotes Safety and Mission Success

* Both OSMA and OCHMO rely on these reports to ensure that Centers are following processes to deliver safe, secure, and reliable software. Additionally:
  + Reports provide assurance that requirements for testing, verification, configuration management, problem reporting, and risk mitigation (e.g., [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) and [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures)) are being properly implemented.
  + Centers are expected to demonstrate how software safety-criticality is managed—including compliance with requirements for high-risk software.
* **Example Application:** Reporting on the safety-critical software discipline allows OSMA and OCHMO to confirm procedures that ensure the health and safety of astronauts, ground personnel, and the public.

### 7. Addresses Emerging Issues (e.g., Cybersecurity)

* Reporting mechanisms allow Centers to address and flag emerging issues—including cybersecurity risks, changes in technology tools, or gaps in workforce expertise. These reports provide NASA leadership the ability to:
  + Monitor cybersecurity policies and practices embedded within software engineering processes.
  + Identify and prioritize funding, resources, or training to meet emerging challenges.
* **Example:** If a Center identifies deficiencies in secure coding practices (aligned with [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access)), reporting to the OCE provides the opportunity for cross-Center collaboration and resolution.

### 8. Provides a Baseline for Evaluations and Reviews

* NASA and its stakeholders often perform evaluations or reviews of software-affected projects (e.g., lifecycle milestones like PDR/CDR, compliance audits, or lessons-learned analyses). A Center’s compliance with this requirement ensures readiness by:
  + Providing a clear overview of its software capabilities, successes, and challenges.
  + Demonstrating that the software engineering discipline meets Agency requirements.
* **Impact:** Reporting strengthens NASA’s ability to evaluate and ensure readiness for critical reviews while avoiding surprises that could jeopardize program schedules or budgets.

## 2.3 Historical Context and Supporting Examples

1. **Mars Climate Orbiter (1999):**
   * Lack of proper oversight resulted in an integration error with catastrophic mission failure.
   * Reporting on software engineering discipline would ensure organizational risks are flagged early for resolution.
2. **James Webb Space Telescope (2019):**
   * Poorly assessed software risks early in the lifecycle contributed to delays and cost overruns.
   * Status reports could have introduced a mechanism for the OCE and OSMA to monitor issues and address them sooner.
3. **Columbia Space Shuttle Accident (2003):**
   * A lack of transparency in engineering processes contributed to systemic blind spots.
   * Reporting requirements promote regular oversight to avoid organizational failures.

## 2.4 Conclusion

This reporting requirement ensures Centers provide transparency and accountability in their software engineering discipline, which forms the backbone of NASA’s mission-critical success. By facilitating oversight, mitigating risks, and fostering continuous improvement, these status reports create a structured pathway for aligning software development across the Agency with safety, mission assurance, and engineering excellence. This practice is essential for maintaining NASA’s leadership in space exploration and protecting the safety and reliability of its systems.

# 3. Guidance

## 3.1 Status of the Center’s Software Engineering Discipline

In addition to the reporting and access requirements for measurement data at the Center level described in [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis), periodic Agency-level reporting of the status of the Center’s software engineering discipline as applied to its projects is also required.  This data may be requested by the NASA OCE or relevant TAs to help them obtain high-level views of the Agency’s software engineering discipline.

Typically requests, made once or twice each year, can be expected to include:

* Project **NPR 7150.2**[083](#_tabs-<p></p>) compliance matrices.
* CMMI assessment status, schedule, and findings.
* Contractor CMMI assessment status, schedule, and findings.
* NPR issues and suggestions.
* Training status.
* Software organization improvement goals and metrics.
* Software metrics.
* Project status and risks.

Responses to NASA OCE or relevant TAs can take the form of email, face-to-face meetings, presentations, spreadsheets, reports, or any other format that provides the requested information in a manner that the OCE or TA can understand the data being provided.  If a specific format is desired, the OCE representative or TA will include that information in the request.

See also [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository), Topic [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report),

See also [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) for the requirement on the Software Engineering Initiative.

See also Topic [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) for additional details on the SPI Initiative.

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

While small projects might have fewer resources, reduced complexity, and lower levels of mission-criticality compared to larger projects, they are still required to comply with periodic reporting on the status of their software engineering practices. This guidance provides small projects with practical steps to fulfill the requirement effectively and efficiently.

Small projects play a critical role in supporting mission objectives and enabling larger systems; however, their size does not absolve them from adhering to NASA software engineering standards. Reporting at the Center level ensures that all projects, regardless of size, contribute to organizational accountability, transparency, and risk mitigation.

For small projects, the key is to streamline reporting practices, leverage lightweight tools, and focus on the most essential and relevant aspects of the software engineering discipline, while minimizing unnecessary overhead.

## 4.1 Guidance for Small Projects

### 4.1.1. Focus on Relevant Metrics and Data

Small projects often have reduced scope, so their reporting should focus on key elements requested by the OCE, OSMA, or OCHMO. Small-scale reporting should prioritize:

* **Compliance Matrices:** Highlight **NPR 7150.2**[083](#_tabs-<p></p>) compliance for the project (using [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) compliance matrices) to show alignment with software engineering requirements.
* **Training:** Report training compliance for personnel involved in the software effort—use simple checklists or logs.
* **Project Status:** Provide high-level information on project milestones, risks, and critical challenges (specific to software).
* **Risks:** Prioritize reporting on risks involving safety-critical software and organizational challenges, such as resource gaps.

#### Example Simplified Metrics for Small Projects:

* Number of completed software testing activities (unit, integration, system-level).
* Percentage of requirements verified and validated to date.
* Current defect density or known software risks with mitigation plans.
* Training completion rates for team members working on software development and assurance tasks.

### 4.1.2. Leverage Lightweight Tools and Processes

Small projects can utilize streamlined tools and processes for tracking, documenting, and reporting their software engineering discipline. Examples include:

* **Configuration and Compliance Tracking Tools:**
  + Use simple spreadsheets (e.g., Excel or Google Sheets) or lightweight compliance tools to track **NPR 7150.2** requirements.
  + Leverage project management software (e.g., Trello, Asana) to manage software tasks and risks.
* **Testing and Metrics:**
  + Perform software testing using open-source or small-scale tools such as Pytest for Python or JUnit for Java.
  + Use simple tools for defect management (e.g., GitHub Issues or Jira for tracking bugs and risks).
* **Training Records:**
  + Keep lightweight logs of team participation in required training programs: Microsoft Word tables or even email tracking can suffice.

### 4.1.3. Address NPR 7150.2 Compliance

For small projects, the compliance matrix ([SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)) is a key document describing adherence to **NPR 7150.2** software engineering requirements. Small projects should:

* Generate a concise compliance matrix that highlights tailored requirements and waivers.
* Summarize compliance challenges (e.g., resource limitations, safety-critical risks).
* Demonstrate how tailored requirements align with project-specific needs and risk tolerances.

### 4.1.4. Focus on Risks and Critical Challenges

Small software projects are often constrained by limited resources, staff, or complexity. Reporting should focus on:

* **Safety-Critical Software Risks:** Ensure that shallow or simplified processes do not create systemic risks for software critical to human or mission safety.
* **Resource Gaps:** Highlight resource constraints (e.g., team size, tool availability) that might impact compliance and quality.

### 4.1.5. Use Streamlined Reporting Formats

Small projects can reduce overhead while fulfilling reporting obligations by using simplified formats:

* **Emails:** Use brief email updates for simple metrics and status reporting.
* **Spreadsheets:** Use a single Excel spreadsheet or table format for metrics, risks, and compliance matrices.
* **Slides or Presentations:** Prepare concise PowerPoint presentations (5–10 slides) for face-to-face or virtual meetings, summarizing high-level data.
* **Standardized Templates:** Request reporting templates from the **Center Process Asset Library (PAL)**[197](#_tabs-<p></p>) or technical authorities at your Center.

### 4.1.6. Proactively Prepare for Requests

Small projects should maintain up-to-date records to minimize disruption when requests for reporting arise. Recommended practices:

* Assign a single point of contact (POC) responsible for software-related reporting and compliance tracking.
* Consistently update compliance matrices, defect logs, training records, and risk registers during regular project reviews.
* Store relevant documents in accessible repositories (e.g., shared drives, NASA’s Engineering Information Management System).

## 4.2 Checklist for Small Project Reporting

| Step | Action |
| --- | --- |
| **Compliance Tracking** | Ensure up-to-date compliance matrices for all **NPR 7150.2** requirements. |
| **Training Records** | Maintain logs of personnel training relevant to software engineering requirements. |
| **Defect and Risk Metrics** | Keep an updated register of known defects and risks and their mitigation statuses. |
| **Tool Usage** | Use lightweight software tools for testing, version control, and issue tracking. |
| **Tailoring Notes** | Document rationale for tailored requirements or waivers approved for the project. |
| **Report Preparation** | Prepare simplified reports (emails, slide decks, spreadsheets) for periodic reviews. |
| **Stakeholder Coordination** | Assign a POC for software reporting and coordinate with the Center Director or designee. |

## 4.3 Example Report Structure for Small Projects

#### Email Example:

Subject: Status of Small Project [Project Name] – Software Engineering Discipline  
Body:

1. **Compliance Status:**
   * **NPR 7150.2** Compliance Matrix: 90% of requirements verified, 10% tailored or waived.
   * Waivers: Rationale and approval documented in the compliance matrix.
2. **Metrics Summary:**
   * Defect Density: [X defects per KLOC]
   * Test Completion: 95% of planned tests completed (unit and integration).
3. **Key Challenges:**
   * Constraint: Limited resources impacting code validation workflow.
   * Mitigation: Planned schedule adjustment and automated testing integration.
4. **Training Updates:**
   * 100% of personnel completed required software assurance training.
5. **Risks:**
   * Risk ID #102: Potential delay due to third-party integration testing—mitigation plan includes simulated testing environment.

#### Spreadsheet Example:

| Category | Status/Notes |
| --- | --- |
| Compliance Matrix | 90% compliance achieved, tailoring applied to [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) and [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures)  requirements. |
| Defect Density | 5 defects per KLOC. |
| Training Completion | 100% team training achieved. |
| Current Risks | 3 known risks (1 resolved, 2 in mitigation). |
| Waivers | 2 active waivers with documented risk mitigations. |

## 4.4 Conclusion

Small projects can efficiently comply with this reporting requirement by streamlining processes, leveraging lightweight tools, focusing on high-priority metrics, and tailoring reporting formats to meet Agency needs. This approach ensures that small projects maintain compliance without adding unnecessary overhead while contributing to NASA’s mission-critical objectives for software engineering excellence.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-252)

  [Software Metrics: SEI Curriculum Module SEI-CM-12-1.1.](http://www.sei.cmu.edu/reports/88cm012.pdf "Click to open in new window")

  Mills, Everald E. (1988). Carnegie-Mellon University-Software Engineering Institute.  Retrieved on December 2017 from http://www.sei.cmu.edu/reports/88cm012.pdf.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-336)

  [Software Metrics Capability Evaluation Guide,](http://www.dtic.mil/docs/citations/ADA325385 "Click to open in new window")

  Software Technology Support Center (STSC) (1995), Hill Air Force Base. Accessed 6/25/2019.
* (SWEREF-355)

  [12 Steps to Useful Software Metrics,](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics_in_12_steps_paper.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2005),   Retrieved November 3, 2014 from http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics\_in\_12\_steps\_paper.pdf
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
* (SWEREF-577)

  [Selection and use of Software Metrics for Software Development Projects](https://llis.nasa.gov/lesson/3556 "Click to open in new window")

  Public Lessons Learned Entry: 3556.
* (SWEREF-683)

  [Anomalous Flight Conditions May Trigger Common-Mode Failures in Highly Redundant Systems](http://llis.nasa.gov/lesson/1778 "Click to open in new window")

  Public Lessons Learned Entry: 1778, Date: 2007-03-6. Submitting Organization: JPL, Submitted by: Martin Ratliff

## 5.2 Tools

## Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN).  NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN. The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Incorporating lessons learned from past projects strengthens understanding and execution of this requirement to ensure transparency, accountability, and effective reporting of software engineering disciplines. These lessons highlight how using metrics, tracking risks, and maintaining oversight enhances software quality and mitigates risks. Below are the relevant lessons learned, including **Flight Software Engineering Lessons (Lesson Number: 2218)** and its recommendations.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Flight Software Engineering Lessons - Jet Propulsion Laboratory [572](#_tabs-<p></p>)

* **Lesson Number:**2218
* **Key Issue:**  
  Developing flight software (FSW) for JPL spacecraft projects is resource-intensive and accounts for significant mission cost and schedule. Defects in the FSW development process represent a major risk to mission success. Software verification adequacy and tracking software development progress are critical to mitigating these risks.
* **Applicable to This Requirement:**
  + Regular reporting on software engineering discipline provides the necessary visibility into software development, verification, and testing activities to ensure risks in FSW are addressed early and thoroughly.
  + Incorporating **objective metrics** into reports allows the OCE, OSMA, or OCHMO to monitor progress, quality, and risk in FSW development.
* **Lesson Learned & Recommendation:**
  + Use **specific and objective measures** to monitor FSW development and verify progress to mitigate the risks from defects. Include the following in reporting:
    - **Percentage of Code and Requirements Tested:** Tracks how much of the system has been verified through code testing relative to requirements.
    - **Test Pass Rates:** Measures the percentage of passed tests in simulated environments, integration testbeds, and under stress scenarios.
    - **Development Progress Metrics:** Report on the number of software units:
      * With allocated requirements and baselined detailed designs.
      * Where coding is complete.
      * That have passed all unit testing in both simulated and testbed environments.
    - **Verification and Validation (V&V) Completion:** Tracks whether FSW has passed its verification milestones and stress testing benchmarks.
* **Connection to the Requirement:**
  + Reporting these measures during regular status updates can improve visibility into high-priority development efforts like FSW. Oversight authorities can use this information to assess the quality of software development, identify areas requiring leadership attention, and prevent delays or defects that might impact mission-critical functionality.

#### 2. Selection and Use of Software Metrics for Software Development Projects [577](#_tabs-<p></p>)

* **Lesson Number:** 3556
* ***(See full case details above)***
* **Reinforcement:**  
  Metrics are essential for status reporting, particularly in monitoring project health and ensuring efficiencies. The Flight Software Engineering Lesson's emphasis on testing progress, requirements verification, and unit testing completion complements the recommendation in **Lesson Number 3556** to track defect rates, requirement changes, and labor allocation as part of Center-level reports. Together, these lessons highlight that tailored, metrics-driven reporting is essential to project success.

#### 3. Mars Climate Orbiter Mishap [529](#_tabs-<p></p>)

* **Lesson Number:**LLIS-0938
* **Key Issue:**  
  The unit conversion error that caused the Mars Climate Orbiter failure stemmed from a lack of oversight and status transparency, which might have been mitigated if metrics (e.g., verification progress) had been part of a structured reporting process.
* **Relevance:**  
  Including metrics on FSW verification (as detailed in Lesson 2218) in periodic reports would allow oversight organizations to detect risks like incomplete testing, unverified requirements, or quality control issues.

#### 4. James Webb Space Telescope Software Risk Mitigation

* **Lesson Number**: LLIS-4646
* *(See full case details above)*
* **Reinforcement:**  
  **Lesson 2218** provides specific measures (e.g., code coverage, verification percentage, successful stress tests) that could have been used to enhance tracking on JWST software. Incorporating these metrics into Center-level reporting ensures leadership can monitor risks and proactively address bottlenecks.

#### 5. Columbia Space Shuttle Accident Organizational Lessons

* **Lesson Number**: LLIS-3326
* **Key Issue:**  
  The lack of reporting and visibility into key engineering disciplines, including software, led to missed opportunities to address risks that significantly contributed to the Columbia tragedy.
* **Relevance:**  
  By reporting FSW metrics and verification progress (as recommended in Lesson 2218), Centers can provide oversight authorities with greater confidence in software quality, V&V progress, and risk mitigation—greatly improving mission safety.

#### 6. Mars Polar Lander Software Error [683](#_tabs-<p></p>)

* **Lesson Number**: LLIS-1778
* **Key Issue:**  
  Incomplete software testing and integration led to a mission failure that could have been identified through more rigorous oversight and better transparency during the development lifecycle.
* **Relevance:**  
  Metrics-driven reporting, as recommended in Lesson 2218, would have provided oversight on gaps in test coverage and V&V adequacy, highlighting the need for additional testing focus.

### 6.1.2  Practical Application of Lessons (Focus on Flight Software Metrics and Reporting):

#### Incorporating Key Metrics into Status Reports:

When reporting the status of the Center’s software engineering discipline—especially for projects involving flight software—include these key metrics derived from Lesson 2218 and complementary lessons:

1. **Verification and Validation Metrics:**
   * Percentage of FSW requirements verified.
   * Percentage of tests passed:
     + **Unit Testing:** Simulation environment and integration testbeds.
     + **Stress Testing:** Completion of performance tests under simulated mission scenarios.
   * Number of unresolved faults/defects in software verification activities.
2. **Development Progress Metrics:**
   * Number of FSW units with:
     + Baselined requirements and designs.
     + Completed coding that has passed all necessary tests.
     + Successful integration in testbed environments.
3. **Defects and Escapes:**
   * Track errors discovered during testing and the percentage of defects resolved.
   * Monitor process escapes (defects found in delivered software).
4. **Resource Alignment:**
   * Compare projected vs. actual labor hours and resource utilization.

#### Key Lessons Integration within Reports:

* Use FSW progress metrics to track compliance with **NPR 7150.2**[083](#_tabs-<p></p>) requirements for software verification (e.g., [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) and [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures)).
* Demonstrate how risks related to incomplete or inadequate testing are being addressed during software development.
* Highlight the adequacy of training resources and organizational process alignment for ongoing flight software improvements.

### 6.1.3  Conclusion: Aligning Lessons Learned with the Requirement

The **Flight Software Engineering Lessons (Lesson Number: 2218)** and **Selection and Use of Software Metrics (Lesson Number: 3556)** emphasize the value of objectively measuring development progress and verification adequacy. This aligns directly with the requirement to provide status reports on the Center’s software engineering discipline that are actionable and transparent.

By incorporating tailored, metrics-driven insights into periodic reports—such as code/test completion rates, FSW verification progress, and defect resolution—Centers can provide the oversight (OCE, OSMA, OCHMO) with critical data to monitor software process health. These lessons reinforce the role of effective reporting in ensuring mission success, preventing software risks, and maintaining accountability across NASA’s software engineering disciplines.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-095 - Report Engineering Discipline Status**

2.1.5.5 The Center Director, or designee, shall report on the status of the Center’s software engineering discipline, as applied to its projects, upon request by the OCE, OSMA, or OCHMO.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

None identified at this time.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support oversight, validate compliance, manage risks, and ensure the quality of delivered products. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

No specific deliverables are currently identified.

## 7.3 Metrics

No standard metrics are currently specified.

## 7.4 Guidance

### 7.4.1  Objective of the Guidance

This requirement ensures the Center Director—or their designee—can provide timely and comprehensive status reports on the Center’s software engineering discipline when requested by key oversight organizations: the Office of the Chief Engineer (OCE), the Office of Safety and Mission Assurance (OSMA), or the Office of the Chief Health and Medical Officer (OCHMO).

Software Assurance (SA) personnel play a vital role in supporting the creation, accuracy, and completeness of these reports. The goal is to provide clear insights into the current state of the Center’s software engineering capabilities, as applied to its projects, in areas such as compliance, performance, risk management, and quality improvement.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Support the Preparation of Status Reports

1. **Understand Report Objectives**:
   * Identify the specific information requested by OCE, OSMA, or OCHMO and tailor the report to address their expectations.
   * Common focus areas may include:
     + Compliance with NASA directives (**NPR 7150.2**[083](#_tabs-<p></p>) and software assurance standards like **NASA-STD-8739.8**[278](#_tabs-<p></p>)).
     + Software assurance practices and their effectiveness (e.g., verification and validation, risk analysis, audits).
     + Progress updates about ongoing software improvement initiatives at the Center.
2. **Gather Data on Center’s Software Engineering Discipline**:
   * Collect relevant data from the Center’s projects, such as:
     + Project classification levels and software criticality.
     + Compliance status with applicable software engineering requirements.
     + Results of software assurance audits and reviews.
     + Key metrics, such as defect density, test coverage, or anomaly resolution rates.
     + Lessons learned and process improvement efforts.
3. **Contribute to Report Content on Software Assurance**:
   * Ensure the report reflects the status of software assurance activities at the Center, such as:
     + How assurance processes are integrated into software development and maintenance.
     + Risks mitigated through assurance activities.
     + Any software assurance findings or recommendations resulting from audits, reviews, or assessments.
4. **Document Risks and Challenges**:
   * Highlight any risks, challenges, or shortfalls in the software engineering or software assurance discipline. These might include:
     + Staffing/training gaps in software assurance personnel.
     + Issues with contractor compliance with NASA standards.
     + Schedule or technical risks associated with specific software projects.

#### 7.4.2.2  Ensure the Report is Comprehensive and Accurate

1. **Validate Data Accuracy**:
   * Verify that all reported data is accurate, up-to-date, and traceable to project activities.
   * Double-check metrics, compliance statuses, and summaries for completeness.
2. **Ensure Alignment with Requirements**:
   * Validate that the software engineering processes and metrics described in the report adhere to **NPR 7150.2**, **NASA-STD-8739.8**, and all other applicable directives.
3. **Address All Stakeholder Areas of Interest**:
   * Confirm the report addresses safety (OSMA), engineering performance and compliance (OCE), and health/reliability concerns (OCHMO) as required.
4. **Include Key Achievements and Improvements**:
   * Highlight successes in improving the Center’s software engineering and assurance discipline, such as advancements in:
     + Testing technology or automation.
     + Implementation of risk mitigation strategies.
     + Process improvements based on past reviews.

#### 7.4.2.3  Facilitate Effective Coordination with Stakeholders

1. **Collaborate with Relevant Teams**:
   * Coordinate with software engineers, project managers, and assurance personnel to provide input into the report.
   * Work with leadership to ensure the Center’s approach aligns with NASA’s priorities.
2. **Review Report Prior to Submission**:
   * Validate that the final report addresses all requested items effectively.
   * Ensure software assurance-related topics are highlighted clearly and factually.
3. **Provide a Response to Follow-Up Questions**:
   * Be prepared to support or clarify the report’s contents if questions arise from OCE, OSMA, or OCHMO during or after submission.

#### 7.4.2.4  Continuously Improve Reporting Processes

1. **Capture Lessons Learned**:
   * After each report request, evaluate what information was challenging to collect or needed improvement.
   * Use feedback from oversight organizations to refine future reporting processes.
2. **Develop Proactive Tracking**:
   * Implement tools or practices for continuously tracking the status of the Center’s software engineering and assurance disciplines, ensuring readiness for future reporting requests.
3. **Support Metrics Refinement**:
   * Work with Center leadership to refine assurance and engineering metrics to better reflect discipline status and maturity over time.

### 7.4.3  Key Software Assurance Focus Areas for the Report

1. **Assurance Activities and Results**:
   * Summary of assurance tasks like V&V, peer reviews, safety assessments, and test activities.
   * Review and audit results, findings, and the status of corrective actions.
2. **Compliance Profile**:
   * Status of the Center’s compliance with software engineering directives and standards.
   * Tailoring decisions documented and approved per NASA policies.
3. **Risk and Issue Management**:
   * Status of software-related risks for ongoing projects.
   * Issues encountered and resolved, particularly those that impacted safety-critical software.
4. **Improvements and Training**:
   * Updates on initiatives to improve software and assurance processes.
   * Training programs conducted to enhance the Center’s software assurance capabilities.
5. **Support for Contractor Oversight**:
   * Assurance-related monitoring of contractors, including compliance tracking and results of external audits.

### 7.4.4  Expected Outcomes

Through the diligent preparation of reports, Software Assurance personnel will:

1. Ensure the accuracy and completeness of the Center’s status report on software engineering and assurance disciplines.
2. Provide oversight organizations (OCE, OSMA, OCHMO) with transparent and detailed insights into performance, compliance, and risks.
3. Support Center leadership by identifying strengths, challenges, and areas for improvement within the software engineering and assurance discipline.
4. Demonstrate mission readiness and adherence to NASA’s high standards for software quality, safety, and reliability.

### 7.4.5  Summary

To fulfill this requirement, Software Assurance personnel must support the Center Director, or designee, by:

* Collecting, verifying, and documenting accurate information on the status of the Center’s software engineering and assurance disciplines.
* Highlighting strengths, compliance, and mitigation of risks, while identifying areas requiring improvement or further attention.
* Ensuring the report effectively addresses stakeholder needs (OCE, OSMA, OCHMO) and complies with all applicable directives.

Proactive planning, consistent monitoring, and continuous improvement of reporting processes will ensure the Center is always prepared to meet reporting requests efficiently and effectively.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) |
