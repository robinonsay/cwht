# SWE-100 - Software Training Funding

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695484. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695484/SWE-100+-+Software+Training+Funding

SWE-100 - Software Training Funding

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695484/SWE-100+-+Software+Training+Funding#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695484)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695484&showCommentArea=true&showComments=true#addcomment)

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

2.1.1.5 The NASA OCE and Center training organizations shall provide training to advance software engineering practices.  

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-100 History

SWE-100 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.6.1 The NASA Headquarters' Office of the Chief Engineer and Center training organizations shall provide and fund training to advance software engineering practices and software acquisition. |
| Difference between A and B | No change |
| B | 2.1.1.5 The NASA OCE and Center training organizations shall provide and fund training to advance software engineering practices and software acquisition. |
| Difference between B and C | Removed fund and software acquisition. |
| C | 2.1.1.5 The NASA OCE and Center training organizations shall provide training to advance software engineering practices. |
| Difference between C and D | No change |
| D | 2.1.1.5 The NASA OCE and Center training organizations shall provide training to advance software engineering practices. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

NASA software development activities in support of projects often require a balanced blend of software engineering development expertise and knowledge. If the software is contracted out, the development activities also require knowledge of NASA's acquisition practices and regulations. The Office of the Chief Engineer(OCE) and the Centers have committed to support these objectives by providing sufficient funding in support of the training.  In some instances, funding for training may be provided by multiple organizations if the training is beneficial to the communities they represent.

### 1. Critical Role of Software in NASA Missions

* **Rationale Overview**: Software plays an increasingly critical role in NASA missions, from controlling spacecraft to data processing, autonomous operations, and safety-critical systems. Ensuring mission success and safety depends on the capability of NASA's software engineering workforce to deliver high-quality, reliable, and secure software. Training is essential to developing and maintaining these skills across the agency.
* **Importance**: Software is not merely a support component; it is central to achieving technological and scientific breakthroughs. Without consistent investment in workforce training, software quality could degrade, increasing risks to mission success.

### 2. Rapidly Evolving Software Engineering Field

* **Rationale Overview**: Software engineering is a dynamic field, constantly evolving with advancements in programming languages, development tools, methodologies (e.g., Agile, DevOps), security requirements, and software assurance practices. Training ensures NASA’s workforce stays current with industry best practices and emerging technologies.
* **Specific Need**: New methodologies (e.g., containerized microservices, artificial intelligence, and machine learning) are being used in space exploration, requiring continuous training to enable NASA engineers to adapt to and effectively use these technologies.
* **Outcome of Training**: This requirement allows NASA to keep pace with advancements, ensuring its software engineering practices remain cutting-edge and aligned with industry standards.

### 3. Enhanced Support for NASA-Specific Challenges

* **Rationale Overview**: NASA projects often involve unique challenges, such as building software for space environments, safety-critical systems, high-reliability needs, and long-duration missions. Generic industry training may not address NASA-specific needs. Thus, OCE and Center training efforts must focus on topics tailored to NASA’s unique requirements, such as:
  + Development and testing in highly constrained environments (e.g., limited bandwidth, power, or processing resources during Mars missions).
  + Implementing robust software assurance in high-risk systems for human spaceflight or autonomous operations.
  + Developing secure systems to counteract cybersecurity threats in mission infrastructure.
* **Outcome of Training**: Training provided by NASA OCE and Centers ensures engineers are equipped with the specialized knowledge needed to solve these NASA-specific software engineering problems.

### 4. Closing Skill Gaps Across Centers and Teams

* **Rationale Overview**: Variability in skill levels and practices across NASA Centers and projects can lead to inefficiencies, poor implementation of processes, and inconsistent software quality. Structured training provided by the OCE and Center training organizations helps close these gaps by:
  + Standardizing practices across the workforce.
  + Promoting shared understanding of NPR 7150.2 (software engineering requirements) and NASA Software Assurance and Software Safety Standards (NASA-STD-8739.8).
  + Ensuring all teams are equipped to meet agency-wide goals consistently.
* **Specific Challenge Addressed**: For example, teams at different Centers may interpret or apply software lifecycle requirements inconsistently, leading to project delays or rework. Consistent, agency-wide training eliminates these discrepancies.

### 5. Ensures Compliance with NASA Standards and Policies

* **Rationale Overview**: Training ensures that engineers have a thorough understanding of NASA’s software engineering requirements (NPR 7150.2), policies, standards (including those for safety and assurance), and processes. Without adequate training, there is a risk of noncompliance, leading to preventable issues during project execution.
* **Connection to Compliance**: Training provides engineers with:
  + Knowledge of NPR requirements for the full software lifecycle.
  + Awareness of how to document evidence for reviews, appraisals, and audits (e.g., OCE compliance surveys or OSMA assessments).
* **Outcome of Training**: Reduces the risk of noncompliance and ensures engineers apply NASA standards consistently.

### 6. Mitigates Risk in High-Reliability Systems

* **Rationale Overview**: NASA’s software systems, especially those used in flight systems or spacecraft, are often safety-critical and mission-critical. Even a minor software error can result in mission loss, compromised safety, or significant cost overruns.
* **Examples of Software Failures**:
  + Mars Climate Orbiter (1999): A software mismatch (metric-to-imperial conversion error) led to the mission’s failure.
  + Ariane 5 Flight 501: A software exception caused by unprepared reuse led to the rocket's destruction.
