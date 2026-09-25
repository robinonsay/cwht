# SWE-083 - Status Accounting

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695465. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting

SWE-083 - Status Accounting

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695465)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695465&showCommentArea=true&showComments=true#addcomment)

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

5.1.6 The project manager shall prepare and maintain records of the configuration status of software configuration items. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-083 History

SWE-083 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.1.5 The project shall prepare and maintain records of the configuration status of configuration items. |
| Difference between A and B | No change |
| B | 5.1.6 The project manager shall prepare and maintain records of the configuration status of configuration items. |
| Difference between B and C | No change |
| C | 5.1.6 The project manager shall prepare and maintain records of the configuration status of software configuration items. |
| Difference between C and D | No change |
| D | 5.1.6 The project manager shall prepare and maintain records of the configuration status of software configuration items. |

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

Configuration status accounting (CSA) provides a way for a project to determine the content of configuration items (CIs) throughout the life cycle by capturing the status of submitted products such as data, models, scripts, code, and their associated change requests. It also allows project managers to monitor the developing software and know, based on status accounting reports, the contents of versions and releases of software.

The requirement to prepare and maintain records of the configuration status of software configuration items (5.1.6) is essential for effective software development and project management. Here is the rationale for including this requirement:

### 1. **Change Management**

* Software development often involves numerous revisions, updates, and changes to configuration items (e.g., source code, documentation, design files). Maintaining detailed configuration status records ensures that any alterations made to the software can be tracked and managed systematically.
* Configuration records allow the project manager to verify that all changes are authorized, documented, and implemented correctly, preventing unauthorized or accidental modifications.

### 2. **Traceability**

* Configuration status records provide a clear history of changes and the state of software items throughout the development lifecycle.
* This traceability is critical for audits, debugging, and understanding the evolution of the software. It ensures accountability for decisions made during development and identifies contributors who made specific changes.

### 3. **Compliance and Standards**

* Many industries (e.g., aerospace, healthcare, automotive, defense) have strict regulatory and compliance standards regarding documentation and configuration management.
* Maintaining configuration status records is necessary to comply with these standards, demonstrating adherence to best practices and ensuring quality assurance.

### 4. **Improved Collaboration**

* Clear configuration records allow team members, stakeholders, and reviewers to understand the current state of software items. This enhances collaboration, reduces misunderstandings, and ensures all parties are working with the correct version of the software.
* By maintaining up-to-date configuration records, teams can synchronize efforts across development, testing, and deployment activities.

### 5. **Risk Mitigation**

* Poor configuration management can lead to scenarios where outdated or incorrect versions of software are deployed, causing defects, system failures, or compliance violations. Configuration status records allow the project manager to identify such issues early and take corrective action.
* Accurate records reduce the risk of introducing inconsistencies and errors, ensuring that all stakeholders have confidence in the software development process.

### 6. **Supports Maintenance and Future Updates**

* Proper documentation of the configuration status enables efficient maintenance after the project is completed. It ensures that future updates, patches, or upgrades can be implemented without introducing errors or unexpected consequences.
* It allows engineers to understand the current state of the software and efficiently make changes without having to reverse-engineer or guess previous configurations.

### 7. **Facilitates Problem Resolution**

* In cases of software bugs, failures, or anomalies, configuration status records help identify when a problem was introduced and which version of the software is affected. This expedites problem resolution and helps teams revert to an earlier, stable state if necessary.

### 8. **Supports Project Planning and Reporting**

* Configuration status records provide the project manager with comprehensive insights into the development progress and the readiness of project deliverables.
* They assist in planning future tasks and in reporting accurate status updates to stakeholders.

### 9. **Enhanced Quality Assurance**

* Configuration status records ensure that all items in the software system meet quality standards and are managed systematically over time. This is integral to maintaining software integrity and reliability.

### Conclusion:

This requirement exists to ensure robust software configuration management systems are in place. It enables effective tracking, accountability, risk management, compliance, and quality assurance throughout the project lifecycle. By adhering to this requirement, the project manager can maintain control of software deliverables, facilitate smooth team collaboration, and enhance the reliability and maintainability of the software product.

See also [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description).

# 3. Guidance

## 3.1 Configuration Status Accounting

