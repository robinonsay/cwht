# SWE-187 - Control of Software Items

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695523. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items

SWE-187 - Control of Software Items

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695523)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695523&showCommentArea=true&showComments=true#addcomment)

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

4.5.4 The project manager shall place software items under configuration management prior to testing.

## 1.1 Notes

This includes the software components being tested and the software components being used to test the software, including components such as support software, models, simulations, ground support software, COTS, GOTS, MOTS, OSS, or reused software components.

## 1.2 History

Click here to view the history of this requirement: SWE-187 History

SWE-187 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.5.4 The project manager shall place software items under configuration management prior to testing. |
| Difference between C and D | No change |
| D | 4.5.4 The project manager shall place software items under configuration management prior to testing. |

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
| * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 2. Rationale

Before software testing begins, all software items are placed under configuration control. This configuration control captures and identifies the versions of what is being tested. This serves several purposes: 1) Ensures that the correct version of the software is being tested. 2) Other items that are needed for the testing should also be under configuration control such as the test scripts, input data, versions of the operating system. This allows the tests to be repeatable to assist in finding defects. 

 Configuration management (CM) is a disciplined and systematic process that has proven essential for managing software development and testing in complex systems like those developed by NASA. By placing software items under configuration management prior to testing, this requirement serves as a critical safeguard to ensure software consistency, traceability, and reliability throughout the testing lifecycle.

Below are the key rationales for this requirement:

---

### **1. Ensures Consistency and Integrity in Testing**

Testing software that is not placed under configuration management can lead to inconsistencies, as uncontrolled versions of the software (or related artifacts) may inadvertently be tested. This introduces ambiguity in the testing process and invalidates results. Configuration management addresses this by ensuring that:

* The exact version of software being tested is clearly identified and controlled.
* The software, test environment, and associated test artifacts are reliable and consistent.
* Changes in the software are carefully tracked, and earlier versions can be referenced or restored if necessary.

#### Example:

If a test failure occurs, the ability to trace the exact version of the software under test allows the team to precisely identify and diagnose the cause of the failure.

---

### **2. Facilitates Reproducibility of Test Results**

Reproducibility is a cornerstone of software testing. Without configuration management, there is no guarantee that the same software and environment conditions can be reproduced for ongoing or future testing. CM ensures that:

* Each version of the software under test is frozen and documented, enabling repeated testing of the same configuration.
* Test results can be reliably reproduced and used for comparison in regression tests.
* Discrepancies between test environments or setups are minimized.

#### Example:

If a critical anomaly is discovered during testing, placing the software item under CM ensures that the same version is available for reproducing the defect and validating any fixes applied in regression tests.

---

### **3. Supports Traceability and Accountability**

Configuration management provides clear traceability from the software requirements to the code being tested and the test cases themselves. With CM:

* Every change, patch, or update to the software being tested is logged and linked to requirements, test artifacts, and test results.
* The testing process maintains accountability as software assurance personnel, reviewers, and stakeholders have access to the controlled artifacts used in every test run.

#### Example:

This traceability is critical for demonstrating compliance with safety-critical or mission-critical requirements during project audits or reviews.

---

### **4. Prevents Testing of Uncontrolled or Unverified Changes**

Without CM, changes to code or related artifacts (e.g., libraries, datasets, build scripts) may be introduced without proper review or approval, potentially rendering the test invalid or incomplete. Under CM:

* All changes are evaluated through a formal review and approval process before incorporation into the software version being tested.
* Unauthorized changes or updates are prevented, reducing the risk of untested or unstable code being released into the test phase.

#### Example:

Imagine a scenario where an overlooked code change modifies a safety-critical function during test preparation. Without CM, this change might not be documented, resulting in incomplete test coverage and significant mission risk.

---

### **5. Enables Efficient Regression Testing**

Regression testing ensures software stability after updates or fixes. CM ensures that:

* Baselines from earlier tests are preserved, so regression tests can confirm that new functionality or fixes do not negatively impact existing behavior.
* Historical test results are tied to specific software versions, facilitating easier identification of when and why regressions might occur.

#### Example:

A regression testing suite tied to a CM-controlled software version can quickly identify if a recent patch inadvertently broke an earlier fix or introduced new defects.

---

### **6. Control of Test Artifacts Beyond Code**

Configuration management also extends to:

* **Test Procedures and Test Plans**: Ensuring that everyone is referencing a consistent and approved set of test documentation aligned with the tested software version.
* **Test Inputs**: Managing the input datasets or conditions used for testing.
* **Test Results**: Maintaining control of generated test results for traceability and reproducibility.

By placing these items under CM, a consistent context for testing is ensured, which helps during audits or when recreating past test scenarios.

---

### **7. Mitigates Risks in Multi-Team, Multi-Phase Development**

In NASA projects, multiple teams often work concurrently on software development and testing. Without CM, there is a significant risk of teams working with outdated or incompatible versions of software, leading to inefficiencies, unreliable results, and mission delays. CM mitigates such risks by:

* Providing a single **controlled source of truth** for all software artifacts.
* Ensuring that updates are transparent and communicated across all teams.
* Preventing downstream effects of misaligned software versions in systems or integration testing.

#### Example:

