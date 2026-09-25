# 5.04 - Maint - Software Maintenance Plan

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695658. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan

5.04 - Maint - Software Maintenance Plan

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695658)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695658&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Minimum Recommended Content](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

Return to [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)

# 1. Minimum Recommended Content

Minimum recommended content for the Software Maintenance Plan. 

1. 1. Plan information for the following activities  

      (1)  Maintenance process implementation.

      (2)  Problem and modification analysis.

      (3)  Modification implementation.

      (4)  Maintenance review/acceptance.

      (5)  Migration.

      (6)  Software Retirement.

      (7)  Software Assurance.

      (8)  Software Risk Assessment for all changes made during maintenance and operations.
   2. Specific standards, methods, tools, actions, procedures, and responsibilities associated with the maintenance process.  In addition, the following elements are included:

          (1)  Development and tracking of required upgrade intervals, including implementation plan.

          (2)  Approach for the scheduling, implementation, and tracking of software upgrades.

          (3)  Equipment and laboratories required for software verification and implementation.

          (4)  Updates to documentation for modified software components.

          (5)  Licensing agreements for software components.

          (6)  Plan for and tracking of operational backup software (e.g., backup flight software, backup to the primary operational software).

          (7)  Approach for the implementation of modifications to operational software (e.g., testing of software in development laboratory prior to operational use).

          (8)  Approach for software delivery process, including distribution to facilities and users of the software products and installation of the software in the target environment (including, but not limited to, spacecraft, simulators, Mission Control Center, and ground operations facilities).

          (9)    Approach for providing NASA access to the software version description data (e.g., revision number, licensing agreement).

# 2. Rationale

The Software Maintenance Plan provides insight into the method, approach, responsibility, and processes to be followed for maintenance of software and its associated documentation.  Having planned, reviewed, and approved activities for carrying out maintenance, operations, and retirement:

* Helps ensure that the outcome of the activities will meet the expectations of the project.
* Allows for thorough deliberation of tasks, methods, environments, and related criteria before they are implemented.
* Allows the plans to be tailored for a specific project's needs.

See also Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews),

# 3. Guidance

For the Software Maintenance Plan, provide separate volumes for each system element (e.g., ground operations, flight operations, mission operations, and spacecraft). The Software Maintenance Plan describes specific standards, methods, tools, actions, procedures, and responsibilities associated with the maintenance process.

When developing the Software Maintenance Plan, include information for carrying out the activities listed below. Where appropriate, references to documents describing existing processes, such as configuration management, may be included in the Software Maintenance Plan, but those documents and the processes they describe will need to be maintained for the life of the plan(s) that reference them.

Any operations, maintenance, and/or retirement activities that require supplier (software provider) support or action will need to be incorporated into the contract, because the contract is the binding document for contractor performance and deliverables. In these situations, maintenance planning is limited to the scope of the maintenance activities agreed to in the contract.

The content of the Software Maintenance Plan is important to consider during the earliest phases of a project when the Request for Proposals (RFPs), the Statement of Work (SOW), and the contract are being developed.

Maintenance planning can be started in these early phases and completed once the conditions for activities, such as software retirement, become known in the later phases of the project life cycle.

**Maintenance process implementation.** Processes and procedures for performing software maintenance, including processing requests for new software features and requests for changes to address problems, anomalies, or documentation changes.

**Problem and modification analysis**. Processes and procedures for capturing, reviewing, analyzing, and identifying the causes, potential solutions, and associated impact for problems and issues found during operations and maintenance (see also [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)); processes and procedures for analyzing the impact of new feature/functionality requests.

**Modification implementation.** Processes and procedures for implementing approved updates.

**Maintenance review/acceptance**. Processes and procedures for review and acceptance of updates:

* Before delivery and installation.
* To "determine the integrity of the modified system." [224](#_tabs-<p></p>)
* To obtain approvals "for the satisfactory completion of the modification as specified in the contract." [224](#_tabs-<p></p>)

**Migration.** Processes and procedures for moving the software to a new operational environment, including tools needed; data conversion activities, if required; support for the previous environment, user notification [209](#_tabs-<p></p>); and running parallel operations in both the old and new environments during the migration, as needed. [224](#_tabs-<p></p>)

**Software Retirement.** Processes and procedures for retiring software ( i.e., decommissioning, disposing, withdrawal of active support [209](#_tabs-<p></p>), making non-operational) including:

* Archival procedures.
* Procedures for securing the retired software and documentation, capturing lessons learned and final software metrics.
* Customer notification procedures.
* "Responsibility for future residual support issues." [224](#_tabs-<p></p>)
* Internal documentation to formally retire the software.
* Assessment of retirement impact on other systems and databases. [209](#_tabs-<p></p>)
* Transition to new.
* Replacement software [209](#_tabs-<p></p>), if applicable.

**Software Assurance.** Processes and procedures for carrying out software assurance through the end of life for the software, including but not limited to the following tasks from NASA-STD-8739.8 [278](#_tabs-<p></p>), Software Assurance and Software Safety Standard :

* Assuring "the transfer and maintenance of any licenses, simulators, models, and test suites from the developer to NASA, or the designated maintenance contractor." [278](#_tabs-<p></p>)
* Assuring "that any metrics collected on the software, along with any trending and reliability data, are transferred to the maintenance organization and maintained." [278](#_tabs-<p></p>) See also [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality).
* Assuring that software engineering and management prepare, approve, and execute a Software Maintenance Plan that includes retirement activities. [278](#_tabs-<p></p>)
* Performing or assisting with impact analysis for proposed changes, including safety impact analyses and impact analysis of COTS (Commercial Off The Shelf) changes. [276](#_tabs-<p></p>)
* Witnessing regression testing. [276](#_tabs-<p></p>)

**Software Risk Assessment for all changes made during maintenance and** **operations.** Processes and procedures for assessing risk associated with software changes made during the operations and maintenance life cycle phases (may be linked to or part of the "Problem and modification analysis" procedures listed above.)

**Development and tracking of required upgrade intervals, including implementation plan.** Software may have planned upgrades built into the overall life cycle; the maintenance plan addresses how those upgrades will be developed, tested, tracked, delivered, and installed according to the appropriate upgrade schedule.

**Approach for the scheduling, implementation, and tracking of software upgrades.** Processes and procedures for capturing the history of upgrades to a software package, including:

* Coordinating upgrades with the software user's operations schedule.
* Tracking delivery and installation of software packages across the customer base, as appropriate, i.e., which customers have which release of the software and when those releases were delivered and installed.

**Updates to documentation for modified software** **components.** Processes and procedures to ensure that development (e.g., design documents) and user documentation (e.g., operations manuals) are updated to match changes in the software and that the updated documentation is delivered with the appropriate software update

**Plan for and tracking of operational backup software, e.g., backup flight software, backup to the primary operational software.** Processes and procedures for maintaining backup software (software that takes over when the primary software fails). The standards, methods, tools, actions, and procedures for maintaining the backup software may be significantly different from the maintenance procedures for the primary software.

**Approach for the implementation of modifications to operational software, e.g., testing of software in development laboratory before operational use.** Processes, procedures, resources, needed to develop, test (including regression testing [276](#_tabs-<p></p>), and approve changes to operational software, including appropriate data capture, e.g., test results.

**Approach for software delivery process, including distribution to facilities and users of the software products and installation of the software in the target environment, including but not limited to spacecraft, simulators, Mission Control Center, and ground operations facilities.** Processes and procedures for release, delivery, and installation of software updates to customers, including coordinating these activities with the customer's operations schedule (e.g., some customers may be operational 24-7 with only limited planned downtime) and supporting configuration and operational data changes, as appropriate. See also Topic [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations)

**Approach for providing NASA access to the software version description data, e.g., revision number, licensing agreement.** Processes and procedures for NASA's access to identification, content information, licenses, etc. for software updates.

**Licensing agreements for software components.** References to agreements with suppliers/providers regarding updates, upgrades, patches, maintenance, etc., particularly, agreements for COTS software.

Licensing agreements typically include:

* Provider notification methods, schedules for patches, new versions, upgrades. [276](#_tabs-<p></p>)
* Compatibility of software upgrades with previous versions. [276](#_tabs-<p></p>)
* Access to developers and other technical support. [276](#_tabs-<p></p>)
* Support for previous software versions. [276](#_tabs-<p></p>)

**Equipment and laboratories required for software verification and implementation.** Description and identification of equipment and laboratory resources that may need to be retained from the development phases or be accessible during operations and maintenance to perform implementation and verification activities.

The project team considers the following general information for inclusion in the Software Maintenance Plan:

* Resources required to perform activities described in the plan, e.g., personnel, equipment, documentation, data, tools, facilities.
* Identification of maintenance organization(s), including subcontractors.
* Schedule for maintenance, if appropriate.
* Budget/costs, as appropriate for the plan.
* Support procedures, such as configuration management, metrics capture, risk management (may be references to existing plans, processes, procedures that will need to be kept up to date for the life of the plan).
* Description of maintenance records and reports to be generated.
* Training for maintenance personnel.

Additionally, guidance related to the Software Maintenance Plan may be found in [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement), [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase), [SWE-199 - Performance Measures](/spaces/SWEHBVC/pages/50889435/SWE-199+-+Performance+Measures),

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

For projects with limited staff or budgets, consider adapting a Software Maintenance Plan from a similar project, making sure to update the plan to reflect the current project's operations, maintenance, and retirement plans. The maintenance plan may also be included as part of another plan, such as the Software Management/Development Plan.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
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
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-540)

  [Computer Hardware-Software/Software Development Tools/Maintenance](https://llis.nasa.gov/lesson/1128 "Click to open in new window")

  Public Lessons Learned Entry: 1128.
* (SWEREF-543)

  [International Space Station (ISS) Program/Computer Hardware-Software/International Partner Source Code](https://llis.nasa.gov/lesson/1153 "Click to open in new window")

  Public Lessons Learned Entry: 1153.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase) * [SWE-199 - Performance Measures](/spaces/SWEHBVD/pages/102695532/SWE-199+-+Performance+Measures)        * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

* **Computer Hardware-Software/Software Development Tools/Maintenance. Lesson Number 1128[540](#_tabs-<p></p>)**: "NASA concurs with the finding that no program-wide plan exists addressing the maintenance of COTS software development tools. A programmatic action has been assigned to develop the usage requirements for COTS/modified off-the-shelf software including the associated development tools. These guidelines will document maintenance and selection guidelines to be used by all of the applicable program elements."
* **International Space Station (ISS) Program/Computer Hardware-Software/International Partner Source Code (Maintenance Agreements.) Lesson Number 1153[543](#_tabs-<p></p>)**: The Recommendation states to "Solidify long-term source code maintenance and incident investigation agreements for all software being developed by the International Partners as quickly as possible, and develop contingency plans for all operations that cannot be adequately placed under NASA's control."

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
