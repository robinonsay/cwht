# SWE-036 - Software Process Determination

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695414. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination

SWE-036 - Software Process Determination

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695414)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695414&showCommentArea=true&showComments=true#addcomment)

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

3.1.6 The project manager shall establish and maintain the software processes, software documentation plans, list of developed electronic products, deliverables, and list of tasks for the software development that are required for the project’s software developers, as well as the action required (e.g., approval, review) of the Government upon receipt of each of the deliverables.

## 1.1 Notes

A list of typical software engineering products or electronic data products used on a software project is contained in Chapter 6 of this directive. The software activities should include plans for software product verification and validation activities, software assurance, methods, environments, and criteria for the project.

## 1.2 History

Click here to view the history of this requirement: SWE-036 History

SWE-036 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.5.5 The project shall determine which software processes, activities, and tasks are required for the project. |
| Difference between A and B | Added to list of required items to be determined by the PM; Added software supplier to the scope. |
| B | 3.12.5 The project manager shall determine which software processes, software documents, electronic products, software activities, and tasks are required for the project and software suppliers. |
| Difference between B and C | Changed "determine" to "establish and maintain"; Expanded the scope of required items for the project to include software documentation plans, list of developed electronic products, deliverables, and list of tasks for the software development; Added requirement to list the action required of the Government upon receipt of each of the deliverables. |
| C | 3.1.6 The project manager shall establish and maintain the software processes, software documentation plans, list of developed electronic products, deliverables, and list of tasks for the software development that are required for the project’s software developers, as well as the action required (e.g., approval, review) of the Government upon receipt of each of the deliverables. |
| Difference between C and D | No change |
| D | 3.1.6 The project manager shall establish and maintain the software processes, software documentation plans, list of developed electronic products, deliverables, and list of tasks for the software development that are required for the project’s software developers, as well as the action required (e.g., approval, review) of the Government upon receipt of each of the deliverables. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

Projects evaluate the environment (e.g., organization, funding, size, personnel) in which they plan to develop software. From this evaluation, they choose an appropriate set of processes, tasks, and activities to develop software that meets their needs. The planning down to the activity and task levels assures that only the appropriate processes are selected from the ones available to the project. Further evaluation of these processes will determine the level of software resources that the project team needs to include in the planning documentation and funding requests.

This requirement ensures that project managers establish and maintain comprehensive and structured software processes, tasks, documentation plans, electronic deliverables, and review/approval actions. It promotes consistency, quality, transparency, and regulatory compliance across the software development life cycle while enabling collaboration and traceability. The inclusion of government oversight actions and standardized processes ensures project deliverables satisfy mission-critical requirements while adhering to regulatory and safety mandates. **This structured approach is essential to managing the complexity of aerospace software development and ensuring mission success.**

## 2.1 Rationale Details

This requirement ensures that the software development process is **structured, well-documented, and traceable** from planning to delivery, focusing on a clear delineation of tasks, deliverables, and government oversight processes. By establishing robust documentation and processes, this requirement creates transparency and accountability for all project stakeholders while minimizing risks associated with software engineering activities. Below is the rationale for this requirement:

### 2.1.1 Ensuring Consistency Through Defined Software Processes

* **Why It Matters:**
  + Aerospace software development involves complex activities that require standardization and consistency to meet mission-critical objectives. Without defined processes, development efforts can be chaotic, leading to variability in quality and performance across deliverables.
  + Clear software processes create a shared understanding of development standards, methodologies, and expectations for all team members, helping mitigate risks such as missed milestones or overlooked requirements.
* **Rationale:**
  + Establishing and maintaining structured software processes lays the foundation for predictable and consistent results, ensuring all tasks align with the mission-specific goals, technical requirements, and safety standards.

### 2.1.2 Providing Transparency for Tasks and Deliverables

* **Why It Matters:**
  + Defining a concise list of tasks and electronic deliverables enables stakeholders, such as project managers, developers, and government representatives, to understand and track exactly what is expected throughout the development life cycle.
  + Deliverables without predefined approval or review actions can result in confusion, bottlenecks, miscommunication, or delays in project milestones.
* **Rationale:**
  + Documentation of tasks and deliverables ensures clear communication, transparency, and accountability for all parties involved, helping to streamline project development and decision-making.

### 2.1.3 Supporting Effective Oversight and Governance

* **Why It Matters:**
  + Aerospace software projects often involve government oversight or external review, such as regulatory compliance or mission-critical sign-offs. Without a formal process defining the actions required (e.g., approval or review), stakeholders may struggle to process deliverables or reach timely decisions.
  + Explicitly outlining government roles (e.g., when approvals are necessary and who provides them) ensures deliverable review processes remain efficient while avoiding misunderstandings.
* **Rationale:**
  + Mapping out oversight actions connected with deliverables ensures compliance with governance requirements, expediting feedback loops and approvals without sacrificing quality.

### 2.1.4 Facilitating Quality Control and Assurance

* **Why It Matters:**
  + Software processes should address **verification, validation (V&V), and assurance activities** to ensure the delivered products consistently meet customer expectations, functionality requirements, and compliance standards.
  + Documenting software activities (including methods, tools, environments, and criteria for verification and validation) ensures deliverables undergo rigorous quality checks before being approved for operational use.
* **Rationale:**
  + Including quality control-related plans ensures that the software undergoes thorough review and testing, identifying and addressing defects or gaps before they affect downstream project phases.

### 2.1.5 Promoting Long-Term Traceability

* **Why It Matters:**
  + Aerospace software projects frequently span multiple phases over several years, involving iterative development, integration, testing, and maintenance efforts. Without robust documentation, critical decisions, processes, or criteria may become difficult to trace during audits or system upgrades.
  + Maintaining comprehensive plans and records ensures all steps taken—from software development to government approvals—are traceable for certification, system reuse, and eventual retirement.
* **Rationale:**
  + Documenting processes, tasks, and deliverables ensures that all efforts are auditable, enabling system evolution, compliance reviews, and knowledge transfer for future projects.

### 2.1.6 Reducing Risks Associated With Missing or Inadequate Documentation

* **Why It Matters:**
  + Inadequate documentation of deliverables, electronic products, or planned tasks increases the likelihood of errors, rework, and miscommunication during critical phases. This can result in delays, non-compliance with safety standards, or failed integration.
  + Comprehensive documentation reduces the risk of missed expectations and gaps between development actions and requirements.
* **Rationale:**
  + By requiring detailed documentation plans up front, this requirement minimizes risks such as schedule overruns or deliverables requiring costly retroactive fixes.

### 2.1.7 Supporting Collaboration Among Stakeholders

* **Why It Matters:**
  + Large-scale aerospace projects require collaboration across multiple teams, departments, contractors, and government bodies. Establishing software processes and deliverable expectations ensures that all contributing groups are aligned and can collaborate effectively.
  + Without a clear process framework, communication among teams can become siloed, leading to inefficiencies and misunderstandings.
* **Rationale:**
  + By creating standardized processes and tasks, the project fosters better collaboration among all stakeholders, ensuring the software deliverables meet everyone’s expectations.

### 2.1.8 Aligning with Mission Objectives

* **Why It Matters:**
  + Deliverables and software processes should align directly with mission objectives (e.g., optimizing system reliability, supporting space-based operations, ensuring real-time communications). Without alignment, tasks may deviate from the project’s ultimate purpose.
  + Activities must also be spelled out clearly to avoid oversights in critical mission-related criteria, such as environmental effects (e.g., microgravity conditions) or operational requirements (e.g., system response times).
* **Rationale:**
  + Documented processes and deliverable plans ensure that software development efforts consistently align with mission-critical requirements and objectives.

### 2.1.9 Facilitating Efficient Resource Allocation

* **Why It Matters:**
  + Software development planning not only affects schedules but also directly impacts resource allocation (e.g., developer efforts, budgets, tools). Undefined processes or insufficient task clarity can waste resources and cause inefficiencies in allocation.
* **Rationale:**
  + Maintaining documentation for tasks and deliverables ensures the project can plan and optimize resource allocation, reducing waste and ensuring efficient use of manpower and tools.

### 2.1.10 Enabling Tailored Processes

* **Why It Matters:**
  + Aerospace projects often require tailored methodologies based on mission scope (e.g., high-risk human spaceflight missions versus lower-risk robotic systems). Processes, documentation plans, and deliverables may need tailoring to match customer requirements while maintaining compliance with overarching requirement.
* **Rationale:**
  + This requirement encourages project managers to tailor processes and deliverables to meet unique mission requirements while adhering to general standards.

### 2.1.11 Supporting System Integration

* **Why It Matters:**
  + Software components often need to integrate seamlessly with hardware systems, legacy systems, or other mission elements (e.g., ground-based operations communicating with orbiting satellites). Undefined deliverables can lead to incomplete integration planning.
* **Rationale:**
  + Documenting specific electronic products and processes related to integration ensures smoother transitions between subsystems without risks of incompatibility.

### 2.1.12 Ensuring Comprehensive Verification and Validation (V&V)

* **Why It Matters:**
  + Software involve complex interdependencies, and incomplete plans for verification and validation (V&V) activities might result in faulty systems slipping through reviews and potentially causing mission failures.
* **Rationale:**
  + Plans for **software assurance, environments, and criteria** ensure robust V&V coverage and accountability throughout the project life cycle.

## 2.2 Notes: Practical Implementation

This requirement ties directly into Chapter 6 of the directive, **Recommended Software Records Content**, which provides examples of typical deliverables and electronic products. The guidance within Chapter 6 can serve as a starting point for project managers developing their documentation and software development plans. Listed elements may include:

* Software Development Plan (SDP),
* Software Test Plans,
* Code repositories,
* Verification and Validation Reports, among others.

# 3. Guidance

The following guidance provides clarity and detail to support the successful planning, selection, and execution of software processes. The aim is to ensure the **formulation phase** lays a strong foundation for the software development life cycle through compliance with **NPR 7150.2 [083](#_tabs-<p></p>)** , alignment with mission objectives, and utilization of best practices.

Investing time and resources during the **formulation phase** ensures that the project’s software processes are well-documented, appropriately tailored, and in full compliance with NASA standards and best practices. By leveraging these processes, teams gain clarity, alignment, and accountability, setting the foundation for a successful project outcome that is efficient, cost-effective, and mission-ready.

## 3.1 Software Process

The **formulation phase** of a software project is critical for establishing the structure and framework required to guide the development and eventual deployment of the software. During this phase, the project team focuses on:

1. **Defining Customer Needs and System-Level Requirements:**

   * Engaging with customers and stakeholders to understand operational expectations and translate these into well-documented system and software requirements.
   * Evaluating constraints such as performance, safety, environmental factors, and integration with existing systems.
2. **Planning and Decision-Making:**

   * Developing high-level project and software management plans that direct all software efforts and activities.
   * Making **make-versus-buy decisions** to determine whether software components and tools will be developed in-house, purchased, or outsourced.
   * Creating the **Work Breakdown Structure (WBS)** to map out actionable tasks, timelines, and deliverables.
   * Performing **software safety assessments** to identify and address potential risks early in the project.
3. **Specifying Deliverables and Work Products:**

   * Establishing a comprehensive list of **primary project deliverables and work products,** including but not limited to software code, documentation, electronic data products, test reports, and configuration records.

### 3.1.1 Core Software Planning Documents

The systematically developed planning documents serve as reference guides for managing and executing the software processes effectively. These plans align all software activities with project objectives while meeting NASA’s regulatory requirements.

The **core set of software plans** includes, but is not limited to:

1. **Software Development or Management Plan (SDP/SMP)** – See [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan).

   * Documents the overarching strategy for managing the software project, including roles, responsibilities, scheduling, and resource allocation.
2. **Configuration Management Plan (SCMP)** – See [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan).

   * Defines the process for managing changes to the software system and tracking versions of software work products.
3. **Test Plan (STP)** – See [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan).

   * Outlines the methodology, criteria, and procedures for verifying and validating software functionality and performance.
4. **Maintenance Plan** – See [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan).

   * Details how the software will be sustained, enhanced, or retired after delivery, including post-deployment support requirements.
5. **Software Assurance Plan** – See [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan).

   * Describes the methods for ensuring software quality, reliability, and compliance with safety standards through quality assurance and auditing.

### 3.1.2 Single Document vs. Standalone Plans:

Depending on the size, complexity, and scope of the project, these plans may be:

* **Combined into a single master document** (e.g., for small projects), or
* **Maintained as standalone plans** (e.g., for larger or more complex projects). The choice should ensure clarity and accessibility.

### 3.1.3 Process Selection and Tailoring

The selection of **software processes** in the formulation phase directly impacts the efficiency and outcomes of the project. These processes should be chosen based on:

1. **Characteristics of Desired Work Products:**

   * Understanding the nature, complexity, and criticality of the software deliverables.
   * Analyzing mission objectives, system requirements, and stakeholder priorities.
2. **Requirements of NPR 7150.2:**

   * Ensuring all selected activities and tasks comply with NPR 7150.2 standards, with appropriate tailoring for project-specific requirements.

#### Steps in Process Selection:

* Identify the processes, activities, and tasks necessary to achieve project objectives.
* Tailor processes to:
  + Fit the project's scope and constraints.
  + Align with **system-level technical requirements** defined in NPR 7123.1 [041](#_tabs-<p></p>) .
* Establish clear ownership of processes between the project and any software suppliers.

### 3.1.4 Other SWE Requirements on Processes

The following SWEs and guidelines provide further insight into establishing, benchmarking, and maintaining software processes:

1. **Process Establishment and Center-Level Improvement Plans:**

   * Focuses on developing and maintaining project-level and center-wide software processes.
     + [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes)
     + [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans)
2. **Benchmarking and Appraisals:**

   * Highlight the value of benchmarking software engineering practices and conducting appraisals to evaluate process maturity.
     + [SWE-004 - OCE Benchmarking](/spaces/SWEHBVD/pages/102695394/SWE-004+-+OCE+Benchmarking)
     + [SWE-129 - OCE NPR Appraisals](/spaces/SWEHBVD/pages/102695491/SWE-129+-+OCE+NPR+Appraisals)
     + [SWE-209 - Benchmarking Software Assurance and Software Safety Capabilities](/spaces/SWEHBVD/pages/102695329/SWE-209+-+Benchmarking+Software+Assurance+and+Software+Safety+Capabilities)
     + [SWE-221 - OSMA NPR Appraisals](/spaces/SWEHBVD/pages/105709899/SWE-221+-+OSMA+NPR+Appraisals)
3. **Reviewing Processes at Key Milestones:**

   * Defines milestones for assessing the effectiveness and appropriateness of software processes.
     + [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones)

### **3.2 Process Resources**

To strengthen the planning and implementation of software processes, projects may leverage the following resources:

### **3.2.1 Internal NASA Resources:**

1. **Software Processes Across NASA (SPAN) [197](#_tabs-<p></p>) :**

   * SPAN provides NASA-wide process assets that aid in selecting and customizing software development activities.
2. **Center Process Asset Libraries (PALs):**

   * Serve as repositories of processes, templates, and examples that align with projects executed at respective NASA Centers.

### 3.2.2 External Best Practices and Standards:

1. **Capability Maturity Model Integration for Development (CMMI-Dev): [153](#_tabs-<p></p>)**

   * A process improvement framework that provides guidance on developing high-quality software products.
   * Emphasizes rigor in documenting and managing project processes.
2. **NPR 7123.1: NASA Systems Engineering Processes and Requirements: [041](#_tabs-<p></p>)**

   * Establishes a core set of Agency-level processes for managing technical development efforts.
3. **AS9100C Aerospace Quality Management Standard: [372](#_tabs-<p></p>)**

   * Lays out a process-based approach to managing quality, emphasizing the integration and coordination of processes.

### 3.2.3 Execution of Software Processes

The tailored processes adopted during the formulation phase are executed through tasks and activities spanning the entire software development life cycle. Each process step should include:

1. **Planned Tasks and Activities:**

   * Align activities with project schedules to ensure timely execution of software processes.
2. **Periodic Review and Refinement:**

   * Review processes at defined **milestones** or as the project evolves to ensure continued alignment with objectives.
3. **Outcome Management:**

   * Ensure the execution of processes directly supports the generation of expected outcomes and deliverables.

#### Guidance from NPR 7123.1:

* NPR 7123.1 emphasizes breaking each process into detailed tasks with traceable outcomes. These tasks form the basis for managing technical efforts and ensuring mission success.

## 3.3 Role of the Agency Software Manager

The **Agency Software Manager** serves as an expert resource for:

* Clarifying software process-related requirements.
* Confirming compliance with NPR 7150.2 and related directives.
* Providing advice on process selection, tailoring, and implementation.

The selections of the processes to support and execute the above planning and definition activities typically are based on an analysis of the desired software work products and their characteristics, and on a determination of which activities and tasks are needed to produce these work products. The selected processes must meet the requirements of the NPR 7150.2 [083](#_tabs-<p></p>) that apply to the project.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) * [SWE-004 - OCE Benchmarking](/spaces/SWEHBVD/pages/102695394/SWE-004+-+OCE+Benchmarking) * [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-129 - OCE NPR Appraisals](/spaces/SWEHBVD/pages/102695491/SWE-129+-+OCE+NPR+Appraisals) - * [SWE-209 - Benchmarking Software Assurance and Software Safety Capabilities](/spaces/SWEHBVD/pages/102695329/SWE-209+-+Benchmarking+Software+Assurance+and+Software+Safety+Capabilities) * [SWE-221 - OSMA NPR Appraisals](/spaces/SWEHBVD/pages/105709899/SWE-221+-+OSMA+NPR+Appraisals)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement)      * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

Small projects often have fewer resources, simpler objectives, and a condensed timeline. To ensure efficiency while maintaining the required rigor, software process guidance for small projects emphasizes **streamlined planning, tailored processes, and scalable documentation practices**. The goal is to balance simplicity with compliance, quality, and mission objectives while avoiding undue overhead.

This streamlined guidance allows small projects to focus on the **essentials of software process planning and execution** while adhering to NASA standards. By simplifying documentation and tailoring processes, small teams can maintain efficiency without sacrificing quality, compliance, or mission success. Leveraging NASA resources, templates, and oversight mechanisms ensures small projects operate within a structured yet flexible framework.

## 4.1 Key Challenges for Small Projects

1. Limited resources (manpower, time, and budget).
2. Less complex requirements compared to large-scale projects.
3. "Small does not mean insignificant" — software may still be mission-critical or safety-sensitive.
4. A need to meet NASA standards (e.g., NPR 7150.2 [083](#_tabs-<p></p>) ) while minimizing administrative burden.

To address these challenges, small projects should focus on **tailored approaches and scaled-down documentation** while maintaining traceability, transparency, and compliance.

## 4.2 General Principles for Small Projects

1. **Simplify Planning:** Focus only on essential processes and deliverables that directly support technical and project objectives.
2. **Combine Documentation:** Where appropriate, consolidate software plans into fewer documents to reduce administrative workload.
3. **Tailor Processes:** Use streamlined processes that meet project-specific needs rather than relying on one-size-fits-all methodologies.
4. **Prioritize Oversight:** Ensure visibility into critical milestones and deliverables without introducing unnecessary complexity.
5. **Leverage Templates and Best Practices:** Use existing NASA-wide templates and resources to accelerate planning and reduce customization efforts.

## 4.3 Steps for Software Process Implementation in Small Projects

### 4.3.1 Early Planning

* **Objectives:** Start with defining clear goals and deliverables tied to mission requirements.
* Develop a **project scope** focused on achieving objectives with minimal complexity.
* Identify essential customer needs and system-level requirements (e.g., safety-sensitive functions, performance thresholds).

### 4.3.2 Core Plans (Consolidated Documentation)

For small projects, reduce complexity by consolidating key software planning documents. For example:

* Combine a **Software Development Plan (SDP), Configuration Management Plan, and Test Plan** into a single "Software Management Plan."
  + See [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan), [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan), [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
* Include only essential sections related to project goals:
  + Development tasks and milestones.
  + Code configuration and version control methods.
  + Testing criteria for functionality and validation.

### 4.3.3 Leverage Existing Processes

* **Use Center Process Asset Libraries (PALs):** These offer pre-approved templates and streamlined guidance. Align small project processes with these established resources to save time and ensure consistency.
* **NASA-SPAN Resources [197](#_tabs-<p></p>) :** Access SPAN to identify and adopt simplified development methodologies suitable for small projects.

### 4.3.4 Tailor Standards

While NPR 7150.2 must be followed, apply tailoring approaches to fit the reduced scale of the project:

* Focus on requirements that directly impact deliverables (e.g., safety-critical software or operational functionality).
* Reduce unnecessary overhead, such as extensive reporting on minor components.

## 4.4 Recommended Streamlining of Core Processes

### 4.4.1 Requirements Management

* Manage requirements in small, concise sets based on customer priorities.
* Use simple tools (e.g., spreadsheets or lightweight requirements management software) instead of complex systems for tracking.

### 4.4.2 Configuration Management

* Develop a small, efficient version control strategy (e.g., Git) for managing changes to source code and documentation.
* Avoid unnecessary bureaucracy—focus on tracking only critical changes that impact functionality or compliance.

### 4.4.3 Testing

Focus on essential testing activities tied to key project risks:

* Use **automated testing frameworks** (where possible) for faster validation.
* Prioritize tests for key functionalities, system integration, and performance thresholds.
* Reduce non-critical test scenarios unless required for regulatory compliance.

### 4.4.4 Maintenance Planning

For small projects, maintenance plans can be scoped minimally:

* Emphasize essential post-delivery tasks, such as bug fixes, documentation updates, and periodic software reviews.
* Use concise maintenance documentation tailored for limited scope iterations.

### **4.4.5** Assurance

Software assurance efforts should focus on core quality attributes:

* Simplify assurance activities where risks are low.
* Consolidate reviews, audits, and compliance checks into fewer steps.

## 4.5 Review Milestones for Small Projects

Small projects should include fewer, clearly defined review milestones to track progress and ensure quality without overburdening the team:

1. **Kickoff Meeting:** Review customer requirements, scope, and process tailoring plans.
2. **Requirements Review:** Ensure customer needs are fully defined and actionable.
3. **Critical Design Review:** Validate that the software architecture and fundamental decisions align with project goals.
4. **Test Readiness Review:** Confirm testing plans and resources before verification/validation activities begin.
5. **Software Approval/Delivery Review:** Final review and approval of all deliverables before software release to the customer.

## 4.6 Templates and Tools

Small projects can benefit from simplified templates and tools to expedite documentation and minimize overhead:

1. Pre-approved templates from **NASA Center Process Asset Libraries (PALs)** or SPAN.
2. Lightweight tools for requirements management, testing tracking, and configuration (e.g., Excel, JIRA, GitHub).
3. Streamlined guidelines from industry standards (e.g., CMMI-Dev for small-scale applications).

## 4.7 Role of Oversight

Small projects must still comply with regulations and oversight requirements:

* Engage the **Agency Software Manager** early to confirm compliance and identify tailored approaches for NPR 7150.2 adherence.
* Ensure required milestones are met for mission-critical functions, even at reduced complexity.

## 4.8 Example of Consolidated Software Management Plan (For Small Projects)

A single **Software Management Plan** may include:

1. **Introduction:** Project scope and objectives.
2. **Development Approach:** Processes to be followed (planning, implementation, testing, assurance, and delivery).
3. **Configuration Management:** High-level procedures for tracking code and documentation changes.
4. **Testing Strategy:** Key verification and validation activities, including acceptance criteria.
5. **Oversight Plans:** Approval actions to be performed, deliverable review steps.
6. **Maintenance Scope:** Brief post-delivery software sustainment activities.

This plan consolidates all essential processes, enabling the team to maintain focus and simplicity.

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
* (SWEREF-153)

  [CMMI © for Development, Guidelines for Process Integration and Product Improvement,](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=31054 "Click to open in new window")

  Chrissis, M.B., Konrad, M., Shrum, S., This book is the definitive reference for CMMI-DEV Version 1.3. It describes best practices for the development and maintenance of products and services across their lifecycle. 3rd Edition, 2010, Addison-Wesley Professional, ISBN: 0-321-71150-5
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-372)

  [Quality Management Systems - Requirements for Aviation, Space and Defense Organizations,](http://standards.sae.org/as9100d/ "Click to open in new window")

  SAE AS9100D, ", 2016. NASA users can access standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of standards.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
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

* **Flight Software Engineering Lessons. Lessons Learned 2218**[572](#_tabs-<p></p>): "The engineering of flight software is a major consideration in establishing JPL project total cost and schedule because every mission requires a significant amount of new software to implement new spacecraft functionality. Constraints to the development and testing of software concurrent to engineering the rest of the flight system have led to flight software errors, including the loss of some missions. The findings of several JPL studies and flight mishap investigations suggest several recommendations for mitigating software engineering risk."

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* The FSW documentation should be made available in multiple formats. **Lesson Number 121**: The recommendation states: "The FSW documentation should be made available in multiple formats."
* Maintain budgets on-line. **Lesson Number 134**: The recommendation states: "Maintain budgets on-line."
* Establish processes early in development. **Lesson Number 331**: The recommendation states: "Establish development and testing methodology and process early in the lifecycle."

# 7. Software Assurance

**SWE-036 - Software Process Determination**

3.1.6 The project manager shall establish and maintain the software processes, software documentation plans, list of developed electronic products, deliverables, and list of tasks for the software development that are required for the project’s software developers, as well as the action required (e.g., approval, review) of the Government upon receipt of each of the deliverables.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm the following are approved, implemented, and updated per requirements:  
     a. Software processes, including software assurance,   
         software safety, and IV&V processes,  
     b. Software documentation plans,  
     c. List of developed electronic products, deliverables, and  
     d. List of tasks required or needed for the project’s   
         software development.

2. Confirm that any required government actions are established and performed upon receipt of deliverables (e.g., approvals, reviews).

## 7.2 Software Assurance Products

This requirement focuses on establishing and maintaining software processes, documentation plans, deliverables, tasks, and required Government actions for software development. Software Assurance (SA) personnel contribute to this requirement by creating, tailoring, and delivering specific products that provide independent oversight, verify compliance, and document the assurance activities carried out to support the project.

Below is a comprehensive list of Software Assurance products associated with this requirement, categorized by key focus areas.

### 7.2.1 Software Assurance Oversight Products

#### 7.2.1.1 Software Process Assessment Report

* **Description**: Evaluates the adequacy, completeness, and compliance of software development processes against NASA standards and models such as **CMMI V2.0**.
* **Contents**:
  + Review results for each documented process (e.g., requirements, design, implementation, testing, maintenance).
  + Non-conformance findings and recommendations for process improvement.
  + Evidence of process alignment with the project's Software Development Plan (SDP).
* **Purpose**: Ensures that the development processes are robust, documented, and aligned with best practices.

#### 7.2.1.2 Software Process Audit Report

* **Description**: Documents the results of SA-led audits of the software development process to confirm adherence to the documented workflows.
* **Contents**:
  + Audit findings (e.g., gaps, risks, or non-compliance issues).
  + Corrective actions taken by the development organization.
  + Process improvement tracking logs.
* **Purpose**: Provides independent verification of process implementation and compliance.

### 7.2.2 Software Documentation Assurance Products

#### 7.2.2.1 Documentation Review Records

* **Description**: Records findings, comments, and recommendations from SA reviews of software documentation plans and deliverables.
* **Contents**:
  + Compliance status with Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance), NASA standards, or contractual requirements (e.g., CDRD).
  + Gaps in documentation plans and recommendations for improvement.
  + Approval status and stakeholder feedback logs.
* **Purpose**: Ensures that all required documentation is planned, executed, and reviewed for quality and completeness.

#### 7.2.2.2. Documentation Traceability Matrix

* **Description**: A matrix relating project-level requirements to the corresponding software documentation plans, deliverables, and review milestones.
* **Contents**:
  + Mapping of requirements to documentation deliverables.
  + Review and approval records for each document.
  + Associated risks or corrective actions linked to documentation gaps.
* **Purpose**: Tracks and ensures the traceability of required documentation to project goals and compliance.

#### 7.2.2.3 Documentation Version Control Log

* **Description**: Tracks updates and revisions to software documentation plans and their review/approval status.
* **Contents**:
  + Version history of each major project document.
  + Rationale for changes and associated review/approval records.
* **Purpose**: Maintains control and accountability over updates to critical project documentation.

### 7.2.3 Deliverables and Product Assurance Products

#### 7.2.3.1 Deliverables Assessment Report

* **Description**: Analyzes whether all project-required deliverables (e.g., software, models, test data) are properly developed, delivered, and validated.
* **Contents**:
  + Checklist of required deliverables versus actual delivered artifacts.
  + Compliance status of each deliverable with project requirements or contract criteria.
  + Evidence of validation (e.g., test reports, simulation results, quality reviews).
* **Purpose**: Confirms that all required deliverables meet quality and project objectives.

#### 7.2.3.2 Product Traceability Assessment

* **Description**: A comprehensive report showing bidirectional traceability between the deliverables, requirements, and associated software development tasks.
* **Contents**:
  + Traceability matrix linking deliverables to project-level requirements.
  + Mapping of deliverables to their development and review life cycles.
* **Purpose**: Verifies that all deliverables are appropriately traceable and validated.

#### 7.2.3.3 Validation and Verification (V&V) Record

* **Description**: Documents evidence of independent validation and verification of software deliverables, including test results and compliance status.
* **Contents**:
  + Test execution logs, test cases matched to deliverables, and regression test reports.
  + Static and dynamic analysis results.
  + Review results for prototypes, tools, and intermediate test builds.
* **Purpose**: Confirms that deliverables meet functional, performance, and safety requirements.

### 7.2.4 Development Task Oversight Products

#### 7.2.4.1. Software Development Task Review Report

* **Description**: Summarizes SA reviews of the development task list to ensure completeness, traceability, and alignment with project objectives.
* **Contents**:
  + Detailed analysis of software tasks linked to milestone reviews (e.g., PDR, CDR, TRR).
  + Comments on schedule consistency and task dependencies.
  + Compliance findings with Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews).
* **Purpose**: Provides confidence that the development team’s task planning aligns with lifecycle and milestone objectives.

#### 7.2.4.2 Risk Management Report

* **Description**: Captures and tracks risks associated with the execution of software development tasks.
* **Contents**:
  + Identified risks, their potential impact, and corresponding mitigation plans.
  + Risk status updates and closure records.
* **Purpose**: Ensures that risks to the timely and successful execution of development tasks are addressed proactively.

#### 7.2.4.3 Development Task Compliance Checklist

* **Description**: A checklist to assess the completion, quality, and compliance of development tasks relative to project and lifecycle requirements.
* **Contents**:
  + Status of completed tasks (e.g., on-schedule, delayed, blocked).
  + Task performance metrics (e.g., adherence to schedules and cost estimates).
  + Open issues or corrective actions associated with task completion.
* **Purpose**: Monitors and reports on task progress and compliance.

### 7.2.5 Government Actions Assurance Products

#### 7.2.5.1 Government Review Readiness Assessment

* **Description**: Documents assessments of the readiness of deliverables for Government reviews or approvals.
* **Contents**:
  + Checklist of deliverables required for each Government review milestone.
  + Review history and corrections made in response to prior feedback.
* **Purpose**: Confirms that all necessary deliverables and supporting artifacts are prepared for Government assessments.

#### 7.2.5.2 Government Oversight Compliance Report

* **Description**: Tracks and evaluates alignment with required Government actions such as formal reviews and approvals.
* **Contents**:
  + Records of formal sign-offs from Government representatives.
  + Review findings and resolutions for flagged deliverables.
* **Purpose**: Ensures deliverables satisfy Government review and approval requirements.

### 7.2.6 SA-Specific Framework and Management Products

#### 7.2.6.1 Software Assurance Plan

* **Description**: Tailored plan capturing the processes, responsibilities, tools, and outputs of SA activities on the project.
* **Contents**:
  + Scope of assurance tasks, alignment with project milestones, and risk management plans.
  + Defined roles, responsibilities, and relationships with project stakeholders.
* **Purpose**: Provides a baseline for all Software Assurance activities and ensures alignment with project goals.

#### 7.2.6.2 SA Metrics Dashboard

* **Description**: Tracks and reports SA-related metrics, such as task progress, deliverable compliance, defect trends, and risk closure rates.
* **Contents**:
  + Summary of SA metrics (e.g., compliance rates, non-conformance rates, documentation review completeness).
  + Charts and reports visualizing metrics over time.
* **Purpose**: Provides visibility into the progress and impact of SA activities on the project.

#### 7.2.6.3 Risk and Defect Tracking Logs

* **Description**: Consolidated logs capturing all risks and defects identified by SA activities, along with their resolution status.
* **Contents**:
  + Risk/defect descriptions, severity levels, and mitigation plans.
  + Open/closed status and links to related work products (e.g., deliverables, processes).
* **Purpose**: Tracks risks and defects to ensure they are resolved before key milestones or final deliveries.

### 7.2.7 Summary of Software Assurance Products

| **Category** | **SA Product Examples** |
| --- | --- |
| **Software Processes** | Assessment Reports, Audit Reports. |
| **Documentation Assurance** | Review Records, Traceability Matrix, Version Control Logs. |
| **Deliverables** | Deliverables Assessment Report, V&V Records, Traceability Reports. |
| **Development Task Oversight** | Development Task Review Reports, Risk Management Reports, Task Compliance Checklists. |
| **Government Actions** | Review Readiness Assessments, Oversight Compliance Reports. |
| **SA Framework** | Software Assurance Plan, Metrics Dashboards, Risk/Defect Logs. |

---

These products ensure that Software Assurance effectively supports compliance with this requirement, monitors project deliverables, enforces quality processes, and addresses risks across the software lifecycle.

## 7.3 Metrics

This requirement mandates that projects establish and maintain software processes, documentation plans, electronic products/deliverables, development tasks, and Government action tracking for approvals and reviews. For Software Assurance (SA), metrics are critical to measure the effectiveness of these activities and to detect gaps or risks that might hinder compliance. These metrics enable monitoring, reporting, and continuous improvement in all aspects of the software development process.

Below is a list of **Software Assurance Metrics** organized by key areas related to this requirement.

### 7.3.1 Metrics for Software Processes

#### 7.3.1.1 Process Documentation Compliance Rate

* **Definition**: Percentage of documented software processes that align with relevant standards, such as NASA standards and CMMI V2.0 practices.
* **Formula**: [ \text{Process Compliance Rate} = \left( \frac{\text{Number of Compliant Processes}}{\text{Total Processes Reviewed}} \right) \times 100 ]
* **Purpose**: Measures how many of the development organization's processes meet established practices and compliance models.
* **Target Value**: ≥95%.

#### 7.3.1.2 Process Audit Findings per Review

* **Definition**: Number of non-conformances or gaps identified during audits of development processes.
* **Formula**: [ \text{Findings per Review} = \frac{\text{Total Audit Findings}}{\text{Number of Processes Audited}} ]
* **Purpose**: Provides insight into the process maturity and health of development workflows.
* **Target Value**: ≤1 finding per review.

#### 7.3.1.3 Process Update Completion Rate

* **Definition**: Percentage of requested updates to software processes successfully implemented.
* **Formula**: [ \text{Update Completion Rate} = \left( \frac{\text{Processes Updated on Time}}{\text{Total Updates Requested}} \right) \times 100 ]
* **Purpose**: Tracks responsiveness to identified areas for improvement in software processes.
* **Target Value**: ≥90%.

### 7.3.2 Metrics for Software Documentation Plans

#### 7.3.2.1 Documentation Coverage

* **Definition**: Percentage of required documentation plans that have been created, reviewed, and approved.
* **Formula**: [ \text{Documentation Coverage} = \left( \frac{\text{Approved Documentation Plans}}{\text{Total Required Plans}} \right) \times 100 ]
* **Purpose**: Ensures all required documentation plans for the project are completed and compliant with guidelines.
* **Target Value**: 100%.

#### 7.3.2.2 Document Review Timeliness

* **Definition**: Percentage of documentation reviews completed on schedule.
* **Formula**: [ \text{Timeliness Rate} = \left( \frac{\text{On-Time Reviews}}{\text{Total Planned Document Reviews}} \right) \times 100 ]
* **Purpose**: Tracks adherence to review schedules for documentation plans and deliverables.
* **Target Value**: ≥95%.

#### 7.3.2.3 Documentation Approval Rate

* **Definition**: Percentage of project documentation plans formally approved after SA and stakeholder review.
* **Formula**: [ \text{Approval Rate} = \left( \frac{\text{Approved Plans}}{\text{Total Reviewed Plans}} \right) \times 100 ]
* **Purpose**: Tracks the successful approval of documentation plans.
* **Target Value**: ≥95%.

### 7.3.3 Metrics for Deliverables and Electronic Products

#### 7.3.3.1 Deliverable Availability Rate

* **Definition**: Percentage of required products and deliverables produced and available to stakeholders.
* **Formula**: [ \text{Availability Rate} = \left( \frac{\text{Delivered Products}}{\text{Total Required Products}} \right) \times 100 ]
* **Purpose**: Monitors the delivery readiness of software artifacts.
* **Target Value**: 100%.

#### 7.3.3.2 Deliverable Review and Approval Rate

* **Definition**: Percentage of deliverables reviewed and approved on time.
* **Formula**: [ \text{Approval Rate} = \left( \frac{\text{Approved Deliverables}}{\text{Total Deliverables Reviewed}} \right) \times 100 ]
* **Purpose**: Ensures the timely review and acceptance of deliverables across the software lifecycle.
* **Target Value**: ≥95%.

#### 7.3.3.3 Non-Conformance Rate for Deliverables

* **Definition**: Percentage of deliverables flagged for non-conformance after review.
* **Formula**: [ \text{Non-Conformance Rate} = \left( \frac{\text{Non-Conforming Deliverables}}{\text{Total Deliverables Reviewed}} \right) \times 100 ]
* **Purpose**: Tracks the quality of deliverables being provided to stakeholders.
* **Target Value**: ≤5%.

#### 7.3.3.4 Sustainability of Deliverables

* **Definition**: Percentage of key deliverables maintained for reuse or repurposing in future analyses.
* **Formula**: [ \text{Sustainability Rate} = \left( \frac{\text{Deliverables Maintained}}{\text{Total Key Deliverables}} \right) \times 100 ]
* **Purpose**: Monitors retention/accessibility of critical project deliverables.
* **Target Value**: ≥95%.

### 7.3.4. Metrics for Software Development Tasks

#### 7.3.4.1 Task Completion Rate

* **Definition**: Percentage of planned software development tasks completed on time.
* **Formula**: [ \text{Task Completion Rate} = \left( \frac{\text{Completed Tasks}}{\text{Total Planned Tasks}} \right) \times 100 ]
* **Purpose**: Monitors the on-track completion of development activities required to meet project goals.
* **Target Value**: ≥95%.

#### 7.3.4.2 Task Compliance Rate

* **Definition**: Percentage of completed tasks that meet project and SA criteria for quality and completeness.
* **Formula**: [ \text{Compliance Rate} = \left( \frac{\text{Tasks Meeting Criteria}}{\text{Total Completed Tasks}} \right) \times 100 ]
* **Purpose**: Ensures completed tasks meet quality and compliance standards.
* **Target Value**: ≥95%.

#### 7.3.4.3 Development Milestone Readiness Rate

* **Definition**: Percentage of development milestones met with all planned software tasks completed.
* **Formula**: [ \text{Readiness Rate} = \left( \frac{\text{Milestones on Schedule}}{\text{Total Planned Milestones}} \right) \times 100 ]
* **Purpose**: Tracks how well software tasks align with key milestone deadlines.
* **Target Value**: ≥90%.

### 7.3.5. Metrics for Government Actions on Deliverables

#### 7.3.5.1 Government Action Timeliness

* **Definition**: Percentage of required Government actions (reviews, approvals) completed on schedule.
* **Formula**: [ \text{Timeliness Rate} = \left( \frac{\text{On-Time Actions}}{\text{Total Required Actions}} \right) \times 100 ]
* **Purpose**: Tracks how effectively Government actions align with the project schedule.
* **Target Value**: ≥95%.

#### 7.3.5.2 Government Rejection Rate

* **Definition**: Percentage of deliverables rejected or requiring rework after Government review.
* **Formula**: [ \text{Rejection Rate} = \left( \frac{\text{Rejected Deliverables}}{\text{Total Deliverables Reviewed by Government}} \right) \times 100 ]
* **Purpose**: Identifies risks from poorly prepared deliverables submitted to the Government.
* **Target Value**: ≤5%.

### 7.3.6. Metrics for Software Assurance Processes

#### 7.3.6.1 SA Product Traceability Rate

* **Definition**: Percentage of SA products that are traceable to the SA plan and project requirements.
* **Formula**: [ \text{Traceability Rate} = \left( \frac{\text{Traceable SA Products}}{\text{Total SA Products}} \right) \times 100 ]
* **Purpose**: Confirms alignment of SA outputs with documented requirements and plans.
* **Target Value**: 100%.

#### 7.3.6.2 SA Risks Addressed Rate

* **Definition**: Percentage of SA-identified risks addressed and mitigated on time.
* **Formula**: [ \text{Risks Addressed Rate} = \left( \frac{\text{Addressed Risks}}{\text{Total Identified Risks}} \right) \times 100 ]
* **Purpose**: Tracks effectiveness in managing SA risks.
* **Target Value**: ≥95%.

#### 7.3.6.3 SA Review Coverage

* **Definition**: Percentage of project artifacts reviewed by SA to ensure quality and compliance.
* **Formula**: [ \text{Review Coverage} = \left( \frac{\text{Artifacts Reviewed by SA}}{\text{Total Project Artifacts}} \right) \times 100 ]
* **Purpose**: Tracks SA involvement in ensuring project compliance.
* **Target Value**: ≥95%.

### 7.3.7 Summary Table of Metrics

| **Category** | **Metric Examples** | **Purpose** |
| --- | --- | --- |
| Software Processes | Process Compliance Rate, Process Update Rate | Evaluate process documentation and improvement. |
| Documentation Plans | Coverage Rate, Approval Rate, Timeliness Rate | Ensure documentation meets requirements. |
| Deliverables | Availability Rate, Review Timeliness, Compliance | Assess deliverable readiness and quality. |
| Development Tasks | Task Completion Rate, Milestone Readiness | Monitor software development progress. |
| Government Actions | Timeliness Rate, Rejection Rate | Track review and approval of deliverables. |
| Software Assurance | Traceability Rate, Risk Addressed Rate | Measure SA contribution and risk management. |

By monitoring these metrics, Software Assurance ensures that this requirement is satisfied, demonstrating compliance, quality, and alignment with project goals. Regular reviews of metrics allow for early risk detection and support continuous improvement in software processes and deliverables.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

**SWE-036 - Software Process Determination**

3.1.6 The project manager shall establish and maintain the software processes, software documentation plans, list of developed electronic products, deliverables, and list of tasks for the software development that are required for the project’s software developers, as well as the action required (e.g., approval, review) of the Government upon receipt of each of the deliverables.

The goal of Software Assurance (SA) in relation to this requirement is to confirm that software processes, plans, deliverables, tasks, and required Government actions are correctly defined, properly documented, implemented, and maintained throughout the software lifecycle. SA personnel are responsible for independently reviewing, verifying, and validating the completeness and correctness of these elements and ensuring alignment with applicable NASA standards, contractual obligations, and project goals.

### 7.4.1 Software Processes

* **Objective**: Confirm that robust, documented software development processes are established and updated as necessary for each phase of the software development lifecycle.
* **SA Actions**:
  1. **Review Development Processes**:
     + Verify the software development organization’s processes are documented in accordance with established quality models such as **CMMI V2.0** (Capability Maturity Model Integration).
     + Assess compliance with NASA standards, project-specific requirements, and software engineering best practices.
  2. **Audit Process Workflows**:
     + Conduct process audits to ensure the organization’s actual practices align with documented processes.
     + Include adherence to requirements for iterative/incremental practices if Agile workflows are used.
  3. **Confirm Implementation and Maintenance**:
     + Ensure processes are implemented consistently across all software phases (requirements, design, implementation, testing, delivery/maintenance).
     + Validate updates to processes in response to changes in project scope or risks.
  4. **Objective Evidence**:
     + Process documentation, audit reports, process compliance tracking logs.

### 7.4.2 Software Documentation Plans

* **Objective**: Confirm that software documentation plans define content requirements, delivery timelines, review processes, and maintenance standards.
* **SA Actions**:
  1. **Content Review**:
     + Evaluate documentation plans against **NASA documentation guidelines**, such as the ones defined in Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) and the **Contract Data Requirements Documents (CDRD)**.
     + Ensure plans address all lifecycle phases (e.g., requirements documentation, test plans/reports, design documentation).
  2. **Alignment with Deliverables**:
     + Confirm alignment between planned documentation and required deliverables specified in contractual agreements and project requirements.
  3. **Timely Updates**:
     + Verify periodic updates to documentation plans to reflect evolving project milestones, risks, or stakeholder needs.
  4. **Objective Evidence**:
     + Review notes, annotated documentation plans, comparison reports documenting gaps/corrections.

### 7.4.3 List of Developed Electronic Products and Deliverables

* **Objective**: Confirm that all required deliverables, developed electronic products, and supporting artifacts are identified, delivered, and maintained appropriately.
* **SA Actions**:
  1. **Evaluate the Deliverables List**:
     + Compare the project deliverables list, as outlined in contractual documentation or project requirements, against the actual outputs produced by the development team.
     + Confirm these deliverables meet project goals and are traceable to system-level requirements.
  2. **Validate Product Accessibility**:
     + Ensure deliverables are accessible to relevant stakeholders (e.g., developers, software assurance teams, customers).
     + Confirm supporting tools, reports, and data necessary for analysis or re-testing are preserved.
  3. **Use of Agency Resources**:
     + Engage the **Agency Software Manager** to verify completeness and accuracy of the deliverables list.
  4. **Example Deliverables**:
     + **Executable and source code**.
     + **Simulations and models**.
     + **Trade study data** for analysis of alternatives.
     + **Prototypes**, including architecture/design models.
     + **Software test scripts** and results.
     + **Metric data** and compliance analyses.
     + **Software build tools**, databases, ground systems, and test environments.
  5. **Objective Evidence**:
     + Approved deliverables list, traceability matrix, validation results ensuring completeness.

### 7.4.4 List of Tasks for Software Development

* **Objective**: Confirm that all software development tasks necessary to meet project requirements are documented, traceable, and tracked.
* **SA Actions**:
  1. **Task List Evaluation**:
     + Review the planned software development tasks and verify traceability to project goals.
     + Ensure tasks cover all phases of the lifecycle (requirements, design, implementation, testing, maintenance).
  2. **Alignment with Milestones**:
     + Confirm that each task is mapped to **milestone reviews** (e.g., PDR, CDR, TRR, SAR) and that completion criteria are well-defined.
     + Assess progress against milestone deadlines using Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews).
  3. **Ensure Accuracy**:
     + Verify that task descriptions, dependencies, and estimates are realistic and achievable within project constraints.
  4. **Objective Evidence**:
     + Development schedule, task tracking dashboard/reports, milestone readiness status reports.

### 7.4.5 Government Actions for Deliverables

* **Objective**: Confirm that required Government actions (review, approval, etc.) are established, tracked, and implemented upon receipt of deliverables.
* **SA Actions**:
  1. **Government Approval Processes**:
     + Ensure the project defines processes for Government review or approval at each delivery milestone.
     + Verify that deliverables requiring specific review actions are flagged and scheduled appropriately.
  2. **Milestone Assessment**:
     + Review Government action requirements for milestone-based reviews, using [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews). for guidance.
     + Confirm any feedback loops for required changes or updates to deliverables based on Government assessment.
  3. **Maintenance of Approval Records**:
     + Ensure formal documentation of approvals is stored and accessible via approved configuration management systems.
  4. **Objective Evidence**:
     + Approved review/approval process documentation, milestone delivery records, meeting notes confirming Government actions.

### 7.4.6 Software Assurance Processes, Plans, Products, Risks, and Tasks

* **Objective**: Develop and tailor Software Assurance processes, plans, products, and tracking tools to support compliance with Requirement 3.1.6.
* **SA Actions**:
  1. **Develop SA Framework**:
     + Create or tailor standard software assurance and software safety processes to align with the project's scope.
     + Plan activities that ensure compliance with requirement-specific actions, such as deliverable tracking and risk mitigation.
  2. **Track SA Outputs**:
     + Establish processes for tracking SA outputs, risks, and completed tasks.
     + Ensure traceability of all SA work products to the Software Assurance Plan and project-level requirements.
  3. **Risk and Compliance Assessments**:
     + Conduct regular risk reviews to ensure software processes and deliverables meet NASA standards and mitigate identified risks.
  4. **Objective Evidence**:
     + SA framework documentation, tracking reports, compliance reviews, risk mitigation plans.

### 7.4.7 Additional Resources

1. **CMMI V2.0 Practices**:

   * Confirm that the development organization’s software processes meet industry-recognized maturity models.
   * Use the **[https://cmmiinstitute.com](https://cmmiinstitute.com/)** repository for access to CMMI V2.0 model practices.
2. **NASA Documentation Guidance**:

   * Refer to Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) for document content requirements.
   * Ensure compliance with any **Contract Data Requirements Documents (CDRD)** specified in contractual agreements.
3. **Milestone Review Processes**:

   * Review Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) for completeness criteria at milestone reviews.

### **Summary of Updated SA Actions**

| **Area** | **SA Actions** | **Objective Evidence** |
| --- | --- | --- |
| **Software Processes** | Review documented processes, audit workflows, confirm updates. | Process documents, compliance tracking reports. |
| **Documentation Plans** | Review content against NASA guidelines, confirm delivery timeline. | Annotated document plans, gap analysis reports. |
| **Deliverables List** | Verify deliverables against requirements, ensure accessibility, validate completeness. | Approved deliverables list, traceability matrix. |
| **Development Task List** | Assess tasks for traceability, milestone alignment, and accuracy. | Task list tracking report, development schedule. |
| **Government Actions** | Confirm review/approval processes for deliverables, track formal actions. | Government actions log, milestone approval records. |
| **SA Processes/Plans** | Create Software Assurance frameworks, track SA products and risks. | SA framework docs, risk review reports. |

This updated guidance ensures Software Assurance personnel contribute effectively to the establishment, review, and maintenance of processes, deliverables, documentation, and Government action plans in compliance with this requirement. All activities aim to ensure the software project meets defined expectations, requirements, and quality standards.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) * [SWE-004 - OCE Benchmarking](/spaces/SWEHBVD/pages/102695394/SWE-004+-+OCE+Benchmarking) * [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-129 - OCE NPR Appraisals](/spaces/SWEHBVD/pages/102695491/SWE-129+-+OCE+NPR+Appraisals) - * [SWE-209 - Benchmarking Software Assurance and Software Safety Capabilities](/spaces/SWEHBVD/pages/102695329/SWE-209+-+Benchmarking+Software+Assurance+and+Software+Safety+Capabilities) * [SWE-221 - OSMA NPR Appraisals](/spaces/SWEHBVD/pages/105709899/SWE-221+-+OSMA+NPR+Appraisals)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

# 8. Objective Evidence

Objective evidence is a collection of tangible artifacts, records, and assessments to verify compliance with this requirement. Software Assurance (SA) personnel are responsible for ensuring that all required processes, plans, deliverables, development tasks, and Government actions are properly established, executed, reviewed, and documented. Below is a detailed guide to the types of objective evidence SA personnel should collect for this requirement.

By collecting these  artifacts as objective evidence, Software Assurance personnel ensure that all aspects of this requirement are properly defined, implemented, reviewed, and maintained. This evidence supports project compliance, tracks progress, and enables periodic assessments to reduce risks and improve software quality.

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

## 8.1 Objective Evidence for Software Processes

#### Documented Software Processes

* **Artifacts**:
  + Software Process Description documents for each phase (e.g., requirements, design, implementation, testing, maintenance).
  + Tailoring reports if standard processes are adapted to meet project-specific needs.
  + Process flowcharts, workflows, or related diagrams for clarity.
  + Evidence of process reviews and approvals (e.g., meeting minutes, review logs).
* **Purpose**: Confirm that the development organizations have documented processes for the software lifecycle and that these processes comply with NASA standards, project objectives, and CMMI V2.0 practices.

#### Process Compliance Audit Reports

* **Artifacts**:
  + Software process audit reports showing alignment with NASA guidelines, industry standards, and CMMI practices.
  + Non-conformance logs identifying gaps, risks, and corrective actions implemented.
  + Software process improvement logs documenting updates made based on audit recommendations.
* **Purpose**: Provide evidence that processes have been assessed and are implemented correctly, updated when necessary, and are aligned with quality management goals.

## 8.2 Objective Evidence for Software Documentation Plans

#### Approved Documentation Plans

* **Artifacts**:
  + Software Documentation Plan, detailing content, timelines, milestones, and maintenance policies.
  + Project-specific documentation guidelines (e.g., Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)).
  + Contract Data Requirements Documents (CDRD) with mapped deliverables.
* **Purpose**: Verify that documentation plans are established, reviewed, and approved, and meet contractual obligations and relevant NASA standards.

#### Review Records

* **Artifacts**:
  + SA review logs, annotations, and checklists for reviewing documentation plans against guidelines.
  + Evidence of stakeholder reviews of documentation plans (e.g., signed meeting minutes, stakeholder feedback forms).
* **Purpose**: Confirm SA and stakeholders have completed all required reviews and validations of the documentation plans.

#### Version Control Logs

* **Artifacts**:
  + Configuration management records showing updates to documentation plans over time.
* **Purpose**: Ensure all changes to documentation plans are tracked and stored appropriately.

## 8.3 Objective Evidence for List of Developed Electronic Products and Deliverables

#### Deliverables List

* **Artifacts**:
  + A consolidated list of required deliverables and electronic products, captured in project requirements or contract documentation.
  + Detailed traceability matrix linking deliverables to requirements and project goals.
  + Stakeholder-approved deliverables list (e.g., confirmation from the Agency Software Manager or customer approval reports).
* **Purpose**: Confirm that all required artifacts are identified, documented, and approved.

#### Delivered Artifacts

* **Artifacts**:
  + Released source code and executable files.
  + Models and simulations (including validation data sets and assumptions).
  + Trade study data used for analysis of alternatives.
  + Prototype architectures, software ground systems, and build tools.
  + Software test reports, including scripts and results.
* **Purpose**: Provide evidence that the required deliverables and electronic products are available, accessible, and complete.

#### Validation Records

* **Artifacts**:
  + Validation logs or reports showing that deliverables were tested, reviewed, and approved per acceptance criteria.
  + Simulations, test results, and peer review data validating each deliverable.
* **Purpose**: Ensure deliverables have been reviewed and validated against project requirements.

#### Product Accessibility Records

* **Artifacts**:
  + Logs or reports confirming deliverables are retrievable in project repositories.
  + Access control permissions documenting who has access to deliverables.
* **Purpose**: Verify stakeholders have appropriate access to deliverables for reference or reuse.

## 8.4 Objective Evidence for List of Tasks for Software Development

#### Software Development Task List

* **Artifacts**:
  + Comprehensive task list detailing all software development activities, milestones, dependencies, and estimated durations.
  + Software schedule showing task progress and milestone deadlines (referencing Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) ).
* **Purpose**: Ensure all development tasks are documented, traceable to milestone reviews, and align with project requirements.

#### Task and Milestone Review Records

* **Artifacts**:
  + Completion reports for development tasks tied to milestone reviews (e.g., PDR, CDR, TRR, SAR).
  + Task performance logs (e.g., percentage completion rates, delays, corrective actions).
* **Purpose**: Provide evidence that development tasks are tracked, monitored, and completed on time and to specification.

#### Risk Mitigation Records

* **Artifacts**:
  + Logs documenting identified risks to task completion and associated mitigation actions.
* **Purpose**: Demonstrate proactive management of risks to development tasks.

## 8.5 Objective Evidence for Government Actions on Deliverables

#### Government Approval Records

* **Artifacts**:
  + Formal sign-off documents approving deliverables post-review (e.g., Software Acceptance Reports).
  + Meeting minutes capturing Government feedback and approval decisions.
* **Purpose**: Confirm that required Government actions (approvals, reviews) for deliverables have been completed satisfactorily.

#### Review Logs

* **Artifacts**:
  + Documentation of review schedules, attendees, and outcomes for Government-required reviews.
  + Records tracking discrepancies raised during reviews and their resolution status.
* **Purpose**: Provide evidence of consistent oversight by Government reviewers for project deliverables.

#### Corrective Action Records

* **Artifacts**:
  + Logs updating deliverables based on Government reviews (e.g., deficiencies corrected before final approval).
* **Purpose**: Demonstrate responsiveness to Government review feedback.

## 8.6 Objective Evidence for SA Processes, Plans, Products, Risks, and Tasks

#### Software Assurance Plan

* **Artifacts**:
  + Approved Software Assurance Plan with detailed processes, tasks, risks, and expected deliverables.
* **Purpose**: Confirm that SA processes and tasks are planned and tailored to enable compliance with this requirement.

#### SA Risk Reports

* **Artifacts**:
  + SA risk assessment logs, showing identified risks and corresponding mitigation status.
  + Risk tracking documentation reporting risk closure rates.
* **Purpose**: Provide evidence of effective risk identification and mitigation.

#### SA Task Completion Status

* **Artifacts**:
  + Reports or dashboards tracking SA task progress and milestone readiness.
  + Logs documenting feedback and improvements from completed tasks.
* **Purpose**: Ensure all required SA tasks are completed to enable compliance with project software requirements.

## 8.7 Summary of Objective Evidence Categories

| **Category** | **Objective Evidence Examples** |
| --- | --- |
| **Software Processes** | Process documentation, audit reports, process improvement logs, flowcharts. |
| **Documentation Plans** | Approved documentation plans, review records, version control logs. |
| **Deliverables and Products** | Deliverables list, traceability matrix, validation records, product accessibility logs. |
| **Development Tasks** | Task lists, milestone reviews, risk mitigation records. |
| **Government Actions** | Approval records, review logs, corrective action logs. |
| **SA Processes & Products** | Approved SA plan, SA risk reports, task tracking reports. |