During system integration, ensuring all teams use the same CM-controlled version of software helps prevent “version mismatch” issues when individual system components are brought together for testing.

---

### **8. Enables Adaptation to Software Changes During Testing**

Testing often reveals defects or areas for improvement, requiring rapid changes to the software under test. CM ensures that these changes are handled systematically:

* Changes are implemented in a controlled environment with clear documentation.
* Dependencies between software components, libraries, and tools are managed effectively.
* Backtracking or undoing changes, if necessary, is possible as earlier baselines are preserved.

#### Example:

After discovering a defect during testing, CM helps ensure that the updated version addressing the defect is validated against the same test conditions as the original, confirming that the fix is effective.

---

### **9. Facilitates Compliance with Standards and Audits**

NASA projects must comply with stringent standards (e.g., NPR 7150.2, NASA-STD-8739.8) for software development and assurance. CM enables:

* Comprehensive documentation to demonstrate conformity to testing requirements.
* Complete transparency for external audits, review teams, and stakeholders.
* Evidence-based assurance that software testing adhered to established processes and covered all relevant requirements.

#### Example:

If an auditor reviews testing processes, CM-controlled artifacts (e.g., approved test procedures, software baselines, and results) provide demonstrable proof that testing adhered to NASA-defined standards.

---

### **10. Promotes Overall Software Quality and Mission Assurance**

Configuration management prior to testing ensures that testing aligns with the highest standards of quality. By maintaining control of versions and their relationships to requirements and results, CM supports:

* Reduced testing errors caused by inadequate version control.
* Better communication and collaboration among development, testing, and assurance teams.
* A higher level of confidence in the software’s compliance, performance, and readiness for deployment.

#### Example:

In a safety-critical mission, this systematic approach avoids preventable defects or inconsistencies that could jeopardize mission success.

---

### **Conclusion**

Requiring that **software items be placed under configuration management prior to testing** is not just a best practice but a necessity for ensuring systematic, reliable, and efficient software testing. By enforcing consistency, traceability, and adaptability while minimizing risks and errors, this requirement directly supports NASA’s commitment to mission assurance, software quality, and operational safety. It reinforces the critical foundation for successful testing and readiness for mission-critical deployment.

# 3. Guidance

## 3.1 Configuration Management

Configuration Management (CM) is a critical and foundational discipline in software engineering. It ensures that all software artifacts are systematically controlled, managed, and tracked throughout the software development life cycle (SDLC), from initial creation to final release and maintenance. Effective CM enhances software quality, supports efficient decision-making, and reduces risks derived from uncontrolled changes or inconsistencies, especially in complex, safety-critical environments like those in NASA projects. Below is an improved and clarified guidance for requirement 3.1:

---

### **Definition and Purpose of Configuration Management**

Configuration management is the **structured process of managing and controlling changes to software systems** and maintaining a verifiable history of their evolution. CM ensures that throughout the project lifecycle:

1. **Configuration Items (CIs)** are clearly identified, defined, and documented.
2. The **release and change control process** is fully implemented to enable tracking and evaluation of modifications.
3. The status of configuration items (e.g., approved, in development, modified, tested) is recorded and reported in real time.
4. The integrity, completeness, traceability, and correctness of configuration items are verified.

---

### **3.1.1 CM Planning**

The first step to enable effective CM is the creation of a tailored **Configuration Management Plan (CMP)**. The CMP should:

* Define **roles and responsibilities** for CM processes (e.g., CM Lead, Change Control Board [CCB] members, stakeholders).
* Identify the specific **tools** (e.g., version control systems, defect trackers, CM database) used for managing configuration items.
* Outline the procedures for:
  + Identifying and documenting **Configuration Items (CIs)**.
  + Tracking and evaluating **changes** made to the software.
  + Maintaining **baselines** (e.g., code baselines, document baselines) as checkpoints for compliance and reviews.
  + Verifying and approving **releases**.
* Be reviewed and approved by appropriate stakeholders.

**Key References**:

* SWE-079: Develop CM Plan — Provides formal requirements and templates for developing a detailed and compliant CM plan.
* SWE-180: Software CM for Safety-Critical Software — Highlights special considerations for environments with safety-critical functions.

---

### **3.1.2 CM During Testing**

### **Independent Testing and CM**

All **software items for testing** should be placed under configuration management **before testing begins**. This is critical to ensure that changes to software items, test artifacts, and their dependencies are:

1. Fully controlled,
2. Traceable to their sources, and
3. Properly reviewed and approved.

#### Testing Artifacts to Place Under CM:

* **Software Components Being Tested**:
  + Source code, binaries, libraries, and executables under evaluation.
* **Testing Support Components**:
  + Test scripts, automated testing tools, datasets, input configurations, and expected outputs.
* **Infrastructure and Auxiliary Components**:
  + Simulation environments, models, mock-ups, and any external tools (e.g., COTS/MOTS like commercial or modified off-the-shelf software).
* **Documentation**:
  + Test procedures, test plans, test logs, test results/reports, and traceability matrices.

Placing these artifacts under CM ensures that:

* Consistency is maintained for test iterations or across environments.
* Future tests (e.g., regression testing) can reproduce the exact conditions of prior tests.
* Issues identified, such as failures or anomalies, can be traced back to specific test configurations or software versions.

