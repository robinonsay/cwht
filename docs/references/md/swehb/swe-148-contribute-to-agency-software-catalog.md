# SWE-148 - Contribute to Agency Software Catalog

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695505. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog

SWE-148 - Contribute to Agency Software Catalog

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695505)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695505&showCommentArea=true&showComments=true#addcomment)

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

3.10.2 The project manager shall evaluate software for potential reuse by other projects across NASA and contribute reuse candidates to the appropriate NASA internal sharing and reuse software system. However, if the project manager is not a civil servant, then a civil servant will pre-approve all such software contributions; all software contributions should include, at a minimum, the following information:

a. Software Title.  
b. Software Description.  
c. The Civil Servant Software Technical POC for the software product.  
d. The language or languages used to develop the software.  
e. Any third-party code contained therein, and the record of the requisite license or permission received from the third party permitting the Government’s use and any required markings (e.g., required copyright, author, applicable license notices within the software code, and the source of each third-party software component (e.g., software URL & license URL)), if applicable.  
f. Release notes.

## 1.1 Notes

Currently, there are more than one Agency-wide software inventories and repositories, several options can be found in NASA-HDBK-2203. In order to obtain and reuse the internal software reuse candidates from these repositories, NASA civil servants may request a copy by requesting and completing a simple Acknowledgment of Receipt of the software form that identifies any restrictions on NASA’s right to use the software, including limiting its use to governmental purposes only. The Civil Servant Software Technical POC for the software product will keep a list of all contributors to the software. Any software shared will contain appropriate disclaimer and indemnification provisions (e.g., in a “README” file) stating that the software may be subject to U.S. export control restrictions, and it is provided “as is” without any warranty, express, or implied and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors (see paragraph 2.1.5.17).

## 1.2 History

Click here to view the history of this requirement: SWE-148 History

SWE-148 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 3.14.3 The project manager shall evaluate software for potential reuse by other projects across the Agency and contribute reuse candidates to the Agency Software Catalog. |
| Difference between B and C | Changed "NASA" to "Agency";  Changed "Agency Software Catalog" to "NASA Internal Sharing and Reuse Software systems";  Added caveats for approval conditions if the project manager is a contractor. |
| C | 3.10.2 The project manager shall evaluate software for potential reuse by other projects across NASA and contribute reuse candidates to the NASA Internal Sharing and Reuse Software systems. However, if the project manager is a contractor, then a civil servant must pre-approve all such software contributions; all software contributions should include, at a minimum, the following information:   1. 1. Software Title.    2. Software Description.    3. The Civil Servant Software Technical Point of Contact for the software product.    4. The language or languages used to develop the software.    5. Any third party code contained therein and the record of the requisite license or permission received from the third party permitting the Government’s use, if applicable. |
| Difference between C and D | Added items e and f per the request of the OGC and OCIO |
| D | 3.10.2 The project manager shall evaluate software for potential reuse by other projects across NASA and contribute reuse candidates to the appropriate NASA internal sharing and reuse software system. However, if the project manager is not a civil servant, then a civil servant will pre-approve all such software contributions; all software contributions should include, at a minimum, the following information:  a. Software Title. b. Software Description. c. The Civil Servant Software Technical POC for the software product. d. The language or languages used to develop the software. e. Any third-party code contained therein, and the record of the requisite license or permission received from the third party permitting the Government’s use and any required markings (e.g., required copyright, author, applicable license notices within the software code, and the source of each third-party software component (e.g., software URL & license URL)), if applicable. f. Release notes. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 2. Rationale

Reusing software can have many benefits for the Agency, including, but not limited to, cost savings.  For this reason, software project managers consider future reuse of software components created for their projects and make those selected components available to future projects through an Agency repository.

Maximizing software reuse across NASA promotes efficiency, reduces duplication of effort, and enables collaborative innovation, all of which are critical in the context of NASA's resource-intensive missions and projects. This requirement ensures that software developed within NASA is systematically evaluated for reuse potential and that candidates are properly contributed to internal repositories, enabling broader sharing and adoption across the agency. By establishing clear guidelines for contributions, the requirement also addresses legal, technical, and operational considerations necessary to protect NASA’s interests and ensure compatibility with other projects.

This requirement ensures that NASA’s software development efforts are leveraged to their fullest potential by systematically identifying, evaluating, and contributing software products for reuse. It promotes efficiency, collaboration, and innovation while safeguarding NASA’s legal, technical, and operational interests. By including clear contribution criteria and technical oversight, this requirement establishes a robust foundation for sharing reusable software across NASA projects, enabling the agency to accomplish more with its resources and maintain its leadership in developing innovative software solutions for space exploration and scientific discovery.

### **Key Objectives of the Requirement**

1. **Maximizing the Value of NASA’s Software Assets**:

   * NASA invests significant resources in developing software for a variety of mission-critical applications, such as simulations, data processing, guidance, navigation, and control. Evaluating and contributing software for reuse ensures these valuable assets are leveraged to support multiple current and future initiatives. This reduces redundancy, prevents "reinventing the wheel," and increases the return on investment of NASA’s software development efforts.
