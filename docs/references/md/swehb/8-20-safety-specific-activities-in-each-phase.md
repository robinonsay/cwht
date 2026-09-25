# 8.20 - Safety Specific Activities in Each Phase

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695762. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase

8.20 - Safety Specific Activities in Each Phase

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695762)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695762&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Safety Specific Activities in Each Phase

This topic provides a summary of the safety-specific activities that should be performed for any safety-critical software. The activities are grouped into the approximate life cycle phases where they will be performed.

## 1.1 All Phases:

* Ensure that software safety is considered throughout the system life cycle, including mission concept, generation of requirements, design, coding, test, maintenance, and operation of the software.
* Develop and maintain a software safety analysis throughout the life cycle.
* Participate in software reviews affecting safety-critical software products.
* Confirm that the identified safety-critical software components and data have implemented the safety-critical software assurance requirements listed in the standard, NASA-STD-8739.8 [278](#_tabs-<p>2</p>).
* Review all safety-related technical issues, risks, and/or assurance findings and ensure that the project is aware of any items needing attention and is addressing them.
* All safety-critical items (e.g. requirements, design, code, test plans, test procedures, hazard reports, data uploads, documentation, etc.) should be kept under configuration management.  Safety personnel need to verify that their safety products are in the configuration management system and they should ensure that they are using the correct versions of the products.

See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), 

## 1.2 Concept Phase:

* The first safety analysis is performed during system concept and beginning requirements phase. A common assessment tool used during this beginning activity is the Preliminary Hazard Analysis (PHA). The results of the PHA are a list of hazard causes and a set of candidate hazard controls, that are taken forward as inputs to the system and software safety requirements flow down process.
* Review the lists of known software-based hazards, hazard contributions and hazard controls to determine whether any of these might be applicable for this project.
* Review the project’s Concept Development and any available Operational Concept information to become aware of any potential security threats and risks that may affect safety. Assure that mitigations are being planned for these.
* Software Safety personnel should develop a good working relationship with any IV&V team on the project to provide more focus any safety-related issues on the project.

## 1.3 Planning:

* Ensure that software safety is addressed in project acquisition, planning, management, and control activities.
* Ensure that the acquisition of software, whether off-the-shelf or contracted, includes evaluation, assessment, and planning for addressing and mitigating risks due to the software’s contribution to safety and any limitations of the software.
* The Engineering Technical Authority and S&MA Technical Authority will jointly determine if the software is designated as “safety-critical”. See criteria in NASA-STD-8739.8A, [278](#_tabs-<p>2</p>) Appendix A.
* Software Safety personnel need to develop a Safety Plan, including safety activities, requirements, effort estimates and schedule. The Safety Plan may be part of the Software Assurance Plan.
  + Additional planning activities may need to be done whenever heritage, reused or COTS software are planned for use, for example:
    - Hazard analysis may need to be done for this software.
    - Additional analysis, testing, and verification may need to be done, depending on the documentation and other information available with the COTS, reused, heritage code.
    - Additional functionality may need to be added; Unused functions may need to be removed.

See Topic  [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) in this Handbook for more information on using COTS.

## 1.4 Requirements:

* Usually, the initial project specific safety requirements are derived from:
  + the identified regulatory and standard safety requirements and
  + the available specific system information and the initial analysis done (probably the PHA)
* Assess that hazard analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD- 8739.8,  [278](#_tabs-<p>2</p>)  Appendix A:
  + Consider functions of software that cause, control mitigate or contribute to hazard.
  + Provides control or mitigation for a system hazardous condition/event,
  + Controls safety-critical functions,
  + Mitigates damage if a hazardous condition/event occurs,
  + Detects, reports, and takes corrective action, if the system reaches a potentially hazardous state.

**Note**:  Software is classified as safety-critical if the software is determined by and traceable to hazard analysis. See appendix A for guidelines associated with addressing software in hazard definitions. See also [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software). Consideration for other independent means of protection (software, hardware, barriers, or administrative) should be a part of the system hazard definition process.

* System hazard controls should be traceable to system requirements.
* If controls identified by the PHA are not in the system specification, safety requirements to control the hazards should be added to that document.
* Assure that the software specification derived from the system specification will include these necessary safety requirements.
* Assure that at least one software requirement is generated for each software hazard control. Each of these requirements is incorporated into the Software Requirements Specification (SRS) as a safety-critical software requirement.
* Assure that the requirements include acceptable mitigations for any safety-related security threats or risks and that any regulatory security requirements that may affect system/software safety are included in the requirements.
* Confirm software (safety) requirements are bi-directionally traced to system hazards.
* Analyze that the software requirements documentation contains the software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and the software.
* Analyze the software requirements and the software design and work with the project to implement NPR 7150.2, [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)  requirement items "a" through "l."

**SWE-134 - Safety-Critical Software Design Requirements**

3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:

a. The software is initialized, at first start and restarts, to a known safe state.  
b. The software safely transitions between all predefined known states.  
c. Termination performed by software functions is performed to a known safe state.  
d. Operator overrides of software functions require at least two independent actions by an operator.  
e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard.  
f. The software detects inadvertent memory modification and recovers to a known safe state.  
g. The software performs integrity checks on inputs and outputs to/from the software system.  
h. The software performs prerequisite checks prior to the execution of safety-critical software commands.  
i. No single software event or action is allowed to initiate an identified hazard.  
j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event.  
k. The software provides error handling.  
l. The software can place the system into a safe state.

* Perform (or review) the requirements analysis portion of the safety analysis and assure that any findings or issues are closed out.
* Review the interface documentation for consistency and completeness and identify any potential vulnerabilities that may affect system/software safety. Consider interfaces with other software components, with hardware, or with human operators. Interface characteristics to be addressed should include inter-process communication methods, data encoding, error checking, synchronization, fault management, cybersecurity considerations, input validation, and issues with hardware startup (initialization).

## 1.5 Architectural Design/Design:

* Identify software safety design features and methods in design documents.
* Confirm the following activities are occurring during design:
  + Maintainability and reliability are being considered in the design. See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality).
  + Ensure software peer reviews include peer reviews for all safety-critical portions of the system and that any errors found are being addressed.
  + Safety-critical code has been analyzed using static code analysis, code logic analysis, code data analysis, code interface analysis, interrupt analysis and unused code analysis.
* Analyze the software architecture to assess whether software safety and mission assurance requirements are met.
* Analyze the software design to ensure:
  + Use of partitioning or isolation methods in the design and code,
  + That the design logically isolates the safety-critical design elements and data from those that are non-safety-critical.
* Ensure that design changes, changes to the requirements, or operational use of the software during design are analyzed for their impacts on system safety.
* Confirm that the software design implements all the required safety-critical functions and requirements.
* Perform a software safety design analysis.
  + The design analysis portion of software safety analysis should be completed by Phase 2 safety reviews.
  + At this point, the software safety analysis supports a requirements gap analysis to identify any gaps and to ensure the risk and control strategies documented in hazard reports are correct as stated.
  + Evaluate the design for the correct balance of fault tolerance and failure tolerance.

**Note**:  Fault tolerant systems are built to handle most probable, and some less probable but hazardous, faults. Taking care of the faults will usually help prevent the software, or the system, from going into failure.  The down-side to fault tolerance is that it requires multiple checks and monitoring at very low levels.  If a system is failure tolerant, it will ignore most faults and only respond to higher-level failures. A presumption is that it requires less work and is simpler to detect, isolate, stop, or recover from the failures. A project must weigh the costs and benefits of each approach and determine what will provide the most safety for the least cost and effort.

* Evaluate the design to ensure that the software design for a failure will not defeat the hardware failure tolerance and vice versa. Review the design for any safety-related features or portions of the code, checking to see that the transformation into code is complete and will support the safety needs of the project during all the expected operational scenarios as well as during any non-nominal
* Review the design for any unintended features that might impact the safety of the system.
* Once the design is fairly detailed, a Software Failure Modes and Effects Analysis (SFMEA) can be performed. It looks at how each component could fail, how the failure propagates through the system, and whether it can lead to a hazard. The use of the SFMEA in conjunction with a software Fault Tree Analysis is quite useful in identifying all possible failure modes or areas of concern. However, it can be quite time-consuming and expensive, so often only one of these methods is used. For the SFMEA, the basic procedure is below: (For more details, see Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis))

**SFMEA Basic Procedure**

1. Define the system to be analyzed.
2. Construct functional block diagrams.
3. Identify all potential item and interface failure modes.
4. Evaluate each failure mode in terms of the worst potential consequences.
5. Identify failure detection methods and compensating provisions.
6. Identify corrective design or other actions to eliminate / control failure.
7. Identify impacts of the corrective change.
8. Document the analysis and summarize the problems which could not be corrected.

* As the design progresses, ensure that any new safety features or capabilities identified are added to the requirements.

See also Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

## 1.6 Implementation:

* Evaluate operating systems for features supporting safety before choosing one for the project.
* Choose a "safe" programming language; one that enforces good programming practices finds errors at compile-time, has strict data types, bounds checking on arrays, discourages the use of pointers, etc.
* Use a coding standard that includes safety considerations and enforces “secure coding” practices.
* Review the static code analysis results to ensure that all safety-related problems and cybersecurity weaknesses are identified and addressed.
  + Ensure that the static code analyzer(s)(SCAs) chosen are configured to support the programming languages and coding standards being used, as well as good coding practices for safety-critical software.
  + SCA tools should use a secure coding standard and at a minimum, check for the following:
    - Memory leaks
    - Dead or unreachable code
    - Declared variables that are never used
    - External software (Identify any that have reported problems)
    - Code quality
    - Variables declared but not initialized
  + The use of more than one static code analyzer is recommended since different analyzers often have strengths in different areas.
  + SCA tools should be run at least on the software changes and definitely on baselined versions of the software.
  + SCA tools typically produce many “false positives”, but even those should be noted for possible reassessment as the software changes.
* Assess that the source code satisfies the conditions in the NPR 7150.2, [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), requirements "a" through "l", for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone.
* Confirm that all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. If not, assure that software developers provide a risk assessment explaining why the cyclomatic complexity value needs to be higher than 15 and why the software component cannot be structured to be lower than 15.
* Ensure that changes and reconfigurations of the software, during development, testing, and operational use of the software, are analyzed for their impacts on system safety.
* Participate in reviews involving safety-critical software, particularly peer reviews, to see that the design is correctly, accurately, and completely transformed into code with no unintended features.
* Review implementations of hazard mitigations, controls, constraints, etc., and/or analyze interfaces for potential safety or security risks.
* Between Phase 2 and 3 safety reviews, the system hazard analysis and software safety analysis support the analysis of test plans to assure the testing is sufficient to show the requirements are met and include adequate testing of safety features and off-nominal scenarios.

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

## 1.7 Testing:

* Develop safety tests for safety-critical software units that cannot be fully tested once the units are integrated.
* Ensure that software verification and validation activities include software safety verifications and validations. Ensure the safety verifications included in the hazard reports are adequate to verify the safety features being tested will mitigate the hazards.
* Use stress testing, stability testing, resistance to failure tests, disaster testing.
* Look specifically for unexpected interactions among units during integration testing. Be sure these are documented and addressed!
* Confirm regression testing is adequate and includes retesting of all safety-critical software code components.
* Confirm regression test procedures are updated to incorporate tests that validate the correction of critical anomalies.
* Confirm 100% code test coverage is addressed for all identified software safety-critical software components or assure that software developers provide a risk assessment explaining why the test coverage is not possible for the safety-critical code component.
* Confirm that the values of the safety-critical loaded data, uplinked data, rules, and scripts that affect hazardous system behavior have been tested.
* Ensure that changes and reconfigurations of the software, during development, testing, and operational use of the software, are analyzed for their impacts on system safety.
* Perform test witnessing for safety-critical software.
* Ensure that any newly identified software contributions to hazards, events, or conditions found during testing are included the system safety data package, and that they get properly documented in the requirements, properly implemented and adequately tested.
* The system hazards analysis must verify the final implementation and verification by ensuring test results permit closure of hazard verifications.
* Confirm that the final hazardous commands support the single command and multi-step command needs and finalized pre-requisite checks, sequencing and unique operator actions are in place.

See also [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage), 

## 1.8 Acceptance/Delivery:

* Confirm that the project has identified all the requirements, approved changes to be implemented, and defects to be resolved for each delivery, particularly any relating to safety.
* Confirm that the project has met all software requirements identified for the delivery.
* Confirm that approved changes have been implemented and successfully tested.
* Confirm that the correct version of the products is provided, including as-built documentation and project records.
* Confirm that all the correct safety-related products are being delivered.
* Ensure that the proper certification requirements are in place and accomplished prior to the actual operational use of the software.

## 1.9 Operations and Maintenance:

* Ensure that changes and reconfigurations of the software, during development, testing, and operational use of the software, are analyzed for their impacts on system safety.
* Monitor the handling of operational inputs, such as command data, and data loads to ensure unauthorized access and validate the accuracy of the data before uploading.
* Analyze actual operational scenarios and activities: identify any new or previously unrecognized hazards and develop mitigations for them.
* Document newly discovered or previously unrecognized hazards and their mitigations and verifications in a Safety Report.
* Where errors or operational issues during operations are discovered, submit problem reports to the maintenance team and work to develop safe workarounds for the problems until fixes can be included in a maintenance release.
* Confirm regression testing of work-around fixes or maintenance releases include retesting of all safety-critical software code components.

## 1.10 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)       * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