Configuration Status Accounting (CSA) refers to the process of recording and maintaining information about the status, contents, and changes to software configuration items (CIs) throughout the software’s lifecycle. This practice ensures transparency, traceability, and accessibility of necessary data for both the acquirer and the provider. Both parties should establish a status accounting system to track and manage configuration data. CSA also supports collaboration, decision-making, and compliance with applicable processes and regulations.

#### Key Functions of CSA:

* Track and document changes to configuration items (e.g., software components, documents, and artifacts) as they evolve during the lifecycle.
* Record the status of CIs, such as their versions, approvals, and current release state.
* Maintain a clear history of changes, which supports audits, maintenance, and integration efforts.

#### **Key Supporting References**:

CSA aligns with other configuration management processes, including:

* **SWE-063**: Release Version Description
* **SWE-080**: Track and Evaluate Changes
* **SWE-084**: Configuration Audits
* **SWE-085**: Release Management

When preparing and maintaining status accounting records, it is important to consider the intended audience and ensure that the information is clear, accessible, and actionable.

#### CSA Records: Key Considerations

When producing CSA records, the following information is crucial to provide a comprehensive view of the system:

1. **Stages of Configuration Items (CIs):**

   * Reflect the lifecycle stage of each CI, such as:
     + Draft
     + Under review
     + Ready for integration/delivery
     + Operational
     + Superseded (obsolete)
2. **Configuration Item Status:**

   * Indicate the following details for each CI:
     + Current version and history of changes
     + Whether the CI is checked in or out of the repository
     + Time of the last update
     + Identity of the person who made changes
     + A summary of what was updated or changed
3. **Change Requests/Problem Reports:**

   * Maintain status information on all Change Requests (CRs) and Problem Reports (PRs):
     + Whether they are open, under review, resolved, or closed.
     + References to the affected CIs and the nature of the resolutions applied.
   * See also **Topic 5.01: CR-PR - Software Change Request and Problem Report Management**.

#### Guidance on Determining CSA Data Needs:

The **SMA (Safety and Mission Assurance) Technical Excellence Program (STEP)** Level 2 Software Configuration Management and Data Management course offers a structured way to determine essential status accounting data for your project. Teams should collect and report data based on project needs. Key questions to consider include:

* What versions of which products are installed at which sites?
* What are the differences between specific versions?
* What is the version history of each CI in every product version?
* Which documents and supporting artifacts apply to specific product versions?
* What hardware configurations or dependencies are required to operate a given version of the product?
* When will the next version of a CI or product be available?
* Which versions of products are affected by specific CI revisions?
* Which revisions of CIs make up a specific product version?
* How many errors were reported, resolved, or remain unresolved in each version of the product during a specified time period?
* Which product versions are impacted by specific Problem Reports (PRs)?

#### Benefits of CSA:

* **Improved Traceability:** Enables the team to track every element and change within the software ecosystem.
* **Facilitates Maintenance:** Clear documentation of configuration statuses simplifies maintenance, upgrades, and issue resolution.
* **Supports Audits and Reviews:** Standardized status reporting ensures confidence during configuration audits and compliance evaluations.

## 3.2 Data Management

Data management in the context of configuration management involves the systematic control, storage, distribution, and access of relevant data items throughout the project lifecycle. While CSA focuses specifically on tracking CIs, data management supports a broader scope by applying similar principles to data assets, ensuring consistency, quality, and accessibility of data.

#### Coordination between CSA and Data Management:

When preparing and executing CSA activities, consider the integration or coordination of data management practices to create a unified, efficient system. This approach minimizes overhead, reduces redundancy, and ensures that all essential project data is readily available to stakeholders.

#### Steps for Effective Data Management:

1. **Define Data Management Requirements:**

   * Identify what information needs to be captured as part of CSA and general data management.
   * Collaborate with stakeholders to determine formats, accessibility requirements, and storage mechanisms.
2. **Capture Data in the CM Plan:**

   * Once the data management and CSA requirements are defined, articulate them in the **Software Configuration Management Plan (SCMP)**.
   * Refer to **SWE-079: Develop CM Plan** and **5.06: SCMP - Software Configuration Management Plan** for guidance.
3. **Ensure Alignment with Configuration Management:**

   * Establish clear connections between configuration management (e.g., specific CIs) and the related data assets (e.g., supporting documents, test reports).
   * Ensure that team members understand both the static (current version) and dynamic (revision history) aspects of the data.

