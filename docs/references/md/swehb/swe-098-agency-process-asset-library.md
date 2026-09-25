# SWE-098 - Agency Process Asset Library

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695483. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library

SWE-098 - Agency Process Asset Library

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695483)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695483&showCommentArea=true&showComments=true#addcomment)

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

2.1.1.6 The NASA OCE shall maintain an Agency-wide process asset library of applicable best practices and process templates for all size projects.  

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-098 History

SWE-098 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.5.1 The NASA Headquarters' Office of the Chief Engineer shall maintain an Agency-wide process asset library of applicable best practices. |
| Difference between A and B | No change |
| B | 2.1.1.6 The NASA OCE  shall maintain an Agency-wide process asset library of applicable best practices. |
| Difference between B and C | No change |
| C | 2.1.1.6 The NASA OCE shall maintain an Agency-wide process asset library of applicable best practices. |
| Difference between C and D | Added process templates to this. |
| D | 2.1.1.6 The NASA OCE shall maintain an Agency-wide process asset library of applicable best practices and process templates for all size projects. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The adoption of the NASA Engineering Network (NEN) Software Engineering Community of Practice site for NASA users promotes the continued development of strong engineering culture. The development, capture, and dissemination of software engineering best practices, examples, and lessons learned through the use of the NEN Software Engineering Community of Practice enable continuous improvement among the software engineers. The assignment of this responsibility to the Office of the Chief Engineer (OCE) assures that relevant software engineering assets and guidance materials are made available to the NASA Software Engineering community.   Funding for and maintenance of the NEN Software Engineering Community of Practice site is provided by the OCE, thus making it independent of Center and project resources.  Centers and projects still have a responsibility to utilize and occasionally share assets via the NEN Software Engineering Community of Practice site.

The establishment and maintenance of an Agency-wide Process Asset Library (PAL) for best practices and process templates are essential for ensuring the consistency, reliability, and efficiency of software engineering efforts across all NASA projects, regardless of size or scope. Below is a detailed rationale for why this requirement is vital to NASA's successful software engineering and project execution.

### 1. Promotes Consistency Across NASA Centers

NASA comprises multiple Centers that often operate independently on diverse projects. Without a centralized repository of best practices, processes, and templates, each Center risks developing its own processes, leading to inconsistencies across the agency.

