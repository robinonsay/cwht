# 7.19 - Software Risk Management Checklists

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695678. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists

7.19 - Software Risk Management Checklists

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695678)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695678&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Software Planning Phase](#tabs-2)
* [3. Software Requirements Phase](#tabs-3)
* [4. Software Design Phase](#tabs-4)
* [5. Software Implementation Phase](#tabs-5)
* [6. Software Test Phase](#tabs-6)
* [7. Software Release Phase](#tabs-7)
* [8. Operations and Maintenance](#tabs-8)
* [9. Plan Compliance](#tabs-9)
* [10. Other Software Risks](#tabs-10)
* [11. Resources](#tabs-11)

# 1. Introduction

Software Risk Management is a process whereby the project identifies and tracks threats to the success of the project. This process provides for mitigation strategies for potential problems and for early intervention with realized problems, lessening their impact to the project.

This guidance provides a set of risk checklists for each phase of the software life cycle.  Each checklist provides a set of potential risk items or areas for software development projects to consider as they plan their risk management activities.  Not all items will be applicable to every project, but these checklists provide starter material for projects to use as the basis for planning risk management specific to their software project.

## 1.1 Other Topics And Requirements Dealing With Risks

* [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) - Risks are an output of the Surveillance process.
* [8.24 - Software Assurance Risk](/spaces/SWEHBVD/pages/150077537/8.24+-+Software+Assurance+Risk) - This chart summarizes SA Risks by Risk Phases
* [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)

# 2. Software Planning Phase

1. Do the customer & implementer (system and software) agree on what is to be built? ([SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation))
2. Has the software been evaluated and assigned a class per class definitions in NPR 7150.2? ([SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification))
3. Is the software assurance organization in agreement with the assigned classification? ([SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification))
4. Has the planning, programming, budgeting, and execution (PPBE) and basis of estimate (BOE) been prepared and approved? ( [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation))
5. Are all requirements known and understood? ( [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis))
6. Are roles and responsibilities for all project activities clearly defined, followed, and sufficient? ( [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans))
7. Has all needed equipment, including spares, been identified? ( [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans))
8. Is there sufficient lead time to get the necessary equipment? ( [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule))
9. Is there a contingency plan for not getting all the necessary equipment? ( [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans))
10. Is the necessary level of technical expertise known and planned for? ( [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training))
11. Is the appropriate level of expertise available within NASA and contractors? ([SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training))
12. Will expertise be available as the schedule demands? ([SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule))
13. Is there more than one person with particular expertise/knowledge? ([SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans))
14. Are there adequate trained personnel on the project? ([SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training))
15. Is there enough time to train all personnel on the project? ([SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule))
16. Is the software project lead experienced at managing this size and/or type of team? ([SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training))
17. Is the software project lead familiar with the technology being used (e.g., OOA/OOD and C++)? ([SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training))
18. Is the budget sufficient for needed equipment? ( [SWE-174 - Software Planning Parameters](/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters))
19. Is the budget sufficient for needed resources and activities? ( [SWE-174 - Software Planning Parameters](/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters))
20. Are the training needs identified? ( [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training))
21. Is the budget sufficient for travel?
22. Is funding likely to change from the original project amount?
23. Is there a plan in place to handle possible funding changes?
24. Is the schedule reasonable considering needed personnel, training, and equipment?
25. Does the system level schedule accommodate the software life cycle?
26. Is there sufficient time in the schedule to address design and/or requirements changes?
27. Has the schedule been defined in enough detail to meet the needs of software development or is it just a time/date when systems will need the software?
28. Is there a schedule for the development of ground and flight systems?
29. Is the software schedule reasonable, does it match reality, and is it being followed?
30. Does the schedule allow adequate time for tests (including verification of all requirements, validation, regression test, and fixes) and delivery activities?
31. Are changes to the schedule being tracked?
32. Are changes to the schedule made by due process, in a planned manner, or are events changing the schedule with no decision regarding whether there is something wrong in the process or program?
33. Are schedules being maintained?
34. Have impacts been accounted for (technical, resources, cost, etc.)?
35. Are peer reviews and major milestone review activities adequately addressed on the schedule?
36. Has all the slack/contingency time on the critical path been expended?
37. Will new development techniques be used?
38. Will a new or different development environment be used?
39. Are deviations to the development plan being tracked/trended?
40. Are the trends reported in a manner to allow timely and appropriate software and project management decisions?
41. Will simulators need to be designed and built?
42. Are time and resources allocated for the development, verification, and execution of simulators?
43. Will this be a distributed development (different groups or individuals working on parts of the project in different locations, e.g., out of state)?
44. Are there proper facilities and management structures to support distributed environment development?
45. Are interfaces with other developers, suppliers, users, management, and the customer understood and documented?
46. Is there a known way to resolve differences between these groups (i.e., conflict resolution; who has ultimate authority, and who is willing to make a decision)?
47. Is there a well-constructed, up-to-date software development plan (SDP) that outlines procedures, deliverables, risk, life cycle, budget, etc.?
48. Is there a plan for tracking changes and are the reasons for the changes well understood?
49. Does the software life cycle approach & time-frame meet the needs of the overall project, and does it have a chance of being close to what is needed?
50. Is software measurement data collected and reported regularly?
51. Are risks collected, discussed and reported regularly?
52. Is there a need for incremental delivery?  If so, does the schedule reflect the planned deliveries?
53. Has the software been assessed to determine safety criticality?
54. Is firmware and/or any other software developed outside of the software development organization?
55. Does work contracted out have sufficient controls and detail to assure quality, meeting the schedule, and meeting the requirements?
56. Are all planning documents complete, communicated, approved, and baselined?
57. Has time been allocated for safety, reliability, and quality assurance (QA) assessments?
58. Has software assurance had input on all standards, procedures, guidelines, and processes?

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 3. Software Requirements Phase

1. Is the requirement process adequately defined in the software development plan (SDP)?
2. Are the tasks and resources for the Requirements Phase identified in the project schedule?
3. Is the adequacy of the process and resources being evaluated and reported on a regular basis?
4. Have the relevant stakeholders been identified in planning for the requirements phase?
5. Are the risks identified and managed for the Requirements Phase?
6. Are there any metrics associated with this process area?
7. Has the project documented the software requirements?
8. Is the project identifying, developing, approving, and maintaining software requirements based on analysis of customer and other relevant stakeholder requirements and the operational concepts?
9. Is software assurance working with developers to incorporate safety, reliability and quality assurance requirements?
10. Is the project performing software requirements analysis based on flowed down and derived requirements from the top-­level systems engineering requirements and the hardware specifications and design?  
    Note: This analysis is for safety criticality, correctness, consistency, clarity, completeness, traceability, feasibility, verifiability, and maintainability. This includes the allocation of functional and performance requirements to functions and sub-functions.
11. Is the project performing, documenting, and maintaining bidirectional traceability between the software requirements and the higher level requirements?
12. Is the project collecting and managing changes to the software requirements? Is there a project-wide method for dealing with future requirements changes?  Is an impact analysis conducted for all changes to baseline requirements?  
    Note: The project should analyze and document changes to requirements for cost, technical, and schedule impacts.
13. Is the project identifying inconsistency between requirements, project plans, and software products and initiating corrective actions as required?
14. Is the project performing requirements validation to ensure that the software will perform as planned in the intended environment?
15. Has the project held, or does the project have, a formal peer review scheduled for the software requirements specification (SRS)?
16. Are the required work products being properly managed and controlled?
17. Are the requirements team meetings being regularly held? Are attendance sheets and minutes being taken? Is stakeholder participation being monitored?
18. Is the requirements team following the defined process in the SDP?  
    Are deviations to the SDP being tracked? Are trends reported in a manner to allow timely and appropriate software and project management decisions?
19. Have risks for those requirements that have cost/schedule/technical impacts been created, reported, and tracked?
20. Are the requirements process and products being regularly audited by software assurance? Have all the findings been resolved?
21. Has the essential training and skills required for requirements development and management been defined and included in the SDP?
22. Does this checklist adequately evaluate the phase? If not, how can it be improved?

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 4. Software Design Phase

1. Is the software development plan (SDP) being followed for design activities?
2. Is the allocation of requirements to design elements well understood and documented?
3. Are applicable design-related templates (e.g. DRDs) being used to produce clear/consistent design?
4. Will there be or has there been a major loss of critical personnel?
5. Is communication between systems and software engineering groups working well in both directions?
6. Is there sufficient communication between those creating and maintaining requirements and those designing to them?
7. Has a requirements baseline been established?
8. Are the requirements being managed?
9. Has bi-directional traceability been established between requirements and design?
10. Do personnel have a good understanding of how to use/integrate COTS into the final product? If COTS meets only a subset of requirements, has the integration task and time been correctly estimated? Can it be estimated? Will custom software need to be written to either get different COTS to interact or to interact with the rest of the system as built or planned?
11. Is there a mitigation plan for addressing software safety and risk issues?
12. Are there Fault Detection, Isolation and Recovery (FDIR) techniques designed for critical software functions?
13. Has software reliability been addressed in the software design?
14. Has fault tolerance been addressed in software design?
15. Are simulators verified for accuracy, completeness, and consistency?
16. Are internal/external design interfaces defined in enough detail to establish & verify functionality?
17. Are inspections and/or peer reviews scheduled and taking place?
18. Is there a Software Configuration Management Plan in place and working?
19. Are software metrics kept and reported regularly?
20. Are deviations to the development plan being tracked? Are trends reported in a manner to allow timely and appropriate software and project management decisions?
21. Is the Design Team working with SA to ensure the implementation of safety-critical requirements?
22. Are design documents approved/baselined?

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations),

## 4.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 5. Software Implementation Phase

1. Are we following the software development plan (SDP) for the implementation activities?
2. Did the implementation follow the SDP and NPR?
3. Are the tools called out in the SDP the only ones being used for coding? If not, has the SDP been updated or a dev/waiver generated?
4. Was there any reuse code?
5. Was the reused code modified?
6. Is there an auto-generated code? Is unit testing planned for auto-generated code?   Are there procedures for testing unit level auto-generated code?
7. Are metrics being collected to demonstrate reuse?
8. Is the code consistent with performance requirements?
9. Does the code match the detailed design? (The problem may be in either the code or the design.)
10. Were the coding standards followed?
11. Does the code completely and correctly implement the design?
12. Are there any uncalled or unneeded procedures or any unreachable code?
13. Are there any leftover stubs or test routines in the code?
14. Can any code be replaced by calls to external reusable components or library functions?
15. Are there any blocks of repeated code that could be condensed into a single procedure?
16. Is storage use efficient?
17. Are all comments consistent with the code?
18. Do all assigned variables have a proper type of consistency or casting?
19. Does the code avoid comparing floating-point numbers for equality?
20. Does the code systematically prevent rounding errors?
21. Does the code avoid additions and subtractions on numbers with greatly different magnitudes?
22. Are divisors tested for zero or noise?
23. Are all loops, branches, and logic constructs complete, correct, and properly nested?
24. Are loop termination conditions obvious and invariably achievable?
25. Are indexes or subscripts properly initialized, just prior to the loop?
26. Can any statements that are enclosed within loops be placed outside the loops?
27. Does the code in the loop avoid manipulating the index variable or using it upon exit from the loop?
28. Are indexes, pointers, and subscripts tested against the array, record, or file bounds?
29. Are imported data and input arguments tested for validity and completeness?
30. Is every memory allocation deallocated?
31. Are timeouts or error traps used for external device accesses?
32. Are files checked for existence before attempting to access them?
33. Are all files and devices left in the correct state upon program termination?
34. Are Software Development Folders (SDFs) being used to capture design and implementation ideas as well as unit test procedures & results?
35. Is the schedule being maintained and schedule impacts being accounted for?
36. Have other impacts been accounted for (technical, resources, etc.)?
37. Are deviations to the development plan being tracked/trended?
38. Are the trends reported in a manner to allow timely and appropriate software and project management decisions?
39. Have any coding requirements for safety-critical code been established?
40. Does the chosen development environment meet flight standards/needs?
41. Has system safety assessed software (subsystem safety analysis)?
42. Has software reviewed this safety assessment?
43. Has software had input to this safety assessment?
44. Do software personnel know how to address safety-critical functions?
45. Is the software working with systems to find the best solution to any hazards?
46. Has FDIR (Fault Detection, Isolation, and Recovery) and/or fault tolerance been implemented as required?
47. Is there a process for managing requirements and design changes and is it understood and used?
48. Do requirements and design changes take into account parent documents?
49. Do the requirements and design changes take into account subsequent changes to child documents?
50. Are the design documents baselined?
51. Are the requirements baselined?
52. Has a code walk-thru been held? (For new and reuse code?)
53. Are all actions taken in walk-thru dispositioned and closed?
54. Were the appropriate software change requests (SCRs) written and dispositioned?
55. Is the software assurance auditing development process and SDFs?

See also Topic [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis),

## 5.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 6. Software Test Phase

1. Is the Software Test Plan complete and approved at the appropriate level?
2. Are the Software Test Procedures (STPr) complete and approved at the appropriate level?
3. Are adequate resources available to complete informal and formal test activities?
4. Is the test environment identified and ready for informal and formal test activities?
5. Have the test criteria for informal and formal testing been identified and documented?
6. Has product integration and integration testing completed successfully?
7. Are work products identified for testing ready to enter the test phase? If so, have the work products been tagged within the development configuration management tool (e.g., Subversion) prior to entering the informal test phase?
8. Has the release software been tagged within the development configuration management tool (e.g., Subversion) prior to the Functional Configuration Audit (FCA)/Physical Configuration Audit (PCA)?
9. Has an FCA and PCA been performed on the release package prior to entering the formal test phase?
10. Has a software review board (SRB) baseline been established for target code and the test configuration identified and documented in preparation for formal test activities?
11. Has the test readiness review (TRR) been planned and scheduled prior to formal testing to include appropriate stakeholders?
12. Has an FCA and PCA been performed on the final release prior to scheduling the SRB?
13. Have FCA and PCA issues been resolved or workaround identified?
14. Has the SRB been scheduled to baseline the release package?
15. Is there a problem identification and resolution process in place? Is there a known recourse/procedure for testing procedure changes? Is it being followed?
16. Has software testing been performed as defined in the Software Development Plan (SDP), Software Test Plan, and STPr?
17. Have test results been analyzed and documented?
18. Have test defects during the informal test phase been identified, documented, and tracked to a closure via Type II software change request (SCR)?
19. Have test defects during the formal test phase been identified, documented, and tracked to a closure via Type I SCR?
20. Have the appropriate metrics been captured (as defined in the SDP) for the test activities?
21. Has bidirectional traceability been established throughout the life cycle?
22. Have peer reviews been performed on test items that the project identified for peer review in accordance with the SDP?
23. Are the SCRs incorporated as required?
24. Has the software been verified against the approved requirements?
25. Has the software been validated using a target-­?like platform or high-­?fidelity simulation?
26. Are the software specifications internally consistent?
27. Have all system-level safety and security requirements been properly implemented?
28. Are all interfaces (internal and external) identified in the interface design specification adequately tested?
29. Has testing of COTS at the software system-level been adequately covered and documented?
30. Have test phase risks been identified, documented, communicated to management, and mitigated, as appropriate?

## 6.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 7. Software Release Phase

1. Has the pre-ship review already taken place?
2. Is software assurance involved with release and acceptance activities?
3. Are all parts of the architecture verified and validated on the ground prior to flight?
4. Is the software version description document (VDD) complete and approved?
5. Are all delivered software release versions listed in VDD?
6. Are all hardware versions appropriate for this release noted in VDD?
7. Are software change management (SCM) release descriptions and build, burn, and installation procedures in VDD?
8. Is the list of all incorporated (closed) and outstanding software change requests (SCRs) in VDD?
9. Is the list of any known discrepancies (software, hardware, documents, etc.) and associated workarounds in VDD?
10. Is the list of changes since the last formal release in VDD?
11. Is a list of all documentation that applies to this release in VDD?
12. Has a clean customer handoff been planned and executed to include: up to date documentation and user/operations manual, as applicable?
13. Has a good configuration management wrap-up been planned and executed to include: a method for future updates/changes; proper off-site storage of data, software, and documentation; what happens to SCM and data when the project is over?
14. Are the release and acceptance activities being conducted in accordance with the software development plan (SDP)?

## 7.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 8. Software Operations and Maintenance

1. Are operations and maintenance (O&M) tasks and resources identified in the project schedule?
2. Does the schedule and resources for O&M satisfy the task plan?
3. Are the necessary Safety & Mission Assurance (SM&A) resources available (software quality, reliability, safety)?
4. Are risks identified and managed for the O&M phase?
5. Are the necessary O&M facilities available?
6. Are the necessary O&M tools available?
7. Are the necessary O&M SCRs identified for each O&M release?
8. Is the resolution of the software change requests (SCRs) agreeable with the customer?
9. Is software safety involved with the SCRs related to safety-­?critical functionality?
10. If required, are O&M metrics being collected, analyzed and reported?
11. Has all the appropriate documentation been reviewed and updated (software development plan (SDP), software change management plan (SCMP), software test plan (STP), software requirements specification (SRS), software design description (SDD), software user manual (SUM), software test procedures (STPr)?
12. Has an O&M Plan been developed?
13. Has the appropriate documentation to support the operations and maintenance phase of the life cycle been provided to the customer upon delivery? Documentation that should be considered for delivery consist of the following items:  
    * Status of accepted change requests to the baselined SRSs.
    * Status of major software capability changes since the baselining of SDDs.
    * Status of major software tests (including development, verification, and performance testing).
    * Status of discrepancy reports written against the software.
    * Status of software requirements deviations and waivers.
    * Status of software user notes.
    * Status of quality measures historically and for this software.
    * Definition of openwork, if any.
    * Software configuration records defining the verified and validated software, including requirements verification data (e.g., requirements verification matrix).
    * Final as-­built version of software documentation, including final software version description documents (VDDs).
    * Status of any open software-­?related risks.
14. Does this checklist adequately evaluate the phase? If not, how can it be improved?

## 8.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 9. Plan Compliance

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-050 - Risk Management Plan Assessment**

## 9.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 10. Other Software Risks

**Customer-related risks**

1. Is this a first time experience with this project manager or system engineer?
2. Does the customer have a solid idea of what is required?
3. Has the customer taken the time to write this down?
4. Will the customer agree to spend time in formal requirements gathering meetings to identify project scope?
5. Is the customer willing to established communication links with the development team?
6. Is the customer willing to participate in reviews?
7. Is the customer technically sophisticated in the product area?
8. Is the customer willing to let people do their job; that is, will the customer resist looking over the developer’s shoulder during technically detailed work?
9. Does the customer understand the software engineering process?

**Development environment risks**

1. Are tools for analysis and design available?
2. Do analysis and design tools deliver methods that are appropriate for the product to be built?
3. Are compilers or code generators available and appropriate for the product to be built?
4. Are testing tools available and appropriate for the product to be built?
5. Are software configuration management tools available?
6. Does the environment make use of a database or repository?
7. Are all the software tools integrated with one another?
8. Have members of the project teams received training in each of the tools?
9. Are local experts available to answer questions about the tools?
10. Is online help and documentation for the tools adequate?

**Process issue risks**

1. Does senior management support a written policy statement that emphasizes the importance of a standard process for software development?
2. Has the development organization developed a written description of the software process to be used on this project?
3. Are staff members signed-up to the software process as it is documented and willing to use it?
4. Is the software process used for other projects?
5. Has the development organization developed or acquired a series of software engineering training courses for managers and technical staff?
6. Are published software engineering standards provided for every software developer and software manager?
7. Have document outlines and examples been developed for all deliverables defined as part of the software process?
8. Are formal technical reviews of the requirements specification, design, and code conducted regularly?
9. Are formal technical reviews of test procedures and test cases conducted regularly?
10. Are the results of each formal technical review documented, including defects found and resources used?
11. Is there some mechanism for ensuring that work conducted on a project conforms to software engineering standards?
12. Is configuration management used to maintain consistency among system/software requirements, design, code, and test cases?
13. Is a mechanism used for controlling changes to customer requirements that impact the software?
14. Is there a documented statement of work, software requirements specification, and software development plan for each subcontract?
15. Is a procedure followed for tracking and reviewing the performance of subcontractors?

**Staff size and experience**

1. Are the best people available?
2. Do people have the right combination of skills?
3. Are enough people available?
4. Are staff committed for the entire duration of the project?
5. Will some staff be working only part-time on this project?
6. Do staff has the right expectations about the job at hand?
7. Have staff received the necessary training?

**Technology risks**

1. Is the technology to be built new to the development organization?
2. Do the customer requirements demand the creation of new algorithms, input or output technology?
3. Does the software interface with new or unproven hardware?
4. Does the software to be built interface with a database system whose function and performance have not been proven in this application area?
5. Does the software to be built an interface with vendor-supplied software products that are unproven?
6. Is a specialized user interface demanded by-product requirements?
7. Do requirements for the product demand the creation of program components that are unlike any previously developed by the developing organization?
8. Do requirements demand the use of new analysis, design, or testing methods?
9. Do requirements demand the use of unconventional software development methods, such as formal methods, AI-based approaches, artificial, or neural networks?
10. Do requirements put excessive performance constraints on the product?
11. Is the customer uncertain that the functionality requested is "do-able"?

## 10.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 11. Resources

## 11.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-009)

  [Agency Risk Management Procedural Requirements,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8000&s=4B "Click to open in new window")

  NPR 8000.4C, NASA Office of Safety and Mission Assurance, 2022. Effective Date: April 19, 2022 Expiration Date: April 19, 2027
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.

## 11.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 11.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-174 - Software Planning Parameters](/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters)        * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.24 - Software Assurance Risk](/spaces/SWEHBVD/pages/150077537/8.24+-+Software+Assurance+Risk) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 11.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>11</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Risk Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Risk+Management) |

## 11.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) * [A.09 Software Risk Management](/spaces/SWEHBVD/pages/133235385/A.09+Software+Risk+Management) |
