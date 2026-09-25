# Book A. Introduction

> NASA Software Engineering Handbook (SWEHB Ver D), page id 100598340. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/100598340/Book+A.+Introduction

Book A. Introduction

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/100598340/Book+A.+Introduction#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=100598340)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=100598340&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Welcome](#tabs-1)
* [2. SWEHB Introduction](#tabs-2)
* [3. Title Material](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Accessing Other Versions of SWEHB](#tabs-5)
* [6. NASA-STD-8739.8B Title Material](#tabs-6)

# 

# **Welcome to the NASA Software Engineering**

# **and Assurance Handbook,** **NASA-HDBK-2203.**

### Software is a core capability and key enabling technology for NASA's missions and supporting infrastructure.

Software plays a vital role as both a key capability and an enabling technology for NASA's missions and supporting infrastructure. This wiki-based handbook provides practical guidance for meeting the requirements outlined in NPR 7150.2, *NASA Software Engineering Requirements*, and NASA-STD-8739.8, *Software Assurance and Software Safety Standard*. These requirements are based on industry standards and NASA’s proven expertise in software engineering.

Designed for those involved in the acquisition, management, development, assurance, maintenance, and operations of NASA software, the handbook offers "best-in-class" strategies for developing safe and reliable software to support NASA’s projects.

NASA-HDBK-2203 serves as a readily accessible reference, consolidating the collective knowledge of experts with extensive experience in all aspects of NASA software systems. It is an integral part of NASA's ongoing effort to enhance software engineering and assurance processes and improve software product quality across the Agency.

**Documents can be viewed and downloaded in PDF format:**

* **The NASA Software Engineering Requirements, [NPR 7150.2D](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D) [083](#_tabs-<p>4</p>)**
* **The NASA Software Assurance and Software Safety Standard requirements, [NASA-STD-8739.8B](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf) [278](#_tabs-<p>4</p>)**

You can submit any inputs and suggestions regarding SWEHB via "Feedback" in the [NASA Technical Standards System (NTSS)](http://standards.nasa.gov/).

**What's New in SWEHB!**

[New Topic - Verification and Assurance Guidelines for Multicore, Concurrent, and Partitioned Software Systems](/spaces/SWEHBVD/blog/2026/06/04/248774669/New+Topic+-+Verification+and+Assurance+Guidelines+for+Multicore+Concurrent+and+Partitioned+Software+Systems)

[Guillermo Del Carmen](    /display/~gdelcarm
) posted on Jun 04, 2026

7.26 - Verification and Assurance Guidelines for Multicore, Concurrent, and Partitioned Software Systems

* [swehb](/label/SWEHBVD/swehb)

[Added Software Lessons Learned from Psyche Project Report](/spaces/SWEHBVD/blog/2026/05/20/245825629/Added+Software+Lessons+Learned+from+Psyche+Project+Report)

[Tim Crumbley](    /display/~rcrumble
) posted on May 20, 2026

Click here for more details ...

## **Lessons Laerned from Psyche Project Report**

## **1. Late and Incomplete Flight Software (FSW) Delivery**

**Incident:**  
The Psyche mission experienced an eight‑month late delivery of the final GNC flight software build, with hundreds of control parameters and fault protection behaviors still undefined. This delay, combined with numerous unresolved software issues, contributed directly to the missed 2022 launch opportunity.

**Lesson Learned:**

* **Early Software Definition & Maturity:** Mission‑critical software requirements, parameters, and behaviors must be fully defined and matured early to prevent cascading delays.
* **Rigorous Defect Disposition:** “Use‑as‑is” and unverified failure dispositions must undergo strict technical review to prevent acceptance of excessive residual risk.

**Implication:**  
Delays and ambiguity in software maturity directly threaten launch schedules, increasing cost, workforce strain, and mission‑risk exposure.

---

## **2. Incomplete Verification & Validation (V&V)**

**Incident:**  
The project faced major V&V shortfalls, including approximately 1,000 unverified system requirements and incomplete GNC, fault protection, and FSW test coverage. Immature and incompatible testbeds further hindered simulation and closed‑loop testing.

**Lesson Learned:**

* **Comprehensive V&V Execution:** V&V must be resourced, scheduled, and monitored with the same rigor as hardware development.
* **Validated Testbeds:** Testbeds and simulations must be synchronized early with vendor tools to ensure accurate system‑level testing.

**Implication:**  
Insufficient V&V undermines mission confidence and may conceal system defects until it is too late to correct them within the launch window.

---

## **3. Undefined and Insufficiently Tested Fault Protection**

**Incident:**  
Fault protection logic was not fully defined or validated prior to the launch delay, leaving mission‑critical behaviors unverified. citeturn1search1.page21

**Lesson Learned:**

* **Early Fault Management Definition:** Fault detection, isolation, and recovery logic must be fully specified and integrated into system testing well before ATLO.
* **Hazard‑Driven Validation:** Fault responses must be validated against hazards and off‑nominal scenarios using high‑fidelity simulations.

**Implication:**  
Incomplete fault protection risks spacecraft safety, autonomy, and ability to recover from anomalies during critical mission phases.

---

## **4. Immature Testbeds and Simulation Environments**

**Incident:**  
Major incompatibilities between JPL and Maxar testbeds delayed verification activities and prevented execution of essential closed‑loop GNC testing. Early assumptions about vendor simulation capabilities proved incorrect.

**Lesson Learned:**

* **Interface Verification:** Simulation environments must be verified early with contractual clarity on capabilities, interfaces, and data integration.
* **End‑to‑End Fidelity:** High‑fidelity closed‑loop simulation must be operational well before system‑level V&V.

**Implication:**  
Faulty assumptions about vendor simulation capacity or testbed interoperability can cripple software testing and threaten mission readiness.

---

## **5. Poor Metrics and Lack of Visibility into Software Health**

**Incident:**  
Psyche’s project metrics masked true software progress. Software risk was consistently under‑reported due to an aversion to categorizing issues as “red,” preventing leadership from recognizing schedule‑threatening problems.

**Lesson Learned:**

* **Objective Software Metrics:** Software maturity must be tracked using measurable indicators such as defect trends, verification progress, and test coverage.
* **Risk Transparency:** Leadership must encourage open reporting and avoid cultural pressures that suppress accurate risk assessments.

**Implication:**  
When metrics fail to reflect reality, management loses the ability to make timely decisions, creating preventable launch‑critical failures.

---

## **6. Insufficient Staffing in Software, GNC, and Systems Engineering**

**Incident:**  
Psyche suffered from persistent understaffing in key areas such as flight software, GNC, systems engineering, and V&V. Many roles were filled with inexperienced personnel, with excessive reliance on stretch assignments and limited mentoring.

**Lesson Learned:**

* **Adequate Expertise:** Complex missions require experienced staff in critical roles (e.g., Project Chief Engineer, GNC CogE, Fault Protection Lead).
* **Sustainable Staffing Models:** Workforce planning must account for burnout, skill mix, mentoring, and retention of highly specialized talent.

**Implication:**  
Understaffing reduces software quality, increases risk of technical debt, delays development, and undermines mission execution.

---

## **7. Communication Failures Suppressing Software Concerns**

**Incident:**  
Software and system engineers raised concerns that were not acted upon. The culture fostered a “prove there is a problem” mentality, making it difficult to elevate software risks. No Independent Technical Authority (ITA) dissents were filed despite significant issues.

**Lesson Learned:**

* **Open Technical Channels:** Projects must maintain safe, responsive pathways for raising technical concerns, including through independent authorities.
* **Cultural Reinforcement:** Leadership must encourage early reporting and prohibit cultures that penalize raising risks.

**Implication:**  
When team members feel unheard, systemic issues go unaddressed, increasing mission risk and slowing problem resolution.

---

## **8. Misalignment with Commercial Vendor (Maxar) Software Capabilities**

**Incident:**  
Misaligned expectations for Maxar’s simulation, interface details, and heritage design significantly delayed testing and integration activities. COVID‑related limitations reduced the required face‑to‑face interaction needed to align on software behaviors.

**Lesson Learned:**

* **Deep Early Integration:** NASA personnel must work side‑by‑side with commercial partners early to align on simulation capabilities, interface assumptions, and development processes.
* **Contractual Clarity:** Software deliverables and testbed capabilities must be unambiguously specified in contracts.

**Implication:**  
Weak alignment with vendor software ecosystems causes delays, rework, and verification gaps that can push missions off launch schedules.

* [swehb](/label/SWEHBVD/swehb)

[Updated the software milestone review criteria and added AI criteria](/spaces/SWEHBVD/blog/2026/05/19/245825574/Updated+the+software+milestone+review+criteria+and+added+AI+criteria)

[Tim Crumbley](    /display/~rcrumble
) posted on May 19, 2026

Click here for more details ...

We updated the software milestone review criteria to strengthen alignment with current engineering best practices and project needs. As part of this revision, we introduced new AI‑focused evaluation criteria to ensure teams are appropriately addressing model reliability, validation and verification, data integrity, risk assessment, and responsible use considerations throughout the development lifecycle.

* [swehb](/label/SWEHBVD/swehb)

[Added Lessons Learned from Starliner CFT and the Lunar Trailblazer mission report](/spaces/SWEHBVD/blog/2026/03/17/235995197/Added+Lessons+Learned+from+Starliner+CFT+and+the+Lunar+Trailblazer+mission+report)

[Tim Crumbley](    /display/~rcrumble
) posted on Mar 17, 2026

* [swehb](/label/SWEHBVD/swehb)

[Added Objective Evidence for Each Requirement](/spaces/SWEHBVD/blog/2025/12/03/223150083/Added+Objective+Evidence+for+Each+Requirement)

[Tim Crumbley](    /display/~rcrumble
) posted on Dec 03, 2025

Added Objective Evidence for Each Requirement

Click here for more details ...

Objective evidence plays a crucial role in ensuring accountability, traceability, and reliability across software assurance and safety activities. It provides documented, unbiased proof that a specific activity has been performed or confirmed by the responsible software assurance/safety personnel — and it’s not just about checking a box. It amplifies the credibility of your processes.

Documenting objective evidence can take multiple forms depending on the activity being verified. Some examples include:

* **Audit Records and Checklist Results**: Observations, findings, or risks identified, documented in a tracking system, or captured in emails.
* **Meeting Records**: Attendance lists, meeting minutes, or notes stored in the project repository.
* **Status Updates**: Memos, emails, or reports confirming an activity took place, supported by summaries or confirmation checklists.
* **Reviewed/Witnessed Activities**: Signatures on reviewed products or processes to validate completion or compliance.
* **Short Summaries**: Concise statements that provide insight into specific activities or milestones, such as:
  + Progress on IV&V Program Execution.
  + Percentage of hazards traced to software requirements.

When implemented consistently, objective evidence strengthens your project’s integrity, enhances collaboration, and aligns with the guidelines set forth in Section 8.16 of the handbook. Not only does it enable teams to track progress effectively, but it also instills confidence in the accuracy of assurance efforts.

The bottom line? Every requirement deserves solid, verifiable evidence. By prioritizing documentation, you’re not just managing activities — you’re building trust across the project.

* [swehb](/label/SWEHBVD/swehb)

# Introduction

The NASA Software Engineering and Assurance Handbook (NASA-HDBK-2203) was created to address requests for additional guidance, rationale, resources, references, and lessons learned in the acquisition, management, development, assurance, and maintenance of NASA software systems. Its electronic wiki-based format was selected to meet evolving needs, including:

* Publishing material in a timely manner.
* Delivering concise, screen-friendly information.
* Simplifying updates to keep the content current.
* Enabling easy searches.
* Providing a platform for engaging the NASA software community by:
  + Sharing best practices.
  + Contributing lessons learned from projects.

The handbook is accessible via:

* [The SWEHB Wiki](https://swehb.nasa.gov/)
* [NASA Technical Standards](https://standards.nasa.gov/)
* NASA Engineering Network (NEN).

It also includes links to additional processes, templates, and tools from the Software Processes Across NASA (SPAN) repository (available only to NASA users via the SPAN tab).

While the handbook can be used like a traditional hard copy guidebook, its digital format provides significant advantages. Users can quickly access relevant, concise information by navigating the structured chapters or searching directly. A brief familiarization with its organization is usually sufficient to fully leverage its resources.

The handbook provides detailed guidance linked to the Software Requirements (SWE) of NPR 7150.2, as well as information on software assurance, software safety requirements, and related topics. Users should also consult their NASA Center’s resources for specific local procedures and guidance.

For NASA users, the Software Engineering Handbook is available on the NEN from the Software Engineering Community of Practice homepage. This site offers additional guidance and information to software developers, including the Ask an Expert pick, a Contact List, a Document Repository, and much more. Frequent users may wish to add a direct bookmark to the NASA Software Engineering and Assurance Handbook, NASA-HDBK-2203 in their browser <https://swehb.nasa.gov>.

Here's an overview of each major section within the NASA Software Engineering and Assurance Handbook, NASA-HDBK-2203:

* A contains the Introduction.
* B contains the developed guidance for each institutional requirement in NPR 7150.2. These SWE descriptions are from Chapter 2 of NPR 7150.2. Each SWE guidance section provides stand-alone explanations and interpretive information about the implementation of the requirement. The guidance material includes hyperlinks for easy reference to related SWEs and Topics.
* C contains the developed guidance for each software project requirement in NPR 7150.2. Each SWE guidance section provides a stand-alone explanation and interpretive information about the implementation of the requirement. The guidance includes hyperlinks for easy reference to related SWEs and Topics. Each requirement in C also includes the software assurance steps and software safety requirements and guidelines.
* D contains special Topics, most in the form of essays, that are broader than any single SWE. Many of the special Topics take the form of "how-to" and instructional material for users seeking to improve their knowledge and practices in software engineering, software assurance, and software safety. The special topics help the user go beyond the minimum descriptions presented in each SWE. Topics are more expansive on particular ideas and contain additional instructions for developing and acquiring software.
* E contains a list of terms including acronyms used in the Handbook, listings of and references to software development and assurance tools used by the Centers, and a complete listing of Handbook references in a numerated References Table.
* F is a link to the Software Processes Across NASA (SPAN) repository accessible to NASA users only. This repository contains processes and process assets approved for use across the Agency.

Explanation of the SEARCH Box in the splash banner above: This utility allows the NASA Software Engineering and Assurance Handbook, NASA-HDBK-2203 user to interrogate the Handbook contents for particular items of interest.

In the handbook, each typical requirement, SWE, has seven sections:

* THE REQUIREMENT: This section is a restatement of the NPR 7150.2 requirement wording, including any Notes from either the requirement paragraph itself or any applicable note from Appendix C. This section also gives a tabular representation of the applicability to each software class [438](#_tabs-<p>4</p>).

* RATIONALE: This section provides useful information regarding the purpose of the requirement. Occasionally, historical information and references are included to support the rationale statement.

* GUIDANCE: This section provides information helpful for interpreting the requirement, its scope, its relationship to other SWE, associated best practices, and references to supporting materials (standards, guides, published technical papers, the NEN, and SPAN materials).

* SMALL PROJECTS: This section suggests implementation aids to small projects to help satisfy the SWE while accommodating the typically limited resources of time, funds, and personnel. The definition of a "small project" needs to be determined by the user.

This determination does not relieve a project from satisfying the requirements of the NPR. When small projects need to reduce the set of applicable software requirements due to constraints, consult the designated Center Software Technical Authority. NPR 7120.5 and the NASA Chief Engineer’s specific direction provide direction on tailoring the NPR 7120.5 requirements.

* RESOURCES: This section provides a listing of referenced and footnoted texts, documents found within publicly accessible NASA repositories and out on the web, and other useful documents (e.g., checklists and templates). The Handbook includes in the Resources sections listings of additional readings, i.e., useful items not specifically cited or linked to in the GUIDANCE section, but thought by the authors to contain educational or expanded discussions of the ideas covered in the SWE write-up. Also, this section usually includes a separate table listing of tools and items that will help the user satisfy the requirement (e.g., developer tools). The Handbook wiki links SWEs and tools through the use of a master [Tools table](/spaces/SWEHBVC/pages/50888844/Tools+Table). The Tools table provides websites for accessing the tool. It also lists the Center(s) that currently use the tool in case the reader wants to seek out the "experiences" of a current user of the tool. Readers are invited to submit their tools for candidate inclusion in the Tools table for the benefit of others around the Agency.

* LESSONS LEARNED (LL): This section contains references to the experiences of others involved in NASA software development activities as well as other industry and government development efforts. The majority are in the Public Lessons Learned library [439](#_tabs-<p>4</p>)  at the Office of the Chief Engineer (OCE). Some are derived from specialized projects or Center collections as well as from reputable industry and government groups. Occasionally a lesson has only indirect applicability to the requirement.

* SOFTWARE ASSURANCE: This section contains the software assurance and software safety steps and requirements needed to assure each engineering requirement, the software assurance and software safety products required for each requirement, the software assurance, and software safety metrics required for each requirement, and the software assurance and software safety guidance associated with each software assurance and software safety step and requirement.

Remember that the NPR 7150.2 is a requirements document. It uses "shall" exclusively to indicate requirements. Applicability of an NPR 7150.2 requirement applies per the NASA Software Classification, and the matrix in Appendix C (of the NPR). The handbook is not a requirements document, only an informational document.

Earlier versions of NPR 7150.2 made extensive use of the NPR's Notes sections to help with the interpretation of the SWE. This Handbook is intended to collaborate with and augment the current NPR Notes, and to include valuable guidance from previous versions of NPR 7150.2.

The Requirements Mapping Matrix (RMM) in NPR 7150.2 provides a list of the applicability of each software project requirement by the class of software. Associated with many of the entries in the RMM are one or more notes that modify the applicability of the requirement for a particular class. Since the handbook makes explicit mention of these modifiers in section 1 of the guidance for each requirement, SWE, an additional explanation for the modifiers is:

* X - Indicates an invoked requirement by this NPR consistent with Software Classification (ref. SWE-139). May be tailored with Technical Authority approval (ref. Chapter 2.2).
* Blank - Optional/Not invoked by this NPR.
* Center - Center Director or the Center Director’s designated Engineering Technical Authority, the Center Director's designated SMA Technical Authority, and the CHMO designated for Health and Medical Technical Authority. The CIO, or the designee, has institutional authority on all Class F software projects and has joint responsibility for the cybersecurity requirements in section 3.11 per the direction in the Requirements Mapping Matrix.
* CIO - The OCIO, or the designee Center CIO, has institutional authority on all Class F software projects and has joint responsibility for the cybersecurity requirements in section 3.11 per the direction in the Requirements Mapping Matrix.

Each requirement marked 'X' for the project's software classification(s) should be addressed in the Requirements Mapping Matrix. All requirements can be tailored per the guidance in this directive. Requirements that do not apply to a given project, such as the IV&V requirements, should be tailored out in the Requirements Mapping Matrix with justification.

Some general comments:

* Note that the SWE titles in the SWEHB may not always agree with those in the NPR. The SWEHB Development Team expanded the titles for some of the SWE to help distinguish between other similarly sounding SWE names (e.g., "bidirectional traceability").
* See the [Terms Table](/spaces/SITE/pages/16122079/Terms) for a complete list of definitions of unique terms used in the SWEHB.
* The referenced material listed in the Resources section is located on the NASA Headquarters NODIS site, e.g., NPRs, NPDs,  in NTSS [442](#_tabs-<p>4</p>), e.g., NASA standards, IEEE standards, or in other NASA sites, e.g., materials from the OCE, Public lesson learned sources; etc. Please note that many of the Agency or Center assets are subject to scheduled updates. While we will make every effort to link to the latest versions, editions, or documents, you may discover references that have broken links or require updating. We invite the community to submit requests for information via "Feedback" at <http://standards.nasa.gov/> and requests for changes to the Handbook via MSFC Form 4657, Change Request for a NASA Engineering Standard.
* The handbook uses citations to external sites and general web-hosted sites. While attempts were made to cite publicly available (i.e., "free") references, there may be an occasional reference that suggests the reader "buy" a copy. If you come across one of these, and you are a NASA user, try to access it through the NASA Technical Standards [442](#_tabs-<p>4</p>) site. This NASA site provides prepaid access to many external repositories through an Agency-wide agreement with the site.
* (Caveat: Since the web is a dynamic place, some references in the Resources section of the SWE may have been discontinued online or moved to another host by their owners.  While all references have been verified on internal Agency networks as well as external Virtual Private Network (VPN) access, the variances in firewall and VPN settings, permissions, and configurations may affect access to these references.)

# Title Material

|  |  |
| --- | --- |
| NASA TECHNICAL HANDBOOKNational Aeronautics and Space AdministrationWashington, DC  20546-0001 | NASA Software Engineering and Software Assurance HandbookNASA-HDBK-2203BApproved: March 08, 2022 Superseding NASA-HDBK-2203A |

## DOCUMENT HISTORY LOG

|  |  |  |  |
| --- | --- | --- | --- |
| **Status** | **Document Revision** | **Approval Date** | **Description** |
| Baseline | 1 | 02-28-2013 | Initial Release |
| Revision | A | 01-13-2017 | Major Handbook updated to address the NASA Software Engineering Requirements, NPR 7150.2B, changes.  Update the guidance topics. |
| Revision | B | 04-20-2020 | Major Handbook updated to address the NASA Software Engineering and Software Assurance Requirements, NPR 7150.2C, changes, and NASA-STD-8739.8 changes. The guidance, topics, objectives, and lessons learned are continually updated as needed. |
| Revision | C | 03-08-2022 | Major Handbook updated to address the NASA Software Engineering and Software Assurance Requirements, NPR 7150.2D, changes, and NASA-STD-8739.8 changes. The guidance, topics, objectives, and lessons learned are continually updated as needed. |

## FOREWORD

This NASA Technical Handbook is published by the National Aeronautics and Space Administration (NASA) as a guidance document to provide engineering information; lessons learned; possible options to address technical issues; classification of similar items, materials, or processes; interpretative direction and techniques; and any other type of guidance information that may help the Government or its contractors in the design, construction, selection, management, support, or operation of systems, products, processes, or services.

This NASA Technical Handbook is approved for use by NASA Headquarters and NASA Centers and Facilities.  It may also apply to the Jet Propulsion Laboratory and other contractors only to the extent specified or referenced in applicable contracts.

This wiki-based NASA Technical Handbook provides users and practitioners with guidance material for implementing the requirements of [NPR 7150.2, NASA Software Engineering Requirements](http://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2A) [083](#_tabs-<p>4</p>)  and the NASA Software Assurance and Software Safety Standard, NASA-STD-8739.8. The use of this Software Engineering and Software Assurance Handbook is intended to provide "best-in-class" guidance for the implementation of safe and reliable software in support of NASA projects. The NASA Software Engineering and Assurance Handbook, NASA-HDBK-2203 is a key component of the NASA Software community implementation of an Agency-wide plan to work toward a continuous and sustained software engineering and software assurance process and product improvement.

Requests for information should be submitted via "Feedback" at <http://standards.nasa.gov/>. Requests for changes to this NASA Technical Handbook should be submitted via MSFC Form 4657, Change Request for a NASA Engineering Standard.

|  |  |
| --- | --- |
|  |  |

# 4. Resources

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-059)

  [ISO/IEC 19770-5:2015(en) Information technology — IT asset management — Overview and vocabulary](https://www.iso.org/obp/ui/#iso:std:iso-iec:19770:-5:ed-2:v1:en "Click to open in new window")

  ISO/IEC 19770-5:2015(en), Information technology — IT asset management —
* (SWEREF-075)

  [Information technology — Vocabulary](https://www.iso.org/standard/63598.html "Click to open in new window")

  ISO/IEC 2382:2015, Information technology — Vocabulary, Replaces ISO/IEC 2382-20:1990,
* (SWEREF-076)

  [Systems and software engineering — Requirements for designers and developers of user documentation](https://www.iso.org/obp/ui/#iso:std:iso-iec:26514:ed-1:v1:en "Click to open in new window")

  ISO/IEC 26514:2008(en), Systems and software engineering — Requirements for designers and developers of user documentation
* (SWEREF-080)

  [Systems and software engineering — Requirements for testers and reviewers of information for users](https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:26513:ed-1:v1:en "Click to open in new window")

  ISO/IEC/IEEE 26513:2017(en), Systems and software engineering — Requirements for testers and reviewers of information for users
* (SWEREF-081)

  [NASA Security Program Procedural Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1600&s=1A "Click to open in new window")

  NPR 1600.1A, Office of Protective Services, Effective Date: August 12, 2013, Expiration Date: December 12, 2021
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-084)

  [Information technology — IT asset management —](https://www.iso.org/obp/ui/#iso:std:iso-iec:19770:-1:ed-3:v1:en "Click to open in new window")

  ISO/IEC 19770-1:2017(en); Part 1: IT asset management systems — Requirements,
* (SWEREF-085)

  [Acceptable Use of Government Office Property Including Information Technology](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2540&s=1I "Click to open in new window")

  NPD 2540.1I, Office of the Chief Information Officer, Effective Date: August 19, 2019, Expiration Date: August 19, 2024,
* (SWEREF-087)

  [NASA Security Policy (Revalidated on 4/2/2015 w/Change 1)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1600&s=2E "Click to open in new window")

  NPD 1600.2E, Office of Protective Services, Effective Date: April 28, 2004, Expiration Date: May 28, 2022
* (SWEREF-088)

  [Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf "Click to open in new window")

  NIST Special Publication 800-53, Revision 5, September, 2020, U.S. Department of Commerce,
* (SWEREF-090)

  [Risk Management Framework for Information Systems and Organizations, Revision 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf "Click to open in new window")

  NIST Special Publication 800-37, Revision 2, National Institute of Standards and Technology, December, 2018,
* (SWEREF-093)

  [Cloud Computing Synopsis and Recommendations](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-146.pdf "Click to open in new window")

  Special Publication 800-146, Badger, Grance, et. al., National Institute of Standards and Technology, May, 2012
* (SWEREF-099)

  [Release of sensitive information.](https://www.govinfo.gov/content/pkg/CFR-2013-title48-vol6/pdf/CFR-2013-title48-vol6-sec1852-237-73.pdf "Click to open in new window")

  NFS 1852.237–73,
* (SWEREF-102)

  [Access to Sensitive Information](https://www.law.cornell.edu/cfr/text/48/1852.237-72 "Click to open in new window")

  48 CFR § 1852.237-72,
* (SWEREF-150)

  [FEDERAL SOFTWARE LICENSES](https://www.gao.gov/assets/gao-14-413.pdf "Click to open in new window")

  GAO-14-413, Report to the Chairman, Committee on Homeland Security and Governmental Affairs, U.S. Senate, May 2014,
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-194)

  [Federal Acquisition Regulation; FAR Case 2005-014, SmartBUY](https://www.federalregister.gov/documents/2007/10/31/07-5405/federal-acquisition-regulation-far-case-2005-014-smartbuy "Click to open in new window")

  Federal Acquisition Regulation; FAR Case 2005-014, SmartBUY,  A Proposed Rule by the Defense Department, the General Services Administration, and the National Aeronautics and Space Administration on 10/31/2007
* (SWEREF-195)

  [Contract Terms and Conditions-Commercial Items](https://www.acquisition.gov/far/52.212-4 "Click to open in new window")

  FAR 52.212-4 Contract Terms and Conditions-Commercial Items, Effective Date: 2021-07/2021-09-10,
* (SWEREF-196)

  [CMMI® V2.0](https://stage.cmmiinstitute.com/cmmi "Click to open in new window")

  CMMI - Capability, Maturity Model, Integration, Version 2.0,  See your SEPG for a NASA licensed copy.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-229)

  [NASA Health and Medical Technical Authority (HMTA) Implementation,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=11A "Click to open in new window")

  NPR 7120.11A - Effective Date: September 08, 2020, Expiration Date: September 08, 2025
* (SWEREF-231)

  [120.16 - Foreign person.](https://www.govregs.com/regulations/expand/title22_chapterI_part120_section120.16 "Click to open in new window")

  22 CFR §120.16
* (SWEREF-258)

  [NASA Engineering Network, Software Engineering Community](https://nen.nasa.gov/web/software "Click to open in new window")

  Welcome to the Software Community. Software engineering is a core capability and a key enabling technology for NASA's missions and supporting infrastructure.  Software Community site covers topics such as software requirements, design, implementation, architecture, assurance, testing, training, tools, process improvement, best practices, software release, models and simulations, and software research and technology innovation.
* (SWEREF-262)

  [NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.](https://nen.nasa.gov/web/oce/ta "Click to open in new window")

  NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-330)

  [NASA Information Technology Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=7A "Click to open in new window")

  NPR 7120.7A, Effective Date: August 17, 2020, Expiration Date: August 17, 2025
* (SWEREF-361)

  [SPACE SYSTEM PROTECTION STANDARD](https://standards.nasa.gov/standard/NASA/NASA-STD-1006 "Click to open in new window")

   NASA-STD-1006A, Approved 7/15/2022,  PUBLIC: Upload Publicly Available Standard
  https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/2022-07-15-NASA-STD-1006A-Approved.pdf
* (SWEREF-363)

  [Quality Attributes for Mission Flight Software: A Reference for Architects](https://ntrs.nasa.gov/citations/20160005787 "Click to open in new window")

  Wilmot, Jonathan, Fesq, Lorraine, Dvorak, Dan, Conference Paper, Publication Date
  March 5, 2016, GSFC-E-DAA-TN30323,
* (SWEREF-406)

  [NASA Requirement Waivers.](http://nodis3.gsfc.nasa.gov/Waivers/Waiver_list.cfm "Click to open in new window")

  January, 2012. This is a list of the NASA Requirement Waivers. Instructions for submitting requirement waivers are outlined in Chapter 4 of NPR 1400.1, NASA Directives Procedural Requirements.
* (SWEREF-411)

  [IV&V Management System (IMS)](https://www.nasa.gov/centers/ivv/ims/home/index.html "Click to open in new window")

  NASA IV&V Facility.
* (SWEREF-438)

  [NASA Software Engineering Requirements, Appendix D,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002C_&page_name=AppendixD "Click to open in new window")

   NPR 7150.2C, Effective Date: August 02, 2019
* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-442)

  [NASA Technical Standards System](https://standards.nasa.gov/ "Click to open in new window")

  NASA users must LOGIN to fully access the NTSS.: https://standards.nasa.gov/
* (SWEREF-489)

  [NPD 1000.5,B, Policy for NASA Acquisition,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=5C "Click to open in new window")

  NPD 1000.5C, Policy for NASA Acquisition, Effective Date: July 13, 2020, Expiration Date: July 13, 2025
* (SWEREF-593)

  [NASA Internal Control (Revalidated w/Change 1, 07/21/2017)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1200&s=1E "Click to open in new window")

  NPD 1200.1E, Office of the Chief Financial Officer, Effective Date: July 21, 2008, Expiration Date: July 21, 2022,
* (SWEREF-594)

  [NASA Surveys, Audits, and Reviews Policy (Revalidated on10/24/2017)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1210&s=2 "Click to open in new window")

  NPD 1210.2, Office of the Chief Financial Officer, Effective Date: January 13, 2005, Expiration Date: October 24, 2023,
* (SWEREF-595)

  [Inventions Made By Government Employees](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2091&s=1C "Click to open in new window")

  NPD 2091.1C, Office of the General Counsel, Effective Date: May 24, 2018, Expiration Date: May 24, 2023,
* (SWEREF-597)

  [NASA Export Control Program](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2190&s=1C "Click to open in new window")

  NPR 2190.1C, NASA Procedural Requirements, Effective Date: September 08, 2017, Expiration Date: September 08, 2022
* (SWEREF-598)

  [Managing Information Technology](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2800&s=1E "Click to open in new window")

  NPD 2800.1E, Office of the Chief Information Officer, Effective Date: December 09, 2019, Expiration Date: December 09, 2024,
* (SWEREF-599)

  [Identity, Credential, and Access Management](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2841&s=1 "Click to open in new window")

  NASA Procedural Requirements, NPR 2841.1, Effective Date: January 06, 2011, Expiration Date: January 06, 2022, (Revalidated w/change 1)
* (SWEREF-600)

  [Technical Standards for NASA Programs and Projects](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=10A "Click to open in new window")

  NASA Procedural Requirements, NPR 7120.10A, Effective Date: February 21, 2017, Expiration Date: February 21, 2022
* (SWEREF-601)

  [Commercial computer software—Licensing](https://www.gpo.gov/fdsys/pkg/CFR-2005-title48-vol6/pdf/CFR-2005-title48-vol6-sec1852-227-86.pdf "Click to open in new window")

  48 CFR Ch. 18 (10–1–05 Edition) 1852.227–86
* (SWEREF-608)

  [Capital Asset Identification and Treatment](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=9250&s=1A "Click to open in new window")

  NPD 9250.1A, Effective Date: October 08, 2010, Expiration Date: October 08, 2024, NASA policy for property, plant, and equipment (PP&E)

# 5. Accessing Handbook Versions

The version of the handbook that you are viewing is noted in the header image. Clicking on this image, while on any page of the SWEHBVD, will take you back to the Introduction page for this version.

To access other versions of the Software Engineering Handbook use the links below:

* [Click here to go back to the Software Engineering Handbook from NPR 7150.2A](/spaces/7150/pages/16449762/Book+A.+Introduction)
* [Click here to go back to the Software Engineering Handbook from NPR 7150.2B](/spaces/SWEHBVB/pages/32604164/Book+A.+Introduction)
* [Click here to go back to the Software Engineering Handbook from NPR 7150.2C](/spaces/SWEHBVC/pages/50888752/Book+A.+Introduction)
* You are already in the Software Engineering and Software Assurance Handbook from NPR 7150.2D

Four versions of the NASA Software Engineering and Assurance Handbook, NASA-HDBK-2203 are available for use (see Tab 5 to access the versions of the handbook)

* The original version of the handbook - addresses the NASA Software Engineering Requirements in NPR 7150.2A. NPR 7150.2A had an effective date of November 19, 2009, to the expiration date of November 19, 2014.
* Revision A - addresses the NASA Software Engineering Requirements in NPR 7150.2B. NPR 7150.2B had an effective date of November 19, 2014, to the expiration date of August 2, 2019.
* Revision B - addresses the NASA Software Engineering Requirements in NPR 7150.2C and the requirements in the NASA Software Assurance and Software Safety standard, NASA-STD-8739.8A. NPR 7150.2C had an effective date of August 2, 2019, to the expiration date of August 2, 2024. NASA-STD-8739.8A [278](#_tabs-<p>4</p>) has an effective date of June 10, 2020.
* Revision C - Addresses the NASA Software Engineering Requirements in NPR 7150.2D, and the requirements in the NASA Software Assurance and Software Safety standard, NASA-STD-8739.8A. NPR 7150.2D had an effective date of 03/08/2022, to the expiration date of 03/08/2027. NASA-STD-8739.8B [278](#_tabs-<p>4</p>) has an effective date of June 10, 2020.
* ### **NPR 7150.2D is the latest version of the NASA Software Engineering Requirements.** **NASA-STD-8739.8B is the latest version of the NASA Software Assurance and Software Safety Standard**

  [278](#_tabs-<p>4</p>) has an effective date of September 8, 2022.

# 5.1 SWE History

**The SWE History Summary includes all SWE numbers and their history of use in all versions of the Software Engineering Handbook.**

Click [SWE History](/spaces/SWEHBVD/pages/102695267/SWE+History) to view.

# NASA-STD-8739.8B Title Material

| Status | Document Revision | Approval Date | Description |
| --- | --- | --- | --- |
| Baseline | Initial | 2004-07-28 | Initial Release |
|  | 1 | 2005-05-05 | Administrative changes to the Preface; Paragraphs 1.1, 1.4, 1.5, 2.1.1, 2.2.2, 3, 5.1.2.3, 5.4.1.1; 5.6.2, 5.8.1.2, 6.7.1.a, 7.3.2, 7.3.3, 7.5, 7.5.1; Table 1; Appendix A; Appendix C to reflect NASA Transformation changes, reflect the release of NASA Procedural Requirements (NPR) 7150.2, NASA Software Engineering Requirements and to make minor editorial changes. Note: Some paragraphs have changed pages as a result of these changes. Only pages where content has changed are identified by change indications. |
|  | A | 2020-06-10 | The revised document addresses the following significant issues: combined the NASA Software Assurance Standard (NASA-STD-8739.8) with the NASA Software Safety Standard (NASA-STD-8719.13), reduction of requirements, bring into alignment with updates to NPR 7150.2, added a section on IV&V requirements to perform IV&V, and moved guidance text to an Electronic Handbook. This change combines the updates to NASA-STD-8739.8 and the content of NASA-STD-8719.13. The update includes the NASA software safety requirements and cancels NASA-STD-8719.13 standard. |
|  | B | 2022-09-08 | Brings into alignment with the update to NPR 7150.2D. Update the Appendix A table containing the additional areas to consider when identifying software causes in Hazard Analysis. |

**DOCUMENT HISTORY LOG**

|  |  |
| --- | --- |
| Approved: TBD | Measurement System Identification: Not Measurement Sensitive |
| NASA TECHNICAL STANDARD  National Aeronautics and Space Administration | NASA-STD-8739.8B  Approved: 2022-09-08 Superseding NASA-STD-8739.8A |
| SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED |  |

## Forward

This NASA Technical Standard is published by the National Aeronautics and Space Administration (NASA) to provide uniform engineering and technical requirements for processes, procedures, practices, and methods that have been endorsed as standard for NASA facilities, programs, and projects, including requirements for selection, application, and design criteria of an item.  
This standard was developed by the NASA Office of Safety and Mission Assurance (OSMA). Requests for information, corrections, or additions to this standard should be submitted to the OSMA by email to [Agency-SMA-Policy-Feedback@mail.nasa.gov](mailto:Agency-SMA-Policy-Feedback@mail.nasa.gov) or via the “Email Feedback” link at <https://standards.nasa.gov>.

|  |  |
| --- | --- |
| William Deloach  NASA Chief, Safety and Mission Assurance | TBD  2022-09-08 |
