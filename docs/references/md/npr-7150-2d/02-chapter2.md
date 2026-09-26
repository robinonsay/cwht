# NPR 7150.2D — Chapter2

> Source: https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter2
> Page title: NPR 7150.2D - Chapter2
> Machine conversion; tables may be flattened. SWE-NNN identifiers are authoritative.

# Chapter 2. Roles, Responsibilities, and Principles Related to Tailoring of the Requirements

## 2.1 Roles and Responsibilities Associated with this Directive

2.1.1 The NASA Office of the Chief Engineer (OCE).

2.1.1.1 The NASA OCE shall lead and maintain a NASA Software Engineering Initiative to advance software engineering practices. [SWE-002]

2.1.1.2 The NASA OCE shall periodically benchmark each Center’s software engineering capability against requirements in this directive. [SWE-004]

Note: Capability Maturity Model® Integration (CMMI®) for Development (CMMI®-DEV) appraisals are the preferred benchmarks for objectively measuring progress toward software engineering process improvement at NASA Centers.

2.1.1.3 The NASA OCE shall periodically review the project requirements mapping matrices. [SWE-152]

2.1.1.4 The NASA OCE shall authorize appraisals against selected requirements in this NPR to check compliance. [SWE-129]

2.1.1.5 The NASA OCE and Center training organizations shall provide training to advance software engineering practices. [SWE-100]

2.1.1.6 The NASA OCE shall maintain an Agency-wide process asset library of applicable best practices and process templates for all size projects. [SWE-098]

2.1.2 NASA Chief, Safety and Mission Assurance (SMA).

2.1.2.1 The NASA Chief, SMA manages Agency software assurance policy and software safety policies and is the Technical Authority (TA) for any requirements in this directive.

2.1.2.2 The NASA Chief, SMA shall lead and maintain a NASA Software Assurance and Software Safety Initiative to advance software assurance and software safety practices. [SWE-208]

2.1.2.3 The NASA Chief, SMA shall periodically benchmark each Center’s software assurance and software safety capabilities against the NASA-STD-8739.8, NASA Software Assurance and Software Safety Standard. [SWE-209]

2.1.2.4 The NASA Chief, SMA shall periodically review the project’s requirements mapping matrices. [SWE-212]

2.1.2.5 The NASA Chief, SMA shall authorize appraisals against selected requirements in this NPR to check compliance. [SWE-221]

2.1.2.6 The NASA Chief, SMA shall provide for software assurance training. [SWE-222]

2.1.2.7 The NASA Chief, SMA shall make the final decision on all proposed tailoring of SWE-141, the Independent Verification and Validation (IV&V) requirement. [SWE-223]

2.1.3 NASA Chief, Office of Chief Information Officer (OCIO)

2.1.3.1 The NASA OCIO Senior Agency Information Security Officer (SAISO) will conduct security assessments and appraisals on selected requirements in this NPR to check compliance.

2.1.3.2 The NASA OCIO SAISO will participate in any software development reviews, as needed.

2.1.4 Chief Health and Medical Officer (CHMO)

2.1.4.1 The CHMO is the TA for any requirements which impact health and medical aspects.

2.1.4.2 The CHMO has approval authority of tailoring of software with health and medical implications as documented in NPR 7120.11, Health and Medical Technical Authority Implementation.

2.1.5 Center Director

2.1.5.1 In this directive, the phrase “the Center Directors shall...” means that the roles and responsibilities of the Center Directors may be further delegated within the organization consistent with the scope and scale of the system.

2.1.5.2 Center Director, or designee, shall maintain, staff, and implement a plan to continually advance the Center’s in-house software engineering capability and monitor the software engineering capability of NASA’s contractors. [SWE-003]

Note: The recommended practices and guidelines for the content of a Center Software Engineering Improvement Plan are defined in NASA-HDBK-2203, NASA Software Engineering Handbook. Each Center has a current Center Software Engineering Improvement Plan on file in the NASA Chief Engineer’s office.

2.1.5.3 Center Director, or designee, shall establish, document, execute, and maintain software processes per the requirements in this directive. [SWE-005]

2.1.5.4 Center Director, or designee, shall comply with the requirements in this directive that are marked with an “X” in Appendix C. [SWE-140]

Note: The responsibilities for approving changes in the requirements for a project is listed for each requirement in the requirement mapping matrix. When the requirement and software class are marked with an “X,” the projects will record the risk and rationale for any requirement that is not completely implemented by the project. The projects can document their related mitigations and risk acceptance in the approved Requirements Mapping Matrix. Project relief from the applicable cybersecurity requirements, Section 3.11, Software Cybersecurity, has to include an agreement from the SAISO or Center CISO, as designated by the SAISO. The NASA Agency CIO, or Center CIO designee, has institutional authority on all Class F software projects.

2.1.5.5 The Center Director, or designee, shall report on the status of the Center’s software engineering discipline, as applied to its projects, upon request by the OCE, OSMA, or OCHMO. [SWE-095]

2.1.5.6 Center Director, or designee, shall maintain a reliable list of their Center’s programs and projects containing Class A, B, C, and D software. The list should include: [SWE-006]

a. Project/program name and Work Breakdown Structure (WBS) number.

b. Software name(s) and WBS number(s).

c. Software size estimate (report in Kilo/Thousand Source Lines of Code (KSLOCs)).

d. The phase of development or operations.

e. Software Class or list of the software classes being used on the project.

f. Software safety-critical status.

g. For each Computer Software Configuration Item (CSCI)/Major System containing Class A, B, or C software, provide:

(1) The name of the software development organization.

(2) Title or brief description of the CSCI/Major System.

(3) The estimated total KSLOCs, the CSCI/Major System, represents.

(4) The primary programming languages used.

(5) The life cycle methodology on the software project.

(6) Name of responsible software assurance organization(s).

2.1.5.7 For Class A, B, and C software projects, the Center Director, or designee, shall establish and maintain a software measurement repository for software project measurements containing at a minimum: [SWE-091]

a. Software development tracking data.

b. Software functionality achieved data.

c. Software quality data.

d. Software development effort and cost data.

2.1.5.8 For Class A, B, and C software projects, the Center Director, or designee, shall utilize software measurement data for monitoring software engineering capability, improving software quality, and to track the status of software engineering improvement activities. [SWE-092]

2.1.5.9 Center Director, or designee, will maintain and implement software training to advance its in-house software engineering capabilities.

2.1.5.10 For Class A, B, and C software projects, each Center Director, or designee, shall establish and maintain software cost repository(ies) that contains at least the following measures: [SWE-142]

a. Planned and actual effort and cost.

b. Planned and actual schedule dates for major milestones.

c. Both planned and actual values for key cost parameters that typically include software size, requirements count, defects counts for maintenance or sustaining engineering projects, and cost model inputs.

d. Project descriptors or metadata that typically includes software class, software domain/type, and requirements volatility.

2.1.5.11 Each Center Director, or designee, shall contribute applicable software engineering process assets in use at his/her Centers to the Agency-wide process asset library. [SWE-144]

2.1.5.12 The designated ETA(s) shall define the content requirements for software documents or records. [SWE-153].

Note: The recommended practices and guidelines for the content of different types of software activities (whether stand-alone or condensed into one or more project level or software documents or electronic files) are defined in NASA-HDBK-2203. The Center defined content should address prescribed content, format, maintenance instructions, and submittal requirements for all software related records. The designated TA for software approves the required software content for projects within their scope of authority. Electronic submission of data deliverables is preferred. “Software records should be in accordance with NPR 7120.5, NPD 2810.1, NASA Information Security Policy, NPD 2800.1, and NPR 2810.1.”

2.1.5.13 The Center Director, or designee, shall ensure that the Government has clear rights in the software, a Government purpose license, or other appropriate license or permission from third party owners prior to providing the software for internal NASA software sharing or reuse. [SWE-215]

2.1.5.14 The Center Director, or designee, shall ensure that all software listed on the internal software sharing or reuse catalog(s) conforms to NASA software engineering policy and requirements. [SWE-216]

2.1.5.15 The Center Director, or designee, (e.g., the Civil Servant Technical Point of Contact (POC) for the software product) shall perform the following actions: [SWE-217]

a. Keep a list of all contributors to the software product.

b. Ensure that the software product contains appropriate disclaimer and indemnification provisions (e.g., in a “README” file) stating that the software may be subject to U.S. export control restrictions, and it is provided “as is” without any warranty, express or implied, and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors.

2.1.5.16 The Center Director or designee (e.g., the Civil Servant Technical POC for the software product) shall perform the following actions for each type of internal NASA software transfer or reuse: [SWE-214]

a. A NASA civil servant to a NASA civil servant:

(1) Verify the requesting NASA civil servant has requested and completed an Acknowledgment (as set forth in the note following paragraph 3.10.2e).

(2) Provide the software to the requesting NASA civil servant.

b. A NASA civil servant to a NASA contractor:

(1) Verify a NASA civil servant (e.g., a Contracting Officer (CO) or Contracting Officer Representative (COR)) has confirmed the NASA contractor requires such software for the performance of Government work under their NASA contract and that such performance of work will be a Government purpose. Center Intellectual Property Counsel should be consulted for any questions regarding what is or is not a Government purpose.

(2) Verify a NASA civil servant (e.g., a CO or COR) has confirmed an appropriate Government Furnished Software clause (e.g., 1852.227-88, “Government-furnished computer software and related technical data”) is in the subject contract (or, if not, that such clause is first added); or the contractor may also obtain access to the software in accordance with the external release requirements of NPR 2210.1, Release of NASA Software.

(3) Verify NASA contractor is not a foreign person (as defined by 22 CFR §120.16).

(4) Verify there is a requesting NASA Civil servant (e.g., a CO or COR), and the requesting NASA civil servant has executed an Acknowledgment (as set forth in the note following paragraph 3.10.2e).

(5) After items (1), (2), (3), and (4) are complete, provide the software to the requesting NASA civil servant. The requesting NASA civil servant is responsible for furnishing the software to the contractor pursuant to the subject contract’s terms.

c. A NASA civil servant to any NASA grantees, Cooperative Agreement Recipients or any other agreement partners or to any other entity under U.S. Government Agency Release, Open source Release, Public Release, U.S. Release, Foreign Release:

(1) If the release is to any NASA grantees, Cooperative Agreement Recipients, or any other agreement (e.g., Space Act Agreement) partners or to any other entity under U.S. Government Agency Release, an Open source Release, a Public Release, a U.S. Release, or a Foreign Release, the software release is completed in accordance with the external release requirements of NPR 2210.1, Release of NASA Software – Revalidated w/change 1.

2.1.6 Center SMA Director

2.1.6.1 In this document, the phrase “the Center SMA Director will…” means that the roles and responsibilities of the Center SMA Directors may be further delegated within the organization consistent with the scope and scale of the system. The Center SMA Director designates SMA TAs for programs, facilities, and projects, providing direction, functional oversight, and assessment for all Agency safety, reliability, maintainability, and quality engineering and assurance activities, including Software Assurance.

2.1.6.2 The Center SMA Director will assure the project completes thorough hazard analyses which include software.

Note: The project manager is responsible for assuring Software Safety Hazard Analyses is performed on their project. The PM is responsible for the development of the project’s software hazard analyses and its independent review. Any differences in software safety’s independent software safety critical determinations will be worked through the ETA and the SMA TA.

2.1.6.3 The Center SMA Director, will review the project’s IV&V ’Project Execution Plan (IPEP) to ensure it meets NASA IV&V criteria as defined in NASA-STD-8739.8.

2.1.6.4 The Center SMA Director will support the project to ensure that acquired, developed, and maintained software, as required by SWE-032, is developed by an organization with a non-expired CMMI®-DEV rating as measured by a CMMI® Institute Certified Lead Appraiser.

2.1.6.5 The Center SMA Director will support the Center organizations in obtaining and maintaining the NASA organization’s CMMI®-DEV ratings.

2.1.6.6 The Center SMA Director, or designee, will ensure that the project’s Requirements Mapping Matrix implementation approach does not impact SMA on the project.

2.1.6.7 The Center SMA Director will ensure that any disagreements between software engineering or the project office and software assurance are identified, reported, tracked, and if not resolved, elevated.

2.1.6.8 The designated SMA TA(s) will review, ensure, and concur on software products and processes throughout the project acquisition, development, delivery, operations, and maintenance.

2.1.7 Contracting Officers

2.1.7.1 Contracting Officers, as defined in FAR 2.101, or Agreement Managers as defined in NAII 1050.3, NASA Partnership Guide, in conjunction with Program/Project Managers shall ensure that the appropriate FAR, NFS, and other provisions/clauses based on this requirements document and NASA-STD-8739.8 are included for all NASA contracts, Space Act Agreements, cooperative agreements, partnership agreements, grants, or other agreements pursuant to which software is being acquired, developed, modified, operated, or managed for NASA. [SWE-218]

2.1.8 Technical Authorities

2.1.8.1 The TA(s) or Institutional Authority(s) for requirements in this NPR will be defined per NPR 7120.5, Section 3.3.

Note: Refer to Appendix C (column titled “Authority”) for requirements and their associated Technical or Institutional Authority. NASA HQ will designate the TA for SWE-032 and SWE-141.

2.1.8.2 The technical and institutional authorities for requirements in this directive shall: [SWE-126]

a. Assess projects’ requirements mapping matrices and tailoring from requirements in this directive by:

(1) Checking the accuracy of the project’s classification of software components against the definitions in Appendix D.

(2) Evaluating the project’s Requirements Mapping Matrix for commitments to meet applicable requirements in this directive, consistent with software classification.

(3) Confirming that requirements marked “Not-Applicable” in the project’s Requirements Mapping Matrix are not relevant or not capable of being applied.

(4) Determining whether the project’s risks, mitigations, and related requests for relief from requirements designated with “X” in Appendix C are reasonable and acceptable.

(5) Approving/disapproving requests for relief from requirements designated with “X” in Appendix C, which falls under this Authority’s scope of responsibility.

(6) Facilitating the processing of projects’ requirements mapping matrices and tailoring decisions from requirements in this directive, which falls under the responsibilities of a different Authority (see column titled “Authority” in Appendix C).

(7) Include the SAISO (or delegate) in all software reviews to ensure software cybersecurity is included throughout software development, testing, maintenance, retirement, operations, management, acquisition, and assurance activities.

(8) Ensuring that approved requirements mapping matrices, including any tailoring rationale against this directive, are archived as part of retrievable project records.

Note: To effectively assess projects’ requirements mapping matrices, the designated Center Engineering Technical and Institutional Authorities for this NPR are recognized NASA software engineering experts or utilize recognized NASA software engineering experts in their decision processes. NASA-HDBK-2203 contains valuable information on each requirement, links to relevant NASA Lessons Learned, and guidance on tailoring. Center organizations or branches may also share frequently used tailoring and related common processes.

b. Indicate the Technical Authority or Technical Authorities approval by signature(s) in the Requirements Mapping Matrix itself, when the Requirements Mapping Matrix is used to tailor from the applicable “X” requirement(s).

Note: The Requirements Mapping Matrix documents the requirements that the project plans to meet, “not applicable” requirements, and any tailoring approved by designated Authorities with associated justification. If a project wants to tailor a requirement marked as HQ TA, then the project is required to get NASA HQ approval (e.g., OCE, OSMA, OCIO, or OCHMO) on a tailored request or a software Requirements Mapping Matrix.

## 2.2 Principles Related to Tailoring Requirements

2.2.1 Software requirements tailoring is the process used to seek relief from NPR requirements consistent with program or project objectives, acceptable risk, and constraints. To accommodate the wide variety of software systems and subsystems, application of these requirements to specific software development efforts may be tailored where justified and approved. To effectively maintain control over the application of requirements in this directive and to ensure proposed tailoring from specific requirements are appropriately mitigated, NASA established TA governance. Tailoring from requirements in this directive are governed by the following requirements, as well as those defined in NPD 1000.3, The NASA OrganizationNPD 2800.1, NPR 2810.1, NPR 7120.5, NPR 7120.7, NPR 7120.8, NPR 7120.11 and NPR 8715.3 for all of the Agency’s investment areas. The Technical and Institutional Authority for each requirement in this NPR is documented in the “Authority” column of Appendix C. The responsible program, project, or operations manager need to formally accept the tailoring risk. Tailoring decided at the Center level are to consult the Center ETA, Center SMA TA, Center Health and Medical TA, and the NASA CIO’s Center IT Authority designee as defined in the requirements mapping matrix. The OSMA has co-approval on any tailoring decided at the HQ level that involves software. The Office of the Chief Medical Officer (OCHMO) has co-approval on any tailoring decided that involves software with health and medical implications. The SAISO, or designee, has co-approval on any tailoring of the cybersecurity requirements in Section 3.11. For tailoring involving human safety risk, the actual risk taker(s) (or official spokesperson[s] and appropriate supervisory chain) need to formally agree to assume the risk. ’

2.2.2 This directive establishes a baseline set of requirements to reduce software engineering risks on NASA projects and programs. Appendix C defines the default applicability of the requirements based on software classification. Each project has unique circumstances, and tailoring can be employed to modify the requirements set appropriate for the software engineering effort. Tailoring of requirements is based on key characteristics of the software engineering effort, including acceptable technical and programmatic risk posture, Agency priorities, size, and complexity. Requirements can be tailored more broadly across a group of similar projects, a program, an organization, or other collection of similar software development efforts in accordance with NPR 7120.5, Section 3.5.5.

2.2.3 In this directive, the phrase “the project manager shall...” means the roles and responsibilities of the project manager may be further delegated within the organization to the scope and scale of the system.

2.2.4 Requirements in this directive are invoked by software classifications as defined in Appendix C:

a. “X” – Indicates an invoked requirement by this directive consistent with software classification (ref. SWE-139).

b. Blank – Optional/Not invoked by this directive.

2.2.5 The approval of the Authority designated in Appendix C is required for all tailoring of requirements designated as “X.” The implementation approach used to meet each requirement is typically determined by the appropriate software engineering management in conjunction with the project.

Note: The request for relief from a requirement includes the rationale, a risk evaluation, and reference to all material that justifies supporting acceptance. The organization submitting the tailoring request informs the next higher level of involved management in a timely manner of the tailoring request. The dispositioning organization reviews the request with the other organizations that could be impacted or have a potential risk (i.e., to safety, quality, cybersecurity, health) with the proposed changes; and obtains the concurrence of those organizations.

2.2.6 Requests for software requirements relief at either the Center or HQ TA level (i.e., partial or complete relief) may be submitted in the streamlined form of a Requirements Mapping Matrix. The required signatures from engineering, NASA CIO, and SMA authorities are to be obtained. A required signature from designated SAISO is required for relief of cybersecurity requirements. If the Requirements Mapping Matrix is completed and approved in accordance with NPR 7120.5’s direction on Authority and this directive, it meets the requirements for requesting tailoring.

2.2.7 The engineering, CIO, and SMA authorities shall review and agree with any tailored NPR 7150.2 requirements per the requirements mapping matrix authority column. [SWE-150]

2.2.8 If a system or subsystem development evolves to meet a higher or lower software classification as defined in Appendix D, then the project manager shall update their plan(s) and initiate modifications to any supplier contracts to fulfill the applicable requirements per the Requirements Mapping Matrix in Appendix C with approved tailoring. [SWE-021]

  

|  |
| --- |
| | [TOC](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=main) | [Preface](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Preface) | [Chapter1](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter1) | [Chapter2](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter2) | [Chapter3](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter3) | [Chapter4](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4) | [Chapter5](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter5) | [Chapter6](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter6) | [AppendixA](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixA) | [AppendixB](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixB) | [AppendixC](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixC) | [AppendixD](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixD) | [AppendixE](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixE) | [ALL](displayAll.cfm?Internal_ID=N_PR_7150_002D_&page_name=ALL) | |
|  |
| | [NODIS Library](main_lib.html) | [Program Formulation(7000s)](lib_docs.cfm?range=7) | [Search](adv_search.cfm) | |
