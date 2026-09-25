# SWE-075 - Plan Operations Maintenance Retirement

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695456. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement

SWE-075 - Plan Operations, Maintenance, Retirement

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695456)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695456&showCommentArea=true&showComments=true#addcomment)

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

4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-075 History

SWE-075 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.5.2 The project shall plan software operations, maintenance, and retirement activities. |
| Difference between A and B | Added requirement to implement. |
| B | 4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities. |
| Difference between B and C | No change |
| C | 4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities. |
| Difference between C and D | No change |
| D | 4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities. |

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
| * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 2. Rationale

Software operations, maintenance, and retirement activities are planned to provide a written or electronic file on how to operate the software, modify and retest the software and provide information on where to archive the software products, the software development environment, and software test environment products and tools.

Software operations, maintenance, and retirement represent critical stages in the software lifecycle for NASA missions and projects. Planning and implementing activities for these stages ensures that software systems remain functional, reliable, and secure throughout their operational use and are properly retired at the end of their lifecycle. Poor planning in these areas can lead to software failures, mission disruptions, security vulnerabilities, and inefficiencies, which can affect mission success, increase cost, or create risks for future reuse.

---

### **Key Rationale**

#### **1. Ensure Sustained Mission Functionality and Reliability**

* **Why It’s Important:** Software systems must consistently perform their intended functions in the **operations phase** to achieve mission objectives. A lack of proper operational planning can result in unexpected downtimes, loss of capability, or mission compromises.
* **Explanation:**

  + Successful mission execution depends on the availability and performance of the software in its operational environment, including handling off-nominal situations. Planning operations activities ensures that:
    - Operational constraints (e.g., resource usage) are met.
    - Software is monitored for anomalies effectively.
    - Contingency measures are in place to mitigate issues.

---

#### **2. Minimize Downtime with Effective Maintenance**

* **Why It’s Important:** Maintenance activities keep software adaptable to changing conditions, bug fixes, or new mission requirements. Without proper planning for maintenance, a system risks accumulating defects or becoming outdated.
* **Explanation:**

  + Software maintenance involves corrective, adaptive, perfective, and preventive changes. By planning for these activities:
    - Bugs or defects noticed during operations can be corrected before they affect mission objectives.
    - Software can be adapted to account for hardware upgrades, security vulnerabilities, or environmental changes.
    - Preventive and perfective measures keep the software robust and relevant for long-term use, minimizing the risk of introducing new defects or creating operational inefficiencies.

---

#### **3. Address Security and Obsolescence Risks**

* **Why It’s Important:** Software in long-duration missions (or legacy systems still in use) may be exposed to cybersecurity vulnerabilities and increasing obsolescence risks (e.g., hardware dependencies, evolving architectures, and unsupported third-party libraries).
* **Explanation:**

  + Regular software maintenance identifies and mitigates:
    - Security vulnerabilities in code by implementing patches and updates.
    - Compatibility issues resulting from new hardware/software integrations.
    - Aging software dependencies, such as unsupported COTS or OSS components.

---

#### **4. Enable Efficient Transition to Retirement**

* **Why It’s Important:** Software retirement ensures the smooth closure of a project or system, while retaining its artifacts for potential future reuse or reference. Poorly executed retirement can lead to data loss, unused intellectual assets, and wasted resources.
* **Explanation:**

  + Proper planning for retirement ensures that:
    - Critical mission data and software artifacts are preserved and archived in accordance with NASA guidelines (e.g., knowledge capture for reuse).
    - Any remaining risks, such as unprotected data or exposed software systems, are mitigated during retirement.
    - If legacy software is to be discontinued, knowledge transfer ensures continued insights for future projects.

---

#### **5. Compliance with Software Life Cycle Processes**

* **Why It’s Important:** NASA’s software engineering standards (e.g., NPR 7150.2) emphasize the importance of the **full software lifecycle,** requiring equal focus on software development, operations, maintenance, and retirement phases.
* **Explanation:**

  + Planning for all phases of the software lifecycle ensures consistency with NASA’s mission assurance requirements and standards.
  + It provides project stakeholders full transparency regarding how software will be managed after deployment.

---

#### **6. Support Cost and Resource Management**

* **Why It’s Important:** Planning maintenance and retirement activities prevents unexpected costs and resource needs later in the lifecycle.
* **Explanation:**

  + A formalized plan ensures that staffing levels, budget allocations, and maintenance schedules are aligned with the project's operational and post-operational needs.
  + Ad hoc operations or poorly coordinated upgrades can increase costs and lead to service disruptions.

---

#### **7. Support Reuse and Knowledge Capture**

* **Why It’s Important:** Software retirement marks an opportunity to capture and archive essential system knowledge and artifacts for future missions.
* **Explanation:**

  + Retiring software appropriately allows future projects to leverage lessons learned, design patterns, legacy code modules, and documentation.
  + Maintaining and retiring software systematically also ensures traceability, which facilitates efforts for reuse or external reviews.

---

### **Connections to Risk Management**

Failing to plan and implement software operations, maintenance, and retirement can result in significant risks, including:

1. **Operational Impact:**

   * Risk of mission downtime or data loss due to unaddressed faults or insufficient operational procedures.
2. **Security Threats:**

   * Legacy software may become vulnerable to exploits if there is no plan for regular updates or eventual retirement.
3. **Cost Overruns:**

   * Correcting operational inefficiencies, legacy dependencies, or retiring software systems without proper planning often requires additional unplanned resources and budget reallocations.
4. **Knowledge Gaps:**

   * Failure to document or preserve software details during retirement can result in the loss of valuable intellectual property for NASA, impairing future missions.

---

### **Keys to Effective Compliance**

1. **Operations Planning:**

   * Define clearly how software will operate in its intended environment (e.g., ground systems, flight systems).
   * Set up monitoring processes, error reporting mechanisms, and operational constraints.
2. **Maintenance Planning:**

   * Establish robust processes for handling software updates, patches, and bug fixes.
   * Create plans for software upgrades, especially for external libraries or third-party components used (COTS/OSS).
   * Ensure processes for integration testing after maintenance activities are included.