2. **Facilitating Collaboration Across Projects and Centers**:

   * By sharing and cataloging reusable software, this requirement enables NASA projects and Centers to benefit from the expertise and work of others. This promotes knowledge sharing, fosters innovation, and reduces development effort for subsequent projects that can build on proven, validated software components.
3. **Ensuring Legal Compliance and Proper Documentation**:

   * The requirement ensures that all software contributions conform to intellectual property laws, licensing agreements, and NASA policies for open-source or third-party code. By mandating thorough documentation—including third-party code details and permissions—it mitigates the legal risks associated with sharing software that involves external contributors or dependencies. This protects NASA’s ability to freely use and distribute its software while promoting transparency and accountability.
4. **Streamlining Reuse Through Standardization**:

   * Including key metadata in software contributions—such as title, description, programming language, and release notes—makes it easier for other projects to identify and evaluate the software’s applicability and compatibility. This standardization ensures the software catalog remains searchable and navigable, improving the efficiency of reuse efforts across NASA.
5. **Enhancing Software Sustainability and Lifecycle Management**:

   * Documenting reusable components within NASA's internal sharing and reuse systems ensures that software is preserved, well-documented, and accessible in the long term. This helps projects adapt or maintain software more effectively, especially for long-duration missions or future iterations.
6. **Promoting Civil Servant Oversight and Accountability**:

   * Requiring pre-approval by a NASA Civil Servant for contributions when the project manager is not a civil servant ensures that contributions are vetted appropriately. This protects NASA from unintentional issues related to intellectual property, compliance, or quality and guarantees that all contributed software aligns with agency standards and policies.

### **Why Contributing Reusable Software is Critical for NASA’s Mission**

#### **Advance Agency-Wide Goals**:

Reusable software accelerates development timelines, reduces costs, and improves mission readiness. For instance, the ability to leverage existing guidance and navigation software or validated simulation environments can shorten schedules for future missions while delivering more reliable systems.

#### **Reduce Redundancy and Wasted Effort**:

Repeatedly developing similar software solutions for different missions or projects leads to inefficiencies and increased costs. Sharing reusable software prevents redundant effort, allowing development teams to focus on innovation and mission-specific challenges.

#### **Ensure Technological Leadership**:

By fostering software reuse, NASA maintains its leadership in cutting-edge aerospace and scientific software development. Reusing, improving, and sharing software leads to higher-quality, well-tested systems and promotes advancements in software engineering best practices and technologies within NASA.

### **Key Safeguards Embedded in the Requirement**

The information required with every software contribution ensures compliance, reusability, and accountability:

* **Software Title & Description**: Provides essential context to ensure software is discoverable and its capabilities are clearly understood by future users.
* **Civil Servant Point of Contact (POC)**: Establishes accountability for the software and provides a technical expert who can answer questions or address future needs related to the software.
* **Development Language(s)**: Identifies software dependencies and ensures compatibility with NASA's technical and operational systems.
* **Third-Party Code and Licensing**: Mitigates legal and compliance risks related to the inclusion of non-NASA components, ensuring proper permissions are documented and adhered to.
* **Release Notes**: Documents the most recent updates, changes, and features of the software, providing key context for other projects considering reuse.

# 3. Guidance

## 3.1 Evaluating Software For Reuse

When evaluating software for potential reuse, consider both **individual components** (e.g., modules, libraries, tools, algorithms) and **entire software systems** (e.g., applications, frameworks) to maximize reuse opportunities across NASA and protect investment in software development.

Evaluating and selecting software for reuse is a vital process that maximizes NASA’s software assets, reduces redundancy, and promotes collaborative innovation. By leveraging tools like Reuse Readiness Levels, considering critical reuse criteria, and incorporating reusability into the software lifecycle, NASA achieves a sustainable approach to software development that benefits current and future projects. Ensuring that reusable software is properly documented, tested, and compliant with legal and technical standards enables NASA to continue its leadership in software engineering and mission success.

### **Reuse Readiness Levels (RRLs)**

The concept of “Reuse Readiness Levels” (RRLs) helps assess the extent to which a software product meets reuse conditions. These levels provide guidance for systematic evaluation of software based on technical, legal, and operational criteria. RRLs help ensure software components are properly vetted before being shared for reuse and integrated into new systems.

The following **Reuse Readiness Levels (RRLs)**, adapted from *“A Proposal on Using Reuse Readiness Levels to Measure Software Reusability”* by Downs and Marshall, provide descriptions for evaluating software readiness for reuse. Use these levels as benchmarks to assess the potential for software to be effectively reused:

| **Level** | **Summary** | **Description** |
| --- | --- | --- |
| **1** | Limited reusability | Basic source code or binaries are available with no support, limited or no documentation, and unclear rights or permissions for reuse. Not recommended. |
| **2** | Initial reusability | Minimal documentation and testing provided, but reuse is impractical due to unclear rights and high costs of adaptation. |
| **3** | Basic reusability | Some modularity and standards compliance exist but limited applicability. Skilled users may reuse with substantial effort and risk. |
| **4** | Reuse is possible | Complete documentation and software proven in lab conditions. Reuse is possible but requires notable effort, negotiation for intellectual property. |
| **5** | Reuse is practical | Modular, extendable, moderately tested software with small user communities. Reuse includes limited risk and reasonable cost. |
| **6** | Software is reusable | Designed for extensibility, modularity, and portability. Tutorials are available, and software is validated in relevant contexts with limited risks. |
| **7** | Highly reusable | Fully portable, modular, standards-compliant software with auto-build tools, and interfaces with documentation available. Minimal reuse risk. |
| **8** | Demonstrated local reusability | Extensible software with support for patches and successful demonstrations of reuse across multiple users/projects. Permission statements are included. |
| **9** | Demonstrated extensive reusability | Fully validated software reused across diverse systems with robust documentation, GUI installers, and strong community support. No reuse restrictions. |

