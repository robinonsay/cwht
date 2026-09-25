# SWE-218 - Contracting Officers

> NASA Software Engineering Handbook (SWEHB Ver D), page id 104497843. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/104497843/SWE-218+-+Contracting+Officers

SWE-218 - Contracting Officers

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/104497843/SWE-218+-+Contracting+Officers#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=104497843)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=104497843&showCommentArea=true&showComments=true#addcomment)

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

2.1.7.1 Contracting Officers, as defined in FAR 2.101, or Agreement Managers as defined in NAII 1050.3, NASA Partnership Guide, in conjunction with Program/Project Managers shall ensure that the appropriate FAR, NFS, and other provisions/clauses based on this requirements document and NASA-STD-8739.8 are included for all NASA contracts, Space Act Agreements, cooperative agreements, partnership agreements, grants, or other agreements pursuant to which software is being acquired, developed, modified, operated, or managed for NASA.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-218 History

SWE-218 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | New |
| D | 2.1.7.1 Contracting Officers, as defined in FAR 2.101, or Agreement Managers as defined in NAII 1050.3, NASA Partnership Guide, in conjunction with Program/Project Managers shall ensure that the appropriate FAR, NFS, and other provisions/clauses based on this requirements document and NASA-STD-8739.8 are included for all NASA contracts, Space Act Agreements, cooperative agreements, partnership agreements, grants, or other agreements pursuant to which software is being acquired, developed, modified, operated, or managed for NASA. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

Ensure that the appropriate FAR, NFS, and other provisions/clauses based on this requirements document and NASA-STD-8739.8 are included for all NASA contracts, Space Act Agreements, cooperative agreements, partnership agreements, grants, or other agreements pursuant to which software is being acquired, developed, modified, operated, or managed for NASA.

### **Purpose of the Requirement**

This requirement ensures that all agreements and contracts involving software-related work for NASA include appropriate provisions to:

1. **Comply with Federal and NASA Standards**: Ensure that software development, acquisition, and management align with federal regulations (e.g., FAR and NFS) and NASA-specific standards (e.g., NASA-STD-8739.8: Software Assurance Standard).
2. **Protect NASA's Intellectual Property (IP), Mission Goals, and Legal Rights**: The inclusion of appropriate clauses ensures that software developed or managed under NASA contracts is clearly governed to retain agency ownership, adhere to licensing obligations, and safeguard against unauthorized use.
3. **Ensure Quality and Accountability**: By embedding the correct provisions/clauses in agreements, NASA establishes enforceable requirements for quality assurance, validation, and compliance with technical, safety, and security standards.
4. **Mitigate Risks**: Comprehensive contractual language reduces vulnerabilities in areas such as liability, software security, export control, and unauthorized reuse.

---

### **Detailed Rationale by Key Objectives**

#### **1. Compliance with Federal and NASA Regulations**

NASA operates within the framework of federal laws, including the Federal Acquisition Regulations (FAR), NASA FAR Supplement (NFS), and agency-specific policies. Ensuring appropriate contractual clauses and standardized provisions fulfills critical regulatory requirements.

* **FAR Compliance**: Critical FAR clauses, applicable to software acquisition, development, and management, must be incorporated to comply with governing federal policies for contract administration. For example:
  + **FAR 52.227-14** (Rights in Data – General): Establishes obligations for protecting NASA's rights to software data.
  + **FAR 52.246-9** (Inspection of Research and Development): Helps ensure contractual requirements for software quality.
* **NFS Compliance**: NASA FAR Supplement clauses incorporate NASA-specific requirements (e.g., NFS 1852.227-88, Government-Furnished Software), further ensuring contracts reflect agency priorities and practices.
* **NASA Standards**: NASA's Software Assurance Standard (**NASA-STD-8739.8**) outlines technical oversight mechanisms to ensure software meets reliability, performance, and security requirements. Incorporating these standards contractually builds accountability.

#### **2. Protection of NASA Intellectual Property (IP) and Mission-Critical Software**

NASA often engages contractors, collaborators, and grantees to acquire or develop mission-critical software. Proper contractual provisions protect NASA's ownership, usage rights, and intellectual property from misuse or misappropriation.

* **Ownership Rights**: Without appropriate clauses, there is a risk of ambiguity regarding who owns the developed software—NASA or the contractor. Explicit clauses (e.g., FAR 52.227-14 or FAR 52.227-11) establish ownership and restrict unauthorized commercial reuse.
* **Government Purpose Licenses**: When software is provided under a partnership or cooperative agreement, terms must ensure its usage aligns with NASA's mission and isn't exploited for purposes outside the government’s interest.
* **Export Control Compliance**: Contracts must restrict access to software subject to export control laws (e.g., ITAR and EAR). Incorporating provisions directly addresses and mitigates legal risks.

#### **3. Quality Assurance and Accountability**

Software projects involve risks related to performance, reliability, security, and compatibility with mission objectives. This requirement ensures contracts incorporate provisions that enforce NASA's standards for quality assurance and accountability.

* **NASA-STD-8739.8**: NASA's Software Assurance Standard provides procedural guidance on software validation, testing, and compliance. Requiring this standard in contracts ensures contractors and partners follow these processes.
* **Technical Oversight**: Provisions ensure deliverables undergo adequate reviews, inspections, and testing by NASA oversight teams, reducing vulnerabilities related to defects or substandard quality.

#### **4. Mitigation of Financial, Legal, and Operational Risks**

Incorporating appropriate clauses in agreements prevents issues like cost overruns, legal disputes, or operational delays. Risks may arise from inadequate protection or misunderstandings of the agreements governing software development.

* **Liability Mitigation**: Contracts must include terms limiting NASA’s liability for software-related risks while holding contractors accountable for defects or failure to meet agreed-upon standards.
* **Security and Data Management**: Provisions ensure that software developed for NASA adheres to cybersecurity requirements, reducing risks of vulnerabilities, hacking, or data breaches.
* **Avoiding Rework and Delays**: Properly enforced contractual requirements prevent scope creep, miscommunication, or deliverables that fail NASA's expectations, reducing cost and schedule risks.

---

### **Key Stakeholder Responsibilities**

The requirement emphasizes collaboration among **Contracting Officers (COs)**, **Agreement Managers**, and **Program/Project Managers** to ensure software-related agreements comply with all necessary standards.

* **Contracting Officers and Agreement Managers**: Responsible for crafting the legal language (e.g., FAR clauses, NFS clauses) and ensuring contracts fully address software-specific requirements.
* **Program/Project Managers**: Provide operational and technical oversight to ensure requirements align with mission goals and technical standards (e.g., NASA-STD-8739.8). Their role is critical for ensuring contractors or partners deliver software that meets reliability and functional needs.

---

### **Impact of Poorly Managed Contracts**

Failure to incorporate appropriate contractual provisions and clauses can lead to:

1. **Software Mismanagement Risks**:
   * Improper licensing agreements or lack of clear IP ownership clauses may lead to disputes, unauthorized commercialization, or the inability to reuse software for other NASA projects.
2. **Legal Noncompliance**:
   * Missing export control provisions or improper security and access terms for sensitive software may result in violations of ITAR, EAR, or other regulations. These violations can lead to fines, penalties, or reputational damage.
3. **Quality and Operational Failures**:
   * Poorly crafted agreements may omit requirements for testing, validation, and verification, leading to subpar deliverables or software that isn’t mission-ready.
4. **Cost/Schedule Overruns**:
   * Ambiguity or lack of specificity in contracts can result in misaligned expectations, scope creep, and delays requiring costly rework.

---

### **Benefits of Compliance with This Requirement**

1. **Clarity and Consistency**:

   * Standardized clauses ensure all contracts aligned with software-related activities have clear terms for licensing, assurance, and risk management.
2. **IP Protection and Secured Rights**:

   * NASA retains control over developed software and establishes clear boundaries for how contractors, collaborators, or other entities might use that software.
3. **Technical Quality and Assurance Oversight**:

   * Incorporation of NASA-STD-8739.8 ensures deliverables meet strict reliability and safety/mission-critical standards.
4. **Risk Avoidance**:

   * Proper clauses address concerns like export control laws, unauthorized commercialization, operational vulnerabilities, and liability issues.

---

### **Why This Requirement is Critical for NASA**

Software is integral to NASA’s missions, ranging from advanced modeling and analysis tools to embedded systems for spacecraft and robotics. Ensuring contracts or agreements governing software include appropriate provisions and clauses helps NASA maintain a high standard of performance, accountability, and legal compliance. By addressing intellectual property, technical oversight, and risk mitigation through contractual language, the agency secures its position as a leader in innovation while protecting its mission objectives and resources.

This requirement ultimately establishes a robust foundation for managing software-related projects with government entities, contractors, and external collaborators, ensuring clarity, accountability, and compliance at all levels.

# 3. Guidance

### **Introduction**

All contracts, grants, cooperative agreements, and other types of partnerships related to the development, acquisition, modification, or management of software for NASA must include appropriate **Federal Acquisition Regulation (FAR)**, **NASA FAR Supplement (NFS)**, and agency-specific clauses. This ensures compliance with legal, technical, and intellectual property requirements while protecting the Government's rights and mission objectives.

This guidance provides a structured approach for Contracting Officers, Agreement Managers, and Program/Project Managers to incorporate the necessary contractual provisions for software-related activities, with a focus on FAR, NFS, and NASA-STD-8739.8 (Software Assurance).

## 3.1. Collaborating with the Contracting Officer