3. **Retirement Planning:**

   * Specify procedures for archiving intellectual property, artifacts, and mission data.
   * Define steps to decommission software safely, addressing residual security risks.
   * Plan for extracting lessons learned and passing knowledge to new projects.

---

### **Conclusion**

Requirement 4.6.2 is critical to enabling the reliable, long-term operation of NASA’s software systems while ensuring projects plan resources, address risks, and capture knowledge during both active use and retirement. By planning for software operations, maintenance, and retirement, NASA projects ensure mission continuity, efficient lifecycle processes, and the preservation of valuable software and knowledge assets for future efforts.

# 3. Guidance

This improved guidance aims for clarity, conciseness, and practicality while emphasizing the importance of thorough planning across operations, maintenance, and retirement. It provides actionable content to ensure software remains functional, maintainable, and secure during mission use and is retired effectively. The updated structure follows a lifecycle approach and highlights key considerations for NASA’s software engineering processes.

---

### **Guidance Overview**

Operations, maintenance, and retirement activities form the final stages of the software lifecycle, where the delivered product transitions into usage, long-term support, and eventual decommissioning. Proper planning ensures that software continues to meet mission requirements while addressing risks, resource constraints, and evolving stakeholder needs throughout its lifecycle.

Planning for operations, maintenance, and retirement is **not static** and should mature as the project progresses. Early drafts should set initial expectations, while subsequent revisions refine the plan to account for operational realities, mission feedback, and emerging risks. These plans serve as the foundation for transitioning the software between lifecycle stages.

---

### **1. Lifecycle Approach and Integration**

* Operations, maintenance, and retirement are **interconnected phases** that benefit from concurrent planning and integration into broader project documentation (e.g., **Software Management Plan (SMP)** or **Software Maintenance Plan**).
* The **Software Maintenance Plan** (see **Topic 5.04**) can consolidate processes for:

  + Development, testing, and configuration management during maintenance and operations.
  + Software decommissioning steps for retirement.
* If processes for these activities are already described in another project document, it is acceptable to **reference rather than duplicate** them.

**Software Development Process Description Document**

"The Software Operation phase spans the time from execution of the software product in the target environment to software retirement. The Software Maintenance phase of the software life cycle begins after the successful completion of the formal test and delivery of the software product to the customer. This Software Maintenance phase overlaps the Software Operation phase and continues until software retirement or discontinuation of software support."[001](#_tabs-<p></p>)

---

### **2. Operations Activities**

**Key Considerations During Operations:**

* **Documentation Support:**

  + Provide user manuals (e.g., **Software User’s Manual**) and "as-built" documentation that guide operators.
  + Maintain availability of configuration and issue resolution logs for operational debugging.
* **Mission and Operational Support:**

  + Establish procedures for software team support, such as help desk activities for operators or mission teams.
  + Define troubleshooting and contingency procedures for resolving software problems.
  + Ensure tools (e.g., issue tracking systems, operational servers, etc.) are available to support operations.
* **Monitoring and Performance Validation:**

  + Plan for **test sequences** during mission simulations or end-to-end mission rehearsals.
  + Develop processes for capturing, analyzing, and addressing performance metrics during operations.
  + Include procedures for backups (e.g., hot backups) to minimize downtime for mission-critical software.
* **Problem Reporting and Lessons Learned:**

  + Plan for PRACA (Problem Reporting and Corrective Action) systems to track issues during operations.
  + Capture and document lessons learned to improve subsequent activities or future software applications.
* **Stakeholder Awareness:**

  + Define operator and maintainer roles clearly, ensuring personnel receive adequate training on updated tools, procedures, and operations workflows.

---

### **3. Maintenance Activities**

**Key Maintenance Considerations:**

* **Start Planning Early:**

  + Maintenance planning should begin as early as the software design phase to ensure software is developed with maintainability in mind.
  + Include **specific design features** that facilitate easier maintenance, such as modular architectures or clear documentation trails.
* **Updating Delivered Software:**

  + Plan for corrective maintenance (bug fixes), adaptive maintenance (updating software for changing hardware or environments), and perfective maintenance (enhancing functionality).
  + Ensure availability of the development, testing, and configuration resources to support maintenance.
* **Modifications and Transition:**

  + Define processes for implementing software modifications after formal delivery, including:
    - Baseline management using configuration control tools.
    - Updates to system documentation (e.g., aligning user manuals, operations notes, etc., with new releases).
* **Testing and Re-Verification:**

  + Plan for rigorous revalidation:
    - Conduct pre- and post-delivery tests to verify that changes address existing requirements while ensuring no unintended consequences.
  + Use regression testing to ensure software modifications maintain compliance with previous system behaviors.
* **Metrics, Analysis, and Reporting:**

  + Include measurement systems to track maintenance performance, such as:
    - # of modifications delivered per release.
    - Resolution times for reported issues.
  + Use these metrics to evaluate and improve maintenance processes over time.
* **Stakeholder Communication:**

  + Notify users of software updates, patches, and their implications (e.g., release notes or **Version Description Documents (VDDs)**).

---

### **4. Retirement Planning and Execution**

**Key Goals for Retirement:**

* **Archival for Future Use or Reference:**

  + Develop processes for storing software artifacts, source code, and project data in the **Configuration Management (CM) System**, ensuring retrievability for future projects or reviews.
  + Archive **project metrics, test results, and change histories**.
* **Transition Planning:**

  + If replacing the retired software, create a transition plan to migrate functionality and data to the new system.
  + Coordinate with stakeholders to ensure minimal disturbance to operations during this transition.
* **Decommissioning and Security:**

  + Outline procedures for system shutdown, including the secure disposal of leftover artifacts, data, or resources.
  + Ensure retired software products are stored or disposed of in a way that prevents unauthorized access or use.
* **Lessons Learned:**

  + Document lessons learned during software retirement and archival to inform future plans, improve lifecycle management, and capture the software's contribution to mission objectives.

---

### **5. Planning for Contingencies and Updates**

While operations, maintenance, and retirement plans may be more stable than those for earlier lifecycle phases, certain events may require updates to these plans:

* Changes in:
  + Resource availability (tools, personnel, budget, etc.).
  + Stakeholder needs or expectations.
  + Processes used for operations, maintenance, and retirement, such as reporting workflows or risk management strategies.
* The emergence of new risks.

**Process for Updates:**

* Any updates to operations, maintenance, or retirement plans should be reviewed, formally approved, and baselined to ensure alignment with system and mission requirements.

---

### **6. Specialized Considerations**

* **COTS, OSS, and Third-Party Software:**

  + Plan for license renewals, updates, and obsolescence management.
  + Ensure compliance with licensing terms during retirement (e.g., appropriate archiving or decommissioning).
* **Support Roles and Tools:**

  + Clearly allocate responsibilities across the project manager, software team, software assurance personnel, and configuration management personnel.
* **Software Assurance:**

  + Software assurance ensures the approved plans for operations, maintenance, and retirement are implemented correctly and that updates/changes align with project requirements.

---

### **Recommended Practices**

1. **Maturity Planning (See Topic 7.08):**

   * Align all lifecycle plans with the project's milestone reviews, gradually increasing their maturity as the project evolves.
2. **Resource Scalability:**

   * Address tool and personnel shortages that may occur over the software’s operational lifespan (e.g., retiring staff, outdated issue trackers).
3. **Center-Specific Guidance:**

   * Consult Center Process Asset Libraries (PALs) for guidance relevant to operations, maintenance, and retirement planning.
4. **Designing for Maintainability:**

   * Account for extensibility, modularity, and clear documentation early in the software development process. These reduce costs and risks for long-term maintenance.

---

### **References to Related Requirements and Topics**

* **SWE-077:** Delivering software products with appropriate lifecycle documentation.
* **SWE-194:** Verifying delivered software products meet mission objectives.
* **SWE-195:** Addressing key elements of the maintenance phase.
* **SWE-196:** Archival and retirement requirements for software products.
* **5.04:** Maintenance plan guidance.
* **5.16:** Description of the Version Description Document (VDD).
* **7.08:** Maturity of lifecycle plans at milestones.

---

### **Conclusion**

By proactively planning and implementing operations, maintenance, and retirement activities, NASA ensures software reliability, maintainability, and proper closure at the end of the lifecycle. These activities reduce risks, mitigate costs, and preserve critical artifacts, ensuring successful mission execution and supporting future endeavors.

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

Additionally, guidance related to operations, maintenance, and retirement planning may be found in [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)  in this Handbook. 

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase) * [SWE-196 - Software Retirement Archival](/spaces/SWEHBVD/pages/102695531/SWE-196+-+Software+Retirement+Archival)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

