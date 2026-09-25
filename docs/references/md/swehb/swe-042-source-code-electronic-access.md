# SWE-042 - Source Code Electronic Access

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695418. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access

SWE-042 - Source Code Electronic Access

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695418)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695418&showCommentArea=true&showComments=true#addcomment)

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

3.1.10 The project manager shall require the software developer(s) to provide NASA with electronic access to the source code developed for the project in a modifiable format.

## 1.1 Notes

The electronic access requirements for the source code, software products, and software process tracking information implies that NASA gets electronic copies of the items for use by NASA at NASA facilities. This requirement should include MOTS software, ground test software, simulations, ground analysis software, ground control software, science data processing software, hardware manufacturing software, and Class E and Class F software.

## 1.2 History

Click here to view the history of this requirement: SWE-042 History

SWE-042 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.6.1.4 The project shall require the software supplier(s) to provide NASA with electronic access to the source code developed for the project, including MOTS (Modified Off the Shelf) software and non-flight software (e.g., ground test software, simulations, ground analysis software, ground control software, science data processing software, and hardware manufacturing software). |
| Difference between A and B | Clarified the source code needs to be in modifiable format; otherwise, NC. |
| B | 3.12.10 The project manager shall require the software supplier(s) to provide NASA with electronic access to the source code developed for the project in a modifiable format, including modified off the shelf (MOTS) software and non-flight software (e.g., ground test software, simulations, ground analysis software, ground control software, science data processing software, and hardware manufacturing software). |
| Difference between B and C | Removed references to MOTS and non-flight software and associated examples. |
| C | 3.1.10 The project manager shall require the software developer(s) to provide NASA with electronic access to the source code developed for the project in a modifiable format. |
| Difference between C and D | No change |
| D | 3.1.10 The project manager shall require the software developer(s) to provide NASA with electronic access to the source code developed for the project in a modifiable format. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

NASA requires electronic access to software source code developed by suppliers with NASA funding to enable independent evaluations, checks, reviews, and testing.  Source code is also needed to be able to run static code analysis on the product to check for software errors, security issues, and coding standard compliance.

The electronic availability of the software work products, and associated process information, facilitates post-delivery testing that is necessary for assessing as-built work product quality, and for the porting of products to the appropriate hosts. This access also accommodates the longer-term needs for performing maintenance, assessing operation or system errors, addressing hardware and software workarounds, and allowing for the potential reuse of the software on future NASA projects.

The intent of this requirement is to ensure that NASA has unfettered electronic access to the **modifiable source code** for all software developed for its missions or projects. This is essential to safeguard NASA's ability to perform maintenance, debugging, updates, modifications, and upgrades both during the active development lifecycle and after project completion. The requirement reflects NASA's need for continuity, adaptability, and control over software assets used for mission-critical purposes.

Source code access applies not only to traditional mission software but also to **off-mission software categories**, including hardware manufacturing software, ground control systems, simulations, science data processing, and Class E/F software (as outlined in NASA procedural standards). Below, the rationale for requiring this access is discussed in detail.

Requiring electronic access to source code in modifiable format ensures that NASA retains control over mission-critical software throughout the development, operational, and post-contract phases. This access empowers NASA to manage software maintenance, debugging, and updates independently, reduce dependency on suppliers, protect intellectual assets, support validation processes, and maintain alignment with mission goals. By including this requirement in project contracts, NASA guarantees the flexibility and adaptability necessary to meet both current and future mission challenges efficiently and effectively.

## 2.1 Key Benefits of the Requirement

### 2.1.1 Ensures Long-Term Maintainability

* Providing NASA electronic access to source code in a **modifiable format** allows NASA to independently maintain, update, and modify the code after the contract ends or the supplier disengages from the project.
* This includes fixing bugs, improving performance, adapting the code for future missions, and addressing operational changes.
* For long-term projects, access reduces dependency on external contractors for future modifications.

#### Example:

For legacy systems or multi-mission reuse scenarios, NASA can directly access and modify source code to meet the evolving demands of future missions without needing to renegotiate contracts with the original developers.

### 2.1.2 Facilitates Debugging and Issue Resolution

* Electronic access to modifiable source code enables NASA to investigate and resolve issues that may arise during:
  + Software testing.
  + Integration with hardware systems.
  + Deployment in operational environments.
* Without access, even small issues could cause delays or require external involvement for resolution, increasing the cost and timeline of fixes.

#### Example:

During ground testing or modeling simulations, unexpected integration errors between hardware and software may require immediate fixes to continue testing. Direct access to modifiable source code ensures NASA engineers can perform rapid diagnosis and resolution.

### 2.1.3 Supports Independent Validation and Verification (IV&V)

* Source code access is vital to NASA’s **IV&V** processes:
  + NASA software assurance teams analyze the modifiable code to verify compliance with requirements, identify defects, perform static analyses, and ensure software safety.
  + Without access, NASA would be dependent on the supplier to perform these critical validations, which could compromise transparency and independence.

#### Example:

For safety-critical code controlling mission operations, NASA IV&V teams can perform in-depth reviews to confirm reliability, ensure hazard-free operations, and verify adherence to standards.

### 2.1.4 Guarantees Transparency and Accountability

* Mandating electronic access in a **modifiable format** ensures supplier accountability:
  + NASA can verify that the delivered code meets contracted specifications, requirements, and performance criteria.
  + Transparency avoids potential conflicts, ambiguity, or gaps in understanding the system implementation.
* It also ensures that all significant developments are accessible for review by NASA's oversight and assurance teams.

#### Example:

Contracted developers working on science data processing software are required to maintain alignment with NASA’s performance requirements. By assessing the source code, NASA can ensure developers meet those goals and maintain consistency across the project's lifecycle.

### 2.1.5 Protects NASA’s Intellectual Assets