* **Rationale Overview:** Maintaining an Agency-wide PAL ensures all Centers have access to standardized, vetted practices that align with NASA policies and standards (e.g., NPR 7150.2 [083](#_tabs-<p></p>), NASA-STD-8739.8 [278](#_tabs-<p></p>)). This provides a common foundation for software engineering and assurance, enforcing consistency and reducing variability in processes.
* **Impact:** Consistent software processes ensure that quality expectations are met across all projects, irrespective of mission size or complexity. For example, a small CubeSat project will follow the same quality assurance principles as a more complex mission like Artemis.

### 2. Facilitates Process Tailoring for All Project Sizes

NASA undertakes projects ranging from small-scale research experiments to large-scale, multi-billion-dollar human space exploration missions. The PAL facilitates the tailoring of processes and templates to ensure projects are using appropriate practices that match their needs and resources.

* **Rationale Overview:**  
  The PAL provides scalable process frameworks designed for each classification of projects, following NASA's software classification system (Class A to Class F). Smaller, lower-risk projects can adopt lightweight versions of the templates, while higher-complexity missions require more comprehensive processes.
* **Impact:**  
  Encouraging process tailoring ensures that projects do not waste resources implementing overly rigorous processes for small efforts or, conversely, applying insufficient rigor to large, mission-critical efforts. This approach increases efficiency while adhering to quality and safety requirements.

### 3. Promotes Reuse of Proven Practices

NASA projects often require high reliability and quality, but past projects have repeatedly encountered similar challenges. The PAL provides a structured way to capture and disseminate proven best practices and reusable process assets from previous missions.

* **Rationale Overview:**  
  By curating process templates and lessons learned, NASA avoids the need to reinvent the wheel for new projects. Engineers can leverage the PAL for resources like:
  + Testing templates for flight software.
  + Risk management frameworks.
  + Safety-critical design checklists.
  + Secure software development practices.
* **Impact:**  
  Reusing established processes accelerates development, reduces costs, and lowers risks for future missions by ensuring teams can build upon what has worked successfully in the past.

### 4. Enables Knowledge Sharing Across Diverse Teams

NASA project teams are often composed of engineers, scientists, systems analysts, and assurance personnel from various roles and disciplines. The PAL serves as a collaborative knowledge-sharing platform that fosters cross-disciplinary alignment.

* **Rationale Overview:**  
  Providing well-organized and centrally accessible process assets ensures that all team members—regardless of their discipline or Center—can effectively collaborate around shared NASA-wide practices. This improves communication, accountability, and integration across diverse roles.
* **Impact:**  
  Processes shared through the PAL enable smoother collaboration in multi-Center and multi-disciplinary missions, reducing miscommunication and fostering technical coherence.

### 5. Enhances Compliance with NASA Policies and Standards

NASA software development must comply with NPR 7150.2 requirements and other regulatory standards. Without centralized process templates, there is a risk of misinterpretation or inconsistent application of these policies across projects.

* **Rationale Overview:**  
  An Agency-wide PAL ensures that all software engineers and assurance personnel have access to templates designed explicitly to comply with NASA requirements. This eliminates ambiguity in implementing standards and ensures that all workflows fulfill compliance obligations.
* **Impact:**  
  By aligning processes with established policies, projects reduce nonconformance findings during audits and reviews, achieve performance objectives more reliably, and avoid costly disruptions caused by deviations from requirements.

### 6. Improves Efficiency and Reduces Costs

The PAL consolidates software engineering resources, eliminating duplicated effort when designing processes for new projects. Teams can focus their energy on mission execution rather than spending valuable time designing processes and templates from scratch.

* **Rationale Overview:**  
  The PAL reduces inefficiencies by providing ready-to-use templates and processes, optimized for varying project types. Process libraries simplify onboarding activities and help team members quickly adopt proven approaches.
* **Impact:**  
  Smaller projects especially benefit from this centralized library because they often lack the resources to develop bespoke processes internally. Reduced effort in process development translates directly into cost savings and faster project mobilization.

### 7. Captures Lessons Learned for Continuous Improvement

NASA endeavors to continually improve software engineering practices and leverage lessons from past successes and failures. The PAL serves as the central repository for institutional knowledge in software engineering.

* **Rationale Overview:**  
  The PAL includes contributions from lessons learned through the NASA Lessons Learned Information System (LLIS). By incorporating these insights, the PAL evolves to address challenges encountered in prior missions. For example:
  + Implementing better testing guidelines to address historical gaps in V&V.
  + Including cybersecurity templates to mitigate increasing risks.
* **Impact:**  
  Projects that use updated PAL templates benefit immediately from refined processes, reducing the likelihood of repeating past mistakes.

### 8. Supports Training and Workforce Development

The success of NASA's software engineering efforts depends on the skills of its workforce. The PAL serves as a teaching resource for engineers and assurance personnel by providing examples of well-documented processes and templates.

* **Rationale Overview:**  
  Engineers across NASA can study the process assets in the PAL to better understand their role in the software life cycle, build familiarity with best practices, and apply them to their work. Incorporating PAL resources ensures that training aligns closely with real-world practices used in NASA projects.
* **Impact:**  
  Providing training tied to the PAL reinforces consistency across projects and enhances workforce competency in applying the defined processes.

### 9. A Standardized Platform for Process Innovation

NASA continues to push the boundaries of engineering innovation. As new techniques, tools, and methodologies are introduced, the PAL allows NASA to standardize innovations quickly across Centers.

* **Rationale Overview:**  
  Adding innovative processes to the PAL (e.g., DevOps workflows, model-based systems engineering [MBSE] templates, or AI-driven assurance techniques) allows new practices to proliferate across the agency. This ensures all projects benefit from cutting-edge developments.
* **Impact:**  
  Standardizing innovation through the PAL ensures the agency remains at the forefront of software engineering excellence.

### 10. Ensures Scalability for Future NASA Missions

As NASA tackles increasingly complex missions, the PAL ensures that scalable processes are consistently available for new projects, including collaborations with commercial entities, international organizations, and academia.

* **Rationale Overview:**  
  The PAL can scale without losing quality, allowing NASA to maintain control over engineering rigor even as mission complexity grows. This is especially important for collaborative commercial space programs (e.g., Artemis Program partnerships) that benefit from NASA’s proven processes.
* **Impact:**  
  A centralized PAL ensures future missions—no matter their scale—have immediate access to NASA's engineering expertise.

### 11. Aids in Risk Mitigation

Risk management is crucial for NASA projects, and lack of established processes often introduces unnecessary uncertainty.

* **Rationale Overview:**  
  Providing reusable risk assessment frameworks, checklists, and mitigation strategies in the PAL ensures that mission-critical and safety-critical risks are adequately addressed throughout the project lifecycle.
* **Impact:**  
  Using predefined processes directly contributes to reducing programmatic, technical, and operational risks across all software projects.

### Conclusion

The establishment of an Agency-wide Process Asset Library by the NASA OCE is essential for ensuring consistency, facilitating process tailoring, supporting collaboration, preserving institutional knowledge, promoting innovation, reducing costs, and improving risk management across all software projects—regardless of size or complexity. This requirement aligns with NASA's goals of increasing efficiency, enhancing compliance, and maintaining technical excellence in software engineering. A centralized PAL ultimately empowers NASA’s workforce to deliver high-quality, reliable, and cost-effective software systems for future missions.

# 3. Guidance

## 3.1 Introduction

Software engineering is a fundamental capability and an enabling technology for achieving NASA's diverse range of missions, from space exploration to Earth science and supporting infrastructure. Given the complexity and criticality of software development in these efforts, NASA's software engineering community focuses on strong discipline-wide practices to deliver high-performing, reliable, and safe software. The community leverages curated resources, shared knowledge, collaborative problem-solving, and innovative tools to uphold software engineering excellence across the agency.

The **[NASA Engineering Network (NEN) Software Engineering Community of Practice (CoP)](https://nen.nasa.gov/web/nen) [043](#_tabs-<p></p>)** functions as the central platform for NASA's software engineering discipline, providing an interactive environment where NASA engineers can engage, collaborate, and enhance their expertise. The NEN site is an essential repository, supporting the Agency's effort to facilitate process asset sharing, distribute best practices, and ensure continued growth in software engineering capabilities.

This guidance outlines the role of the NEN Software Engineering Community of Practice, the resources it provides, and how it strengthens the software engineering culture and practices across NASA.

## 3.2 Software Engineering Community of Practice

### 3.2.1  Purpose of the NEN Software Engineering Community of Practice

The NEN Software Engineering Community of Practice (CoP) supports the NASA workforce by serving as:

* A centralized repository of software engineering assets for best practices, process templates, training resources, tools, metrics, and guidelines.
* A collaborative network that reduces organizational silos and encourages knowledge sharing, peer interaction, and collective problem-solving.
* An enabling platform for ongoing learning and adaptation to emerging software engineering challenges, technologies, and methodologies.

NASA’s Office of the Chief Engineer (OCE) actively curates the CoP resources to ensure relevance, accessibility, and alignment with agency-wide policies and standards such as NPR 7150.2 [083](#_tabs-<p></p>) and associated NASA Software Engineering Standards. The CoP provides structured and intuitive access to information, helping software engineers perform their roles more effectively.

### 3.2.2 Key Components of the NEN Software Engineering Community of Practice

1. **Knowledge Sharing and Collaboration**
   * The CoP is a distributed, peer-driven online network of individuals, designed to foster the sharing of collective knowledge across disciplines.
   * Community members participate in active discussions, share lessons learned, and develop or refine best practices collaboratively.
   * The platform provides NASA personnel across centers with exposure to a broader range of expertise, viewpoints, and lessons—connecting individuals working on both small-scale and large-scale missions.
2. **Comprehensive Software Engineering Resources**
   * The CoP hosts **Agency-wide process assets** organized into an intuitive structure. Assets are searchable and curated to address the needs of NASA software engineers at different stages of the project life cycle.
   * Resources available on the platform include:
     + **Process templates** for software planning, requirements, design, testing, and assurance.
     + **Best practices** documented from past projects and lessons learned.
     + **Checklists and worksheets** for compliance, verification, validation, and assurance reviews.
     + **Tools and software catalogs** to aid in development and management.
     + **Metrics repositories** to guide process assessment and improvement.
     + **Course materials and training** to ensure continuous workforce development.
     + **Reports, presentations, and handbooks** that consolidate knowledge and guidance from across the agency.
3. **Access to Industry Trends and Research**
   * The CoP provides software engineers with curated insights into emerging industry trends, such as:
     + Model-Based Systems Engineering (MBSE).
     + Agile and DevOps practices tailored to NASA's systems.
     + Secure software development standards and methodologies.
     + AI/ML software engineering techniques.
   * Research findings and case studies are regularly updated to encourage the adoption of innovative technologies while ensuring alignment with NASA’s rigorous quality and safety expectations.
4. **Open, Collaborative Problem-Solving**
   * The CoP fosters a culture of trust and mutual assistance by creating opportunities for members to discuss common challenges and explore potential solutions collectively. Members can submit questions, share project-specific issues, and receive advice from their peers and subject matter experts across Centers.

### 3.2.3  How the CoP Benefits NASA’s Software Engineering Efforts

The NEN Software Engineering Community of Practice provides significant value to NASA’s software engineering practice by:

1. **Centralizing Best Practices and Reducing Duplication**
   * The OCE-managed CoP ensures NASA Centers and projects have access to unified and vetted process templates, preventing the development of redundant or inconsistent processes.
   * By capturing proven approaches used in previous missions, the repository allows engineers to reuse high-quality practices that save time and reduce project risk.
2. **Supporting Project Tailoring**
   * Templates and guidance in the CoP are designed with flexibility, enabling team leads to tailor processes for different project classifications (e.g., small projects, Class D, to large human-rated missions, Class A).
   * Small projects benefit from lightweight, streamlined templates and processes that avoid excessive overhead while maintaining rigor.
3. **Promoting Compliance with NASA Standards**
   * Process templates and checklists in the CoP are aligned with key NASA requirements, such as NPR 7150.2, NPR 7123.1 [041](#_tabs-<p></p>), and NASA-STD-8739.8 [278](#_tabs-<p></p>).
   * By using the resources available in the CoP, engineers can simplify compliance workflows and ensure adherence to NASA-wide standards.
4. **Enhancing Workforce Competency**
   * The CoP supports formal training by providing learning materials and access to self-paced courses that improve the skills of NASA software engineers.
   * As the software engineering field evolves, the CoP ensures that NASA personnel remain current on new tools, techniques, and practices.
5. **Encouraging Cross-Center Collaboration**
   * Engineers across different NASA Centers can interact, share expertise, and align their work using the CoP, reducing the separation between Centers and fostering greater unity in software engineering practices.

### 3.2.4  Capabilities of the NEN Software Engineering CoP

The CoP is built around key capabilities that enable it to serve its users effectively:

1. **Intuitive Search and Hierarchical Organization**
   * Resources in the CoP are indexed and searchable by topic, ensuring users can quickly locate the desired information, whether they need handbooks, tools, or best practices.
2. **Dynamic Resource Updates**
   * To stay relevant, the OCE regularly updates the CoP contents with new resources, including examples from recent projects, research findings, and emerging industry trends.
3. **Collaboration Opportunities and Events**
   * In addition to the asset repository, the CoP hosts virtual discussions, forums, and webinars that connect engineers with thought leaders in software engineering disciplines.
4. **Agency-Wide Accessibility**
   * The CoP is accessible across NASA, ensuring engineers in all Centers benefit from a shared pool of resources, templates, and expertise.
5. **Secure, NASA-Only Access**
   * While the resources in the CoP are invaluable for internal use, the CoP is only accessible to NASA personnel. This ensures the quality and confidentiality of resources supporting mission-critical efforts.

### 3.2.5  Future Goals for the CoP and Agency Collaboration

The OCE aims to continuously expand and improve the CoP, ensuring that it meets the evolving needs of NASA and its workforce. Key goals include:

* Enhancing resource depth by linking the CoP with datasets from NASA’s Lessons Learned Information System (LLIS) and mission archives.
* Expanding resources for new and emerging disciplines like autonomous systems, AI-driven software development, and edge computing.
* Promoting the CoP further across Centers to expand participation and contributions.

### 3.2.6  Conclusion

The NASA Engineering Network (NEN) Software Engineering Community of Practice is a cornerstone of NASA’s software engineering discipline. Its centralized repository of best practices, coupled with collaborative tools, training materials, and knowledge-sharing opportunities, empowers NASA engineers at all Centers to adopt consistent, reliable, and innovative processes that support mission success. By maintaining and continuously optimizing this platform, the OCE ensures that NASA's software community has the resources needed to tackle increasingly complex challenges while meeting the agency's high standards for safety, quality, and performance.

See also [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans).

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small NASA projects often operate under constraints such as limited budgets, reduced personnel, and shorter timelines. These constraints, however, do not exempt small projects from the need to meet software requirements, ensure quality, manage risks, and adhere to agency-wide standards. The Process Asset Library (PAL) maintained by the OCE is specifically tailored to provide resources that support the unique needs of small projects alongside larger efforts. Below is guidance on how small projects can effectively utilize the PAL to meet this requirement.

## 4.1 Guidance for Small Projects

### 4.1.1  Purpose of the Guidance for Small Projects

The goal of this guidance is to enable small projects to:

1. Leverage the Process Asset Library (PAL) to streamline operations and avoid "reinventing the wheel."
2. Tailor the processes, templates, and best practices to their scale and classification.
3. Meet NASA standards (e.g., NPR 7150.2 [083](#_tabs-<p></p>) compliance) without unnecessary overhead.
4. Optimize resources by maximizing the utility of pre-developed and proven assets.

### 4.1.2  Characteristics of Small Projects at NASA

Small projects may include, but are not limited to:

* CubeSat missions or other small satellite projects.
* Low-cost research and development (R&D) initiatives.
* Software tools that support operations, data analysis, or simulations.
* Prototyping efforts for proof-of-concept software systems.
* Class C, D, or F software under NPR 7150.2 (non-human-rated, lower criticality).

These projects focus on delivering results under tight constraints while minimizing risks, which makes efficiency a critical success factor.

## 4.2  Guidelines for Leveraging the Agency-Wide Process Asset Library (PAL)

### 4.2.1  Identify and Use Lightweight Templates and Processes

The PAL contains processes, best practices, and templates designed for different project sizes, ensuring scalability for small projects. For small projects:

* **Tailor the resources to fit project scope:**  
  Use scalable templates for software requirements, design, and testing that align with the reduced complexity of small systems. For example:
  + Simplified **Software Development Plans** (SDPs).
  + Lightweight **Requirements Traceability Matrices** (RTMs).
  + Streamlined **Risk Management Plans** tailored to small teams.
  + Sample process flows and lifecycle diagrams for rapid software development.
* **Focus on minimal compliance:**  
  Small projects should focus on adhering to core requirements like safety, risk management, and verification, while skipping unnecessary documentation or overly complex processes.

### 4.2.2  Access Predefined Best Practices

* **Software Assurance:**  
  Small projects still require assurance processes to mitigate failure risks. The PAL includes checklists, handbooks, and process flows for core assurance activities that are right-sized for your project.
* **Testing Practices for Resource-Constrained Projects:**  
  Utilize existing testing templates for unit testing, system validation, and integration testing. For cost efficiency, small projects can adopt a risk-based testing approach (focusing on the most critical areas).
* **Programming and Coding Standards:**  
  The PAL includes code writing guidelines, such as secure coding principles and best practices, that can help small teams ensure maintainability and reliability with relatively low effort.

### 4.2.3  Focus on Reuse of Proven Processes

* **Learn from Other Small Projects:**  
  The PAL includes lessons learned, sample workflows, and successful process adaptations that were implemented in other small NASA projects. These assets can directly inform your project's strategies.
  + Example: Adopt a DevOps-based development model used successfully on a CubeSat project to speed up delivery timelines.
* **Use Established Tools and Techniques:**  
  The PAL provides recommendations for tools and methods designed for small projects, such as open-source software tools for configuration management (e.g., GitHub) or testing frameworks (e.g., JUnit).

### 4.2.4  Leverage Risk Management Resources

* Even though small projects have fewer resources, risk management should remain a priority:
  + Utilize checklists tailored for small projects from the PAL to identify high-priority risks.
  + Focus effort on addressing mission-critical risks or high-probability issues.
  + Use lightweight templates for risk monitoring and mitigation planning (e.g., a simple spreadsheet-based or Agile issue tracker).

### 4.2.5  Prioritize Knowledge Sharing and Collaboration

* Collaborate with peers in the **[NEN Software Engineering Community of Practice (CoP)](https://nen.nasa.gov/web/nen) [043](#_tabs-<p></p>)**:  
  Small project teams can connect with other teams working on similar-sized projects through the NEN platform to share solutions, work through challenges, or identify reusable resources. Discussions can include topics like lightweight testing, efficient requirement management, and compliance simplification.
* Submit feedback to improve PAL resources:  
  Small projects can contribute their tailored templates and lessons learned to the PAL for future use by others, ensuring continuous improvement of agency-wide resources.

## 4.3. Tailoring Resources for Small Projects

The following examples illustrate how small projects might tailor specific PAL resources to suit their size and scope:

### Case A: Developing a CubeSat Control Software

* **Complexity:** Moderate; software aims to control satellite actuators and sensors in low-Earth orbit, but the mission is low-risk (Class D).
* **PAL Resources Used:**
  + **Simplified SDP template:** Reduce unnecessary documentation sections (e.g., no need for overly detailed design decisions; focus on interfaces).
  + **Unit testing templates:** Leverage prebuilt unit and integration testing templates for hardware/software interaction validation.
  + **Risk management:** Focus on high-severity risks like actuator failures during deployment while skipping low-impact risks.
* **Outcome:** Compliance with NPR 7150.2 while maintaining lightweight operations and fast development cycles.

### Case B: Data Analytics Tool for Mission Support

* **Complexity:** Low; software provides visualization to assist scientists in analyzing Earth observation data.
* **PAL Resources Used:**
  + **Requirements templates:** Adopt simplified templates for software requirements capturing, like user stories or Agile epics.
  + **Code standards:** Use open-source Python code standards from the PAL.
  + **Configuration management:** Rely on a checklist with simplified processes for version control.
* **Outcome:** The team delivers a tool on time without excessive process overhead, ensuring reusable code for future analytics projects.

## 4.4 Training from the Process Asset Library

* **Role-Specific Training:** Small project leads and engineers can use training materials (e.g., videos, presentations, and checklists) available in the PAL to quickly gain familiarity with essential processes for planning, development, and assurance.
* **Workshops/Webinars for Small Projects:** Use the NASA Engineering Network (NEN) to participate in webinars or small-group coaching sessions focused on applying lessons learned or adapting best practices for small-scale efforts.

## 4.5 Benefits of Using the PAL for Small Projects

* **Efficiency Gains:** Proven processes and templates save time and effort.
* **Cost Reduction:** Reuse of agency-wide assets minimizes the need to develop processes from scratch.
* **Improved Quality and Assurance:** Standardized templates ensure critical areas like safety assurance and risk management are not overlooked.
* **Faster Compliance:** Pre-developed resources are aligned with NASA standards, reducing the time required to achieve compliance.

## 4.6 Summary of Key Actions for Small Projects

1. **Start with the PAL:** Visit the NEN Software Engineering Community of Practice to identify the resources most applicable to your project’s size and needs.
2. **Tailor Appropriately:** Focus on adapting processes and templates for lightweight use while ensuring compliance with requirements.
3. **Leverage Knowledge Sharing:** Engage with the broader software engineering community to learn from similar projects.
4. **Contribute Back:** Share any small-project-specific lessons learned or innovations with the PAL to improve future resources.

## 4.7 Conclusion

The Process Asset Library (PAL) provides small NASA projects with the tools and resources needed to streamline operations, adhere to standards, manage risks, and deliver reliable software within tight constraints. By tailoring and leveraging the PAL effectively, small project teams can achieve mission success while minimizing costs, effort, and time.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-043)

  [NASA Engineering Network Communities of Practice.](https://nen.nasa.gov/web/nen "Click to open in new window")

  NASA Engineering & Safety Center. Retrieved October, 2025 from https://nen.nasa.gov/web/nen.
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-117)

  [2018 NASA Strategic Plan,](https://nodis3.gsfc.nasa.gov/npg_img/N_PD_1001_000C_/N_PD_1001_000C__main.pdf "Click to open in new window")

  NPD 1001.0C, NASA Office of Office of the Chief Financial Officer, 2018.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-261)

  [NASA Governance and Strategic Management Handbook,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=0C "Click to open in new window")

  NPD 1000.0C, NASA Governance and Strategic Management Handbook, Effective Date: January 29, 2020, Expiration Date: January 29, 2025
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA has benefited significantly from lessons learned during prior missions, particularly with respect to software engineering and process improvement. Maintaining and utilizing a centralized Process Asset Library (PAL) aligns with these lessons and addresses key challenges identified in past projects. Below are several relevant lessons learned from [NASA’s Lessons Learned Information System (LLIS)](https://llis.nasa.gov/) **[439](#_tabs-<p></p>)** that support the rationale for this requirement.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. The Importance of a Centralized Repository for Process Assets

* **LLIS Reference:** *Mars Climate Orbiter Mishap* (LLIS-1900)
* **Summary of Incident:**  
  The Mars Climate Orbiter mission failed due to a navigation error caused by the usage of incompatible units in the software—pounds-force seconds instead of newton-seconds. This serious oversight was not caught because there was no formal, centralized process for enforcing best practices in requirements verification, unit management, and system testing.
* **Lesson Learned:**  
  A centralized repository of best practices, checklists, and lessons learned is critical to ensuring teams across NASA consistently apply proven engineering and software assurance processes.
* **Relevance to Requirement:**  
  The OCE's Process Asset Library (PAL) can act as a tool to standardize key practices, including those for requirements verification processes and reducing systemic risks caused by oversight or miscommunication.

#### 2. Reusing Proven Practices and Templates Saves Time

* **LLIS Reference:** *Apollo Program Resource Management* (LLIS-1400)
* **Summary of Observation:**  
  The success of the Apollo program was enabled, in part, by the reuse and adaptation of processes originally developed for earlier spacecraft projects like Gemini. By standardizing and reusing these assets, NASA saved significant time and effort while improving reliability.
* **Lesson Learned:**  
  Reuse of proven processes ensures efficiency and reliability, especially in time-sensitive and resource-limited projects.
* **Relevance to Requirement:**  
  The PAL supports resource-constrained projects by enabling teams to utilize predeveloped templates, checklists, and tools designed for success. This eliminates the need for teams to "start from scratch."

#### 3. Tailoring Processes for Small Projects

* **LLIS Reference:** *Challenges in Small Spacecraft Missions* (LLIS-2257)
* **Summary of Issue:**  
  A NASA small satellite project encountered challenges with applying the same level of process rigor used for large, high-criticality missions. The team lacked access to lightweight versions of process templates and struggled to appropriately tailor the standards, causing both delays in development and avoidable noncompliance issues.
* **Lesson Learned:**  
  Process tailoring is essential to ensure that small projects meet NASA standards without unnecessary overhead. A central repository for scalable templates designed specifically for small projects can help improve efficiency and focus effort on mission-critical tasks.
* **Relevance to Requirement:**  
  The PAL ensures that projects across the classification spectrum (including small missions) have access to right-sized templates and guides, simplifying compliance while reducing unnecessary effort.

#### 4. Consistent Application of Standards Across Projects

* **LLIS Reference:** *Inconsistent Software Practices Across Centers* (LLIS-1720)
* **Summary of Issue:**  
  Discrepancies in how different NASA Centers implemented NPR 7150.2 [083](#_tabs-<p></p>) software requirements led to inconsistent quality levels across projects. Certain teams lacked consistent process guidance and relied on ad hoc approaches, increasing the risk of defects and late-stage rework.
* **Lesson Learned:**  
  Establishing a centralized process library ensures uniformity and compliance with NASA software standards across all Centers. This reduces variability in quality and enables smoother collaboration on multi-Center projects.
* **Relevance to Requirement:**  
  The PAL mitigates the risk of inconsistent practices by providing shared, Agency-approved templates and assets accessible to all Centers.

#### 5. Lessons Learned on Software Risks

* **LLIS Reference:** *Software Assurance Neglect and Mission Risk* (LLIS-1623)
* **Summary of Incident:**  
  On a major NASA project, software design issues went unnoticed until late in the development cycle because best practices in independent software assurance and risk monitoring were not enforced. This caused significant delays and cost overruns.
* **Lesson Learned:**  
  Software assurance best practices, such as V&V checklists and iterative risk reviews, should be integrated into processes starting from the early stages of development. Centralized resources can help enforce these practices.
* **Relevance to Requirement:**  
  The PAL acts as a repository for software assurance templates and assurance-related best practices, ensuring that all projects integrate risk prevention efforts early in the software lifecycle.

#### 6. Knowledge Sharing Reduces Rework and Mistakes

* **LLIS Reference:** *Hubble Space Telescope Spherical Aberration* (LLIS-0150)
* **Summary of Incident:**  
  A miscalculation during the manufacturing of the Hubble Space Telescope's mirror caused severe spherical aberration in its observations, resulting in the need for costly corrective measures post-launch. Better documentation and sharing of existing verification processes could have prevented the miscalculation.
* **Lesson Learned:**  
  A centralized repository for lessons learned, best practices, and processes can prevent teams from repeating errors made on previous projects, saving time and resources.
* **Relevance to Requirement:**  
  The PAL helps aggregate documentation, processes, and lessons learned, enabling teams to preemptively address potential errors through knowledge sharing.

#### 7. Streamlined Collaboration Using Shared Resources

* **LLIS Reference:** *International Space Station (ISS) Software Integration Challenges* (LLIS-2003)
* **Summary of Issue:**  
  Distributed teams working on ISS software integration faced significant challenges due to inconsistent use of tools and processes. This caused delays in integration and testing phases. If all teams had access to shared tools and templates, these challenges could have been mitigated.
* **Lesson Learned:**  
  Shared processes, tools, and templates are essential to ensuring successful collaboration between distributed teams. A central repository can enable distributed and cross-Center collaboration by providing access to common resources.
* **Relevance to Requirement:**  
  The OCE’s PAL facilitates collaboration and ensures all teams—regardless of location—operate using consistent and synchronized software engineering practices.

#### 8. Lessons on Long-Term Process Improvements

* **LLIS Reference:** *Continuous Process Improvement During Shuttle Program* (LLIS-0875)
* **Summary:**  
  The Space Shuttle program implemented a continuous improvement model where lessons learned from early missions were applied to refine processes over time. Institutionalizing these updates and sharing them across missions ensured long-term program success.
* **Lesson Learned:**  
  Process improvement should include mechanisms for constant feedback and iteration, with updates to processes shared across teams and projects.
* **Relevance to Requirement:**  
  The PAL allows the OCE to integrate emerging best practices and lessons learned into templates, ensuring NASA’s engineering practices continually evolve and improve.

#### 9. Scaling Innovation from Small Projects to Large Missions

* **LLIS Reference:** *Small-Scale Project Innovation Lessons* (LLIS-2108)
* **Summary of Issue:**  
  Innovations on small projects were not readily scaled or applied to larger missions due to the absence of standardized processes for transferring knowledge or sharing methodologies.
* **Lesson Learned:**  
  Centralized repositories should not only store standardized best practices but also serve as platforms for disseminating innovative solutions developed on smaller projects.
* **Relevance to Requirement:**  
  The PAL bridges the gap between small and large projects by capturing innovative practices from small efforts and making them accessible as scalable solutions for larger missions.

### 6.1.2  Conclusion

These lessons underscore the importance of maintaining an Agency-wide Process Asset Library (PAL) to improve consistency, reuse proven practices, and mitigate risks across NASA projects. The PAL supports knowledge sharing, avoids duplication of effort, and ensures that all teams—regardless of project size—can benefit from NASA’s institutional expertise in software engineering. By learning from past successes and failures, the OCE helps ensure future projects deliver reliable, high-quality results efficiently and effectively.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-098 - Agency Process Asset Library**

2.1.1.6 The NASA OCE shall maintain an Agency-wide process asset library of applicable best practices and process templates for all size projects.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

None identified at this time.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support oversight, validate compliance, manage risks, and ensure the quality of delivered products. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

No specific deliverables are currently identified.

## 7.3 Metrics

No standard metrics are currently specified.

## 7.4 Guidance

Software assurance (SA) at NASA plays a critical role in ensuring software reliability, safety, security, and compliance with mission requirements. It focuses on identifying and mitigating risks across the software lifecycle, thereby reducing the likelihood of defects, failures, or vulnerabilities that could negatively impact mission success.

To effectively support software assurance activities, the Process Asset Library (PAL) maintained by the OCE should provide a centralized hub of resources tailored to meet the assurance needs of NASA projects of all sizes. This guidance outlines how to implement software assurance effectively using the PAL and describes the key resources, processes, and best practices that teams should adopt to satisfy assurance requirements.

### 7.4.1  Role of the Process Asset Library in Software Assurance

The PAL supports software assurance in several ways:

1. **Centralized Resources**: It provides templates, checklists, lessons learned, and guidance for key assurance activities across the software lifecycle.
2. **Consistency Across Projects**: It ensures that assurance activities, regardless of project size or classification, align with NASA standards, such as NPR 7150.2 [083](#_tabs-<p></p>) and NASA-STD-8739.8 [278](#_tabs-<p></p>).
3. **Tailored Assurance for Mission Risk Levels**: It includes scalable assurance processes and allows tailored application for small, medium, and large projects.
4. **Efficiency and Reuse**: By providing predeveloped tools and practices, assurance teams can save time and resources while focusing on quality results.

### 7.4.2  Core Software Assurance Activities and PAL Support

Software assurance must be embedded throughout the entire software lifecycle, from planning to decommissioning, and focuses on reviewing, verifying, and validating all critical activities. Below are the core software assurance activities and how the PAL assists teams in implementing them:

#### A. Software Assurance Planning

* **Key Action:** Develop a Software Assurance Plan (SAP) that covers the scope, objectives, and methods for software assurance activities. (See [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan).)
* **PAL Resources:**
  + **SAP Templates:** Preconfigured templates aligned with NPR 7150.2, including simplified versions for small projects.
  + **Guidelines:** Recommended practices for tailoring assurance plans to project size, classification, and risk level.
* **Best Practice:** Use the PAL's SAP checklist to ensure coverage of critical areas like risk assessment, V&V (verification and validation), and software safety/security.

#### B. Requirements Verification and Validation (V&V)

* **Key Action:** Ensure that software requirements (functional, performance, and safety/security) are complete, unambiguous, and verifiable.
* **PAL Resources:**
  + **Requirements Verification Templates:** Tools to document traceability from requirements to test cases (e.g., simple Requirements Traceability Matrices [RTMs]).
  + **Assurance Checklists:** Assurance-specific validation checklists to verify that requirements reflect mission-critical quality, reliability, and safety standards.
* **Best Practice:** Engage assurance personnel early during requirements review to identify potential gaps and ambiguities.

#### C. Software Design Assurance

* **Key Action:** Assess software design for alignment with requirements, maintainability, extensibility, and risk identification.
* **PAL Resources:**
  + **Design Review Best Practices:** Guidelines for conducting formal Preliminary Design Reviews (PDRs) and Critical Design Reviews (CDRs) with assurance oversight.
  + **Checklists for Architecture Evaluation:** Tools to assess modularity, complexity, and potential single points of failure.
* **Best Practice:** Use PAL-provided checklists to perform a risk-based assurance review of safety-critical design elements, ensuring traceability to safety requirements.

#### D. Implementation Assurance (Code Quality)

* **Key Action:** Monitor coding and integration activities to ensure adherence to NASA’s coding standards and practices.
* **PAL Resources:**
  + **Coding Standards:** Resources aligned with NASA’s quality coding guidelines, addressing secure, maintainable, and reliable code practices.
  + **Static Analysis Tools:** Recommended open-source or Agency-proven tools (e.g., SonarQube, Coverity) with instructions on integrating them into workflows.
  + **Peer Review Checklists:** Templates for performing code reviews that address common defects, potential security issues, and maintainability concerns.
* **Best Practice:** Automate static code analysis through toolchains recommended in the PAL and validate adherence to coding standards via assurance-led periodic reviews.

#### E. Testing and Verification Assurance

* **Key Action:** Evaluate the adequacy of testing procedures and independently analyze test results to verify software functionality and risk mitigation.
* **PAL Resources:**
  + **Testing Templates:** Readily available test plans and procedures, tailored for different scales of projects.
  + **Risk-Based Test Planning Frameworks:** Lightweight frameworks that prioritize testing for the most critical risk areas.
  + **Defect Tracking Tools:** Tools and templates to log, track, and resolve defects during testing.
* **Best Practice:** Include assurance personnel in all test planning phases, and ensure independent test coverage verification for critical mission functions.

#### F. Risk Management and Assurance

* **Key Action:** Identify, track, and ensure mitigation of risks associated with software development, implementation, and deployment.
* **PAL Resources:**
  + **Risk Assessments Templates:** Templates for documenting identified risks, probability, impact, and mitigation strategies.
  + **Lessons Learned Database Links:** Access information on historical software assurance risks and how they were mitigated.
* **Best Practice:** Use PAL-provided risk management checklists to prioritize risks based on likelihood and impact, and keep assurance integrated into risk monitoring.

#### G. Safety Assurance

* **Key Action:** Identify, analyze, and ensure mitigation of safety risks associated with software systems, especially in safety-critical areas.
* **PAL Resources:**
  + **Hazard Analysis Templates:** Focused analysis tools and workflows for identifying software-related hazards.
  + **Safety-Critical Identification Tools:** Standards for recognizing parts of the codebase that interact with safety-critical components.
* **Best Practice:** Focus early effort on identifying and mitigating safety-critical software elements to reduce downstream rework.

#### H. Software Security Assurance

* **Key Action:** Ensure that software is designed and implemented to address cybersecurity vulnerabilities and threats.
* **PAL Resources:**
  + **Secure Coding Templates:** Guidelines on prevention of vulnerabilities like buffer overflows and SQL injection.
  + **Security Testing Tools:** Recommended tools for penetration testing and static/dynamic security analysis.
  + **Checklists for Cybersecurity Practices:** A security-first checklist based on NASA and industry standards.
* **Best Practice:** Incorporate security reviews into every software milestone and validate that every software assurance process includes security considerations.

#### I. Maintenance and Sustainment Assurance

* **Key Action:** Oversee the post-deployment lifecycle of software, including updates, patches, and decommissioning processes.
* **PAL Resources:**
  + **Maintenance Assurance Plans:** Guidance for ensuring that any changes made during sustainment follow validated processes.
  + **Configuration Management Templates:** Documents for tracking and monitoring software changes over its operational lifecycle.
* **Best Practice:** Keep assurance staff engaged during proposed updates to prevent functional and security regressions.

### 7.4.3. Key Assurance Features of the Process Asset Library

The PAL helps assurance activities by providing:

1. **Tailored Templates for Each Project Size**: Adaptable tools for large and small projects alike.
2. **Authority Documents and References**: Assurance guidelines mapped explicitly to NASA directives (e.g., NPR 7150.2, NASA-STD-8739.8).
3. **Lessons Learned and Case Studies**: Insights into past assurance challenges and how they were resolved.
4. **Reusable Tools**: Easy-to-implement checklists for V&V, code reviews, and risk reviews.
5. **Scalability for Risk Levels**: Resources for high-criticality Class A missions as well as simpler Class D/F projects.

### 7.4.4  Assurance Considerations for Small Projects

For small projects, it’s critical to:

* **Focus on Scalable Assurance Processes:** Use PAL resources like lightweight V&V processes and risk-based assurance plans to stay efficient.
* **Adopt Prebuilt Tools:** Avoid developing new assurance templates by using tools in the repository.
* **Emphasize Risks Over Rigor:** Prioritize critical assurance activities for high-risk areas while reducing unnecessary documentation on non-critical workflows.

### 7.4.5  Training and Continuous Improvement in Software Assurance

The OCE, through the PAL, offers resources that promote continuous improvement in software assurance, such as:

* Training courses on V&V, configuration management, and code reviews.
* Webinars and workshops that address common assurance challenges.
* Timely updates to best practices in response to lessons learned from ongoing projects.

### 7.4.5  Conclusion

The Process Asset Library (PAL) is an essential resource for facilitating effective software assurance at NASA. By providing structured, scalable assurance resources, the PAL ensures standardized quality and risk management across all projects. Small and large teams alike benefit from reusable tools, checklists, and expertise that help them integrate assurance throughout the software lifecycle, contributing significantly to mission success.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) |
