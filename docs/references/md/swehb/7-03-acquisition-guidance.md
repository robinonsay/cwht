# 7.03 - Acquisition Guidance

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695620. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance

7.03 - Acquisition Guidance

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695620)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695620&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Planning](#tabs-2)
* [3. Solicitation, Selection, and Award](#tabs-3)
* [4. Technical Monitoring and Quality Assurance](#tabs-4)
* [5. Contract Administration](#tabs-5)
* [6. Product Acceptance and Control](#tabs-6)
* [7. Contract Closeout](#tabs-7)
* [8. Useful Practices, Activities and Templates](#tabs-8)
* [9. Resources](#tabs-9)
* [10. Lessons Learned](#tabs-10)

# 1. Purpose

Guidance for projects implementing those requirements in NASA Procedural Requirement (NPR) 7150.2, NASA Software Engineering Requirements that address software acquisition. This guidance is intended for all persons responsible for the software acquisition process, from the planning stages through contract closeout. The acquisition may involve procedures and regulations external to the software community, including variations by contract type; therefore, it is important to consult Center guidance and coordinate acquisition activities among the proper stakeholders, including, but not limited to, software engineering, procurement, finance, and contracts.

## 1.1 Roles

| Role | Responsibility |
| --- | --- |
| Project Manager | Approve the procurement plan. |
| Software Lead Engineer | Prepare procurement plan; prepare a statement of work (SOW) software requirements and software data requirements for the contract; monitor execution of the contract; conduct trade studies, engineering analyses. |
| System Engineer | Conduct trade studies, engineering analyses. |
| Contracting Officer (CO) | Prepare acquisition approach, prepare solicitation, guide proposal evaluation, prepare contracts, prepare modifications to contracts. |
| Contracting Officer's Representative (COR) | Work with CO to plan the acquisition approach, prepare SOW, evaluate proposals, determine the technical adequacy of the proposed approach, monitor technical implementation. |
| Software Technical Authority | Before contract release, verify that the SOW includes the complete flow down of the Agency and Center software requirements [recommended practice]. |

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 2. Planning

Before software acquisition can be carried out, a need must be identified for which a solution is required.  During the planning stage, various options to address the identified need are evaluated.  The following are possible options:

* Acquire off-the-shelf (OTS) product.
* Develop/perform service in-house (make/buy decision). (See [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment))
* Contract development/service.
* Use/enhance existing product/service (consider reuse of existing software components for applicability to project).

If the solution to the need will involve software, NPR 7150.2 applies, and the acquisition planning guidance below supports project success:

1. Define the scope of the system of interest.
2. Identify the goals and objectives of the software portion of the system.
3. Identify key stakeholders.
4. Perform “make or buy” market research/trade studies to determine if an off the shelf (OTS) solution exists.
5. Establish criteria (and a plan) for the studies:
   * Assess potential products and technologies.
   * Assess how well technical requirements are addressed.
   * Assess estimated costs, including support.
   * Assess safety criticality.
   * Identify risks (delivery, safety, development practices used by the supplier, supplier track record, etc.). See also [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)
   * Assess provider business stability, past performance, ability to meet maintenance requirements, etc.
   * Assess commercial off-the-shelf/government off-the-shelf/military off-the-shelf products for potential use. (See [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software).)
   * Assess the availability of existing products that could meet the need or be modified to meet the need.
   * Assess the availability of qualified personnel for development or modification activities.
   * Assess estimated costs (time, personnel, materials, etc.), including support.
   + Use past projects as a basis, where appropriate.* Identify risks.

* Technical requirements (functional, operational, performance):
* NPR 7150.2 classification.
* Constraints and limitations (cost, schedule, resources).
* Use past studies, known alternatives, existing make/buy criteria.
* Conduct studies:
* Identify in-house capabilities to meet the need:
* Determine if the solution will be custom made, an existing product, or a modified existing product.

6. Identify any acquisition risks based on requirements and “make or buy” decisions.
7. Create at least one government software cost estimate ([SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation)) for this work.
8. Document analysis:

* Expected classification of the software to be acquired.
* Availability of in-house staff and funding resources.
* Availability of the software product(s).
* Projected licensing and support costs.
* List of potential suppliers.
* Security considerations.
* Potential risks related to supplier viability and past performance.

9. Document solution choice and basis for that choice:

* The estimate of in-house versus acquisition costs (including OTS solutions and any associated costs for requirements not met by the OTS solution).
* Comparison of cost estimates to available funding.
* Risk assessment.
* Assumptions, observations, rationale, determining factors.
* Significant issues, impacts of each option.
* If the solution is in-house development/service, an acquisition is no longer required.
* If the solution is to acquire product/service, continue with this guidance as needed based on development under contract or purchase OTS solution.
* Other planning decisions resulting in the best overall value to NASA.
* Description of the chosen acquisition strategy.

10. Identify "relevant stakeholders" based on requirements and “make or buy” decisions:

* Those directly concerned with or affected by, the acquisition decision.
* May include management, the project team, procurement, customers, end-users, and suppliers.

11. Ensure acquisition team includes organization from NASA (acquirer) with appropriate (see [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software)) non-expired Capability Maturity Model Integration (CMMI®) rating as measured by a CMMI Institute authorized or certified lead appraiser.\*
12. Report analysis and resulting decision to appropriate stakeholders.
13. Document lessons learned for future acquisition activities.
14. Develop acquisition schedule, including solicitation, supplier selection, supplier monitoring, and product acceptance and transition to operations, as appropriate. See also [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones).
15. Develop an acquisition plan using a Center-specific template.

**Class A software acquisition guidance** – When a project seeks to acquire a system that includes Class A software, the project's acquisition team is required to have support from personnel in an organization that has been rated at a Capability Maturity Model Integration for Development (CMMI®-DEV) Maturity Level 3 or higher or rated at CMMI®-DEV Capability Level 3 in at least the process areas of Supplier Agreement Management and Process and Product Quality Assurance. Evidence that a CMMI®-DEV Level 3 rated organization has participated in the acquisition activities could include direct support on the acquisition team and/or review and approval of the acquisition products by the CMMI®-DEV rated organization. The extent of the CMMI®-DEV Level 3 rated organization's support required for a Class A acquisition should be determined by the Center's Engineering Technical Authority responsible for the project. Identification of the appropriate personnel from an organization that has been rated at a CMMI®-DEV Level 3 or higher to support the project acquisition team is the responsibility of the designated Center Engineering Technical Authority and Center management.

**Class B software acquisition guidance** - In the case of the project's acquiring a system that includes Class B software, the project's acquisition team is required to have support from organizations that have been rated at CMMI®-DEV Level 2 or higher or rated at CMMI®-DEV Capability Level 2 in at least the process areas of Supplier Agreement Management and Process and Product Quality Assurance. Evidence that a CMMI®-DEV Level 2 rated organization has participated in the acquisition activities could include direct involvement in the development of supplier agreements or review and approval of these agreements. The support must also include the review and approval of any software-related contract deliverables. The Center Engineering Technical Authority responsible for the project determines the extent of the CMMI®-DEV Level 2 rated organization's support required for a Class B acquisition. Identification of the appropriate personnel from an organization that has been rated at a CMMI®-DEV Level 2 or higher to support the project acquisition team is the responsibility of the designated Center Engineering Technical Authority and Center management.

**Classes A and B general guidance -** The Center Engineering Technical Authority has the responsibility for ensuring that the appropriate and required NASA software engineering requirements are included in an acquisition. For those cases in which a Center or project desires a general exclusion from the NASA software engineering requirement(s) in this NPR or desires to generically apply specific alternate requirements that do not meet or exceed the requirements of this NPR, the requester shall submit a waiver for those exclusions or alternate requirements for approval by the NASA Headquarters' Chief Engineer with appropriate justification.

See [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects).

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 3. Solicitation, Selection, and Award

Once the planning activities for software acquisition have been completed and the decision has been made to acquire the software or software development services, a selection process needs to be followed to choose the best provider for the project. This process typically begins with the development of a Statement of Work (SOW).

Typically, solicitations are prepared by the procurement or contracts department with input from project management and engineering. Solicitations are as complete as possible to ensure potential providers are aware of all tasks and activities for which they will be held responsible.

Checklists (e.g., the NASA Process Asset Library (PAL) contains checklists for NPR 7150.2 requirements by class and safety criticality) and solicitations for similar projects help ensure that all required activities are included in the solicitation. Example solicitations, Statements of Work, and work breakdown structures (WBSs) that are considered "best practices" are also helpful starting points; using problematic examples will only carry forward the problems exhibited or caused by those documents.

The following is a list of useful practices when documenting tasks and activities in the solicitation:

* Keep the task descriptions clear, concise, and in terms that providers will understand.
* Avoid over-specifying (specifying every item to the smallest detail leaving no options).
* Avoid under-specifying (providing insufficient or incomplete details).
* Clearly mark mandatory versus optional/recommended tasks, activities, standards, etc.

The following recommendations should be considered as part of the SOW development process. Additionally, an SOW checklist reference is included in the Useful Practices, Activities and Templates section (tab 8) of this guidance document.

1. Develop solicitation, including Statements of Work:

* Acceptance criteria ([SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria)).
* Solicitation constraints.
* Proper requirements  from the software development perspective\*:

+ Software classification (from NPR 7150.2) and the software safety-criticality determination (NASA-STD-8739.8 [278](#_tabs-<p>9</p>)).
+ Technical requirements.
+ Adherence to requirements for safety-critical software (see [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), and NPR 7150.2, Appendix C).
+ Development standard to be followed, if any.
+ Development cycle to be followed or indication that the developer can choose the appropriate life cycle.
+ Surveillance activities (and acquirer involvement), including monitoring activities, reviews, audits ([SWE-045 - Project Participation in Audits](/spaces/SWEHBVD/pages/102695419/SWE-045+-+Project+Participation+in+Audits)), decision points, meetings, etc. ([SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight))
+ Management and support requirements (project management, schedule and schedule updates ([SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)), configuration management, non-conformance and change tracking, risk management, metrics collection, Independent Verification and Validation (IV&V) support, required records, traceability records, electronic records and code access ([SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access)), V&V, etc.)
+ Requirements for maintenance, support, updates, new versions, training to be included in life cycle and cost estimates.
+ Concise task and deliverable descriptions, including delivery format ([SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products)).
+ Media format for code deliverables ([SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products)).
+ Templates or Data Item Descriptions (DIDs) for documentation deliverables. ([7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance))
+ Complete set of deliverables with delivery dates, review periods, and acceptance procedures for each.
+ The time period for responses to review findings, including making changes.
+ Data Requirements Documents (DRDs) for deliverables, if appropriate.
+ Government and contractor proprietary, usage, ownership, warranty, data, and licensing rights, including transfer.
+ The requirement to include notice of the use of open-source software in developed code.
+ Off the Shelf (OTS) software requirements ([SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software)) (identity which requirements are met by software, provide OTS software documentation, such as usage instructions, etc.)
+ List of all mandatory NASA software development standards and DIDs, as applicable.
+ Requirements for non-expired CMMI (Capability Maturity Model Integration®) rating as measured by a Lead Appraiser certified by the CMMI Institute ([SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software)). (See the Useful Practices, Activities and Templates section (tab 8) of this topic for sample text for the solicitation.)

Acquisition should not simply levy NPR 7150.2 as a whole on a potential supplier, as it contains some NASA institutional requirements. If a project is acquiring software development services for Classes A through H software, the project should only levy the applicable minimal set of supplier requirements, plus additions that address specific risk concerns. Requirements that are the responsibility of the Agency, Center, or Headquarters should not be levied on a contractor, as they will cause confusion and unnecessary expense.

If the class of software and the safety-critical designation are known when the SOW is written, the project can levy, via a compliance matrix, the project-/system-specific set of NPR 7150.2 requirements to be satisfied by the contractor. If the class and/or safety-critical designation are not yet known, the SOW should list applicable requirements for each class and safety-critical designation with instructions to comply accordingly when a class and safety-critical designation are determined.

The full list of project-related requirements can be found in the compliance matrices found in the Software Engineering Community of Practice Document Repository on the NASA Engineering Network (NEN).

2. Ensure proper review of SOW before delivery to procurement/contracts official:

* + Technical Authority to ensure proper flow down of NPR 7150.2 requirements.
  + Coordinate with the Safety and Mission Assurance Office to ensure all quality assurance requirements, clauses, and intended delegations are identified and included.

3. Identify potential suppliers.  
4. Distribute solicitation package.  
5. Evaluate proposals (typically an evaluation team), based on selection criteria established during the acquisition planning phase, including:

* + Cost estimation comparisons.

+ - Evaluation of how well proposed solutions meet the requirements (including interface and technology requirements, NPR 7150.2 requirements).
  - Staff available.
  - Past performance.
  - Software engineering and management capabilities.
  - Prior expertise on similar projects.
  - Available resources (facilities, hardware, software, training, etc.).
  - Capability Maturity Model Integration (CMMI®) ratings.
  - Check the CMMI Published Appraisal Results (PARs) [327](#_tabs-<p>9</p>)  to confirm the non-expired rating  .
  - Be sure to check the scope of the organization holding the CMMI® rating to confirm the rating is held by the specific organization submitting the proposal.
  - Other factors that are relevant to the project.

6. Select supplier/contractor and document the basis for selection.  
7. Negotiate, finalize and document contract:

* + Based on SOW.
  + Management reviews and meetings, such as:  
    - Formal reviews, such as those found in NPR 7123.1, NASA Systems Engineering Processes and Requirements, and NPR 7120.4, NASA Engineering and Program/Project Management Policy.
    - Technical reviews.
    - Progress reviews.
    - Peer reviews (see Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) in Handbook).
    - Software quality assurance meetings.
    - System integration test and verification meetings.
    - System safety meetings.
    - Configuration management meetings.
    - Other relevant reviews for this project.
  + Consider for inclusion in contract provisions (description of the method to be used) for verification of:  
    - Contractor handling of requirements changes.
    - Accuracy of contractor transformation of high-level requirements into software requirements and detailed designs.
    - Interface specifications between the contractor’s product and systems external to it.
    - Adequacy of contractor’s risk management plan and its implementation in accordance with the required activities in the project Software Risk Management Plan.
    - Adequacy of the contractor’s integration and test plan and its implementation in accordance with the required activities in the project Software Integration and Test Plan.
    - Adequacy of the contractor’s configuration management plan and its implementation in accordance with the required activities in the project Software Configuration Management Plan.
  + Consider for inclusion in the contract the content and frequency of progress reports and metrics submissions.
  + Consider for inclusion in the contract identification of quality records to be maintained by the supplier.
  + Consider for inclusion in the contract the delivery process and how it will be accomplished; if incremental development and delivery agreed upon, state how the validation process works, e.g., incremental validation, and whether it requires integration and test with software/hardware products developed by acquirer and/or other contractors or organizations (other institutes, universities, etc.).
  + Consider for inclusion in the contract a policy for maintaining the software after delivery: Who is responsible for maintenance of the software, tools, testbeds, and documentation updates.

See also [PAT-024 - Checklist for Choosing Off-The Shelf Software](/spaces/SITE/pages/116293728/PAT-024+-+Checklist+for+Choosing+Off-The+Shelf+Software),

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 4. Technical Monitoring and Quality Assurance

Once the provider has been chosen, the acquisition process moves into a technical monitoring role.  The following guidance should be included when establishing the process for provider monitoring and quality assurance:

1. Provide technical requirements interpretation for the contractor.
2. Ensure contractor requirements documents meet original intent.
3. Evaluate contractor progress with respect to cost.
4. Periodically monitor contractor skill mix to ensure agreed-upon skills and experience levels are being provided.
5. Oversee government-furnished equipment (GFE) to ensure equipment and information provided in a timely manner.
6. Periodically assess contractor processes to ensure conformance to process requirements stated in the contract.
7. Review and assess the adequacy of contractor-provided documentation and ensure contractor implementation of feedback, consider using Formal Inspections ([SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures)) to accomplish this task.
8. Track status considering the following example questions:

* + Is the contractor meeting their staffing plan?
  + Have the project and the contractor met the user’s needs?
  + Does the contractor have a stable, educated staff?
  + Does the contractor’s project have adequate resources, e.g., adequate staffing and computer resources?
  + Is there realistic planning/budgeting in place?
  + Is the build plan being met?
  + Does the contractor have a good understanding of what is required?
  + Are the requirements stable?
  + Is the completion of designed functionality visible?
  + Is the evolving capability and performance of the contractor’s product likely to impact development on the acquirer side of the interface?
  + Are integration and testing proceeding as planned?
  + Is contractor cost/schedule performance on target?
  + Is the contractor developing a quality product?

9. Provide regular status reviews to higher-level management on contractor progress.  
10. Regularly assess the status of identified risks and provide reports during management reviews.   
11. Software engineering should provide a technical review of the level required to enhance the probability of mission success. (See the "Useful Practices, ..." tab of this topic for a list of areas to consider for software engineering technical review.)

## 4.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 5. Contract Administration

In addition to monitoring the selection provider’s progress and quality, contract administration activities are also carried out for the project.  The following guidance should be included when establishing the process for contract administration:

1. Regularly assess contractor financial data and invoices against budget.
2. Work with Contracting Officer to ensure timely resolution of any contract-related issues.
3. Work with Contracting Officer to ensure the timely address of needed modifications to contract terms and conditions, as needed.  These are primarily those affecting schedule, costs, services/products, resources (people, facilities), deliverables.
4. Periodically evaluate contractor performance in a manner consistent with the contract and provide a documented evaluation to the Contract Officer.

## 5.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 6. Product Acceptance and Control

Once the provider is ready to deliver the software product, the acquirer should have a process in place for review and acceptance of the product.  The following guidance should be included when establishing the process for product acceptance:

1. Review deliverables based on agreed-upon acceptance criteria (or generally accepted standards, if specific criteria have not been established), document results, and work with a contractor to resolve acceptance issues.

* + Typically, an acceptance test plan is created addressing the following:  
    - Acquirer and contractor roles and responsibilities.
    - Defined test strategy.
    - Defined test objectives.
    - Defined acceptance criteria.
    - Developed test Scenarios.
    - Developed test scripts.
    - Developed a test matrix.
    - Time and resources estimate.
    - Approval cycle.
    - Strategy for post-delivery problem resolutions.
  + Once approved, the test plan is executed and results are documented:  
    - Select test tools.
    - Select and train team members.
    - Execute the test plan (manual and automated methods).
    - Track test progress.
    - Regression test.
    - Document test results.
    - Resolve problems.

2. Complete a Physical Configuration Audit (PCA) and a Functional Configuration Audit (FCA) to ensure that traceability is complete, that necessary waivers are in place, and that all required documentation has been developed.  
3. Place formal deliverables under configuration control.  
4. After acceptance of delivered products, support transition to an operational and/or maintenance environment.

## 6.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 7. Contract Closeout

The final acquisition step is to close out the contract. The following guidance should be included when establishing the process for contract close-out:

1. Verify satisfaction of all contract terms and conditions, considering the following sample questions:

* + Has the contract period of performance expired (level of effort type contract)?
  + Have all deliverables been delivered (completion type contract)?
  + Have all Contract Data Requirements List (CDRL) items been delivered and accepted?
  + Was the contractor’s performance of the SOW acceptable?
  + If the contract involved patent rights, has the final patent report been filed?
  + Has the final invoice been received?

2. Verify the return of all Government Furnished Equipment (GFE), as appropriate.  
3. Complete final reports as requested by the Contracting Officer.  
4. Provide final contractor performance evaluation to the Contracting Officer.  
5. Capture Lessons Learned, if not captured earlier in the project life cycle.

## 7.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 8. Useful Practices, Activities, and Templates

The documents below are tools collected from various Centers that have been deemed good practices or practices that work well and produce good results. They are included here as aides for carrying out the software acquisition process.

## 8.1 CMMI® Rating Language for Request for Proposal (RFP)

If a project wants to procure the development of Classes A, B or C software, the project must levy the associated requirements for which the project has the responsibility and also clearly specify that the contractor meets CMMI® maturity level requirements associated with the class. Below are examples of wording that could be used in a statement of work to describe the CMMI® maturity level requirements:

**For Class A software:**

The contractor responsible for the acquisition, development, or maintenance of Class A software shall have a non-expired CMMI®-DEV rating, as measured by a CMMI Institute authorized or certified lead appraiser, of CMMI®-DEV Maturity Level 3 rating or higher for software, or CMMI®-DEV Capability Level 3 rating or higher in all CMMI®-DEV Maturity Levels 2 and 3 process areas for software.

**For Class B software, except payload class D missions:**

The contractor responsible for the acquisition, development, or maintenance of Class B software shall have a non-expired CMMI®-DEV rating, as measured by a CMMI authorized or certified lead appraiser, of CMMI®-DEV Maturity Level 2 rating or higher for software or CMMI®-DEV Capability Level 2 rating or higher for software.

**For Class C software:**

The project can minimally choose to pass down this requirement in accordance with the Center's procedures related to Class C, as long as the project provides some action that determines the contractor's capability to develop software in a "meets or exceeds" manner. As many NASA contractors are already at CMMI® Maturity Level 2 or higher, the project may alternatively choose to simply require Maturity Level 2 in the RFP for Class C software.

If a contractor chooses to subcontract the development of Classes A, B, or C software, then the subcontractor(s) is also required to have a CMMI® Maturity Level 2 (for Class B), Maturity Level 3 (for class A), or Center-specified (for Class C) rating.

## 8.1.1  General Example

The contractor and its subcontractors' organizations associated with software development responsibilities shall be at CMMI Software CMMI®-DEV Maturity Level 3 or higher, before the Preliminary Design Review.

## 8.1.2  Examples for RFP Information Technology (IT) Management Section

**Example 1: IT Management**

For IT applications, Class F software, other than mission-specific flight and non-flight software, the contractor shall use commercial off-the-shelf and existing government off-the-shelf products that were cost-effective to NASA. All IT applications, other than mission-specific flight and non-mission flight software, shall comply with NASA requirements as outlined in NPR 7150.2 as applicable for the project, MPR 2800.4, Marshall Operational Readiness Review (MORR) for Center Applications and Web Sites, and NPR 2830.1, NASA Enterprise Architecture (EA) Procedures.

**Example 2: IT Management**

For IT applications, other than mission-specific software, the contractor shall:

* Where cost-effective to NASA, use commercial off-the-shelf and existing government off-the-shelf products.
* Ensure compatibility with existing NASA applications and systems.
* Comply with NASA requirements for NPR 7150.2 for the appropriate software classes.

## 8.1.3  Examples for RFP Software Section

**Example 1: Embedded Software (Firmware)**

The contractor shall develop and maintain the software in accordance with NPR 7150.2 for the appropriate software classes and as applicable for the project and NASA-STD-8739.8 [278](#_tabs-<p>9</p>) , NASA Software Assurance and Software Safety Standard.

**Example 2: Software Engineering**

1. 1. The contractor shall define, design, develop, test, qualify, integrate, verify, validate, deliver, and maintain all software. The plans for accomplishing this work shall be documented in DRD, Software Development Plan.
   2. The contractor shall justify the reuse of existing software, modification of existing software, and the development of new software in DRD, Software Development Plan.
   3. The contractor shall, under project direction, participate in coordinating with the NASA IV&V Facility in accordance with NASA-STD-8739.8 to plan for the participation of the NASA IV&V Facility in the software development life cycle activities.
   4. The contractor and its subcontractors' organizations associated with software development responsibilities shall be at CMMI Software CMMI®-DEV Maturity Level 3 or higher, before the Preliminary Design Review. This requirement does not apply to commercial off-the-shelf software procured for the project.
   5. The contractor shall develop, update, and maintain all software and software development tools under configuration management in accordance with the DRD, Software Configuration Management Plan.
   6. The contractor shall develop and maintain electronic Software Development Folders for all flight, ground, and test software in accordance with DRD, Software Development Folder.
   7. The contractor shall use the following guidance document for the development of all software document deliverables:

* + - Project Classification Matrix (use as guidance in interpreting flight software classification definitions in NPR 7150.2).

h. The contractor shall use the following Standards for designing, developing, and testing all software:

* + - NPR 7150.2.
    - NASA-STD-8739.8

**Example 3:**

The contractor shall define, design, code, test, integrate, and qualify the software. The contractor shall treat the software component of firmware, which consists of computer programs and data loaded into a class of memory that cannot be dynamically modified by the computer during processing, as software for the purposes of this SOW. The scope of this activity applies to the reuse of existing software, modification of existing software, and/or development of new software. The contractor shall provide information and access to products under development to provide the Government with insight into software development and test activities, including monitoring integration and verification adequacy, auditing the software development process, and participation in all software and system reviews. The contractor shall support the implementation of the overall risk management process, as well as program status and progress reviews for the software development process. The contractor shall support software Technical Interchange Meetings and other status meetings, as required, to facilitate Government insight into the software development. The Government insight may include Government civil servant insight, Government support contractor insight, and independent verification and validation review. The contractor shall perform peer reviews on Software Requirements Specifications, Software Test Plans, and on selected design and code items and provide results to the Government via Software Inspection/Peer Review Reports. The contractor shall maintain software metrics and provide Software Metrics Reports in accordance with DRD.

The contractor shall provide the Government web-based electronic access (with access control) to intermediate and final software products (including code) and software process tracking information, including software development and management metrics.

The software development shall comply with NPR 7150.2 as applicable for the project by NASA software classification.

## 8.1.4  Example for RFP EGSE Software Section

**Example 1: EGSE Software**

a. The contractor shall perform the design, code, verification, validation, and delivery of all EGSE code and executables in response to the EGSE Subsystem Requirements Document.

b. The contractor shall develop and maintain the software in accordance with NPR 7150.2 for the appropriate software classes and as applicable for the project and NASA-STD-8739.8. [278](#_tabs-<p>9</p>)

## 8.2 Recommended Technical Review Activities List

Areas to consider for software engineering technical review consist of the following:

* Performing independent assessment of software systems engineering, software processes, software products, software integration, and software test analyses.
* Reviewing all mission-critical software products.
* Performing software schedule and resource assessments and analyses.
* Developing software technical oversight plans.
* Coordinating any software related issues with the project.
* Participating in reviews and Technical Interchange Meetings.
* Performing periodic audits on the pre-defined process(es).
* Serving as chair board, as a board member, or as Review Item Disposition (RID) writer, at a formal review.
* Participating in the resolution and closure of issues.
* Checking and comparing vendor data with independent models.
* Performing evaluations of software products (software documentation, code, etc.)
* Serving as Software Technical Authority responsible for acquired software products.
* Providing planning and project support:

+ Support and coordinate software trade studies.
+ Assess software development processes.
+ Support review of system-level requirements specifications.
+ Support development and review of system-level verification and validation test plans.
+ Verify compliance with the Software Development Plan(s).
+ Verify compliance with Software Quality and Configuration Management Plans.
+ Participate in project documentation reviews.
+ Support risk management activities.
+ Participate in project and software developer review boards, Technical Interchange Meetings, Working Groups, and telecons.
+ Participate in developer's daily and/or weekly software development activities to maintain knowledge of software development progress.
+ Identify and track software metrics.
+ Review and assess the schedule of software development activities.
+ Provide the status of the developer's software progress, metrics, and any problems to the project.
+ Conduct periodic site visits as needed to attain knowledge of software development progress.
+ Review and assess the content and completeness of instrumentation and command control list (engineering integration database).

* Requirements analysis:

+ Verify the absence of problems and risk items associated with requirements:

- Documentation standards used and properly applied.
- System requirements clearly organized.
- Even emphasis and levels of detail.
- Consistent identification schemes.
- Clear or concise requirement statements.
- Good sentence structure.

+ Good word selection, unambiguous terms.
+ Track growth in size and complexity of requirements to identify positive/negative trends.
+ Estimate variances in schedule and costs based on requirements size and completeness.
+ Support software requirements problem and issue resolution.
+ Review and assess the interface specifications and data.
+ Verify software requirements traceability.
+ Support software requirements walkthroughs.
+ Support evaluation of potential requirements changes and associated impacts through the life of the project.

* Design Phase:

+ Support review of preliminary and detailed design specifications (DDS)
+ Support software design problem and issue resolution.
+ Verify traceability of design to software requirements.
+ Support design walk-throughs.

* Code analysis:

+ Track the growth and complexity of source code modules across builds.
+ Rank source code modules according to their relative risk, as determined by:

- Percent of internal documentation.
- Overly large files or modules.
- Use of unstructured programming constructs.
- Complexity.
- Unused or "dead" code.

+ Poor implementation, if applicable.
+ Comply with program coding standards.
+ Develop and maintain knowledge of code functionality.
+ Present code functionality to subsystems for validity.
+ Support code development and integration testing.
+ Support software code problem and issue resolution.
+ Support developer code walk-throughs.

* Test Phase:

+ Support development and review of test plans, test procedures, and test cases.
+ Support the test readiness review (TRR):

- Review and identify discrepancies in software documentation.
- Support final closure of discrepancies.

+ Support software test problem and issue resolution.
+ Support computer software configuration items (CSCI) integration and test activities.
+ Review software test reports.

* Software problem report and effort data analyses:

+ Analyze problem reports and present understandable graphical summaries.
+ Track error detection and correction rates.
+ Assess the adequacy of the test program.
+ Detect schedule risks early.
+ Predict the effective completion date.

* Software metrics:

+ Help the project office identifies applicable software metrics.
+ Review and assess the software metric data provided by the contractor.
+ Develop, maintain, and report software insight metric data to the project.

* Software Independent Verification and Validation (IV&V) support:

+ Perform software criticality assessments.
+ Perform software risk assessments.
+ Develop software IV&V project plans.
+ Develop software IV&V statements of work.
+ Support projects in the review of all software IV&V products.
+ Provide expertise and assistance to the projects in resolution and implementation of any software IV&V recommendations.

See also Topic [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance)

## 8.3 Statement of Work Checklist

Langley Research Center LMS-CP-5523, Rev. B, Statement of Work (SOW) Review Procedures, contains a useful SOW checklist. See the NASA PAL, accessible to NASA users via the SPAN tab in this Handbook for the latest version of this checklist.

## 8.4 Example Templates

The following NASA DID are listed as sample documentation templates that can be called for during the solicitation portion of the software acquisition process. Center PALs are to be consulted for DID and DRD relevant to a specific NASA Center.

## 8.4.1 Software Documentation Requirements

The NASA software engineering documentation recommendations are provided in Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) in this Handbook.  Included are descriptions for:

* Software Development or Management Plan.
* Software Configuration Management Plan.
* Software Test Plan.
* Software Maintenance Plan.
* Software Assurance Plan.
* Software Requirements Specification.
* Software Data Dictionary.
* Software Design Description.
* Interface Design Description
* Software Change Request/Problem Report.
* Software Test Procedures.
* Software User Manual.
* Software Version Description.
* Software Metrics Report.
* Software Test Report.
* Software Peer Review/Inspection Report.

## 8.4.2 Center DIDs and DRDs

NASA-specific acquisition process information, including sample DIDs and DRDs, is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook. Consult your own Center PAL for templates relevant to work performed for your Center.

## 8.5 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-9) in the Resources tab.

# 9. Resources

## 9.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-007) WBS Checklist Tool,
   NASA Goddard Space Flight Center (GSFC), 2007.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-062) Software Supplier Agreement Management Plan (SSAMP) Template,
   NASA Jet Propulsion Laboratory, 2002. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-118)

  [A Method for Reasoning About an Acquisition Strategy,](http://www.sei.cmu.edu/library/abstracts/presentations/method2005.cfm "Click to open in new window")

  Mary Catherine Ward, Joseph P. Elm, Software Engineering Institute (SEI), 2005.  Download the PDF at http://www.sei.cmu.edu/library/abstracts/presentations/method2005.cfm.
* (SWEREF-120)

  [Software Acquisition Best Practices: 2004 Edition,](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=18780 "Click to open in new window")

  Suellen Eslinger (The Aerospace Corporation), Karen L. Owens (The Aerospace Corporation), Mary A. Rich (The Aerospace Corporation),  This 2004 presentation was delivered at the 3rd OSD Conference on the Acquisition of Software Intensive Systems by Richard J. Adams and others of the Aerospace Corporation.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-301)

  [Software Assurance: Five Essential Considerations for Acquisition Officials,](http://www.crosstalkonline.org/storage/issue-archives/2007/200705/200705-0-Issue.pdf "Click to open in new window")

  Polydys, M. L. and Wisseman, S. (May 2007). CrossTalk The Journal of Defense Software Engineering, Vol. 20. No. 5 (14-18).  Retrieved February 29, 2012 from http://www.crosstalkonline.org/storage/issue-archives/2007/200705/200705-0-Issue.pdf.
* (SWEREF-327)

  [Published Appraisal Results (PAR).](https://cmmiinstitute.com/pars/ "Click to open in new window")

  Software Engineering Institute (SEI), architecture web site.

## 9.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 9.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-045 - Project Participation in Audits](/spaces/SWEHBVD/pages/102695419/SWE-045+-+Project+Participation+in+Audits) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)        * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [PAT-024 - Checklist for Choosing Off-The Shelf Software](/spaces/SITE/pages/116293728/PAT-024+-+Checklist+for+Choosing+Off-The+Shelf+Software) |

## 9.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>9</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting)      * [Purchasing](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Purchasing) |

## 9.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 10. Lessons Learned

### 10.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 10.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