* By retaining electronic access to the source code created for its projects, NASA preserves its intellectual property (IP). This includes tools, methods, and software solutions developed for mission purposes.
* This protection is particularly important for:
  + Mixed off-the-shelf solutions (MOTS software).
  + Ground systems software.
  + Custom scientific analysis tools.
* Having direct access ensures future reuse, adaptation, and extension of IP without contractual or licensing roadblocks.

### 2.1.6 Reduces Vendor Lock-In

* Access to source code in modifiable format eliminates dependency on one supplier for ongoing maintenance or future modifications.
* This ensures NASA can:
  + Shift development responsibilities internally or to new contractors if necessary.
  + Transition software to multi-mission teams or centers without requiring additional costly licensing or modification permissions.

#### Example:

Ground control software for telemetry monitoring can be adapted for a new mission using strategy shifts from internal NASA resources, avoiding costs and delays tied to re-engaging original developers.

### 2.1.7 Improves Collaboration and Integration

* Electronic access allows NASA developers to collaborate seamlessly with contractors and teams working on other aspects of the project.
* Access ensures smoother integration between software components, subsystems, and hardware, especially during testing and mission-critical operations.

## 2.2 Applicability Notes

To clarify the scope of this requirement, NASA’s electronic access needs are comprehensive and apply to various types of software development efforts, including:

### 2.2.1 MOTS Software (Modified Off-the-Shelf Software)

* When a supplier modifies pre-existing off-the-shelf software for mission-specific use, NASA must have access to the modifiable source code for the modifications (even if the supplier retains rights to the underlying COTS package). This ensures that NASA can maintain or modify the mission-specific portions of the software.

### 2.2.2 Ground Test Software

* Software used in a testing environment to validate system performance must be accessible for adjustments as needed during testing phases.

### 2.2.3 Simulations

* Software used for system modeling or environment simulation must be modifiable to accommodate changing project requirements or address unforeseen testing challenges.

### 2.2.4 Ground Control and Analysis Software

* Mission ground systems (e.g., telemetry monitoring, command control) rely on highly dynamic and modifiable software. Access is critical to enable NASA teams to make adjustments during mission operations.

### 2.2.5 Hardware Manufacturing Software

* Software controlling manufacturing processes for mission hardware (e.g., robotic components) must be accessible to ensure operational accuracy and adaptability for quality assurance.

### 2.2.6 Class E and Class F Software

* For smaller, less safety-critical projects (Classes E and F), NASA may not need full oversight, but electronic access is vital for NASA to assess and reuse components effectively.

## 2.3 Definition of Modifiable Format:

* "Electronic access in modifiable format" means providing the **source code** in a form suitable for editing and modification by NASA personnel using commonly available tools and development environments (e.g., clean and editable .c, .cpp, .java files, scripts, etc., without obfuscation or compilation-only restrictions).
* Encapsulated or cryptic formats designed to obscure code functionality are not compliant under this requirement.

## 2.4 Relationship to Other Requirements

* This requirement dovetails with several related NASA mandates, particularly:
  + [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) -  Governs general electronic access to supplier work products and tools.
  + [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) -  Addresses licensing and reuse of COTS, legacy, and proprietary software elements integrated into deliverables.

# 3. Guidance

This guidance directs NASA project managers and teams on implementing the requirement to provide **electronic access to software source code** developed using NASA funding. Access enables independent evaluations, reviews, and testing, facilitates long-term software maintenance, mitigates operational challenges, and supports future reuse. The guidance includes best practices for planning, managing contractual obligations, addressing contractor concerns, and promoting compliance with intellectual property and federal acquisition regulations.

### Key Elements of Electronic Access Requirement - Purpose and Benefits

* **Independent Evaluation:** NASA must have unrestricted access to modifiable source code to independently review, analyze, and validate the software through its own tools and procedures.
* **Maintenance and Debugging:** Access ensures NASA can promptly address operational issues, conduct hardware/software workarounds, resolve errors, and perform upgrades without vendor reliance.
* **Future Reuse:** Enables NASA to leverage developed software for follow-on projects or new missions, enhancing cost-effectiveness and agility.
* **Transparency and Oversight:** Provides NASA necessary insight into vendor progress and compliance with requirements, ensuring proper execution of the government's oversight responsibilities (as per [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight)).

This requirement is crucial for enabling NASA to effectively manage, assess, and maintain software developed with NASA funding. By planning upfront, defining access clearly in contracts, addressing vendor concerns, and ensuring compliance with FAR and intellectual property standards, NASA can retain control over its software assets for current and future missions. Access to modifiable electronic source code ensures operational independence, long-term maintainability, and cost-efficient reuse—all foundational to NASA’s success.

See also [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs),

## 3.1 Planning for Access

### 3.1.1 Front-End Contract Planning

Electronic access requirements must be **explicitly defined** during contract negotiations to avoid ambiguity or disputes later. This includes:

* **Statement of Work (SOW):** Specify access requirements, formats, schedules, and scope in the SOW or task agreements.
* **Subcontractor Clauses:** Ensure subcontractors are subject to the same electronic access provisions as prime contractors to maintain visibility across the entire development team.
* **Documentation:** Include provisions for modifiable source code, build tools, configuration data, software telemetry, and related documentation, aligned with [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) and [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products).

### 3.1.2 Electronic Access Definition

Electronic access should allow unrestricted remote access without requiring physical presence at vendor sites. Common access methods include:

* **Secure FTP or Remote Web Access:** Secure remote access from NASA Centers or approved sites provides real-time or periodic visibility into development artifacts.
* **Magnetic Media (Last Resort):** In cases where remote access is not feasible due to IT policy conflicts (e.g., firewalls), contractors may deliver code via USB drives, external disks, or other portable devices.

### 3.1.3 Security Considerations

