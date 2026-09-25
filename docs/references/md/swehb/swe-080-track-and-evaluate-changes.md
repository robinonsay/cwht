# SWE-080 - Track and Evaluate Changes

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695459. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes

SWE-080 - Track and Evaluate Changes

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695459)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695459&showCommentArea=true&showComments=true#addcomment)

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

5.1.3 The project manager shall track and evaluate changes to software products.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-080 History

SWE-080 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.1.2 The project shall track and evaluate changes to software products. |
| Difference between A and B | No change |
| B | 5.1.3 The project manager shall track and evaluate changes to software products. |
| Difference between B and C | No change |
| C | 5.1.3 The project manager shall track and evaluate changes to software products. |
| Difference between C and D | No change |
| D | 5.1.3 The project manager shall track and evaluate changes to software products. |

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
| * [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) |

# 2. Rationale

As software teams design, develop, and deploy software, it is common for multiple versions of the same software to be used on different sites and for the software developers to be working simultaneously on updates. Bugs or defects in the software are often only present in certain versions (because of the fixing of some problems and the introduction of others as the program develops). Therefore, to locate and fix bugs, it is important to be able to retrieve and run different versions of the software to determine in which version(s) the problem occurs. It may also be necessary to develop two versions of the software concurrently (for instance, where one version has bugs fixed, but no new features, while the other version is where new features are developed.  Change requests address not only new or changed requirements but also failures and defects in software products. Change requests are analyzed to determine the impact that the change will have on the software product, related software products, the budget, and the schedule. Tracking and evaluating changes are useful for a variety of reasons, not the least of which is to maintain documented descriptions of problems, issues, faults, etc., their impact on the software and system, and their related resolutions. Evaluating changes allows key stakeholders to determine the cost-benefit of implementing changes and to make decisions based on that information.

Effective software development and maintenance depends on managing change. This requirement ensures that software products are consistently modified in a controlled and deliberate manner, providing traceability, accountability, and evaluation of the impact of every change. Software is rarely static, and as projects evolve, requirements, features, defects, and environments change, leading to necessary updates and modifications. Tracking and evaluating these changes helps maintain consistency, quality, and alignment with project goals.

Below is the rationale for this requirement, organized into several key points:

---

### **1. Maintain Software Integrity and Quality**

* Changes to software products, whether they involve updating source code, modifying design documents, or revising test plans, must be tracked to ensure that the final product behaves as expected.
* Tracking and evaluating changes prevents unauthorized, incomplete, or incorrect modifications, which could introduce defects or inconsistencies in the software.
* A well-documented change history creates a roadmap to identify and fix issues when anomalies arise. It ensures software integrity across its lifecycle, reducing the likelihood of introducing new errors while addressing existing issues.

---

### **2. Enable Traceability**

* Traceability is critical to ensure that every change aligns with project objectives, requirements, standards, and user needs.
* Tracking changes ensures that updates can be mapped to specific features, requirements, or defects. This is especially important for **safety-critical systems**, where every change must be clearly linked to safety requirements or risk assessments.
* Change traceability allows teams to understand "why" a change was made, "what" the change involved, and "who" authorized or implemented it. This helps in debugging, auditing, and ensuring accountability.

---

### **3. Risk Management**

* Every change introduces the risk of unintended impacts. By **evaluating** changes before they are implemented, project managers can:

  + Assess the potential impact on system performance, safety, and reliability.
  + Identify possible conflicts with other software components or requirements.
  + Prevent changes that could introduce vulnerabilities or instability.
* Rigorous evaluation of changes enables stakeholders to make **informed decisions** about whether a particular change should be approved, modified, or rejected, reducing the risk of costly errors later in the project.

---

### **4. Support Controlled Evolution of Software**

* Software is designed to evolve over time to meet new requirements, fix defects, or adapt to changes in hardware, external libraries, or operating environments. A project manager's responsibility to track and evaluate changes ensures that this evolution occurs **in a controlled manner**.
* Without proper tracking, software change history can become fragmented and undocumented, leading to:

  + Confusion among team members.
  + Difficulties in accurately rolling back to previous versions if a change introduces problems.
  + Challenges in re-creating builds, baselines, or releases.
* Controlled evolution reinforces consistency and ensures confidence in future releases, limiting the chance of regression issues or incomplete deliveries to end users.

---

### **5. Ensure Compliance with Standards and Regulations**

* For **safety-critical systems** and projects governed by specific industry standards (e.g., aerospace, medical devices), tracking and evaluating software changes is essential to demonstrate compliance. Regulatory bodies (e.g., NASA, FAA, FDA) often require:
  + Complete documentation of what changes were made, why they were made, and how they were tested.
  + Records demonstrating that changes were reviewed and approved by authorized personnel.
* Failure to track changes could lead to non-compliance, delays, and increased costs.

---

### **6. Facilitate Collaboration and Communication**

* Software development often involves multiple team members, sometimes across geographically dispersed locations. Without tracking changes, collaboration becomes chaotic, leading to:

  + Duplicate efforts or conflicts when developers work on the same component without knowledge of overlapping work.
  + Disputes over ownership of changes and accountability for errors.
* A clear process for tracking changes fosters transparency, enabling team members to:

  + Stay informed about recent modifications.
  + Collaborate effectively on shared resources.
  + Communicate the impact of changes to stakeholders in a structured, actionable way.

---

### **7. Support Efficient Issue Resolution**

* Every software project faces challenges such as bugs, defects, or operational issues. Tracking and evaluating changes ensures that the project team can:

  + Pinpoint which change caused an issue (e.g., which code commit introduced a defect).
  + Roll back to previous working versions if necessary.
  + Avoid repeating mistakes during future changes by reviewing historical impacts.
* This level of oversight minimizes downtime when problems occur and facilitates quick resolution, particularly in mission-critical systems.

---

### **8. Enhance Reusability and Knowledge Retention**

* Software knowledge doesn’t always remain with individuals—team turnover or transitions are common in long-term projects. Without proper change tracking and evaluation:

  + New team members may struggle to understand the evolution of the software product.
  + Efforts to reuse software components may fail due to undocumented or poorly tracked changes.
* A well-documented change history ensures that knowledge is retained and shared across team transitions, enabling reusability and scalability for future projects.

---

### **9. Support Metrics Collection and Process Improvement**

* Tracking changes provides valuable data for analyzing team performance and improving processes:

  + How many changes are being made per cycle?
  + Which changes were rejected during evaluation and why?
  + What types of changes (e.g., bug fixes, feature enhancements, refactoring) dominate the lifecycle?
* These insights allow the project manager to identify bottlenecks, inefficiencies, or areas needing process improvement.

---

### **10. Alignment with NASA Best Practices**

* NASA has emphasized Configuration Management (CM) as a cornerstone of software management, and tracking changes to software products is a critical part of CM. Lessons learned (e.g., NASA Lessons Learned Database #0838, #1023, and #1481) show that weak or inadequate change tracking processes can lead to issues such as:
  + Untraceable errors.
  + Operational disruptions.
  + Increased cost and schedule overruns.

Adhering to the requirement to track and evaluate changes aligns with NASA’s best practices and lessons learned, ensuring project success and reducing risks.

---

### **Summary**

This requirement exists to ensure that software changes are effectively managed, properly documented, and carefully evaluated to maintain the quality, integrity, and reliability of the software product. By tracking and evaluating changes, project managers can:

* Manage risk.
* Ensure compliance and accountability.
* Improve collaboration and efficiency.
* Maintain traceability and quality of the software.

Ultimately, this requirement supports project success by reducing the likelihood of errors, improving process maturity, and enabling the software to evolve in a controlled and predictable manner.

# 3. Guidance

## 3.1 Tracking And Evaluating Changes

Tracking and evaluating changes occurs throughout the project life cycle and applies to all software providers, internal and subcontracted.

Tracking and evaluating changes is a critical process that spans the entire project lifecycle. It ensures that all modifications to software products are systematically controlled, evaluated for impact, and executed in an efficient and traceable manner. This applies to all software providers, including both internal teams and subcontractors.

#### **Reference to Change Control Process**

The **NASA Systems Engineering Handbook (NASA/SP-2007-6105, Rev1)** provides a flowchart outlining a "typical" change control process. This flowchart highlights key activities, roles, and responsibilities for capturing and tracking changes. It offers a strong foundation for projects establishing new change control processes and aligns with best practices for configuration management and software assurance.

Key components of the flowchart include:

* Preparing the change request form.
* Evaluating the impact and feasibility of the requested change.
* Tracking the requested change through the change control system.

Additional related guidance is available in this Handbook, including:

* **SWE-083** - Configuration Status Accounting.
* **SWE-053** - Manage Requirements Changes.
* **SWE-187** - Control of Software Items.
* **SWE-024** - Plan Tracking.
* **SWE-179** - IV&V Submitted Issues and Risks.

## 3.2 Considerations for Capturing the Change

Changes can originate from multiple sources and apply to a wide range of software products, such as specifications, requirements, design, code, databases, test plans, user documentation, and operational software. Common scenarios prompting change requests include:

* Discrepancies, defects, or failures.
* Reconfiguration changes, including routine operational software updates.
* System upgrades or improvements.
* Enhancement and feature requests.

#### **How to Capture a Change Request:**

1. **Use a Predefined Format:**

   * Document change requests on a standardized change request (CR) form or through a problem report system. This ensures all relevant details are captured and formatted for easy processing and evaluation.
   * Include key information such as origin, description, reason for the change, impacted areas, urgency/priority, and affected baselined products.
2. **Utilize a Change Tracking System:**

   * If available, track changes using a robust system designed to log, monitor, and trace changes through their lifecycle. Tools such as PRACA (Problem Reporting and Corrective Action) systems are commonly used, especially for operational software.
3. **Who Can Submit Requests:**

   * Change requests may come from various stakeholders, including developers, testers, end-users, help desk personnel, or others with system access and project authorization.

#### **Change Capture Best Practices:**

* **Separate CRs for Each Change:**
  + Ensure each change request or problem report addresses a single issue or modification to maintain clarity and avoid confusion during evaluation.
* **Guide Request Submission:**
  + Use forms or automated systems that prompt submitters to include all required details (source, problem description, impact areas, etc.), reducing incomplete or unclear requests.

For additional guidance:

* See **5.01 - CR-PR - Software Change Request - Problem Report**.

## 3.3 Considerations for Evaluating the Change and Suggested Solution

To evaluate a change effectively, the project team must analyze its technical, managerial, and operational impacts, weighing the costs and benefits, including safety, schedule, and quality implications. Evaluation should involve appropriate stakeholders such as procurement, software assurance, risk management, and project leadership.

#### **Key Aspects of Change Evaluation:**

1. **Project Impact Analysis:**

   * Assess the potential impact on schedule, cost, resources, and risks.
   * Define and evaluate impacts to other groups, interfaces, and baseline items (e.g., design, requirements, test plans).
   * Use traceability matrices to track changes through associated products.
2. **Cost-Benefit Analysis:**

   * Analyze the advantages and tradeoffs of implementing the change.
   * For example, changes from high-visibility customers may require management decisions, while less critical requests for minor issues may be deferred based on cost/value analysis.
3. **Safety and Risk Evaluation:**

   * Ensure software assurance and safety personnel evaluate changes for their potential impact on safety-critical software and hazardous functions.
   * Consider these questions:
     + Does the change create new hazards or alter existing hazard controls?
     + Does it negatively affect system safety or software reliability?
   * Include system-level hazard evaluations and necessary safety mitigations in the decision-making process.
4. **Alignment with Scope and Requirements:**

   * Verify whether the change is within the scope of the project and aligned with mission objectives or project requirements.
   * Evaluate its impact on functionality, features, performance, reliability, scalability, and overall quality.
5. **Technical and Alternative Solutions:**

   * Consider alternative approaches to solve the reported problem or implement the requested enhancement.
   * Evaluate the size, complexity, and priority level of the change to determine the optimal implementation path.

#### **Documentation and Decision Capture:**

* Record all evaluation results in detail, including impact analyses, action items, and decisions related to each requested change.
* Resolve whether the request is approved, deferred, or disapproved, and communicate decisions with stakeholders.

For related guidance:

* See **SWE-082 - Authorizing Changes**, **SWE-058 - Detailed Design**, **SWE-066 - Perform Testing**, and **SWE-071 - Update Test Plans and Procedures**.

## 3.4 Considerations for Tracking the Change

Tracking a change through its disposition (approve, defer, disapprove, etc.) is made easier if the tracking can be done as part of the same system used to capture the change request/problem report. Once disposition decisions are made, the relevant stakeholders are informed of the decisions.

Once a change has been approved, it must be tracked throughout its implementation lifecycle to maintain accountability, traceability, and consistency.

#### **Key Tracking Practices:**

1. **Change Control System:**

   * Select a change control system that aligns with the project environment and is capable of tracking changes from submission through implementation, verification, and closure.
2. **Comprehensive Records:**

   * Maintain records for every step in the process, including:
     + The original change request/problem report.
     + Results from the impact analysis and authorization decisions.
     + Approval notes and evaluation/board meeting minutes.
3. **Monitor Product Updates:**

   * Track updates made to software products, including requirements, design, code, test artifacts, specifications, and operational documents.
   * Link all related changes for traceability between configuration items and safety-critical products.
4. **Change Closeout:**

   * Close requests only after:
     + Changes are verified and validated during functional/regression testing.
     + Documentation has been updated.
     + Relevant stakeholders have approved the implementation.

#### **Change Communication:**

* Inform stakeholders of the final disposition of the request, including any unimplemented requests that may affect the future system.

#### **Status Reporting:**

* Present change status at key project reviews (e.g., lifecycle milestones), along with a summary of historical trends or open issues for informed decision-making.

For additional information:

* Refer to **SWE-079 - Develop CM Plan**.

### **Conclusion**

Tracking and evaluating changes is vital to maintaining software quality, safety, and consistency throughout the lifecycle. Structured processes for capturing, evaluating, and tracking changes ensure that projects remain under control while improving communication, reducing risks, and maintaining alignment with mission goals. Use this guidance to develop a robust change control process tailored to your project's scope and risk profile.

See also [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes), [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items), [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking), [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks),

A basic description of data management is provided in [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan).

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

# 4. Small Projects

Managing changes in small projects, where resources such as budget and personnel are limited, requires streamlining processes without compromising quality, traceability, or consistency. Small projects can achieve these goals by balancing automation, team collaboration, and simplified methods of implementation. Below is refined guidance tailored for small projects:

---

### **1. Leverage Automated Tools to Minimize Overhead**

Small projects can reduce the administrative burden associated with tracking and evaluating changes by using existing **automated change request tools**. These tools streamline the change management process and reduce the need for manual documentation while maintaining thoroughness and traceability.

* **Advantages of Automated Tools:**

  + **Reduced Costs:** Projects can use open-source or existing tools within the organization to avoid purchase and setup costs.
  + **Familiarity:** Choosing tools that team members are already skilled in reduces training time and start-up effort.
  + **Multi-Functionality:** Many automated tools provide integrated features such as change tracking, evaluation workflows, metrics collection, and reporting. This allows multiple activities to be managed in one system, saving time and reducing complexity.
* **Examples of Tools:**

  + Tools such as JIRA, Bugzilla, GitHub Issues, or Redmine can help capture, track, and manage change requests while providing a user-friendly interface for small teams.

---

### **2. Simplify the Evaluation Process**

Small projects can adopt more **informal change evaluation processes** appropriate to a smaller scale, without compromising on key areas such as impact analysis and decision-making. These streamlined processes save time while retaining accountability.

* **Incorporate Evaluation into Existing Team Meetings:**

  + Instead of holding separate meetings or forming a formal change control board (CCB), include impact analysis and discussions about changes within the context of regular team meetings.
  + Assign action items to team members as part of these meetings, replacing the need for formal evaluation reports when the scale and risks of the project allow.
* **Assign Shared Responsibilities:**

  + In smaller teams, individuals may fill multiple roles. For example, a team lead or software assurance engineer can facilitate the evaluation process to limit additional resource demands.
* **Consider Team Consensus for Small Changes:**

  + For low-risk changes, such as minor bug fixes or small updates, the team can adopt a lightweight approval process (e.g., decision by team consensus). Major changes requiring safety or performance analysis should still follow a structured evaluation.

---

### **3. Maintain Records of Changes and Decisions**

Regardless of project size, maintaining a record of changes and their associated decisions is critical for ensuring traceability, accountability, and confidence in the software product.

* **Capture Key Information:**

  + Every change should have a basic record, including:
    - The reason for the change.
    - The decision made (approved, deferred, disapproved).
    - The impact analysis (even if brief).
    - Implementation details (who performed the change, when it was completed).
    - Any final approvals or verification results.
* **Use Existing Systems for Change Tracking:**

  + Leverage lightweight tools like group spreadsheets, Trello boards, or simple database systems as an alternative to more feature-rich tools when project budgets or personnel are especially constrained.
  + Ensure that these systems allow easy updates and access by all team members.
* **Benefits of Records:**

  + Maintain a historical log of changes for future debugging, audits, or rollbacks.
  + Ensure team alignment and knowledge retention, especially as personnel roles or team structures shift.

---

### **4. Preserve Confidence in Process and Final Products**

Even with reduced formality, clear communication and consistent records are essential for small projects. Failure to properly track and evaluate changes could lead to:

* Errors being reintroduced due to poor traceability.
* Uncertainty over what decisions were made and why, undermining team confidence.
* Higher risks to the project schedule and software quality.

To prevent these risks:

* Ensure all team members understand and follow the simplified change management process.
* Regularly communicate progress on changes and their status during team meetings.

---

### **5. Tailored Processes for Small Teams**

Small projects inherently benefit from agility and close collaboration. By using **scaled-down processes** that retain the essence of formal change management requirements, teams can ensure product quality while working efficiently.

#### **Recommendations for Small Teams:**

* **Prioritize Impactful Processes:** Focus on documenting and evaluating critical changes (e.g., safety, performance, or mission-related changes) while simplifying non-critical updates.
* **Integrate Change Discussions into Daily Workflows:** Use techniques such as stand-ups, team check-ins, or even informal chat tools (e.g., Slack or MS Teams) for routine oversight of change requests.
* **Conduct Lightweight Retrospectives:** Occasionally review closed changes to identify lessons learned and improve your small project’s workflow incrementally.

---

### **Conclusion**

For small projects, a simplified approach to tracking and evaluating changes can maintain efficiency while fulfilling requirements for traceability, accountability, and software quality. By leveraging automated tools, informal evaluation methods, and minimal yet comprehensive record-keeping, small teams can reduce overhead while delivering reliable final products. Despite the reduced formality, maintaining clear documentation and a robust understanding of changes remains essential for project success.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document, EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. See Chapter 13. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-011) Change Request Log Template,  NASA Goddard Space Flight Center, 2015.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-212)

  [IEEE Guide to Software Configuration Management,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=89631&tag=1 "Click to open in new window")

  IEEE Computer Society, IEEE STD 1042-1987, 1987.  This link requires an account on the NASA START (AGCY NTSS) system (https://standards.nasa.gov ). Once logged in, users can access Standards Organizations, IEEE and then search to get to authorized copies of IEEE standards.
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-343)

  [STEP Level 2 Software Configuration Management and Data Management course, SMA-SA-WBT-204, SATERN (need user account to access SATERN courses).](https://saterninfo.nasa.gov/ "Click to open in new window")

  This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-431)

  [SPMN Focus Team Lessons Learned.](http://www.spmn.com/lessons.html "Click to open in new window")

  (2012). Software Program Managers Network (SPMN)  Lessons Learned Reference.
* (SWEREF-520)

  [Problem Reporting and Corrective Action System](https://llis.nasa.gov/lesson/738 "Click to open in new window")

  Public Lessons Learned Entry: 738.
* (SWEREF-576)

  [Software Requirements Management](https://llis.nasa.gov/lesson/3377 "Click to open in new window")

  Public Lessons Learned Entry: 3377.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Tracking and evaluating software changes is a cornerstone of software configuration management, ensuring alignment between software development processes and project goals. Lessons learned from historical programs, as documented in **NASA's Lessons Learned database**, emphasize the critical value of robust change management practices, particularly in improving reliability, managing requirements, and ensuring customer satisfaction. These lessons highlight the importance of proper tools, early problem identification, and effective requirements management in a software project's success.

### **Lessons Learned from the NASA Lessons Learned Database**

#### **1. Problem Reporting and Corrective Action System (PRACAS)**

* **Lesson Number 0738**
  + **Lesson:** "The information provided by the Problem Reporting and Corrective Action System (PRACAS) allows areas in possible need of improvement to be highlighted to engineering for the development of corrective action if deemed necessary. If initiated in the early phases of a program, this system enables the early elimination of the causes of failures, contributing to both **reliability growth** and **customer satisfaction**. Additionally, PRACAS facilitates **data trending**, which can identify areas requiring design or operational changes to prevent recurring issues."
  + **Key Takeaways:**
    - **Early implementation pays off:** Establishing PRACAS in the **early stages** of the project lifecycle allows quick identification and resolution of potential issues, enabling proactive reliability improvements.
    - **Trend analysis for improvement:** Collecting and analyzing historical problem data allows projects to identify patterns, design weaknesses, or operational inefficiencies, providing valuable insight for continuous improvement.
    - **Enhanced reliability and satisfaction:** Proactively resolving issues early reduces the likelihood of late-stage problems, increasing both **system reliability** and **stakeholder confidence.**

#### **2. Software Requirements Management**

* **Lesson Number 3377**
  + **Lesson:** "The ability to manage and trace software requirements is critical to achieving success in any software project. Proper management ensures cost-effective and timely production of software products. However, incomplete, incorrect, or changing software requirements result in **cost and schedule impacts** that grow exponentially the later they are discovered in the software lifecycle. Current technology, processes, and tools offer innovative, automated methods to facilitate effective requirements management."
  + **Key Takeaways:**
    - **Requirements volatility is costly:** Late discovery of issues in software requirements can lead to **expensive rework**, **project delays**, or unexpected failures. Early tracking and evaluation of changes to requirements minimize these risks.
    - **Traceability reduces errors:** By tracking changes to individual requirements and tracing them across design, development, and testing artifacts, teams can ensure alignment between software behavior and stakeholder expectations.
    - **Use automation to your advantage:** Leveraging automated tools for managing requirements (e.g., change tracking systems, requirements management platforms) can streamline processes, reduce human error, and improve compliance with project baselines.

### **Additional Lessons Learned Related to Tracking and Evaluating Software Changes**

#### **3. Importance of Integrated Change Control**

* **Lesson (Derived from Industry Practices and NASA Projects):**
  + Integrated change control ensures that all changes to software products are **evaluated, approved, and documented consistently** across all lifecycle phases. Failure to integrate change control with configuration management can lead to discrepancies between software artifacts (e.g., requirements, design, code, and tests).
  + **Key Takeaways:**
    - Align change control with configuration management processes to ensure the software baseline remains consistent across the project.
    - Avoid "scope creep" by evaluating whether proposed changes align with project goals, mission requirements, and resource constraints.
    - For **safety-critical systems**, verify that all changes undergo rigorous impact analysis, including effects on software safety and system hazards.

#### **4. Early Detection of Problems Saves Time and Cost**

* **Lesson (Derived from Apollo, Space Shuttle, and Mars Pathfinder programs):**
  + Early capture and tracking of defects and issues in the software lifecycle reduces **long-term costs** and prevents ripple effects caused by late changes. Issues that go undetected during early phases will likely propagate through design, implementation, and testing, requiring costly rework in later stages.
  + **Key Takeaways:**
    - Establishing effective problem reporting processes (e.g., PRACAS or similar systems) in early development stages ensures **early risk mitigation**.
    - Baseline software products early (requirements, designs, and test cases) to maintain version control and support early detection of inconsistencies.

#### **5. Role of Comprehensive Impact Analysis**

* **Lesson (Derived from Various NASA Project Reviews):**
  + Change requests must always be evaluated for their **impact on cost, schedule, performance, and safety**, as even small, seemingly benign changes can have far-reaching effects on other software components or the system as a whole.
  + **Key Takeaways:**
    - Always involve appropriate stakeholders (e.g., software assurance, risk managers, domain experts) in the change evaluation process, particularly when working on safety-critical systems.
    - Factor in both the immediate cost of implementing changes and the long-term operational risks or benefits.

### **Summary of Lessons Learned Best Practices:**

1. **Implement Problem Reporting Tools Early:**

   * Systems like PRACAS are essential for tracking and resolving issues effectively. Early deployment enhances system reliability and supports proactive resolution of issues.
2. **Maintain Traceability:**

   * Track changes to software requirements, design, and code throughout the lifecycle. This reduces errors, ensures alignment with project goals, and enables cost-effective updates.
3. **Rigorously Analyze Impact:**

   * Conduct thorough impact analyses for all change requests and involve cross-functional stakeholders to assess risks, costs, and schedule implications.
4. **Leverage Automation:**

   * Use automated tools to streamline problem reporting, trend analysis, and traceability. This reduces manual errors and improves process efficiency while lowering overhead, especially for small or resource-constrained teams.
5. **Monitor Metrics and Trends:**

   * Collect and review metrics about change requests (e.g., number, type, resolution time) and analyze trends to identify recurring issues, inefficiencies, or high-risk areas that require attention.
6. **Address Volatility Early:**

   * Minimize software requirements volatility by making early updates and controlling changes throughout the lifecycle. Late-stage requirement changes are expensive and disruptive.
7. **Ensure Stakeholder Involvement:**

   * Involve all relevant parties—engineering, software assurance, risk management, operations—when evaluating significant changes, especially for safety-critical software systems.

---

### **Conclusion: The Value of Tracking and Evaluation in Software Change Management**

NASA's lessons from past projects emphasize the importance of integrating robust change management practices into software development processes. By leveraging proper tools, maintaining a systematic approach to capturing and evaluating changes, and understanding the costs of volatility or late-stage adjustments, teams can ensure software reliability, reduce risks, and improve customer satisfaction. These lessons highlight the direct relationship between early change tracking and long-term project success, particularly for high-stakes missions where reliability and precision are paramount.

## 6.2 Other Lessons Learned

Additionally, the Software Program Managers Network [431](#_tabs-<p></p>) documents the following relevant lesson as one of its configuration management lessons learned following "visits with many different software-intensive development programs in all three Services. It describes problems uncovered ... on several Department of Defense (DoD) software-intensive programs."

* "The change control board's structure used by software projects is often overly cumbersome. It does not adequately assess, before authorizing a change, the impacts of a proposed change or the risk and cost of making these changes."

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Downstream impacts of decisions made early in the development life cycle](https://software.gsfc.nasa.gov/lesson-details/158/). **Lesson Number 158**: The recommendation states: "Fully evaluate downstream impacts of decisions made early in the development life cycle, particularly on testing."

# 7. Software Assurance

**SWE-080 - Track and Evaluate Changes**

5.1.3 The project manager shall track and evaluate changes to software products.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Analyze proposed software and hardware changes to software products for impacts, particularly safety and security.

2. Confirm the following:  
   a. The project tracks the changes.  
   b. The changes are approved and documented before   
        implementation.  
   c. The implementation of changes is complete.  
   d. The project tests the changes.

3. Confirm software changes follow the software change control process.

## 7.2 Software Assurance Products

Software assurance ensures that changes to software products are tracked, evaluated, and verified in a manner consistent with project objectives while maintaining compliance with agency regulations. The guidance below improves the clarity, structure, and completeness of software assurance practices, emphasizing key responsibilities, lessons learned, and critical considerations.

Software assurance personnel contribute to the overall success of the project by monitoring and verifying the effectiveness of the software change management process. The primary products of software assurance activities related to this requirement include:

#### **Analysis Activities:**

* **Software Design Analysis:**
  + Analyzes the design for potential impacts of approved changes, ensuring the design remains aligned with software requirements and quality standards.
* **Source Code Analysis:**
  + Reviews any modified source code for adherence to coding standards, possible defects, and security vulnerabilities introduced by the change.
* **Verification Activities Analysis:**
  + Assesses the adequacy of the test procedures used to verify the change. Ensures that functional and regression testing plans meet the necessary depth and scope.
* **Impact Analysis of Changes:**
  + Evaluates the change's impact across multiple dimensions, including project risks, safety, reliability, performance, security, interfaces, and traceability.

#### **Review of Supporting Data:**

* **Problem Reporting or Defect Tracking Data:**
  + Monitors defect tracking logs to identify trends, ensure alignment with risk management plans, and validate that issues tied to changes are resolved.
* **Software Configuration Management System Data:**
  + Verifies that configuration items related to changes are properly updated, versioned, and traceable through the change control process.
* **Audit Results of Change Management Processes:**
  + Confirms that audits of the change management processes identify and address discrepancies or areas for improvement.

## 7.3 Metrics

Software assurance should monitor metrics related to software changes, as these provide valuable insights into the health of the project's change management processes and overall software maturity.

#### **Recommended Metrics:**

1. **Change Processing Metrics:**
   * Number of software process non-conformances by life cycle phase over time.
   * Trends of change status over time (e.g., # of changes approved, # in implementation, # in test, # closed).
2. **Testing Metrics:**
   * Number of detailed software requirements tested to date vs. total detailed requirements.
   * Number of tests completed vs. total tests planned.
   * Number of hazards containing software tested vs. total hazards.
   * Number of requirements linked to tests executed vs. total requirements.
3. **Defect Management Metrics:**
   * Number of non-conformances identified during each testing phase (e.g., Open, Closed, Severity breakdown).
   * Number of safety-related non-conformances identified by life cycle phase over time.
   * Number of safety-related requirement issues (Open, Closed) over time.
4. **Progress Metrics:**
   * Number of tests executed vs. number of tests finalized.

#### **See Also:**

* **Topic 8.18 - SA Suggested Metrics**
* **SWE-202 - Software Severity Levels**

## 7.4 Guidance

#### **Impact Analysis:**

Software assurance teams must rigorously **analyze all proposed changes** to ensure they do not adversely affect software safety, reliability, performance, or compliance. This analysis includes:

1. **Safety and Security Analysis:**

   * Evaluate the potential safety and security impacts of the change, specifically:
     + Could the change invoke or exacerbate hazardous conditions?
     + Does the change affect hazard controls, reduce safety margins, or modify safety-critical functionality?
     + Assess whether the software is no longer compliant with security policies or introduces new vulnerabilities.
   * Consider whether hardware changes could indirectly affect software behavior or criticality.
2. **Integration and Maintenance Analysis:**

   * Evaluate whether the change impacts system interfaces, the use of COTS, GOTS, MOTS, or reused software.
   * Assess if the change introduces complexities that will impact future maintenance costs or efforts.
3. **Risk Assessment:**

   * Identify any risks associated with the change and communicate these risks during Configuration Control Board (CCB) discussions.
   * Verify that risks are appropriately tracked in the project or facility risk management system.

#### **Evaluation of Changes:**

Software assurance should validate:

* Whether the request is an error correction or a new requirement.
* Whether the change impacts only the intended area or affects downstream dependencies.
* Whether changes to other areas/systems are minimal or necessary.
* The implementation effort and its associated trade-offs (e.g., cost, time, resources).

### **Approval Tracking and CCB Role:**

* Software assurance personnel must confirm that all submitted changes:
  + Follow an established change control process.
  + Are properly documented, justified, and impact-assessed before implementation.
* **CCB Involvement:**
  + SA personnel are voting members of the CCB (Configuration Control Board) to ensure decisions regarding accepting or rejecting changes consider quality, safety, reliability, and security risks.
  + Ensure that all decisions are formally recorded and aligned with NPR 7150.2 and project risk posture.

#### **Acceptance Criteria:**

For changes:

1. Verify that the resolution (acceptance/rejection) aligns with the Project’s risk tolerance and agency requirements.
2. Ensure that software quality, safety, security, and reliability are not negatively impacted.
3. Confirm that the resolution does not introduce new discrepancies, hazards, or risks.
4. Validate that severity levels of associated software risks are consistently assigned and managed.

#### **Implementation Validation:**

Once a change is approved:

* Verify that the change is implemented as specified in the change request.
* Confirm that all associated documentation (e.g., requirements, design, test procedures) is updated appropriately.
* Ensure that no discrepancies exist between the approved change and the applied implementation.

#### **Testing of Changes:**

* **General Testing:**
  + Confirm that all implemented changes undergo appropriate testing, including regression testing, to ensure no adverse effects on other functionalities.
* **Safety-Critical Software Testing:**
  + Ensure that all safety-critical changes undergo a complete set of regression tests to guarantee no impact on safety-critical software capabilities.
  + Test results must demonstrate adherence to safety requirements and operational compliance.

#### **Control Process Verification:**

* Verify that all changes follow the established **software control process**. This includes:
  + Recording and tracking the status of each change at all stages (e.g., investigation, approval, implementation, testing, and closure).
  + Conducting an audit trail to align changes with NPR 7150.2.

#### **Closure Verification:**

* Confirm that completed changes meet all acceptance criteria (e.g., approval, testing, documentation updates).
* Ensure final decisions are formally communicated to relevant stakeholders and recorded within the system.

### **Lessons Learned for Software Assurance:**

* Early adoption of automated tools like PRACAS improves defect and trend tracking, preventing systemic issues.
* Regular audits of change processes identify process weaknesses early, ensuring consistent adherence to requirements.
* Maintaining traceability from the original change request to final implementation helps reduce rework and debugging time, especially in complex systems.

By maintaining rigorous oversight of changes, software assurance can enhance software quality, maintain mission-critical functionality, and reduce project risks while ensuring compliance with NASA's software engineering requirements.

See also [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

The purpose of objective evidence is to provide tangible proof that the processes and activities associated with tracking and evaluating software changes meet the established requirements. The evidence demonstrates compliance with relevant standards, such as **NPR 7150.2**, and supports reviews, audits, and assessments conducted during the project lifecycle.

Below is the **objective evidence** that software assurance personnel should collect, evaluate, and maintain to prove compliance with the stated requirements for tracking and evaluating software changes.

### **1. Evidence of Impact Analysis**

* **Impact Analysis Reports:**

  + Documentation evaluating the potential effects of proposed changes on:
    - Software requirements, design, code, and documentation.
    - Safety-critical software or hazardous functionalities.
    - Performance, reliability, security, and maintainability.
    - Interfaces, including hardware/software dependencies and external system connections.
  + Include the results of safety analysis, particularly for critical updates involving hardware/software interactions.
* **Risk Assessment Logs:**

  + Records of risks identified during the evaluation of changes.
  + Details on risk categorization (e.g., severity, likelihood) and mitigation strategies.
  + Evidence that these risks were submitted to the project’s risk management system.
* **CCB Meeting Minutes (Impact Assessment):**

  + Meeting minutes from the Configuration Control Board (CCB) reflecting discussions on the risks, impacts, and justification for approving/rejecting changes.
  + Confirmation that software assurance representatives participated in these evaluations.

### **2. Evidence of Change Request Submission and Documentation**

* **Change Control Records:**

  + Change Request (CR) or Problem Report (PR) forms that show:
    - A complete description of the problem or requested modification.
    - Background, rationale, and expected outcomes for the change.
    - Proper prioritization and urgency assignment.
    - Life cycle phase in which the issue or need was detected.
  + Evidence that all submitted changes are tracked in a **centralized change control or problem reporting system** (e.g., PRACAS, JIRA, Bugzilla).
* **Change History Logs:**

  + A detailed record of all submitted change requests, including:
    - Status updates (e.g., under review, approved, rejected, implemented, tested, closed).
    - Associated version numbers of requirement documents, design specifications, or source code.
    - Evidence of traceability (linkage to originating problem reports, requirements, or test results).
* **Configuration Status Accounting Reports:**

  + Provide evidence that the configuration management system captures the current state of all Configuration Items (CIs) impacted by changes.
  + Include a history of changes applied to software baselines, test artifacts, or operational documents.

### **3. Evidence of Change Evaluation and Approval**

* **Change Evaluation Analysis:**

  + Records proving that changes underwent thorough impact analysis, considering:
    - Project impacts (cost, schedule, resources, scope).
    - Technical impacts (functionality, interoperability, systems performance).
    - Alternative solutions, if applicable.
    - Deviations from any expected baseline behavior or standards.
* **CCB Approval Records:**

  + Approval decisions generated by the Configuration Control Board for each change, with:
    - Justifications for approval, deferment, or rejection.
    - A list of attendees (including software assurance personnel).
    - Votes or consensus-based decisions.
  + Include associated software assurance audit checks verifying the adequacy of these decisions.
* **Change Evaluation for Safety-Critical Software:**

  + Records of software assurance safety analyses, including:
    - Identification of any new hazards introduced by the change.
    - Evaluations of hazard controls, mitigations, or updates to safety analysis artifacts.
    - Assessments of the software’s compliance with system-level safety concerns.
  + Evidence of prioritization of safety-related risks where conflicts with other non-safety requirements occurred.

### **4. Evidence of Change Implementation and Testing**

* **Implementation Records:**

  + Evidence that the approved changes were incorporated into the software, including:
    - Code commits or updates linked to the corresponding change request (e.g., version control system logs from Git, SVN, etc.).
    - Updated design documents, requirement specifications, user manuals, test procedures, and related artifacts.
  + Change requests that include details of implementation, such as resource estimates and effort expended.
* **Test Artifacts:**

  + Records showing that changes were tested appropriately, including:
    - Test plans and procedures for functional testing and regression testing.
    - Test logs/results proving that changes worked as intended without introducing side effects.
    - Evidence that safety-critical software underwent full regression testing, focusing on hazard-related functionalities.
  + Defect tracking records tied to changes (if any issues were identified during testing).
  + Updates to test coverage metrics demonstrating the inclusion of new or modified code paths in the testing process.
* **Verification Checkpoints:**

  + Records of software assurance reviews verifying that implemented changes complied with project documentation and intentions.
  + Certification that the changes are complete, correctly linked to the originating change request, and ready for closure.

### **5. Evidence of Traceability and Closure**

* **Traceability Matrix:**

  + A requirements traceability matrix (RTM) showing the linkage between:
    - Change requests, modified requirements, design elements, and code modules.
    - Corresponding test artifacts that validate the change.
  + Evidence of closed-loop confirmation that all aspects affected by the change have been addressed.
* **Change Status and Closure Reports:**

  + Documentation proving that changes progressed through all stages of the process:
    - Submission → Evaluation → Approval → Implementation → Testing → Closure.
  + Include resolution details, such as:
    - "Accepted as is."
    - "Rejected due to..."
    - "Deferred until additional resources are available."
  + Evidence of final confirmations that changes comply with NPR 7150.2 requirements and project objectives.

### **6. Evidence of Process and Compliance Audits**

* **Audit Reports of Change Management:**

  + Audit checklists completed by software assurance teams showing compliance with:
    - The project's change control process.
    - Proper documentation, approvals, and completed actions for all change requests.
  + Records of discrepancies found during audits and their resolutions.
* **Software Configuration Data Audits:**

  + Periodic audits of the software configuration management system (e.g., validation of change history accuracy, correct versioning of baselines).
  + Confirmation that software assurance has reviewed and confirmed the integrity of configuration items after modifications.

### **7. Evidence of Metrics and Trend Analysis**

* **Change Metrics Dashboards:**

  + Reports and visualizations that track:
    - Number and status of changes over time.
    - Trends in unresolved or rejected change requests.
    - Percentage of safety-critical change approvals vs. total changes.
  + Provide trend data to demonstrate continuous improvement of the change management process.
* **Non-Conformance Data:**

  + Records of non-conformance issues related to software changes, including:
    - Rates of detection by life cycle phase.
    - Severity classifications and resolutions.
  + Evidence that non-conformance trends are monitored and inform systems improvement efforts.

### **Conclusion: Comprehensive Objective Evidence**

To demonstrate compliance with this requirement, **objective evidence** must encompass the entire lifecycle of software changes, from initial proposal through approval, implementation, validation, and closure. This includes detailed analysis reports, records of decisions, test artifacts, and audit results. Collecting clear, complete, and traceable evidence ensures confidence in the software assurance process and supports project oversight, certification, and accountability.

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
