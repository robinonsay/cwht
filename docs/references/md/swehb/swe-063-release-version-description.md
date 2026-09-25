# SWE-063 - Release Version Description

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695447. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description

SWE-063 - Release Version Description

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695447)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695447&showCommentArea=true&showComments=true#addcomment)

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

4.4.7 The project manager shall provide a software version description for each software release. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-063 History

SWE-063 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.3.5 The project shall provide a Software Version Description document for each software release. |
| Difference between A and B | No change |
| B | 4.4.6 The project manager shall provide a software version description document for each software release. |
| Difference between B and C | No change |
| C | 4.4.7 The project manager shall provide a software version description for each software release. |
| Difference between C and D | No change |
| D | 4.4.7 The project manager shall provide a software version description for each software release. |

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
| * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |

# 2. Rationale

 A software version description document (VDD) is used to identify and record the exact version of software to be delivered to a user, support, or other sites.

A **Software Version Description (SVD)** is a critical document that ensures the controlled and transparent release of software for any project. It provides a snapshot of the software's current state, detailing the features, changes, and fixes contained in the release while identifying the exact configuration of the software being deployed. The rationale for this requirement stems from its importance in software quality assurance, traceability, accountability, communication, and efficient lifecycle management.

Below are the primary reasons for requiring a Software Version Description for each software release:

---

### **1. Establishes a Traceable Record of Releases**

* **Why it Matters**:
  + Traceability ensures a clear history of changes across software versions, enabling better understanding of the software's evolution.
  + By detailing the differences between each version, developers, testers, and maintainers can identify when specific features, bug fixes, or modifications were introduced.
* **Benefit**:
  + Facilitates root cause analysis for issues that arise post-release.
  + Supports audits or reviews for compliance with quality standards and software lifecycle requirements (especially important in regulated industries like aerospace, healthcare, and government).
* **Key Example**:
  + A bug is reported in the field. With an SVD, the team can identify the exact version deployed, compare it to prior releases, review documented code changes, and track the issue to the update or module responsible for the defect.

---

### **2. Enhances Software Quality Assurance and Configuration Management**

* **Why it Matters**:
  + An SVD documents the exact configuration of the software, including the versions of source code, dependencies, libraries, and tools used for building the release. This ensures that builds are reproducible and any potential inconsistencies can be addressed.
  + Inadequate version identification and documentation can lead to unintended deployment of outdated or unapproved software.
* **Benefit**:
  + Strengthens verification and validation activities by providing an authoritative reference point for testing and deploying software.
  + Ensures alignment between the software release and the configuration management plan, reducing the risk of errors due to mismatched versions.
* **Key Example**:
  + A small difference in a library version can cause an incompatibility, leading to unexpected software failure. With an SVD, the exact version of the library can be identified and aligned with the target environment.

---

### **3. Facilitates Communication Among Stakeholders**

* **Why it Matters**:
  + Software teams often involve multiple roles—developers, testers, project managers, quality assurance, and customers—all of whom need clear communication about what is included in each release.
  + An SVD provides a single source of truth regarding:
    - New features added in the release.
    - Known limitations or bugs that are still unresolved.
    - Changes to functionality that impact the user or other components.
* **Benefit**:
  + Reduces misunderstandings or incorrect assumptions about the capabilities or behavior of the software.
  + Builds trust with stakeholders by formalizing the release as a documented milestone.
* **Key Example**:
  + A customer receiving the SVD can directly refer to it for understanding what is newly delivered, ensuring their expectations align with the actual release.

---

### **4. Ensures Alignment with Safety-Critical Standards (as Applicable)**

* **Why it Matters**:
  + In safety-critical systems, strict documentation and traceability are necessary for audits, certification, and compliance with standards such as DO-178C (aviation), ISO 26262 (automotive), and NASA-STD-8739.8.
  + An SVD provides an important component of the safety evidence, recording:
    - Any hazard mitigations or fault-tolerant features included.
    - Verification and validation results demonstrating compliance with safety requirements.
* **Benefit**:
  + Helps reviewers confirm the completeness of the release and identify any risks introduced by changes with safety implications.
  + Provides a documented baseline to determine if safety-critical software can be deployed in operational environments.
* **Key Example**:
  + Before deployment of a new spacecraft software version, the SVD demonstrates all hazard-related defects have been resolved and properly tested to meet mission-critical reliability.

---

### **5. Improves Change Management and Risk Mitigation**

* **Why it Matters**:
  + Each software release introduces some level of risk, even with thorough testing. An SVD clearly states the purpose and scope of the release, making it easier to assess the level of risk and identify unanticipated downstream effects in operational use.
  + By documenting all updates, patches, and deviations from previous software behavior, the SVD helps teams proactively identify dependencies or conflicts early.
* **Benefit**:
  + Ensures that all changes are assessed for their potential to introduce errors or affect other components.
  + Helps prevent "version confusion" that can arise from undocumented interim versions or hotfixes applied outside of controlled processes.
* **Key Example**:
  + A testing team can refer to the SVD to determine whether prior test cases are sufficient or if new test cases are required due to changes introduced in the new version.

---

### **6. Supports Continuous Integration, Deployment, and Maintenance**