---

### **3.1.3 Scope of Software Items under CM**

Configuration management **does not apply only to code**. It is a system-wide practice that involves all software aspects contributing to project success. Items under CM include, but are not limited to:

#### **1. Software and Code**

* Application source code, firmware, scripts, and executables.
* Libraries or reusable components (both custom and third-party).
* Software development tools such as compilers, linkers, and debuggers.
* Build scripts and configuration files.

#### **2. Documents**

* Software Requirements Specification (SRS).
* Software Design Documents (SDD).
* Test-related documents (e.g., test plans, test procedures, test logs).
* Configuration Management Plans and records.

#### **3. Test Infrastructure**

* Models, simulators, integrated testing environments.
* Hardware-software interface files.
* Ground support software (used for validating launch or space systems).

#### **4. Changes and Reviews**

* Change Request/Problem Report (CR/PR) forms/files.
* Hazard Reports (HR) and their code impacts (e.g., inadvertent operator action HR-33).

**Reference**: SWE-081 - Identify Software CM Items provides additional guidance on the specific software artifacts that should be placed under configuration management.

---

### **3.1.4 Special Considerations for Safety-Critical Software**

For Class A **(human safety-critical)** or hazardous functionality software, configuration management takes on additional importance due to the potential consequences of unverified changes or incomplete controls. Specific considerations include:

* **Hazard-Related Software Management**:

  + Identify all software contributing to hazardous operations.
  + Place all hazard reports, hazard mitigation software, and related test artifacts under configuration management.
  + Take extra care to identify dependencies between software components affecting safety-critical operations.
* **HR-33 (Inadvertent Operator Action)**:

  + Ensure CM controls prevent unvalidated changes introduced via operator interfaces or related software components that could inadvertently activate hazardous functionality.
* **Verification of Test and Operational Environment Consistency**:

  + Confirm that flight software and ground-support tools operate under controlled conditions identical to those tested during software qualification.

**Reference**: Topic 5.01 - CR-PR - Software Change Request/Problem Report provides further details on managing changes associated with hazards and high-risk software.

---

### **3.1.5 Change Control and Traceability**

The **Software Change Request (SCR)** process should be fully integrated with CM to control all changes made across project artifacts. This process should:

* Ensure changes are reviewed and documented in CR-PR forms prior to implementation.
* Include analysis of potential **downstream impacts** of proposed changes, especially for safety-critical software.
* Regularly audit the state of configuration items to verify traceability between:
  + Requirements ↔ Design ↔ Code ↔ Tests.

**Reference**: SWE-080 - Track and Evaluate Changes provides insight into tracking changes and evaluating their impacts throughout the lifecycle.

---

### **3.1.6 Benefits of CM to Projects**

Effective configuration management offers multiple benefits:

1. **Testing Integrity**: Testing is conducted on known, verified versions, reducing the risk of invalid or unreliable results.
2. **Risk Mitigation**: Eliminates risks caused by uncontrolled changes, particularly in safety-critical systems.
3. **Traceability**: Enables full traceability between software versions, test cases, requirements, and defect reports.
4. **Reproducibility**:
   * Ensures that test environments can be recreated at any point.
   * Facilitates regression testing by providing access to historical versions.
5. **Streamlined Audits**: Satisfies NASA compliance requirements (e.g., NPR 7150.2, NASA-STD-8739.8) by maintaining updated, controlled records of all CM artifacts.

---

### **Conclusion**

Configuration Management is far more than a "nice-to-have" process — it is an essential practice for ensuring software integrity, especially in high-stakes projects involving safety-critical and hazardous functionality. By planning CM early, rigorously applying controls to software artifacts, and integrating change management processes, projects can ensure their software products are traceable, repeatable, and reliable throughout the development and testing lifecycle. Compliance with CM practices ultimately supports NASA’s mission assurance objectives while minimizing risks to project success.

See also [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan).

See also [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes), [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items). See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report),

For Class A software take care to analyze all software affecting safety-critical software  and hazardous functionality including: [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation)      * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

# 4. Small Projects

Configuration management (CM) is a critical process for ensuring control, consistency, and traceability of software development and testing artifacts, even in smaller projects where resources and complexity may be limited. For small projects, CM can be streamlined to balance practicality and rigor without sacrificing software quality or safety assurance. The following guidance is tailored to small projects to help efficiently implement CM processes that align with the requirements of SWE-079, SWE-080, and SWE-081.

---

### **1. Simplify Configuration Management Planning**

* **Use Lightweight CM Plans**: For small projects, the CM plan can be a brief document outlining:
  + The tools used (e.g., Git, Subversion) for managing baselines and changes.
  + The process for identifying, controlling, and tracking configuration items (CIs).
  + Roles and responsibilities (e.g., a single person may act as the CM lead, change manager, and reviewer).
  + The frequency of status reporting and reviews.
* **Focus on the Essentials**:
  + Start with basic CM processes for version control, change tracking, and baseline management.
  + Gradually expand CM activities if the project's scope grows or becomes more complex.

*Reference*: SWE-079 - Develop CM Plan, which includes templates and flexibility for tailoring CM plans based on project size.

---

### **2. Identify and Control Key Configuration Items**