For small projects with limited staff, budgets, or resources, adapting practices to balance thoroughness with efficiency is critical to ensuring compliance without unnecessary overhead. The guidance below provides streamlined recommendations to help small projects effectively plan and execute operations, maintenance, and retirement activities in a practical, sustainable, and resource-friendly manner.

---

### **1. Leveraging Existing Plans (Reuse to Save Effort)**

* **Adapting From Similar Projects:**

  + Identify and reuse maintenance plans or templates from similar projects (e.g., those with comparable size, complexity, or mission objectives).
  + Ensure the plan is **tailored to the specific needs of the current project**, including differences in operational use, resource availability, or software requirements.
  + Example: Use an archived **Software Maintenance Plan** from a past project as a starting point and update sections such as testing procedures, support team availability, and specific tools to align with the current project's circumstances.
* **Streamlining Documentation:**

  + Instead of creating a standalone **Software Maintenance Plan**, integrate the required content into other existing project documents, such as the:
    - **Software Management Plan (SMP)** — Include sections for operations, maintenance, and retirement activities.
    - **Configuration Management Plan (if available).**
    - **Software User’s Manual** — Provide operational instructions and details for users and maintainers.
* **Use VDDs for Updates in Place of Full Plans:**

  + Small projects can capture updates and modifications as part of the **Version Description Document (VDD)** for each new software release. This simplifies documentation while keeping track of key changes.

---

### **2. Keep the Plans Lightweight**

Small project teams should focus on **providing “just enough” detail** to ensure that operational and maintenance tasks are understood, actionable, and achievable without creating excess documentation.

* **Minimum Contents of an Operations and Maintenance Plan:** Include core topics like:
  + **Support Responsibilities:** Identify who will handle operations and maintenance, and their specific roles (e.g., troubleshooting lead, testing lead, or general software support roles).
  + **Tools and Resources:** List the tools required (e.g., issue trackers, test environments) and ensure their availability.
  + **Update and Issue Resolution Process:** Define how defects or updates will be logged, tracked, and addressed during operations.
  + **Transition Planning:** If maintenance involves handing off software to another team or organization, describe how and when the handover will occur.
  + **Retirement Planning Basics:** Outline simple steps for retiring the software, such as archiving source code or informing users of its decommission.

---

### **3. Use a Simplified Template for Planning**

Small projects can reduce complexity by using a **short, simplified format for their operations, maintenance, and retirement plans**, structured around the following questions:

* **Operations Phase:**

  + Who will oversee operational support?
  + How will issues or bugs during operations be reported and resolved?
  + What tools or logs will operators use?
  + Are any backups required for critical data or functionality?
* **Maintenance Phase:**

  + How will updates and patches be handled?
  + What are the minimum testing requirements for modifications?
  + What is the process for notifying stakeholders of updates or significant changes?
  + What metrics will be tracked to evaluate maintenance efforts?
* **Retirement Phase:**

  + What steps must be taken to safely archive software artifacts, source code, documentation, and data?
  + Are there any replacement systems planned, and how will data or functionality transition to the replacements?
  + How long will retired software products be retained for future reference?
  + What steps are needed to safely dispose of sensitive data or proprietary code?

---

### **4. Assign Clear Responsibilities**

In small projects, limited staffing makes role clarity even more important. To ensure smooth workflows during operations, maintenance, and retirement:

* Assign **team members dual roles** to simplify communication. For example:
  + A developer might also function as the maintenance lead.
  + A configuration manager may also track archival needs during retirement.
* Define ownership of key tasks, even if the same individual covers multiple areas. Example:
  + "Operations errors are reported via the issue tracker. Developer A will monitor and track issues weekly."

---

### **5. Focus on Automation Where Possible**

Small teams should leverage tools and automation to minimize manual effort during the operations, maintenance, and retirement phases:

* **Operations Support Tools:** Use ticketing systems (e.g., Jira, GitHub Issues) to track and resolve problems efficiently.
* **Maintenance Environment:** Automate testing (e.g., regression test suites) and delivery processes to reduce manual errors.
* **Retirement Archival:** Use a CM system or repository (e.g., Git, Bitbucket) for automated version control during the software retirement process.

---

### **6. Budget-Conscious Strategies**

For projects with restricted budgets:

* **Share Tools Across Teams or Projects:** Use shared environments or tools licensed at the Center level (e.g., testing or tracking software maintained by the NASA Center’s IT department).
* **Outsource Maintenance and Retirement Tasks Where Feasible:** Particularly for open-source or COTS-heavy solutions, consult or engage with the software vendor or community for long-term maintenance and archival needs.

---

### **7. Retirement Can Be Streamlined**

Small projects may simplify retirement planning using the following approaches:

* **Focus on Archival:** Prioritize proper archival of key artifacts (e.g., source code, final operational documentation, test reports), ensuring the software can be referenced or reused by future projects.
* **Simplify Handover:** If retiring software will be replaced, ensure only critical operational data and functionality are handed off to successor systems.
* **Minimize Documentation for Non-Essential Code:** If specific tools, modules, or features are unlikely to be used again, avoid over-documenting and focus solely on decommissioning processes.
* **Use Tools Already in Place:** Leverage existing CM systems to meet data retention/security needs for retired software.

---

### **Examples of How Small Projects Can Adapt**

Consider the following scenarios for small projects to streamline activities:

* **Example 1: Extending a Small Payload Controller Software Project**

  + Reuse architectural and maintenance plan elements from a similar payload software system.
  + Integrate minimal retirement steps into a major release's deployment plan (e.g., "Archive all documentation and metrics in Git repository").
* **Example 2: Small Ground Support Software with Limited Team**

  + Include maintenance and operational steps in an appendix of the **Software Management Plan** (e.g., detailing how issue tracking, patching, and operator training will be handled).
  + Plan the retirement process as a single task to archive code, documents, and metrics after the mission concludes.

---

### **8. Key Benefits of This Approach**

* **Efficiency:** Leveraging existing plans and tools reduces effort and documentation costs.
* **Flexibility:** Combining the plans into other documents allows small projects to reduce administrative overhead.
* **Maintainability:** Designing lightweight plans ensures that critical tasks are documented without unnecessary complexity.

---

### **Conclusion**