### Summary:

* **CSA** helps track, document, and manage the status of configuration items across the software lifecycle, ensuring traceability, quality assurance, and regulatory compliance.
* **Data Management** extends these principles to all project data assets and ensures their effective coordination with CSA activities.
* CSA and data management efforts should align to support efficient workflows, reduce redundancies, and foster project-wide accountability.

By explicitly addressing the data needs of every stakeholder and documenting them in the appropriate plans, teams can ensure that status accounting and data management deliver actionable value in software engineering projects.

See also [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description), [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes), [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits), [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management), 

See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report),

See [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) and [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan)).

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

# 4. Small Projects

For small projects, the complexity and scope of Configuration Status Accounting (CSA) can be greatly simplified while still maintaining its vital functions. The goal is to ensure tracking and accountability without introducing excessive overhead or unnecessary bureaucracy. The following guidance is tailored for small projects with limited resources and smaller teams:

---

### **Purpose of CSA in Small Projects**

Configuration Status Accounting ensures that the current status of software Configuration Items (CIs), including their versions and changes, is clearly documented. In small projects, this enables smooth coordination between team members while providing traceability and accountability for changes throughout the project's lifecycle.

---

### **Step-by-Step Guidance**

#### **1. Define Configuration Items (CIs)**

Start by identifying the items in the software project that require tracking. For small projects, focus on key assets such as:

* **Source Code:** Core files and scripts.
* **Documentation:** Requirements specifications, user manuals, and test plans.
* **Executable Builds:** Release binaries or packaged software components.
* **Configuration Files:** Environment or system-specific files necessary for deployment.

Keep the CI list concise and limited to the necessary items to minimize tracking complexity.

---

#### **2. Establish a Simple Version Control Process**

For small projects, use a lightweight version control system to track changes and store historical versions. Options include:

* **Version Control Tools:** Tools like Git, Subversion (SVN), or Mercurial suffice for small teams.
* **Best Practices:**
  + Use clear commit messages to document changes.
  + Maintain a structured branching strategy (e.g., main branch for production, development branch for active work).

If the team is small (e.g., 2-5 people), a single collaborative repository may suffice.

---

#### **3. Maintain a Simple CSA Logging Document**

Instead of complex status reporting tools, create a single, lightweight document or spreadsheet (e.g., using Excel or Google Sheets) for CSA records. Include the following fields:

* **Configuration Item Name:** Identify the CI (e.g., “Source Code – Module A”).
* **Version Number:** Current version of the CI (e.g., “v1.2”).
* **Status:** Stage of the CI, such as:
  + Draft
  + Under Review
  + Ready for Integration/Delivery
  + Operational
  + Superseded (Obsolete)
* **Last Updated:** Date and time of the most recent update.
* **Change Summary:** Brief description of the changes made.
* **Responsible Person:** Owner or contributor who made the changes.
* **Associated Change Request/Issue:** Link or reference to the related change request, issue, or ticket (if applicable).

Use consistent formats to make the document easy to update and reference.

---

#### **4. Automate Where Possible**

For small projects, automation reduces effort and error:

* **Integrate Version Control with CSA Records:** Tools like GitLab or GitHub automatically provide version history and change tracking. These can serve as the primary CSA records.
* **Use CI/CD Tools:** If feasible, use Continuous Integration/Continuous Deployment (CI/CD) tools (e.g., Jenkins, GitHub Actions) to automate build history tracking.

---

#### **5. Regularly Update and Review CSA Records**

* Designate one team member (e.g., the project manager or lead developer) to oversee CSA updates. This minimizes responsibility overlap and ensures consistency.
* Update CSA records:
  + **Weekly:** For active small projects with frequent code changes.
  + **Major Milestone Completion:** When transitioning from one project phase to another (e.g., development to testing, testing to delivery).

---

#### **6. Perform Informal Audits**

Small projects don't require formal audits but should check CSA records periodically for:

* Accuracy: Ensure records match the actual status of CIs (e.g., version numbers, changes).
* Completeness: Confirm all major changes have been logged, and obsolete items are appropriately marked.
* Usability: Make sure records meet the needs of team members or stakeholders.

---

#### **7. Release Tracking**

For small projects, managing software releases is simpler:

* Define release versions (e.g., "v1.0" for initial delivery, "v1.1" for a minor update).
* Use a **Release Version Description (RVD)** to record:
  + What CIs are included in the release.
  + Changes/new features since the last version.
  + Known issues or limitations.

Tie each release to the CSA records for traceability.

---

#### **8. Keep Stakeholders in Mind**

Even in small projects, CSA records should be formatted for easy consumption by stakeholders. Examples:

* Developers: Need detailed CI information (e.g., version history, change summaries).
* Clients/End Users: May only need high-level information, such as release notes summarizing changes or new features.

Tailor CSA deliverables to the audience, avoiding unnecessary detail where possible.

---

### **Small Project Tools and Templates**

For small projects, the following tools and templates can streamline CSA:

* **Tools:**

  + **GitHub/GitLab:** Provides built-in version history tracking and release tagging.
  + **Google Sheets/Excel:** Simple spreadsheets for tracking CI status records.
  + **Trello/Jira:** Lightweight task boards for tracking change requests or problem reports.
* **Templates:**

  + Create a lightweight **CSA Log** with columns for CI name, version, status, last updated, responsible person, and change summary.
  + Develop a simplified **Release Version Description (RVD)** template to document releases.

---

### **Benefits for Small Projects**

Implementing CSA in small projects ensures:

* **Traceability:** Every configuration item’s history is easily accessible, reducing confusion about project progress.
* **Collaboration:** Team members work more efficiently by identifying the current state of CIs without guesswork.
* **Minimized Risk:** Changes are tracked, reducing the likelihood of introducing regressions or losing work.