In small projects, Configuration Items (CIs) may be fewer and easier to manage. Focus on identifying only the essential items that must be controlled to ensure software consistency and traceability:

#### **Essential Configuration Items for Small Projects**:

1. **Source Code**:
   * Application code, scripts, and any dependency files used in the software build.
2. **Test Artifacts**:
   * Test plans, test procedures, test results, automated test scripts, and datasets.
3. **Requirements and Design Documents**:
   * Concisely documented requirements and design artifacts directly tied to code and test cases.
4. **Build and Deployment Artifacts**:
   * Build scripts, environment configuration files, and packaged binaries (as applicable).
5. **Change Requests and Problem Reports**:
   * Logs or simple forms to track issues, changes, and resolutions.

**Tip**: Document the items under CM in an easily accessible file (e.g., a "README" configuration file in the version control repository).

---

### **3. Use Simple Version Control Tools**

For small projects, a lightweight but robust version control system can serve as the cornerstone of CM:

* Use tools like **Git** or **Mercurial** (free and widely supported across platforms).
* If unfamiliar with version control, start with a simple GUI-based tool (e.g., GitHub Desktop, Sourcetree).
* **Organize the Repository**:
  + Establish a clear structure (e.g., separate directories for code, documents, and test artifacts).
  + Use meaningful commit messages to document changes, linking them to specific requirements or issue reports where possible.

#### **Best Practices**:

1. Create **branches** for testing, development, and production versions of the software to isolate changes.
2. Document how the repository is structured in a "CONTRIBUTING" or "README" file to help team members follow the workflow.

---

### **4. Streamline Change Control**

In small projects, formal processes like a Change Control Board (CCB) may not be practical. A simpler, streamlined change control process can help manage changes efficiently:

#### **Steps for Managing Changes**:

1. **Record the Change**:
   * Use a simple log (spreadsheet, lightweight ticketing system, or issue tracking tool like GitHub Issues or Jira) to track:
     + Description of the change.
     + Who requested the change.
     + Who is implementing the change.
     + The date and purpose of the change.
2. **Review and Approve Changes**:
   * Even if the project is small, changes should be **peer reviewed** or approved by someone other than the developer to confirm their alignment with requirements.
3. **Implement the Change in Version Control**:
   * Use commits to document what was changed, why, and what files were affected.
4. **Test and Verify**:
   * Before closing a change request, verify the changes through an appropriate level of testing (e.g., confirm fixes for requirements, verify no regressions).

---

### **5. Establish Baselines**

For small projects, critical milestones (e.g., before testing, delivery, or major changes) should trigger the creation of **baselines**—snapshots of software and related artifacts to preserve their state.

#### **Key Baselines for Small Projects**:

1. **Development Baseline**:
   * Established at major progress points in development (e.g., completion of a feature or module).
2. **Test Baseline**:
   * Created before formal or independent testing begins to track what version of the software and test artifacts are being tested.
3. **Release Baseline**:
   * Captures what was delivered to the customer or end user.

#### How to Manage Baselines:

* Tag versions in the version control system (e.g., use Git tags to label baselines).
* Document the configuration of each baseline in an index file (e.g., record the version of code, test scripts, and dependencies used).

---

### **6. Automate Wherever Possible**

Small projects often have limited resources. Using automation can reduce administrative overhead and improve CM adherence:

* **Automate Builds**:
  + Use tools like **GitHub Actions**, **Jenkins**, or **GitLab CI/CD** to automate building the software for testing or releases.
* **Automate Testing**:
  + Use build and test scripts to validate software automatically when changes are made, ensuring continued functionality.
* **Automate Version Control Hooks**:
  + Set up commit hooks to enforce naming conventions, require commit messages, or trigger specific actions after a change is pushed.

---

### **7. Integrate CM into Testing**

* Ensure all software, test scripts, and test environment configurations are fixed under CM **before testing begins**.
* For regression testing, use baselined versions of both software and tests to reproduce prior results.
* Record the versions of every CI involved with test results, linking them back to baselines and change requests for traceability.

*Reference*: SWE-080 - Track and Evaluate Changes is especially helpful for linking testing results with CM processes.

---

### **8. Special Considerations for Safety-Critical or High-Risk Features**

Even small projects may include software with safety-critical features or interfaces that contribute to hazardous functionality. In these cases:

* **Prioritize Control of Safety-Critical Items**:
  + Ensure that all software impacting safety-critical functionality is clearly identified and tracked.
  + Scrutinize all changes to software contributing to hazard controls, with additional reviews and approvals as necessary.
* **Document Dependencies**:
  + If high-risk software relies on external tools (e.g., COTS/MOTS components), their configurations and versions must also be documented under CM.
* **Perform Additional Testing**:
  + For hazard-related software, verify that each change is tested under nominal, off-nominal, and stress scenarios.

*See*: Topic 5.01 - CR-PR for managing software changes tied to hazard controls.

---

### **9. Communicate Roles and Expectations**

In small projects, it is common for one person to wear multiple hats (e.g., developer, tester, and CM lead). Communication becomes critical:

* **Designate Clear Responsibilities**:
  + Assign someone as the CM lead (even if they perform other roles), responsible for maintaining baselines and overseeing change control.