* **Why it Matters**:
  + Modern software projects often use iterative development, making it even more critical to document frequent version releases to avoid losing track of changes.
  + The SVD helps teams confirm that each software release is correctly deployed to the intended environment and that ongoing maintenance aligns with the precise version deployed.
* **Benefit**:
  + Enhances the reliability of agile and DevOps workflows by providing consistent version documentation.
  + Reduces confusion during maintenance and problem resolution, especially when multiple deployments or configurations exist.
* **Key Example**:
  + A satellite support team can compare the SVD of the current onboard software version with the previous version to ensure operational compatibility during updates.

---

### **7. Reduces Long-Term Sustainment Costs**

* **Why it Matters**:
  + Many software systems, especially in government and aerospace projects, have lifecycles that span years or even decades. Early and consistent version documentation ensures maintainers can understand and update the software long after the original development team is gone.
* **Benefit**:
  + Provides future teams with all necessary information (e.g., dependencies, configuration, past releases, bug fixes) to address issues and add functionality without requiring costly reverse-engineering efforts.
  + Facilitates compliance with standards for legacy software updates.
* **Key Example**:
  + Decades after the deployment of space mission software, maintainers can use SVDs to implement updates that adhere to the system’s original functionality.

---

### **8. Enables Effective User Support**

* **Why it Matters**:
  + The SVD informs end-users or operational teams about:
    - Known issues they'd need to workaround.
    - New functionality or features they can expect.
    - Updates or patches related to previously reported problems.
  + Makes it easier to diagnose issues that arise in the operational environment by knowing exactly which version of the software is in use.
* **Benefit**:
  + Creates a feedback loop between users and developers, as users can report issues with specific releases and developers can issue fixes with the necessary context.
* **Key Example**:
  + An SVD for ground systems software alerts operators to new support for additional telemetry data formats while advising that compatibility with legacy formats has not yet been tested.

---

### **Key Elements of a Software Version Description**

To meet the objectives above, an SVD typically contains:

1. **Version Information**: Identifier for the release (e.g., version number, build number, or timestamp).
2. **Release Overview**: Summary of the purpose, scope, new features, fixes, and known issues.
3. **Configuration Information**: Details of software and hardware dependencies, build tools, and versions.
4. **Release Deliverables**: Artifacts included in the release (e.g., executables, documentation, test results).
5. **Installation Instructions**: Steps to install or deploy the software.
6. **Test Results**: Evidence of the verification and validation performed (especially for critical systems).
7. **Applicable Documentation**: Reference to user manuals, interface control documents, etc.

---

### **Conclusion**

The Software Version Description (SVD) ensures that every software release is adequately documented, traceable, and communicated across stakeholders. It provides transparency and accountability for changes, supports efficient deployment and maintenance, and ensures compliance with critical industry and safety standards. For NASA, where the reliability of software can directly impact mission success, the SVD is not just a best practice—it's a necessity.

# 3. Guidance

Effective management and communication of software versions are central to ensuring that development, testing, deployment, and post-deployment activities proceed smoothly. A **Software Version Description (SVD)**—sometimes referred to as a **Version Description Document (VDD)** in NASA terminology—serves as the authoritative record for each software release. It communicates the contents, configuration, and context of a release and provides a foundation for maintaining traceability, mitigating risks, and enabling collaboration across distributed teams and stakeholders.

Below is an improved and detailed version of the guidance for this requirement.

---

### **Background and Importance**

Software systems evolve significantly over their lifecycle through iterative development, testing, corrections, enhancements, and reuse. These continuous updates create multiple software versions, with each version potentially existing in different phases of use—some in production, some under testing, and others in maintenance or retirement. Without a well-documented Software Version Description (SVD) for every released version, the following challenges can arise:

* Incorrect or outdated software versions may be used inadvertently.
* Teams may face difficulties debugging or managing compatibility issues.
* Configuration management can fail to match delivered software to the associated documentation or requirements.

### **Purpose of the Software Version Description Document (SVD)**

The SVD acts as a definitive record of a software release, detailing the content, configuration, and context of the release. This document:

* Provides transparency about what has changed, including added features, bug fixes, and known issues.
* Forms the basis for regression, re-creation, or validation of a released product.
* Helps manage versioned baselines and dependencies within a larger system.
* Documents installation, integration, and operating instructions specific to the release.
* Complies with project and contractual requirements for artifact visibility and traceability.

---

## 3.1 Software Version Description (SVD): Definition and Use

#### **Definition**

As stated in ISO/IEC/IEEE 24765:2017, the SVD is **“a document that accompanies and identifies a given version of a system or component.”** It typically includes:

* A list of the software and system components in the version.
* Identification of changes incorporated into the release.
* Information on installation, operations, and any dependencies unique to the release.

#### **Components of the SVD**

1. **Inventory of the Release:**

   * List of all system and software items included in the release.
   * Software version identifiers for each included component, beyond just a top-level version number (e.g., library versions, APIs, or third-party tools in use).
2. **Details on Changes in the Current Version:**

   * Functional changes (added features, removed features, or performance improvements).
   * Bug fixes and patches, including reference to defect reports.
   * Known limitations or unresolved issues (e.g., workarounds).
3. **Installation or Deployment Information:**

   * Clear instructions for installing or deploying the version.
   * Notes on special configuration or integration scenarios related to the release.
