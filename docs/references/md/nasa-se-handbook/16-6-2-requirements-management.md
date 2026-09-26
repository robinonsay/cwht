# 6.2 Requirements Management

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 130–134. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §6.2`.

Requirements Management Requirements management activities apply to the management of all stakeholder expectations, customer requirements, and technical product requirements down to the lowest level product component requirements (hereafter referred to as expectations and requirements). This includes physical functional and operational requirements, including those that result from interfaces between the systems in question and other external entities and environments. The Requirements Management Process is used to:
- Identify, control, decompose, and allocate requirements across all levels of the WBS.
- Provide bidirectional traceability.

Refer to Section 6.1.2 in the NASA Expanded Guidance for Systems Engineering at https://nen.nasa. gov/web/se/doc-repository for additional guidance on:

DEFINITIONS Traceability: A discernible association between two or more logical entities such as requirements, system elements, verifications, or tasks. Bidirectional traceability: The ability to trace any given requirement/expectation to its parent requirement/ expectation and to its allocated children requirements/expectations.

From system design processes Expectations and Requirements to Be Managed From project and Technical Assessment Process Requirements Change Requests From Technical Assessment Process TPM Estimation/ Evaluation Results From Product Verification and Validation Processes Product Verification and Product Validation Results

Prepare to conduct requirements management

To Configuration Management Process Requirements Documents

Conduct requirements management

Conduct expectations and requirements traceability

Manage expectations and requirement changes

Approved Changes to Requirements Baselines

To Technical Data Management Process

Capture work products from requirements management activities

Requirements Management Work Products

FIGURE 6.2‑1 Requirements Management Process

- Manage the changes to established requirement
baselines over the life cycle of the system products.

#### 6.2.1 Process Description

FIGURE 6.2-1 provides a typical flow diagram for the

Requirements Management Process and identifies typical inputs, outputs, and activities to consider in addressing requirements management.
##### 6.2.1.1 Inputs

There are several fundamental inputs to the Requirements Management Process.
- Expectations and requirements to be managed:
Requirements and stakeholder expectations are identified during the system design processes, primarily from the Stakeholder Expectations Definition Process and the Technical Requirements Definition Process.

- Requirement change requests: The Requirements
Management Process should be prepared to deal with requirement change requests that can be generated at any time during the project life cycle or as a result of reviews and assessments as part of the Technical Assessment Process.
- TPM estimation/evaluation results: TPM estimation/evaluation results from the Technical
Assessment Process provide an early warning of the adequacy of a design in satisfying selected critical technical parameter requirements. Variances from expected values of product performance may trigger changes to requirements.
- Product verification and validation results:
Product verification and product validation results from the Product Verification and Product Validation Processes are mapped into the

requirements database with the goal of verifying and validating all requirements.

and initiate corrective actions to eliminate inconsistencies.

##### 6.2.1.2 Process Activities

6.2.1.2.3  Conduct Expectations and Requirements

6.2.1.2.1  Prepare to Conduct Requirements

Traceability As each requirement is documented, its bidirectional traceability should be recorded. Each requirement should be traced back to a parent/source requirement or expectation in a baselined document or identified as self-derived and concurrence on it sought from the next higher level requirements sources. Examples of self-derived requirements are requirements that are locally adopted as good practices or are the result of design decisions made while performing the activities of the Logical Decomposition and Design Solution Processes.

Management Preparing to conduct requirements management includes gathering the requirements that were defined and baselined during the Requirements Definition Process. Identification of the sources/owners of each requirement should be checked for currency. The organization (e.g., change board) and procedures to perform requirements management are established. 6.2.1.2.2 Conduct Requirements Management

The Requirements Management Process involves managing all changes to expectations and requirements baselines over the life of the product and maintaining bidirectional traceability between stakeholder expectations, customer requirements, technical product requirements, product component requirements, design documents, and test plans and procedures. The successful management of requirements involves several key activities:
- Establish a plan for executing requirements
management.
- Receive requirements from the system design processes and organize them in a hierarchical tree
structure.
- Maintain bidirectional
requirements.

traceability

between

- Evaluate all change requests to the requirements
baseline over the life of the project and make changes if approved by change board.

The requirements should be evaluated, independently if possible, to ensure that the requirements trace is correct and that it fully addresses its parent requirements. If it does not, some other requirement(s) should complete fulfillment of the parent requirement and be included in the traceability matrix. In addition, ensure that all top-level parent document requirements have been allocated to the lower level requirements. If there is no parent for a particular requirement and it is not an acceptable self-derived requirement, it should be assumed either that the traceability process is flawed and should be redone or that the requirement is “gold plating” and should be eliminated. Duplication between levels should be resolved. If a requirement is simply repeated at a lower level and it is not an externally imposed constraint, it may not belong at the higher level. Requirements traceability is usually recorded in a requirements matrix or through the use of a requirements modeling application.

- Maintain consistency between the requirements, the ConOps, and the architecture/design,

6.2.1.2.4  Managing Expectations and Requirement

6.2.1.2.5 Key Issues for Requirements Management

Changes Throughout early Phase A, changes in requirements and constraints will occur as they are initially defined and matured. It is imperative that all changes be thoroughly evaluated to determine the impacts on the cost, schedule, architecture, design, interfaces, ConOps, and higher and lower level requirements. Performing functional and sensitivity analyses will ensure that the requirements are realistic and evenly allocated. Rigorous requirements verification and validation will ensure that the requirements can be satisfied and conform to mission objectives. All changes should be subjected to a review and approval cycle to maintain traceability and to ensure that the impacts are fully assessed for all parts of the system.

Requirements Changes

Once the requirements have been validated and reviewed in the System Requirements Review (SRR) in late Phase A, they are placed under formal configuration control. Thereafter, any changes to the requirements should be approved by a Configuration Control Board (CCB) or equivalent authority. The systems engineer, project manager, and other key engineers usually participate in the CCB approval processes to assess the impact of the change including cost, performance, programmatic, and safety. Requirement changes during Phases B and C are more likely to cause significant adverse impacts to the project cost and schedule. It is even more important that these late changes are carefully evaluated to fully understand their impact on cost, schedule, and technical designs. The technical team should also ensure that the approved requirements are communicated in a timely manner to all relevant people. Each project should have already established the mechanism to track and disseminate the latest project information. Further information on Configuration Management (CM) can be found in Section 6.5.

Effective management of requirements changes requires a process that assesses the impact of the proposed changes prior to approval and implementation of the change. This is normally accomplished through the use of the Configuration Management Process. In order for CM to perform this function, a baseline configuration should be documented and tools used to assess impacts to the baseline. Typical tools used to analyze the change impacts are as follows:
- Performance Margins: This tool is a list of key
performance margins for the system and the current status of the margin. For example, the propellant performance margin will provide the necessary propellant available versus the propellant necessary to complete the mission. Changes should be assessed for their impact on performance margins.
- CM Topic Evaluators List: This list is developed
by the project office to ensure that the appropriate persons are evaluating the changes and providing impacts to the change. All changes need to be routed to the appropriate individuals to ensure that the change has had all impacts identified. This list will need to be updated periodically.
- Risk System and Threats List: The risk system
can be used to identify risks to the project and the cost, schedule, and technical aspects of the risk. Changes to the baseline can affect the consequences and likelihood of identified risk or can introduce new risk to the project. A threats list is normally used to identify the costs associated with all the risks for the project. Project reserves are used to mitigate the appropriate risk. Analyses of the reserves available versus the needs identified by the threats list assist in the prioritization for reserve use.

The process for managing requirements changes needs to take into account the distribution of information related to the decisions made during the change process. The Configuration Management Process needs to communicate the requirements change decisions to the affected organizations. During a board meeting to approve a change, actions to update documentation need to be included as part of the change package. These actions should be tracked to ensure that affected documentation is updated in a timely manner.

- Establish a strict process for assessing requirement changes as part of the Configuration
Management Process.

Requirements Creep

- Measure the functionality of each requirement
change request and assess its impact on the rest of the system. Compare this impact with the consequences of not approving the change. What is the risk if the change is not approved?

“Requirements creep” is the term used to describe the subtle way that requirements grow imperceptibly during the course of a project. The tendency for the set of requirements is to relentlessly increase in size during the course of development, resulting in a system that is more expensive and complex than originally intended. Often the changes are quite innocent and what appear to be changes to a system are really enhancements in disguise. However, some of the requirements creep involves truly new requirements that did not exist, and could not have been anticipated, during the Technical Requirements Definition Process. These new requirements are the result of evolution, and if we are to build a relevant system, we cannot ignore them. There are several techniques for avoiding or at least minimizing requirements creep:
- The first line of defense is a good ConOps that has
been thoroughly discussed and agreed-to by the customer and relevant stakeholders.
- In the early requirements definition phase, flush
out the conscious, unconscious, and undreamed-of requirements that might otherwise not be stated.

- Establish official channels for submitting change
requests. This will determine who has the authority to generate requirement changes and submit them formally to the CCB (e.g., a contractor-designated representative, project technical leads, customer/science team lead, or user).

- Determine if the proposed change can be accommodated within the fiscal and technical resource
budgets. If it cannot be accommodated within the established resource margins, then the change most likely should be denied. 6.2.1.2.6 Capture Work Products

These products include maintaining and reporting information on the rationale for and disposition and implementation of change actions, current requirement compliance status and expectation, and requirement baselines.
##### 6.2.1.3 Outputs

Typical outputs from the requirements management activities are:
- Requirements Documents: Requirements documents are submitted to the Configuration
Management Process when the requirements are baselined. The official controlled versions of these documents are generally maintained in electronic format within the requirements management tool