* **Clarify Processes and Tools**:
  + Ensure all team members understand the CM workflow, including how to commit changes, request reviews, and verify baselines.

---

### **Conclusion**

Configuration management for small projects doesn't have to be overly complex but must provide the basic structure for managing software and its evolution. By focusing on lightweight planning, essential artifact control, simplified change management, and automation, small projects can maintain CM compliance without burdening resources. This approach ensures software consistency and quality while mitigating risks and satisfying key NASA requirements.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

Configuration management (CM) is a fundamental practice for ensuring consistency, traceability, and reliability in software systems. Properly managing software artifacts and changes throughout the software lifecycle is critical for project success, especially in high-stakes environments such as those overseen by NASA. This section draws from NASA's **Lessons Learned Information System (LLIS)** and documented mission experiences to highlight the key insights and lessons related to Requirement 3.1: placing software items under configuration management prior to testing.

---

### **Lesson 1: Lack of Proper Configuration Management Can Lead to Mission Failure**

**Lesson Learned #0338** - *Mars Climate Orbiter: Metric Conversion Error*

* **Summary**: NASA’s Mars Climate Orbiter was lost due to a failure to properly manage and verify the configuration of software items. A discrepancy between metric and English units in critical navigation-related software was not caught during development or testing because different teams (contractor and NASA) were using inconsistent tools and data sets.
* **Root Cause**: The navigational software and related ground-support equipment were not fully controlled under a unified CM process that accounted for unit consistency.
* **Takeaway**:
  + Clearly identify all software configuration items (including engineering units, tools, and data).
  + Ensure that all items under CM are validated and verified before use in testing or operations.

**Related Guidance**: Utilize the CM process to document every software artifact, including supporting datasets, and confirm their consistency within the operational context.

---

### **Lesson 2: Uncontrolled Software Changes Introduce Critical Risks**

**Lesson Learned #0589** - *Mars Exploration Rover: Inadequate Control of Changes*

* **Summary**: A software patch introduced for the Spirit Mars Rover during the operational phase inadvertently caused a serious fault that resulted in loss of communication with the rover for several days.
* **Root Cause**: The patch was not properly reviewed, tested, or controlled under CM processes prior to deployment. This mistake disrupted the programming logic and led to memory overflows.
* **Takeaway**:
  + Every change to software, including transient patches or updates, must follow the CM process, even during operational or testing phases.
  + Test software under controlled and traceable conditions, ensuring all changes are associated with appropriate reviews and approvals.

**Related Guidance**: Apply rigorous CM to all software updates and align the testing environment to CM-controlled baselines.

---

### **Lesson 3: Insufficient Test Baseline Control Leads to Inconsistent Results**

**Lesson Learned #0798** - *X-43A Software Testing Issues*

* **Summary**: During testing of the X-43A scramjet propulsion system, critical software items, such as test scripts and support models, were not appropriately governed under a unified CM process. Competing versions of scripts were used in different testing phases, leading to unintentionally modified inputs.
* **Root Cause**: Lack of a single, unified test baseline under configuration control caused inconsistent and unrepeatable test outcomes.
* **Takeaway**:
  + Baseline all test artifacts (e.g., test scripts, datasets, and simulators) before formal or informal testing begins.
  + Use CM to ensure that all updates or changes are controlled, traceable, and aligned with project requirements.

**Related Guidance**: Clearly define and enforce baselines for testing, and use tools (e.g., version control systems) to track modifications and their approvals.

---

### **Lesson 4: Overlooking Configuration Dependencies Causes Operational Failures**

**Lesson Learned #1322** - *SOHO Mission: Software Configuration Issue*

* **Summary**: The SOHO spacecraft lost orientation control due to a software update that was not fully tested in the operational environment. The configuration dependencies between the newer software and legacy components were not properly managed, resulting in an incompatibility.
* **Root Cause**: The CM process failed to address dependencies between software items, resulting in an undetected incompatibility between the updated software and existing units.
* **Takeaway**:
  + Properly document and track configuration dependencies, especially for systems where legacy components interact with newer software.
  + Test software as part of an integrated system under CM-controlled configurations to uncover potential issues.

**Related Guidance**: Use CM to maintain detailed records of interoperability requirements and thoroughly test any changes in environments that mimic the integration and operational conditions.

---

### **Lesson 5: A Lack of CM Oversight Reduces Traceability During Development**

**Lesson Learned #2236** - *Lunar Atmosphere and Dust Environment Explorer (LADEE)*

* **Summary**: During the development of LADEE software, insufficient documentation and traceability of software versions and their associated test results complicated the debugging and verification process. The team struggled to trace certain anomalies to the version they originated from and wasted valuable time performing redundant tests.
* **Root Cause**: Configuration items were not consistently baselined or labeled in a version control system, leading to confusion during testing and fixes.
* **Takeaway**:
  + Ensure consistent use of version control tools to track all changes to software and test artifacts.
  + Label software builds and testing environments clearly and systematically to support traceability during debugging and regression testing.

**Related Guidance**: Leverage modern CM tools such as Git or Subversion for small or large projects, ensuring every build, change, and test artifact is clearly versioned and documented.

---

### **Lesson 6: Configuration Management Prevents Regressions**