### **Guidance for Applying RRLs**

1. **Assess Against RRLs**: Start by identifying the current RRL of the software based on its documentation, modularity, compliance, and testing. The goal is to improve the software's RRL to make it more reusable for new applications with reduced effort, risk, and cost.
2. **Plan Reuse Improvements**: If deficiencies are found during the evaluation (e.g., minimal documentation or unclear licensing), outline the steps required to make the software more reusable, such as adding better documentation, modularizing code, or clearing intellectual property considerations.
3. **Match Software to Context**: Consider where and how the software is likely to be reused. A higher RRL may be necessary for software intended for large-scale adoption or diverse systems, while a lower RRL may suffice for specialized or limited reuse cases.

## 3.2 Reuse Requirements

When assessing software for potential reuse, consider critical characteristics that influence how effectively software can be reused. This ensures software meets both current project needs and reuse conditions for future applications.

### **Critical Characteristics for Reusability**

1. **Documentation**:

   * Includes clear design, usability, and developer documentation for easy integration.
   * Explains interfaces, system architecture, and configuration details to streamline understanding for future users.
2. **Extensibility**:

   * Software should be designed with extensibility in mind for adaptation to new requirements or projects while avoiding code modifications.
3. **Intellectual Property Issues**:

   * Verify ownership, licensing agreements, open-source usage, and third-party contributors to avoid legal risks during reuse.
4. **Modularity**:

   * Modular software ensures components can be reused independently. Proper separation between functions minimizes dependencies and simplifies integration.
5. **Packaging**:

   * Provide encapsulated packages for easy deployment, including installation manuals, setup files, and required tools.
6. **Portability**:

   * Software should be compatible with various environments/platforms, ensuring broad applicability across NASA systems.
7. **Standards Compliance**:

   * Adhere to NASA, industry, or open-source standards (e.g., coding standards, testing protocols) that facilitate reuse across different teams and projects.
8. **Support**:

   * Include developer-organized support channels, user forums, or FAQs to address common issues or questions about the software.
9. **Verification and Testing**:

   * Ensure proper testing artifacts (e.g., test cases, reports, validations) are included, showing reliability and robustness in intended contexts.

### **Additional Criteria to Consider**

* **Cost-Benefit Evaluation**: Is the software expensive to develop but likely to provide cost savings through reuse?
* **High Quality and Testing**: Has the software undergone rigorous testing to ensure reliability and quality for reuse?
* **Ease of Future Integration**: Are boundaries, interfaces, and design clearly defined to simplify integration?
* **Multiple Applicability**: Does the software have broad applicability across different projects or industries?
* **Self-Contained Components**: Does the software limit external dependencies, allowing for easier reuse?

## 3.3 Selecting Software for Reuse

Selecting software for reuse early in the software lifecycle is critical for ensuring reusability requirements are incorporated into the design and development process. This proactive approach reduces re-engineering costs and expedites future reuse.

### **Key Practices for Selecting Software for Reuse**

1. **Identify Reusability Candidates Early**:

   * During the planning phase, identify components or entire systems that have reuse potential and ensure they are designed with modularity, portability, and extensibility (see SWE-147).
2. **Adopt Reusability Standards**:

   * Use NASA guidance to ensure all candidates meet minimum standards for documentation, testing, and verification before selection.
3. **Prioritize Valuable Components**:

   * Focus on selecting large-impact components, such as algorithms, tools, or systems that are broadly applicable across NASA projects.
4. **Collaborate with Relevant Teams**:

   * Work with software assurance, legal teams, and technical experts to ensure intellectual property compliance and technical readiness for reuse.
5. **Document for Repository Submission**:

   * Software identified for reuse should be provided with complete metadata (title, description, contact details, licensing, etc.) and transferred to the relevant repository, such as NASA’s Internal Sharing and Reuse Systems.
6. **Initiate Final Transfer**:

   * At the end of the project, submit reusable software to the NASA Internal Sharing and Reuse Software system through the Center’s Technology Transfer Office.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

Small projects often face constraints in resources such as time, budget, and personnel. Meeting Requirement 3.10.2 in a small project environment requires a focused and pragmatic approach that balances limited resources while maintaining compliance with software reuse policies. This guidance provides small projects with tailored strategies to identify, document, and contribute software for potential reuse without introducing unnecessary overhead.

For small projects, adhering to the reuse requirements outlined in 3.10.2 is achievable with a focused, step-by-step approach. By evaluating reuse potential early, documenting key metadata, and leveraging NASA’s existing processes and repositories, small projects can effectively contribute valuable software to the agency’s larger mission. Tailoring documentation and reuse strategies to the scale and scope of a small project avoids unnecessary burden while still supporting efficient and impactful software sharing within NASA.