* **Outcome of Training**: Training enables engineers to understand the importance of robust design, verification, validation (V&V), and how to eliminate classes of errors that pose risks to high-reliability systems.

### 7. Encourages Use of Best Practices and Lessons Learned

* **Rationale Overview**: NASA has accumulated lessons from past projects through its Lessons Learned Information System (LLIS). These lessons, such as those extracted from software-related failures or successes, are valuable for improving future software systems. However, disseminating lessons from LLIS into actionable and practical guidance often requires formal training.
* **Enhancing Engineering Rigor**: Training provides engineers with access to these institutional lessons, incorporating them into day-to-day practices, including:
  + Risk management in software projects.
  + Effective use of verification and validation techniques.
  + The importance of traceability in requirements management.
* **Outcome of Training**: Lessons learned become part of the agency's collective engineering discipline, reducing preventable errors and improving outcomes across all Centers.

### 8. Promotes Innovation Through Upskilling and Exposure

* **Rationale Overview**: Training not only focuses on maintaining a baseline skill set but also fosters innovation by introducing engineers to new ideas, tools, and methodologies. NASA missions often require innovative solutions to unprecedented problems, and training sparks the creativity needed to explore those solutions.
* **Example Areas for Breakthroughs**:
  + Artificial intelligence and machine learning in autonomous systems.
  + Integration of new paradigms like DevOps or Agile within safety-critical environments.
  + Use of cloud computing for ground systems and data-intensive missions.
* **Outcome of Training**: A formally trained workforce is better equipped to innovate, providing NASA with a competitive edge in exploring bold new frontiers.

### 9. Builds Workforce Continuity and Retention

* **Rationale Overview**: Investing in training signals NASA’s commitment to developing its workforce, increasing job satisfaction, and fostering a culture of growth and excellence.
* **New Generations of Engineers**: As many engineers with decades of experience in NASA’s unique programs retire, new engineers require formal training in software engineering practices to bridge the generational knowledge gap.
* **Outcome of Training**: Enhances workforce retention and continuity while ensuring new engineers are properly equipped to meet NASA’s unique challenges.

### 10. Strengthens Collaboration Across NASA Centers

* **Rationale Overview**: Agency-wide training by the OCE and Centers ensures that employees from different Centers learn to collaborate effectively and use shared standards, terminology, and processes.
* **Consistency Across Projects**: Training facilitates better integration of software engineering practices for multi-Center missions, such as the Artemis Program or James Webb Space Telescope, where collaboration between geographically distributed teams is vital.
* **Outcome of Training**: Promotes collaboration, reducing ambiguity and misalignment between Centers working on joint missions.

### 11. Supports Compliance with External Audits and Reviews

* **Rationale Overview**: NASA is often subject to external reviews by entities such as the Government Accountability Office (GAO), Office of Inspector General (OIG), and others. Training ensures workforce competency in meeting compliance expectations during such reviews and audits.
* **Outcome of Training**: Reduces audit findings related to workforce capability gaps and demonstrates NASA’s commitment to excellence in technical and procedural adherence.

### 12. Fulfilling NASA’s Institutional Mission

* **Rationale Overview**: As a leading space exploration agency, NASA has a responsibility to lead by example in engineering expertise. Providing training for software engineering aligns with the agency’s broader mission to advance scientific understanding and enhance technological capability for broader societal benefit.
* **Outcome of Training**: NASA continues to uphold its reputation for technical excellence and inspires the broader engineering community.

### Summary of Rationale

This requirement ensures that:

1. Software engineers maintain and improve their ability to deliver reliable, mission-critical, and innovative solutions.
2. NASA’s workforce evolves with the field’s rapid advancements.
3. Practices are consistent across Centers, compliant with NASA policies, and aligned with the unique challenges and risks of agency missions.
4. Lessons learned from past missions are institutionalized, and engineers are empowered to innovate, collaborate, and maintain NASA’s high standards of safety and mission success.

By investing in software engineering training through NASA’s OCE and Center efforts, the agency guarantees its workforce can continue to meet the demands of current and future missions with confidence, excellence, and innovation.

# 3. Guidance

Software engineering skills and expertise are vital for the success of NASA’s missions and can be developed through a combination of formal courses, on-the-job training, and specialized work assignments. While some skill advancements occur naturally during the execution of project activities (funded by the project), many require structured training programs to enhance foundational capabilities and advance the overall proficiency of the software engineering workforce.

This guidance divides training responsibilities into OCE and Center-funded training and project-funded training, clarifying objectives and focuses for each funding source.

## 3.1 OCE and Center-Funded Training

### 3.1.1  Purpose and Focus of OCE and Center-Funded Training

The NASA Office of the Chief Engineer (OCE) and Center training organizations collaborate to provide foundational and career-long training opportunities for software engineers. This training ensures that engineers across the agency benefit from consistent, high-quality development programs designed to elevate NASA’s software engineering capabilities.