**Lesson Learned #1281** - *International Space Station (ISS) Software*

* **Summary**: During development and regression testing for ISS control software, an issue occurred where an older, incompatible version of a critical software module was reintroduced into the build by mistake. The problem caused errors during integration testing and delayed delivery.
* **Root Cause**: The CM system did not enforce the tracking of specific module versions in the software product hierarchy, allowing older versions to inadvertently reenter the software baseline.
* **Takeaway**:
  + Use the CM process to enforce strict versioning of software components and restrict reintroduction of outdated or incompatible modules.
  + Perform audits of component versions before testing to ensure the software under test is aligned with controlled baselines.

**Related Guidance**: Implement automated build and CM processes to reduce the likelihood of human error when managing software baselines.

---

### **Lesson 7: Ensure Testing Includes CM-controlled Supporting Software**

**Lesson Learned #2047** - *Support Software Impacts on Testing*

* **Summary**: A project team testing a flight-capable instrument software package realized late in the process that results generated from simulations varied due to inconsistencies in the simulation support software version. The support software had not been placed under CM, resulting in unexpected discrepancies between test runs.
* **Root Cause**: The CM process focused only on the flight software and neglected configuration control of the support software used for evaluation and validation.
* **Takeaway**:
  + Place all supporting software—such as simulators, models, and test automation scripts—under configuration management to ensure consistent test conditions.
  + CM should extend to all dependencies that could impact the quality and accuracy of testing.

**Related Guidance**: Ensure CM processes include a comprehensive view of all software affecting development and testing environments.

---

### **Overall Insights and Best Practices**

From these lessons, the following key themes emerge to guide the implementation of CM for meeting Requirement 3.1:

1. **Control Before Testing**: Always ensure software components, test artifacts, and dependencies are placed under configuration management before testing begins.
2. **Track Everything**: Use version control and CM tools to track all changes, dependencies, and baselines for traceability and consistency.
3. **Test in Controlled Environments**: Align the test environments with CM-controlled baselines to ensure reproducibility and reliability.
4. **Document Dependencies**: Record all software items and their interactions (legacy compatibility, simulator versions, etc.) to avoid integration issues.
5. **Enforce Rigor**: Even in small or simple projects, ensure CM policies are followed consistently to prevent costly mistakes.

By applying these lessons learned, NASA projects can reduce risks, improve testing reliability, and ensure software meets mission-critical needs.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-187 - Control of Software Items**

4.5.4 The project manager shall place software items under configuration management prior to testing.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that software items to be tested are under configuration management before the start of testing. 

2. Confirm the project maintains the software items under configuration management through the completion of testing.

## 7.2 Software Assurance Products

Software Assurance (SA) plays a critical role in ensuring that all necessary software items are placed under strict configuration management (CM) before and during testing. This guidance expands and clarifies the responsibilities of Software Assurance to monitor, review, and verify the CM process, ensuring that the software testing activities and supporting artifacts are fully controlled and traceable.

## 7.3 Metrics

To guide improvements and ensure accountability, Software Assurance should track and monitor key CM metrics throughout the software lifecycle. One such fundamental metric is:

* **Number of software work product Non-Conformances identified by life cycle phase over time**:
  + This metric tracks instances of software configuration errors, missing version controls, or mismanaged baselines that disrupt the testing process.
  + By reviewing these metrics, trends can emerge that highlight weak points in the CM process, enabling corrective actions to be implemented.

For additional metrics related to Software Assurance practices, see **Topic 8.18 - SA Suggested Metrics**, which outlines other measures of success tied to quality assurance and configuration management compliance.

---

## 7.4 Guidance: Software Assurance Responsibilities and Considerations

#### **1. Review and Confirm Items Are Under Configuration Management Before Testing**

Before formal, independent, or any major test activity begins:

* **Confirm the Software Items Under CM**:

  + SA will review the list of configuration items intended for testing, ensuring the following:
    - The software being tested is included (e.g., source code, executables, libraries).
    - Supporting components (test scripts, simulators, environments) are also under CM.
    - All items have been baselined in preparation for testing, meaning they are documented, approved, and traceable.
    - Configuration history (including any revisions) is properly maintained for all test-related items.
* **Key Artifacts to Review**:

  + **Software configuration management data**:
    - Ensure complete, accurate, and up-to-date documentation of all CM-controlled items.
  + **SA audit results** on the implementation of the CM process:
    - Conduct CM audits to confirm that policies and procedures are effectively applied.
  + **Test Procedures and Plans**:
    - Verify that formal testing documentation aligns with the current software baseline being tested.
  + **Test Reports**:
    - Review previous test reports to identify whether any untested changes or updates remain unresolved.

#### **2. Monitor All Testing Components under Configuration Control**

Beyond the software being tested, confirm that **all supporting components** needed for testing are placed under CM and remain so throughout the testing lifecycle. This ensures test consistency, traceability, and repeatability.

**Items Software Assurance Should Confirm Are Under CM**:

1. **Test Scripts or Testing Software**:

   * Automated test scripts and any software used to drive the test cases must be version-controlled and reviewed as part of the configuration management process.
   * This includes utilities or helper scripts that generate test conditions and inputs.
