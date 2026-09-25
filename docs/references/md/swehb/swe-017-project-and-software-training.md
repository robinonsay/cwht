# SWE-017 - Project and Software Training

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695403. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training

SWE-017 - Project and Software Training

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695403)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695403&showCommentArea=true&showComments=true#addcomment)

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

3.4.1 The project manager shall plan, track, and ensure project specific software training for project personnel.

## 1.1 Notes

This includes any software assurance personnel assigned to the project.

## 1.2 History

Click here to view the history of this requirement: SWE-017 History

SWE-017 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.5 The project shall plan, track, and ensure project specific software training for project personnel. |
| Difference between A and B | No change |
| B | 3.4.1 The project manager shall plan, track, and ensure project specific software training for project personnel. |
| Difference between B and C | No change |
| C | 3.4.1 The project manager shall plan, track, and ensure project specific software training for project personnel. |
| Difference between C and D | No change |
| D | 3.4.1 The project manager shall plan, track, and ensure project specific software training for project personnel. |

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

This requirement is to ensure that project personnel receives the necessary training in project selected software tools, programming languages, techniques, and methodologies to develop quality work products.  Furthermore, the system under development typically has aspects that need to be thoroughly understood by software personnel. The development and use of a controlled training plan ensure that the skills and expertise required by a project are available when they are needed.

Effective software development, management, and assurance require that all personnel involved in the project have the necessary skills, knowledge, and training tailored to meet the project's specific needs. Software projects, especially in domains like aerospace, where NASA operates, often involve complex, safety-critical systems, unique processes, and specialized tools. This requirement ensures that all project personnel—including Software Assurance (SA) personnel—are adequately trained, which directly contributes to project success, product quality, and mission safety.

This requirement ensures that the project manager plans, tracks, and ensures the completion of project-specific training for software personnel, including SA personnel, to address the complexity of software systems, mitigate project risks, and ensure successful project execution. Training plays an integral role in creating a knowledgeable workforce capable of navigating the challenges of modern software development while ensuring safety, compliance, and operational success. The rationale for training is grounded in its ability to create a strong foundation for software quality, mission reliability, and overall project success.

## 2.1 Addressing the Complexity of Modern Software Projects

Modern software projects involve complex systems, tools, and practices such as Agile development, embedded systems, real-time operating systems, and protocols for cybersecurity. These complexities necessitate that personnel are appropriately trained to effectively design, develop, test, and assure software systems. Without proper training, risks such as coding errors, system vulnerabilities, or integration failures increase, jeopardizing both the project and mission success.

Training ensures personnel understand:

* Project-specific tools and environments (e.g., cFE/cFS for flight software, JIRA, static analysis tools).
* Development methodologies (e.g., Agile, Scrum).
* Unique project challenges (e.g., reuse of heritage code, embedded systems, or real-time operations).

## 2.2 Enhancing the Competence of Software Assurance Personnel

Software Assurance plays a critical role in ensuring software reliability, safety, and compliance with applicable standards and requirements. For SA personnel to perform their duties effectively, they need:

* Basic SA training (e.g., software testing, safety practices, and assurance planning).
* Discipline-specific training on tools and technologies used in the project (e.g., configuration management systems, risk management tools).
* Project-specific training to familiarize them with the requirements, lifecycle, and objectives of the project.

Training ensures SA personnel can effectively identify and mitigate risks, assess compliance, and contribute to the overall quality of the software product.

## 2.3 Supporting Compliance with Standards and Processes

NASA software projects are governed by a range of standards, requirements, and best practices (e.g., NPR 7150.2, SWE Standards). Training ensures that project personnel understand how to apply these requirements throughout the software lifecycle. For example:

* Personnel need training in NASA, CMMI, or other organizational processes (e.g., software lifecycle planning, configuration management, root cause analysis).
* SA personnel need to understand and verify compliance with specific NPR standards (e.g., [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions)).

Without training, personnel may unintentionally omit critical compliance activities, increasing risks of software defects or regulatory nonconformance.

## 2.4 Supporting Agile or New Development Methodologies

When a project adopts new methodologies, such as Agile, Scrum, or Spiral development, personnel require specific training to ensure proper usage and integration. For instance:

* Developers, managers, and SA personnel may require Agile methodology training, including training on roles like Scrum Master or Product Owner.
* SA personnel must learn to adapt assurance practices to iterative development.

Training ensures that everyone understands their roles and responsibilities under the chosen development framework, avoiding confusion or inefficiencies.

## 2.5 Ensuring the Safe Integration of New or Complex Technologies

Software projects that incorporate new or immature technologies, tools, or processes require personnel to adapt quickly. Training ensures personnel understand the risks, limitations, and best practices associated with these technologies. For example:

* In projects using the Core Flight Executive (cFE) or Core Flight System (cFS), personnel trained in these frameworks can develop, test, and assure software functionality more efficiently.
* Teams using COTS tools or real-time operating systems need training on their proper implementation to fulfill performance, security, and reliability requirements.

## 2.6 Reducing Errors and Increasing Efficiency

Training personnel in the tools, processes, and systems used in a project reduces the likelihood of human error and inefficiencies. Training ensures:

* Tools are used optimally (e.g., Integrated Development Environments, static code analyzers, or version control systems like Git).
* Processes are followed in a standard, repeatable manner (e.g., static analysis, peer reviews, and testing cycles).

Properly trained personnel are also better equipped to identify and resolve issues early, reducing the time and cost of rework.

## 2.7 Ensuring Successful Collaboration Among Multi-Disciplinary Teams

NASA projects often involve multi-disciplinary teams working across different locations and expertise areas. Training helps:

* Create a common understanding of project-specific goals, software processes, and methodologies.
* Standardize skills and practices used across the team.  
  For example, an orientation session introducing the project’s concept of operations ensures that software developers, hardware engineers, and SA personnel align with the project’s objectives.

## 2.8 Mitigating Software-Specific Risks

Poorly trained personnel can introduce errors that may result in software failures, cybersecurity vulnerabilities, or degradation of system performance. Some common risks mitigated by training include:

* Inadequate understanding of software safety for safety-critical systems.
* Inefficient testing strategies leading to undetected defects.
* Misconfiguration of tools or misuse of embedded software, leading to functional errors or resource overuse.

Proper training ensures personnel have the knowledge to manage risks proactively and respond effectively to unexpected challenges.

## 2.9 Supporting Continuous Professional and Organizational Development

Beyond project-specific benefits, ongoing training programs like the **SMA Technical Excellence Program (STEP)** contribute to the continuous improvement of the workforce:

* Builds expertise within the Software Assurance discipline.
* Allows personnel to grow and specialize through a structured learning path.
* Improves the overall capability of the organization, leading to better project outcomes.

## 2.10 Supporting NASA’s Mission of Excellence

As a high-reliability organization, NASA’s mission is built on a foundation of excellence in every activity, process, and deliverable. Software projects are no exception. Software training ensures that:

* Personnel are well-prepared to deliver reliable, safe, and high-quality software that aligns with NASA’s standards.
* Mission success is supported through higher levels of competence and preparedness.

# 3. Guidance

Training is essential for enabling the software team to meet project requirements, leverage new tools and methodologies, and effectively address domain-specific challenges. Developing and implementing effective training plans ensures the necessary skills, expertise, and knowledge are available to successfully deliver software work products that meet NASA’s rigorous standards for performance, safety, and reliability.

The development, implementation, and tracking of software training plans ensure that all project personnel—including Software Assurance personnel—are equipped with the skills and expertise necessary to successfully execute complex software projects. Continuous evaluation ensures that training remains aligned with evolving needs and promotes excellence in project outcomes. By leveraging NASA’s resources, tools, and programs, teams can ensure competency and adaptability in a dynamic environment.

## 3.1 Development of Training Plans

### 3.1.1 Preparation in the Formulation Phase

The development of software training plans begins in the **Formulation Phase** of the project. As the project's software requirements and performance characteristics are defined, the **Project Team** conducts an assessment of the software-specific skills, domain knowledge, and expertise needed to:

* Develop software deliverables aligned with project requirements.
* Execute key software activities, including development, testing, and assurance.
* Support emerging methodologies, technologies, and tools selected for the project.

The assessment also examines whether the software engineering staff requires **non-software domain expertise** to complement their technical skills (e.g., project management and scheduling). This broader understanding allows personnel to better collaborate with multi-disciplinary teams and manage project goals effectively.

### 3.1.2 Assessment Techniques

The **Project Team** uses multiple approaches to identify existing capabilities and expertise gaps during the formulation phase:

* **Surveys and Interviews**: Task managers, team leaders, and software engineers are engaged to assess the team's existing capabilities and identify skill deficiencies.
* **Reviews of Past Projects**: Lessons learned and historical records from similar projects help ensure robust analysis and provide insight into recurring training needs.

### 3.1.3 Documentation of Training Requirements

Training requirements identified during the assessment are documented in two key plans:

1. **Software Development Plan (SDP) or Software Management Plan (SMP)**: Includes details on project-specific software training needs and plans for implementation (see Topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)).
2. **Center’s Training Plan**: Consolidates training needs across multiple projects at the Center level to prevent duplication and optimize shared training resources (see Section 5.15).

## 3.2 Training Areas

The assessment identifies essential training areas to address skill gaps and ensure personnel have the required expertise for the project. Key software-specific training areas to evaluate include:

### 3.2.1 Software Engineering Training Areas

1. **Software Architecture and Design Development**
   * Training on the principles of design patterns, architectural assessment methods, and scalability.
2. **Process Methods**
   * Training on NASA’s software engineering lifecycle processes, Agile or other development methodologies, and process tools.
3. **Requirements Development**
   * Training on eliciting, documenting, validating, and tracing software requirements.
4. **Configuration Management**
   * Training to ensure rigorous control of baselines, versioning, and change management processes.
5. **Software Development Languages and Environments**
   * Training on programming languages (e.g., C++, Python) and Integrated Development Environments (IDEs) used in the project.
6. **Target Processing Systems**
   * Training for real-time operating systems, embedded frameworks (e.g., cFE/cFS), or hardware-software integration tools.
7. **Verification and Validation Skills**
   * Training on software testing practices, test-driven development, use of automated testing tools, and software quality assurance.
8. **Software Assurance Skills**
   * Training on safety-critical software assurance, software risk identification, defect analysis, and regulatory compliance.

### 3.2.2 Supporting Disciplines

* **Project Management and Scheduling**: Necessary for team members needing leadership roles or participating in core project planning activities.
* **Domain-Specific Knowledge**: Training to complement software knowledge for technical applications such as aerospace systems, cybersecurity, or scientific data processing.

## 3.3 Identify Training Opportunities

Once training needs have been identified, the **Project Team** reviews possible training opportunities with training organizations and course providers. Training modes include formal coursework, self-study, webinars, or on-the-job development. Sources of training include:

### 3.3.1 NASA Training Organizations

1. **Office of the Chief Engineer (OCE)**: Provides engineering-focused curricula.
2. **APPEL (Academy of Program/Project and Engineering Leadership)**: Offers leadership and technical development programs.
3. **Center’s Software Engineering Process Group (SEPG)**: Provides training on center-specific processes and tools.
4. **STEP - SMA Technical Excellence Program**: NASA’s university for Safety and Mission Assurance workforce training, including specialized courses for Software Assurance personnel.
5. **Center Training Officers**: Coordinate training across disciplines at individual NASA Centers.

### 3.3.2 NASA’s Training Tools

* **SATERN (System for Administration, Training, and Educational Resources for NASA)**: A centralized NASA training management platform that provides scheduling, registration, and tracking capabilities for training activities.

### 3.3.3 Collaboration with Providers

If deficiencies are identified in available training (e.g., lack of expertise in new technologies or methodologies), the **Project Team** works with training organizations to:

* Develop tailored content to address gaps.
* Procure external training opportunities to supplement NASA resources.
* Build informal training programs (e.g., mentor-led learning, peer workshops).

## 3.4 Scheduling and Tracking Training

### 3.4.1 Tracking Training Completion

Once training plans are developed for individuals or teams, the training activities are scheduled, monitored, and recorded. Tracking ensures:

* **Completion Adherence**: Verify training completion aligns with planned schedules.
* **Progress Monitoring**: Personnel achieve planned training benchmarks (e.g., 40 hours of annual training as recommended).

### 3.4.2 Use of Center-Specific Processes

Each NASA Center has unique processes and tools to manage training schedules and retention records. These typically align with local procedural requirements. Relevant documentation includes:

* **Training Plans:** Detailed outlines of individual roles and required training per personnel.
* **SDP Section for Training:** Justification of training efforts (or absence of training needs) linked to project activities (see Section 5.08).

## 3.5 Evaluation of Training

### 3.5.1 Assessing Training Effectiveness

The impact of completed training on project performance and software activities should be evaluated periodically using:

* **Surveys:** Collect feedback on training experiences and practical applicability.
* **Lessons Learned:** Incorporate retrospective insights on the effectiveness of training.
* **Performance Improvements:** Measure improvement in productivity, quality, or risk mitigation resulting from training activities.

### 3.5.2 Addressing Deficiencies

Training gaps identified during evaluations can be addressed through remedial courses or refinement of ongoing training efforts. Feedback mechanisms allow refinement of training for future projects.

## 3.6 Additional Training for Software Team Members

### 3.6.1 Beyond Software-Specific Expertise

While software-specific training is critical, **supporting discipline capabilities** help team members build cross-functional expertise that enhances collaboration and project performance. These may include:

1. **Project Leadership and Management**: Training on interdisciplinary collaboration, scheduling, and milestone-focused planning.
2. **Domain Knowledge Training**: Embedded systems, real-time systems, scientific computing, or mission-focused software requirements.

### 3.6.2 Center Coordination

NASA Centers coordinate general and discipline-specific training schedules to optimize resources and ensure availability for team members.

## 3.7 Additional Guidance

Additional guidance related to software training may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-100 - Software Training Funding](/spaces/SWEHBVD/pages/102695484/SWE-100+-+Software+Training+Funding) * [SWE-222 - Software Assurance Training](/spaces/SWEHBVD/pages/105710148/SWE-222+-+Software+Assurance+Training)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.15 - Train - Software Training Plan](/spaces/SWEHBVD/pages/102695676/5.15+-+Train+-+Software+Training+Plan) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Training](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Training) |

# 4. Small Projects

Small projects often face resource constraints, including limitations in time, budget, and personnel. To streamline the process and reduce redundancy, small projects can use adaptive strategies for training planning, such as leveraging pre-existing training plans or creating reusable umbrella training frameworks. Below is an improved version of the small project guidance for meeting training-related requirements.

Small projects often involve teams with diverse backgrounds and overlapping skill sets. By leveraging **pre-existing training plans** or developing **umbrella training plans**, organizations can streamline the process, saving time and resources while still addressing project-specific training requirements. This approach ensures training supports project success while maximizing efficiency for small, iterative, or repetitive project environments.

## 4.1 Guidance for Small Projects

### 4.1.1 Leverage Pre-Existing Training Plans

Small projects can take advantage of existing training plans from similar previous projects to save time and effort. By comparing project requirements, tools, and methodologies, small projects can determine the applicability of earlier plans and adapt them as needed. Key considerations include:

* **Reuse Criteria**: Ensure the pre-existing training plan aligns with the following:
  + The tools and technologies used in the small project (e.g., IDEs, configuration management tools, static analysis tools).
  + The development methodologies employed (e.g., Agile, Scrum, traditional waterfall).
  + The type of software being developed (e.g., embedded systems, flight software, scientific software).
* **Gap Assessment**: Review the pre-existing plan for gaps in training coverage specific to the small project. If additional training is necessary, supplement the plan with targeted courses or resources.
* **Lessons Learned Integration**: Refine the pre-existing plan using lessons learned and feedback from previous projects to ensure it reflects best practices and addresses recurring training gaps.

### 4.1.2 Develop an Umbrella Training Plan for Similar Projects

Organizations that oversee the development of numerous, small, and similar projects can create a reusable **umbrella training plan** to cover shared training needs across these projects. An umbrella training plan serves as a framework and can be tailored to the unique attributes of each small project. Steps for developing and applying an umbrella training plan include:

1. **Analyze Common Training Needs**:

   * Identify shared tools, frameworks, and methodologies commonly used across the organization's small projects.
   * Determine core skills and knowledge that are typically required for project personnel, including:
     + Development skills (e.g., programming languages relevant to the projects like C++, Python).
     + Methodology knowledge (e.g., Agile principles, configuration management processes).
     + Verification, validation, and assurance activities (e.g., testing methods, Software Assurance requirements).
2. **Standardize Core Training Areas**:

   * Define a list of essential training courses or activities that apply to the majority of small projects. These may include:
     + General software engineering topics (e.g., architecture, configuration management, requirements development).
     + Software Assurance basics and safety criticality considerations.
     + Project-specific tools commonly used across projects (e.g., JIRA, Git, specific Integrated Development Environments).
3. **Incorporate Supporting Discipline Training**:

   * Include supplemental training in disciplines tied to small project success, such as basic project management or scheduling.
   * Consider any domain-specific knowledge, such as knowledge of embedded systems if applicable.
4. **Create a Modular Training Approach**:

   * Structure the umbrella plan as a set of training modules to allow individual small projects to select and implement only the applicable sections.
   * Include optional or project-specific courses that may be necessary when uniqueness exists in a project (e.g., introducing specific cybersecurity tools or practices for certain small projects).
5. **Streamline Documentation**:

   * Document the umbrella training plan in a way that is easy to access, interpret, and adapt for each new small project.
   * Provide templates or checklists to ensure project managers can efficiently tailor the plan to the small project’s unique requirements.
6. **Update Periodically**:

   * Ensure the umbrella plan is revisited periodically to integrate updates based on new tools, technologies, methods, and lessons learned from ongoing projects.

### 4.1.3 Tailoring Training Efforts for Small Projects

Small projects may have limited scope, and in some cases, training needs may be minimal. For small projects:

1. **Focus on Just-in-Time Training**:

   * Concentrate on providing short, targeted training opportunities (e.g., webinars, self-paced learning modules) based on immediate project needs.
   * Use pre-existing agency resources such as NASA’s SATERN system for quick access to relevant materials.
2. **Utilize Cross-Training**:

   * Leverage personnel who have already received similar training in previous projects. Cross-trained personnel can transfer their knowledge to other team members through informal mentorship or on-the-job learning.
3. **Confirm Completeness via SDP or SMP**:

   * For small projects with minimal training requirements, document the rationale in the project’s **Software Development Plan (SDP)** or **Software Management Plan (SMP)** training section. For example:
     + State that no new training is required since existing team members already possess the required skills.
     + Reference or attach portions of the umbrella or pre-existing training plan being applied to the project.

## 4.2 Benefits of This Approach

* **Efficiency**: Saves time by avoiding the redevelopment of training plans for each individual project.
* **Cost-Effectiveness**: Reduces expenses associated with identifying and providing redundant training.
* **Consistency**: Ensures all small projects adhere to a standard training baseline while still allowing flexibility for project-specific needs.
* **Scalability**: Provides a framework that scales easily across multiple small projects without significant overhead.

## 4.3 Examples of How Pre-Existing or Umbrella Training Plans May Be Used

* **Similar Small Embedded Software Projects**: An umbrella plan provides baseline training related to real-time operating systems, such as VxWorks, and methodologies like Agile.
* **Flight Software Projects Using cFE and cFS**: A pre-existing plan from a project using the same framework may include training on cFE libraries, flight software integration, and verification methods that can be reused with minor modifications.
* **Agile-Driven Small Projects**: Modular Agile training (e.g., Scrum methodology, JIRA usage) may be shared across several small projects and only expanded if custom workflows are introduced.

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
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-266)

  [NASA OCE Agency PAL.](https://nen.nasa.gov/web/software/nasa-software-process-asset-library-pal "Click to open in new window")

  This NASA-only resource is available to NASA users at https://nen.nasa.gov/web/software/nasa-software-process-asset-library-pal.
* (SWEREF-289)

  [OCE Software Engineering Training](https://nen.nasa.gov/web/software/training "Click to open in new window")

  NESC Academy Software Discipline. Topics include software requirements, design, implementation, architecture, assurance, testing, training, tools, process improvement, best practices, software release, models and simulations, and software research and technology innovation.
* (SWEREF-294)

  [OSMA/NSC's SMA Technical Excellence Program (STEP) program.](https://nsc.nasa.gov/professional-development/safety-and-mission-assurance-technical-excellence-program "Click to open in new window")

  The Safety and Mission Assurance (SMA) Technical Excellence Program (STEP) is a career-oriented, professional development roadmap for SMA professionals.
* (SWEREF-490)

  [History of NASA’s Academy of Program/Project & Engineering Leadership.](http://appel.nasa.gov/about-us/history/ "Click to open in new window")

  Academy of Program/Project and Engineering Leadership (APPEL). Retrieved on September 14, 2015 from http://appel.nasa.gov/about-us/history/.
* (SWEREF-491)

  [Academy of Program/Project & Engineering Leadership (APPEL) - Learning Course Catalog](https://appel.nasa.gov/courses/ "Click to open in new window")

  Access the APPEL curriculum catalog from this URL.
* (SWEREF-513)

  [Mars Climate Orbiter Mishap Investigation Board - Phase I Report](https://llis.nasa.gov/lesson/641 "Click to open in new window")

  Public Lessons Learned Entry: 641.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

* **Lessons Learned: Class D Staffing Model Leading to Insufficient Software Assurance Depth**

**Problem/Observation:**  
Class D mission constraints resulted in limited staffing depth and gaps in key technical and assurance roles. The Anomaly Review Board (ARB) identified several resourcing shortfalls that directly affected flight software (FSW), fault protection (FP), and mission assurance readiness.

**Contributing Factors:**  
• Junior engineers were placed in critical FSW and FP roles without senior technical backstops.  
• Chief Engineer and FSW Lead positions remained vacant for extended periods.  
• Mission operations staffing relied heavily on students rather than experienced operators.  
• No dedicated Anomaly Response Team (ART) was established.

**Resulting Impacts:**  
Resourcing gaps reduced the mission’s ability to maintain technical rigor, ensure independent oversight, and execute timely issue resolution. Critical analyses, reviews, and test preparation activities were delayed or completed without adequate depth, increasing mission risk.

**Relevant SWEHB Guidance:**  
While Class D missions may tailor processes and operate with small teams, certain competencies and roles cannot be reduced or left unfilled.  
• SWE‑017 (Training) requires personnel to be trained and qualified for their assigned roles—tailoring does not waive the requirement for demonstrated competency.  
• SWE‑087 and SWE‑088 (Peer Reviews/Inspections) reinforce the need for independent review, even in resource‑limited environments, to ensure defects are identified early.

**Lesson Learned:**  
Tailoring for Class D missions must not come at the expense of essential systems engineering and software assurance expertise. Critical leadership roles—such as FSW Lead, FP Architect, and Mission Assurance—require experienced personnel, and their absence cannot be offset by junior staff or temporary support. Adequate staffing depth is foundational to maintaining software quality, executing independent reviews, and ensuring readiness throughout the life cycle.

* **Lesson Learned (Starliner CFT):**  
  **Insufficient domain expertise and qualification in critical roles increases the likelihood of misinterpretation and weak assurance.**

  **Project Context:**  
  Derived from Starliner CFT Investigation.

  **Problem/Observation:**  
  Key technical roles operated without robust senior backstops or validated qualifications to the problem domain (e.g., propulsion command and control nuances).

  **Contributing Factors:**

  + Incomplete training and onboarding for complex, safety‑critical subsystems.
  + Over‑reliance on junior personnel in roles requiring seasoned judgment.

  **Impacts:**

  + Requirements and hazard analyses accepted with gaps.
  + Anomalies were not fully understood or resolved due to limited domain fluency.

  **Recommended Practices (Aligned to SWE‑017):**

  + Validate **role‑specific qualifications** (e.g., propulsion control, timing/network effects, flight operations) with objective criteria.
  + Assign **experienced technical mentors** to junior staff in critical roles; document mentorship outcomes.
  + Track **training completion** against a skills matrix tied to subsystem risk.

  **Actionable Checks:**

  + Skills/qualification matrix mapped to roles is current and audited.
  + Training records demonstrate completion and proficiency assessments.
  + Mentorship assignments and outcomes are captured in review artifacts.
* **Mars Climate Orbiter Mishap Investigation Board - Phase I Report[513](#_tabs-<p></p>):** The MCO Mishap Investigation Board (MIB) has determined that the root cause for the loss of the MCO spacecraft was the failure to use metric units in the coding of a ground software file, "Small Forces," used in trajectory models. Specifically, thruster performance data in English units instead of metric units were used in the software application code titled SM\_FORCES (small forces). A file called Angular Momentum Desaturation (AMD) contained the output data from the SM\_FORCES software. The data in the AMD file was required to be in metric units per existing software interface documentation, and the trajectory modelers assumed the data was provided in metric units per the requirements.

Root Cause: Failure to use metric units in the coding of a ground software file, "Small Forces," used in trajectory models.

Contributing causes include:

1. 1. 1. 1. Undetected mis-modeling of spacecraft velocity changes.
         2. Navigation Team unfamiliar with spacecraft.
         3. The trajectory correction maneuver number 5 was not performed.
         4. The system engineering process did not adequately address the transition from development to operations.
         5. Inadequate communications between project elements.
         6. Inadequate operations Navigation Team staffing.
         7. Inadequate training.
         8. The verification and validation process did not adequately address ground software

* **Late and Incomplete Flight Software (FSW) Delivery**

**Incident:**  
The Psyche mission experienced an eight‑month late delivery of the final GNC flight software build, with hundreds of control parameters and fault protection behaviors still undefined. This delay, combined with numerous unresolved software issues, contributed directly to the missed 2022 launch opportunity.

**Lesson Learned:**

* **Early Software Definition & Maturity:** Mission‑critical software requirements, parameters, and behaviors must be fully defined and matured early to prevent cascading delays.
* **Rigorous Defect Disposition:** “Use‑as‑is” and unverified failure dispositions must undergo strict technical review to prevent acceptance of excessive residual risk.

**Implication:**  
Delays and ambiguity in software maturity directly threaten launch schedules, increasing cost, workforce strain, and mission‑risk exposure.

**Additional NASA lessons**

**LLSW18 — Training and Standardization for Hazard Authors and CBCS**

* **Context/Background: Providers lacked training on CBCS requirements and hazard report expectations; reviews inefficient.**
* **Lesson Learned: Provide early training and program‑managed templates/guidelines for hazard reports and CBCS interpretation.**
* **Evidence/Observation: Late/walk‑on comments; mismatches between L2 needs and L3 ability; excessive IHCRs.**
* **Cause(s): Insufficient trained personnel; unclear expectations.**
* **Recommendation/Corrective Action: Develop training materials; mentor programs; Client Safety Engineer support; standardized templates.**
* **Implementation Guidance: SWE017 (training) and SWE024 (plan tracking).**
* **Success Criteria/Verification: Reduced late comments; improved hazard report quality; faster review cycles.**
* **Applicability/Scope: All providers and IPs producing safety data.**
* **Related Standards/Requirements: SWE017, SWE024.**

**LLSW01 — Standards for Heritage Software Reuse and Testing**

* **Context/Background: Legacy flight software reuse assumed minimal testing; defects emerged late.**
* **Lesson Learned: Treat heritage software as if new—perform full requirements validation, interface verification, regression testing, environmental qualification.**
* **Evidence/Observation: PPE planned legacy reuse; issues remained open at pause; assumptions delayed defect discovery.**
* **Cause(s): Belief prior flight obviates testing; lack of reuse standards.**
* **Recommendation/Corrective Action: Establish project‑level reuse standards specifying test scope, verification criteria, acceptance gates.**
* **Implementation Guidance: Embed reuse criteria in plans (SWE013), trace reused functionality to req/design/tests (SWE052/059/064/072), determine safety impacts (SWE133/134).**
* **Success Criteria/Verification: Reuse plan; executed test campaigns; bidirectional traceability; IV&V closure; defect rates comparable to new development.**
* **Applicability/Scope: All mission/safety‑critical software; heritage and third‑party components.**
* **Related: SWE027, SWE013, SWE050, SWE052/059/064/072, SWE133/134.**

**LLSW11 — COTS/Reuse Software Policy for Safety‑Critical Systems**

* **Context/Background: Teams struggled to apply NPRs to COTS/reuse; safety controls missing in COTS; insight difficult.**
* **Lesson Learned: Create program‑specific COTS/reuse policy clarifying applicability of NPR****7150.2/standards to CBCS, including safety control expectations.**
* **Evidence/Observation: Reliability/availability/upgrade issues with COTS critical items; provider resistance to design insights.**
* **Cause(s): Undefined requirements/expectations; lack of upfront safety control provisions.**
* **Recommendation/Corrective Action: Update Agency NPRs/standards (or tailor) for COTS in human‑rated contexts; perform early feasibility against safety controls.**
* **Implementation Guidance: SWE027, SWE133/134, SWE158.**
* **Success Criteria/Verification: Documented COTS policies; hazard controls traceable to requirements; successful verification closeouts.**
* **Applicability/Scope: Safety‑critical CBCS, avionics, integrated systems.**
* **Related: SWE027, SWE133, SWE134, SWE158.**

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Project specific training requirements should be identified and tracked](https://software.gsfc.nasa.gov/lesson-details/54/). **Lesson Number 54**: The recommendation states: "Project specific training requirements should be identified and tracked."
* [In prelaunch ensure each subsystem gives training to the FOT](https://software.gsfc.nasa.gov/lesson-details/102/). **Lesson Number 102**: The recommendation states: "Reserve more time in prelaunch to ensure each subsystem gives training to the FOT."
* [Plan and initiate team training early](https://software.gsfc.nasa.gov/lesson-details/282/). **Lesson Number 282**: The recommendation states: "The PDL needs to think about/identify and document all knowledge the team members need to have, including topics like how to use the OTS products that will be incorporated into the project’s software. The PDL should do this early, so training opportunities/offerings can be timed appropriately and delivered before that knowledge/skill is needed by the project."
* [Ensure that early career team members receive adequate support](https://software.gsfc.nasa.gov/lesson-details/329/). **Lesson Number 329**: The recommendation states: "Be proactive in providing support to early career team members."
* [Expose team members to multiple aspects of the FSW](https://software.gsfc.nasa.gov/lesson-details/330/). **Lesson Number 330**: The recommendation states: "Prevent silo-ing by exposing team members to multiple aspects of the FSW."

# 7. Software Assurance

**SWE-017 - Project and Software Training**

3.4.1 The project manager shall plan, track, and ensure project specific software training for project personnel.

This requirement ensures that all personnel, including Software Assurance (SA) personnel, receive the necessary project-specific software training to effectively support software development activities. Training is critical for ensuring competence in project tools, processes, methodologies, and systems. Software Assurance personnel must confirm that training requirements are planned, tracked, and completed, including any discipline-specific training needed to fulfill their oversight roles.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that any project-specific software training has been planned, tracked, and completed for project personnel, including software assurance and software safety personnel.

2. Confirm that software assurance and software safety personnel have completed the appropriate software assurance and/or software safety training to satisfactorily conduct assurance and safety activities.

## 7.2 Software Assurance Products

### 7.2.1 Software Assurance Training Plan Compliance Report

**Purpose**: Provides an assessment of whether the required project-specific software training for SA personnel has been planned, tracked, and completed.  
**Contents**:

* Documentation of SA training requirements, including:
  + Project-specific training topics (e.g., Agile, cFE/cFS, embedded systems, tools).
  + Basic software assurance training requirements.
* Tracking information on planned training courses, participants, and completion status.
* Identification of training gaps for SA personnel and risks related to incomplete training.
* Recommendations for addressing training gaps or delays in completion.

### 7.2.2 Training Records for SA Personnel

**Purpose**: Maintains up-to-date training completion records for project-specific software training for SA personnel.  
**Contents**:

* Name, role, and discipline of each SA personnel.
* A log of training courses completed, including:
  + Course names and descriptions (e.g., Intermediate Software Assurance, Agile Development, cFE/cFS training).
  + Training hours documented for each participant.
  + Dates of training completion.
* Tracking totals for completed training hours compared to recommended benchmarks (e.g., 40 hours annually).
* Status of in-progress or omitted training.

### 7.2.3 SA Professional Development Plan Evaluation

**Purpose**: Evaluates the professional development and baseline training for SA personnel as aligned to agency-level programs like the **SMA Technical Excellence Program (STEP)**.  
**Contents**:

* List of STEP-required courses and training milestones for SA personnel (e.g., Intermediate Software Assurance, Software Testing, Agile Software Development).
* Identification of SA personnel training progress by STEP level (Levels 1–4).
* Assessment of whether SA personnel meet or exceed recommended training benchmarks.
* Recommendations for additional professional development activities, such as advanced SA discipline-specific training or cross-discipline training.

### 7.2.4 Training Gaps and Risk Assessment Report

**Purpose**: Identifies and analyzes risks or issues resulting from incomplete or missing training for SA personnel and other project personnel performing assurance tasks.  
**Contents**:

* Analysis of training shortfalls for SA personnel (e.g., incomplete or delayed project-specific training).
* Risks to project outcomes or software quality resulting from untrained or undertrained personnel.
* Proposed mitigation actions to address gaps, including scheduling additional training or leveraging experienced personnel to fill roles in the short term.

## 7.3 Metrics

Metrics measure the progress, coverage, and completion of software training activities for both Software Assurance and general project personnel.

### Key Metrics

### 7.3.1 Training Completion Metrics:

* **% of Required Training Completed by Project SA Personnel:**
  + Tracks the percentage of planned training activities that are completed by each SA team member.
* **% of Project Personnel Completing Project-Specific Training Against Planned Schedule:**
  + Tracks overall project personnel training adherence to the scheduled training plan.

### 7.3.2 Training Gaps Metrics:

* **Avg. Training Hours per SA Personnel vs. Benchmark (40 hours):**
  + Measures whether SA personnel meet the recommended benchmark for training hours annually.
* **Training Late Completion Rate:**
  + Tracks how many training activities were completed late versus planned milestones.

### 7.3.3 STEP Participation Metrics (for SA Professional Development):

* **% of SA Personnel Completing Level 1–4 STEP Courses:**
  + Tracks STEP program progression for SA personnel, helping ensure they meet discipline-specific curriculum goals.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

### Step 1: Define Training Requirements

* Collaborate with the project team to determine the specific software training needs for the project:
  + Confirm project-specific training topics (e.g., Agile methodology, cFE/cFS, operating environments, embedded systems, tools like JIRA/Confluence).
  + Confirm training needs for software processes and tools (e.g., static analysis tools, version control systems, build tools).
  + Gather basic training needs and orientation requirements for SA personnel based on the project processes, goals, and challenges.

### Step 2: Plan, Track, and Verify Training Activities

* Review the **Software Management/Development Plan (SMP/SDP)** and **Software Assurance Plan (SAP)** to identify required training activities for SA and project personnel.
* Ensure training activities include:
  + Project resources for software training (e.g., specific Agile methodology training, cFE/cFS tools).
  + General SA and safety training (such as SATERN and STEP courses).
  + Orientation sessions on system goals, requirements, and the project lifecycle.
* Establish a mechanism for tracking training progress (e.g., training logs, SATERN progress transcripts).

### Step 3: Develop and Monitor Training Records

* Maintain accurate and up-to-date logs of SA personnel training, including planned courses and completed courses.
* Access records from SATERN, STEP, and other training platforms.
* Monitor individuals against benchmarks, including the recommended yearly 40 hours of training.

### Step 4: Mitigate Training Gaps and Risks

* Identify personnel who have not completed their required training on time.
* Assess risks to project outcomes or SA effectiveness due to incomplete or inadequate training.
* Develop mitigation plans, such as immediate training sessions for essential topics or reallocating trained personnel to critical roles until gaps are addressed.

### Step 5: Include Professional Development Initiatives

* Recommend SA personnel complete **STEP Levels 1–4** as part of their professional development.
* Verify that mandatory SA discipline-specific training (e.g., Intermediate Software Assurance, Agile, and Software Testing) is included in training plans or benchmarked for professional growth.

### 7.4.1 Examples of Training Topics:

* **Methodologies**: Agile Development (e.g., Scrum), Model-Based Assurance.
* **Tools**: Static code analysis, JIRA, Confluence, IDEs.
* **Frameworks**: cFE/cFS or real-time operating systems.
* **Processes**: Software risk management, safety-critical software assurance planning.

By consistently implementing the above guidance, Software Assurance personnel can ensure training requirements are thoroughly addressed, tracked, and completed, helping to meet this requirement and support successful project execution.

## 7.5 Additional Guidance

Additional guidance related to software training may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-100 - Software Training Funding](/spaces/SWEHBVD/pages/102695484/SWE-100+-+Software+Training+Funding) * [SWE-222 - Software Assurance Training](/spaces/SWEHBVD/pages/105710148/SWE-222+-+Software+Assurance+Training)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.15 - Train - Software Training Plan](/spaces/SWEHBVD/pages/102695676/5.15+-+Train+-+Software+Training+Plan) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

See also [SWE-222 - Software Assurance Training](/spaces/SWEHBVD/pages/105710148/SWE-222+-+Software+Assurance+Training) for more on funding for SA training.

# 8. Objective Evidence

Objective evidence substantiates compliance with the requirement to plan, track, and complete project-specific software training activities for all personnel involved in software development, including Software Assurance personnel.

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

## 8.1 Objective Evidence to Be Collected

### 8.1.1 Training Planning Evidence:

* Training schedules or plans showing planned software training activities (e.g., cFE/cFS, Agile Development).
* Documentation from Software Management/Development Plans (SMP/SDP) or Software Assurance Plans (SAP) identifying required training topics for SA and software personnel.

### 8.1.2 Training Completion Evidence:

* Training logs confirming completion of required project-specific training for SA personnel:
  + Types of training completed (technical, tool-specific, process, methodology).
  + Completion dates.
  + Documented training hours (total and per course).
* STEP or SATERN transcripts for SA personnel tracking progress toward completion of Level 1–4 courses.

### 8.1.3 Orientation Evidence:

* Material from project orientation sessions provided to project personnel, including SA, covering system requirements, concepts of operations, and project-specific goals.