* **Core Focus:** OCE and Center-funded training provides access to courses that build foundational software engineering knowledge and support long-term improvement efforts across the agency. These courses aim to:
  + Establish a baseline of software engineering expertise.
  + Reinforce the importance of best practices, methodologies, and compliance with NASA policy.
  + Support continual growth throughout an engineer’s career and ensure engineers stay current with evolving tools, technologies, and processes.

### 3.1.2  Developing a Training Framework

* The OCE and Centers collaboratively develop and maintain training curricula as part of the Developing a Curriculum (DACUM) process. This ensures that the courses are well-structured, tailored to NASA’s unique requirements, and aligned with the latest advancements in software engineering.
* DACUM courses are regularly reviewed and updated to maintain relevancy, ensuring that NASA engineers benefit from modern, innovative training tailored to Agency needs.

### 3.1.3  Balanced Offerings and Agency-Wide Availability

* The OCE plays a key role in co-funding courses across Centers to ensure both consistent training quality and equal access for engineers at different locations. This joint funding ensures that all Centers offer a balanced portfolio of training programs, with sufficient capacity to accommodate agency needs.
* Training is designed to be standardized at the agency level while accommodating Center-specific needs to address local expertise gaps or project priorities.

### 3.1.4  Funding Priorities for OCE-Supported Training

OCE-funded training focuses on two key areas that align with broader agency goals:

1. **Continuous Process Improvement and Software Capabilities Growth:**
   * Courses designed to support Capability Maturity Model Integration (CMMI)**®** appraisals and improvement initiatives aligned with the OCE’s Software Engineering Improvement Initiative.
   * These initiatives aim to elevate the performance of NASA’s software development processes and produce measurable quality improvements across the agency.
2. **Core Software Engineering Courses:**
   * Formal training courses that span a software engineer’s career, supporting the entire software development lifecycle:
     + Requirements engineering.
     + Software design and architecture.
     + Robust coding practices.
     + Agile methods and DevOps.
     + Verification, validation, and software assurance.
     + Cybersecurity and secure software development.
   * The training is tailored to provide engineers with cross-project knowledge applicable across multiple programs, rather than being tied to a specific project or tool.

By establishing a strong foundation of core knowledge and higher-level process skills, OCE and Center training ensures that NASA engineers contribute to the consistent application of best practices that result in reliable, safe, and high-quality software systems.

## 3.2 Project-Funded Training

### 3.2.1  Purpose and Focus of Project-Funded Training

While OCE and Center-funded training supports broad software engineering capabilities, project-specific training is targeted toward developing skills and expertise relevant to a particular mission, system, or project team.

* **Core Focus:** Project-funded training is designed to meet “just-in-time” skill needs for delivering software specific to a project’s objectives. These courses or learning opportunities typically focus on:
  + Programming languages and frameworks required for the project (e.g., Python, C++, Java).
  + Development and testing tools (e.g., IDEs, debugging tools, continuous integration pipelines).
  + Operating systems, drivers, and embedded systems unique to mission hardware.
  + Project and subsystem-specific coding standards or guidelines.
  + Implementation of unique algorithms or software tailored for mission-specific constraints (e.g., AI/ML models for autonomous capabilities, fault-tolerant systems, etc.).

### 3.2.2  Key Features of Project-Funded Training

* **Customization:** Training is customized to the needs of the specific system or subsystem within the project. For example:
  + If a system includes integration with a legacy database or architecture, training might focus on dealing with older standards.
  + For systems using advanced computing techniques (e.g., GPU acceleration or real-time navigation algorithms), training would focus on those specific technologies or methods.
* **On-the-Job Learning:** In addition to formal courses, project-funded training often supports on-the-job learning that is specific to project deliverables, processes, or tools.
* **Short-Term Focus:** Unlike agency-wide foundational training, project-specific training is often shorter and narrowly focused to address immediate needs.

## 3.3 Key Differences Between OCE/Center-Funded and Project-Funded Training

| **Aspect** | **OCE/Center-Funded Training** | **Project-Funded Training** |
| --- | --- | --- |
| **Scope** | Broad, foundational, and spans the engineer’s career. | Specific to project requirements and short-term needs. |
| **Funding** | Provided jointly by OCE and Centers. | Funded entirely by the project. |
| **Focus Areas** | Core competencies, methodologies, and continuous improvement (e.g., CMMI). | Programming languages, tools, standards, specific technologies. |
| **Training Tools/Courses** | General purpose/software engineering lifecycle courses. | Project-oriented (e.g., for a particular operating system or subsystem tool). |
| **Strategic Objective** | To advance NASA’s overall software capability and standardization. | To equip engineers with the skills to meet specific project deliverables. |

## 3.4 Implementation Recommendations and Best Practices

1. **Balanced Blended Training Model:**
   * Combine Center/OCE-funded foundational training with project-funded skill-specific training to ensure engineers are well-rounded and equipped for both general needs and project-specific challenges.
2. **Training Tracking and Assessment:**
   * Establish a centralized system to track engineers’ training progress over their careers.
   * Use performance metrics and assessments to evaluate the effectiveness of both OCE/Center and project-specific training programs.
3. **Tailoring Training Through Feedback:**
   * Collect feedback post-training from engineers and project teams to continuously refine training course content and delivery methods.
4. **Flexible Training Delivery Options:**
   * Offer courses in in-person, virtual, and hybrid formats to increase accessibility across the agency.
   * Leverage asynchronous training modules for project-funded skill acquisition to reduce time constraints on busy project schedules.