2. **Support Software**:

   * Components that support the software under test, such as tools that manage data feeds, ground station simulators, or telemetry simulation tools, should also be baselined.
3. **Models, Simulations, and Simulators**:

   * Simulators that replicate mission conditions or hardware models used for validation testing must remain under CM to ensure consistency across multiple test iterations.
   * Updates to these simulation components should receive the same level of scrutiny as the software under test.
4. **Ground Support Software**:

   * Verify that the baseline for ground support software has been effectively placed under CM. This addresses any software that:
     + Interfaces with mission hardware or test platforms.
     + Provides infrastructure for deployment or debugging during tests.
5. **Third-Party or Reused Software Components**:

   * Include all COTS (Commercial Off-The-Shelf), GOTS (Government Off-The-Shelf), MOTS (Modified Off-The-Shelf), OSS (Open Source Software), or reused software items needed for testing.
   * SA should ensure configuration dependencies and licenses for these components are valid and documented.
6. **Operating Systems and Dependencies**:

   * Operating systems or specific system-level drivers used during testing should also be identified under configuration management, particularly when dealing with tests conducted in hardware-in-the-loop (HIL) environments or on embedded platforms.

---

#### **3. Validate CM Control During the Testing Lifecycle**

Once testing begins, Software Assurance must ensure that all software testing components:

* Remain under configuration control throughout the **entire testing lifecycle**.
* Are not modified without proper review and approval via the CM process.

#### Key Activities for Software Assurance During Testing:

1. **Audit Testing Environments**:

   * Verify that the test environments are correctly initialized with only CM-controlled versions of the software and support items. Spot-check environments to ensure only approved versions are present.
   * Identify and flag any unapproved or uncontrolled software modifications introduced into testing environments.
2. **Monitor Change Requests (CR)**:

   * Ensure all changes identified during testing (e.g., through anomaly reports or defects) are processed through configuration control.
   * Confirm that all test-related Change Requests (CRs) are tracked and evaluated for their impact on other components, subsystems, or testing conditions.
3. **Confirm Traceability**:

   * Verify traceability between test results and the items tested under configuration management. This includes linking test cases, outputs, and findings to the specific software version and configuration used during that test.

#### **4. Post-Test Assessment**

* After testing is complete, Software Assurance should verify:
  + **Test Reports**:
    - Evaluate test reports for consistency and accuracy, ensuring they reflect the CM-controlled artifacts and versions used.
  + **Baselined Updates**:
    - Confirm that any fixes, patches, or adjustments to software as a result of testing are baselined and remain under configuration control for further testing or deployment.

---

### **Best Practices for Small and Large Projects**

* For **small projects**, automate baseline tracking and versioning where possible using lightweight CM tools (e.g., Git, Subversion). Ensure even minimal CM procedures are rigorously followed to prevent common issues, like reusing outdated test scripts or uncontrolled bug fixes.
* For **large or complex projects**, SA should frequently engage with the project CM lead or Change Control Board (CCB) to ensure each artifact is aligned with project-wide configuration management policies.

---

### **Additional References**

1. **Topic 8.18 - SA Suggested Metrics**:
   * For metrics on CM compliance, tracking defects, and non-conformance resolution for supporting software.
2. **SWE-081 - Identify Software CM Items**:
   * Guidance on correctly identifying and categorizing software items to be placed under configuration control.
3. **SWE-080 - Track and Evaluate Changes**:
   * Best practices for managing and monitoring change requests during software testing.

---

### **Conclusion**

The role of Software Assurance in the CM process is to ensure that all testing is performed with fully controlled items to guarantee consistency, reproducibility, and traceability. By validating that every software-related artifact—whether it's the test software, support models, or operating systems—is properly baselined and controlled, SA helps to reinforce software quality and minimize risks to project success. This approach ensures a high level of reliability during testing and provides clear traceability for defects, test results, and resolutions throughout the lifecycle.

Configuration Management needs to be maintained even if changes in the software need to be made to complete the test(s).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is the documented proof that a process has been followed correctly, ensuring that software items and related artifacts are under configuration management (CM) prior to testing. This evidence is essential for demonstrating compliance with NASA policies, such as requirement 3.1, and for audits, reviews, and mission assurance processes. Below is a list of possible forms of objective evidence that can be used to verify compliance with this requirement.

---

### **1. Configuration Management Plan (CMP)**

* **Description**: A reviewed and approved Configuration Management Plan that outlines the processes and tools used to identify, control, and track configuration items.
* **Relevance**: Demonstrates that a formalized CM process is in place, tailored to the project's requirements, and that testing will adhere to CM controls.
* **Key Elements**:
  + List of identified configuration items (CIs).
  + Roles and responsibilities for configuration control (e.g., CM lead, Change Control Board [CCB]).
  + Procedures for baseline creation, change control, and version management.

---

### **2. List of Configuration Items (CIs)**

* **Description**: A detailed inventory of all configuration items, including those needed for testing.
* **Relevance**: Confirms that the software and all testing-related components are explicitly identified and accounted for under configuration management.
* **Key Elements**:
  + Software under test (e.g., source code, binaries, libraries).
  + Test scripts, test plans, test results, and related documentation.
  + Supporting tools, simulations, models, datasets, and environments.
  + Third-party or reused components (e.g., COTS, GOTS, MOTS, OSS).