* Work closely with the **Contracting Officer (CO)** or **Agreement Manager** to determine which FAR, NFS, and custom clauses are appropriate for the scope of work. The CO is responsible for ensuring compliance with acquisition laws and regulations.
* Access the Federal Acquisition Regulations at **[acquisition.gov](https://www.acquisition.gov/)** to browse clauses. Use keywords like "*software*", "*data rights*", "*technical data*", and "*intellectual property*" to identify relevant clauses.

## 3.2. Understanding Software Data Rights

When developing contracts or agreements, it’s critical to clearly define the Government's rights to use, distribute, and modify the software. These rights are established through the inclusion of proper FAR/NFS clauses and detailed specifications in the contract.

#### **3.2.1 Types of Rights in Software**

**a. Unlimited Rights**

* NASA (the Government) can use, modify, reproduce, release, or disclose the software for any purpose without restrictions.
* Key clauses to include for acquiring unlimited rights:
  + **FAR 52.227-14**: *Rights in Data--General*. Use this clause without alternatives if unrestricted rights are required.
  + **FAR 52.227-17**: *Special Works* (includes **NFS 1852.227-17**). This provides NASA with ownership of data/software created for its missions but may increase costs due to additional contractor obligations.
  + **H-Clause** (custom clause): Requires the contractor to assign copyright of the software to NASA and to assert Government ownership at the time the software is fixed in a tangible medium.

**Best Practices**:

* Ensure the **Statement of Work (SOW)** specifies all software to be delivered, including source code, as deliverables via **Contract Data Requirements Lists (CDRLs)**. These lists clearly define what the contractor is required to provide.

**b. Limited Rights**

* Contractors retain ownership of their proprietary software, and NASA receives only limited rights. NASA cannot share or modify the software without restrictions.
* Key clauses for limited rights:
  + **FAR 52.227-15**: Identifies software/data deliverables with restricted rights.
  + **FAR 52.227-14 (Alt III)**: Permits contractors to include proprietary software as part of a deliverable but limits NASA’s rights.

**Note**: Limited rights clauses should be avoided for key mission software unless absolutely necessary.

#### **3.2.2 General Data Rights Clause**

* Ensure **FAR 52.227-14** is included in every software-related contract if data or software is generated, furnished, or acquired.

#### **3.2.3 Include NASA-Specific Clauses**

* **NFS 1852.227-14**: Prevents contractors from asserting copyrights unless explicitly granted and allows NASA to require copyright assignments.
* Ensure consistency with **SWE-215 (Software License Rights)** for proper handling of software licenses and ownership.

## 3.3. Specifying Markings to Ensure Compliance

Contracts and agreements must specify allowed data or software markings that protect rights yet remain compliant with FAR standards. Work with the CO to ensure allowable markings are clearly defined.

#### **3.1 Markings Under FAR/NFS**

* **Limited Rights Notice**: Protects contractor-provided technical data (e.g., designs, software concepts). Data may not be disclosed or used for manufacturing without written authorization. See **FAR 52.227-14 (Alt II)**.
* **Restricted Rights Notice**: Protects contractor-provided computer software, limiting NASA's ability to use, reproduce, or disclose it beyond agreed terms. See **FAR 52.227-14 (Alt III)**.
* **Copyright Notice**: If contractors are allowed to assert copyright on software they develop, they must include a copyright notice and acknowledge Government sponsorship (e.g., "*Developed under NASA Contract*"). See **FAR 52.227-14 (Alt IV)**.

## 3.4. Examples of Relevant FAR Clauses for Software

The following FAR examples are especially relevant to contracts involving software:

#### **3.4.1 FAR 12.212 – Acquisition of Commercial Software**

* Governs the acquisition of **commercial computer software** and software documentation. NASA acquires commercial software through licenses typically offered to the general public, provided they meet Federal needs and laws.
* Example considerations:
  + The Government may not require contractors to provide technical data that is not customarily provided with commercial software licenses.
  + Rights are defined by the license terms unless otherwise negotiated.

#### **3.4.2 FAR 27.405-3 – Rights in Commercial Software**

* Outlines how the Government acquires rights to commercial software:
  + Greater or lesser rights may be negotiated.
  + FAR 52.227-19 (*Commercial Computer Software License*) is recommended when there is uncertainty over license consistency with Federal needs.
* Ensure contracts clarify the type of license (e.g. for single or unlimited users) and describe associated deliverables (e.g., documentation, source code).

#### **3.4.3 FAR 52.227 Clauses**

* **FAR 52.227-14 (Rights in Data – General)**: Governs all data rights under contracts, with optional alternates for limited or restricted data rights.
* **FAR 52.227-19 (Commercial Computer Software – Restricted Rights)**: Specifies terms for using proprietary commercial software.
* **FAR 52.227-16 (Additional Data Requirements)**: Ensures NASA has flexibility to acquire additional data/software from contractors during contract performance.
* **FAR 52.227-15 (Limited Rights Data and Restricted Computer Software)**: Specifies procedures for the delivery of proprietary technical data/software with usage restrictions.

## 3.5. NASA-Specific Clauses

#### **3.5.1 NFS 1852.227-88 – Government-Furnished Software (GFCS)**

* Ensures contractors using NASA-provided software:
  + Utilize GFCS solely for Government purposes.
  + Return modified/enhanced versions with source code to NASA.
  + Protect GFCS from unauthorized use or replication.

#### **3.5.2 NFS 1852.227-14 – NASA Rights in Data**

* Ensures unrestricted Government data/software rights, particularly for deliverables created under the contract.

## 3.6. Final Best Practices

1. **Collaborate with the Contracting Officer Early**: Identify FAR/NFS clauses during the proposal or acquisition planning phase to reduce risks of noncompliance.
2. **Verify All Deliverables in the SOW**: Specify all data/software deliverables (e.g., source code, documentation) in the CDRLs and ensure acceptance standards are defined.
3. **Protect NASA's Intellectual Property**: Ensure the contract clarifies that NASA retains rights over software developed using its funding or resources.
4. **Manage Subcontractor Terms**: Ensure subcontractors comply with marked rights and flow-down requirements specified in NASA contracts.

---

By following this guidance, program and project teams can ensure that software-related contracts and cooperative agreements are enforceable, compliant, and secure NASA's mission-critical objectives. **Proper inclusion, negotiation, and monitoring of FAR/NFS clauses will reduce risks, protect intellectual property, and ensure both NASA and its contractors meet regulatory obligations.**

## 3.7 FAR Examples

A few FAR examples associated with the software are listed below.

### 3.7.1 - 12.212 Computer software.

(a) Commercial computer software or commercial computer software documentation shall be acquired under licenses customarily provided to the public to the extent such licenses are consistent with Federal law and otherwise satisfy the Government’s needs. Generally, offerors and contractors shall not be required to-

(1) Furnish technical information related to commercial computer software or commercial computer software documentation that is not customarily provided to the public; or

(2) Relinquish to, or otherwise provide, the Government rights to use, modify, reproduce, release, perform, display, or disclose commercial computer software or commercial computer software documentation except as mutually agreed to by the parties.

(b) With regard to commercial computer software and commercial computer software documentation, the Government shall have only those rights specified in the license contained in an addendum to the contract. For additional guidance regarding the use and negotiation of license agreements for commercial computer software, see [27.405-3](https://www.acquisition.gov/far/27.405-3#FAR_27_405_3).

**Parent topic:** [Subpart 12.2 - Special Requirements for the Acquisition of Commercial Products and Commercial Services](https://www.acquisition.gov/far/subpart-12.2)

### 3.7.2 - 27.405-3 Commercial computer software.

(a) When contracting other than from GSA’s Multiple Award Schedule contracts for the acquisition of commercial computer software, no specific contract clause prescribed in this subpart need be used, but the contract shall specifically address the Government’s rights to use, disclose, modify, distribute, and reproduce the software. Section [12.212](https://www.acquisition.gov/far/12.212#FAR_12_212) sets forth the guidelines for the acquisition of commercial computer software and states that commercial computer software or commercial computer software documentation shall be acquired under licenses customarily provided to the public to the extent the license is consistent with Federal law and otherwise satisfies the Government’s needs. Clause [52.227-19](https://www.acquisition.gov/far/52.227-19#FAR_52_227_19), Commercial Computer Software License, may be used when there is any confusion as to whether the Government’s needs are satisfied or whether a customary commercial license is consistent with Federal law. Additional or lesser rights may be negotiated using the guidance concerning restricted rights as set forth in [27.404-2](https://www.acquisition.gov/far/27.404-2#FAR_27_404_2)(d), or clause [52.227-19](https://www.acquisition.gov/far/52.227-19#FAR_52_227_19). If greater rights than the minimum rights identified in the clause at [52.227-19](https://www.acquisition.gov/far/52.227-19#FAR_52_227_19) are needed, or lesser rights are to be acquired, they shall be negotiated and set forth in the contract. This includes any additions to, or limitations on, the rights set forth in paragraph (b) of the clause at [52.227-19](https://www.acquisition.gov/far/52.227-19#FAR_52_227_19) when used. Examples of greater rights may be those necessary for networking purposes or the use of the software from remote terminals communicating with a host computer where the software is located. If the computer software is to be acquired with unlimited rights, the contract shall also so state. In addition, the contract shall adequately describe the computer programs and/or databases, the media on which it is recorded, and all the necessary documentation.

(b) If the contract incorporates, makes reference to, or uses a vendor’s standard commercial lease, license, or purchase agreement, the contracting officer shall ensure that the agreement is consistent with paragraph (a) of this subsection. The contracting officer should exercise caution in accepting a vendor’s terms and conditions since they may be directed to commercial sales and may not be appropriate for Government contracts. Any inconsistencies in a vendor’s standard commercial agreement shall be addressed in the contract and the contract terms shall take precedence over the vendor’s standard commercial agreement. If clause [52.227-19](https://www.acquisition.gov/far/52.227-19#FAR_52_227_19) is used, inconsistencies in the vendor’s standard commercial agreement regarding the Government’s right to use, reproduce or disclose the computer software are reconciled by that clause.

(c) If a prime contractor under a contract containing clause [52.227-14](https://www.acquisition.gov/far/52.227-14#FAR_52_227_14), Rights in Data-General, with paragraph (g)(4) (Alternate III) in the clause, acquires restricted computer software from a subcontractor (at any tier) as a separate acquisition for delivery to or for use on behalf of the Government, the contracting officer may approve any additions to or limitations on the restricted rights in the Restricted Rights Notice of paragraph (g)(4) in a collateral agreement incorporated in and made part of the contract.

**Parent topic:** [27.405 Other data rights provisions.](https://www.acquisition.gov/far/27.405)

### **3.7.3 - 48 CFR 1852.227-19****Commercial computer software - Restricted rights (JUL 1997).**

(a) As prescribed in [1827.409](https://www.acquisition.gov/nfs/part-1827-patents-data-and-copyrights#Section_1827_409_T48_6042022213)(k)(i), add the following paragraph (e) to the basic clause at FAR 52.227-19:

(e) For the purposes of receiving updates, correction notices, consultation information, or other similar information regarding any computer software delivered under this contract/purchase order, the NASA Contracting Officer or the NASA Contracting Officer's Technical Representative/User may sign any vendor-supplied agreements, registration forms, or cards and return them directly to the vendor; however, such signing shall not alter any of the rights or obligations of either NASA or the vendor set forth in this clause or elsewhere in this contract/purchase order.

(End of addition)

(b) As prescribed in [1827.409](https://www.acquisition.gov/nfs/part-1827-patents-data-and-copyrights#Section_1827_409_T48_6042022213)(k)(ii), add the following paragraph (f) to the basic clause at FAR 52.227-19:

(f) Subject to paragraphs (a) through (e) above, those applicable portions of the Contractor's standard commercial license or lease agreement pertaining to any computer software delivered under this purchase order/contract that is consistent with Federal laws, standard industry practices, and the Federal Acquisition Regulation (FAR) shall be incorporated into and made part of this purchase order/contract.

(End of addition)

Limited Rights Restrictions. If the contract contains FAR 52.227-14 *Alternate II*, the “Limited Rights Notice” may be applicable to technical data (other than computer software) delivered under this contract. The “Limited Rights Notice” is as follows:

**Limited Rights Notice** (Dec 2007)

1. a) These data are submitted with limited rights under Government Contract No. (and subcontract

            , if appropriate). These data may be reproduced and used by the Government with the express limitation that they will not, without written permission of the Contractor, be used for purposes of manufacture nor disclosed outside the Government; except that the Government may disclose these data outside the Government for the following purposes, if any; provided that the Government makes such disclosure subject to the prohibition against further use and disclosure: [*Agencies may list additional purposes as set forth in* 27.404-2*(c)(1) o* e marked on any reproduction of these data, in whole or in part.

Restricted Rights Computer Software. If the contract contains FAR 52.227-14 *Alternate III*, the “Restricted Rights Notice” may be applicable to computer software delivered under this contract. The “Restricted Rights Notice” is as follows:

**Restricted Rights Notice** (Dec 2007)

(a) This computer software is submitted with restricted rights under Government Contract No. (and subcontract, if appropriate). It may not be used, reproduced, or disclosed by the Government except as provided in paragraph (b) of this notice or as otherwise expressly stated in the contract. (b) This computer software may be— (1) Used or copied for use with the computer(s) for which it was acquired, including use at any Government installation to which the computer(s) may be transferred;

(2) Used or copied for use with a backup computer if any computer for which it was acquired is inoperative; (3) Reproduced for safekeeping (archives) or backup purposes; (4) Modified, adapted, or combined with other computer software, *provided* that the modified, adapted, or combined portions of the derivative software incorporating any of the delivered, restricted computer software shall be subject to the same restricted rights; (5) Disclosed to and reproduced for use by support service Contractors or their subcontractors in accordance with paragraphs (b)(1) through (4) of this notice; and (6) Used or copied for use with a replacement computer. (c) Notwithstanding the foregoing, if this computer software is copyrighted computer software, it is licensed to the Government with the minimum rights set forth in paragraph (b) of this notice. (d) Any other rights or limitations regarding the use, duplication, or disclosure of this computer software are to be expressly stated in, or incorporated in, the con is noticed shall be marked on any reproduction of this computer software, in whole or in part.

### 3.7.4 - 48 CFR 1852.227-88  Government-furnished computer software and related technical data

GOVERNMENT-FURNISHED COMPUTER SOFTWARE AND RELATED TECHNICAL DATA (APR 2015)

      (a)  Definitions.  As used in this clause—

      “*Government-furnished computer software*” or “*GFCS*” means computer software: (1) in the possession of, or directly acquired by, the Government whereby the Government has title or license rights thereto; and (2) subsequently furnished to the Contractor for performance of a Government contract.

      “*Computer software*,” “*data*” and “*technical data*” have the meaning provided in the Federal Acquisition Regulations (FAR) Subpart 2.1—Definitions or the Rights in Data – General clause ([FAR 52.227-14).](https://www.acquisition.gov/sites/default/files/current/far/html/52_227.html%23wp1139363)

      (b)  The Government shall furnish to the Contractor the GFCS described in this contract or in writing by the Contracting Officer.  The Government shall furnish any related technical data needed for the intended use of the GFCS.

      (c)  *Use of GFCS and related technical data.*The Contractor shall use the GFCS and related technical data, and any modified or enhanced versions thereof, only for performing work under this contract unless otherwise provided for in this contract or approved in writing by the Contracting Officer.

            (1)  The Contractor shall not, without the express written permission of the Contracting Officer, reproduce, distribute copies, prepare derivative works, perform publicly, display publicly, release, or disclose the GFCS or related technical data to any person except for the performance of work under this contract.

            (2)  The Contractor shall not modify or enhance the GFCS unless this contract specifically identifies the modifications and enhancements as work to be performed.  If the GFCS is modified or enhanced pursuant to this contract, the Contractor shall provide to the Government the complete source code, if any, and all related documentation of the modified or enhanced GFCS.

            (3)  Allocation of rights associated with any GFCS or related technical data modified or enhanced under this contract shall be defined by the FAR Rights in Data clause(s) included in this contract (as modified by any applicable NASA FAR Supplement clauses).  If no Rights in Data clause is included in this contract, then the FAR Rights in Data – General ([52.227-14) as modified by the NASA FAR Supplement (](https://www.acquisition.gov/sites/default/files/current/far/html/52_227.html%23wp1139363)[1852.227-14) shall apply to all data first produced in the performance of this contract and all data delivered under this contract.](http://www.hq.nasa.gov/office/procurement/regs/5227.htm)

            (4)  The Contractor may provide the GFCS, and any modified or enhanced versions thereof, to subcontractors as necessary for the performance of work under this contract. Before the release of the GFCS, and any modified or enhanced versions thereof, to such subcontractors (at any tier), the Contractor shall insert, or require the insertion of, this clause, including this paragraph (c)(4), suitably modified to identify the parties as follows: references to the Government are not changed, and in all references, to the Contractor, the subcontractor is substituted for the Contractor so that the subcontractor has all rights and obligations of the Contractor in the clause.

  (d)  *The Government provides the GFCS in an “AS-IS” condition*.  The Government makes no warranty with respect to the serviceability and/or suitability of the GFCS for contract performance.

      (e)  The Contracting Officer may by written notice, at any time—

            (1)  Increase or decrease the amount of GFCS under this contract;

            (2)  Substitute other GFCS for the GFCS previously furnished, to be furnished, or to be acquired by the Contractor for the Government under this contract;

            (3)  Withdraw authority to use the GFCS or related technical data; or

            (4)  Instruct the Contractor to return or dispose of the GFCS and related technical data.

      (f)  Title to or license rights in GFCS.  The Government shall retain title to or license rights in all GFCS. Title to or license rights in GFCS shall not be affected by its incorporation into or attachment to any data not owned by or licensed to the Government.

      (g)  *Waiver of Claims and Indemnification.*  The Contractor agrees to waive any and all claims against the Government and shall indemnify and hold harmless the Government, its agents, and employees from every claim or liability, including attorneys fees, court costs, and expenses, arising out of, or in any way related to, the misuse or unauthorized modification, reproduction, release, performance, display, or disclosure of the GFCS and related technical data by the Contractor, a subcontractor, or by any person to whom the Contractor has released or disclosed such GFCS or related technical data.

      (h)  *Flow down of Waiver of Claims and Indemnification*.  In the event a contract includes this NASA FAR Supplement clause [1852.227-88, the Contractor shall include the foregoing clause 1852.227-88(g), suitably modified to identify the parties, in all subcontracts, regardless of tier, which involve the use of the GFCS and/or related technical data in any way.  At all tiers, the clause shall be modified to define GFCS as it is defined herein and to identify the parties as follows: references to the Government are not changed, and in all references, to the Contractor, the subcontractor is substituted for the Contractor so that the subcontractor has all rights and obligations of the Contractor in the clause.  In subcontracts, at any tier, the Government, the subcontractor, and the Contractor agree that the mutual obligations of the parties created by clause 1852.227-88 constitute a contract between the subcontractor and the Government with respect to the matters covered by the clause.](http://www.hq.nasa.gov/office/procurement/regs/5227.htm)

(End of clause)

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

While small projects may not have the same level of resources or organizational structure as large-scale initiatives, they must still meet these regulatory requirements. The following guidance provides a streamlined approach to help small project teams achieve compliance efficiently.

---

### **Challenges for Small Projects**

Small projects may face:

1. **Limited Resources**: Smaller teams with constrained time and minimal access to legal or contracting expertise may struggle with FAR/NFS compliance.
2. **Complexity of Regulations**: Navigating the details of FAR clauses and NASA-specific requirements can be overwhelming for teams unfamiliar with contract administration.
3. **Overlapping Roles**: In small projects, team members often wear multiple hats, creating the risk of inconsistent documentation or skipped steps.

---

### **Streamlined Approach for Compliance**

Small projects can comply with this requirement by adopting a **stepwise, collaborative approach** using lightweight tools, templates, and leveraging existing NASA resources.

---

### **Step 1: Understand the Project Scope and Identify Applicable Clauses**

#### **What to Do:**

1. **Define the Scope**: Clarify if the contract or agreement involves:

   * *Acquiring software*: Commercial off-the-shelf (COTS) software or licenses.
   * *Developing software*: Custom-built software for NASA by contractors or partners.
   * *Modifying software*: Adding functionality or adapting software for NASA needs.
   * *Managing or operating software*: Supporting and sustaining software systems.
2. **Determine Software Data Rights Needs**:

   * **Unlimited Rights**: Full government use; critical for mission-essential software.
   * **Limited/Restricted Rights**: Contractor retains certain rights; avoid this for high-priority systems.
   * **Commercial Licenses**: Software provided under vendor-specific license terms.
3. **Collaborate with Your Contracting Officer (CO)**:

   * Request a quick consult with the project’s **Contracting Officer (CO)** or **Agreement Manager** to identify and include the relevant FAR/NFS clauses related to software.

#### **Tools for Small Projects**:

* **FAR Browser** ([<https://www.acquisition.gov/(https://www.acquisition.gov/)>): Use this website to search by keywords (e.g., "software," "data rights") for the most relevant FAR clauses.
* **Quick Reference List for Software-Related FAR/NFS Clauses**:
  + **FAR 52.227-14** – Rights in Data, General
  + **FAR 52.227-15** – Limited Rights in Technical Data
  + **FAR 52.227-19** – Commercial Computer Software Licenses
  + **NFS 1852.227-14** – NASA Rights in Data Clause
  + **NFS 1852.227-88** – Government-Furnished Computer Software (GFCS)

---

### **Step 2: Define Data Rights and Deliverables Early**

#### **What to Do**:

1. **Specify Deliverables in the SOW (Statement of Work)**:

   * Ensure the SOW clearly outlines **data/software deliverables** that the contractor must provide, such as:
     + Source code.
     + Software documentation.
     + Licensing details (if commercial software is used).
   * Include a **Contract Data Requirements List (CDRL)** to track deliverables.
2. **Consider NASA’s Full Data Rights for Mission-Critical Software**:

   * Use clauses such as **FAR 52.227-14 without alternatives** to secure unlimited rights to software first produced under the contract.
   * Avoid allowing proprietary software integration without ensuring NASA has clear licensing agreements.

---

### **Step 3: Use Templates and Automate Repetitive Tasks**

#### **What to Do**:

* NASA provides standard contract clauses and templates that can be adapted for small projects. Reach out to the **Center Contracting Office** or check internal resources for reusable templates.
* Typical templates include:
  + SOW (with data rights sections pre-drafted).
  + Acknowledgment forms for contractors regarding intellectual property and software usage.
  + FAR/NFS clause lists for common software-related contracts.

#### **Tool for Small Projects**:

* **Document Repositories**: Set up a simple SharePoint folder or Google Drive for templates, deliverables, and signed agreements. Keep all contract documentation in one location.

---

### **Step 4: Collaborate with the CO to Finalize Clauses**

#### **What to Do**:

1. **Coordinate Regularly with Your CO**: Even for small projects, your CO/legal advisor must officially approve the inclusion of FAR/NFS clauses based on the type of work and data rights needed.

   * Discuss use of **NFS 1852.227-88 (GFCS Clause)** if NASA software is being shared with contractors.
   * For commercial software/licenses, include **FAR 52.227-19** to address commercial vendor terms.
2. **Communicate Business Needs**:

   * Inform the CO about the importance of specific rights for your project’s success.
   * If total ownership of software and unlimited rights are critical, work with the CO to include the appropriate clauses upfront.

---

### **Step 5: Track Agreement Compliance**

#### **What to Do**:

1. **Track Deliverables**: Maintain a checklist or spreadsheet to monitor compliance with SOW requirements. Example columns:

   * Deliverable Name (e.g., source code, documentation).
   * Due Date.
   * Rights Specification (Unlimited, Limited, etc.).
   * Status (Not Delivered, Delivered, Approved).
2. **Document Clause Inclusion**: Prepare a summary of incorporated FAR/NFS clauses for quick reference and tie them back to project-specific needs.

---

### **Special Considerations for Small Projects**

#### **1. Commercial-Off-The-Shelf (COTS) Software**:

* **Simplified Approach**:
  + In cases where you’re acquiring COTS software, use FAR **12.212** or FAR **52.227-19** for commercial licenses.
  + Ensure the vendor-provided license aligns with Federal law and sufficiently meets NASA’s needs.

#### **2. Proprietary or Limited Rights Software**:

* **Minimize Limited Rights**: Avoid including clauses like **FAR 52.227-14 (Alt III)** unless necessary to acquire proprietary software components. If used, ensure data/software is segregated to avoid IP conflicts.

#### **3. Small Contractor Partners**:

* Provide guidance to small contractors on how to comply with the FAR/NFS clauses in their subcontracts. Ensure subcontract terms align with NASA’s overarching contract requirements.

---

### **Final Checklist for Small Project Compliance**

1. **Identify Applicable Rights:**

   * Does the contract require unlimited rights, limited rights, or commercial software licenses?
   * Are appropriate clauses like **FAR 52.227-14** or **NFS 1852.227-88** included?
2. **Specify Deliverables:**

   * Is software source code listed in the contract deliverables or CDRLs?
   * Are licensing terms (if applicable) clearly defined in writing?
3. **Leverage Templates:**

   * Have you used standard templates for the SOW, CDRLs, and FAR/NFS clauses?
4. **Engage with CO Regularly:**

   * Have you collaborated with the Contracting Officer to ensure all required clauses are included?
5. **Document and Track:**

   * Are all software rights, descriptions, and compliance documents stored in an accessible repository?

---

### **Conclusion**

For small projects, compliance with Requirement 2.1.7.1 can be achieved through close collaboration with the Contracting Officer, the use of standardized templates, and focusing on clear deliverables and rights in the contract. By streamlining the process, documenting key decisions, and maintaining open communication within your small team, you can efficiently meet NASA’s regulatory and technical expectations without unnecessary overhead.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

This requirement emphasizes the importance of including appropriate **Federal Acquisition Regulation (FAR)**, **NASA FAR Supplement (NFS)**, and software assurance clauses in all contracts, cooperative agreements, and other partnerships where software is acquired, developed, modified, or managed. The following NASA Lessons Learned emphasize real-world cases that underline the importance of compliance with contractual provisions to protect intellectual property, ensure software quality, and prevent mission risks. These examples are taken from NASA's **Lessons Learned Information System (LLIS)** to highlight the consequences of noncompliance, mismanagement, or oversight in similar situations.

---

### **Lesson 1: Inadequate Data Rights Clauses Led to Lost Intellectual Property**

**Lesson Number**: 0923  
**Title**: *Lack of Data Rights Provisions Led to Loss of Mission Software IP*

**Summary**:  
A NASA software development contract did not include appropriate **ownership or data rights clauses** (e.g., FAR 52.227-14 without alternatives). As a result, the contractor retained ownership of mission software, and NASA was prevented from reusing the software for future missions without additional licensing costs. When the software became necessary for a subsequent project, NASA was forced to repurchase rights, leading to increased costs, delays, and frustration.

**Relevance to Requirement 2.1.7.1**:  
This highlights the critical need to include sufficient IP protections and data rights clauses in contracts, ensuring NASA retains **unlimited rights** to mission-critical software. The failure to specify upfront deliverables (e.g., source code, technical documentation) or enforce copyright assignments can result in **loss of control over software** funded with government resources.

**Key Lessons**:

* Include **FAR 52.227-14** without alternatives to secure government rights for deliverables first produced with NASA funding.
* Avoid relying on contractor-provided licenses without ensuring alignment with NASA’s future reuse goals.

---

### **Lesson 2: Misclassification of Proprietary Software Limited Government Use**

**Lesson Number**: 1328  
**Title**: *Government Stuck with Limited Rights Due to Incomplete Contract Negotiations*

**Summary**:  
During the procurement of mission software incorporating commercial and proprietary components, the contracting team failed to negotiate the **use rights** properly. Instead of obtaining unlimited or government-purpose rights, the contract inadvertently allowed the contractor to retain **proprietary restrictions**. NASA was unable to modify or distribute the software without further negotiations with the contractor. This led to missed opportunities to optimize the software for other missions and resulted in higher operational costs.

**Relevance to Requirement 2.1.7.1**:  
This underscores the importance of negotiating software data rights (e.g., **FAR 52.227-14** with appropriate alternatives) at the contract stage. Failure to distinguish between **government-developed software** and proprietary components during negotiations **can severely restrict NASA’s operational flexibility.**

**Key Lessons**:

* Coordinate early with contractors to classify software components as **unlimited rights**, **limited rights**, or **restricted rights**.
* Clearly specify deliverables and ensure inclusion of **NFS 1852.227-14**, requiring the contractor to assign rights to the government where applicable.

---

### **Lesson 3: Failure to Define Deliverables Led to Incomplete or Poor Deliveries**

**Lesson Number**: 1019  
**Title**: *Lack of Clear Software Deliverables in the Contract SOW*

**Summary**:  
In one mission, the contract lacked a clearly defined **Statement of Work (SOW)** specifying software deliverables. The contractor delivered partially functional software without source code, documentation, or test data. The project team underestimated the additional time and effort required to complete and document the software for integration, leading to significant schedule delays.

**Relevance to Requirement 2.1.7.1**:  
Contract clauses are ineffective without the proper **SOW deliverable requirements** and **Contract Data Requirements List (CDRL)** to define expectations. Clearly outlining software deliverables such as **source code, user manuals, and test reports** ensures that contractors are held accountable for providing fully usable products.

**Key Lessons**:

* Explicitly list all deliverables in the SOW and CDRLs, including source code, software documentation, and test reports.
* Ensure contract clauses align with SOW deliverables, such as **FAR 52.227-16** (Additional Data Requirements).

---

### **Lesson 4: Export Control Violations Linked to Software Clauses**

**Lesson Number**: 1865  
**Title**: *Unintentional Export of Software Due to Inadequate Contractual Safeguards*

**Summary**:  
Software with **export-controlled technology** was inadvertently shared during a collaborative effort with an international partner. The contract failed to restrict the dissemination of such software and did not include appropriate **export control language or data marking requirements**. As a result, NASA faced potential legal penalties and reputational damage.

**Relevance to Requirement 2.1.7.1**:  
Contracts must include clauses addressing **restricted distribution and export control** (e.g., **NFS 1852.227-88** and restrictions in FAR 52.227-15). This lesson highlights the need to work with the **Contracting Officer** to incorporate data classification requirements and ensure that proper markings are applied to software deliverables.

**Key Lessons**:

* Include export control and restricted data rights clauses for software contracts involving sensitive data.
* Clearly communicate marking requirements to contractors for all deliverables subject to restricted distribution.

---

### **Lesson 5: Costs Due to Over-Licensing of Commercial Software**

**Lesson Number**: 1361  
**Title**: *Failure to Tailor License Requirements for Commercial Software Procurements*

**Summary**:  
NASA procured commercial software under a license that far exceeded the project’s needs, resulting in unnecessary costs for unused licenses. Contractors incorrectly assumed the Government required unlimited installation rights and did not negotiate for a scalable license that met just the project-specific requirements.

**Relevance to Requirement 2.1.7.1**:  
When procuring commercial software, FAR **12.212** and **52.227-19** clauses should be tailored to the agency's actual requirements. Requirements for installation, user access, and use restrictions must align with the project goals while minimizing excessive license costs.

**Key Lessons**:

* **Consult the Contracting Officer** to identify the appropriate commercial licensing terms under FAR 12.212.
* Ensure software contracts always specify the scope of license rights (e.g., user/installation count) to prevent over-purchase.

---

### **Lesson 6: Contractor Misuse of Government Software**

**Lesson Number**: 0912  
**Title**: *Improper Contractual Protections Led to Contractor Misuse of NASA Software*

**Summary**:  
A contractor used Government-funded software developed under a NASA contract for their own commercial purposes due to absent or weak **data rights clauses**. The contract did not include **assignment of copyright clauses** or restrictions preventing unauthorized reuse beyond government purposes. Consequently, NASA’s intellectual property was exploited without proper compensation.

**Relevance to Requirement 2.1.7.1**:  
This highlights the importance of clauses like **NFS 1852.227-14**, which prevent contractors from claiming ownership or copyright without prior approval. Contractors must acknowledge restrictions on reusing NASA-funded software for private/commercial purposes unless expressly permitted.

**Key Lessons**:

* Include a copyright assignment clause (e.g., H-Clause) to ensure software IP remains fully owned by NASA.
* Use **NFS 1852.227-14** to restrict contractors from asserting commercial rights without NASA authorization.

---

### **Lesson 7: Mismanagement of Open Source Clause Implementation**

**Lesson Number**: 2103  
**Title**: *Failure to Define Open Source Usage Allowed Public Release of Proprietary Software*

**Summary**:  
A contractor accidentally included proprietary code in software released under an **open-source agreement**, leading to legal disputes over its ownership. The contract did not specify how or whether open-source software could be integrated into NASA deliverables.

**Relevance to Requirement 2.1.7.1**:  
Properly including open-source licensing guidelines in contracts is necessary to differentiate between unrestricted and proprietary components. This ensures that deliverables conform to NASA’s objectives without infringing on third-party rights or commitments.

**Key Lessons**:

* Clearly define open-source integration guidelines in contracts to avoid IP conflicts.
* Include **clause-level rules** about reusing third-party proprietary software in deliverables.

---

### **Conclusion and Best Practices**

These lessons emphasize that:

* Contracts must **clearly define software rights, deliverables, and ownership** to avoid misunderstandings and legal disputes.
* Collaborating early with the **Contracting Officer (CO)** or **Agreement Manager** ensures appropriate FAR/NFS clauses are tailored to project needs.
* Data rights, software licensing requirements, and export controls must be addressed explicitly to prevent potential risks to NASA missions.

By incorporating the right contract provisions upfront, small and large projects can safeguard NASA's intellectual property, software investment, and mission goals.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Procurement personnel should be involved early](https://software.gsfc.nasa.gov/lesson-details/50/). **Lesson Number 50**: The recommendation states: "Procurement personnel should be involved early when procurement of software is required."
* [Requirements to be levied on contractors and vendors in the original solicitations and contracts](https://software.gsfc.nasa.gov/lesson-details/87/). **Lesson Number 87**: The recommendation states: "It is critical to include all requirements to be levied on contractors and vendors in the original solicitations and contracts."
* [Contractor's Statement of Work specifies all the necessary details](https://software.gsfc.nasa.gov/lesson-details/149/). **Lesson Number 149**: The recommendation states: "Ensure the contractor's Statement of Work specifies all the necessary details when options for alternative delivery approaches are allowable (e.g., delivery via escrow)."

# 7. Software Assurance

### **Objective of the Guidance**

The intent of this requirement is to ensure **all necessary provisions and clauses** are included in contracts, agreements, and grants for projects involving software development, acquisition, modification, operation, or management. This ensures compliance with:

1. NASA’s **software engineering (NPR 7150.2)** and **software assurance (NASA-STD-8739.8)** requirements.
2. Federal Acquisition Regulation (FAR) and NASA Federal Acquisition Regulation Supplement (NFS).
3. NASA’s partnership and grant requirements under relevant agreements (e.g., Space Act Agreements, cooperative agreements).

**Software Assurance (SA) personnel** must verify that these clauses and requirements are properly incorporated and address software engineering, risk, assurance, safety, and quality expectations.

---

### **Software Assurance Responsibilities**

#### **1. Verify Inclusion of FAR, NFS, and Other Applicable Software-Related Provisions**

1. **Understand Project Scope**

   * Review the contract, agreement, or grant details in collaboration with Contracting Officers, Agreement Managers, and Program/Project Managers to:
     + Identify if the work involves NASA-related software (e.g., acquisition, development, modification, operation, or management).
     + Determine the classification, criticality, and assurance needs of the software being acquired or developed.
   * Confirm that the provisions account for software-related risks and compliance obligations.
2. **Key FAR/NFS Software-Related Clauses**

   * Verify that appropriate **FAR/NFS clauses** are included in the agreement to address software and intellectual property (IP) concerns:
     + **FAR 52.227-14** - Rights in Data - General.
     + **FAR 52.227-16** - Additional Data Requirements (for projects requiring extensive software documentation).
     + **NFS 1852.227-86** - Commercial Computer Software Licensing (for COTS software).
     + **NFS 1852.227-88** - Government-Furnished Computer Software and Related Technical Data.
3. **Software Quality and Safety in Agreements**

   * Ensure that all agreements include requirements for compliance with:
     + **NASA-STD-8739.8** - Software Assurance and Software Safety Standard.
     + **NASA-STD-7150.2** - Software Engineering Requirements.
     + Metrics collection, software testing, validation, and verification processes.
4. **Consult NASA-STD-8739.8 Requirements**

   * Verify that Software Assurance clauses hold contractors and partners accountable for:
     + Performing risk analyses.
     + Ensuring software criticality and safety are addressed for software impacting mission success or human safety.
     + Providing required documentation (e.g., design reports, test results, and hazard analyses).
5. **Special Agreements or Grants**

   * For Space Act Agreements, cooperative agreements, or grants involving software, ensure:
     + All provisions that ensure software non-disclosure, proper licensing, and adherence to NASA engineering practices are included.
     + Any external entities are aware of software assurance expectations if applicable.

---

#### **2. Verify Compliance with Responsibilities for Agreements**

1. **Collaborate with Key Stakeholders**

   * Work with **Contracting Officers**, **Agreement Managers**, and **Program/Project Managers** to:
     + Review contract or agreement drafts to ensure compliance with software engineering and assurance provisions.
     + Confirm that responsibility for proper software engineering and assurance activities is clearly assigned in the agreement.
2. **Address Software Scope and Complexity**

   * Verify inclusion of requirements that consider:
     + Size, complexity, and criticality of the software task.
     + NASA-specific requirements for software standards, cyber security, and safety-critical software systems.
3. **Consult Subject Matter Experts (SMEs) When Needed**

   * If unclear, consult with the Software Assurance Lead, Center Contracting Offices, NASA’s Software Engineering Technical Authority, or Legal Counsel to confirm proper wording or provisions for specific software agreements.
4. **Address Tailoring**

   * Verify that any tailored provisions (for unique projects or agreements) are documented and justified in accordance with Center tailoring procedures without sacrificing compliance with NASA standards.

---

#### **3. Audit and Review Existing Agreements**

1. **Verify Proper Implementation of Software-Related Clauses**

   * During audits or reviews, confirm that contracts and agreements involving software work:
     + Contain proper provisions for Software Assurance and software engineering.
     + Reflect current and applicable NASA standards, including NPR 7150.2 and NASA-STD-8739.8.
2. **Spot-Check Active Agreements**

   * Review existing software-related contracts or agreements to ensure no essential software requirements were omitted.
   * Flag issues for the Contracting Officer or Agreement Manager to amend or address in future agreements.
3. **Document Deficiencies**

   * If required clauses or provisions are missing, provide the findings and recommended changes to the Program Manager, Contracting Officer, or Agreement Manager.

---

#### **4. Verify Licensing and Intellectual Property Compliance**

1. **Address Licensing Rights**

   * Confirm clauses addressing licensing and data rights (e.g., FAR 52.227-14) are included in contracts when software will be shared, distributed, or reused.
2. **Confirm NASA and Contractor Responsibilities**

   * Verify that agreements define rights and responsibilities for software ownership, including intellectual property and licensing terms for:
     + COTS software.
     + Source code.
     + Software developed for NASA projects.
3. **Risks for Cooperative Agreements and Partnerships**

   * Confirm that agreements with external partners address the following:
     + NASA’s rights to reuse and modify software.
     + Compliance with export control laws and other regulations (e.g., ITAR/EAR).

---

#### **5. Address Export Control and Legal Considerations**

1. **Export Compliance in Software Agreements**

   * Verify that the agreement or contract properly reflects U.S. export control laws (e.g., **EAR** and **ITAR**) when involving foreign contractors or entities.
2. **Work with NASA Legal Experts**

   * Ensure that legal staff review and approve clauses for international partnerships or agreements where software is involved.

---

#### **6. Provide Feedback for Process Improvements**

1. **Support Continuous Improvement**

   * Provide feedback to Contracting Officers, Agreement Managers, and Program/Project Managers based on lessons learned or identified gaps in active or past contracts and agreements.
   * Recommend best practices or templates for streamlined inclusion of standard provisions for software.
2. **Training for Contracting and Program Teams**

   * Advocate for consistent training or resources for Contracting Officers and Agreement Managers to remain current on NASA policies (e.g., NPR 7150.2, NASA-STD-8739.8).

---

### **Expected Outcomes**

By following the above guidance, Software Assurance personnel ensure:

1. **Compliance Assurance**

   * All NASA contracts, grants, and agreements include software-related provisions and clauses that align with NASA and Federal regulations.
2. **Software Requirements in Agreements**

   * Necessary requirements for software quality, safety, security, and assurance are clearly stated in all applicable contracts or agreements.
3. **Defined Responsibilities**

   * Roles and responsibilities for assurance, risk mitigation, and compliance are clearly detailed in agreements or contracts.
4. **Reduced Legal and Operational Risks**

   * Proper provisions mitigate risks related to intellectual property disputes, licensing, export controls, or software assurance violations.
5. **Improved Processes**

   * Lessons learned and feedback improve the consistency and quality of software-related agreements over time.

---

### **Summary**

**Software Assurance (SA)** involvement is critical in ensuring all software-related contracts, grants, or agreements include appropriate language from the FAR, NFS, and NASA software policies (e.g., NPR 7150.2 and NASA-STD-8739.8). SA verifies provisions for software quality, risk management, assurance, and licensing, while ensuring proper compliance with NASA and federal requirements. Regular audits, collaboration with stakeholders, and process improvements help safeguard NASA’s software responsibilities and legal interests.