4. **Comparison with Prior Versions:**

   * Dependencies or integration impacts between the current version and previous releases in the development lifecycle.
   * Traceability to previous versions and the associated baselines.
5. **Supporting Artifacts and References:**

   * Details from supporting artifacts like the software architecture, detailed design, and source code.
   * Validation details, such as results from unit, integration, or system testing.

#### **Key Benefits of the SVD**

* **Configuration Control and Traceability**: Establishes precise mapping between software versions, code baselines, and related documentation.
* **Repeatability**: Ensures the ability to reproduce the system for testing, certification, or production.
* **Risk Mitigation**: Facilitates rollbacks to prior versions when an updated release introduces unforeseen issues.

#### **Using a Template**

Using a common SVD template across projects:

* Simplifies the generation of SVDs and improves consistency.
* Reduces the initial workload for developers and release managers.
* Ensures all required elements of the SVD are uniformly documented.

The content and recommended structure of an SVD are specified in Section 7.18 of NASA’s Handbook.

---

## 3.2 Software Release Version: Versioning and SVD Updates

Software versioning and configuration management are essential for maintaining clarity, integrity, and accountability throughout the software lifecycle. Each release or sub-release must adhere to a standardized versioning scheme, which is reflected in the corresponding SVD.

#### **Key Considerations for Software Release Versions:**

1. **Uniqueness**:  
   Each version of the software must be uniquely identifiable through its version number, ensuring there is no ambiguity when referencing a release.
2. **Version Granularity**:  
   Versioning should support multiple levels:

   * Major versions (e.g., functionality updates).
   * Minor versions (e.g., feature enhancements or critical patches).
   * Build numbers (e.g., internal development checkpoints or release candidates).
3. **Configuration Management**:  
   Configuration management systems (e.g., Git, SVN) must track:

   * Source code associated with each release.
   * Component dependencies.
   * Build configurations (e.g., makefiles or build scripts).
4. **Rollback Support**:  
   Configuration management should account for the ability to roll back software to earlier releases. This includes archiving prior source code and associated SVDs for future reference.
5. **SVD Updates for Each Release**:

   * Each updated SVD must fully document the changes from prior versions, enabling developers and stakeholders to understand the evolution of the software without referring to multiple documents.

#### **Risks Without Effective Version Control**:

* Team members could unknowingly work on outdated releases, reintroducing previously resolved bugs or misaligned functionality.
* Discrepancies between the operational environment and documented versions could impact mission success.

---

## 3.3 NASA-Specific Best Practices for the SVD

1. **Integration with Configuration Management Tools**

   * Regularly integrate SVDs with version control systems (e.g., a tagged release in Git corresponds to an SVD entry).
   * Automate metadata generation (e.g., build timestamps, component checksums) for inclusion in the SVD as part of the release process.
2. **Document Known Issues and Workarounds**

   * Promptly document unresolved issues and highlight their operational impact within the SVD.
   * Offer practical workarounds in the SVD to mitigate risks in operations.
3. **Validation Before Release**

   * The SVD should reflect code that has passed all planned verification and validation activities.
   * Flag any deferred testing tasks or partial compliance with requirements in the SVD.
4. **Collaboration and Security**

   * Coordinate with stakeholders to ensure SVDs address their needs (e.g., operational teams, customers, or auditors).
   * For sensitive projects, avoid including classified, proprietary, or unnecessary implementation details in externally shared SVDs.
5. **Utilize Lessons Learned**

   * Leverage NASA’s Software Processes Across NASA (SPAN) library to reinforce best practices and improve SVD content over time.

---

## 3.4 References to Related Requirements

* **SWE-077 Deliver Software Products**: Ensure that SVDs are included with every software delivery to provide traceable and comprehensive documentation for stakeholders.
* **SWE-083 Status Accounting**: Ensure that all components within the software release (and the SVD) are properly accounted for and traceable.

---

### **Conclusion**

A well-maintained Software Version Description for every release ensures precise software configuration management and contributes to mission assurance by:

* Facilitating stakeholder communication.
* Reducing the risk of errors and inconsistencies.
* Supporting certification, maintenance, and troubleshooting activities.

By embedding the SVD as a regular part of the software development and release process, NASA projects can ensure the controlled delivery of reliable and maintainable software systems.

Software systems and work products undergo multiple builds, reviews, and rebuild cycles before reaching a fully operational state.  Even then, modifications, error corrections, expanded requirements sets, and even code reuse on other projects result in newer versions of the coded product.  The configuration control of these versions, many of which may be used simultaneously on different projects, requires detailed descriptions to assure the correct work is being performed on the released version of interest.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting)        * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For smaller projects, the SVD can focus on delivering the essential details required for tracking, managing, and reproducing software releases. Below are the suggested simplified components of an SVD for small projects:

#### **1. Basic Release Information**

Clearly identify the release:

* Unique version identifier (e.g., Semantic Versioning: `v1.0.0`, `v1.1.0` for features, `v1.0.1` for patches).
* Date of release.
* Purpose of the release (e.g., "Initial release," "Bug fixes," "Feature update").

#### **2. Changes Summary**

Provide a concise description of what has changed in the release:

* New features or functionality added.
* Bugs or issues resolved.
* Any known limitations, workarounds, or incomplete features.

#### **3. Configuration Details**