By using lightweight processes and tools, small projects can benefit from CSA without unnecessary complexity.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-212)

  [IEEE Guide to Software Configuration Management,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=89631&tag=1 "Click to open in new window")

  IEEE Computer Society, IEEE STD 1042-1987, 1987.  This link requires an account on the NASA START (AGCY NTSS) system (https://standards.nasa.gov ). Once logged in, users can access Standards Organizations, IEEE and then search to get to authorized copies of IEEE standards.
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-343)

  [STEP Level 2 Software Configuration Management and Data Management course, SMA-SA-WBT-204, SATERN (need user account to access SATERN courses).](https://saterninfo.nasa.gov/ "Click to open in new window")

  This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Configuration Status Accounting (CSA) is a critical aspect of managing software development and maintenance throughout the lifecycle. NASA has learned many lessons over years of conducting complex projects, and these lessons can provide valuable guidance for implementing CSA effectively. Below is a consolidated list of NASA lessons learned relevant to this requirement:

---

### **1. Importance of Accurate and Timely Configuration Status Accounting**

#### **Lesson**

Failure to maintain accurate and timely CSA records can lead to delays, errors, and wasted resources during software development and deployment.

#### **Example**

In one NASA mission, the lack of updated configuration status records caused confusion about which version of the software was ready for testing. Developers inadvertently tested an outdated version that did not include critical bug fixes, wasting time and resources and delaying the project timeline.

#### **Guidance**

* Update CSA records immediately following any changes to software configuration items.
* Ensure CSA records consistently reflect the current state of hardware, software versions, and associated documentation.

---

### **2. Establish Clear Configuration Item Definitions**

#### **Lesson**

Ambiguity in what constitutes a configuration item (e.g., source code, documentation, tools) can lead to confusion and missed tracking.

#### **Example**

On a NASA project, CIs were poorly defined, resulting in certain critical items (such as calibration files for instruments) being excluded from CSA tracking. As a result, an incorrect calibration file was used during operations, leading to erroneous data.

#### **Guidance**

* Clearly identify and document what is considered a configuration item in the project’s **CM Plan** (Configuration Management Plan).
* Include all critical components that impact software functionality (e.g., source code, test plans, data files, hardware configurations).

---

### **3. Track Configuration Change Requests and Problem Reports**

#### **Lesson**

NASA projects have demonstrated that tracking the status of change requests (CRs) and problem reports (PRs) ensures transparency and provides stakeholders critical visibility into project risks and progress.

#### **Example**

During the development of flight software for a planetary mission, CRs and PRs were tracked inconsistently, causing confusion about the status of open issues. Team members implemented duplicate fixes, wasting time and effort.

#### **Guidance**

* Implement a consistent process for logging, tracking, and reviewing CRs and PRs, ensuring they are linked to the affected configuration item(s).
* Include tracking metrics for CR/PR resolution rates to monitor project progress and identify bottlenecks early.

---

### **4. Ensure CSA Records Are Scalable for Small and Large Teams**

#### **Lesson**

On larger NASA projects, CSA processes tend to be more formalized and extensive. However, smaller teams often struggle with "adapting" these formalized systems due to resource constraints, leading to incomplete CSA tracking.

#### **Example**

A smaller NASA software development team attempted to replicate the CSA process of a larger program but found the overhead too burdensome. Critical updates to status records were missed, leading to inconsistencies and confusion.

#### **Guidance**

* For smaller teams and projects, use lightweight CSA processes and tools (e.g., spreadsheets, Git version control logs).
* Scale CSA system complexity based on the size, budget, and scope of the project to avoid overwhelming the team.

---

### **5. Automate Configuration Status Accounting Where Possible**

#### **Lesson**

Manual status tracking can introduce errors and inefficiencies, particularly for large, fast-moving projects that require frequent updates.

#### **Example**

On a NASA software project, CSA records were managed manually, resulting in inconsistent entries and difficulties during audits. Discrepancies caused delays when reconciling different versions of the software and related documentation.

#### **Guidance**

* Leverage automation tools such as:
  + Version control systems (e.g., Git/GitHub, SVN).
  + Continuous Integration/Continuous Deployment (CI/CD) systems for automating build and release history tracking.
* Use automated scripts to pull version information, change logs, and CI statuses directly into CSA records.

---

### **6. Communicate CSA Records to the Right Audience**

#### **Lesson**

Failing to tailor CSA information to stakeholders can lead to misunderstandings or lack of engagement, especially if the information provided is too complex or irrelevant.

#### **Example**

On a NASA spacecraft mission, the CSA data presented to the mission assurance team included unnecessary low-level source code details. This led to confusion and delayed decision-making when evaluating whether software was ready for deployment.

#### **Guidance**

* Tailor CSA records based on the intended audience:
  + Developers: Include detailed version history, change summaries, and CI impact analysis.
  + Management/Stakeholders: Provide high-level summaries focused on project progress, risks, and readiness.
* Use templates or dashboards for presenting CSA records to different audiences clearly and efficiently.

---

### **7. Perform Regular CSA Reviews and Audits**

#### **Lesson**

Inaccuracies or omissions in CSA data are often discovered too late when audits or reviews are not conducted regularly, leading to significant project risks.

#### **Example**

During a NASA flight software audit, gaps in CSA records for prior versions of the software caused confusion over the lineage of changes. This introduced delays while the team reconstructed historical data.

#### **Guidance**

* Conduct regular reviews (e.g., weekly or monthly, depending on the project size) to ensure CSA records are accurate and complete.
* Schedule periodic configuration audits (see SWE-084 **Configuration Audits**) to verify the alignment of CSA records with the actual state of configuration items.

---

### **8. Develop a Lightweight CM Plan for CSA**

#### **Lesson**

Projects sometimes adopt overly complex configuration management plans that are unwieldy, especially for small teams. This can lead to incomplete CSA implementation and lack of buy-in from team members.

#### **Example**

On a NASA CubeSat software project, an overly detailed CM plan overwhelmed the small team, resulting in skipped updates to CSA records. This caused discrepancies during deployment, negatively impacting the mission's software readiness.

#### **Guidance**

* Develop a concise and tailored CM Plan for small projects that outlines essential CSA practices.
* Include minimal but necessary elements such as CI definitions, version control procedures, and the status reporting format.

---

### **9. Capture Lessons Learned for CSA Post-Project**

#### **Lesson**

Projects that fail to document lessons learned regarding CSA often repeat the same mistakes in subsequent missions.

#### **Example**

During a follow-on NASA satellite development project, the same CSA process deficiencies (e.g., incomplete tracking of calibration files) were encountered due to a lack of recorded lessons learned from a previous project.

#### **Guidance**

* At the end of the project, conduct a retrospective on CSA processes:
  + Evaluate what worked well and what could be improved.
  + Document lessons learned and incorporate them into the CM Plan for future projects.

---

### **Key Takeaways from NASA Lessons Learned**

* Always ensure CSA records are accurate, timely, and appropriately tailored to the audience.
* Automate CSA processes where possible to reduce errors and improve efficiency.
* Scale CSA processes to match the complexity and size of the project.
* Regularly review CSA records and conduct audits to maintain compliance and accuracy.
* Capture and integrate lessons learned into future projects to continuously improve CSA practices.

By adhering to these guidelines, small and large projects alike can benefit from effective Configuration Status Accounting and avoid common pitfalls encountered in NASA missions.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Develop a long term plan for labs](https://software.gsfc.nasa.gov/lesson-details/120/).**Lesson Number 120**: The recommendation states: "Develop a long term plan for labs that covers inventory and maintenance."

# 7. Software Assurance

**SWE-083 - Status Accounting**

5.1.6 The project manager shall prepare and maintain records of the configuration status of software configuration items.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project maintains records of the configuration status of the configuration items.

## 7.2 Software Assurance Products

Software assurance plays a key role in evaluating and verifying the completeness, accuracy, and effectiveness of configuration status accounting (CSA) processes. As part of this responsibility, software assurance should review and leverage the following key artifacts to assess compliance with this requirement:

1. **Software Problem Reporting or Defect Tracking Data:**

   * Evaluate the data from the tracking system to ensure defects and problem reports are appropriately linked to specific software configuration items (CIs), versions, and baselines. Verify that resolution statuses are updated accurately and consistently to maintain reliable CSA records.
2. **Software Configuration Management System Data:**

   * Analyze output from the project's software configuration management (SCM) tools (e.g., version control logs, change tracking history, statuses of CIs). Ensure that version histories, baselines, and operational states of each CI are consistently captured and reported.
3. **Software Assurance Audit Results of the Change Management Processes:**

   * Provide assurance that change control processes are properly implemented and auditable. Verify that all modifications to CIs (e.g., addition of a feature or fix of a bug) have been reviewed, approved, and logged in CSA records. Audit results should reflect adherence to change control policies.
4. **Software Version Description Document(s):**

   * For every software release or delivery, confirm the completeness and accuracy of the version description document (VDD). Verify that the VDD includes details on CIs in the current version, changes since the last version, any known issues, and the relationship between versions and baselines.

**Software Assurance Objective:** Confirm that these products collectively demonstrate accurate tracking of configuration statuses, the traceability of changes, and the completeness of status records across the lifecycle of the project.

## 7.3 Metrics

No specific metrics have been identified for this requirement at this time. However, software assurance teams may consider developing and applying the following project-specific metrics to measure the effectiveness and completeness of the CSA process:

1. **Metrics Specific to CSA:**

   * **Configuration Records Accuracy Rate:** Percentage of configuration records audited that were accurate and complete.
   * **Defect Traceability Metric:** Percentage of defects/problem reports (PRs) where the related CI(s) and version(s) are unambiguously identified.
   * **Change Implementation Time:** Average time taken to close change requests (CRs), starting from creation to final resolution and update in the CSA system.
   * **Baseline Approval Cycle Time:** Time required to approve and document a baseline or version after the associated CIs are finalized.
2. **Optional Metrics Categories:**

   * Percentage of overdue updates to CSA records.
   * Rework instances caused by incomplete or inaccurate CSA information.
   * Frequency of audits that result in findings related to missing or inaccurate configuration records.

**Metrics Tip:** Tailor these metrics to the specific software development project to ensure relevance and actionable insights.

## 7.4 Guidance

The software assurance role in supporting this requirement focuses on confirming the completeness, accuracy, and consistency of records generated through the configuration management process. Here are actionable steps for supporting software assurance activities:

---

#### **1. Leverage the Engineering Guidance in SWE-083**

* **Key Focus Areas:** Confirm that the records specified in SWE-083 are being kept, such as:

  + The items and their versions in each baseline.
  + Records describing the configurations being delivered (e.g., verification of consistency between the version description documents and the actual software being delivered).
  + The states of configuration items, such as “draft,” “approved,” or “superseded,” and the transition history between states.
* **Review the CSA Record Types:**

  + Ensure that all required record types (e.g., CIs, baselines, problem reports, CRs) have been logged and are auditable.
  + Verify that CSA records include sufficient detail to support traceability.

---

#### **2. Confirm the Completeness of Configuration Management Records**

* **Audit Configuration Records:**

  + Compare a random sample of CSA records for accuracy and alignment with the actual state of software components.
  + Verify that each CI is associated with the appropriate versions, baselines, and approvals.
* **Consistency Checks:**

  + Ensure records reflect the current state of the software, including accurate statuses for change requests, problem reports, and baselines.
  + Confirm that no key items are "orphaned" (i.e., not properly tracked in the system).
* **Traceability Audits:**

  + Perform spot checks to confirm that changes made to CIs are fully traceable through CRs, problem reports, and related software assurance reviews.

---

#### **3. Validate Version Description Documents (VDDs)**

* Review the software version description documents for each release and ensure they include:
  + A detailed description of what CIs were included in the release.
  + Changes made since the previous version.
  + Known issues or limitations in the current release.
  + Configuration baselines referenced in the release.
* Ensure versioning in the VDDs matches the actual version(s) recorded in the CSA system to avoid discrepancies.

---

#### **4. Assess the Change Management Process**

* Use software assurance audits to verify that the change management process accurately tracks all changes to CIs.
* Confirm that changes are evaluated for potential risk, reviewed by the appropriate authority, and only implemented after necessary approvals.

---

#### **5. Verify Tool Utilization**

* Confirm that tools (e.g., version control systems, problem reporting systems, and CI/CD pipelines) support the CSA process by:
  + Automatically capturing relevant configuration data.
  + Providing accessible reporting capabilities.
  + Supporting integration between change management, defect tracking, and version control.

---

#### **6. Tailor Guidance Based on Project Scale**

* For small projects, simplify CSA activities using lightweight tools (e.g., Git logs, spreadsheets) and focus on core records (e.g., critical CIs, baselines, and versions).
* For larger projects, enforce formal processes, such as regular audits, automated tools, and version description documentation for every delivery milestone.

---

### **Key Takeaways for Software Assurance:**

1. Confirm that all CSA records are being properly maintained, are accurate, and reflect the current status of the software.
2. Validate that there is alignment and traceability between configuration items, change requests, audits, and version description documentation.
3. Leverage software assurance audits to monitor and evaluate the CSA process, identifying any risks or nonconformances.
4. Use defined metrics or create project-specific ones to measure the effectiveness of CSA and highlight potential areas for improvement.

By focusing on these points, software assurance ensures that configuration status accounting contributes to project success, minimizes risks, and maintains compliance with SWE-083.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is required to demonstrate compliance with the requirement for tracking and maintaining configuration management records. This evidence establishes whether the processes, systems, and outputs related to Configuration Status Accounting (CSA) are functioning correctly, producing accurate records, and ensuring traceability and accountability throughout the software lifecycle.

Below is a detailed description of objective evidence Software Assurance and project teams can produce and collect to verify compliance:

---

### **1. Configuration Records**

Configuration records are the primary evidence demonstrating the state and status of configuration items (CIs). These records should include the following:

* **Version History:**

  + Documentation of all changes made to CIs as part of the project, including:
    - CI name
    - Version number
    - Status (e.g., Draft, Under Review, Approved, Released, Superseded)
    - Change history entries (author, date, description of changes).  
      Example: Version history logs from Git, Subversion (SVN), or other version control systems.
* **Baseline Definitions:**

  + Evidence of the baselines established throughout the software development lifecycle (e.g., requirements baseline, design baseline, test baseline). These records should include the CIs included in each baseline and their associated versions.  
    Example: A baseline document or project configuration report listing all items included in the baseline.
* **Release Documentation:**

  + A record of all items in a release, including which versions of which CIs were delivered in that release. Links to the software version description document (VDD) may serve as evidence.

---

### **2. Tracking Logs for Changes to CIs**

Records that provide traceability of changes made to a configuration item over time:

* **Change Request (CR) Tracking Logs:**

  + Records of all submitted change requests and their statuses, including traceability to affected CIs and the current state of each CR (e.g., Open, In Progress, Resolved, Rejected).  
    Example: Jira tickets or CR logs exported from a change management tool.
* **Problem Reports (PR) Logs:**

  + Records of problem reports to track defects or issues associated with CIs, including traceability to the changes made in response.  
    Example: Database extracts from tools like Bugzilla, GitHub Issues, or other defect tracking systems.
* **Audit Results of Changes:**

  + Records from software assurance audits of CR and PR processes. These audits confirm adherence to change control policies and accuracy of updates made to CSA records.

---

### **3. Software Version Description Documents (VDDs)**

The VDD provides critical information about the configuration of software releases. It is an essential piece of evidence for verifying the accuracy of tracked configuration data.

* Evidence includes:
  + Software items included in the release (and their versions).
  + Differences and changes made compared to prior versions.
  + Known issues or defects identified in the release.
  + Requirements or items supported in this version.  
    Example: Approved version description documents with sufficient detail to trace the release configuration.

---

### **4. Configuration Management Tool Outputs**

Automated tools used for Configuration Management (CM) and version control can provide objective evidence for CSA compliance:

* **Version Control System Logs:**

  + Evidence of the configuration items stored in the repository, version history of files, and commit messages.  
    Example: Logs from Git, GitLab, or similar tools showing commit history, branch structure, and tags.
* **Baseline Tags or Snapshots:**

  + System-generated tags or snapshots of the repository showing the versions of all CIs at the time of a specific baseline.  
    Example: Git tags for major release points, or baseline reports from tools like ClearCase or Perforce.
* **Build and Release Notifications:**

  + Continuous Integration/Continuous Deployment (CI/CD) logs from tools like Jenkins, Azure DevOps, or GitHub Actions showing the artifacts built for a specific version and which configuration was used.

---

### **5. Audit Reports**

Audit reports offer third-party confirmation that CSA processes were implemented and followed properly:

* **Configuration Management Audits:**

  + Reports from periodic audits of configuration management practices, confirming that:
    - Baselines were established and maintained.
    - Configuration records are updated and accurate.
    - Change requests and approvals are correctly logged and implemented.  
      Example: Configuration audit reports conducted by software engineering or assurance teams.
* **Process Compliance Audits:**

  + Reports verifying adherence to processes described in the Configuration Management Plan (CMP), as well as compliance with SWE-083.

---

### **6. Configuration Management Plan (CMP)**

The **Software Configuration Management Plan (SCMP)** or equivalent documentation provides evidence that the project has defined and implemented processes for CSA.

* Items to review in the CMP:
  + Policies for status accounting and record maintenance.
  + Description of versioning methods, baselines, and processes for tracking changes.
  + Defined roles and responsibilities for maintaining CSA records.  
    Example: A signed and approved CMP document stored in the project repository.

---

### **7. Status Reports**

Periodic reports summarizing the status of configuration items and baselines as the project progresses:

* Evidence includes:
  + Reports showing the state of all CIs at various milestones (e.g., draft, under review, approved).
  + Release readiness or integration readiness reports summarizing the current configuration of the software.

---

### **8. Traceability Evidence**

Traceability is critical for CSA and demonstrates the connection between requirements, design, code, and tests:

* **Traceability Matrices:**

  + Matrices that connect requirements, CIs, test cases, and their implementation in specific software versions.  
    Example: A requirements traceability matrix (RTM) that ties specific requirements to baselines and versioned CIs.
* **Change Traceability:**

  + Evidence showing traceability between a change request/problem report and the CI versions impacted by the change.

---

### **Examples of Objective Evidence**

Here’s a summary table of examples of objective evidence based on the artifacts listed above:

| **Artifact** | **Example Evidence** |
| --- | --- |
| Version Control Logs | Git logs showing commits, change description, and version tags. |
| Baseline Artifacts | Repository snapshots, baseline configuration reports, or tagged versions. |
| Problem Reports (PR) | Jira tickets, Bugzilla logs, or exported PR status data. |
| Software Version Description (VDD) | Approved document listing changes, CIs, defects, and known issues for each release. |
| Audit Reports | Audit summary showing results of CM compliance audits. |
| Change Request Logs | Reports from change management tools linking requests to CIs and state transitions. |
| Configuration Management Plan (CMP) | Signed, detailed CMP outlining the CSA process. |

---

### **Key Takeaways**

Objective evidence ensures that configuration status accounting processes are traceable, auditable, and compliant with requirements. Evidence should align with the project's processes and be accessible for audits and reviews throughout the lifecycle. By using automated tools, maintaining comprehensive documentation, and validating through audits, projects can ensure compliance with CSA requirements in SWE-083.

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
