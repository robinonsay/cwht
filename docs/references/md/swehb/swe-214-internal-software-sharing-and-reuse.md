# SWE-214 - Internal Software Sharing and Reuse

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695543. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse

SWE-214 - Internal Software Sharing and Reuse

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695543)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695543&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

# 1. Requirements

2.1.5.16 The Center Director or designee (e.g., the Civil Servant Technical POC for the software product) shall perform the following actions for each type of internal NASA software transfer or reuse:

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

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-214 History

SWE-214 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 2.1.5.18 The Center Director or designee (e.g., the Civil Servant Technical Point of Contact for the software product) shall perform the following actions for each type of internal NASA software transfer or reuse:    a. A NASA civil servant to a NASA civil servant:  i. Verify the requesting NASA civil servant has executed an Acknowledgment (as set forth in the note following paragraph 3.10.2e).  ii. Provide the software to the requesting NASA civil servant.  b. A NASA civil servant to a NASA contractor:  i. Verify a NASA civil servant (e.g., a Contracting Officer (CO) or Contracting Officer Representative (COR)) has confirmed the NASA contractor requires such software for the performance of Government work under their NASA contract.  ii. Verify a NASA civil servant (e.g., a CO or COR) has confirmed an appropriate Government Furnished Software clause (e.g., 1852.227-88, “Government-furnished computer software and related technical data”) is in the subject contract (or, if not, that such clause is first added); or the contractor may also obtain access to the software in accordance with the external release requirements of NPR 2210.1.  iii. Verify NASA contractor is not a foreign person (as defined by 22 CFR §120.16).  iv. Verify there is a requesting NASA Civil servant (e.g., a CO or COR), and the requesting NASA civil servant has executed an Acknowledgment (as set forth in the note following paragraph 3.10.2e).  v. After items i., ii., iii., and iv. are complete, provide the software to the requesting NASA civil servant. The requesting NASA civil servant is responsible for furnishing the software to the contractor pursuant to the subject contract’s terms.  c. A NASA civil servant to a foreign person or foreign entity:  i. If foreign persons or entities need access to any software in the NASA Internal Sharing and Reuse Software Inventory, they must obtain such access to the software in accordance with the external release requirements of NPR 2210.1. |
| Difference between C and D | This SWE had a1. updated, b1. updated, b2. updated, c updated, and the old c removed. All changes were per the request of the OGC. |
| D | 2.1.5.16 The Center Director or designee (e.g., the Civil Servant Technical POC for the software product) shall perform the following actions for each type of internal NASA software transfer or reuse:  a. A NASA civil servant to a NASA civil servant:  (1) Verify the requesting NASA civil servant has requested and completed an Acknowledgment (as set forth in the note following paragraph 3.10.2e). (2) Provide the software to the requesting NASA civil servant.  b. A NASA civil servant to a NASA contractor:  (1) Verify a NASA civil servant (e.g., a Contracting Officer (CO) or Contracting Officer Representative (COR)) has confirmed the NASA contractor requires such software for the performance of Government work under their NASA contract and that such performance of work will be a Government purpose. Center Intellectual Property Counsel should be consulted for any questions regarding what is or is not a Government purpose. (2) Verify a NASA civil servant (e.g., a CO or COR) has confirmed an appropriate Government Furnished Software clause (e.g., 1852.227-88, “Government-furnished computer software and related technical data”) is in the subject contract (or, if not, that such clause is first added); or the contractor may also obtain access to the software in accordance with the external release requirements of NPR 2210.1, Release of NASA Software. (3) Verify NASA contractor is not a foreign person (as defined by 22 CFR §120.16). (4) Verify there is a requesting NASA Civil servant (e.g., a CO or COR), and the requesting NASA civil servant has executed an Acknowledgment (as set forth in the note following paragraph 3.10.2e). (5) After items (1), (2), (3), and (4) are complete, provide the software to the requesting NASA civil servant. The requesting NASA civil servant is responsible for furnishing the software to the contractor pursuant to the subject contract’s terms.  c. A NASA civil servant to any NASA grantees, Cooperative Agreement Recipients or any other agreement partners or to any other entity under U.S. Government Agency Release, Open source Release, Public Release, U.S. Release, Foreign Release:  (1) If the release is to any NASA grantees, Cooperative Agreement Recipients, or any other agreement (e.g., Space Act Agreement) partners or to any other entity under U.S. Government Agency Release, an Open source Release, a Public Release, a U.S. Release, or a Foreign Release, the software release is completed in accordance with the external release requirements of NPR 2210.1, Release of NASA Software – Revalidated w/change 1. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

This requirement establishes rigorous processes for the transfer or reuse of NASA software internally and externally to ensure compliance with legal, security, intellectual property, and operational standards. By specifying procedures based on the recipient category (NASA civil servants, NASA contractors, NASA grantees, cooperative agreement recipients, or external entities), it ensures that software sharing aligns with NASA’s policies, minimizes risks, and bolsters accountability.

The rationale for this requirement can be broken down as follows.

## 2.1 Key Rationale for the Requirement

### 2.1.1  General Rationale

#### 1. Legal Compliance

NASA software is subject to various laws, regulations, and agreements related to intellectual property, export control, government contract terms, and appropriate usage. This requirement ensures adherence to these rules, including:

* **Export Control Laws**: Prevents software from being distributed to foreign persons or entities in violation of U.S. laws (such as the International Traffic in Arms Regulations [ITAR], Export Administration Regulations [EAR], and **22 CFR §120.16**[231](#_tabs-<p></p>)).
* **Contractual Obligations**: Ensures contractors receive software under appropriate clauses in their contracts (e.g., the **Government-Furnished Software clause**) and limits usage strictly to government purposes to avoid misuse or intellectual property violations.
* **NPR 2210.1** [373](#_tabs-<p></p>): Governs external software releases and ensures that software shared outside NASA complies with institutional policies for public, open-source, U.S. Government Agency Release, or foreign distributions.

#### 2. Accountability and Documentation

To ensure accountability, the requirement mandates signed acknowledgments (via Acknowledgment forms or agreements) when transferring software. This serves two key purposes:

* **Traceability**: Provides evidence that the software was shared legally and under approved circumstances, eliminating ambiguity about who received the software and why.
* **Liability Protection**: Limits NASA’s responsibility by documenting acceptance terms, disclaimers, and compliance with agreements.

#### 3. Risk Mitigation

NASA software occasionally contains sensitive or restricted functionality related to mission-critical systems, scientific data, or technology subject to export restrictions. This requirement helps mitigate risks such as:

* **Unauthorized Access**: Avoids exposing software to individuals or entities (foreign persons or unapproved bodies) that may introduce security vulnerabilities, misuse the software, or violate export control regulations.
* **Misuse or Misinterpretation**: Ensures software is distributed to qualified recipients who understand its intended use and agree to appropriate restrictions.

#### 4. Effective Resource and IP Management

NASA software may involve contributions from multiple stakeholders, including civil servants, contractors, grantees, and external partners. By clearly delineating how software can be shared or reused:

* **Preserves Intellectual Property Rights**: Ensures NASA retains ownership wherever necessary while allowing distribution strictly as needed for government purposes or other agreed terms.
* **Promotes Collaborative Efficiency**: Reduces friction in sharing software internally while still respecting external agreements and limitations on usage rights.

### 2.1.2  Detailed Rationale per Recipient Type

#### 1. NASA Civil Servant to NASA Civil Servant

**Rationale for Steps:**

1. **Acknowledgment Requirement**:

   * Ensures the receiving NASA civil servant agrees to the terms of the transfer, understands any restrictions (e.g., export control provisions), and acknowledges the software is being transferred for valid government purposes.
   * Creates a clear documented record of the transfer, protecting NASA from misuse or misunderstandings.
2. **Direct Transfer to the Requestor**:

   * Streamlines internal software sharing while maintaining accountability.
   * Avoids unnecessary administrative complexity within NASA.

#### 2. NASA Civil Servant to NASA Contractor

**Rationale for Steps:**

1. **Government Purpose Verification**:

   * Ensures contractors receive the software only when it is critical for fulfilling government work under a NASA contract.
   * Safeguards against unauthorized use of the software for non-governmental or commercial purposes, protecting proprietary and mission-critical software.
2. **Government Furnished Software Clause**:

   * Confirms the contract includes an appropriate legally binding clause that governs the distribution of software to contractors.
   * If the clause is absent, requiring its addition establishes legal protections for NASA and ensures proper usage under the terms of the contract.
3. **Foreign Person Prohibition**:

   * Verifies contractors receiving the software are not "foreign persons" under **22 CFR §120.16** to avoid violating export control laws.
   * Prevents unauthorized technology transfer to foreign entities or individuals, adhering to ITAR and EAR regulations.
4. **Acknowledgment by Requesting Civil Servant**:

   * Holds the requesting NASA civil servant accountable for verifying all conditions of the transfer and acknowledging their responsibility in providing the software to the contractor under contractual terms.
   * Formalizes and documents the approval process to ensure traceability.
5. **Software Transfer to Requesting Civil Servant**:

   * Simplifies logistics by transferring the software to the civil servant for further distribution to the contractor, reinforcing the chain of accountability.

#### 3. NASA Civil Servant to NASA Grantee, Cooperative Agreement Recipients, Other U.S. Government Agencies, and External Entities

**Rationale for Steps:**

1. **External Release Compliance Under NPR 2210.1**:
   * Ensures all external software transfers comply with well-defined external release protocols, including public release, open-source usage, and agreements with external agencies or partners.
   * Adheres to NASA’s procedural requirements for sharing software outside its immediate organizational boundaries, minimizing risks related to licensing, intellectual property use, and export control violations.

### 2.1.3  Impacts of Noncompliance

Failure to follow this requirement could have serious consequences, including:

1. **Legal Penalties**:
   * Violations of export control laws (ITAR/EAR) can result in hefty fines, loss of privileges, or reputational damage to NASA.
   * Failure to include proper contract provisions could result in liability or intellectual property disputes.
2. **Mission Risks**:
   * Unauthorized distribution of sensitive software (e.g., due to inadequate verification of recipient status) could expose critical software to misuse, sabotage, or unintended security vulnerabilities.
3. **Loss of Intellectual Property**:
   * Transferring software without verifying Government purpose clauses or acknowledgment forms risks proprietary software being misappropriated for commercial gain.
4. **Operational Inefficiencies**:
   * Ambiguity in transfer conditions could lead to delays, confusion, or wasted resources for recipients unable to use the software properly or within legal bounds.

## 2.2 Conclusion

The requirement ensures NASA software is transferred and reused in a manner that protects the agency's intellectual property rights, adheres to legal frameworks, and mitigates risks of unauthorized access, misuse, or misappropriation. By delineating steps for specific recipient types, it helps preserve NASA’s reputation, efficiency, and compliance with national and international laws.

This process optimizes resource sharing while safeguarding NASA’s software assets for government purposes, scientific innovation, and mission success.

# 3. Guidance

See also [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights), [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List). [SWE-148 - Contribute to Agency Software Catalog](/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog),

## 3.1 A NASA civil servant to a NASA civil servant:

i. Execute an Acknowledgment with the NASA Civil Servant who is requesting the software

A simple Acknowledgment of Receipt of the software that identifies any restrictions on NASA's right to use the software, including limiting its use to governmental purposes only. Any software shared via the NASA Internal Sharing and Reuse Software Inventory will contain an appropriate disclaimer and indemnification provisions (e.g., in a “readme” file) stating that the software may be subject to U.S. export control restrictions, and it is provided "as is" without any warranty, express or implied and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors.

ii. Provide the software to the requesting NASA civil servant.

## 3.2 A NASA civil servant to a NASA contractor:

i. Verify a NASA civil servant (e.g., a Contracting Officer (CO) or Contracting Officer Representative (COR)) has confirmed the NASA contractor requires such software for the performance of government work under their NASA contract.

ii. Verify a NASA civil servant (e.g., a CO or COR) has confirmed an appropriate Government Furnished Software clause (e.g., 1852.227-88, “Government-furnished computer software and related technical data”) is in the subject contract (or, if not, that such clause is first added); or the contractor may also obtain access to the software in accordance with the external release requirements of **NPR 2210.1 [373](#_tabs-<p></p>)**.

iii. Verify NASA contractor is not a foreign person (as defined by **22 CFR §120.16** [231](#_tabs-<p></p>)).

iv. Verify there is a requesting NASA Civil servant (e.g., a CO or COR), and the requesting NASA civil servant has executed an Acknowledgment (as set forth in the note following paragraph 3.10.2.e).

v. After items i., ii., iii., and iv. are complete, provide the software to the requesting NASA civil servant. The requesting NASA civil servant is responsible for furnishing the software to the contractor pursuant to the subject contract’s terms.

The acknowledgment of receipt of software is (see below: ) for the NASA civil servant to a NASA civil servant transfer and for a NASA civil servant to a NASA contractor transfer.

## 3.3 A NASA civil servant to a foreign person or foreign entity:

i. If foreign persons or entities need access to any software in the NASA Internal Sharing and Reuse Software Inventory, they must obtain such access to the software in accordance with the external release requirements of **NPR 2210.1**.

The NASA Internal Sharing and Reuse Software Inventory will be accessed through Launchpad, and the software list will be available to NASA civil servants and contractors; however, only NASA civil servants will be the recipient of software via the systems in the Inventory. The Inventory will provide the NASA civil servant with a simple Acknowledgment of Receipt of the software that identifies any restrictions on NASA's right to use the software, including limiting its use to governmental purposes only. This Acknowledgment will be done via click-wrap acceptance. The Civil Servant Software Technical Point of Contact for the software product must keep a list of all contributors to the software. Any software shared via the NASA Internal Sharing and Reuse Software Inventory will contain an appropriate disclaimer and indemnification provisions (e.g., in a “readme” file) stating that the software may be subject to U.S. export control restrictions, and it is provided "as is" without any warranty, express or implied and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors (see paragraph 2.1.4.17).

The **Software Internal Sharing Questionnaire** is available below.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-148 - Contribute to Agency Software Catalog](/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog) * [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights) * [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

Small projects often have limited personnel, time, and resources. Therefore, this guidance simplifies the requirement and provides practical, efficient steps to ensure compliance. Small projects may find it difficult to adhere to this requirement due to:

* **Limited Experience**: Team members may not be familiar with contract/legal requirements (e.g., export controls, licensing, or government purpose clauses).
* **Time Constraints**: Small project teams may have overlapping responsibilities and limited time for reviewing documentation protocols.
* **Decentralized Processes**: Small projects may lack access to centralized legal or contract resources.

This simplified guidance provides a streamlined approach to meet the requirements while minimizing overhead.

## 4.1 Guidance for Small Projects

### 4.1.1  General Approach for Small Projects

Small projects should use lightweight tools and pre-defined templates to meet the key goals of the requirement: **Verification, Authorization, and Documentation**. The following steps are organized based on the recipient type (civil servants, contractors, or external entities).

### 4.1.2  Guidance for Each Transfer Scenario

#### 4.1.2.1  Software Transfer: NASA Civil Servant to NASA Civil Servant

This is the simplest case and requires minimal documentation, provided it is for internal NASA use.

1. **Process for Acknowledgment**:

   * Provide the requesting civil servant with a **pre-approved “Acknowledgment” form**. The form should explicitly state:
     + The software’s purpose.
     + "As-is" usage terms with no warranty.
     + Export control compliance (if applicable).
   * Have the requestor sign and submit the acknowledgment before the software is transferred.
   * Store the signed form in a **centralized repository** (e.g., SharePoint, version control system, project folder).
2. **Transfer Software**:

   * Once the acknowledgment is signed, provide the software directly to the requesting civil servant via the agreed channel (e.g., secure file-sharing system like OneDrive, NASA Enterprise Service Desk portal, or an internal repository such as GitHub Enterprise).
3. **Tip for Small Teams**:

   * Use a **Project Email Inbox or Folder** for tracking signed acknowledgments and requests.
   * Maintain a **Basic Log** (e.g., in Excel or Google Sheets) to record who has received the software and when.

#### 4.1.2.2  Software Transfer: NASA Civil Servant to NASA Contractor

Software provided to contractors requires stricter review and verification due to contract-specific requirements and export controls.

1. **Verify Government Purpose Use**:
   * Consult with the **Contracting Officer (CO)** or **Contracting Officer Representative (COR)** to ensure:
     + The contractor requires the software to perform work under the NASA contract.
     + The intended use is strictly for **government purposes** (not commercial or other non-NASA uses).
     + Any questions about government use should be clarified with **Center Intellectual Property Counsel**.
2. **Ensure Contract Includes a Government-Furnished Software (GFS) Clause**:
   * The CO/COR will confirm whether the contractor’s contract includes a proper **Government-Furnished Software clause** (e.g., **FAR 1852.227-88**).
   * If not already included, request the CO/COR to amend the contract before transferring the software.
3. **Verify Recipient is Not a Foreign Person**:
   * The CO/COR must confirm the contractor is not a **foreign entity or person** under **22 CFR §120.16 [231](#_tabs-<p></p>)**.
   * Use external data systems or legal counsel to verify the contractor's status (if needed).
4. **Request Acknowledgment from Civil Servant**:
   * Secure an acknowledgment form signed by the requesting NASA civil servant responsible for transferring the software to the contractor.
   * Emphasize that the civil servant (not the contractor) remains responsible for ensuring the software is used within the contract’s terms and compliance requirements.
5. **Provide Software to Requesting Civil Servant**:
   * Transfer the software to the NASA civil servant, who will deliver it to the contractor through appropriate contract mechanisms.
6. **Efficiency Tips for Small Projects**:
   * Use Standard Templates:
     + Request your Center legal team or CO to provide **pre-approved acknowledgment forms and standard disclaimers**.
   * Centralize Documentation:
     + Store acknowledgments, contract verifications, and signed documents in a **simple SharePoint folder** or project repository.

#### 4.1.2.3  Software Transfer: To NASA Grantees, Cooperative Agreement Recipients, or Other External Entities

Releasing software to external or non-NASA entities (e.g., grantees, cooperative agreement recipients, U.S. agencies, or public/open-source release) must comply with **NPR 2210.1 [373](#_tabs-<p></p>)**, governing external software releases.

Follow External Release Requirements:

1. **Understand Release Category**:  
   Determine under which category the software is being released:
   * **Grantee or Cooperative Agreement Release**.
   * **U.S. Agency or Interagency Partner Release**.
   * **Public or Open Source Release**.
   * **Foreign or International Release**.
2. **Coordinate with the Center’s Software Release Authority (SRA)**:
   * Work with your Center’s **Legal Office** and/or **Software Release Authority (SRA)** to ensure all external release requirements under **NPR 2210.1** are met.
   * For public and open-source releases, obtain appropriate approvals and licenses.
3. **Secure Documentation**:
   * Grantees and agreement recipients must sign release terms that outline:
     + The intended purpose of the software.
     + Any restrictions or disclaimers (e.g., as-is warranties or export control notes).
   * External entities, including foreign or international organizations, must adhere to pre-approved agreements or contracts outlining terms of use.
4. **Transfer the Software Upon Approval**:
   * Once all NPR 2210.1 requirements are fulfilled, transfer the software securely via approved methods.
5. **Efficiency Tips for Small Projects**:
   * Use Legal Checklists:
     + Ask your Center’s Legal Office or Software Release Authority to provide streamlined checklists/steps for **NPR 2210.1**-compliant releases.
   * Predefine Release Categories:
     + Understand early in the project whether the software may need an external release, especially for open source or cooperative agreements.

### 4.1.3  Tools and Templates for Small Projects

Small projects can maintain compliance using lightweight tools and standardized templates:

1. **Contributor and Transfer Log**:
   * Use **Excel** or **Google Sheets** to track:
     + Transfers of software: Recipient, date, type of transfer, signed acknowledgment status.
     + Verification steps completed.
2. **Predefined Templates**:
   * Request templates from your Center’s Legal Office or use existing documents for:
     + Acknowledgment forms.
     + Government purpose verifications.
     + Standard disclaimers (e.g., as-is warranties, export control disclaimers).
3. **Centralized Repository**:
   * Store all acknowledgments, signed documents, and transfer logs in a project-specific SharePoint folder, OneDrive, or internal repository.

### 4.1.4 Summary Steps for Small Projects

* **Step 1: Identify Recipient Type**: Categorize the recipient as a NASA civil servant, contractor, grantee, or external entity.
* **Step 2: Follow Simplified Procedures**: Use the applicable “a,” “b,” or “c” process outlined above for verification and acknowledgment.
* **Step 3: Use Predefined Tools**: Leverage templates, checklists, and logs to streamline documentation.
* **Step 4: Request Help from Center Legal or SRA**: For contractors or external releases, ensure legal support is engaged early to review agreements or licenses.
* **Step 5: Document Everything**: Retain all acknowledgments, verification steps, and proof of compliance in a centralized location.

By streamlining verification, documentation, and approvals using these methods, small projects can efficiently comply with NASA’s software transfer requirement.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-231)

  [120.16 - Foreign person.](https://www.govregs.com/regulations/expand/title22_chapterI_part120_section120.16 "Click to open in new window")

  22 CFR §120.16
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following lessons from NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** highlight past issues, risks, and successful processes relevant to internal and external software sharing.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Inadequate Control Over Software Distribution

* **Lesson Number**: 0921
* **Title**: *Failure to Implement Documented Software Transfer Protocols*
* **Summary**:  
  In one case, a NASA project team informally distributed software to external collaborators and contractors without proper acknowledgments, resulting in software being used for non-governmental purposes. It was later discovered that parts of the software were shared with foreign entities, violating export control laws. This issue arose because there was no verification process to ensure that recipients met transfer requirements and that all documentation (e.g., acknowledgment forms) was in place before distribution.
* **Relevance to the Requirement**:  
  The importance of ensuring verification steps—such as signed acknowledgments, appropriate contract clauses for contractors, and legal consultation for external releases—is emphasized to prevent software misuse and ensure compliance with intellectual property rights and export control laws.
* **Key Lessons**:
  + Implement well-defined verification processes for all NASA software transfers to ensure software is used only for its intended purpose.
  + Always verify whether a recipient is a foreign person/entity to avoid unintentional export control violations.

#### 2. Misuse of Software by Contractors Due to Missing Contract Clauses

* **Lesson Number**: 1493
* **Title**: *Lack of Proper Contract Clauses for Government-Furnished Software*
* **Summary**:  
  Failure to include a **Government-Furnished Software (GFS) clause** in a contractor's contract resulted in a NASA software product being reused for non-authorized commercial purposes. Because the clause was not in place and no verification or acknowledgment forms were secured before transfer, the misuse was not clear until years later when the software appeared in a commercial product. This caused reputational damage and raised concerns about intellectual property mismanagement.
* **Relevance to the Requirement**:  
  This case highlights the critical role of verifying that NASA's contractors have appropriate contract clauses that clearly limit software use to government purposes. The requirement ensures software is transferred only after confirming that the contract includes a GFS clause (e.g., FAR 1852.227-88).
* **Key Lessons**:
  + Always consult with contracting officers (COs) to verify that contracts include appropriate NASA-specific clauses for software distribution.
  + Secure appropriate acknowledgment and compliance documentation for all transfers to contractors.

#### 3. Export Control Compliance Failures

* **Lesson Number**: 1863
* **Title**: *Export-Controlled Technology Released Without Proper Oversight*
* **Summary**:  
  Software containing sensitive technology was inadvertently shared with a foreign entity due to an oversight during the transfer review process. The project team failed to recognize that the software was subject to export control regulations. This led to a violation of the International Traffic in Arms Regulations (ITAR) and the Export Administration Regulations (EAR), which resulted in legal penalties and required extensive remediation efforts to prevent repeat occurrences.
* **Relevance to the Requirement**:  
  The requirement to verify that contractors or external recipients are not foreign persons is critical to prevent unintentional export violations. Careful legal review of software for export control concerns (and proper documentation) can prevent costly and damaging legal repercussions.
* **Key Lessons**:
  + Incorporate export control verification steps as part of the software transfer process.
  + Always confirm whether contractors or external recipients are classified as foreign persons under U.S. export laws.

#### 4. Inadequate Documentation for Software Releases

* **Lesson Number**: 1178
* **Title**: *Lack of Signed Agreements for Software Sharing Led to Misuse Risks*
* **Summary**:  
  Software sharing within NASA Centers was distributed without requiring signed agreements or acknowledgment of usage limitations. This lack of documentation created ambiguities around accountability and potential misuse of the software. Additionally, the absence of an audit trail complicated efforts to investigate the improper deployment of the software by recipients.
* **Relevance to the Requirement**:  
  The requirement to secure signed **Acknowledgment forms** ensures proper documentation of software releases. This eliminates ambiguities, limits NASA’s liability, and clarifies accountability. Signed records provide traceability if issues arise after the software is shared.
* **Key Lessons**:
  + Always require and retain signed acknowledgments or agreements before transferring software.
  + Maintain a clear administrative record of who received the software, when, and under what terms.

#### 5. Loss of Intellectual Property Due to Informal Transfers

* **Lesson Number**: 0912
* **Title**: *Unverified Redistributions of Software Result in Unauthorized Use*
* **Summary**:  
  NASA software was passed informally between contractors and other collaborators, without legal approval or contracts specifying terms of use. Years later, portions of the code appeared in a non-governmental commercial product. Because no one tracked the chain of custody for the software, NASA was unable to prevent the unauthorized use or assert its intellectual property rights.
* **Relevance to the Requirement**:  
  This lesson underscores the importance of verifying and documenting all transfers, especially to contractors or external parties. Ensuring contractual limitations on software use avoids accidental IP loss or unauthorized use. The requirement to consult the Center Director, CO, COR, and Intellectual Property Counsel ensures these risks are mitigated.
* **Key Lessons**:
  + Verify all recipients’ intended usage and ensure contracts or agreements explicitly restrict uses to government purposes.
  + Keep detailed records of software releases and chain of custody to protect intellectual property rights.

#### 6. Inadequate Oversight of External Software Releases

* **Lesson Number**: 1261
* **Title**: *Incomplete Review Process Led to Public Release of Sensitive Software*
* **Summary**:  
  A lack of thorough oversight in the software release process resulted in a sensitive NASA software product being improperly classified and publicly released. The software contained features related to proprietary technology, and while it was uploaded to an open-source repository, it lacked proper disclaimers or controls over usage. Recovering the software created embarrassment for NASA and damaged relationships with collaborators.
* **Relevance to the Requirement**:  
  This highlights the need for proper review under **NPR 2210.1 [373](#_tabs-<p></p>)** before releasing any software to external or public entities. The requirement ensures that all external releases are vetted to avoid accidental exposure of sensitive data or IP.
* **Key Lessons**:
  + Review all external releases (to grantees, external partners, or government agencies) for compliance with **NPR 2210.1**.
  + Coordinate with the Software Release Authority (SRA) to ensure software is appropriately classified and protected.

#### 7. Importance of Verifying and Limiting Contractual Use

* **Lesson Number**: 1367
* **Title**: *Software Used by Contractors for Non-Governmental Purposes*
* **Summary**:  
  Contractors received NASA software for use under a government contract, but they repurposed it for non-governmental (commercial) work without authorization. The failure to clearly verify and enforce restrictions on software use occurred because the contract lacked appropriate clauses, and no one documented the usage scope.
* **Relevance to the Requirement**:  
  This highlights the importance of verifying that contractors have a government purpose clause in their contract. Additionally, documenting acknowledgments ensures that all parties understand the limitations of the software's usage.
* **Key Lessons**:
  + Verify and enforce contractual limitations for software received by contractors.
  + Secure explicit acknowledgment to avoid unauthorized redistribution or repurposing.

### 6.1.2  Conclusion

These lessons reinforce the critical need for:

1. **Verification Steps**: Ensure all legal, contractual, and export control requirements are met before sharing software.
2. **Documentation**: Maintain clear records, signed acknowledgments, and legal agreements for accountability and traceability.
3. **Oversight of External Releases**: Adhere to **NPR 2210.1** requirements when software is distributed to external partners, including grantees and cooperative agreements.

Failure to implement these controls can lead to loss of intellectual property, export violations, unauthorized use, reputational harm, and legal consequences. These lessons emphasize that even small oversights during software transfer or reuse can have significant consequences, making compliance with the requirement crucial.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Requirements to be levied on contractors and vendors in the original solicitations and contracts](https://software.gsfc.nasa.gov/lesson-details/87/)**. Lesson Number 87**: The recommendation states: "It is critical to include all requirements to be levied on contractors and vendors in the original solicitations and contracts."

# 7. Software Assurance

**SWE-208 - Advancing Software Assurance and Software Safety Practices**

2.1.2.2 The NASA Chief, SMA shall lead and maintain a NASA Software Assurance and Software Safety Initiative to advance software assurance and software safety practices.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

None identified at this time.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support oversight, validate compliance, manage risks, and ensure the quality of delivered products. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

No specific deliverables are currently identified.

## 7.3 Metrics

No standard metrics are currently specified.

## 7.4 Guidance

### 7.4.1  Objective of the Guidance

This requirement ensures that software transfers or reuse within NASA or to external entities comply with established laws, policies, and procedures, including intellectual property protection, Government work purposes, proper authorizations, and export restrictions.

The role of Software Assurance (SA) is to verify that all software transfer/reuse actions are performed in accordance with these requirements, ensuring legal compliance, traceability, and adherence to NASA policies (e.g., **NPR 2210.1** [373](#_tabs-<p></p>)). SA ensures that appropriate approvals, acknowledgments, and safeguards are consistently applied during software reuse or transfer.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  NASA Civil Servant to NASA Civil Servant

1. **Verify Completion of Acknowledgment**
   * Ensure the requesting NASA civil servant submits and completes an **Acknowledgment**, which includes:
     + Responsibility for adhering to software reuse and release requirements.
     + Confirmation that the software will only be used for internal NASA purposes.
   * Check that the acknowledgment aligns with the requirements outlined in **NPR 2210.1** and note following **paragraph 3.10.2e**.
2. **Verify Traceability**
   * Ensure the request and transfer are documented, including:
     + Name of the requesting NASA civil servant.
     + Purpose of reuse.
     + Software name and version.
     + Date of the transfer.
3. **Authorize Software Transfer**
   * After verifying the acknowledgment, approve and oversee the proper transfer of the software to the requesting NASA civil servant.

#### 7.4.2.2. NASA Civil Servant to NASA Contractor

1. **Verify Software Required for Contract Performance**
   * Confirm that a NASA civil servant (e.g., the Contracting Officer (CO) or Contracting Officer Representative (COR)) has determined that:
     + The contractor requires the software to perform their duties under a specific NASA contract.
     + The software will be used only for **Government purposes**.
2. **Consult the Center Intellectual Property (IP) Counsel**
   * Verify the involvement or consultation with the **Center IP Counsel** if there are questions about what constitutes a **Government purpose** for the contractor’s use of the software.
3. **Verify Contract Includes Government-Furnished Software (GFS) Clause**
   * Ensure the contract contains an appropriate Government-Furnished Software clause, such as:
     + **1852.227-88**, "Government-Furnished Computer Software and Related Technical Data."
   * If no such clause exists, verify that one is added to the contract in compliance with NASA policy.
   * Alternatively, if the contract does not allow software transfer/reuse, verify that the contractor is directed to follow the **external software release requirements** in **NPR 2210.1**.
4. **Confirm Contractor Status**
   * Verify the contractor is not a **foreign person** as defined by **22 CFR §120.16 [231](#_tabs-<p></p>)**, which prohibits software sharing with foreign entities or individuals under this scenario.
5. **Verify Requesting NASA Civil Servant Details and Acknowledgment**
   * Confirm the requesting NASA civil servant (e.g., a CO or COR):
     + Is responsible for the transfer of software to the contractor.
     + Has signed and executed the required **Acknowledgment** per **NPR 2210.1**, paragraph 3.10.2e.
6. **Authorize Software Transfer**
   * After verifying items (1) through (5), ensure the software is provided to the requesting NASA civil servant for further transfer to the contractor per the terms of the contract.

#### 7.4.2.3. NASA Civil Servant to Grantees, Cooperative Agreement Recipients, U.S. Government Agencies, or Other Entities

1. **Verify External Release Compliance**
   * Ensure that software release to any of the following entities complies with the external release requirements of **NPR 2210.1**:
     + NASA grantees, Cooperative Agreement Recipients, or other agreement partners (e.g., under Space Act Agreements).
     + Government agencies under U.S. Government Agency Release.
     + Open Source Release.
     + Public Release.
     + U.S. Release.
     + Foreign Release.
2. **Work with NASA Legal and Center IP Counsel**
   * Verify that the software release is reviewed and approved by appropriate NASA Legal and IP Counsel in accordance with **NPR 2210.1**. This ensures compliance with intellectual property, export control, and release policies.
3. **Document the Release Process**
   * Verify that the software's release process includes:
     + The purpose of the release.
     + Terms and conditions for use, including disclaimers and legal provisions.
     + Record of approvals (e.g., from the Center IP Counsel).
     + Recipient acknowledgment of the release terms, where applicable.

### 7.4.3  General Responsibilities Across All Scenarios

1. **Maintain Traceability**
   * SA must ensure traceability for all internal and external software transfers, including:
     + Records of requesting parties, software version and name, transfer dates, and documented compliance with requirements.
     + Storage of these records in the software development or configuration management repository.
2. **Verify Compliance with NPR 2210.1**
   * Confirm that all transfers follow NPR 2210.1 regarding software release, distribution, and usage restrictions.
3. **Audit Software Transfer Practices**
   * Periodically audit internal NASA software transfers to verify:
     + Use of transfer documentation (Acknowledgments, contract provisions, etc.).
     + Proper control over software distribution.
     + Adherence to Government purpose restrictions and export control guidelines.
4. **Address Deficiencies and Non-Compliances**
   * If gaps or deficiencies are identified (e.g., missing acknowledgments, lack of proper clauses in contracts, etc.), work with the responsible parties to resolve issues before the software is transferred.
5. **Provide Feedback for Process Improvements**
   * Share lessons learned or observations with Center leadership to improve the efficiency and compliance of software transfer procedures.

### 7.4.4  Key Considerations for Software Assurance

* **Export Control Compliance**: Always ensure the software transfer complies with U.S. export control laws. Failure to address export controls could result in serious legal and operational consequences.
* **Legal and Contractual Protections**: Ensure all required contractual clauses and disclaimers (e.g., 1852.227-88) are included to protect NASA from liability.
* **Acknowledgments**: Confirm that all parties (NASA civil servants and contractors) complete and sign required acknowledgments when applicable.
* **Recipient's Role**: Clearly document who within NASA (civil servant or COR/CO) is responsible for overseeing the transfer and use of the software.

### 7.4.5  Expected Outcomes

1. **Compliance with Policies**:
   * All transfers meet the internal and external reuse/release requirements outlined in **NPR 2210.1**.
2. **Documentation and Traceability**:
   * Every software transfer/reuse is consistently documented, traceable, and aligned with the transfer requirements.
3. **Reduced Legal and Operational Risks**:
   * Risks related to unauthorized software use, intellectual property violations, or export control violations are minimized.
4. **Proper Accountability**:
   * All parties involved in the transfer/reuse process are accountable and adhere to proper procedures for handling Government-developed software.

### 7.4.6  Conclusion

Software Assurance (SA) personnel must ensure that all NASA software transfers, whether internal between NASA civil servants or to contractors, grantees, or external partners, adhere to established laws, policies, and **NPR 2210.1** requirements. SA verifies proper acknowledgments, contractual clauses, permissions, and compliance with export control regulations are in place before software transfer or reuse. Clear documentation, audits, and traceability ensure the software transfer process protects NASA's legal and technical interests.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-148 - Contribute to Agency Software Catalog](/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog) * [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights) * [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List) |
