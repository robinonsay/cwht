# 5.08 - SDP-SMP - Software Development - Management Plan

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695668. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan

5.08 - SDP-SMP - Software Development - Management Plan

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695668)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695668&showCommentArea=true&showComments=true#addcomment)

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

Minimum recommended content for the Software Development - Management Plan. 

1. 1. Project organizational structure showing authority and responsibility of each organizational unit, including external organizations (e.g., Safety and Mission Assurance, Independent Verification and Validation (IV&V), Technical Authority, NASA Engineering and Safety Center, NASA Safety Center).
   2. The safety-critical determination and software classification of each of the systems and subsystems containing software.
   3. Tailored requirements mapping/compliance matrix for approval by the designated Engineering Technical Authority, if the project has any waivers or deviations to this NPR.
   4. Engineering environment (for development, operation, or maintenance, as applicable), including test environment, library, equipment, facilities, standards, procedures, and tools.
   5. Work breakdown structure of the life cycle processes and activities, including the software products, software services, non-deliverable items to be performed, budgets, staffing, acquisition approach, physical resources, software size, and schedules associated with the tasks.
   6. Management of the quality characteristics of the software products or services.
   7. Management of safety, security, privacy, and other critical requirements of the software products or services.
   8. Subcontractor management, including subcontractor selection and involvement between the subcontractor and the acquirer, if any.
   9. Verification:  
      1. Identification of selected software verification methods and criteria across the life cycle (e.g., software peer review/inspections procedures, re-review/inspection criteria, testing procedures).
      2. Identification of selected work products to be verified.
      3. Description of software verification environments that are to be established for the project (e.g., software testing environment, system testing environment, regression testing environment).
      4. Identification of where actual software verification records and analysis of the results will be documented (e.g., test records, software peer review/inspection records) and where software verification corrective action will be documented.
   10. Validation  
       1. Identification of selected software validation methods and criteria across the life cycle (e.g., prototyping, user groups, simulation, analysis, acceptance testing, operational demonstrations).
       2. Identification of selected work products to be validated.
       3. Description of software validation environments that are to be established for the project (e.g., simulators for operational environment).
       4. Identification of where actual software validation records and analysis of the results will be documented (e.g., user group records, prototyping records, and acceptance testing records) and where software validation corrective action will be documented.
   11. Project involvement.
   12. User involvement.
   13. Risk management.
   14. Security policy.
   15. Approval required by such means as regulations, required certifications, proprietary, usage, ownership, warranty, and licensing rights.
   16. Process for scheduling, tracking, and reporting.
   17. Training of personnel, including project unique software training needs.
   18. Software life cycle model, including description of software integration and hardware/software integration processes, software delivery, and maintenance.
   19. Configuration management.
   20. Software document deliverables.
   21. Software peer review/inspection process of software work products.
   22. Process for early identification of testing requirements that drive software design decisions (e.g., special system level timing requirements/checkpoint restart).
   23. Software metrics.
   24. Content of software documentation to be developed on the project.
   25. Management, development, and testing approach for handling any commercial-off-the-shelf (COTS), government-off-the-shelf (GOTS), modified-off-the-shelf (MOTS), reused, or open source software component(s) that are included within a NASA system or subsystem.

# 2. Rationale

Software development requires thought and planning before implementation. It is important to document, review, and approve the activities, tools, responsibilities, and other tasks needed to develop software before beginning the work. Planning helps the team consider and put in place those elements needed to efficiently produce the software in the allotted time frame and within the allotted budget.  The plan also provides a basis for monitoring the project's adherence to these processes.

Planning allows others within the project and external to the project to evaluate, integrate, and critique the proposed approach, and the resulting plan helps new members of the software team get up to speed when joining the project. Planning also allows a current project to consider lessons learned from previous projects to avoid previously experienced difficulties.

# 3. Guidance

The Software Development or Management Plan provides insight into, and a tool for monitoring, the processes to be followed for software development, the methods to be used, the approach to be followed for each activity, and project schedules, organization, and resources. This plan details the system software, project documentation, project schedules, resources requirements and constraints, and general and detailed software development activities. See [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans), [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule),

Begin writing the plan as soon as any information about the project definition and scope becomes available. Complete the plan by the end of the requirements analysis phase, except for information available only at later phases, e.g., the build plan is typically inserted during the design phase. See also [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), If items in the Software Development or Management Plan (SDP or SMP) are missing for any reason, the manager indicates who will supply the information and when it will be supplied. [031](#_tabs-<p></p>) It is important to keep the plan up to date throughout the project life cycle. Refer to Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) for expected plan maturity and updates at various life cycle milestones.

The following roles may be involved in creating the SDP/SMP:

* Software Lead Engineer.
* Test Team Lead. [453](#_tabs-<p></p>)
* Software Engineers.
* Software Assurance Engineer (to coordinate assurance activities and schedule).
* Software Acquisition personnel.
* Users/customers.
* Software Configuration Management Engineer.
* System Engineer.

If other plans, such as the Software Configuration Management Plan, are incorporated into the SDP/SMP, additional roles may be involved in authoring the SDP/SMP.

The content of the SDP/SMP is the recommended minimum content; additional content may be included as appropriate for the project. This content may be entirely captured in the SDP/SMP, or it may be captured in the SDP/SMP and some number of other plans. When other plans capture any of the recommended SDP/SMP content, reference those plans in the SDP/SMP.

When developing an SDP/SMP, consider the following guidance for each of the minimum recommended elements of the plan:

## 3.1 Project Organizational Structure

Describe in text, graphics, or both the authority and responsibility of each unit of the organization having a role in the development of the software. Include both internal and external organizations relevant to the software development effort:

* Software Engineering.
* Organizational support, such as configuration management, verification and validation (V&V), training, metrics, process development.
* Hardware development and manufacturing.
* System Engineering.
* Safety and Mission Assurance.
* Independent Verification and Validation (IV&V).
* Software/Engineering Technical Authority.
* Subcontractors.
* Users.
* NASA Engineering and Safety Center.
* NASA Safety Center.

## 3.2 Safety Critical Determination and Software Classification

Capture the results of software classification ([SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)) and safety critical determination ([SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)) of the project systems and subsystems containing software. This information may change as the project proceeds through its life cycle and the team is responsible for keeping this part of the SDP/SMP current with those changes.

Also see [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records), [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), and Topic [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality).

## 3.3 Tailored Requirements Mapping Matrix

The tailored Requirements Mapping Matrix shows how the project will comply with **NPR 7150.2** (see [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix)). If the project has any waivers or deviations to **NPR 7150.2**, include a table showing the **NPR 7150.2** requirements the project plans to meet, those waived by the project, and those from which the project plans to deviate. For waivers and deviations, follow the appropriate approval processes, and record in the table those waivers and deviations approved for the project. Until those approvals are received, the table represents the planned compliance for the project.

The matrix is reviewed and approved by the appropriate Engineering Technical Authority or Center-designated authority for review of tailoring.

See also [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements), [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations), [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records), Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)

## 3.4 Engineering Environment (for development, operation, or maintenance, as applicable)

Describe "the methods, tools, and techniques to be used to specify, design, build, test, integrate, document, deliver, modify, and maintain the software products". [057](#_tabs-<p></p>)  
Include information such as:

* Development methodologies.
* Programming languages.
* Technical standards.
* Development and test tools.
* Coding standards.
* Libraries.
* Operating systems.
* Networks.
* Equipment such as simulators or specialized testbeds.
* Facilities, including any physical security needs.
* Policies and procedures.

See also [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation), [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards), [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification), and [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase).

## 3.5 Work Breakdown Structure (WBS)

The WBS describes the life cycle processes and work activities and their relationships (order, dependencies, etc.) among those activities. Decompose the WBS to a level that allows "accurate estimation of resource requirements and schedule duration for each work activity." [057](#_tabs-<p></p>)  
Include in the WBS the software products and non-deliverable items to be created; the software services to be performed; budgets, staffing, acquisition approach, physical resources, software size, and schedules associated with the tasks. For additional guidance, see Topic [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software).

If appropriate or desired, a complete schedule and a staffing plan may be provided in their own sections of the SDP/SMP or in separate documents with references included in the SDP/SMP.

See also [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes), [SWE-006 - Center Software Inventory](/spaces/SWEHBVD/pages/102695396/SWE-006+-+Center+Software+Inventory), [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans), [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation), [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule), [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review), [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones), [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule), [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions), and [SWE-174 - Software Planning Parameters](/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters).

## 3.6 Management of Quality Characteristics

Describe how the quality characteristics (e.g., availability, reliability, usability, maintainability, portability, performance, correctness) of the software products and services will be managed for the software development life cycle. Include the processes for measuring, tracking, reporting, and determining if the software meets the required levels of these characteristics, as specified in the software requirements. If addressed in a separate document, reference that plan in the SDP/SMP. See also [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality).

See also [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository).

## 3.7 Management of Safety, Security, Privacy, and Other Critical Requirements

Describe how the safety, security, privacy, and other critical requirements of the software products and services will be managed for the software development life cycle, including information security, controlled data access, and other information management aspects of the software functionality. If addressed in a separate software assurance plan, reference that plan in the SDP/SMP. Possible items to include are:

* Assessment of the sensitive information that is to be managed and controlled by the software.
* Development, validation, verification, and management of security, privacy, and safety requirements.
* Identification of safety-critical requirements.
* Compliance with **NASA-STD-8739.8, Software Assurance and Software Safety Standard**.
* Compliance with **NPD 2810.1, NASA Information Security Policy** , as applicable.
* Compliance with **NPR 2810.1, Security of Information and Information Systems**, as applicable.

See the Security Policy section below for additional, related information.

See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software), [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis), [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes), [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions), and [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions).

## 3.8 Subcontractor Management

Describe subcontractor selection and involvement between the subcontractor and the acquirer, if any. If subcontractor selection, including the process, personnel, and criteria used, is described in a procurement plan, reference that document here. See also Topic [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance).

Involvement between the subcontractor and acquirer includes but is not limited to any or all of the following:

* On-site audits of subcontractor processes and products.
* Meetings and decision points that occur during the software development life cycle.
* Formal, progress, and technical reviews.
* Progress reports and deliverables.

See also [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight),

## 3.9 Project Involvement

Describe how the project will be involved in any software development performed by an organization external to the acquirer (e.g., another NASA organization, subcontractor), including activities such as but not limited to:

* Conducting or attending reviews.
* Conducting or reviewing the results of audits.
* Attending informal meetings.
* Receipt and/or review of reports.
* Review and/or approval of modifications and changes.
* Involvement in implementation tasks.
* Acceptance of the product.

Include in this section any access to facilities needed by the acquirer for their involvement in the software life cycle.

See also  [SWE-018 - Software Activities Review](/spaces/SWEHBVB/pages/32604449/SWE-018+-+Software+Activities+Review), [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes), [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice).

## 3.10 User involvement

Describe how the user will be involved in the software life cycle, including activities such as requirements development, prototype demonstrations, and software evaluations.  Items to consider capturing include scheduling, level of participation, expected inputs, expected results, and/or which specific user groups will be involved in each activity. Additionally, capture any expected or planned items to be supplied by the user, such as operational scenarios, a piece of software, a test facility, or a piece of hardware into which the software will be integrated.

See also [SWE-018 - Software Activities Review](/spaces/SWEHBVB/pages/32604449/SWE-018+-+Software+Activities+Review), [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis), [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test), Topic [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report),

## 3.11 Risk management

Describe how risk management will be performed on this software project, or reference a separate risk management plan (see [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) ). The risk management plan addresses initial risks and mitigation approaches for them,  as well as the plan for identifying and mitigating new risks as the software development progresses. Risk management also includes the risk strategy, such as the criteria or process by which risks get raised to the mission level or determining which risks need mitigation plans.

## 3.12 Security policy

Describe "the rules for need-to-know and access-to-information at each project organization level." Include the processes for ensuring the control and protection of the software being developed, associated support tools, and data. Include the plans for physical security of facilities. As applicable, include compliance with **NPD 2810.1** and with **NPR 2810.1**.

See also [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks).

## 3.13 Approval Required

Describe approvals required by the project for acceptance, operation, and maintenance activities, including regulatory approvals, required certifications, proprietary, usage, ownership, warranty, and licensing rights.

See also [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse), [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice).

## 3.14 Process for Scheduling, Tracking, and Reporting

Describe how task scheduling, progress tracking, and reporting will be performed for this project. Include information such as:

* The "plan for tracking the progress and cost of the individual work elements in each WBS category using an approved method."
* A description of the use of Earned Value (EV) or similar technique, as applicable.
* A description of the lowest WBS where progress reporting will be performed and how those low-level progress values will be rolled up and reported.
* "Methods, tools, techniques used to estimate and periodically re-estimate project cost, schedule, and resource requirements."
* Basis of estimation.
* Triggers for re-estimation.
* Types of reports and frequency of reporting (to Mission project, Branch, division, etc.).

See also [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes), [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule), [SWE-018 - Software Activities Review](/spaces/SWEHBVB/pages/32604449/SWE-018+-+Software+Activities+Review), [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule).

## 3.15 Training of personnel

Describe the plans for training software personnel, including project-unique software training needs such as mission-specific training or training for knowledge, skills, and tools used only on this project. The training plan may be included in the SDP/SMP or in a separate plan. When developing the training plan, be sure to address:

* Type of training to be provided.
* When training will be provided, e.g., just before a particular life cycle phase or a specific task.
* Personnel to receive specific types of training by role.
* Process for capturing, maintaining, and storing training records.

Refer to the Center Training Plan in this topic for opportunities that may meet some of the project's training needs. See also [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training)

## 3.16 Software life cycle model

Provide a description of the planned life cycle model chosen for the project, making sure to address:

* Life cycle phases and transition from one to the next.
* Life cycle reviews.
* Milestones to be achieved.
* Baselines to be established.
* Required approvals.
* The software integration and hardware/software integration processes.
* Software delivery processes.
* Software operations and maintenance processes.

See also [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones)

## 3.17 Configuration management

Describe how configuration management will be performed for the software, or reference a separate Software Configuration Management Plan (see [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) and the Software Configuration Management Plan section of this topic for recommended minimum content). The Software Configuration Management Plan includes information such as:

* The build or release plan, including the number of planned builds.
* Identification of configuration items.
* Description of the configuration management system.
* The process for baselining work products.
* Processing change requests.
* Change control board activities.
* Status accounting.
* Communication of configuration management decisions and action, e.g., to appropriate stakeholders.
* Data management, if not captured elsewhere.

See also [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement), [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting), [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management), [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase)

## 3.18 Document Deliverables

Describe the work products and documents to be created as part of the project, the relationships among those documents, and the role or organization responsible for each document. This includes the list of project deliverables. It may be graphical (e.g., a chart, table, or tree diagram, textual, or combination) to convey the relationships and document descriptions in the best manner possible to those who will need to understand it.

See also [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination).

## 3.19 Software Peer Review/Inspection Process

Describe or provide an overview of the peer review and/or inspection process to be used for products created as part of the software development life cycle, e.g., plans, requirements, design, code. Specify which types of products will be reviewed, and if all code will not be reviewed, specify how code to be inspected is determined. Reference the appropriate project peer review/inspection processes and procedures (see [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), and [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)). If the peer review/inspection process is documented in a separate document(s), provide an overview followed by a reference to the appropriate document(s).

See also [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination).

## 3.20 Process for early identification of testing requirements that drive software design decisions

Describe how testing requirements that drive design decisions (e.g., special system-level timing requirements/checkpoint restart) will be identified and captured in the earliest phases of the life cycle, before costly design decisions are made that will need to be altered or replaced to accommodate testing requirements.

Describe any test requirements that drive or require early builds/deliveries to conduct tests on other system components. For example, an early software build is often required to enable early testing of some hardware capabilities.

See also [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination).

## 3.21 Software Metrics

Describe or provide an overview of the planned software measures to be collected, analyzed, and the metrics to be used for tracking and reporting progress, improving processes, identifying issues, and other purposes. Include collection and analysis procedures for the project. Define the project objectives for collecting the measures. Include references for any project processes and procedures that further describe or provide details for software metrics collection and processing (see [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)). Include, for each identified measure and metric:

* Format/units.
* Collection method and frequency.
* Role responsible for collecting the data.
* Storage location and data retention.
* Analysis method and frequency.
* Analysis reporting method, frequency, and audience.
* Threshold that, if crossed, would prompt further analysis or other action.

See also Topic [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects), [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements), [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements), [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data), [SWE-199 - Performance Measures](/spaces/SWEHBVD/pages/102695532/SWE-199+-+Performance+Measures).

## 3.22 Software Documentation Content

Provide content lists for the documents to be created as part of the project or a list of templates or standards governing and describing that content. This topic in the Handbook provides recommended content lists for several software documents. The content lists need not be incorporated in the SDP/SMP; they may be included by reference.

See also [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software), [SWE-153 - ETA Define Document Content](/spaces/SWEHBVD/pages/102695509/SWE-153+-+ETA+Define+Document+Content).

## 3.23 Management, Development, and Testing Approach for COTS, GOTS, MOTS

Describe or reference processes specific to development, management, and testing of Commercial Off the Shelf (COTS), Government Off the Shelf (GOTS), Modified Off the Shelf (MOTS), reused, or open-source software component(s) that are included within the NASA system or subsystem(s) in this project. By their nature, these types of software present challenges because access may be limited to requirements, design, and testing documentation. Additionally, software stability, access and inclusion of updates and upgrades, and access to persons with critical knowledge of the software can present challenges not found in new software development.

Guidance for [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) in this Handbook also describes special considerations relative to these types of software and their inclusion in NASA projects.

Include plans for dealing with these challenges and considerations in the SDP/SMP, or include references to the project documents that address them.

See also [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks), [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items), [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels), [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances), [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software).

## 3.24 Other possible content

Other information that might be included, or referenced if captured elsewhere, in a SDP/SMP includes but is not limited to:

* Software deliverables. [453](#_tabs-<p></p>)
* External dependencies affecting schedule and budget. [453](#_tabs-<p></p>)
* Development method, such as structured programming or object-oriented programming. [453](#_tabs-<p></p>)
* Prototyping, modeling, or simulation activities. [453](#_tabs-<p></p>)
* Software assurance activities. [453](#_tabs-<p></p>)
* Schedule. [453](#_tabs-<p></p>)
* Effort. [453](#_tabs-<p></p>)
* Budget. [453](#_tabs-<p></p>)
* Data management, including project data, records, and information to be captured and maintained. [453](#_tabs-<p></p>)
* Stakeholder involvement. [453](#_tabs-<p></p>)
* Assumptions, e.g., planning and estimation assumptions. [453](#_tabs-<p></p>)
* Issue handling for entities outside the control of the project, including escalation/appeal process. [057](#_tabs-<p></p>)
* Staffing levels across the life cycle.
* User training.

See also [SWE-174 - Software Planning Parameters](/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters), [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records), [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability), [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage), [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior), [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase), [SWE-196 - Software Retirement Archival](/spaces/SWEHBVD/pages/102695531/SWE-196+-+Software+Retirement+Archival), [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs).

## 3.25 Plan updates

Review at regular intervals, revise, and update the SDP/SMP to keep its content current "following significant changes in customer-specified requirements, budget, schedule, or other constraints.  Criteria that often trigger re-planning include:

* Significant changes in scope, schedule, or budget.
* Delay in receipt of key component or service that is externally supplied.
* Inability to meet a major milestone." [453](#_tabs-<p></p>)

Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) provides guidance for the maturity of plans, including the SDP/SMP, at various life cycle reviews.

See also SWE-013[SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans).

## 3.26 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

SDPs/SMPs are required for every project because they provide the overall view of the development and management effort. However, plans are written to a level of detail appropriate for and commensurate with the size, complexity, risk, and required safety of the software. Small projects may wish to work with the Engineering Technical Authority to tailor an existing SDP/SMP specifically for small projects. Tailoring a proven plan from a similar project can reduce the overall plan development effort. Another option for small projects is to use one generic SDP/SMP to cover several small projects if they are managed in a similar fashion.

When writing the SDP/SMP, small projects may choose to incorporate other plans, such as the software assurance plan or the configuration management plan, in the SDP/SMP. This means that project roles responsible for those plans may be part of the group authoring of the SDP/SMP.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-031)

  [Manager's Handbook for Software Development,](http://www.everyspec.com/NASA/NASA-General/SEL-84-101_REV-1_1990_30283/ "Click to open in new window")

  SEL-84-101, Revision 1, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1990.
* (SWEREF-057)

  [Software Management Plan (SMP) Template,](https://nasa.sharepoint.com/:w:/r/teams/grcsepg/_layouts/15/Doc.aspx?sourcedoc=%7BF3CD9E46-25D3-4622-BDF6-FDDDE2EA7D58%7D&file=GRC-SW-TPLT-SMP%20-%20Software%20Management%20Plan%20Template.docx&action=default&mobileredirect=true&DefaultItemOpen=1 "Click to open in new window")

  GRC-SW-TPLT-SMP, NASA Glenn Research Center (GRC), 2009.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-145)

  [Software Quality Assurance Plan Template,](http://users.csc.calpoly.edu/~jdalbey/308/Resources/NASAsqaplan.html "Click to open in new window")

  California Polytechnic University, extracted from Reusable Software Management Plan, NASA Goddard Space Flight Center (GSFC). Accessed January 3, 2012 from http://users.csc.calpoly.edu/~jdalbey/308/Resources/NASAsqaplan.html.
* (SWEREF-165)

  [Software Development Management Planning,](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=5010194 "Click to open in new window")

  Cooper, Jack, IEEE Transactions on Software Engineering, January 1984.  Retrieved December 21, 2011 from http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5010194&tag=1.
* (SWEREF-217)

  [IEEE Computer Society, "IEEE Standard for Software Project Management Plans",](http://standards.ieee.org/findstds/standard/1058-1998.html "Click to open in new window")

  IEEE 1058-1998, 1998.  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-328)

  [Software Engineering Institute. (November, 2010). "CMMI for Acquisition, Version 1.3,"](http://www.sei.cmu.edu/reports/10tr032.pdf "Click to open in new window")

  Software Engineering Institute. (November, 2010). CMU/SEI-2010-TR-032. Carnegie-Mellon University. For SWE-035, see page 351 of this document.
  Retrieved on November 20, 2017 from http://www.sei.cmu.edu/reports/10tr032.pdf.
* (SWEREF-402)

  [NASA Information Security Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2810&s=1E "Click to open in new window")

  NASA Office of the Chief Information Officer, May, 2015. NPD 2810.1E,
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-453) Project Planning Process,  580-PC-004-07, Software Engineering Division (ISD), NASA Goddard Space Flight Center (GSFC), 2020. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-532)

  [Computer Software/Software Safety Policy Requirements/Potential Inadequacies](https://llis.nasa.gov/lesson/1021 "Click to open in new window")

  Public Lessons Learned Entry: 1021.
* (SWEREF-542)

  [Computer Hardware-Software/International Space Station/Software Development](https://llis.nasa.gov/lesson/1132 "Click to open in new window")

  Public Lessons Learned Entry: 1132.
* (SWEREF-552)

  [Kennedy Space Center (KSC) Projects and Resources Online (KPRO) Software Development and Implementation](https://llis.nasa.gov/lesson/1384 "Click to open in new window")

  Public Lessons Learned Entry: 1384.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes) * [SWE-006 - Center Software Inventory](/spaces/SWEHBVD/pages/102695396/SWE-006+-+Center+Software+Inventory) * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) * [SWE-153 - ETA Define Document Content](/spaces/SWEHBVD/pages/102695509/SWE-153+-+ETA+Define+Document+Content) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-174 - Software Planning Parameters](/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters) * [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase) * [SWE-196 - Software Retirement Archival](/spaces/SWEHBVD/pages/102695531/SWE-196+-+Software+Retirement+Archival) * [SWE-199 - Performance Measures](/spaces/SWEHBVD/pages/102695532/SWE-199+-+Performance+Measures) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs) * [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse) * [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice)        * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

* **Computer Software/Software Safety Policy Requirements/Potential Inadequacies (Cover essential requirements for the project). Lesson Learned 1021[532](#_tabs-<p></p>):**  "NASA is committed to assuring that required program management plans and any subordinate plans such as software or safety management plans cover the essential requirements for programs where warranted by cost, size, complexity, lifespan, risk, and consequence of failure."
* **Computer Hardware-Software/International Space Station/Software Development** **(Plan for user involvement). Lesson Learned 1132[542](#_tabs-<p></p>):**  "The lack of user involvement results in increased schedule and safety risk to the program... follow a concurrent engineering approach to building software that involves users and other key discipline specialists early in the software development process to provide a full range of perspectives and improve the understanding of requirements before code is developed."

* **Kennedy Space Center (KSC) Projects and Resources Online (KPRO) Software Development and Implementation (Project team planning).** **Lesson Learned 1384[552](#_tabs-<p></p>):**  "When planning and selecting team resources for a project, consider how the resources can work together and support each other, along with the skills required. This can be a factor in meeting or delaying software project milestones if an alternative resource has not been endorsed by the team members."

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Stakeholder agreements should be formally documented](https://software.gsfc.nasa.gov/lesson-details//). **Lesson Number 51**: The recommendation states: "Stakeholder agreements should be formally documented so commitments are understood and planned for well in advance."
* [Roles & Responsibilities should be documented and agreed to by all parties](https://software.gsfc.nasa.gov/lesson-details//). **Lesson Number 52**: The recommendation states: "Document roles and responsibilities for all positions, and identify and address potential areas of overlap, underlap, ambiguity, or conflict."
* [Document stakeholders' expectations](https://software.gsfc.nasa.gov/lesson-details//). **Lesson Number 55**: The recommendation states: "Stakeholder expectations, for all lifecycle phases, should be documented and agreed to early in the project."