### **Guidance for Small Projects**

#### **1. Keep it Simple and Strategic**

* Focus on software components that are **most likely to add value** to NASA's overall software library. For small projects, this is likely to include:
  + Standalone tools or utilities.
  + Modular code libraries.
  + Algorithms, models, and simulations specific to NASA operations.
  + Software with broad applicability across multiple projects or disciplines.
* Avoid overanalyzing every software component—prioritize usefulness and relevance when evaluating software for contribution.

#### **2. Tailor Evaluation for Reuse Potential**

To minimize resource strain, adopt a simple checklist for evaluating reuse potential:

* Is the software broadly applicable to other NASA projects?
* Is the software self-contained or modular (with few dependencies)?
* Has the software been properly tested and validated?
* Are intellectual property rights and third-party licenses resolved?
* Is sufficient documentation available, or can basic documentation be created easily?

If the answer is "yes" to most of these questions, the software is likely a good candidate for reuse.

#### **3. Leverage NASA Tools and Precedents**

* Use existing tools like the **NASA Internal Sharing and Reuse System** to assess whether similar software already exists. If a similar resource exists, evaluate whether your project’s software provides additional functionality or improvements.
* Consult reuse guidelines, templates, and checklists from NASA’s software engineering handbook or your Center’s Technology Transfer Office to streamline the evaluation and documentation process.

#### **4. Streamline Documentation for Reuse Submission**

Small projects can meet the minimum documentation requirements (a–f) without overwhelming resources:

* **Software Title**: Use a clear and concise title that describes the function or purpose of the software.
* **Software Description**: Write a short, one-paragraph description that includes:
  + The software’s primary purpose.
  + Its potential application in other projects.
  + Key technical features or highlights (e.g., modularity, compatibility with NASA platforms).
* **Technical Point of Contact (POC)**: Provide the name and contact information of a NASA Civil Servant familiar with the software. This can be a systems engineer, software lead, or anyone involved with the development process.
* **Languages Used**: List the programming language(s) (e.g., Python, C++, MATLAB) to allow future users to assess compatibility.
* **Third-Party Code**: Use a **lightweight inventory checklist** to track and document third-party code, including:
  + Source of the third-party components.
  + Relevant licensing information and compliance statements.
  + URLs or sources for inspection.
* **Release Notes**: Provide a simple summary of the software version being submitted, outlining:
  + Any updates or bug fixes.
  + Known issues.
  + An overview of core functionality.

> **Tip:** Assign a team member (if available) to maintain brief but clear documentation throughout the project lifecycle to avoid rushing documentation work at the end.

#### **5. Minimize Legal and Licensing Complexity**

Small projects can avoid potential risks associated with intellectual property or licensing as follows:

* **Early Verification**: Verify intellectual property ownership and licensing at the project initiation phase, particularly for third-party or open-source components.
* **Keep It Clean**: Minimize reliance on third-party libraries or software with restrictive licenses, as this can complicate reuse eligibility.
* **Consult Legal Resources**: Collaborate with your Center’s Legal Office or Technology Transfer Office for any questions related to licensing and ownership.
* Document compliance with **SWE-027** (Use of Commercial, Government, and Legacy Software) and **SWE-217** (List of Contributors and Disclaimer Notice).

#### **6. Incorporate Evaluation into the Software Lifecycle**

* **At Milestones**: Use software design reviews or testing milestones to evaluate the software for reuse potential. Incorporate a brief reuse evaluation as part of these regular reviews.
* **Before Closure**: Before the project closes, verify that reusable components are ready for submission. Utilize the final project report or handoff processes to certify the software for reuse.

#### **7. Submission Pathway for Small Projects**

Small projects can streamline the submission of reusable software as follows:

* **Submit via Internal Reuse Systems**: Use the NASA Internal Sharing and Reuse Software Systems or your Center’s designated repository to submit reusable software.
* **Preapproval for Non-Civil Servant Project Managers**: If the project manager is not a civil servant, coordinate with a NASA Civil Servant early in the submission process to obtain the necessary pre-approvals for all software contributions.

#### **8. Focus on Lightweight Contributions for Reuse**

Small project deliverables often involve focused tools, rather than large systems. Examples of software contributions that small projects could submit for reuse:

* **Reusable Libraries**: Algorithms for trajectory analysis, data processing, or numerical modeling.
* **Simulation Tools**: Lightweight simulations for environment modeling or sensor analysis.
* **Utilities**: Code for data visualization, process automation, or error analysis.
* **Documentation Enhancements**: Clear user guides, developer tutorials, or API references to support future adoption by other teams.

Focus on submitting small, modular tools that are easy for other teams to use and integrate.

### **Checklist for Small Projects – Software Reuse Evaluation**

Use this **quick checklist** to ensure compliance with Requirement 3.10.2:

1. **Evaluated Software Components**:
   * Has the software been assessed for reuse potential (e.g., modularity, portability)?
2. **Resolved Licensing**:
   * Are intellectual property rights and third-party licenses documented and clear?
3. **Prepared Metadata**:
   * Are title, description, point of contact, language, and release notes included?
4. **Collected Documentation**:
   * Are key documents (e.g., design, test reports, user guides) available or simplified for easy delivery?
