# 7.13 - Transitioning to a Higher Class

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695646. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class

7.13 - Transitioning to a Higher Class

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695646)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695646&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Preparation](#tabs-2)
* [3. Process Overview](#tabs-3)
* [4. Determine Preliminary Transition Risk](#tabs-4)
* [5. Determine Requirements Gap](#tabs-5)
* [6. Determine Transition Strategy](#tabs-6)
* [7. Resources](#tabs-7)

# 1. Purpose

Provide guidance for projects that desire to transition software from a lower to a higher classification.This guidance is provided for Technical Authorities to use in determining:

* If the transition activity is within acceptable risk boundaries, e.g., intended use, resource constraints.
* And, if so, what strategy is needed to complete the transition to the higher classification.

## 1.1 Roles

|  |  |
| --- | --- |
| **Role** | **Responsibility** |
| Technical Authority | Reviews and approves transition strategy, waivers. |
| Software Project Lead | Reviews requirements gap, documents transition strategy, writes waiver requests, carries out a transition strategy. |
| Lead Software Author | Provides documentation, code, other artifacts, and insights into software considered for the transition. |
| Project Manager | Decides budget and schedule resources associated with the transition. |
| Software Assurance | Ensures transition strategy is carried out. |

## 1.2 Transition Categories

* Non-flight to non-flight (Class E -> Class D).
* Non-flight to flight (Class E -> Class C, Class B, or Class A; Class D -> Class C, Class B, or Class A).
* Flight to flight (Class C -> Class B or Class A; Class B -> Class A)

The greatest risk exists for software that crosses the flight boundary and for the software making large transitions, so those projects should be analyzed with the greatest care.

## 1.3 Records

See [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records) for requirements on record keeping related to software classifications.

See also [SWE-021 - Transition to a Higher Class](/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class), topic [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality), [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)

# 2. Preparation

Before transition risk or a strategy can be determined, the Software Project Lead should work with the original author (if available) of the software to obtain the information, e.g., documentation, classification, upon which that determination will be based and make it available to the Technical Authority. Such information includes:

* Original software proposed for the transition.
* Artifacts of original software development.
* Description of a new environment/project where transitioned software will be used.

# 3. Process Overview

This process diagram includes the roles with primary responsibility for carrying out each activity or decision. While the named roles have primary responsibility for the activity, the actual completion of the activity will involve other roles as needed or in compliance with Center standards.

# 4. Determine Preliminary Transition Risk

Before choosing a transition strategy, it is important for the Technical Authority to determine if the transition effort is within acceptable risk boundaries or if new development is a less risky solution. The following questions should be considered when evaluating transition versus new development solutions. Some of these topics are addressed in more detail in later analysis steps.

1. Is this a new project, midstream change of an existing project, or transition of an older, completed project?
2. What was the classification and safety criticality of the software to be transitioned? What are the higher classification and safety criticality?
   1. A larger gap, e.g., non-safety-critical Class E to safety-critical Class B, means a larger number of new requirements to fulfill.
   2. The larger the gap, the more likely that the new requirements will need to be met, as opposed to being tailored or waived.
   3. If the gap is too large, e.g., non-safety-critical Class E to safety-critical Class A, the amount of work to close the gap may simply be too large to consider, and transitioning is not a viable option.
3. Will the software operate in a different environment at the higher classification? If so, is the software appropriate to be used in the new environment? If so, what changes are needed to support this environment (hardware and software interfaces, etc.)?
4. Do software artifacts/documentation exist, and can they be built upon for the transitioned software or must artifacts/documentation be created from scratch?
5. Do personnel have sufficient knowledge and skills related to the prior development to support a transition effort? What additional training is needed?
6. What are the tradeoffs of coding from scratch versus transitioning the existing work?
7. Does this preliminary assessment cause the transition to fall outside the bounds of acceptable risk, which would result in abandonment of the transition?

See also [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)

# 5. Determine Requirements Gap

Once the Technical Authority has deemed that the transition effort is within acceptable risk boundaries, the Software Project Lead has the following primary responsibilities:

* To ensure the project begins to adhere to the requirements for the higher classification and safety criticality, as this will begin to reduce the existing requirements gap.
* To determine the NPR 7150.2 requirements gap between the original software classification and safety criticality and the higher classification and safety criticality.

The requirements gap is input to the transition strategy activity described below.

To determine the requirements gap, use the NPR 7150.2 compliance matrix to determine:

1. Which requirements were met by the software when it was developed.
2. Which requirements must be met for the higher classification and safety criticality.
3. Which requirements that were met in the original software must be met at a more rigorous level at the higher classification.

# 6. Determine Transition Strategy

Once the NPR 7150.2 requirements gap has been determined, a strategy for accomplishing the transition needs to be developed and documented. The Software Project Lead should develop this strategy with input from the Software Assurance organization that will be part of the group responsible for ensuring the transition strategy is carried out. The development of the transition strategy may involve a requirement by requirement review. Additionally, review and approval of the strategy and the associated risk are the responsibilities of the Technical Authority.

During this process, new information may be identified that shows the transition risk is no longer acceptable. In that case, the Technical Authority can determine that transition is no longer within the acceptable risk boundaries and stop the transition attempt.

The questions below should be considered when establishing the transition strategy.

## 6.1 Evaluation of Additional Requirements

1. Which requirements become more significant at the higher classification? Consider:
   1. Safety requirements.
   2. Risk reduction requirements.
   3. Software assurance requirements.
   4. Requirements for reaction to adverse conditions (data, system, environmental, etc.).
   5. Requirements for the required functionality.
   6. Other.
2. Which requirements are candidates to be waived?
   1. What are the tradeoffs of not doing the higher-level requirement(s)?
   2. What are the risks of doing/not doing the higher-level requirement(s)?
   3. What requirements do not make sense to retroactively fulfill or provide little added value, e.g., related to the phase of project development?
3. Which requirements will be tailored?
   1. Which requirements must be retroactively applied, e.g., peer reviews, and which requirements will be applied only to remaining work, e.g., cost estimates?
4. Process-related requirements, e.g., configuration management and planning, should already be met but should be checked to confirm completeness for higher-level classification requirements.
   1. Are there products that need to be placed under configuration management that were not for the lower class?
   2. Is the schedule and cost estimate up to date and detailed enough for the higher-level classification?
   3. What new metrics need to be collected to meet requirements as well as to benefit future transition efforts?
   4. What processes need to be updated to meet the higher classification requirements, e.g., peer reviews, stakeholder reviews, audits?
5. Does this effort cause the transition to fall outside the bounds of acceptable risk?

## 6.2 Documentation Needed

1. What is the state/status of existing documentation?
   1. Review documents as well as existing change requests, inspection/peer review reports, etc., to determine state and quality of documentation.
   2. What new material/content and revisions will be necessary to meet the higher requirements?
   3. To what depth will the new content need to go to meet the higher level requirements?
2. What new documentation will be required to meet all of the higher requirements and to what depth/rigor?
3. Does this effort cause the transition to fall outside the bounds of acceptable risk?

## 6.3 Software Modifications Needed

1. What is the status of the software? Can it be used "as is," or do parts of the software require modification?
   1. Review existing change requests, inspection/peer review reports, test reports, etc., to determine the state and quality of software.
   2. What code (to meet new requirements such as redundancy) or documentation (design, comments, etc.) must be added to fulfill the higher requirements? What is the size of anticipated code modifications versus original code size? Note: If the size of modifications is significantly greater than the size of the original code, the risk could be higher than coding from scratch.
   3. What new standards, e.g., coding standards, must be implemented/met by the code to fulfill the higher requirements?
   4. What non-essential code ("bells and whistles," test hooks, "dead" code, etc.,) should be removed to conform to higher-level requirements?
   5. If not already performed or data is not current, conduct static analysis to identify existing errors in the code, identify missing pieces of the code, generate complexity data, etc.
2. What is the status of the verification and validation (V&V) activities?
   1. Has V&V been performed on the software to be transitioned?
   2. Are existing V&V results invalidated by the new environment or application?
   3. What new or revised/more rigorous V&V activities (analysis, tests, results, documentation, etc.) will be needed to fulfill the higher requirements?
   4. Are there areas of the project that are more safety-critical or higher risk and that will require focused V&V effort at the higher-level classification?
   5. If code modifications are needed, what V&V activities are required for those modifications?
3. Does this effort cause the transition to fall outside the bounds of acceptable risk?

See also Topic [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software).

## 6.4 Resources Needed

1. What resources (people, time, budget, etc.) are available for the transition effort?
   1. Are there tools and/or methods/techniques that could reduce the required effort and still provide the appropriate level of documentation? Some examples are:
      1. Doxygen [456](#_tabs-<p>7</p>) to document the design of the existing code.
      2. Model-based tools to check requirements completeness.
      3. Model-based tools to check design completeness.
   2. In-house personnel or contractors, i.e., are new or renegotiated contracts or internal agreements needed to support the transition effort?
2. What additional resources are needed?
   1. What additional personnel is needed, e.g., software assurance, IV&V, etc.?
   2. What new tools and/or equipment are needed, e.g., for V&V?
   3. Are any new skills needed, e.g., new tools or coding techniques, to meet higher level requirements?
3. Does the resource needs to cause the transition to fall outside the bounds of acceptable risk?

## 6.5 Reference Documentation Table

This table provides guidance on what documentation a project will need to develop for software that will be reused, in whole or in part, from a previous development effort. The documentation to be developed depends on the classification of the project that will be using the software and on decisions made by the project as to which documents are necessary, based on NASA Center procedures.

| **Software Documentation** | **Class A** | **Class B** | **Classes C** | **Class D** | **Class F**  **(In-house)** |
| --- | --- | --- | --- | --- | --- |
| Software Management Plan | 1 | 1 | 1 | 1 | 1 |
| Software Configuration Management Plan | 1 | 1 | 1 | 1 | 1 |
| Software Test Plan | 1 | 1 | 1 | 1 | 1 |
| Software Maintenance Plan | 1 | 1 | 1 |  | 1 |
| Software Assurance Plan | 1 | 1 | 1 |  | 1 |
| Software Safety Plan | 1 | 1 | 1 | 1 | 1 |
| Software Requirements Specification | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 |
| Software Data Dictionary | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 |  | 2, 3, or 4 |
| Software Design Description | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 |
| Interface Design Description | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 |  | 2, 3, or 4 |
| Software Change Request/ Problem Report | 1 | 1 | 1 | 1 | 1 |
| Software Test Procedures | 2 | 2 | 2 |  | 2 |
| Software Users Manual | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 |  | 2, 3, or 4 |
| Software Version Description | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 | 2, 3, or 4 |
| Software Metrics Report | 1 | 1 | 1 |  | 1 |
| Software Test Report | 2 | 2 | 2 |  | 2 |
| Software Inspection/Peer Review Report | 1 | 1 | 1 |  | 1 |

Legend

**Key**:  
1. The project already responsible for developing this document; it needs to address the integration of the transitioning software.  
2. Develop the document if it does not exist.  
3. Modify the project/document to accommodate the transitioning software.  
4. Incorporate existing documents into the project.

**Note: A blank cell indicates that the document does not need to be developed.**

Classes E does not appear in the table since they are the lowest classifications. It is not possible to transition up to either of them. Documents with multiple keys allow for decisions to be made in the best interest of the project. A block with 2, 3 or 4 in it gives the project three options. For instance, a requirements document can be developed as a stand-alone document if it does not exist or the requirements can be included in another of the project's requirements documents or, if the requirements document exists, it can be directly incorporated into the project.

## 6.6 Reference Code Size Decision Chart

Decision making for software transition involves a detailed investigation of the subject code and of the resources available to apply to its modification or rebuilding. The following chart provides some guidance with respect to code size, noting that Modification Size should only reflect modification within the original code, not any code to which the original software will be linked. This table should be tailored even further, depending on the nature of the code's language, local experience with the programming languages involved, and availability of alternate language development resources.

|  |  |  |
| --- | --- | --- |
|  | **Size of Existing Code** |  |
| **Size of Modifications** | Small | Big |
| Small | Determine the size of the original code plus the modifications.   If the determined size is big, then:  Write new code from scratch, following Center procedures and project plans. Exit this process.   If the size is small, then:  1. Analyze and determine risk based on:  • Relative size of original code to mod size.  • Comparison of specialized resources needed/available.  • Reuse: reduced effort, but older language skills/maintenance required.  • Re-code: increased effort, but newer language skills/capabilities available.  • State of the original code: less of these items requires more resources to validate original code and assure to the higher control level.  • Documentation is available.  • Known reliability/applicability/readability.  2. Evaluate the risk.  • If the risk is acceptable, reuse the original code. Perform mods if needed. Follow Center procedures and project plans. Continue with this process.  • If the risk is not acceptable, write new code from scratch, following Center procedures and project plans. Exit this process. | Reuse original code. Perform mods if needed. Follow Center implementations of NPR 7150.2 and project plans. Continue with this process. |
| Big | Write new code from scratch following Center procedures and project plans. Exit this process. | 1. Analyze and determine risk based on:  • Relative size of original code to mod size.  • Comparison of specialized resources needed/available.  • Reuse: reduced effort, but older language skills/maintenance required.  • Re-code: increased effort, but newer language skills/capabilities are available.  • State of the original code.  (If few of these items exist, more resources are required to validate original code and assure to higher classification level.)  • Documentation is available.  • Known reliability/applicability/readability.  2. Evaluate the risk.  • If the risk is acceptable, reuse the original code. Perform mods if needed. Follow Center procedures and project plans. Continue with this process.  • If the risk is not acceptable, write new code from scratch. Exit this process. |

# 7. Resources

## 7.1 Resources

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-456)

  [Doxygen,](http://www.doxygen.nl/ "Click to open in new window")

  Doxygen is the de facto standard tool for generating documentation from annotated C++ sources, but it also supports other popular programming languages such as C, Objective-C, C#, PHP, Java, Python, IDL (Corba, Microsoft, and UNO/OpenOffice flavors), Fortran, VHDL, Tcl, and to some extent D.

## 7.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 7.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-021 - Transition to a Higher Class](/spaces/SWEHBVD/pages/102695406/SWE-021+-+Transition+to+a+Higher+Class) * [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) |

## 7.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>7</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Classification](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Classification) |

## 7.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |
