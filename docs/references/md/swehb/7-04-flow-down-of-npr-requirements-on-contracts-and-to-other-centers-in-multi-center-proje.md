# 7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695621. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects

7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695621)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695621&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Requirements and Flow Down to Contracts](#tabs-2)
* [3. Requirements Flow Down to Multi-Center Teams](#tabs-3)
* [4. Flow Down Considerations](#tabs-4)
* [5. Allocation of SWEs to Performing Organizations](#tabs-5)
* [6. Resources](#tabs-6)
* [7. Lessons Learned](#tabs-7)

# 1. Purpose

NPR 7150.2, NASA Software Engineering Requirements, [083](#_tabs-<p>6</p>) is applicable to all NASA software development activities, including single and multi-Center projects and contracted development efforts. This topic provides suggestions to the software lead for applying the Agency-level requirements contained in NPR 7150.2 to contracts. It also helps NASA's lead Centers determine the NPR requirements that are appropriate for each Center participating in multi-Center projects. This topic supplements the NPR by providing some brief examples for imposing the requirements, or their intent, on software development activities.

## 1.1 Introduction

Many of NASA's original software development activities were project-specific and were created with the particular project's needs in mind. New software development was required because software adaptation and reuse seldom occurred. Usually, software development occurred at a Center or at a contractor site. While multi-Center software development did occur, NASA had minimal available resources for assuring the effective management and compliance with the specified requirements. This situation changed dramatically with the development of NPD 2820.1, NASA Software Policy, and the first issuance of NPR 7150.2. The need for Center development processes to be consistent with NPR 7150.2 also increased as NASA began greater use of multi-Center teams.

NPR 7150.2 addresses these needs by imposing requirements on various software development activities and tasks used by NASA to acquire, develop, assure, and maintain software for its programs. NPR 7150.2 provides procedural requirements to the responsible NASA project managers and contracting officers for NASA contracts. The NPR applies to the Jet Propulsion Laboratory, contractors, grant recipients, or other parties to agreements only to the extent specified or referenced in the appropriate contracts, grants, or agreements. The NPR is made applicable to contractors through contract clauses, specifications, or statements of work in conformance with the NASA Federal Acquisition Regulation (FAR) Supplement. [259](#_tabs-<p>6</p>)

This topic discusses examples for the application and flows down of the requirements to contractors and/or other parties as described above. Other approaches for flowing down NPR 7150.2 can be employed, as long as compliance with the applicable requirements is shown.

# 2. Requirements and Flow Down to Contracts

Contractors and subcontractors develop in-house policies and procedures to provide quality software products and to fulfill the requirements passed down to them contractually. The correct application of the NASA acquisition process typically results in the specification of the applicable technical standards and requirements documents in the contract statement of work for software development activities that are performed by a prime contractor. Contractor and subcontractor policies and procedures are typically designed to satisfy different customers in an effective and efficient manner. Because many contract organizations have software development capabilities that match or even exceed those of NASA, the resulting list of included requirements is often subject to negotiation and modification as a part of the software acquisition process. NPR 7150.2 provides software acquisition guidance (see Topic [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance)), but it does not specify the exact manner for imposing its requirements to the contract. (The further flow down of requirements to subcontractors is managed by the prime contractor.)

The final agreed-to requirements may be levied on the contract in a number of different ways. The important point is that, whatever approach is chosen, the effectiveness of the final list of applied requirements is to be equivalent to or better than the intent of the NPR.

The important point is that, whatever approach is chosen, the effectiveness of the final list of applied requirements is to be equivalent to or better than the intent of the NPR.

This can be assured when the software development team assesses the final set of requirements and the selected processes for equivalency and compliance with the intent of the NPR.

The following paragraphs illustrate some scenarios of levying the NPR requirements on a contracted software development effort. These are just some example methods; other methods may be utilized.

**Scenario 1**

The developing Center makes NPR 7150.2 requirements a direct part of the contract statement of work. NASA's intent is that the performing contract organization will use the requirements statements of the NPR according to the wording and assistance notes to develop its software. Deviations from NPR 7150.2 or the use of equivalent substitutions can be explicitly specified or referenced in the contract statement of work.

The following paragraphs provide scenarios and examples of contract language that can be used and adjusted as needed for applying NPR 7150.2 requirements:

1. The contractor shall develop and maintain the software in accordance with NPR 7150.2, NASA Software Engineering Requirements, [083](#_tabs-<p>6</p>) for the appropriate software classes.
2. The contractor may substitute its in-house software development processes if the government accepts that they have been shown to be equivalent to or better than the intent of the requirements in NPR 7150.2.
3. For IT applications, Class F software, mission-specific flight, and non-flight software, the contractor shall use commercial off-the-shelf and existing government off-the-shelf products were cost-effective to NASA.

**Scenario 2**

The developing Center flows down the requirements of NPR 7150.2 into its Center-level or project-level procedures and requirements documents, which, in turn, are applied to the contract statement of work. Center-level or project-level directives are developed by NASA Centers to document their local software policies, requirements, and procedures. These directives are responsive to the requirements that are hierarchically above them while addressing the specific application areas and the Center's mission within the Agency. Prior assessments and independent reviews provide assurance that the Center or project processes and requirements documents are equivalent to or better than the intent of NPR 7150.2. The responsible Center then assures compliance with the requirements of the NPR by assuring compliance with the Center or project documents levied on the contractor. This approach, while taking more time for Center personnel to prepare, may be more efficient for the performing contractor, since the levied documents are tailored to the Center or project needs and to the project at hand.

The following paragraphs provide examples of contract language that can be used and adjusted as needed when Center-defined documents are used to capture and flow down some or all of the NPR 7150.2 requirements:

1. The contractor shall use the following document for the development of all software document deliverables:

* CXP-02009, Constellation Software Classification Matrix (use as guidance in interpreting flight software classification definitions in NPR 7150.2).

2. For IT applications, Class F Software, other than mission-specific software, the contractor shall:

* Where cost-effective to NASA, use commercial off-the-shelf and existing government off-the-shelf products.
* Ensure compatibility with existing NASA applications and systems.
* Comply with NASA requirements for NPR 7150.2 for the appropriate software classes, limited to Classes F.

3. The developing Center levies equivalent internal documents that have been shown to be compliant with the minimum acceptable requirements of NPR 7150.2, even though one-to-one traceability is not possible. These internal documents are formed by giving consideration for what makes sense and for what the project wants. This scenario and scenario 1 are similar but not identical. Whereas the previous scenario above flows NPR requirements through its Center procedures down to the contractor, this scenario uses a unique set of requirements statements that produce the same end effect but through the application of a set of different or unique procedural steps.

* The following Figure 2.1 provides an example of how equivalent but unique Center processes and requirements may evolve for application to the contract statement of work. This example approach can be used and adjusted as needed for applying NPR 7120.5 [082](#_tabs-<p>6</p>) requirements.

# 3. Requirements Flow Down to Multi-Center Teams

The previous two scenarios for contracted efforts can also be adapted to supporting Center activities in a multi-Center approach. When dealing with support Centers in multi-Center development activity, the lead Center usually develops the approach for establishing the governing standards and requirements documents to be used during the software development activity. Lead Centers and supporting Centers have the additional task of determining which Center's software development processes will be used during the project. Consider using the following steps:

1. Describe and document the implementation approach for the project, including the acquisition strategy, e.g., all in-house, NASA Centers, and contractors.
2. Describe and document how participating NASA Centers' implementation policies and practices will be utilized in the execution of the project. (Note: for tightly coupled projects, the project manager and the Center Chief Engineer(s) or designees participate in the establishment of the engineering best practices to be used.)
3. Come to an agreement on a common/shared compliance matrix against NPR 7150.2, which is to be maintained by the Lead Center. This matrix typically notes which Center has primary responsibility for each applicable requirement and the extent (if any) of support provided by another Center(s). When a Center is assigned a subset of the overall software system, consider if a stand-alone compliance matrix is more effective.
4. Document the agreements for the use of the policies and procedures.
5. Document the approach for ensuring that interfaces do not increase the risk to mission success. (Also, see [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management).)

When the lead Center develops a project, it needs to evaluate each SWE to see which ones are applicable to the project. In a multi-Center project, the lead Center needs to decide which SWE it will 'keep' for its own execution and which will be jointly or uniquely performed by supporting Centers. More likely than not, this division of assignments will be based on project needs, Center and or contractor expertise, and level of importance of the task. (The items that are assigned to the contracted statement of work remain the responsibility of the contracting Center to show compliance.)

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 4. Flow Down Considerations

## 4.1 Assessment of Compliance

There are two approaches for assuring the successful implementation of NPR 7150.2 on a contract. The first is government verification of the contractor activities through the use of the Insight process (see [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight)). In this approach, the government uses a series of meetings, inspections, and evaluations to ascertain that the contractor is satisfying the approved requirements and processes in the contracted statement of work. The second approach concerns the development of software when a tiered set of contractors (prime/subcontractor) develops the software. In this latter approach, the government and the prime may share responsibility for verifying the subcontractor's performance. The prime may use oversight and its own verification processes to assure that the subcontractor is meeting the flow down of NPR requirements. The government, in turn, will use insight and possibly independent verification (see [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) and [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation)) that the software is being developed using the required processes.

## 4.2 Safety Considerations

NPR 8715.3C, NASA General Safety Program Requirements, chapter 2, [267](#_tabs-<p>6</p>) discusses safety and risk management requirements for NASA contracts. Responsibilities of the project/program manager, Contracting Officer, and Safety and Mission Assurance personnel are described in various chapters.

**NASA Software Safety Guidebook**

12.2 Contractor-developed Software  
"With a contract, especially a performance-based contract, it is usually difficult to specify how the contractor develops the software. The end result is the primary criteria for successful completions. However, with safety-critical software and systems, how is very important. The customer needs to have insight into the contractor development processes. This serves two purposes: to identify major problems early so that they can be corrected, and to give confidence in the final system."[276](#_tabs-<p>6</p>)

      According to NPR 8715.3, the following items can be considered for inclusion in any contract:

* Safety requirements.
* Mission success requirements.
* Risk management requirements.
* Submission and evaluation of safety and risk management documentation from the contractor, such as corporate safety policies, project safety plans, and risk management plans.
* Reporting of mishaps, close calls, and lessons learned.
* Surveillance by NASA. Performance-based contracts still have a requirement for surveillance!
* Subcontracting: require that the safety requirements are passed on to subcontractors!

The contract should also clearly state what analyses or special tests need to be done for safety and mission assurance, who will do them, and who will see the results. In a performance-based contract, usually, the contractor performs all functions, including analyses. In other cases, some of the analyses may be handled from the NASA side. Regardless, the tests and analyses should be spelled out, as well as the responsible party. see [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), Topic [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance)

## 4.3 Multi-Center Considerations

When executing their portions of a multi-Center project, supporting Centers receive governing requirements and processes from the lead Center through one of the examples approaches described earlier. Since each Center has its own set of software development processes and procedures, it may occasionally run into a difference of opinion as to which Center's approach will be used. While discussions and negotiations can clear up the majority of issues, a few may remain that require additional help to resolve. Several of these 'help' are discussed briefly below:

a. Technical Authority: The NASA governance model prescribes a management structure that employs checks and balances between key organizations to ensure that decisions have the benefit of different points of view and are not made in isolation. (See NPD 1000.0, NASA Governance and Strategic Management Handbook [261](#_tabs-<p>6</p>).) NASA has established the technical authority process as part of its system of checks and balances to provide independent oversight of programs and projects in support of safety and mission success.

Occasionally, a disagreement may arise regarding the implementation of Center designated requirements. In the event negotiations do not solve the disagreement, the technical authority process may be used to assure that the appropriate viewpoints are heard at the appropriate levels of management.

b. Deviations and Waivers: Whenever the requirements specified in a multi-Center software development project come under dispute, the deviation and waiver process may be used to arrive at an agreed-to amended set of requirements. (See [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations).)

c. Reviews: Occasionally, the choice of chairperson and method for conducting reviews will result in a disagreement between Center and contractor and/or lead Center and supporting Center procedural documents. The clear flow down and agreement on requirements and process documents ahead of time can negate these types of issues. (See [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review)).

## 4.4 CMMI Rating Considerations

When a project acquires either Class A or Class B software, at a minimum, personnel from an organization that has a non-expired CMMI® Maturity Level (ML)3 or ML2 rating, respectively, in the Supplier Agreement Management (SAM) process area are required to support the acquiring organization during the acquisition planning process in the software area. This ensures that the project is supported by a smart buyer who is knowledgeable of the best software practices associated with CMMI® resident within the supplier's engineering capability. This SAM-only alternative allows a Center or prime contractor who might only procure small amounts of Class A and Class B software and who may not have a full CMMI® ML2 or ML3 rating to acquire this type of software and to participate in a project that requires its use.

## 4.5 Software-related Federal Acquisition Regulation (FAR) Considerations

While not directly related to the flow down of NPR 7150.2 requirements, the Federal Acquisition Regulations have data rights clauses that are important to be included on contracts for software acquisition.  See the FAR for further details and work with procurement, but, in general, given the conditions shown below, ensure the appropriate clauses are included in the contract.

* General Data Rights Clauses  
  + Include a General Data Rights Clause if it is contemplated that data will be produced, furnished, or acquired under the contract.
  + Include an NFS 1852.227-14 data rights clause which prevents the contractor from asserting copyright without permission and requires the contractor to assert and assign its copyright interest to NASA when directed by the Contracting Officer.
* Unlimited Rights Clauses  
  + Include a FAR 52.227-14 General Data Rights Clause so long as alternate clauses are not included.
  + Include a FAR 52.227-17 Special Works Clause, including NFS 1852.227-17, (Drawback:  potential for increased costs).
  + Include an H Clause requiring the contractor to assert copyright and assign a title to NASA as soon as the software is fixed in a tangible medium for “software and all derivative works”.
  + Specify the data to be delivered; ensure the source code is listed as a deliverable in the Statement of Work (SOW) and the contract deliverables (CDRLs).
* Limited Rights Clauses  
  + Include a FAR 52.227-15 clause in solicitations to identify what data and software will be delivered with limited or restricted rights.
  + Include a FAR 52.227-14 clause with Alternate III to allow the contractor to incorporate proprietary software into the final product and leave NASA with less than unlimited rights in the complete software product.

## 4.6 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 5. Allocation of SWEs to Performing Organizations

Appendix C of NPR 7150.2 indicates the office or organization that is responsible for each SWE's execution. The content of these requirements needs to be evaluated by the project and assigned to the development team (lead Center, supporting Center, contractor) as indicated by the analysis. The results and rationale for the assignments can be documented as needed.

For instance, the project is responsible for developing software plans ([SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans)), developing a life cycle or model, and performing the classification of software ([SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)). These are typically performed by the lead Center. Training ([SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training)), scheduling ([SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule)), and reviews ([SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review)) can be assigned to supporting Centers and contractors for the execution of their portions of the software plan.

Some SWEs are not the direct responsibility of projects but require inputs from projects or Center staff. For example, the Office of the Chief Engineer and the Chief of Safety and Mission Assurance are responsible for conducting software inventory activities for classes of software development under their respective areas of responsibility. Although not responsible for executing ([SWE-006 - Center Software Inventory](/spaces/SWEHBVD/pages/102695396/SWE-006+-+Center+Software+Inventory)), Centers do need to support the development of data for the software inventory.

## 5.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 6. Resources

## 6.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-035)

  [NASA Enterprise Architecture Procedures,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2830&s=1A "Click to open in new window")

  NPR 2830.1A, Office of the Chief Information Officer, Effective Date: December 19, 2013, Expiration Date: November 30, 2021
* (SWEREF-038)

  [NASA Software Engineering Initiative Implementation Plan,](http://www.nasa.gov/pdf/417063main_NSII_Plan.pdf "Click to open in new window")

  Release 1.0, NASA Office of the Chief Engineer, 2002.
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
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-259)

  [NASA FAR Supplement website.](https://www.hq.nasa.gov/office/procurement/regs/NFS.pdf "Click to open in new window")

  The NFS is issued as Chapter 18 of Title 48, Code of Federal Regulations. The NFS has been modified through PN 19-05, dated June 11, 2019.
* (SWEREF-261)

  [NASA Governance and Strategic Management Handbook,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=0C "Click to open in new window")

  NPD 1000.0C, NASA Governance and Strategic Management Handbook, Effective Date: January 29, 2020, Expiration Date: January 29, 2025
* (SWEREF-267)

  [NASA General Safety Program Requirements (Updated w/Change 3)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8715&s=3D "Click to open in new window")

  NASA Procedural Requirements, NPR8715.3D, Effective Date: August 01, 2017, Expiration Date: August 01, 2022
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
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
| * [SWE-006 - Center Software Inventory](/spaces/SWEHBVD/pages/102695396/SWE-006+-+Center+Software+Inventory) * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation)        * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) |

## 6.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>6</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting)      * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

## 6.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 7. Lessons Learned

### 7.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 7.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