5. **Approved Submission**:
   * If applicable, has the contribution been pre-approved by a NASA Civil Servant?

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-479)

  [Reuse Readiness Levels as a Measure of Software Reusability,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4779626 "Click to open in new window")

  Marshall, James. And Downs, Robert, IEEE, 2008. Retrieved from http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4779626 on August 19, 2015.
* (SWEREF-480)

  [A Proposal on Using Reuse Readiness Levels to Measure Software Reusability,](https://academiccommons.columbia.edu/catalog/ac:180794 "Click to open in new window")

  Downs, Robert and Marshall, James. Data Science Journal, Volume 9, July 24, 2010.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

  

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA Lessons Learned that align with **Requirement 3.10.2** (*Evaluating and Contributing Software for Reuse*). These lessons provide valuable context and guidance for fostering software reuse, improving documentation, addressing intellectual property concerns, and preserving software for future NASA missions:

### **1. Lesson Learned: Importance of Software Reuse in Technical and Budget-Constrained Environments**

* **Lesson ID**: 1372
* **Key Insight**:  
  Software reuse can enable cost, schedule, and risk reductions for NASA projects, particularly those with budget and time constraints. However, achieving successful reuse requires early integration of reusability planning, effective modular design, and thorough documentation with reuse in mind. Lack of foresight in planning reusable components can lead to significant integration challenges, even if the software technically fulfills its current mission's requirements.
* **Relevance to Requirement 3.10.2**:  
  This lesson highlights the need to evaluate software for reuse early in project development. When contributing reusable software, ensuring modularity, thorough testing, and good documentation can enhance the software's usability for future projects. Adding reusable components to NASA’s software repositories can prevent repetitive development efforts across the agency.
* **Source**: NASA's Lessons Learned database.

### **2. Lesson Learned: Issues with Inadequate Documentation for Reuse**

* **Lesson ID**: 0857
* **Key Insight**:  
  Many NASA projects encountered difficulties in reusing software due to incomplete, ambiguous, or missing documentation. Even when the software itself was functional, the absence of clear installation instructions, operating procedures, or design explanations made it impractical to adapt or reuse. This points to a critical need for providing detailed release notes and metadata during submission for reuse.
* **Relevance to Requirement 3.10.2**:  
  This lesson emphasizes the importance of ensuring that every submitted software component includes the required basic information (e.g., purpose, instructions, languages used, dependencies, contact POC, and licensing). Clear descriptions make software easier to locate and reuse, reducing future workload.
* **Practical Takeaway**: Small projects, in particular, should maintain lightweight but detailed documentation throughout the development lifecycle to streamline reuse submissions.
* **Source**: NASA’s Lessons Learned Information System (LLIS).

### **3. Lesson Learned: Risks of Neglecting Licensing and Intellectual Property (IP)**

* **Lesson ID**: 1258
* **Key Insight**:  
  Some software reuse initiatives were delayed or abandoned because of improperly documented intellectual property rights (IPR) or third-party licensing issues. Projects that didn't confirm reuse rights for included components (e.g., commercial, open-source libraries) encountered legal barriers during software distribution.
* **Relevance to Requirement 3.10.2**:  
  This lesson reinforces the need for small projects to clearly detail third-party content, licenses, and permissions when submitting their software for reuse. A compliance check for licensing is critical to ensuring agency-wide adoption of reusable components. Documentation of third-party code, licenses, and source URLs is mandatory to verify compatibility with reuse policies.
* **Source**: NASA Office of the Chief Engineer (OCE).

### **4. Lesson Learned: Difficulty in Reusing Monolithic Software**

* **Lesson ID**: 0765
* **Key Insight**:  
  Software that was not modular in design posed challenges for reuse in subsequent missions. Dependencies on specific hardware, tightly coupled interfaces, and inflexible structures made adaptation and integration difficult and expensive. Designing for modularity and extensibility is essential for successful software reuse.
* **Relevance to Requirement 3.10.2**:  
  Software contributions to NASA’s reuse repositories should prioritize modular architectures, encapsulated functionality, and clear interface definitions. Small projects should embrace modularity early in development to ensure that reusable components can operate independently without requiring the entire system.
* **Source**: NASA Goddard Space Flight Center (GSFC).

### **5. Lesson Learned: Ensuring Reusability Through Verification and Validation**

* **Lesson ID**: 1014
* **Key Insight**:  
  Reuse candidates that lacked sufficient verification and validation (V&V) created additional risks for later projects. Software reused without robust testing in its native or other relevant environments led to costly integration errors and mission delays. Future reuse depends on the credibility and reliability of the software in question.
* **Relevance to Requirement 3.10.2**:  
  Before submission, software should meet at least minimal verification and validation criteria. Even for small projects, documenting how successfully the software performed (e.g., in lab tests, simulations, or operational use) can improve confidence in its reusability. Including release notes with known limitations and test reports is essential for transparent submission.
* **Practical Advice**: Small projects should run reuse candidates through basic functionality tests and record the results, even if formal V&V processes are not feasible.
* **Source**: NASA Engineering Practice Standards.

### **6. Lesson Learned: Leveraging Repositories for Knowledge Transfer**

* **Lesson ID**: 1119
* **Key Insight**:  
  NASA’s centralized sharing systems, such as the NASA Internal Sharing and Reuse System, are underutilized by small teams. Projects often develop valuable software but fail to submit it to a repository, resulting in lost opportunities for reuse across NASA. Conversely, projects that shared software and properly used internal repositories allowed other missions to build on their work, saving time and resources.
* **Relevance to Requirement 3.10.2**:  
  This lesson emphasizes the importance of using NASA’s internal sharing systems to disseminate and preserve reusable software components. By submitting well-documented contributions, small projects actively support knowledge transfer and agency-wide collaboration.
* **Practical Application**: Small projects should designate a team member to handle repository submissions and ensure metadata compliance (e.g., title, description, POC, and licensing). This ensures no reusable component is overlooked at the project’s conclusion.
* **Source**: NASA Center for Excellence in Collaborative Development.

### **7. Lesson Learned: Cost-Saving Benefits of Early Reuse Planning**

* **Lesson ID**: 1425
* **Key Insight**:  
  Projects that explicitly identified and planned for reusable software components at the beginning of development saw measurable cost savings in future applications. By factoring reusability into requirements, design, and documentation, teams reduced technical debt and avoided creating software that was only fit for a single-use purpose.
* **Relevance to Requirement 3.10.2**:  
  Small projects can incorporate reusability planning in early development stages, focusing on modularity, well-defined interfaces, and lightweight documentation. Ensuring that reusability is part of the software design process avoids the need for redesign and enables easier submission later.
* **Source**: NASA Headquarters, Software Engineering Division.

These lessons highlight common challenges and strategies related to software reuse within NASA. They reinforce the importance of modular design, clear documentation, intellectual property compliance, thorough testing, and systematic sharing. For small projects, these insights are particularly valuable in ensuring successful contributions to NASA's software repositories while maximizing efficiency and collaboration across the agency.

Small teams should focus on building reusable software from the start and leverage the lessons learned from previous projects to minimize effort and maximize the impact of their contributions.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Leverage projects to create benefits that go beyond the project](https://software.gsfc.nasa.gov/lesson-details/73/). **Lesson Number #**: The recommendation states: "Leverage projects to create benefits that go beyond the project."
* [Coordination with Export Control Office](https://software.gsfc.nasa.gov/lesson-details/168/). **Lesson Number 168**: The recommendation states: "Coordinate early in the project or release cycle with Export Control and Patent Counsel, via direct real-time communication."

# 7. Software Assurance

**SWE-148 - Contribute to Agency Software Catalog**

3.10.2 The project manager shall evaluate software for potential reuse by other projects across NASA and contribute reuse candidates to the appropriate NASA internal sharing and reuse software system. However, if the project manager is not a civil servant, then a civil servant will pre-approve all such software contributions; all software contributions should include, at a minimum, the following information:

a. Software Title.  
b. Software Description.  
c. The Civil Servant Software Technical POC for the software product.  
d. The language or languages used to develop the software.  
e. Any third-party code contained therein, and the record of the requisite license or permission received from the third party permitting the Government’s use and any required markings (e.g., required copyright, author, applicable license notices within the software code, and the source of each third-party software component (e.g., software URL & license URL)), if applicable.  
f. Release notes.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that any project software contributed as a reuse candidate has the identified information in items “a” through “f.”

## 7.2 Software Assurance Products

This software assurance guidance for Requirement 3.10.2 ensures that reusable software contributions meet NASA’s expectations for quality, compliance, and future adaptability. By leveraging assurance metrics and focusing on evaluating readiness levels, documentation, and licensing compliance, the assurance team can ensure consistency and maximize the value of reusable software contributions across NASA projects. These activities help promote software reuse as a strategic asset for NASA’s missions.

**Purpose**: To identify and ensure the delivery of necessary assurance artifacts supporting software reuse for NASA projects and missions.

#### **Recommended Software Assurance Products for Reuse Evaluations**:

1. **Software Reuse Evaluation Reports**:

   * A summary of software components analyzed for reuse potential (including justification for inclusion or exclusion). This report ensures traceability of decisions regarding reuse eligibility.
   * Includes key factors such as modularity, test results, quality assessments, and compliance with reuse readiness levels.
2. **Verification and Validation (V&V) Results**:

   * Include records of V&V activities performed to ensure the software is reliable, meets NASA standards, and is suitable for reuse.
   * Clear documentation of functional testing, boundary condition testing, and regression testing results contributes to confidence in the software’s reusability.
3. **Reuse Compliance Checklist**:

   * A checklist to verify adherence to reuse requirements, such as licensing resolution, modularity, portability, and documentation completeness.
   * Confirms compliance with metadata requirements outlined in Requirement 3.10.2.
4. **Documentation Review Record**:

   * An evaluation of reusable software documentation, ensuring adequate instructions, descriptions, and metadata fields are completed (e.g., software title, POC, etc.).
5. **Risk Assessment Report (Optional)**:

   * Identifies potential risks associated with reusing the software (e.g., unresolved licensing concerns, reliance on obsolete technologies).

## 7.3 Software Assurance Metrics

#### **Purpose of Metrics**:

Metrics help assess the effectiveness of software reuse efforts and identify opportunities for improvement by tracking the volume, quality, and completeness of products submitted for internal reuse.

#### **Suggested Metrics for Software Reuse**:

1. **Quantity of Products Submitted for Reuse**:

   * *Metric*: Total number of software products submitted for reuse.
   * *Utility*: Provides basic insight into how actively a project is contributing reusable items.
2. **Submission Rate**:

   * *Metric*:  
     [ \text{# of products submitted for reuse / Total # of developed products} ]
   * *Target*: A higher ratio reflects a greater emphasis on reusability.
   * *Utility*: Tracks the percentage of software eligible for reuse from the total produced during the project lifecycle.
3. **Submission to Repository Ratio**:

   * *Metric*:  
     [ \text{# of products submitted to the NASA Internal Sharing & Reuse System / Total # of developed products} ]
   * *Target*: Aim for all reusable software to be entered into NASA’s designated repository for maximum benefit.
   * *Utility*: Measures how many reusable software components were shared appropriately within NASA systems.
4. **Reuse Readiness Compliance**:

   * *Metric*:  
     [ \text{# of products submitted for reuse meeting Reuse Readiness Level (RRL) 5 or higher / Total # of products submitted for reuse} ]
   * *Target*: A higher ratio indicates that submitted software is being prepared to meet high reuse criteria for reduced risk and easier integration.
   * *Utility*: Determines the quality and reusability of submitted software by aligning it with RRL standards.
5. **Reuse Utilization Tracking (Optional)**:

   * *Metric*: Number of software components reused by other projects (secondary NASA missions).
   * *Utility*: Provides long-term feedback on how effectively reusable products are meeting cross-program needs.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

#### **Key Objectives for Software Assurance in Reuse Evaluations**:

The role of software assurance (SA) in Requirement 3.10.2 is to verify that software designated for reuse:

* Meets the technical and documentation standards necessary to facilitate reuse by other NASA projects.
* Complies with NASA’s licensing and intellectual property expectations.
* Includes sufficient verification and validation evidence to inspire confidence in the software’s reliability and safety.
* Adheres to modularity and portability principles to reduce integration risks.

#### **Recommended Assurance Activities for Reusable Software**:

**Evaluate Reuse Readiness Levels (RRLs):**

* + Use RRLs as a tool to define the software’s maturity for reuse and to ensure alignment with NASA policies.
  + Verify that reusable components meet at least the minimum RRL baseline (e.g., **RRL 4 or higher**) and include documented evidence to substantiate the level.

**Ensure Compliance with Required Metadata**:

* + Verify that, at a minimum, the following metadata fields are included with submissions:

    - Software Title.
    - Software Description (with intended application and purpose).
    - Civil Servant Technical POC.
    - Programming Language(s) used in development.
    - List of third-party code and licenses, with any associated permissions for government reuse.
    - Release Notes describing functionality, updates, and known issues.
  + Conduct **traceability reviews** to ensure that metadata fields match the actual content of the software (e.g., does the source code reflect the stated programming language and third-party usage?).

**Verify Documentation Quality**:

* + Conduct a documentation review to ensure that reusable software includes:

    - Instructions for setup and installation.
    - Clear boundary/interface descriptions and usability manuals.
    - Basic design overviews, such as system architecture diagrams or workflows.
  + Ensure all documentation is understandable to users unfamiliar with the software’s origin.

**Check for Intellectual Property/Third-Party Compliance**:

* + Conduct a **licensing review** to confirm:
    - Any third-party dependencies are clearly listed with licensing details.
    - No components violate guidelines for intellectual property or open-source licenses incompatible with NASA’s needs.
  + Work with the project’s Technology Transfer Office and legal counsel to address unresolved IP issues, if necessary.

**Perform Assurance Testing on Reuse Candidates**:

* + Verify that all reusable components have undergone appropriate testing, including:
  + Functional testing to demonstrate that the software performs as intended.
  + Validation in relevant environments (e.g., simulations for operational systems).
  + Risk analysis to assess reliability, including evidence of known issues and patches provided with the software.

**Audit Software Submission to NASA Repositories**:

* + Verify that all reusable software products are entered into the appropriate repositories, such as the NASA Internal Sharing and Reuse System, with complete metadata and compliance documentation.
  + Establish tracking mechanisms (e.g., logs) to monitor submissions and improve submission practices over time.

#### **Relation to SWE-147 (Specify Reusability Requirements)**:

See the software assurance guidance for **SWE-147**, which addresses how to define and plan reusability requirements early in the project lifecycle. The key is ensuring upfront planning to design software with modularity, documentation, and portability in mind from the start.

See the [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements)software assurance guidance information.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence is tangible proof that demonstrates compliance with Requirement 3.10.2. This involves verifying that reusable software has been identified, evaluated for reuse, and submitted to NASA's internal sharing and reuse system, along with required metadata and documentation.

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

Below is guidance on the type of objective evidence that can be collected and submitted to support compliance:

### **1. Evidence of Software Evaluation for Reuse**

Demonstrates that the software has been evaluated to determine its eligibility for reuse across NASA projects.

#### **Artifacts**:

* **Reuse Evaluation Report**:

  + A document that lists all software components developed by the project along with their reuse potential.
  + Includes descriptions of modularity, applicability, test results, dependencies, and reasoning for inclusion/exclusion.
  + Example content:

    ```
    Software Component A - Evaluation Complete  
    - Modular: Yes  
    - Platform Independent: Yes  
    - Documentation Available: Yes  
    - Licensing Confirmed: Yes  
    - Reuse Readiness Level: RRL 5
    ```
* **Reuse Readiness Level (RRL) Assessment**:

  + Evidence that the reusable software components meet relevant RRL benchmarks (e.g., RRL 4 or higher). Include documentation that explains level determination, such as testing results, portability assessments, and documentation reviews.
  + Example: "Software X meets RRL 5. It has modularity, full documentation, and verification in a relevant simulation environment."

### **2. Evidence of Documentation**

Demonstrates that reusable software is properly documented, addressing key usability and metadata requirements.

#### **Artifacts**:

* **Documentation Package**:

  + Includes all required documentation fields:
    - Software Title.
    - Software Description.
    - Programming Languages Used (e.g., Python, C++).
    - Licensing and Permissions (e.g., third-party components with licenses maintained).
    - Civil Servant Technical Point of Contact (POC).
    - Release Notes summarizing software functionality and known limitations.
* **README file or User Guide**:

  + Contains setup instructions, operating instructions, and technical descriptions. Should be part of the software package, either as a standalone file (e.g., [README.md](http://README.md)) or as embedded documentation within the project repository.

Examples:

**[README.md](http://README.md)**:

`**Title**: Data Processing Tool for Satellite Telemetry`

`**Purpose**: Cleans satellite telemetry data for further analysis.`

`**POC**: Jane Doe, NASA GSFC`

`**Programming Language**: Python`

`**Dependencies**: Requires NumPy and Pandas libraries (BSD licenses).`

`**Release Notes**: Version 1.2 fixes known issues with time-series data filtering.`

**3. Evidence of Licensing and Intellectual Property Compliance**

Demonstrates that intellectual property rights, licensing, and permissions have been validated.

**Artifacts**:

> ```
>
> ```

* **Third-Party Software Inventory**:

  + A document listing all third-party libraries/code included in the software, along with their licenses and corresponding URLs or references to license files.
  + Example:

    ```
    Dependencies for Software Y:  
    - Library 1: NumPy (BSD License) - https://numpy.org/license.html  
    - Library 2: Matplotlib (MIT License) - https://matplotlib.org/stable/users/license.html
    ```
* **IPR Verification Report**:

  + Evidence the software and all included components comply with NASA, government, and third-party licensing policies.
  + Example content: "All third-party components used in Software X are approved for government use under permissive licensing agreements (BSD or MIT)."

### **4. Evidence of Testing and Validation**

Demonstrates that reusable software has been tested and validated in its intended environments and operates reliably.

#### **Artifacts**:

* **Verification and Validation Test Results**:

  + Includes functional testing, interface testing, and simulations performed on reusable software.
  + Highlights evidence that the software can be integrated into other systems with minimal risk.
  + Example: "Software Z passed integration tests with NASA’s telemetry processing systems without errors during execution in simulated environments."
* **Test Coverage Report**:

  + Document showing which software features, modules, and integrations have been tested and validated.
  + Example content:

    ```
    Test Coverage Results:
    - Core Algorithm: PASSED (100% coverage at boundary conditions).
    - Input Parsing Module: PASSED (95% coverage of valid inputs).
    ```

### **5. Evidence of Submission to NASA Repositories**

Demonstrates that reusable software has been submitted to the appropriate NASA systems and repositories for sharing and potential reuse.

#### **Artifacts**:

* **Submission Record from NASA Internal Sharing and Reuse System**:
  + A log or confirmation entry proving that reusable software has been submitted. This can include:
    - Submission date.
    - Metadata fields.
    - Repository link or confirmation email.
  + Example:

    ```
    Submission Confirmation for Software Y:  
    - Title: Orbital Calculation Tool  
    - Description: Calculates planetary orbits based on gravitational inputs.  
    - Submitted on: 2023-06-20  
    - Repository Link: https://software.nasa.gov/internal-shared/orbit-tool  
    - Submitted by: John Smith, NASA JPL
    ```

### **6. Evidence of Software Metrics Tracking**

Demonstrates that reuse-related metrics have been tracked and analyzed for improvement.

#### **Artifacts**:

* **Metric Reports**:
  + Metrics tracked as part of project software assurance efforts, such as:
    - Number of reusable products identified vs. total products developed.
    - Number of reusable products submitted to NASA repositories.
  + Example Metrics Content:

    ```
    Project Metrics Report:
    - Total Developed Products: 12  
    - Products Submitted for Reuse: 6 (50%)  
    - Products Successfully Entered into NASA Sharing System: 5
    ```

### **Objective Evidence Checklist for Compliance with Requirement 3.10.2**

| **Evidence Type** | **Description** |
| --- | --- |
| Reuse Evaluation Report | Details software reuse eligibility (modularity, testing results, etc.). |
| Documentation Package | Includes required metadata fields (title, description, languages used, etc.). |
| Third-Party Software Inventory | Documents third-party licenses and permissions for reuse eligibility. |
| Verification & Validation Results | Proof that reusable software meets functional and integration requirements. |
| NASA Repository Submission Record | Confirmation and details of reusable software entered into NASA databases. |
| Metrics Report | Tracks submission rates and reuse eligibility statistics. |