5. **Promoting Collaboration Between Centers and Projects:**
   * Encourage cross-Center sharing of training resources and expertise to reduce duplication of effort.
   * Allow project-specific training resources to be shared among projects handling similar systems, ensuring efficiency.

## 3.5 Conclusion

This dual-focus training model—supported by both OCE/Center and project funding—ensures that NASA engineers are equipped with the competencies needed for success. Foundational training provides long-term software engineering growth and agency-wide consistency, while project-specific training meets urgent system-level requirements. Together, these approaches create a robust workforce prepared to deliver the innovative, reliable, and safety-critical software solutions required for NASA’s missions.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-222 - Software Assurance Training](/spaces/SWEHBVD/pages/105710148/SWE-222+-+Software+Assurance+Training)        * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement)      * [Training](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Training) |

# 4. Small Projects

Small projects at NASA often face resource constraints in terms of budget, schedule, and personnel, making it necessary to approach training in a tailored, streamlined, and resource-conscious manner. Despite these constraints, small projects still rely on high-quality software to succeed. Ensuring that software engineering practices align with NASA's expectations and standards is achievable with an effective training strategy scaled to the project's size and complexity.

## 4.1 Guidance for Small Projects

The following guidance highlights how small projects can comply with this requirement while addressing their unique constraints:

### 4.1.1  Recognizing the Importance of Training for Small Projects

* Purpose-Specific Training: Small projects may involve simpler systems but still face critical challenges, such as the need for reliability, safety, or mission-critical software engineering. Training is a cost-effective way to improve team skills and reduce project risks.
* Value of Foundational Knowledge: Even small teams can greatly benefit from participating in focused training that equips them with a solid foundation in software engineering best practices, lifecycle processes, and NASA-specific requirements (e.g., NPR 7150.2 [083](#_tabs-<p></p>), NASA-STD-8739.8 [278](#_tabs-<p></p>)).

### 4.1.2  Tailoring the Training Approach

Small projects differ in scope, but training should always be proportionate to the project's size, criticality, and classification (risk level). Below are strategies and considerations for tailoring training to meet this requirement effectively:

1. **Focus on Critical Topics for Small Projects**  
   Identify and prioritize the training topics that are most relevant to small projects. The following areas often align with the needs of smaller efforts:  
   * **Basic Software Engineering Lifecycle Knowledge**: Focus on topics like requirements management, design principles, implementation best practices, and verification/validation.
   * **Lightweight Documentation and Process Management**: Train teams on streamlined processes for maintaining compliance without creating unnecessary overhead.
     + Example: Introduction to using simplified Requirements Traceability Matrix (RTM) templates.
   * **Risk Management for Small-Scale Systems**: Emphasize practical approaches for identifying, tracking, and mitigating software risks (e.g., mismatched interfaces, insufficient testing).
   * **Implementing Agile or Iterative Development**: Provide guidance on adapting Agile methodologies for small teams with minimal resources.
   * **Software Configuration Management**: Focus on lightweight tools and processes for managing code, artifacts, and baselines without heavy infrastructure investment.
   * **Cybersecurity for Small Projects**: Cover basic secure coding practices, protecting test environments, and integrating security in the project lifecycle.
2. **Leverage Free or Low-Cost Resources**  
   Small projects often have limited budgets, so training options should focus on free or low-cost solutions:
   * **OCE/Center Catalog of Training**: Utilize the Developing a Curriculum (DACUM) catalog, often co-funded by the OCE and Centers, which provides access to core courses at no additional cost to projects.
   * **Internal Workshops**: Conduct informal peer training or workshops leveraging expertise from experienced team members or mentors.
   * **NASA Engineering Network (NEN)**: Access lessons learned, case studies, and self-paced training modules available via the NEN portal.
   * **Open-Source or Public Resources**: Supplement training with publicly available educational materials, such as those provided by MIT OpenCourseWare, Coursera, or Stack Overflow (in non-sensitive areas).

### 4.1.3  Training for Small Project Teams

1. **Encourage Multi-Disciplinary Training**  
   Small project teams often wear multiple hats, with engineers taking on roles in development, testing, assurance, and management. Training should reflect this versatility:  
   * **Cross-Functional Skills**: Provide training that bridges disciplines (e.g., an engineer learning both implementation and verification) for greater team flexibility.
   * **Assurance Awareness**: Ensure all team members—whether or not they directly handle software assurance—are familiar with assurance principles and practices.
   * **Example Courses**:
     + "Introduction to Software Assurance for Small Projects."
     + "How to Manage Requirements and Risk in a Streamlined Environment."
2. **Promote On-the-Job Learning**  
   Small projects frequently rely on hands-on work for skill-building:
   * **Practical Pair Programming and Reviews**: Pair junior engineers with senior engineers for real-time knowledge transfer while writing or reviewing code.
   * **Embedded Learning in Process Activities**: Use project meetings (e.g., sprint reviews, design reviews) as informal training opportunities to reinforce software engineering processes (e.g., design critique sessions).
3. **Train for Tools and Resources Suited to Small Projects**  
   Small projects often rely on lightweight tools and flexible processes rather than heavyweight enterprise systems. Train teams to use:
   * **Version Control Tools**: GitHub, Bitbucket, or GitLab for software configuration management and branch-controlled collaboration.
   * **Low-Cost Testing Frameworks**: Open-source test tools (e.g., Jenkins for CI/CD, JUnit for unit testing) to encourage efficient but thorough software validation.
   * **Requirements Management Tools**: Train teams on low-overhead options for managing requirements (e.g., Confluence, spreadsheets, or Trello).

### 4.1.4  Funding Considerations for Training

1. **OCE and Center-Funded Training**
   * Leverage courses tailored for foundational skills or general capabilities. Small projects can rely on OCE and Center-funded training opportunities as their primary source for building baseline software engineering knowledge.
     + Example Courses:
       - Basic software engineering lifecycle practices.
       - Software assurance techniques applicable to small-scale software development.
       - Agile methodology for small teams.
2. **Project-Specific Training**
   * Small projects may allocate a modest portion of their budgets to specialized training directly tied to project goals. Training could focus on specific tools, languages, or technologies required for implementation or integration tasks.
     + Example: A small CubeSat software project might provide training on real-time operating system programming (e.g., VxWorks, FreeRTOS).

### 4.1.5  Communication and Collaboration at the Agency Level

1. **Cross-Project Sharing of Materials**
   * Small projects can benefit from adopting training resources, templates, and tools that have already been developed and validated by other NASA projects of similar scale. Sharing resources reduces duplication of effort and accelerates readiness.
2. **Leverage Mentorship Opportunities**
   * Leverage the expertise of experienced engineers and mentors across NASA, particularly from larger projects, to enhance the training of small project staff.
   * For instance, mentorship can focus on training topics like safety-critical software assurance or lessons learned from prior small project experiences.

### 4.1.6  Ensuring Training Effectiveness for Small Projects

1. **Measure Impact on Processes and Deliverables**
   * Evaluate how training has improved software engineering processes for small projects:
     + Are defects being caught earlier in the lifecycle due to better requirement management or testing practices?
     + Are tools and concepts from training being actively used in daily workflows?
2. **Feedback Loop for Tailored Improvement**
   * After each training session, gather feedback from small project engineers to assess areas of value and identify gaps. This ensures future OCE/Center-provided training aligns better with small project needs.
3. **Incremental Learning Over Project Phases**
   * Deliver training in manageable increments based on the project lifecycle phase:
     + **Early Phases**: Focus on requirements engineering and design principles.
     + **Mid-Phases**: Provide deeper training on implementation practices and V&V.
     + **Late Phases**: Concentrate on testing, deployment, and post-launch assurance.

## 4.2 Example Use Cases

### 4.2.1  Small CubeSat Project

* *Challenge*: A CubeSat team needs training to ensure reliable software for autonomous operations but has limited staff.
* *Training Focus*: Basic lifecycle processes, safety assurance, testing with limited resources, and tools for real-time systems.
* *Implementation*: Use OCE-funded courses for high-level topics (e.g., NASA software lifecycle) and provide project-specific training on FreeRTOS or similar platforms.

### 4.2.2  Small Data-Focused Science Mission

* *Challenge*: The mission relies on a lightweight data analysis pipeline but needs assurance that the system meets critical quality standards.
* *Training Focus*: Secure coding practices, requirements validation, and open-source testing frameworks.
* *Implementation*: Train the lead engineer using OCE tools while leveraging group learning via informal workshops to extend team skills.

## 4.3 Conclusion

Small projects can effectively meet this training requirement by leveraging lightweight, cross-functional, and resource-efficient training strategies—combining OCE/Center-funded foundational courses with project-specific skill development. Tailored training helps small project teams build the capabilities necessary to deliver high-quality software, reduce risks, and ensure compliance with NASA's engineering and assurance standards, all within their constrained environments.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
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
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-289)

  [OCE Software Engineering Training](https://nen.nasa.gov/web/software/training "Click to open in new window")

  NESC Academy Software Discipline. Topics include software requirements, design, implementation, architecture, assurance, testing, training, tools, process improvement, best practices, software release, models and simulations, and software research and technology innovation.
* (SWEREF-294)

  [OSMA/NSC's SMA Technical Excellence Program (STEP) program.](https://nsc.nasa.gov/professional-development/safety-and-mission-assurance-technical-excellence-program "Click to open in new window")

  The Safety and Mission Assurance (SMA) Technical Excellence Program (STEP) is a career-oriented, professional development roadmap for SMA professionals.
* (SWEREF-491)

  [Academy of Program/Project & Engineering Leadership (APPEL) - Learning Course Catalog](https://appel.nasa.gov/courses/ "Click to open in new window")

  Access the APPEL curriculum catalog from this URL.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database (LLIS) contains many examples demonstrating the importance of training in software engineering practices and how inadequate training has led to failures or inefficiencies in NASA projects. Below, we outline several key lessons learned that emphasize the need for consistent, well-designed training programs to advance software engineering practices and ensure mission success.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Software Engineering Training Reduces Risk of Critical Failures

* **LLIS Reference:** *Mars Climate Orbiter Mishap Investigation Board Report* (LLIS-1900)
* **Summary of Incident:**  
  The loss of the Mars Climate Orbiter was traced to a software engineering error—a failure to properly convert units from the imperial system to the metric system. Engineers weren’t sufficiently trained to identify issues with requirements traceability, integration, and cross-discipline communication.
* **Lesson Learned:**  
  Inadequate training in software engineering practices, including unit conversion standards, software interface control, and requirements verification, can result in catastrophic mission failure. Engineers must understand engineering standards, and those involved in integration must receive training that emphasizes adherence to interface control agreements.
* **Connection to Requirement:**  
  Training provided by the OCE and Centers can help ensure that staff are proficient in relevant practices such as requirements traceability, software validation, and interdisciplinary communication, thereby reducing risk during development.

#### 2. Ensure Consistent, Agency-Wide Software Training

* **LLIS Reference:** *Gap in Training Contributed to Software Quality Discrepancies* (LLIS-1720)
* **Summary of Issue:**  
  A review of software across multiple NASA Centers revealed significant variability in software quality and the application of software development standards. This was attributed to differences in local training approaches, leaving some Centers underprepared to handle software assurance activities.
* **Lesson Learned:**  
  Training for software engineers and assurance personnel must be consistent across Centers. Center-led efforts alone can result in gaps in understanding core standards like NPR 7150.2 and NASA-STD-8739.8. Training at the agency level (coordinated by the OCE) ensures that all Centers meet the same baseline competency requirements and quality standards.
* **Connection to Requirement:**  
  The OCE's training mandate ensures uniformity in core software engineering principles, helping reduce discrepancies in quality and fostering consistent application of NASA policies.

#### 3. Continuous Training Improves Response to Emerging Software Challenges

* **LLIS Reference:** *Software Technical Excellence in Emerging Areas* (LLIS-2155)
* **Summary of Issue:**  
  As software complexity increased in projects like the James Webb Space Telescope (JWST), there was a lack of training in emerging practices like distributed systems, cybersecurity, and automation. This knowledge gap led to integration issues that contributed to cost overruns and significant schedule delays.
* **Lesson Learned:**  
  Engineers must receive continuous training in emerging software technologies, tools, and practices, especially in high-complexity systems. Without regular training updates, NASA risks increased technical debt, integration challenges, and missed opportunities to leverage innovative technologies.
* **Connection to Requirement:**  
  The OCE should ensure programs include coursework on leading-edge practices (e.g., Model-Based Systems Engineering [MBSE], secure software design, AI/ML in autonomous systems) and prioritize career-long learning aligned with NASA's increasing software demands.

#### 4. Insufficient Guidance on Assurance Practices Led to Safety Risks

* **LLIS Reference:** *Langley Software Safety Gap in Small Projects* (LLIS-1768)
* **Summary of Incident:**  
  A small research project at Langley Research Center lacked experienced staff with formal training in software safety assurance. Despite the relatively low project cost, the software developed had implications for personnel safety and critical hardware operations. The team neglected testing and failed to adhere to principles laid out in safety standards like NASA-STD-8739.8.
* **Lesson Learned:**  
  Safety can be overlooked in small projects due to limited budgets, time, or the assumption that safety-critical software assurance is only relevant to large-scale missions. NASA must provide targeted training for all projects, regardless of size, on safety-critical assurance practices.
* **Connection to Requirement:**  
  OCE-developed training should include content tailored to small projects, emphasizing scalable safety assurance practices and how to apply them to resource-constrained environments.

#### 5. Lack of Software Assurance Training Causes Inadequate Risk Coverage

* **LLIS Reference:** *Software Assurance Neglect and Resultant Mission Risk* (LLIS-1623)
* **Summary of Incident:**  
  A critical failure within a simulation software package occurred during testing because software assurance activities (including independent verification) were deprioritized. Engineers involved in the project had not received full training in software assurance principles and undervalued the importance of early defect identification and rigorous testing methods.
* **Lesson Learned:**  
  Training must emphasize early assurance involvement in the software lifecycle to reduce costly late-phase defect discovery and ensure compliance with NASA-STD-8739.8. Proper training strengthens implementation of V&V efforts, risk prevention, and alignment between developers and assurance personnel.
* **Connection to Requirement:**  
  This aligns with the guidance to include software assurance-focused training in formal coursework offered by the OCE and Centers, ensuring assurance personnel and engineers understand their roles in managing software-related risks.

#### 6. On-the-Job Training Alone Cannot Fill Skill Gaps

* **LLIS Reference:** *Mars Polar Lander Loss* (LLIS-2205)
* **Summary of Incident:**  
  The Mars Polar Lander was lost due to a software issue involving an erroneous sensor signal interpretation in the descent software. The engineers lacked formal training on debugging and system-level testing methodologies. The project relied heavily on on-the-job learning, which proved insufficient to identify the subtle but critical issues that ultimately caused the failure.
* **Lesson Learned:**  
  NASA projects should not rely solely on informal, on-the-job learning to meet critical software skills requirements. Formalized coursework and structured mentoring programs are essential to ensure engineers are equipped with baseline and advanced skills to handle subtle integration and testing problems.
* **Connection to Requirement:**  
  This underscores the importance of OCE and Center-led training that goes beyond incidental learning and offers structured, comprehensive programs across the software lifecycle.

#### 7. Learning from Discrepancies in Agile and Lightweight Practices

* **LLIS Reference:** *Balancing Documentation in Agile Development* (LLIS-2418)
* **Summary of Issue:**  
  A small NASA project experimented with Agile development but produced insufficient documentation due to a misunderstanding of Agile principles. Software engineers lacked training in how to balance minimal documentation requirements with NASA standards, leading to a failure to provide adequate artifacts for assurance reviews.
* **Lesson Learned:**  
  As lightweight or Agile methodologies are adopted by smaller projects, it is crucial to provide training that explains how to integrate these approaches into standard NASA processes while maintaining compliance with NPRs and software assurance requirements.
* **Connection to Requirement:**  
  Training should teach engineers how to adapt methodologies like Agile to NASA mission-critical environments, ensuring the right balance between flexibility and rigor.

#### 8. Training Builds Cross-Functional Collaboration

* **LLIS Reference:** *Team Skills Alignment Through Training* (LLIS-2250)
* **Summary of Issue:**  
  A mission team faced integration issues due to a lack of shared understanding of software processes between diverse team members (e.g., systems engineering, software developers, and safety analysts). The absence of a common knowledge baseline resulted in miscommunication about software interfaces, testing, and assurance.
* **Lesson Learned:**  
  Training programs should emphasize cross-functional collaboration by providing courses that integrate systems engineering, software development, and assurance practices. These programs foster better communication and shared mental models across teams.
* **Connection to Requirement:**  
  OCE and Center training programs should offer cross-disciplinary coursework to train engineers in collaboration and shared workflows.

### 6.1.2  Conclusion

These lessons highlight the importance of formal NASA-provided training in software engineering practices. Training equips engineers and assurance teams with the tools and knowledge to avoid costly mission failures, mitigate risks, and adhere to agency standards. By integrating lessons learned into the design of OCE and Center training programs, NASA can ensure its workforce is well-prepared to meet the demands of current and future projects.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Ensure that early career team members receive adequate support](https://software.gsfc.nasa.gov/lesson-details/329/). **Lesson Number 329**: The recommendation states: "Be proactive in providing support to early career team members."

# 7. Software Assurance

**SWE-100 - Software Training Funding**

2.1.1.5 The NASA OCE and Center training organizations shall provide training to advance software engineering practices.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

None identified at this time.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support oversight, validate compliance, manage risks, and ensure the quality of delivered products. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

No specific deliverables are currently identified.

## 7.3 Metrics

No standard metrics are currently specified.

## 7.4 Guidance

Software assurance (SA) plays a crucial role in ensuring software reliability, functionality, safety, security, and compliance with NASA’s stringent mission and project standards. In advancing software engineering practices, it is essential that software assurance is fully integrated into the training process to develop a workforce capable of recognizing risks, implementing mitigations, and verifying software quality throughout the project life cycle.

Below is tailored software assurance guidance to support this requirement:

### 7.4.1  The Role of Training in Software Assurance

* **Embed Software Assurance Fundamentals**: Training for software engineering must include a strong emphasis on software assurance. This ensures that engineers, assurance personnel, and project managers have the skills and knowledge to assess and improve software quality, safety, and security.
* **Develop Organizational Awareness**: Training should promote the importance of software assurance across all teams—not just SA-focused roles—so that software assurance is woven into every phase of the software life cycle.
* **Meet NPR and NASA-STD Compliance**: Software-focused training should ensure understanding and compliance with:
  + NPR 7150.2: NASA Software Engineering Requirements.[083](#_tabs-<p></p>)
  + NASA-STD-8739.8: Software Assurance and Software Safety.[278](#_tabs-<p></p>)
  + Other applicable standards related to cybersecurity, safety, and mission assurance.

### 7.4.2  Key Objectives for Software Assurance-Focused Training

Training programs should be designed to address the following key objectives:

1. **Principles and Practices:** Equip participants with the ability to apply software assurance principles within their work scope, including both proactive (e.g., prevention) and reactive (e.g., testing) measures.
2. **Lifecycle Coverage:** Ensure software assurance proficiency spans the entire software development life cycle (SDLC)—from planning and requirements definition through testing, deployment, and maintenance.
3. **Tailoring for Risk:** Provide guidance on tailoring assurance processes based on the project’s classification, the software criticality (per NASA’s software classification scheme, Appendix D of NPR 7150.2), and the associated risk.
4. **Cybersecurity Knowledge:** Enhance awareness of secure coding standards, threat modeling, penetration testing, and other key practices to address cybersecurity risks in software-intensive systems.
5. **Verification and Validation (V&V):** Train engineers on V&V techniques to ensure that software meets its technical, functional, and mission requirements while addressing safety and security considerations.

### 7.4.3  Content Areas for Software Assurance Training

To develop a robust software assurance capability within the workforce, the following content areas should be included in training programs:

#### 7.4.3.1. Software Safety

* Understanding the relationship between software safety, engineering, and assurance.
* Identifying and mitigating safety risks associated with software, especially in mission-critical or human-rated systems.
* Analyzing hazards and failure modes through techniques such as:
  + [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) (FTA).
  + [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) (FMEA).

#### 7.4.3.2  Software Quality Assurance (SQA)

* Planning and tracking SQA activities to monitor adherence to established processes, standards, and policies.
* Assessing software deliverables for consistent application of quality checkpoints.

#### 7.4.3.3  Risk Management in Software Assurance

* Identifying software-related risks (e.g., design flaws, inadequate test coverage) during development.
* Tracking and managing risks throughout the life cycle.
* Emphasizing the role of assurance in preventing recurrence of lessons from prior software-related mishaps (e.g., Mars Climate Orbiter).

#### 7.4.3.4  Verification and Validation (V&V)

* Teaching practical V&V techniques to evaluate software requirements, design, implementation, and performance.
* Training teams to develop and execute robust test plans using:
  + Regression testing.
  + Functional testing.
  + Boundary testing.
  + Fault injection testing (for safety-critical software).

#### 7.4.3.5  Software Requirements Assurance

* Ensuring completeness, consistency, and verifiability in software requirements.
* Teaching how to trace requirements through design, implementation, and testing (Requirements Traceability Matrix, or RTM).
* Emphasizing validation of requirements to prevent downstream errors.

#### 7.4.3.6  Secure Software Development Practices

* Incorporating secure coding principles and NASA-specific cybersecurity policies.
* Recognizing security vulnerabilities (e.g., buffer overflows, injection attacks) during design and development.
* Training teams on practices such as Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST).

#### 7.4.3.7  Software Configuration Management Assurance

* Providing knowledge of configuration management tools and their assurance requirements.
* Ensuring all software artifacts (e.g., requirements, code, test scripts, documents) are version-controlled, auditable, and linked through a traceable process.

#### 7.4.3.8  Continuous Integration and Continuous Deployment (CI/CD) Assurance

* Developing understanding of how software assurance fits into modern CI/CD pipelines.
* Training practitioners to assess and validate automated test results before deployment.

### 7.4.4  Methods for Delivering Software Assurance Training

#### 7.4.4.1  Formal Courses through OCE and Centers

* Leverage the DA Curriculum (DACUM) framework to develop courses on core software assurance topics.
* Suggested courses include:
  + Introduction to Software Assurance.
  + Advanced Verification and Validation Techniques.
  + Software Safety Criticality Analysis.
  + Secure Software Development and Threat Mitigation.
* Make these courses available agency-wide to support consistency in assurance practices.

#### 7.4.4.2  Specialized Workshops

* Conduct hands-on workshops focusing on:
  + NASA CASE tools for requirements and testing data.
  + Failure analysis case studies (e.g., Columbia and Mars Climate Orbiter) and how proper software assurance could have mitigated them.
* Target specific domains such as embedded systems, AI/ML integration, or edge computing.

#### 7.4.4.3  On-the-Job Training (OJT)

* Develop mentoring or rotational assignments in software assurance roles. Examples include:
  + Assigning junior engineers to teams working on safety-critical systems.
  + Building expertise through involvement in software peer reviews.
* Provide guidance for new engineers to actively participate in risk reviews, requirement validation workshops, or defect triage boards.

#### 7.4.4.4  eLearning Modules and Certifications

* Develop modular, online offerings for flexible learning opportunities.
* Offer certifications (such as NASA Software Quality Engineer Certification) to validate and incentivize completion of assurance-focused training.

### 7.4.5  Measuring the Effectiveness of Software Assurance Training

NASA must monitor the impact of training programs to ensure they meet software assurance objectives. Adopt the following metrics:

* **Skill Coverage Metrics:** Analyze how well training addresses the skills defined in NPR 7150.2 and NASA-STD-8739.8.
* **Participation and Curriculum Effectiveness:** Track employee participation rates and conduct post-training surveys to assess knowledge retention and applicability.
* **Process and Project Improvements:** Measure reductions in defects, quality assurance findings, or compliance issues in the projects supported by trained engineers.
* **SQA Audit Performance:** Evaluate the performance of teams during SQA audits and whether nonconformance findings have decreased.

### 7.4.6  Alignment with Agency-Wide Policies

* **Collaborative Training Strategy:** Ensure software assurance training is integrated with broader OCE and Center-funded initiatives for advancing software engineering practices. This avoids duplication and ensures consistent adoption of assurance practices across NASA Centers.
* **Tailoring for Project-Specific Needs:** While foundational training is crucial, ensure that Centers and projects have the budget and flexibility to provide specialized training elements based on specific mission needs, risk profiles, or new technologies.

### 7.4.7  Conclusion

Effective software assurance training ensures that NASA’s workforce is equipped with the expertise to develop and maintain high-quality software aligned with mission requirements and agency standards. By prioritizing foundational assurance knowledge, risk management principles, and modern assurance practices across the software project lifecycle, NASA can mitigate risks, improve software quality, and achieve mission success. Training by OCE and Center organizations, coupled with project-specific training, creates a culture where software assurance becomes an automatic and integral part of all development activities.

The software Assurance training approach can be found on OSMA/NSC's SMA Technical Excellence Program (STEP) [294](#_tabs-<p></p>) program website.  See also [SWE-222 - Software Assurance Training](/spaces/SWEHBVD/pages/105710148/SWE-222+-+Software+Assurance+Training).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-222 - Software Assurance Training](/spaces/SWEHBVD/pages/105710148/SWE-222+-+Software+Assurance+Training)        * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) |