Include basic information about the configuration:

* The software environment (e.g., "Built for Windows v10 and Linux Ubuntu 22.04").
* Dependencies or third-party libraries: versions of key tools, frameworks, and APIs used for the build.
* Source code repository and branch/tag info (e.g., Git tag `v1.0.0` or branch `main`).

#### **4. Installation Information**

Provide simple instructions for installing or deploying the software:

* How to install/setup the software (e.g., executable, scripts, or files to use).
* Any special operating environment requirements (e.g., necessary runtimes, hardware specifications).

#### **5. Traceability**

Maintain a lightweight traceability record for the release to:

* Link changes to high-level requirements (as applicable).
* Reference defect tracking IDs if bugs were fixed (e.g., "Fixed issue #145 reported in bug tracker").
* Point to previous versions for comparison (e.g., "Based on baseline version v0.9.0").

#### **6. Known Issues (Optional but Recommended)**

List any known issues that remain in this version:

* Briefly describe the problem and any workarounds.
* Mention if a resolution is planned for a future release.

---

### **Best Practices for Small Projects**

#### **1. Don't Overcomplicate the Process**

* Use templates or pre-filled forms for SVDs to save time (e.g., a simple Word document, spreadsheet, or markdown file).
* Limit the SVD to the essential details—focus on clarity and usability rather than exhaustive documentation.
* Automate where possible (e.g., generate version tags, include dependency lists, or export release notes from a version control system like Git).

#### **2. Use Version Control Effectively**

* Ensure the software repository is well-organized, with clear branching and tagging policies (e.g., use Git tags like `v1.0.0` or `release_candidate` to indicate software versions).
* Include the SVD file in the repository alongside the codebase for clear traceability.

#### **3. Set a Lightweight Versioning Strategy**

* Adopt a simple versioning scheme like **Semantic Versioning**:
  + `Major.Minor.Patch` (e.g., `1.0.0` where `1` is a major release, `0` is the initial minor version, and `0` is for no patches).
  + Increment versions consistently with each release to avoid confusion.

#### **4. Leverage Existing Tools**

Simplify the creation and management of the SVD by using tools and workflows that integrate with your development processes:

* **Issue Tracking Tools**: Tools like Jira, Trello, or GitHub Issues can help track and summarize fixes and features for inclusion in the SVD.
* **CI/CD Pipelines**: Automated pipelines (e.g., GitHub Actions, GitLab CI/CD, Jenkins) can generate version numbers, compile dependencies, and export basic configuration details.
* **Release Note Generators**: Tools like `changelog.md`, GitHub Release Notes, or Git tools can automatically create summaries of changes.

#### **5. Build the SVD Incrementally**

Don’t wait until the end of the project to create SVDs. Instead, update the SVD throughout development:

* Add entries for new features or fixed bugs as they are implemented.
* Maintain configuration information as builds are completed.
* Use the SVD as a "living document" during development rather than an afterthought.

#### **6. Engage the Team**

Since small teams typically juggle multiple responsibilities:

* Assign a single person (e.g., the project manager or lead developer) responsibility for ensuring each release has an SVD.
* Standardize the SVD process so all team members understand and contribute consistently.

#### **7. Focus on Communication**

For small projects, it is especially important that the SVD is written in clear and simple language so it can be easily understood by all stakeholders, even those without technical expertise.

---

### **Implementation Example for a Small Project**

#### **Software Version Description for Release v1.2.0**

**Project Name**: Mars Rover Navigation Software  
**Release Version**: v1.2.0  
**Release Date**: 2023-11-01

**1. Changes Summary**:

* **New Features**: Added support for obstacle detection using lidar sensors.
* **Bug Fixes**: Fixed issue causing the rover to misreport GPS coordinates during low-battery conditions (Bug #27).
* **Improvements**: Optimized terrain analysis algorithm, reducing computation time by 15%.

**2. Configuration Details**:

* **Test Environment**: Python 3.10, Ubuntu 22.04, TensorFlow 2.10.
* **Dependencies**:
  + NumPy v1.23.0
  + OpenCV v4.6.0
  + ROS (Robot Operating System) v2.2.5
* **Git Repository Tag**: `v1.2.0`

**3. Installation Instructions**:

* `pip install -r requirements.txt` to install required packages.
* Execute the `run_navigation.py` script to begin.

**4. Known Issues**:

* Obstacles smaller than 10 cm may not be detected reliably.
* Currently optimized for terrains with sharp elevation changes; minor terrain undulations may require further calibration.

---

### **Tools and Templates for SVDs in Small Projects**

* **Template Options**:

  + Use NASA's simplified VDD template from SPAN as a starting point.
  + Create a markdown template (e.g., `VERSION.md`) to standardize all releases within repositories.
  + Build release tracking summaries in tools like Google Docs/Sheets or Confluence.
* **Automation Tools**:

  + **GitHub Releases**: Automatically generate a release with changelogs and version tags.
  + **Semantic Release**: Automates versioning and changelog generation based on commit messages.
  + **Dependency Management Tools**: Tools like `pip freeze`, `npm ls`, or Maven's `dependency:tree` can export dependency lists.

---

### **Summary**

For small projects, the SVD ensures clarity, accountability, and quality compliance while addressing the practical constraints of limited resources. Utilize lightweight processes, templates, and tools to maintain an effective and sustainable version control and documentation process. By focusing on simplicity, automation, and incremental updates, small projects can generate SVDs that satisfy both internal needs and external standards like NASA’s requirements.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-230)

  [ISO/IEC/IEEE 24765:2017 Systems and software engineering -- Vocabulary.](https://www.iso.org/standard/71952.html "Click to open in new window")

  ISO/IEC/IEEE 24765:2017  It was prepared to collect and standardize terminology. Copy attached.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-573)

  [Aquarius Reflector Over-Test Incident](https://llis.nasa.gov/lesson/2419 "Click to open in new window")

  Public Lessons Learned Entry: 2419.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

#### **Original Lesson Summary from NASA Lessons Learned Database**

**Incident**:  
The **Aquarius Reflector** was damaged in 2007 during testing at the Jet Propulsion Laboratory (JPL) acoustic test chamber. The incident arose from an **over-test**, in which excessive test conditions were applied, compromising the hardware.

**Root Cause**:

* A **procedural deviation** led to improper execution of the test procedure.

**Proximate Cause**:

* A **test control system safing feature** (intended to prevent unsafe test operations) **did not activate**.
* Contributing factor: The **test control software** used to monitor and control the simulation had not been updated to the **current version**, further compounding the procedural failure.

**Outcome**:  
The Aquarius Special Review Board issued recommendations to prevent over-test incidents in the future. These recommendations emphasized:

1. Strict adherence to test procedures without deviation.
2. Ensuring test control software is kept updated to the latest validated version.
3. Implementing additional safeguards and redundant checks in test control systems.

---

### **Improved Lesson Analysis and Applicability**

This lesson underscores several key principles that are broadly applicable to software-reliant systems, especially in environments where safety, quality, and performance are paramount. Enhancing the analysis highlights other opportunities for improvement.

---

#### **1. Importance of Test Procedures**

* **Lesson Learned**: The deviation from approved test procedures contributed directly to the over-test incident. Procedural compliance is critical for ensuring complex testing operations are safely executed.
* **Guidance**:
  + Review and validate test procedures thoroughly, ensuring they account for all foreseeable risks.
  + Train personnel to follow these procedures rigorously and prohibit procedural deviations without formal review and approval.
  + Schedule periodic audits to ensure procedural compliance during tests.

---

#### **2. Configuration and Version Management of Test Control Software**

* **Lesson Learned**: Using outdated or improperly maintained test control software created a gap in the system’s ability to autonomously prevent excessive testing conditions. Software version mismatches can lead to misaligned configurations, reduced safeguards, and testing risks.
* **Guidance**:
  + Establish strong **configuration management** policies to track and manage software versions used in test environments.
  + Regularly verify and validate all test control software, ensuring it is updated to the latest certified version before use.
  + Introduce software version audits in pre-test checklists to prevent mismatches.

---

#### **3. Safing Systems and Redundancy in Test Environments**

* **Lesson Learned**: The failure of the test control system safing feature highlights the need for robust, redundant safeguards in critical operations. A single-point failure in safing mechanisms can have catastrophic consequences.
* **Guidance**:
  + Implement multiple layers of safing features, such as independent hardware- and software-based safing systems, to ensure one failure does not compromise safety.
  + Perform **fault tree analysis (FTA)** and **failure modes and effects analysis (FMEA)** to evaluate the reliability of all safing mechanisms and identify potential weaknesses.
  + Periodically simulate failure modes during non-critical operations to ensure safing features perform as designed under various scenarios.

---

#### **4. Design and Execution of Risk Reviews**

* **Lesson Learned**: Had earlier risk reviews included consideration of potential procedural deviations or outdated software issues, this incident might have been avoided. A systematic review of risks associated with manual processes and automated controls could enhance prevention.
* **Guidance**:
  + Establish **comprehensive special review boards**, like the Aquarius Special Review Board, for key phases of testing and operations.
  + Proactively identify risks specific to **hardware over-testing** and **software malfunctions**.
  + Collaborate cross-discipline to ensure operational risks are reviewed by engineers, software developers, safety teams, and mission personnel.

---

#### **5. Integrated Software-Hardware Testing**

* **Lesson Learned**: Test environments that involve both software and hardware components demand integrated testing and validation across both domains to prevent mismatches between expected and actual behavior.
* **Guidance**:
  + Conduct **end-to-end testing** where the hardware, software, and test environment operate as an integrated system during final validation stages to identify outliers.
  + Use simulations to mimic real-world conditions, ensuring that both hardware and software perform safely and fully within their design limits.

---

#### **6. Communication and Collaboration Across Testing Teams**

* **Lesson Learned**: The disconnect between the procedural team and the team responsible for maintaining the test control software led to the use of an outdated software version. This incident illustrates the need for better communication between teams managing different aspects of the test environment.
* **Guidance**:
  + Establish clear channels of communication across all teams involved in testing, including software, hardware, system engineering, and operations.
  + Require pre-test meetings to confirm that all procedural, software, and hardware elements are up to date and synchronized.
  + Use collaborative tools and processes (e.g., configuration control boards) to track and share information on system and software updates.

---

### **Additional Applicable NASA Lessons Learned**

#### **1. NESC Technical Bulletin: Rigorous Testing and Software Version Control**

* **Lesson Summary**:
  + Poorly defined processes for validating software tools used in test/operational environments have historically contributed to mission failures.
* **Guidance**:
  + Develop a robust strategy for validating test control software before its use in operations.
  + Specify exactly how software updates will be tested and approved before deployment.
  + Create an archive of previous software versions, formalizing rollback methods in case defects arise.

#### **2. Spirit and Opportunity Rover Lessons: Command Validation**

* **Lesson Summary**:
  + On the Mars "Spirit" rover mission, an improperly validated command was sent to the rover, leading to a reboot issue that temporarily jeopardized mission objectives.
* **Guidance**: Apply similar rigor to command verification during all phases of testing. Even in non-flight systems like test chambers, commands issued to hardware should be fully simulated and validated under notional conditions.

#### **3. Lesson from SOFIA Program: Ground Control System Variability**

* **Lesson Summary**:
  + The SOFIA airborne observatory encountered delays because software variabilities were insufficiently tracked across ground control equipment.
* **Guidance**:
  + Synchronize test control system versions and their dependencies (firmware, middleware, etc.) with project-wide hardware baselines to avoid downstream issues.

---

### **Summary of Lessons for Small and Large Projects**

The **Aquarius Reflector Over-Test Incident** provides broad insights applicable to any project, particularly when test environments involve a mix of software and hardware controls. By addressing the root causes of the incident—procedural deviations, outdated software, and inadequate safing mechanisms—future over-test risks can be mitigated. Additional lessons from NASA projects reinforce that establishing robust processes for test control software maintenance, communication, risk management, and integrated testing is critical for the success of both small-scale tests and mission-critical operations.

Proactively incorporating such lessons into standard practices can significantly enhance the reliability, safety, and performance of NASA software-reliant systems.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-063 - Release Version Description**

4.4.7 The project manager shall provide a software version description for each software release.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project creates a correct software version description for each software release.

2. For each software release, confirm that the software has been scanned for security defects and coding standard compliance and confirm the results.

## 7.2 Software Assurance Products

To ensure compliance with the requirement to maintain and verify software version descriptions for each release, software assurance plays a critical role in identifying, tracking, and resolving non-conformances, as well as ensuring accurate and reliable documentation. Below are the key deliverables and best practices for software assurance:

1. **List of Non-Conformances Tracked in an Issue Tracking System**:

   * Software assurance must verify that all identified **non-conformances** are documented in the project's tracking system. This includes:
     + Corrections tied to the **version description document (VDD)** (e.g., missing information or errors in version descriptions).
     + **Security defects**, including cybersecurity vulnerabilities (e.g., weaknesses, exploits).
     + Deviations from **coding standards** (tracked per severity or priority).
   * Ensure that tracking entries contain the following information:
     + Description and impact of the non-conformance.
     + Lifecycle phase in which the issue was found.
     + Assigned personnel and associated timelines for resolution.
     + Resolution status (open, closed, work in progress).
2. **Software Version Description Data for Each Release**:

   * For every software release, software assurance must verify the accuracy, completeness, and integrity of version description data.
   * Cross-check the project’s **SVD** with software configuration records to ensure consistency (e.g., version numbers, dependencies, and documentation).
   * Identify any discrepancies in release materials early and track them as non-conformances until resolved.

---

## 7.3 Metrics to Monitor Software Version Description Quality and Security

Software assurance teams can use key metrics to monitor the quality and accuracy of version descriptions, track vulnerabilities, and ensure alignment with project goals. Collecting and trending data over time provides insight into project health and helps mitigate risks.

**Cybersecurity Metrics**:

1. **Number of cybersecurity vulnerabilities and weaknesses identified** during testing, audits, and scans.
2. **Status of vulnerabilities and weaknesses** over time:
   * Open vulnerabilities (unresolved).
   * Closed vulnerabilities.
   * Categorized by severity (e.g., Critical, High, Medium, Low).
3. **Trends in vulnerabilities (open vs. closed)** over time, to track overall project risk and management efficiency.
4. **Types of vulnerabilities and weaknesses identified** (e.g., code injection vulnerabilities, authentication weaknesses, or hardcoded credentials).
5. **Lifecycle breakdown** of where vulnerabilities were found:
   * Design phase, implementation, testing, integration, deployment, or maintenance.
6. **Vulnerabilities identified vs. resolved** during implementation to measure remediation efficiency.
7. **Non-conformances in cybersecurity coding standard compliance**:
   * Open non-conformances remaining.
   * Non-conformances resolved after review or audit.

**Versioning and Documentation Metrics**:

1. **Planned vs. implemented requirements per release**:
   * Planned software requirements implemented per build.
   * Actual number of requirements delivered in the final release.
2. **Planned vs. delivered software units per release**:
   * Measure any discrepancies between expected and actual software components.
3. **Open vs. closed non-compliances in software scans or audits**:
   * Track findings from security scans or coding standard audits to ensure resolution before a release.
4. **Non-conformances identified in release documentation**:
   * Compare open vs. closed issues related to the **version description document** or other artifacts to track progress toward correct and complete documentation.

**Trending of Metrics**:

* Use trending metrics to identify recurring problem areas (e.g., cybersecurity weaknesses that frequently emerge during project phases or challenges in reconciling delivery documentation). Use these insights to improve processes and planning for future releases.

For additional metrics or suggestions, see **Topic 8.18 - SA Suggested Metrics**.

---

## 7.4 Guidance: Software Assurance for the Software Version Description

Software assurance has several important responsibilities to confirm compliance with the requirement to maintain and verify version descriptions for software releases. Following these practices ensures the accuracy, completeness, and security of all releases.

---

### **Key Software Assurance Responsibilities**

#### **1. Confirm Maintenance of SVD for Every Release**

* Ensure the project has a **Software Version Description (SVD)** (or Version Description Document, VDD) for each software release.
* The SVD should be updated after any release that involves new functionality, bug fixes, or configuration changes.

#### **2. Verify SVD Completeness and Accuracy**

* Review the SVD to ensure it contains all required elements outlined in **7.18 - Documentation Guidance, Software Version Description Document (VDD)**. These typically include:
  + Release identification.
  + Inventory of components included in the release.
  + Description of changes from prior versions.
  + Traceability to requirements or defects addressed.
  + Known issues, uncorrected problems, and workarounds.
  + Version information for tools, libraries, and dependencies.
  + Installation instructions.
  + Testing and validation artifacts.
* Cross-check that listed documentation, items, and artifacts are present in the release package and match the software version being released.

#### **3. Ensure Consistency Between Documentation and Deliverables**

* Perform/participate in **configuration audits** to ensure consistency between the documented version (SVD) and the physical release artifacts.
  + Confirm that software binaries, test results, build instructions, tools, and scripts are correctly documented in the SVD.
  + Check alignments, such as:
    - Code repository version tags.
    - Build outputs (release artifacts).
    - Documentation delivered with the release.

#### **4. Verify Virus Free Software**

* Confirm that the software to be released/delivered is free of viruses and malicious content.
  + Ensure all release packages or deliverables are scanned using up-to-date antivirus software prior to deployment.
  + Document results of the virus scans, including tools used and dates of the scans.
  + Immediately address and track any identified security issues until resolved.

#### **5. Requirements and Traceability Checks**

* Ensure the SVD properly tracks delivered artifacts (e.g., software executables, libraries, tools) to the approved requirements baseline.
* Confirm traceability between versioned software requirements, bug fixes, or enhancements mentioned in the SVD and those implemented in the actual release:
  + Verify that each planned requirement has been properly delivered and documented in the release.
  + Address any discrepancies before approval.

---

### **Physical Configuration Audit (PCA) Participation**

* For releases delivered to external groups (e.g., another NASA center, contractor, or operational customer), ensure that a **Physical Configuration Audit (PCA)** is executed.
  + The PCA confirms that the physical software artifacts, documentation, and SVD match the release requirements.
  + Software assurance may conduct or participate in the PCA to ensure compliance. Specific checks include:
    - All release components, including required tools, documents, and test results, are present.
    - All components match their documented versions, checksums, and identifiers.

---

### **Additional Guidance**

* Refer to **5.16 - VDD - Version Description Document** for specific data required within the SVD.
* Incorporate virus scans and traceability checks into pre-release workflows to streamline quality verification for subsequent releases.
* Monitor all open and closed issues in documentation through efficient tracking, including resolution of non-conformances prior to final delivery.
* Maintain alignment with **SWE-083 - Status Accounting** to ensure proper status tracking of all versioned components.

---

By fully integrating these practices, software assurance ensures the integrity of software version descriptions and supports the delivery of high-quality, safe, and reliable software tailored to NASA’s mission-critical operations.

 See the software guidance in this requirement for more information on a software version description document [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting)        * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical for verifying compliance with this requirement. It demonstrates through tangible artifacts and processes that the project maintains and reviews a **Software Version Description (SVD)** for each software release. Below is a comprehensive list of objective evidence that can be used to fulfill this requirement.

---

### **1. Version Description Document (SVD/VDD)**

* **Artifact**: A completed and signed-off Software Version Description (SVD) or Version Description Document (VDD) for each software release.

  + Includes the following elements (refer to NASA Handbook's *Topic 7.18 - Documentation Guidance* for details):
    - Software version number and identification.
    - Description of changes from prior versions.
    - List of components and their corresponding versions (e.g., libraries, APIs, third-party software).
    - Traceability to resolved issues, requirements, or prior releases.
    - Installation and setup instructions.
    - Known issues, workarounds, and limitations.
    - Validation and test reports for the release.
* **Verification Process**:

  + Ensure the SVD aligns with the software release version.
  + Confirm the presence of version-specific details, such as software configuration and dependencies.
  + Compare the SVD against the actual release package to verify completeness.

---

### **2. Configuration Management Records**

* **Artifact**: Configuration management system logs and artifacts that demonstrate control and tracking of software versions.

  + Key records include:
    - Repository tags or branches indicating each release version (e.g., Git tags like `v1.0.0`).
    - Commit/change history showcasing feature additions, bug fixes, or changes incorporated into the release.
    - Archived versions of software builds in the configuration management system.
  + Examples: Git, SVN, or other version control tools showing tagged repository snapshots or branches for `v1.0.0`, `v1.1.0`, etc.
* **Verification Process**:

  + Match repository tags or snapshots with the version mentioned in the SVD.
  + Confirm that the source code, artifacts, and dependencies are uniquely identified and traceable to the documented release version.

---

### **3. Release Package**

* **Artifact**: Verified release artifacts delivered as part of the software package. This includes:

  + Executables, source code, or libraries corresponding to the release.
  + Required build scripts or documentation (e.g., Makefiles, configuration files).
  + Dependency manifests or associated libraries/tools (e.g., `requirements.txt`, Maven `pom.xml`, or npm `package.json`).
  + Validation test results (see below).
* **Verification Process**:

  + Perform checksum validation or hash comparisons to verify release artifact integrity and consistency with the version specified in the SVD.
  + Ensure compliance with the configuration and versioning information in the SVD.

---

### **4. Validation and Test Reports**

* **Artifact**: Evidence of validation and testing performed for the release. These include:

  + Test reports validating the release against functional requirements (e.g., unit testing, integration testing).
  + Results of performance, security, and other non-functional tests.
  + Logs documenting successful execution of automated test suites during builds/releases.
* **Verification Process**:

  + Ensure that tests cover all requirements and known issues documented in the SVD.
  + Confirm that all test results are documented and associated with the correct software version.
  + Check logs of automated test suites to confirm versioned test coverage.

---

### **5. Physical Configuration Audit (PCA)**

* **Artifact**: Physical Configuration Audit (PCA) records verifying that the software and documentation in the release match the SVD and other configuration items.

  + PCA ensures alignment of:
    - Delivered artifacts (binaries, libraries, scripts).
    - Documentation (SVD, release notes, user manuals).
    - Build environment and tools.
* **Verification Process**:

  + Review signed PCA checklists ensuring all physical components match the documented SVD.
  + Validate audit logs documenting the reconciliation of software items with their version identifiers.

---

### **6. Traceability Matrices**

* **Artifact**: Traceability matrices linking the software release to its corresponding requirements, bug fixes, or prior versions.

  + Includes:
    - Requirements traceability matrix (RTM) showing planned vs. implemented requirements for the release.
    - Defect tracking matrix connecting resolved issues to the release version.
    - Change control records linking feature requests, CRs (Change Requests), or system updates to the version released.
* **Verification Process**:

  + Check that all resolved requirements and issues are appropriately documented in the SVD and traceable to the release package.
  + Ensure all discrepancies are tracked and explained in the SVD.

---

### **7. Security Assurance Artifacts**

* **Artifact**: Evidence of security analysis performed on the release.

  + Includes:
    - Results of virus scanning or malware detection for release artifacts.
    - Records from vulnerability scans or penetration tests for the release.
    - Summary of resolved and unresolved cybersecurity issues.
* **Verification Process**:

  + Confirm that all security vulnerabilities found in the release have been tracked and resolved prior to delivery.
  + Ensure that virus scan logs document no malicious code or content in the software.
  + Validate that all findings from vulnerability scans are accounted for in the SVD.

---

### **8. Metrics and Reports**

* **Artifact**: Metrics and trend analysis reports documenting the health and progress of the release process.

  + Examples include:
    - Trend of open vs. closed non-conformances associated with the release.
    - Number of planned features vs. implemented features in the release.
    - Trends in cybersecurity vulnerabilities (identified vs. resolved).
    - Audit results from software coding standard compliance checks.
* **Verification Process**:

  + Confirm that metrics align with the release goals and objectives outlined in the SVD.
  + Review reports to ensure all tracked metrics are accurate and reflect project reality.

---

### **9. Issue Tracking System Records**

* **Artifact**: Issue tracking system logs documenting all non-conformances identified during audits or testing.

  + Examples include:
    - Software defects impacting the release.
    - Missing information or errors in the SVD.
    - Non-compliance with coding standards or security standards.
* **Verification Process**:

  + Ensure all issues are resolved before release and documented in the SVD.
  + Reconcile issue tracking logs with the SVD for completeness and consistency.

---

### **10. Tools and Logs**

* **Artifact**: Evidence from development tools, build systems, and logs supporting the release.

  + Examples include:
    - Build logs confirming versioning consistency.
    - Logs of automated configuration checks or dependency validations.
    - Artifacts documenting rollback options if defects are found in the release.
* **Verification Process**:

  + Use tools like checksum generators, dependency scanners, or automated pipeline logs to validate release artifacts and version descriptions.

---

### **List of Objective Evidence for Review**

When reviewing objective evidence for this requirement, ensure the presence of the following items:

1. **Software Version Description (SVD/VDD)** document for the release.
2. Configuration management system documentation for tagged versions.
3. Release package artifacts (e.g., executables, build scripts, etc.).
4. Validation and test reports demonstrating compliance.
5. Physical Configuration Audit (PCA) records.
6. Requirements and defect traceability matrices.
7. Security assurance artifacts (virus scan and vulnerability analysis).
8. Metrics reports (e.g., cybersecurity trends, feature tracking).
9. Issue tracking system records.
10. Build tool logs and configuration validation artifacts.

---

### **Conclusion**

The objective evidence listed here demonstrates that every software release is accompanied by a comprehensive and validated Software Version Description (SVD). These artifacts provide the transparency, traceability, and accountability necessary to ensure high-quality software releases that comply with project requirements, security expectations, and NASA standards

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