---

### **3. Baseline Approvals**

* **Description**: Documentation showing that baselines for the software and supporting artifacts have been formally approved and placed under CM prior to testing.
* **Relevance**: Demonstrates that specific versions of all configuration items have been locked in preparation for testing, preventing unauthorized changes.
* **Key Elements**:
  + Approval signatures or electronic approvals from the project manager, software assurance lead, or other stakeholders.
  + Version information for the baseline, clearly linking to specific builds or artifacts.

---

### **4. Version Control Reports**

* **Description**: Reports from version control systems (e.g., Git, Subversion, or equivalent) showing the history, tags, and status of configuration-managed items.
* **Relevance**: Demonstrates that all software and test-related artifacts are version-controlled and properly tracked.
* **Key Elements**:
  + Commit history with descriptive messages.
  + Tagged versions representing baselines (e.g., "v1.0\_TestBuild").
  + Evidence of branch management (e.g., separate testing, development, and release branches).

---

### **5. Configuration Audit Reports**

* **Description**: Results of audits performed by Software Assurance or CM personnel to verify that all necessary items are under CM before testing begins.
* **Relevance**: Proves that the scope of CM is complete and adheres to the approved CMP.
* **Key Elements**:
  + Audit findings (e.g., conformance to CMP, missing or improperly controlled items).
  + Proof of corrective actions for identified issues, if any.
  + Certification that the configuration items are ready for testing.

---

### **6. Test Readiness Review (TRR) Artifacts**

* **Description**: Documentation from the Test Readiness Review process that highlights the status of CM for the software and related test artifacts.
* **Relevance**: Verifies that all test-related items are formally approved, controlled, and baselined prior to testing.
* **Key Elements**:
  + TRR checklist confirming CM adherence.
  + Approvals indicating that test artifacts are ready and controlled.
  + Verification that no unauthorized changes are pending in the test baseline.

---

### **7. Change Request (CR) and Problem Report (PR) Logs**

* **Description**: Logs that track all Change Requests and Problem Reports, ensuring changes to software under test and related items are managed within the CM process.
* **Relevance**: Demonstrates that any changes to software or artifacts impacting testing are formally reviewed, approved, and tracked.
* **Key Elements**:
  + Detailed descriptions of requested or approved changes.
  + Links between CRs/PRs and versions of software or artifacts under test.
  + Status of each CR/PR (e.g., "proposed," "approved," "closed").

---

### **8. Software Product Baseline (SPB)**

* **Description**: A final, baselined version of the software and all associated documentation for testing purposes.
* **Relevance**: Demonstrates that all aspects of the software product and test artifacts are baselined and immutable for the duration of testing.
* **Key Elements**:
  + References to source code versions, compiled binaries, and libraries.
  + Linkage to testing documentation (e.g., test procedures and scripts).
  + Approvals for baselined items (e.g., sign-off from the technical lead or assurance personnel).

---

### **9. Test Procedures and Plans**

* **Description**: Detailed test plans and procedures that identify and reference the CM-controlled software and artifacts used during testing.
* **Relevance**: Provides assurance that testing activities are conducted on consistent, controlled items.
* **Key Elements**:
  + References to specific software versions under test.
  + Links to baselined testing components (e.g., simulators, test scripts).
  + Alignment with test objectives and requirements.

---

### **10. Software Assurance Reviews**

* **Description**: Results of Software Assurance reviews confirming CM compliance for all test-related items.
* **Relevance**: Serves as third-party verification that the configuration management process was followed and all items under test are controlled.
* **Key Elements**:
  + Reports on the completeness and correctness of CM activities.
  + Validations of test baseline integrity.
  + Sign-offs indicating SA's approval to proceed with testing.

---

### **11. Observations from Independent Verification & Validation (IV&V)**

* **Description**: Findings from an Independent Verification and Validation (IV&V) activity assessing adherence to CM requirements during testing preparation.
* **Relevance**: Provides independent evidence that CM controls are implemented and effective, particularly for safety-critical or mission-critical software.
* **Key Elements**:
  + Validation results of configuration items.
  + IV&V reports or recommendations accepted and addressed by the project team.

---

### **12. Tools and Configuration Reports**

* **Description**: Reports from CM tools used to track configuration items.
* **Relevance**: Demonstrates the automated enforcement of CM policies and provides snapshots of artifact statuses at key points in the lifecycle.
* **Key Elements**:
  + Listings of objects under CM (e.g., test files, libraries, datasets).
  + Reports detailing change histories, current baselines, and approved configurations.

---

### **Submission of Evidence for Compliance**

For compliance with NASA’s **Require­ment 3.1**, the appropriate objective evidence may be submitted as part of:

1. **Software Configuration Reviews**.
2. **Test Readiness Reviews (TRRs)**.
3. **Audits and Assessments conducted by Software Assurance or IV&V teams**.
4. **Mission-specific assurance documentation repositories**.

By systematically gathering and submitting the above evidence, the project team ensures traceability, accountability, and compliance with configuration management practices. These records not only fulfill requirements but build stakeholder confidence that the software being tested is of the highest quality and controls are in place to mitigate risks.

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
