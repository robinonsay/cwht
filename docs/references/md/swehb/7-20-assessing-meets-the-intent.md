# 7.20 - Assessing - Meets the Intent

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695679. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695679/7.20+-+Assessing+-+Meets+the+Intent

7.20 - Assessing - Meets the Intent

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695679/7.20+-+Assessing+-+Meets+the+Intent#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695679)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695679&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Provider approaches to alternate standards](#tabs-2)
* [3. Assessment approach: Focus on key life cycle activities](#tabs-3)
* [4. Assessment approach: Functional requirement grouping review](#tabs-4)
* [5. Assessment approach: Requirement level review](#tabs-5)
* [6. Resources](#tabs-6)

# 1. Purpose

Guidance for projects that need to assess whether an industry partner or subcontractor’s standards meet the intent of NASA requirements. The phrase “meets the intent” could be defined as “controls, reduces, or mitigates the same risks” as intended by the NASA standard or practice.  In general, as the consequence of design or implementation errors increase, so does the rigor in the software development practices. The following illustration captures the everyday process of software development and the multiple ways that defects can be inserted into the software product

Controlling, reducing, or mitigating the same risks (“meeting the intent”) entails 1) reducing the introduction of any of these defect paths, and 2) detecting these defects as soon as possible. The allowable probability of these defect paths and the rigor of the required standards and practices is driven by the acceptable consequence of the mission. To “meet the intent” is to map each risk to a risk matrix, and the probability and consequence of each risk, as shown in the risk matrix, is identical to using the NASA standards and practices.

This document describes processes used on the Commercial Crew Program (CCP) to assess whether commercial partner alternate standards met the intent of the NASA standards for which they were proposed alternates. This document describes:

* Provider approaches to alternate standards.
* Sample assessment approaches.

# 2. Provider approaches to alternate standards

As experienced in the CCP, providers may take different approaches to provide alternates to NASA standards. Each approach has its challenges for NASA’s assessment of whether the approach truly meets the intent of NASA standards. Additionally, a provider may choose to combine methods or may choose to present a variance to the standard. If the variance is approved, it can waive or modify how the provider is required to meet the intent of the applicable standard(s).

* Providers may write their own standard and submit it to NASA as an equivalent, e.g., a software standard for NPR 7150.2, a model & simulation standard for NASA-STD-7009. Assessing this type of standard against a NASA standard is straightforward, but the challenge is knowing early in the project life cycle, before project plans and other work products are delivered, if the provider truly follows this proposed standard in practice. If the alternate standard is approved by NASA, but the provider does not truly follow it, then issues will be discovered later in the life cycle when the impact is greater.
* Providers may deliver a package of project documentation in lieu of a true alternate standard, e.g., software development plans, configuration management plans, risk management plans, software quality plans. Assessing this type of alternate standard package requires more work on the part of NASA to find and evaluate the elements in the plans that show that the provider meets the intent of the NASA standard. The advantage of this approach is that a clearer picture is shown upfront of the provider’s adherence to their submitted “alternate standard” because the assessment is performed on actual work products and project plans.
* Providers may also submit industry standards as their equivalent or alternate to NASA standards. This was not one of the options seen by the CCP, at least for software engineering, software safety, and software assurance, but it is an option a provider could choose. The challenges with this approach are similar to those when a provider writes their own alternate standard as described above.

See also Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009).

# 3. Assessment approach: Focus on key life cycle activities

When assessing provider alternate standards, some key areas to assess, along with recommended practices for which equivalents should exist in the alternate standard or expected considerations for the activity include:

* Requirements Validation.  
  + *Modeling and simulation:* Modeling and simulation are used to set and evaluate performance parameters requirements affecting software performance, quality of communication services in the data transport layers, requirements for responses to failures and anomalous conditions, and human/software or system interactions.
  + *Non-advocate software and system requirements reviews:* Reviews by knowledgeable third parties can uncover problems or issues that may have been overlooked by the primary requirements developers.
  + *Use of relevant “golden rules” and “lessons learned”:* Golden rules or lessons learned are excellent sources of requirements and are recommended to be reviewed as part of the requirements validation process.
  + *Hazards and safety analyses:* Hazards analyses, such as failure modes and effects analyses and fault trees.
* Requirements Verification.  
  + *Early planning:* Assure adequate planning for simulation testbeds, communications equipment, test tools, and data collection devices.
  + *Verification methods for low observable parameters:* Instrumentation methods development for throughput, response time, or reliability.
  + *Anticipating ephemeral failure behaviors:* The verification strategy is to anticipate failure behaviors and plan for how this information can be captured – particularly if they are ephemeral and non-reproducible.
  + *Testing of diagnostics and failure isolation capabilities:* Diagnostic and fault isolation capabilities for off-nominal behavior.
  + *Capturing of unanticipated failures or behaviors:* Ensure that test plans and procedures have provisions for the recording of unanticipated behaviors.

* Requirements Management.  
  + *Gathering resources for software test and verification*: Assembling modeling and simulation capabilities, domain expertise, identifying areas of uncertainty.
  + *Scheduling of software test and verification:* A robust software test and verification program include managing critical path scheduling pressures.
  + *Tracking and maintaining requirements throughout the development process:* Newly discovered software requirements are propagated back into the higher-level software and systems requirements documentation, and changes in existing requirements are documented and tracked.
  + *Configuration management of software requirements:* Ensure that changes to software requirements are controlled and that when changes are made, they are propagated to all entities and stakeholders involved in the project.
* Software Architecture Trades.  
  + *Distributed vs. centralized architectures:* Distributed single point transmission failures include undetected or unregulated message delays or loss of synchronization in replicas of common data. Centralized architectures are vulnerable to failures in the central node of a centralized system.
  + *The extent of modularity:* Uncoupled development, integration of revised components, and utilization of previously developed (or commercial off-the-shelf (COTS)) components traded against increases the number of interfaces.
  + *Point-to-point vs. common communications infrastructure:* The reduction of interdependencies among software elements and the use of common inter-process communications constructs traded against vulnerabilities in terms of lost or delayed messages, message integrity, and message validity.
  + *COTS or reused vs. reused/modified vs. developed software:* Reliability benefits are the ability to begin early test and integration of such software. An understanding of the operational condition differences, constraints and trade-offs are necessary. In safety-critical applications, uncertainties about undocumented design decisions and tradeoffs embodied in the code may necessitate redevelopment. Verification of the suitability of the re-used software components by means of assessment of operational service history, the applicability of the allocated requirements to the published capabilities of the software, compatibility with other runtime elements, and proper version numbers.
* Software Design.  
  + *Traceability:* Requirements are to be traceable to the functional elements or classes defined in the design.
  + *Exception handling and other failure behaviors:* Exception handlers are to consider all failure conditions defined in the requirements and in safety analyses. Where possible, exceptions are handled as close to the locations in the code where they are generated.
  + *Diagnostics capabilities:* Special attention is paid to response time anomalies, priority inversion, and resource contention. The diagnostic capability of the system as a whole will largely depend on the diagnostic capabilities in all of the constituent software components.
  + *Implementation language:* The implementation language and runtime environment (including virtual machines) are to be capable of realizing the design.
  + *Interfaces:* Interfaces among software modules are completely defined and include not only arguments for the inputs and outputs of the function or object itself, but also additional parameters for status, error handling, and recovery. Interfaces are designed “defensively”.
  + *Class library definition and inheritance:* For object-oriented architectures, the definition of base and derived classes is consistent and traceable to both the requirements and the architecture.
  + *Compatibility with hardware and resource constraints:* The software allocated to each hardware element conforms to memory, processor capacity, and interface constraints.
  + *COTS and Non-developmental runtime elements:* Existing software components and runtime elements are configuration controlled, well-characterized with respect to the intended use, and fully documented.
  + *Automated coding tools:* Newer techniques, based on object-oriented design or model-based development, have resulted in tools that can go directly from design to executable code. Among the advantages is the ability to generate an executable design that can be evaluated prior to detailed coding. Among the concerns is the quality of the automatically generated code, particularly with respect to off-nominal conditions or inputs.

* Code Implementation.  
  + *Use of “safe” subsets for safety or mission-critical functions:* Modern languages such as Ada, C, C++, and Java have safe subsets defined (or in the process of being defined) for their use in safety-critical applications. Disadvantages of such subsets are the implementation in the language requires more source code which both reduces productivity (thereby adding to development cost), complicates software maintenance, and discourages reusability.
  + *Routine or class libraries, and runtime environments:* The runtime libraries and other environmental components that support the developed software conform to the constraints of the architecture and design and provide the necessary capabilities to support desired failure behavior – including reliability, performance, throughput; failure response, detection, and recovery; and diagnostics requirements.
  + *Definition of suitable coding standards and conventions:* Coding standards and conventions can enhance reliability by considering such issues as:  
    - Policies on dynamic memory allocation in safety-critical systems (generally, not allowed).
    - Policies on the use of “pointers.”
    - “Defensive” coding practices for out of range inputs and response times.
    - Exception handler implementation.
    - Coding to enhance testability and readability.
    - Documentation to support verification.
    - Interrupt versus deterministic timing loop processing for safety-critical software.
    - Policies on allowable inter-process communications mechanisms (e.g., point to point vs. publish and subscribe).
    - Permitted use of dynamic binding (an alternative is static “case statements”).
    - Policies on initialization of variables (some standards prohibit the assignment of dummy values to variables upon initialization in order to enable detection of assignment errors in subsequent execution).
    - Use of “friend” (C++) or “child” (Ada) declarations to enable testing and evaluation of encapsulated data code during development without requiring the subsequent removal of “scaffold code.”
  + *Coding tools and development environments:* Coding tools and integrated development environments can be used to for many purposes including automated documentation generation, enforcement of coding standards, debugging, diagnosis of potentially troublesome coding practices, cross-reference listing, execution profiles, dependency analysis, design traceability, and many other purposes.
  + *Configuration management practices:* Defect tracking and configuration management practices for software units and higher levels of integration are defined to avoid uncertainty in the actual configuration of the software.
* Test and Inspection of Code.  
  + *Code execution:* Numerous methods for verification of executable code (see tables below); however, code execution testing cannot cover all possible code execution states.
  + *Code inspections:* Code inspections by knowledgeable individuals can find and fix mistakes overlooked in the initial programming. Another form of code inspection is the use of automated code analysis tools. Other types of reviews may occur in conjunction with code reviews including “walkthroughs” and “code audits”.
  + *Formal methods:* Testing is often insufficient to provide the necessary degree of assurance of correctness for safety-critical software. Formal methods use mathematical techniques to prove the specification, the verification test suite and also automatic code generators to create the software. The NASA Langley Research Center has been active in advancing formal methods, and extensive information is available from their web site.
  + *Cleanroom technique:* The cleanroom technique was developed as an alternative approach to producing high-quality software by preventing software defects by means of more formal notations and reviews prior to coding. The cleanroom technique has been used in several projects including the NASA Jet Propulsion Laboratory Interferometer System Integrated Testbed.

Table 1: Software Test Types

# 4. Assessment approach: Functional requirement grouping review

Similar to the life cycle activities approach, assessment via functional groupings of requirements from the NASA standards can be performed. For example, NPR 7150.2 groups requirements into categories such as organizational capabilities, software life cycle planning, off-the-shelf software, software verification and validation, software requirements, software design, risk management, training, etc. The NASA Software Assurance and Software Safety Standard (NASA-STD-8739.8 [278](#_tabs-<p>6</p>)) defined the software assurance and software safety requirements.

Review each of these requirement groupings as a whole to gather a basic understanding of the intent and focus of that group of requirements. Using that understanding, assess the alternate standard package to see if the intent of the set of requirements is met.

Once the groupings of requirements have been assessed, it is also important to evaluate the alternate standard package for completeness and overall content. It is recommended that a recognized expert or person with several years of experience with the specific standard perform this type of review given that assessment of overall content and completeness is focused on determining the provider’s conceptual understanding of the standard for which the alternate is being supplied.

# 5. Assessment approach: Requirement level review

Once NASA receives a provider’s submitted alternate standard package, that alternate needs to be assessed to determine, from NASA’s perspective, if the alternative meets the intent of the equivalent NASA standard.  Below is a brief description of one alternate standard assessment process as developed and used on the CCP.  Other approaches may be used, but this option provides a detailed view of the alternate against the NASA standard.

* Tailor requirement set.  
  + For each requirement in the NASA standard:  
    - Determine applicability for the contract, program, or project and document justification (justification rationale for requirements determined to be not applicable is required, the rationale for applicable requirements is optional).  
      * E.g., requirements for a NASA Center or the Office of the Chief Engineer likely do not apply to providers.
      * E.g., some requirements may not apply in a commercial program where NASA is only “buying a ride” and will not own the software.
      * E.g., some program contracts may only hold commercial providers to a subset of the requirements in a standard; for CCP, a subset of the Models & Simulations Standard (NASA-STD-7009) requirements were required to be met by the providers.
  + For each applicable requirement:  
    - Identify the criticality of the requirement to the contract, program, or project.  
      * If the requirement is a constraint, such as a safety requirement, the requirement must be satisfied by the provider.
      * If the requirement is simply a good practice or something strongly desired, criticality could be defined on a scale of 1 to 10 to help identify the requirements most strongly desired.
      * For requirements with multiple parts (i.e., requirement X has sub-elements a-e), it may be helpful to define criticality for each part; for example, in a requirement for a documented content that includes training as well as technical content, the technical content might have a higher criticality than training.
      * When resources or time are short, or there are other issues that indicate not all requirements will have an equivalent in the alternate standard package, attention, focus, and pressure can be applied to the requirements or parts of requirements at the top of the criticality list, e.g., the “musts” and highly desired “wants.”
* Develop assessment criteria to help ensure consistent and reasonably objective assessments.  
  + For each applicable requirement in the NASA standard:  
    - Determine the requirement’s intent, e.g., why the requirement is important to NASA (i.e., rationale, purpose, basis, objective).  
      * This information can be obtained from handbooks such as the Software Engineering Handbook for NPR 7150.2, guidebooks such as the software safety guidebook, text in the standard that provides context for the requirement, subject matter experts, working groups, etc.
    - Develop questions/evaluation criteria based on the requirement’s intent.  
      * Questions are to allow confirmation that the intent of the requirement is met in the alternate standard.
      * Program-specific references may be included where appropriate to help evaluators focus their assessment; e.g., “Does the provider have the safety criticality assessment and results recorded and available upon request (e.g., to the CCP)?” or “Are software safety personnel and other stakeholders, including NASA or CCP members participating in software reviews?”
      * A peer review or a team approach is recommended to ensure the questions/criteria adequately represent the intent of the requirement.
* Determine document set to assess.  
  + Based on the provider’s approach to alternate standards as described above, NASA may have received one or more documents to evaluate.
* Assess provider documents individually using the question set/evaluation criteria and the requirement text, capturing notes to ensure the results are evidence-based.  
  + It may be helpful to capture sections, pages, quoted text, etc. for later review during the overall assessment results roll-up.
* For each requirement, roll up assessment results to show an overall summary of the coverage of the required intent.
* Categorize summary results.  
  + E.g., “Fully Meets”, “Partially Meets”, “Does Not Meet.”
* Generate an overall summary of results showing recommendations for “meets the intent” or not and identifying any gaps.
* If applicable, generate comments/feedback for the provider.  
  + If allowed, provide feedback to help close gaps.

The images below are samples from the spreadsheet template used for this approach on the CCP.  Figures 1-3 show how the spreadsheet was organized as well as how applicability, applicability rationale, and evaluation criteria were captured in the spreadsheet.  Figure 4 shows the columns used to capture the identification of each evaluated document and the evaluation summary and overall assessment for each requirement.

Figure 1a: Spreadsheet Title Row - Left Portion

Figure 1b: Spreadsheet Title Row - Right Portion

The columns in this figure are intended to contain:

* Document Name – Name of NASA Standard.
* Requirement Number – Identification of the requirement (e.g., SWE-022).
* Requirement Text – Text of requirement from the NASA standard.
* CCP Applicability – Assessment of applicability for the NASA program (this example was for the CCP); if consistent text established, can be used to generate metrics for evaluation results, e.g.:  
  + “Out of Scope” or “Not Applicable.”
  + “Primary Focus” (for requirements that must be met without much flexibility).
  + “Secondary Focus” (for requirements that are not as critical for a provider to meet or which may have flexibility in meeting the intent).
* CCP Applicability Rationale – Rationale for applicability choices.
* Evaluation Criteria – Question set or criteria generated from requirement rationale.
* Compliance Assessment – Summary text entered after Compliance Assessment Summary is completed; if consistent text established, can be used to generate metrics for evaluation results, e.g.:  
  + “Fully Meets.”
  + “Partially Meets.”
  + “Does Not Meet.”
  + “Unable to Assess” (might apply if the provider alternate standard references procedures or work instructions which contain the data needed to assess compliance, but which were not provided to NASA).
  + “Assessed Elsewhere” (might apply to safety or assurance standard requirements in NPR 7150.2 since the full intent of those requirements is to meet the NASA safety or software assurance standards).
* Compliance Assessment Summary – Summary notes from all documents assessed in that row; especially important to identify gaps here which can be used as the basis for feedback to the provider.
* Artifacts Evaluated – identification information for each document assessed, including dates and versions/revisions; duplicate this column for each artifact evaluated.

Figure 2: Applicability Rationale

Figure 3: Evaluation Criteria

Figure 4: Artifact Capture and Rollup Columns

If this type of spreadsheet is used, the Artifacts Evaluated column is to be duplicated to the right, one column for each document assessed.  The results for each individual document are captured in the appropriate column and the set of results across that row are combined to determine an overall assessment of “meets the intent” for that requirement.  The overall results are entered into the Compliance Assessment Summary and Compliance Assessment.

**Recommended Practices for the requirement level review**

* Spreadsheets work well for this type of work.
* A single spreadsheet can be used for multiple standards; simply add rows to the bottom of the spreadsheet for the next standard to be assessed.   
  + Separating the sections for each standard with a dividing row can be helpful when doing assessments.
  + Using the spreadsheets filters to only show the rows for a single standard at a time is also helpful.
* Key information to capture in the cell for each document in the sections, pages, quoted text, etc. where each requirement is met (fully or partially).
* If using a spreadsheet to perform assessments for multiple standards, it is helpful to mark the cells for the standards to which a document does not apply as “NA” so there is no question about a missed or overlooked assessment.
* Don’t forget to determine the applicability of requirements for a given program/project and capture the rationale for applicability choices.  Capturing the rationale is important for historical purposes as well as to allow peer review of those choices.
* For requirements that reference meeting other standards, assess the alternate standard against the referenced standard. For example, NPR 7150.2, SWE-022, requires the project to implement software assurance per NASA-STD-8739.8,[278](#_tabs-<p>6</p>) so unless the alternate standard explicitly states the project will meet NASA-STD-8739.8, the alternate standard is to be assessed against meeting the intent of NASA-STD-8739.8.
* If using a spreadsheet, use filters and hide columns to help manage the data during an assessment (e.g., filter out non-applicable requirement rows, hide columns for documents already assessed or yet to be assessed).
* Have results peer-reviewed; even with agreed-upon assessment criteria, subjectivity factors into these evaluations, so multiple viewpoints help ensure consistent results.
* It may be helpful to insert an additional column into the spreadsheet to capture where each requirement has been addressed in the provider’s alternate standard package. While this information may also be found throughout the assessment results, capturing only the location information (e.g., document name and section or paragraph number) in a single column, creates a trace matrix for easy reference for subsequent assessments and reviews.  This is especially helpful if a change to a submitted and evaluated alternate standard needs to be assessed for impact against meeting the NASA standard.

# 6. Resources

## 6.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-272)

  [NASA Standard for Models and Simulations,](https://standards.nasa.gov/standard/nasa/nasa-std-7009 "Click to open in new window")

  NASA-STD-7009A w/ CHANGE 1: ADMINISTRATIVE/ EDITORIAL CHANGES 2016-12-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 6.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 6.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) |

## 6.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>6</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Center Libraries](https://nen.nasa.gov/web/software/wiki) |

## 6.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.09 Software Risk Management](/spaces/SWEHBVD/pages/133235385/A.09+Software+Risk+Management) |