NASA and contractors must maintain robust security measures to protect sensitive software artifacts and proprietary information. Both parties must agree on security protocols, access roles, and restrictions.

## 3.2 Access to All Code Data

NASA requires comprehensive access to all software deliverables to ensure oversight, debugging capabilities, and operational efficiency. The project team must gain electronic access to:

1. **Source Code:**  
   Includes modifiable code for flight software, ground control software, science data processing software, simulations, and related systems.
2. **Executable Code:**  
   Essential for static analysis, independent assessments, and validation against system requirements.
3. **Supplementary Data:**

   * Configuration files.
   * Data loads.
   * Programmable logic artifacts.
   * Telemetry software.
   * Embedded MOTS (modified off-the-shelf) and legacy components.

### 3.2.1 Support Long-Term Maintenance

Electronic access ensures operational continuity even after vendor disengagement. NASA must retain modifiable versions of source code and supporting documentation for:

* **In-house maintenance:** Allow NASA teams to perform routine updates and fixes as systems evolve.
* **Vendor transitions:** Enable third-party vendors to seamlessly pick up maintenance responsibilities when needed.

### 3.2.2 Future Reuse

Access supports efficient adaptation of previously developed software for future missions or follow-on projects:

* Reduces development costs by leveraging existing products.
* Promotes knowledge transfer and system compatibility across missions.

## 3.3 Addressing Contractor Concerns

### 3.3.1 Managing Resistance

Contractors may resist electronic access due to concerns over intellectual property (IP) or proprietary code reuse. Resistance can be mitigated by:

* **Clear Contract Language:** Address intellectual property rights, licensing, and copyright protections explicitly in the SOW to avoid misunderstandings.
* **Use Restrictions:** Implement security features to ensure proprietary software elements (non-NASA funded components) are protected from unauthorized reuse or distribution. For mixed funding development (vendor-funded and NASA-funded), spell out access rights for NASA-funded portions only.

### 3.3.2 Intellectual Property Considerations

The SOW must outline access rights that accommodate proprietary and mixed-source development:

* **NASA-Funded Code:** Clearly designate rights in the NASA-funded source code to ensure unrestricted government access and usage.
* **Licensing:** Include rights to modify, distribute, or integrate the software into other systems or missions, as appropriate.
* **Consult Chief Counsel:** Engage the Center’s Chief of Patent/Intellectual Property Counsel to define rights and address copyright assignments when required.

## 3.4 Contract Deliverables and Data Rights

### 3.4.1 SWE-077 and Ensuring Comprehensive Deliverables

The SOW must specify the timeline, format, and nature of electronic access for all deliverables:

* **By Build Releases:** Include clauses for access during incremental build releases, not just the final delivery.
* **Scope of Software:** Cover all software types, including flight software, ground systems software, MOTS applications, embedded telemetry, and simulations.

See [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products),

### 3.4.2 Federal Acquisition Requirements

All NASA projects must comply with **FAR 52.227-14 Rights in Data—General** [186](#_tabs-<p></p>) regarding data rights, licensing, and usage restrictions. Ensure FAR requirements are integrated into acquisitions contracts to preserve government rights over developed software.

## 3.5 Recommended Best Practices for Implementation

### 3.5.1 Early Collaboration and Communication

Engage suppliers and subcontractors early to negotiate access requirements and avoid resistance. Ensure both sides understand the shared benefits of electronic access for project success.

### 3.5.2 Security Protocols

Define robust security mechanisms for accessing source code repositories or databases remotely. Use NASA-approved platforms that comply with IT regulations and firewall restrictions.

### 3.5.3 Dispute Mitigation

Include clear clauses in the SOW regarding intellectual property ownership and data rights to avoid disputes during or after the contract period.

### 3.5.4 Traceability

Enable bi-directional traceability for software deliverables and updates to track progress and ensure alignment with requirements throughout the development lifecycle.

### 3.5.5 Long-Term Planning

Consider future project needs, transitions, and reuse potential when drafting access clauses. Focus on maintaining modifiable versions of source code and comprehensive documentation.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting) |

# 4. Small Projects

For small projects, the requirement to provide NASA with electronic access to software source code in a **modifiable format** is still essential but should be tailored to the project's smaller scope, reduced complexity, lower budget, and resource constraints. This guidance provides practical recommendations to implement the requirement effectively without imposing unnecessary overhead or complexity on small NASA projects.

Small projects benefit from tailored electronic access requirements that emphasize simplicity and proportionality while maintaining compliance with NASA’s need for transparency, oversight, and future reuse. By focusing on essential deliverables, minimizing access complexity, and incorporating efficient methods, project teams can implement this requirement effectively without excessive resource investment.

## 4.1 Principles for Applying the Requirement in Small Projects

1. **Proportional Scope:**

   * Tailor deliverables and access mechanisms to match the size and risk of the project. Focus on high-priority items rather than exhaustive access to all artifacts.
2. **Minimized Overhead:**

   * Avoid complex or costly access methods that could strain resources. Opt for simple, scalable solutions suited to small teams and budgets.
3. **Mission-Focused Approach:**

   * Prioritize source code and artifacts directly tied to mission-critical functionality or safety-critical components.
4. **Reusability:**

   * Plan for future reuse by ensuring clear access to all deliverable code and related documentation aligned with minimal project needs.

## 4.2 Key Steps for Implementing Electronic Access in Small Projects

### 4.2.1. Define Essential Deliverables

For small projects, prioritize the **minimum set of items** necessary for NASA's oversight, testing, and reuse purposes. Examples of essential deliverables include:

* Modifiable **source code** (core functionality or mission-critical features).
* Configuration files or dependencies directly required for operation (e.g., data loads, telemetry software).
* Test results for critical components (e.g., safety-critical units or integration results).
* Basic documentation sufficient for operating and maintaining the software, such as:
  + [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual)
  + [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document)

### 4.2.2. Choose Simplified Access Methods

* **Direct Repository Access:**

  + Use widely available repositories (e.g., GitHub, Bitbucket, cloud-based platforms like SharePoint) for hosting source code and associated documentation. Limit access to core deliverables based on project needs.
  + Benefits: Low setup cost and easy access for both NASA and developers.
* **Periodic File Transfers (Magnetic Media):**

  + For very small projects, deliverables can be loaded onto portable drives (e.g., USB thumb drives) or shared via secure file transfer protocols.
  + Best suited for projects with low access frequency during development (e.g., periodic milestone reviews).

### 4.2.3. Minimize Access Complexity

Work with contractors upfront to streamline access:

* Negotiate a **reduced number of required updates** or builds for review (e.g., at milestone completions only).
* Ensure manageable security protocols (e.g., password-protected file access or role-based repository permissions) without overcomplicating implementation.

### 4.2.4. Focus on Risk-Based Oversight

For small projects, allocate oversight based on the **risk level** of the project components:

* **Low Risk:**

  + Focus access on key milestone deliverables and final source code without requiring continuous oversight.
* **High Risk or Safety-Critical Software:**

  + Require detailed access for validation and verification of critical components. Include source code reviews, testing results, and configuration tracking more frequently.

## 4.3 Examples of Implementing Electronic Access in Small Projects

#### **Example 1: Internal Administrative Tool**

A small project is developing non-critical software for internal NASA workflows:

* **Deliverables:**
  + Source code for the main tool functionality.
  + Basic user guide and testing documentation.
  + Results of integration testing (if applicable).
* **Access Approach:**
  + Provide electronic copies of files via secure email delivery or shared cloud folders at milestone completions.
  + Minimal updates or static analysis unless deemed necessary.

#### **Example 2: Safety-Critical Test Environment**

A project developing software for simulation of spacecraft operations in the lab:

* **Deliverables:**
  + Source code for core simulation logic.
  + Configuration files for interfacing with hardware.
  + Test results for units with safety-critical implications.
* **Access Approach:**
  + Provide real-time remote access to the source repository for testing feedback and early issue resolution.
  + Include provisions for code inspection during test milestones.

## 4.4.Contractual Considerations for Small Projects

### 4.4.1 Simplified Contract Language

Small projects should include compact language in the **Statement of Work (SOW)** that specifies:

* Access schedule tied to milestone deliverables (e.g., draft versions, integration builds, final delivery).
* Scope limited to required code and artifacts directly relevant to mission/non-mission needs.
* Data rights requirements per **FAR clause 52.227-14** [186](#_tabs-<p></p>) with alignment to NASA’s reuse standards.

### 4.4.2 Address Intellectual Property Concerns

For contractors concerned about protecting proprietary code:

* Clearly delineate vendor-owned code from NASA-funded deliverables.
* Ensure source code access is restricted to NASA-funded components only.
* Include specific clauses for licensing or reuse rights if mixed source development is involved.

## 4.5 Recommended Best Practices

1. **Keep Deliverables Focused:**

   * Avoid requiring access to unnecessary artifacts. Focus on core requirements (source code, basic documentation, and test data) for reduced complexity.
2. **Integrate Efficiency:**

   * Use existing tools or repositories with minimal overhead to ensure NASA teams can access deliverables without extensive resource investment.
3. **Engage Stakeholders Early:**

   * Communicate access expectations early with developers and subcontractors to address concerns proactively and align on deliverable schedules.
4. **Adjust Oversight Frequency:**

   * Small projects may require fewer oversight reviews. Opt for milestone-based access instead of continuous updates.
5. **Security Alignment:**

   * Work within NASA’s IT policies and firewall restrictions while respecting contractor security protocols.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-186)

  [FAR 52.227-14 Rights in Data---General.](https://www.acquisition.gov/far/52.227-14 "Click to open in new window")

  Federal Acquisition Requirements (FAR) clause 52.227-14
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-541)

  [Computer Hardware-Software/International Space Station/Software Configuration Management](https://llis.nasa.gov/lesson/1130 "Click to open in new window")

  Public Lessons Learned Entry: 1130.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

A documented lesson from the NASA Lessons Learned database notes the following:

* **Computer Hardware-Software/International Space Station/Software Configuration Management. Lesson No: 1130**[541](#_tabs-<p></p>): Although it was "grandfathered" out of NPR 7150.2 compliance, the experience regarding source code for the International Space Station (ISS) is an important caveat when establishing software supplier agreements. NASA does not have source code access for all partners' deliveries for the ISS. The partners cite their concerns that the delivery of source code could compromise their contractors' proprietary data. The ISS has initiated discussions with all partners to reach an agreement on what level of source code visibility is necessary to ensure adequate knowledge by the control centers for on-orbit anomaly resolution. It is not clear how much extra effort these discussions have taken.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Benefits of receiving GN&C algorithm in HiFi code](https://software.gsfc.nasa.gov/lesson-details/72/). **Lesson Number 72**: The recommendation states: "Receiving GN&C algorithm in HiFi code facilitates configuration management and updates to FSW based on algorithm changes."

# 7. Software Assurance

**SWE-042 - Source Code Electronic Access**

3.1.10 The project manager shall require the software developer(s) to provide NASA with electronic access to the source code developed for the project in a modifiable format.

This requirement ensures that NASA receives electronic access to source code and associated artifacts in modifiable formats, enabling independent analysis, maintenance, troubleshooting, and reuse. Software Assurance (SA) personnel must develop products and verify objective evidence to demonstrate compliance with this requirement while identifying risks related to access, delivery, and intellectual property considerations.

The guidance ensures:

* NASA can independently verify, validate, and analyze the software products.
* Software is available for defect identification, corrections, and reuse.
* Compliance with intellectual property rights while ensuring full transparency and accessibility.
* Project costs are reduced through streamlined analysis processes and long-term access facilitation.

By following this enhanced guidance, SA personnel can ensure compliance with this requirement, verify electronic access, and support project goals effectively.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that software developers provide NASA with electronic access to the source code generated for the project in a modifiable form.

## 7.2 Software Assurance Products

SA personnel are responsible for creating deliverables that document compliance, assess risks, and verify NASA has full access to software source code in appropriate formats. Below is an outline of the SA products required to meet this requirement.

### 7.2.1 Source Code Access Verification Report

**Purpose**: Documents the SA team's verification of electronic access to source code files, ensuring they are provided in modifiable formats and meet project requirements.

**Contents**:

* List of source code deliverables provided by the developer.
* Confirmation of electronic formats (e.g., plain-text files, version-controlled repositories).
* Verification of access credentials for build systems, version control systems (e.g., Git, SVN), and online repositories.
* Assessment of modifiability (editable and compatible formats).

### 7.2.2 Compliance Checklist for Source Code Deliverables

**Purpose**: Tracks and verifies compliance with required deliverables, including source code and related artifacts.

**Contents**:

1. Checklist of required deliverables, including:
   * Flight and ground software source code.
   * Prototype software and architectures.
   * Data definitions and data sets.
   * Programmable logic device code (e.g., FPGA firmware).
   * Software build products (e.g., configuration files, scripts, dependencies).
   * Software test scripts.
   * Software database(s).
2. Status columns indicating whether:
   * Deliverables were provided.
   * Access credentials were verified.
   * Formats are modifiable and usable.
3. Notes on missing, incomplete, or restricted deliverables.

### 7.2.3 Static Analysis Report

**Purpose**: Provides detailed results of NASA's independent static code analysis, verifying the quality of delivered source code.

**Contents**:

* Summary of static analysis tools used (e.g., CodeSonar, Coverity, Polyspace).
* List of identified defects, coding standard violations, security vulnerabilities, and quality concerns.
* Recommendations for corrective actions.
* Trend analysis comparing delivered source code quality (e.g., defect rate, coding compliance level).

### 7.2.4 Configuration and Version Control Access Report

**Purpose**: Verifies the developer has provided NASA electronic access to version control systems and build configurations.

**Contents**:

* List of version control systems (e.g., Git repositories, Subversion) with access details.
* Inventory of branches, tags, and baselines available to NASA.
* Verification of build system compatibility and the ability to replicate builds from provided artifacts.
* Assessment of configuration management compliance with NASA's guidelines.

### 7.2.5 Intellectual Property and Proprietary Rights Compliance Report

**Purpose**: Ensures that intellectual property or proprietary rights limitations do not impede NASA's ability to access, modify, and maintain the source code.

**Contents**:

* Review of contracts, intellectual property agreements, or licenses to confirm delivery and use of source code aligns with project requirements.
* Documentation verifying developers complied with proprietary restrictions while providing modifiable source code to NASA.
* Recommendations for resolving conflicts or limitations.

### 7.2.6 Post-Delivery Review and Risk Assessment Report

**Purpose**: Documents the SA team's assessment of software deliverables after delivery, ensuring long-term accessibility and identifying potential risks or gaps.

**Contents**:

* Verification of long-term accessibility (e.g., credentials still active, formats usable for future testing and maintenance).
* Assessment of risks related to missing products, restricted access, format compatibility, or lack of documentation.
* Recommendations for risk mitigation and follow-up actions with the developers.

## 7.3 Metrics

The purpose of the metrics for this requirement is to ensure that NASA has proper electronic access to project-related source code and associated artifacts in a format suitable for modification, with a special focus on accessibility, completeness, correctness, compatibility, and long-term access. These metrics assess compliance, track progress, and identify gaps in the provision and management of source code and related software artifacts.

### **Key Metrics Categories**

1. **Accessibility and Completeness Metrics**
2. **Source Code Quality and Format Metrics**
3. **Source Code Deliverability and Timeliness Metrics**
4. **Verification and Validation Metrics**
5. **Long-Term Access and Maintenance Metrics**

### **7.3.1** Accessibility **and Completeness Metrics**

These metrics measure the completeness and accessibility of source code deliverables and associated software artifacts provided to NASA.

#### 7.3.1.1 Source Code Accessibility Compliance

* **Definition**: The percentage of source code deliverables provided by the software developer that include correct access credentials and are electronically accessible to NASA personnel.
* **Formula**:  
  [ \text{Accessibility Compliance} = \left( \frac{\text{Accessible Source Code Deliverables}}{\text{Total Required Source Code Deliverables}} \right) \times 100 ]
* **Purpose**: Ensures source code provided to NASA is electronically accessible without restrictions (e.g., access credentials, links to repositories, or electronic formats worked as expected).
* **Target**: ≥ 95%.

#### 7.3.1.2 Artifact Completeness Rate

* **Definition**: The percentage of required source code and software artifacts delivered (e.g., source code, test scripts, data definitions, build scripts, software databases).
* **Formula**:  
  [ \text{Artifact Completeness Rate} = \left( \frac{\text{Artifacts Delivered}}{\text{Artifacts Required}} \right) \times 100 ]
* **Purpose**: Verifies that all required software-related artifacts are included with the source code deliverables.
* **Target**: 100%.

#### 7.3.1.3 Correctness of Delivered Source Code

* **Definition**: Measures the percentage of delivered source code that satisfies project requirements in terms of modifiability, electronic access, and completeness.
* **Formula**:  
  [ \text{Correctness Rate} = \left( \frac{\text{Correct Source Code Deliverables}}{\text{Total Source Code Deliverables}} \right) \times 100 ]
* **Purpose**: Evaluates whether the delivered source code meets specified quality and modifiability requirements.
* **Target**: ≥ 90%.

#### 7.3.1.4 Unrestricted Access Compliance

* **Definition**: Percent of delivered source code for which intellectual property (IP) or proprietary rights do not limit NASA’s ability to modify or maintain.
* **Formula**:  
  [ \text{Unrestricted Access Compliance} = \left( \frac{\text{Source Code Deliverables Without Restrictions}}{\text{Total Source Code Deliverables}} \right) \times 100 ]
* **Purpose**: Ensures the source code is provided to NASA in compliance with intellectual property or proprietary rights agreements.
* **Target**: ≥ 95%.

### 7.3.2 Source Code Quality and Format Metrics

These metrics evaluate the quality, format correctness, and compatibility of the delivered source code.

#### 7.3.2.1 Modifiability Rate

* **Definition**: Measures the percentage of delivered source code files that are provided in a modifiable, editable format.
* **Formula**:  
  [ \text{Modifiability Rate} = \left( \frac{\text{Source Code in Modifiable Format}}{\text{Total Source Code Files Delivered}} \right) \times 100 ]
* **Purpose**: Ensures the source code is delivered in a format that NASA can modify for updates, maintenance, or analysis.
* **Target**: 100%.

#### 7.3.2.2 Static Analysis Compatibility Rate

* **Definition**: The percentage of delivered source code files that are compatible with NASA’s preferred static analysis tools (e.g., CodeSonar, Coverity, Polyspace).
* **Formula**:  
  [ \text{Static Analysis Compatibility Rate} = \left( \frac{\text{Compatible Source Code Files}}{\text{Total Delivered Files}} \right) \times 100 ]
* **Purpose**: Ensures the delivered source code can be analyzed using NASA’s tools for identifying software errors, vulnerabilities, and coding standard violations.
* **Target**: ≥ 95%.

#### 7.3.2.3 Coding Standard Compliance Rate

* **Definition**: The percentage of source code files that comply with defined coding standards (e.g., MISRA, NASA-specific standards).
* **Formula**:  
  [ \text{Coding Standard Compliance Rate} = \left( \frac{\text{Files Passing Coding Checks}}{\text{Total Files Reviewed}} \right) \times 100 ]
* **Purpose**: Verifies adherence to coding standards to ensure consistency, reliability, and maintainability of source code.
* **Target**: ≥ 90%.

### 7.3.3 Source Code Deliverability and Timeliness Metrics

#### 7.3.3.1 Timeliness of Source Code Delivery

* **Definition**: The percentage of source code deliverables received on or before the agreed-upon delivery deadlines.
* **Formula**:  
  [ \text{Timeliness Rate} = \left( \frac{\text{Deliverables On Time}}{\text{Total Deliverables Due}} \right) \times 100 ]
* **Purpose**: Ensures the developer adheres to the project timeline for source code submissions.
* **Target**: ≥ 90%.

#### 7.3.3.2 Deficient Deliverables Rate

* **Definition**: The percentage of source code deliverables that are rejected due to missing, incomplete, or incorrect content.
* **Formula**:  
  [ \text{Deficient Deliverables Rate} = \left( \frac{\text{Rejections Due to Deficiencies}}{\text{Total Deliverables Reviewed}} \right) \times 100 ]
* **Purpose**: Tracks the frequency of rejected deliverables to identify delivery issues or bottlenecks.
* **Target**: ≤ 5%.

### 7.3.4 Verification and Validation Metrics

These metrics confirm that NASA’s V&V processes facilitate the independent analysis and quality assessment of the delivered source code.

#### 7.3.4.1 Static Analysis Defect Rate

* **Definition**: The number of defects or issues identified by static analysis tools per 1,000 lines of code (KLOC).
* **Formula**:  
  [ \text{Defect Rate} = \frac{\text{Total Number of Static Analysis Issues}}{\text{Total KLOC}} ]
* **Purpose**: Evaluates code quality based on defects identified through independent static analysis.
* **Target**: Defined as project-specific limits or thresholds.

#### 7.3.4.2 Post-Delivery Non-Conformance Identification Rate

* **Definition**: The number of non-conformances identified during post-delivery testing as a percentage of total delivered source code.
* **Formula**:  
  [ \text{Post-Delivery Non-Conformance Rate} = \left( \frac{\text{Post-Delivery Non-Conformances Identified}}{\text{Total Delivered Files}} \right) \times 100 ]
* **Purpose**: Tracks the quality of delivered source code by identifying issues detected after delivery.
* **Target**: ≤ 5%.

### 7.3.5 Long-Term Access and Maintenance Metrics

#### 7.3.5.1 Long-Term Access Fulfillment Rate

* **Definition**: The percentage of source code and associated artifacts verified to be accessible for maintenance or future reuse without compatibility or access issues.
* **Formula**:  
  [ \text{Long-Term Access Fulfillment Rate} = \left( \frac{\text{Artifacts Accessible Post-Delivery}}{\text{Artifacts Required for Long-Term Use}} \right) \times 100 ]
* **Purpose**: Ensures the delivered source code and artifacts remain accessible and usable over time.
* **Target**: 100%.

### **Summary of SA Metrics for Requirement**

| **Category** | **Example Metrics** |
| --- | --- |
| **Accessibility and Completeness** | Source Code Accessibility Compliance, Artifact Completeness Rate, Correctness Rate. |
| **Source Code Quality** | Modifiability Rate, Static Analysis Compatibility, Coding Standard Compliance Rate. |
| **Deliverability and Timeliness** | Timeliness of Source Code Delivery, Deficient Deliverables Rate. |
| **Verification and Validation** | Static Analysis Defect Rate, Post-Delivery Non-Conformance Identification Rate. |
| **Long-Term Access** | Long-Term Access Fulfillment Rate. |

  

By tracking these metrics, Software Assurance personnel can ensure compliance with this requirement and provide actionable insights into the accessibility, quality, and maintainability of the delivered source code and associated work products. This strengthens project outcomes and aligns with NASA's needs for independent assessments, long-term availability, and reuse opportunities.

## 7.4 Guidance

The guidance must align with organizational policies, including properly addressing proprietary rights, intellectual property considerations, and scope exclusions (e.g., COTS software). Below is updated **Software Assurance (SA)** guidance that clarifies expectations, strengthens oversight processes, and ensures the electronic access requirements are executed properly.

### 7.4.1 Purpose of the Requirement

This guidance outlines that NASA’s direct electronic access to modifiable source code serves critical purposes, including:

* **Independent Assessments**:

  + Enabling NASA’s teams to run their own static code analysis tools to assess software for errors, security vulnerabilities, adherence to coding standards, and quality metrics.
* **Verification and Validation (V&V)**:

  + Facilitating post-delivery verification activities, including regression testing, host compatibility checks, and functional performance evaluations.
* **Cost Reduction and Efficiency**:

  + Reducing project costs associated with troubleshooting by allowing early detection of defects through separate analysis processes.
  + Reducing hardware/software integration troubleshooting costs.
* **Long-Term Maintenance and Reuse**:

  + Ensuring software accessibility for defect repairs, enhancements, and component augmentations post-delivery.
  + Allowing for operations error diagnostics and enabling software reuse in future NASA projects.

### 7.4.2 Updated Roles and Responsibilities

**Software Assurance Responsibilities**:

1. SA personnel must **verify and confirm** that the developer has provided NASA with:

   * Complete and unrestricted **electronic access** to the source code and associated software deliverables.
   * The ability for NASA to modify the source code and run independent tools.
   * Accurate and complete lists of all products that need to be accessible per the requirements.
2. SA personnel must ensure that **access includes** flight, ground, test, simulation, and prototype software.
3. SA personnel must oversee that access is provided in **modifiable electronic formats** suitable for use with NASA's tools (e.g., text-based formats that are compatible with static analysis tools like CodeSonar or Coverity).

### 7.4.3 Expanded Scope of What Needs to be Accessible

To meet this requirement, SA personnel must confirm the availability and modifiability of the following types of software artifacts, source code, and electronic data:

* **Flight and Ground Software**:

  + Source code for software used onboard the flight systems and supporting ground operations.
* **Models and Simulations Source Code**:

  + Code used for simulated environments, mathematical models, or system behavior prediction purposes.
* **Programmable Logic Device Code**:

  + Logic definitions, design files, and software source code for programmable logic devices (e.g., FPGA or ASIC firmware).
* **Prototype Software**:

  + Source code used in early-stage prototypes, such as experimental architectures, features, or designs.
* **Data Definitions and Data Sets**:

  + Access to data definitions (e.g., schemas) and datasets (e.g., test data, flight data, configuration data).
* **Software Ground Products Source Code**:

  + Source code for data processing systems, telemetry systems, and other tools used in ground operations.
* **Build Products Source Code**:

  + Information relevant to software build processes, including instructions for build execution, dependencies, and scripts.
* **Software Test Scripts**:

  + Source code of scripts used for automated testing, verification, and validation purposes.
* **Software Database(s)**:

  + Documentation and source-level access to databases associated with software components.

**Software Assurance Action**: SA personnel must confirm that all the above artifacts are provided electronically, are modifiable, and are reconciled against NASA’s project requirements. Any missing elements must be flagged as findings with corrective action recommendations.

### 7.4.4 Oversight of Source Code Access

Ensuring access involves confirming:

1. **Electronic Access in Modifiable Format**:

   * Source code must be accessible in modifiable, editable formats (e.g., plain text, structured files compatible with version control systems like Git, or software development environments like Eclipse or Visual Studio).
   * Executables provided alongside source packages for dynamic analysis.
2. **Access for Software Assurance and Safety**:

   * Verify that Software Assurance (SA) and Software Safety personnel have direct access to the software for source-level reviews, analyses, and static/dynamic testing.
   * Confirm access credentials, permissions, and any restrictions imposed by intellectual property rights.
3. **Access for Independent Analysis Tools**:

   * Confirm that source code is accessible in formats compatible with NASA’s preferred static code analysis tools, such as:
     + CodeSonar
     + Coverity
     + Polyspace
     + Other NASA-mandated tools for quality checks.
4. **Access Duration**:

   * Verify agreements for long-term access to source code for maintenance, post-delivery analysis, and potential reuse for other NASA projects.

**Software Assurance Action**: Conduct **audits/inspections** with both the developers and NASA project team members to ensure that source code accessibility meets project needs without violating proprietary or intellectual property rights.

### 7.4.5 Intellectual Property and Proprietary Rights

During the software planning phase, SA personnel should confirm:

1. **Delivery Agreements**:

   * Source code delivery and electronic access methods adhere to intellectual property ownership agreements.
   * Methods are in place for ensuring the electronic transfer of source code does not violate proprietary rights or contractual restrictions.
2. **Software Development Documentation**:

   * Requirements for electronic access and delivery methods explicitly documented in the:
     + [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)
     + [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan)
     + Software Data Management Plan (SDMP)
3. **Compliance with [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software)**:

   * Exclusion of COTS or third-party software products from the requirement unless expressly negotiated as part of the contract.

**Software Assurance Action**: Perform **reviews of software planning and procurement documentation** to ensure these agreements and restrictions are adhered to. Any risks regarding access limitations should be escalated to the project manager immediately.

### 7.4.6 Methods for Verification

**Software Assurance Methods**:

1. Perform **artifact checklist reviews** of accessible deliverables, ensuring:

   * Source code and data formats are modifiable and usable.
   * Files are provided without encryption or proprietary locks that limit accessibility.
   * Associated metadata (documentation, build instructions, dependencies) is complete.
2. Ensure **technical compatibility**:

   * Confirm that source code formats are compatible with NASA’s analysis tools and systems.
3. Conduct **interviews with NASA personnel**:

   * Verify with software assurance and project engineers whether they encountered access limitations during testing or analysis activities.
4. Ensure **version control systems integration**:

   * Verify that developers grant NASA electronic access to source code stored in version control systems (e.g., Git repositories, Subversion) for traceability and audits.

### 7.4.7 Documentation of Compliance

**Software Assurance Products**:

1. **Source Code Availability Audit Report**:

   * Summarizes findings of source code accessibility reviews, including missing or inaccessible elements.
2. **Corrective Action Recommendations**:

   * Documents SA actions required to resolve access issues or format errors.
3. **Configuration Audit Results**:

   * Validates access to version control systems and software build tools.
4. **Long-Term Access Assessment**:

   * Ensures agreements for post-delivery accessibility are documented.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) |

# 8. Objective Evidence

Objective evidence refers to the artifacts SA personnel collect and evaluate to verify compliance with this requirement. This includes all tangible deliverables, reports, logs, and tools that demonstrate the software developer has provided NASA with complete electronic access to modifiable source code.

By collecting these products and evaluating this objective evidence, SA personnel can verify compliance with this requirement, ensure the suitability of all delivered source code and artifacts, and mitigate risks related to accessibility, quality, delivery, and intellectual property rights.

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

Below is a list of objective evidence that corresponds to the requirements and accountability tasks.

## 8.1 Source Code Files

**Evidence**:

* Delivered source code files for flight, ground, test, and prototype software in usable, modifiable formats.
* Electronic files provided in text-based formats compatible with version control systems (e.g., `.c`, `.cpp`, `.py`, `.java`).
* Example: Source code for programming logic devices, models, simulations, etc.

**Verification**:

* Check file formats to ensure compatibility with NASA's tools (editable and unencrypted).
* Confirm access permissions if code is hosted in repositories.

## 8.2 Test Scripts and Automation Code

**Evidence**:

* Delivered test scripts (e.g., for regression testing or automated verification).
* Examples: Python scripts for testing APIs, data verification scripts, or simulation validation routines.

**Verification**:

* Verify scripts are executable and compatible with NASA’s testing infrastructure.
* Ensure NASA has modifiable access to scripts for post-delivery testing.

## 8.3 Configuration Management Records

**Evidence**:

* Access to version control logs showing code baselines, modifications, branches, and history (e.g., Git logs, SVN revision history).
* Delivered configuration files for builds, dependencies, and testing environments.
* Example: `Dockerfile` for containerized builds, `Makefile` for compiled software.

**Verification**:

* Confirm the use of configuration management best practices (e.g., maintaining baselines, resolving conflicts).
* Verify NASA can replicate builds using provided configuration files.

## 8.4 Intellectual Property and Proprietary Rights Documentation

**Evidence**:

* Signed agreements or licenses granting NASA access to source code under intellectual property terms without restrictions on modification or maintenance.
* Documentation of proprietary restrictions, if any, and measures to ensure compliance.

**Verification**:

* Confirm that NASA has long-term rights to access and modify source code without violating proprietary agreements.
* Ensure restrictions are appropriately managed without inhibiting source code use.

## 8.5 Source Code Access Credentials

**Evidence**:

* Access credentials to repositories, platforms, or software systems where source code is hosted.
* Example: Login credentials to Git repositories or cloud-hosted tools (e.g., GitHub, Bitbucket, Atlassian tools).

**Verification**:

* Test credentials to confirm NASA personnel (including SA and software safety teams) can access the software.
* Flag any issues with restricted or incomplete access.

## 8.6 Static Analysis Reports

**Evidence**:

* Results from independent static analysis performed by NASA or SA personnel.
* Example: CodeSonar, Coverity, or Polyspace output logs detailing issues like unused variables, null pointer dereferences, buffer overflows, or coding standard violations.

**Verification**:

* Ensure analysis tools can read and parse delivered code.
* Confirm metrics like defect density and security vulnerabilities align with project tolerances.

## 8.7 Build Logs and Artifacts

**Evidence**:

* Logs and metadata for builds derived from delivered source code.
* Examples: Detailed build logs showing steps, warnings, errors, and outcomes.

**Verification**:

* Verify that the provided build instructions replicate outputs successfully using NASA systems.
* Confirm the inclusion of all dependent files and configurations.

## 8.8 Delivered Metrics

**Evidence**:

* Project metrics related to source code quality and access, including:
  + Percentage of delivered source code tested and validated.
  + Static analysis defect rates.
  + Timeliness of delivery (% artifacts submitted on time).
* Example: Metrics summarized in a compliance tracking report.

**Verification**:

* Ensure metrics align with the project’s defined acceptance thresholds and guidelines.
* Flag discrepancies related to missing or deficient deliverables.

## 8.9 Summary of SA Products and Objective Evidence

| **Category** | **SA Product** | **Objective Evidence** |
| --- | --- | --- |
| **Source Code Access** | Source Code Access Verification Report | Source code files, repository credentials, modifiable formats. |
| **Artifact Completeness** | Compliance Checklist for Deliverables | Full list of artifacts, including test scripts, configurations, and databases. |
| **Code Quality and Static Analysis** | Static Analysis Report | Static analysis output, defect data, coding compliance logs. |
| **Configuration Management** | Configuration and Version Control Access Report | Version control logs, configuration files, build replication success logs. |
| **Intellectual Property Rights** | Intellectual Property Compliance Report | Signed agreements and licenses granting electronic access and modification rights. |
| **Post-Delivery and Risk Review** | Post-Delivery Review and Risk Assessment Report | Metrics showing long-term access compliance and usability of delivered artifacts. |