Small projects can ensure compliance with requirement 4.6.2 by focusing on adapting existing resources, consolidating plans, simplifying documentation, and leveraging automation. By tailoring activities to available resources, small teams can achieve success in operations, maintenance, and retirement while adhering to NASA's required rigor and standards. This approach retains efficiency without sacrificing quality or mission alignment.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-037)

  [NASA Records Management Program Requirements (Updated w/Change 3),](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1441&s=1E "Click to open in new window")

  NPR 1441.1E, NASA Office of the Chief Information Officer, Effective Date: January 29, 2015, Expiration Date: January 29, 2024
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-209)

  [IEEE Standard for System, Software, and Hardware Verification, and Validation](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8055462 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1012-2016 (Revision of IEEE Std 1012-2012), Published September 29, 2017,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards. Non-NASA users may purchase the document from: http://standards.ieee.org/findstds/standard/1012-2012.html
* (SWEREF-215)

  [IEEE Standard for Software and System Test Documentation,](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4578271 "Click to open in new window")

  IEEE Computer Society, IEEE Std 829-2008, 2008.  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-228)

  [International Standards Organization (ISO), "Software Engineering - Software Life Cycle Processes - Maintenance,"](http://www.iso.org/iso/cataloguedetail.htm?csnumber=39064 "Click to open in new window")

  ISO/IEC 14764:2006, 2006. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-525)

  [Benefits of Implementing Maintainability on NASA Programs](https://llis.nasa.gov/lesson/835 "Click to open in new window")

  Public Lessons Learned Entry: 835.
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-540)

  [Computer Hardware-Software/Software Development Tools/Maintenance](https://llis.nasa.gov/lesson/1128 "Click to open in new window")

  Public Lessons Learned Entry: 1128.
* (SWEREF-543)

  [International Space Station (ISS) Program/Computer Hardware-Software/International Partner Source Code](https://llis.nasa.gov/lesson/1153 "Click to open in new window")

  Public Lessons Learned Entry: 1153.
* (SWEREF-550)

  [ADEOS-II NASA Ground Network (NGN) Development and Early Operations -- Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned](https://llis.nasa.gov/lesson/1346 "Click to open in new window")

  Public Lessons Learned Entry: 1346.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains valuable insights and historical learnings related to maintenance planning and implementation. These lessons emphasize the importance of early planning, maintainability considerations during design, and proactive measures to mitigate risks and challenges during operations, maintenance, and retirement. Below are the original lessons from NASA's database, improved and supplemented with additional context and actionable takeaways for software engineering projects.

---

### **1. Benefits of Implementing Maintainability on NASA Programs**

**Lesson Number: 0835**

* **Impact of Non-Practice:**  
  "Maintainability requirements for programs that require ground and/or in-space maintenance and anomaly resolution must be established early in the program to be cost-effective. Lack of management support to properly fund maintainability activities upfront can result in increased program risk. Including maintainability in the design process will greatly reduce operational problems associated with system maintenance, improve system availability, and reduce program costs."
* **Key Takeaways:**

  + Design for maintainability is not optional; failing to include maintainability during the design phase results in higher corrective costs and increased risks later in the lifecycle, particularly for long-term missions.
  + Maintainability reduces system downtime, improves reliability, and optimizes resource use during operations and maintenance.
  + Ground operations and anomaly resolution systems designed with ease of maintenance in mind can save time and effort during troubleshooting, ensuring mission continuity.
* **Recommendations for Future Projects:**

  + Engage stakeholders early to define maintainability requirements.
  + Allocate funding and resources for maintainability efforts as part of the initial project budget.
  + Incorporate maintainability metrics into design and testing reviews.

---

### **2. Software Design for Maintainability**

**Lesson Number: 0838**

* **Impact of Non-Practice:**  
  "Due to the increasing size and complexity of software products, software maintenance tasks have become more challenging. Software maintenance should not be treated as an afterthought in design. The software should be designed such that maintainers can enhance or update products without requiring extensive rewrites of code."
* **Key Takeaways:**

  + Software modularity, clear documentation, and code organization enable efficient and effective maintenance.
  + Designs that rely on tightly coupled systems increase the technical debt and complexity of future maintenance efforts.
  + Proper software engineering practices during development (e.g., modular design, adherence to coding standards) can reduce maintenance overhead.
* **Recommendations for Future Projects:**

  + Emphasize coding standards and modular development to create self-contained modules that are easier to modify or replace.
  + Conduct maintainability reviews during major milestones to detect and address potential challenges.
  + Ensure maintainers are involved in the design process to provide feedback on future usability and maintainability needs.

---

### **3. COTS Software Development Tools/Maintenance**

**Lesson Number: 1128**

* **Finding:**  
  “No program-wide plan existed for maintaining Commercial Off-the-Shelf (COTS) software development tools. A programmatic action was assigned to define usage requirements for COTS/modified off-the-shelf software, including their associated development tools. These guidelines highlighted the importance of developing selection and maintenance criteria for long-term COTS product sustainability.”
* **Key Takeaways:**

  + COTS tools require early and proactive planning for their use, management, and eventual replacement.
  + Many COTS or Modified Off-The-Shelf (MOTS) tools may have limited vendor support or become obsolete over time.
* **Recommendations for Future Projects:**

  + Develop a maintenance plan specifically for third-party tools, including alternative solutions in case of obsolescence or failure.
  + Include vendor/product longevity analyses in COTS selection criteria.
  + Budget for periodic re-evaluation of COTS tools and ensure maintenance contracts extend through critical phases of the mission.

---

### **4. ISS Program: Maintenance Agreements for International Partner Software**

**Lesson Number: 1153**

* **Recommendation:**  
  “Solidify long-term source code maintenance and incident investigation agreements for all software developed by International Partners, and develop contingency plans for all operations that cannot be adequately placed under NASA's control.”
* **Key Takeaways:**

  + Strong partnership agreements are critical for software maintenance, particularly when third-party or international organizations develop portions of a system.
  + Contingency plans are essential for operations and maintenance activities outside of NASA’s direct control.
  + Source code access or maintenance agreements must be formalized early to reduce risks tied to dependency on external teams.
* **Recommendations for Future Projects:**

  + Ensure maintenance agreements with partners are formalized before entering the operations phase.
  + Include source code storage agreements to mitigate risks resulting from personnel, organizational, or geopolitical changes.
  + Outline clear communication and collaboration protocols for maintenance and incident resolution.

---

### **5. ADEOS-II NASA Ground Network (NGN): Maintenance Tools and Planning**

**Lesson Number: 1346**

* **Lesson Learned No. 3:**  
  “Lessons learned during the SAFS/CSAFS [Standard Autonomous File Server and Central Standards Autonomous File Server] system development include the following:

  + Perform on-site installations when possible to capture real-world constraints.
  + Secure support/maintenance contracts for both hardware and software through development, deployment, and the initial year of operation.
  + Use visual representations of system interactions for better understanding during troubleshooting.
  + Collect end-user feedback during the operational phase.
  + Maintain prototype systems after deployment.
  + Prioritize COTS products capable of internal logging.”
* **Key Takeaways:**

  + Early feedback from operators and a clear representation of system interactions are critical for identifying issues during operations.
  + Strong support contracts (covering both hardware and software) reduce maintenance risks during early operational phases and system hand-off.
  + Select tools that achieve operational objectives with features (e.g., logging) that support troubleshooting and maintenance.
* **Recommendations for Future Projects:**

  + Design simple visualization tools for system dependencies and workflows (e.g., flowcharts, block diagrams).
  + Secure maintenance contracts as part of project planning and ensure coverage for the critical early phases of operation.
  + Use end-user feedback for iterative improvements in both documentation and software updates.

---

### **6. Additional Lessons Learned (Proposed from NASA Practices):**

**a. Early Maintenance and Retirement Planning Minimizes Risks**

* Planning for software maintenance and retirement during the development phase reduces transition risks, lifecycle costs, and obsolescence issues.
* Establishing defined retirement triggers ensures software is not left unsupported beyond its effective operational life.

**b. Include Data Integrity as a Maintenance and Retirement Goal**

* Lessons from past projects highlight the risks of failing to archive operational data or project metrics correctly during decommissioning. These data issues often result in missed opportunities for knowledge retention, impact analysis, or system reuse.

**c. Coordination is Key When Multiple Teams are Involved**

* Distributed development or multi-party contributions (e.g., international partners or contractors) require simple, well-structured maintenance plans to prevent hand-off issues or unaddressed maintenance tasks.

---

### **7. Conclusion**

The NASA Lessons Learned database highlights the critical role of early planning, stakeholder alignment, maintainable software design, proactive COTS management, and strong maintenance agreements in reducing risks and lifecycle costs. Taking these lessons into account enables projects to improve system continuity, ensure cost-effectiveness, and guarantee the long-term success of NASA missions.

## 6.2 Other Lessons Learned

### 6.2.1 Operations

* Ensure Ops procedures (production, test, launch/recovery, and mission) fully incorporate and/or reference applicable Ops Notes. Reinforce the use of written Op Procedures for work performed on vehicles in all operations.
* Establish minimum testbed configuration (required hardware in the loop) to support time-critical testing during missions and require appropriate control board approval for any deviations. The existence of hardware in the lab allowed critical issues to be identified during the OFT mission.
* Operation is a critical element of multi-level redundancy.

### 6.2.2 Software Engineering

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Dedicate more hours to FSSE preparation for post-commissioning](https://software.gsfc.nasa.gov/lesson-details/79/). **Lesson Number 79**: The recommendation states: "Dedicate more hours to FSSE preparation for post-commissioning, particularly in the preparation of the Lab as long-term asset for the mission."
* [Projects should work with the Space Network (SN)](https://software.gsfc.nasa.gov/lesson-details/83/). **Lesson Number 83**: The recommendation states: "Projects should work with the Space Network (SN) to understand and consider the mission's (and other SN customer's) operational constraints."
* [Staffing plan takes into account continuing support for activities that occur after software is delivered](https://software.gsfc.nasa.gov/lesson-details/90/). **Lesson Number 90**: The recommendation states: "Develop a staffing plan that takes into account continuing support for activities that occur after software is delivered."
* [Bring on a Mission Director 2 years before launch](https://software.gsfc.nasa.gov/lesson-details/93/). **Lesson Number 93**: The recommendation states: "Bringing on a Mission Director 2 years before launch would smooth out the transition process."
* [Operational database needs to reflect operational definitions and approach](https://software.gsfc.nasa.gov/lesson-details/101/). **Lesson Number 101**: The recommendation states: "Scrub the operational database and revise to reflect operational definitions and approach (for example, the operational definitions for R/Y/G limits)."
* [Integrate FSSE engineers into the Flight team](https://software.gsfc.nasa.gov/lesson-details/106/). **Lesson Number 106**: The recommendation states: "It is beneficial to integrate Flight Software Sustaining Engineering (FSSE) engineers into the Flight team."
* [Develop a long term plan for labs](https://software.gsfc.nasa.gov/lesson-details/120/). **Lesson Number 120**: The recommendation states: "Develop a long term plan for labs that covers inventory and maintenance."
* [The FSW Lab setup should meet the needs/requirements across the Project and FSW Lifecycle](https://software.gsfc.nasa.gov/lesson-details/237/). **Lesson Number 237**: The recommendation states: "The FSW lab is a project resource used across the FSW lifecycle including initial development/testing, later FDC and system testing, and finally FSSE usage during operations post launch. Initial development/testing might only need communications between the FSW and a simulator.  Later development/testing might need to configure simulator telemetry via a command from ground system or even dynamically model simulator telemetry points.  All lifecycle development/testing/diagnostics may need additional information from FSW or simulator to diagnose and troubleshoot problems. While the future can never be predicted and no lab components can be ""perfect"" given all potential development, testing, and diagnostic cases, the lab items should be setup considering current, future, and potentially future needs and requirements.  Where appropriate, lab items should be designed for possible updates in the future (i.e. settable telemetry point to model operational telemetry point)."
* [Consider PROM based boot loaders to support updates to non-volatile memory](https://software.gsfc.nasa.gov/lesson-details/238/). **Lesson Number 238**: The recommendation states: "There is and always has been the possibility of corrupting a non-volatile FSW image (error in FSW, error in load, error in command, error in command sequence, adversarial actions, etc.).  In addition, EEPROMs have a data retention issue which would corrupt the FSW image. Given enough time EEPROMs can lose their charge. This is normally not a concern except in harsh environments like space.   Also, board designs can allow EEPROM corruption during power down sequences (some board designs protect against this). Ideally there would be a way to reload a non-volatile image via a method that cannot be corrupted, such as a PROM based boot loader (PROM is a fused chip and not subject to accidental/intentional modification, radiation upset, data retention, or any other modification)."

# 7. Software Assurance

**SWE-075 - Plan Operations, Maintenance, Retirement**

4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess the maintenance, operations, and retirement plans for completeness of the required software engineering and software assurance activities.

2. Confirm that the project implements software operations, software maintenance, and software retirement plans.

## 7.2 Software Assurance Products

This updated guidance improves clarity, structure, and actionable details for software assurance (SA) activities and responsibilities related to operations, maintenance, and retirement phases. It emphasizes SA’s role in ensuring plans, processes, and outputs meet quality, safety, and reliability standards while supporting mission objectives.

**1. Software Assurance Plan Assessment:**

* Evaluate the project’s Software Assurance Plan to confirm that it adequately addresses SA processes for the operations, maintenance, and retirement phases.
* Verify that the Software Assurance Plan includes mechanisms for audits, metrics collection, risk identification, and tracking during operations, maintenance, and retirement.

**2. Software Engineering Plans Assessment:**

* Assess engineering deliverables (e.g., Software Management Plan, Software Maintenance Plan, Configuration Management Plan, Software Test Plan) to ensure alignment with SA goals.
* Verify that engineering plans for maintenance, operations, and retirement account for software quality, safety, defect handling, and secure archival procedures.

**3. Software Assurance Assessment of Maintenance, Operations, and Retirement Plans:**

* Review the completeness and reasonableness of the plans with respect to the lifecycle requirements, available resources, and mission constraints.
* Identify and address any gaps, inadequacies, or risks in the plans that could impact software reliability, safety, or operational readiness.

**4. Audit Results for Maintenance, Operations, and Retirement Processes:**

* Conduct periodic audits during operations and maintenance to ensure compliance with approved plans and procedures.
* For retirement processes, ensure that archival, system closure, and decommissioning efforts adhere to pre-established plans.
* Document audit findings, communicate non-conformances, and ensure corrective actions are implemented.

---

## 7.3 Metrics

Software assurance metrics provide insights into the effectiveness of operations, maintenance, and retirement activities by tracking non-conformances, process deviations, and product quality. Key metrics include:

**Recommended Metrics (See Topic 8.18 - SA Suggested Metrics):**

1. **Non-Conformances Identified by Lifecycle Phase Over Time:**

   * Track the number of issues identified during operations, maintenance, and retirement.
   * Use trend analysis to detect recurring patterns or systemic weaknesses in these phases.
2. **Non-Conformances Identified in Plans and Processes:**

   * Assess operational, maintenance, and retirement-related plans (e.g., SMP, SDP, CM Plan, SA Plan, Safety Plan).
   * Measure the number of deviations between activities performed and planned processes.
3. **Defect Metrics:**

   * Record reported software defects during operations and unexpected disruptions caused by faulty updates during maintenance.
   * For retirement, track issues related to incomplete transitions or the archival of project artifacts.
4. **Process Conformance Metrics:**

   * Measure adherence to documented procedures for software testing, user manual updates, archival, and license transfers during all phases.

---

## 7.4 Guidance

#### **Software Assurance Responsibilities Across the Lifecycle Phases**

**1. Operations Phase:**

* **Assess Operational Documentation:**

  + Confirm completeness and accuracy of the **Software User Manual** and **Procedures Documentation.**
  + Verify inclusion of safety-critical commands, limitations, error messages, and corrective actions.
  + Ensure operational instructions are consistent with system testing outcomes.
* **Support Operational Testing and Workaround Updates:**

  + Evaluate updates to operational manuals based on defects detected during live operations.
  + Verify the inclusion of workarounds for unaddressed issues, especially those related to safety-critical software.
* **Monitor Operator Adherence to Processes:**

  + Conduct process audits during operations to ensure operators follow documented procedures.
  + Focus on adherence to safety-related instructions and verify corrective actions for anomalies are implemented effectively.
* **Safety and Reliability Monitoring:**

  + Track safety, reliability, and performance metrics during operations to evaluate system behavior in real-world conditions.
  + Ensure contingency measures for mission-critical operations are clearly documented and functional.

---

**2. Maintenance Phase:**

* **Assess Maintenance Plans:**

  + Verify that the Software Maintenance Plan adequately addresses processes for defect resolution, adaptive modifications, testing, validation, and stakeholder notification.
  + Confirm that the plan aligns with maintainability goals and budget/resource constraints.
* **Review Configuration Management Practices:**

  + Validate the availability and configuration of systems for tracking, applying, and documenting defect fixes.
  + Ensure version control systems prevent overwritten or improperly integrated updates.
* **Evaluate Testing of Software Modifications:**

  + Confirm that defect fixes and modifications are rigorously tested beforehand using regression testing to prevent disruptions to normal operations.
  + Assess testing procedures for updates to ensure high reliability of newly integrated versions.
* **Ensure Compliance with Documentation Updates:**

  + Verify that system and user documentation is updated for all maintenance actions, including defect fixes, adaptive changes, and new releases.
* **Monitor Process Implementation:**

  + Conduct periodic audits to confirm maintenance activities follow the Software Maintenance Plan.
  + Ensure a robust process exists for stakeholder communication regarding updates, new defect reporting, or unexpected changes.

---

**3. Retirement Phase:**

* **Confirm Adherence to Retirement Plans:**
  + Software assurance personnel should verify that all retirement activities are executed as documented.
  + Ensure data archival, copyright/license handling, and secure disposal of system artifacts adhere to NASA standards.

**Specific Focus Areas:**

1. **Archival Activities:**

   * Confirm that software artifacts, documentation, operational logs, and data are securely archived in configuration management systems or specified repositories for future use.
   * Assess the security and integrity of archived software, ensuring protection against unauthorized access or unintended degradation.
2. **Decommissioning Equipment:**

   * Verify that furniture and equipment are properly transferred or disposed of, and that sensitive project information is securely removed from all devices before excessing.
3. **License Transfers:**

   * Ensure commercial software licenses are properly transferred to successor teams, renewed, or canceled to prevent legal or financial issues.
4. **Lessons Learned:**

   * Collaborate with project teams to document lessons learned during the operations, maintenance, and retirement phases, focusing on challenges and successes related to SA activities.
   * Make SA-specific lessons learned available to NASA’s database for reuse in future projects.
5. **Contract Review and Closure:**

   * Confirm that project-specific contracts are finalized and closed by coordinating with contracting officers to prevent lingering obligations or risks.

---

### **Improved Operational Documentation Recommendations**

Software assurance should perform the following for operational documentation:

1. Ensure detailed safety-related information is included in user manuals, operational procedures, and other relevant artifacts.
2. Verify that all error messages, their meaning, and required corrective actions are clearly explained and consistent with system design.
3. Evaluate the incorporation of defect-related workarounds in updated user manuals to ensure safe and reliable system operation.

---

### **Additional Recommendations for SA Processes**

**A. Proactive Risk Assessment:**

* Regularly assess risks specific to the operations, maintenance, and retirement plans, including resource shortages, stakeholder conflicts, or system obsolescence.

**B. Collaborative Stakeholder Engagement:**

* Work alongside operations, maintenance, and retirement teams to bridge gaps between SA expectations and operational realities.

**C. Automated Compliance Checks:**

* Utilize automated SA tools to verify adherence to testing, defect tracking, and auditing requirements during maintenance and operations.

---

### **Conclusion**

By implementing the improved guidance, software assurance personnel can systematically assess and verify the completeness, accuracy, and effectiveness of maintenance, operations, and retirement activities. These activities ensure risks are identified, software reliability is maintained, safety-critical operations are executed effectively, and project resources are archived compliantly for long-term reference or reuse. A proactive approach enhances mission safety, cost-effectiveness, and knowledge retention for future NASA projects.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase) * [SWE-196 - Software Retirement Archival](/spaces/SWEHBVD/pages/102695531/SWE-196+-+Software+Retirement+Archival)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence refers to demonstrable artifacts, records, or data that verify compliance with this requirement. The following categorized examples ensure that operations, maintenance, and retirement activities are carried out and documented effectively, allowing independent observers to confirm adherence.

---

### **1. Planning Documentation**

Objective evidence related to the planning of operations, maintenance, and retirement activities demonstrates that these processes have been sufficiently documented, approved, and baselined.

#### Examples of Objective Evidence:

* **Software Maintenance Plan**

  + Clearly outlines plans for defect resolution, adaptive changes, configuration management, and testing.
  + Includes stakeholder responsibilities, required resources, and timelines.
  + Contains details of metrics to be tracked during maintenance.
* **Software Operations Plan**

  + Operational procedures for using the software, including safety-critical commands and processes.
  + Backup protocols, error reporting processes, and anomaly resolution plans.
  + Contingency plans for critical operational failures.
* **Software Retirement Plan (May Be Part of the Maintenance Plan):**

  + Steps for archival of software artifacts, licenses, documentation, and project data.
  + Decommissioning and disposal procedures for hardware/software resources.
  + Transition plan for replacing functionality or preserving operational data (if applicable).
* **Documentation Reviews and Approvals:**

  + Records showing that operations, maintenance, and retirement plans have been reviewed, approved, and baselined by stakeholders (e.g., project manager, software assurance, safety team).

---

### **2. Operational Artifacts**

Objective evidence from the operational phase verifies that the software was used as intended and any issues were addressed through the predefined procedures.

#### Examples of Objective Evidence:

* **Software User’s Manual / Operational Documentation:**

  + Contains instructions for starting and using the software.
  + Includes safety-critical operations (e.g., handling of errors and commands that mitigate risks).
  + Documents all error messages and corresponding responses/corrective actions.
* **Operational Logs:**

  + Logs captured during actual software operation, including system outputs, operational states, and user commands.
  + Records of incident reports or anomalies during operations and their corrective actions.
* **Problem Reporting and Corrective Action (PRACA) Records:**

  + Problem reports submitted during operations, including resolutions or ongoing investigations.
  + Evidence that software anomalies are tracked and addressed through a well-defined corrective action system.
* **Operator Training Records:**

  + Evidence of user/operator training sessions, including attendance rosters, materials provided, and certifications (if applicable).
* **Backup and Recovery Testing Results:**

  + Records showing that operational backups are tested for functionality and readiness in case of system disruptions.

---

### **3. Maintenance Evidence**

Objective evidence for maintenance demonstrates that the delivered software is being actively maintained, tested, and updated over its lifecycle.

#### Examples of Objective Evidence:

* **Defect Tracking and Resolution Reports:**

  + Reports documenting the discovery, categorization, and resolution of software bugs or issues.
  + Metrics tracking the number and type of defects addressed over time.
* **Configuration Management Records:**

  + Change requests (CRs) for software updates or modifications.
  + Baseline control records tracking approved code changes and updated documentation.
  + Audit trails documenting configuration changes and their justifications.
* **Test Results for Software Updates:**

  + Results from regression testing of patches, adaptive updates, or changes to ensure no new issues are introduced.
  + Evidence of testing performed for specific defect fixes or new software enhancements.
* **Release Notes or Version Description Documents (VDDs):**

  + Documentation tracking the updates included in each successive software release.
  + Includes details of changes, fixes, and any impact on dependencies or stakeholders.
* **Metrics on Maintenance Effectiveness:**

  + Quantitative data such as response/resolution times for corrective maintenance.
  + Records of how many updates were tested, implemented, or reverted due to issues.
* **Milestone Review Documentation (e.g., Software Maintenance Plan Review Results):**

  + Records demonstrating review and approval of maintenance plans during key project milestones, such as Software Acceptance Reviews (SARs).

---

### **4. Retirement Evidence**

Objective evidence from the retirement phase ensures that software systems are properly decommissioned, archived, or transitioned.

#### Examples of Objective Evidence:

* **Archival Records:**

  + Evidence that all software artifacts (source code, executables, as-built documentation, test results) have been stored in a secure repository or configuration management system for future reference.
  + Retention records specifying the duration and location of archived data.
* **Decommissioning Logs:**

  + Logs or reports documenting the shutdown of systems, including steps to ensure sensitive data was erased or migrated.
  + Evidence confirming the safe disposal of hardware or release of system resources.
* **Software License Transfer or Cancellation Records:**

  + Documentation of actions taken to transfer licenses to successor teams or officially terminate agreements with vendors as part of software decommissioning.
* **Lessons Learned Reports:**

  + Documentation summarizing key takeaways from the software lifecycle, including operations, maintenance, and retirement.
  + Evidence that these lessons were submitted to NASA’s Lessons Learned Information System (LLIS) or similar repositories for reuse by future projects.
* **Process Audit Reports (Final Verification):**

  + Results from software assurance audits confirming that all retirement activities (e.g., data archival, license transfer, equipment disposal) followed the approved retirement plan.
* **Transition Plan Execution Records (If Applicable):**

  + Evidence of successful data/function transfers for software replaced by successor systems, including logs of data migration and verification that the replacement system operates as intended.

---

### **5. Software Assurance Products**

The following SA-specific products also serve as objective evidence to ensure compliance with Requirement 4.6.2.

#### Examples of Objective Evidence:

* **Audit Reports on Operations, Maintenance, and Retirement:**

  + Record of findings from audits conducted by software assurance personnel regarding adherence to plans and procedures.
  + Highlight any non-conformances and the process for mitigating them.
* **Risk Management Logs:**

  + Identified risks related to operations, maintenance, and retirement, including mitigation efforts and closure evidence.
* **Compliance Checklists and Records:**

  + Completed checklists against lifecycle standards to confirm compliance with NPR 7150.2 objectives.
* **Updated Software Assurance Plan:**

  + Evidence of how SA activities evolve through operations, maintenance, and retirement, ensuring continuous assurance of reliability and quality.

---

### **Conclusion**

Objective evidence for Requirement 4.6.2 spans the entire lifecycle, from planning to retirement. Comprehensive and verifiable artifacts—including documented plans, operational logs, test records, defect resolutions, user manuals, archival evidence, and audit results—help demonstrate that NASA projects fulfill compliance obligations while adhering to mission and stakeholder requirements. These records offer transparency, traceability, and independent checks to facilitate mission success and long-term system reliability.

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
