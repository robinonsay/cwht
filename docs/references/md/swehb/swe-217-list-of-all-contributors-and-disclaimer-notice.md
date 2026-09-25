# SWE-217 - List of All Contributors and Disclaimer Notice

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695548. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice

SWE-217 - List of All Contributors and Disclaimer Notice

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695548)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695548&showCommentArea=true&showComments=true#addcomment)

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

2.1.5.15 The Center Director, or designee, (e.g., the Civil Servant Technical Point of Contact (POC) for the software product) shall perform the following actions:

a. Keep a list of all contributors to the software product.

b. Ensure that the software product contains appropriate disclaimer and indemnification provisions (e.g., in a “README” file) stating that the software may be subject to U.S. export control restrictions, and it is provided “as is” without any warranty, express or implied, and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-217 History

SWE-217 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 2.1.5.17 The Center Director or designee (e.g., the Civil Servant Technical Point of Contact for the software product) shall perform the following actions:  a. Keep a list of all contributors to the software product.  b. Ensure that the software product contains appropriate disclaimer and indemnification provisions (e.g., in a “README” file) stating that the software may be subject to U.S. export control restrictions, and it is provided “as is” without any warranty, express or implied, and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors. |
| Difference between C and D | Editorial fix 'Point of Contact' became POC |
| D | 2.1.5.15 The Center Director, or designee, (e.g., the Civil Servant Technical Point of Contact (POC) for the software product) shall perform the following actions:  a. Keep a list of all contributors to the software product.  b. Ensure that the software product contains appropriate disclaimer and indemnification provisions (e.g., in a “README” file) stating that the software may be subject to U.S. export control restrictions, and it is provided “as is” without any warranty, express or implied, and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

This requirement serves multiple purposes critical to NASA's operational, legal, and technical obligations. Maintaining a list of software contributors ensures transparency, accountability, and compliance with intellectual property and licensing laws. Including appropriate disclaimers and indemnification provisions protects NASA from potential legal liabilities while ensuring compliance with export control laws and mitigating risks when software is distributed internally or externally.

The rationale for this requirement is detailed below by addressing two key responsibilities:

1. Maintaining a list of contributors.
2. Including disclaimers and indemnifications in the software.

## 2.1 Key Rationale for the Requirement

### 2.1.1  Rationale for Maintaining a List of All Contributors

#### Why It’s Important:

Maintaining an accurate list of contributors to a software product is essential for the following reasons:

##### **a. Intellectual Property and Ownership Visibility**

* A contributor list ensures clear identification of all individuals and organizations involved in developing the software. This is critical for determining intellectual property (IP) rights, as contributors’ contracts (e.g., government employees, contractors, or external collaborators) may differ in terms of IP ownership.
* Proper tracking of contributors supports compliance with licensing and distribution requirements (e.g., verifying third-party contributions comply with open-source licenses).

##### **b. Ensuring Proper Use, Attribution, and Licensing Alignment**

* Knowing who contributed to the software enables NASA to track licensing obligations for third-party or open-source components integrated into the software.
* Accurate attribution of contributions fosters a culture of ethical development and transparency.

##### **c. Facilitating Collaboration Across NASA and Beyond**

* A clear contributor record promotes trust and collaboration within NASA and with external partners by documenting team members’ involvement in software development. This visibility may also assist in future software maintenance or specialized troubleshooting efforts.

##### **d. Supporting Risk Mitigation and Legal Accountability**

* In cases where defects, vulnerabilities, or compliance issues arise, a contributor list allows stakeholders to trace the development history of the software. This can accelerate issue resolution, maintain accountability, and reduce project risks.

**Key Takeaway**: The contributor list ensures ownership and licensing compliance while facilitating collaboration and accountability. It is an important tool for managing risks and preserving institutional knowledge over the software's lifecycle.

### 2.1.2  Rationale for Disclaimer and Indemnification Provisions

#### Why It’s Important:

Including disclaimers and indemnification provisions is a critical risk mitigation strategy that serves NASA’s legal, compliance, and operational interests when it distributes software. The rationale for these provisions includes the following:

##### **a. Legal and Liability Protections**

1. **"As Is" Disclaimer**:
   * The software disclaimer ensures that NASA is not liable for any issues or damages caused by the use or misuse of the software.
   * By explicitly stating that the software is provided "as is" without any guarantees or warranties, NASA protects itself from claims related to software failures, inaccuracies, or defects.
   * This disclaimer shields NASA from legal actions by recipients regarding the usability, functionality, or performance of the software.
2. **Indemnification Provision**:
   * This clause requires recipients of the software to assume responsibility for any legal claims arising out of their use, further protecting NASA and its contractors and subcontractors.
   * Without this provision, recipients might attempt to shift liability back to NASA, exposing the agency to unnecessary legal and financial risks.

##### **b. Compliance with U.S. Export Control Laws**

* NASA software products can contain technologies that are subject to export control restrictions under U.S. regulations like the **International Traffic in Arms Regulations (ITAR)** or the **Export Administration Regulations (EAR)**. Noncompliance with these laws could result in significant penalties for NASA.
* A disclaimer reminding recipients that the software is subject to export control laws helps mitigate accidental violations. It also clarifies that end-users bear the responsibility for ensuring compliance with U.S. laws.

##### **c. Risk Mitigation in External Distribution**

* Distributing software can introduce potential risks, including misuse, modification, or unintended incorporation into critical systems by recipients.
* By requiring recipients to waive claims against NASA and assume responsibility for any damages or legal liabilities, these provisions protect NASA, its contractors, and subcontractors from economic or reputational harm.

##### **d. Alignment with NASA Legal Policy and Precedent**

* Similar disclaimer and liability provisions are standard in agreements for open-source and proprietary software distributed by NASA (e.g., under NASA's **Open Source Agreement (NOSA)**). Maintaining these provisions allows NASA to apply consistent legal protections for its intellectual property.

### 2.1.3  Impact of Noncompliance

Failing to meet these requirements could result in the following negative outcomes:

1. **Legal Vulnerabilities**: Absence of disclaimers or indemnifications could lead to claims against NASA in the event of software failures or accidents involving recipients. Such lawsuits would divert agency resources and present reputational risks.
2. **Regulatory Noncompliance**: Non-compliance with U.S. export control laws could result in severe federal penalties, fines, or restrictions on NASA's software distribution activities.
3. **Intellectual Property Disputes**: Lack of a contributor list could cause legal disputes concerning the ownership of specific components of the software, delaying distribution and reuse efforts.
4. **Inefficiencies in Software Maintenance**: Without a contributor list, tracing software origins and resolving future issues or updates becomes difficult, adding unnecessary costs and delays.

### 2.1.4  How This Requirement Benefits NASA

1. **Risk Management**: Improves NASA’s ability to control risks associated with software distribution, including legal claims, export compliance violations, and operational misuse.
2. **Transparency and Accountability**: Facilitates clear documentation and accountability in software development by recording contributors and adhering to licensing terms.
3. **Compliance Assurance**: Ensures compliance with U.S. laws and NASA’s internal policies regarding software engineering, export controls, and liability protections.
4. **Institutional Knowledge Preservation**: Trackable contributor data and embedded disclaimers support long-term software reuse, collaboration, and modernization.

## 2.2 Conclusion

This requirement ensures that NASA can distribute software safely, legally, and with minimal risk. Maintaining a contributor list guarantees clear ownership and IP traceability, while appropriate disclaimers and indemnifications protect NASA and its contractors from legal liabilities and ensure export compliance. These actions collectively bolster NASA's reputation as a technically proficient and legally compliant organization, enabling its software to be reused both effectively and responsibly.

# 3. Guidance

The guidance below is intended to clarify and improve the responsibilities, considerations, and steps the **Civil Servant Technical Point of Contact (POC)** must follow when managing software products for sharing or reuse across NASA Centers. This revised guidance provides more structure, ensures clearer communication of legal and technical obligations, and emphasizes practical steps for compliance.

## 3.1 Civil Servant Technical Point of Contact Responsibilities

The Civil Servant Technical POC for the software product is responsible for ensuring that the software is handled and distributed in compliance with NASA policies, ensuring legal protection, and managing the software’s reusability. Their responsibilities include:

#### a. Keeping a List of Contributors

* **What**: Create and maintain an up-to-date list of all contributors to the software product, including individuals and organizations (e.g., civil servants, contractors, academic collaborators).
* **Why**: This is critical to determine software ownership, intellectual property (IP) rights, and potential licensing constraints.
* **How**:
  1. Use a centralized and clearly defined format (e.g., a contributor log within the version control system or in a standalone document).
  2. Include details such as names, roles, employers, and contributions (e.g., lines of code, testing, or documentation).
  3. Track contributions of commercial and open-source components as applicable (see Section 3.2).

#### b. Ensuring Disclaimer and Indemnification Provisions

* **What**: Ensure the software product includes appropriate disclaimers and indemnifications in a **“README”** file or equivalent documentation.
* **Why**: This protects NASA from liabilities and ensures compliance with export control laws.
* **How**:
  1. Add the following standard disclaimer to the documentation (e.g., in readme files or source code comments):  

     Standard Disclaimer

     "The software may be subject to U.S. export control restrictions. It is provided 'as is' without any warranty, express or implied. The recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors.
  2. Verify disclaimer inclusion as part of the submission process.
  3. If unsure about the necessity, seek guidance from you**r Center’s Legal Office.**

**Applicability**: These responsibilities apply across all NASA Centers and span all Software Classifications under **NPR 7150.2** [083](#_tabs-<p></p>).

## 3.2 List of Contributors

The **list of contributors** ensures traceability of all parties involved in software development, providing transparency for intellectual property (IP) rights and compliance with licensing requirements.

#### Steps to Create and Maintain a Contributor List:

1. **Document Contribution Information**: For each contributor, include:
   * Name and role (e.g., developer, tester, systems engineer).
   * Employer or affiliation (e.g., NASA civil servant, contractor, academic partner).
   * Type of contribution (e.g., source code, design, verification and validation).
2. **Track Commercial and Open Source Software Component Contributors**:
   * Identify and document if the software includes any commercial-off-the-shelf (COTS) or open-source components.
   * Record details of the original source, including the license type and any usage documentation.
3. **Maintain the List in a Centralized Repository**:
   * Use your Center’s designated software tracking tool or version control system (e.g., GitHub Enterprise, Jenkins pipeline documentation) to log information.
   * Update the list during software development activities such as version releases, contributions by new personnel, or the integration of third-party components.

#### Why This Is Important:

* Ensures accurate ownership and usage rights for the software.
* Avoids future conflicts or disputes over licensing terms.
* Simplifies risk assessments during software reuse or modification.

## 3.3 Disclaimer and Warranty Provision

The inclusion of a disclaimer and indemnification clause in the software documentation is critical to protect both NASA and its contractors. Here’s how to ensure compliance:

#### Steps to Include a Disclaimer:

1. **Add the Standard Disclaimer**:  
   Ensure the following statement is inserted into **software documentation** (e.g., README files, user guides, or in the comment block at the top of the source code file):  

   Standard Disclaimer

   "The software may be subject to U.S. export control restrictions, and it is provided 'as is' without any warranty, express or implied. The recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors."
2. **Verify Export Control Compliance**:
   * Work with your **Center’s Legal Office** to validate whether the software is subject to export control restrictions, and clearly communicate this responsibility to the recipient.
3. **Document the Disclaimer’s Placement**:
   * Ensure the disclaimer appears in prominent locations within the software package (both user-facing and in technical documentation).
4. **Ensure No Implied Warranties**:
   * The disclaimer emphasizes that the software is provided **“as is”**, meaning that NASA offers no guarantees regarding its reliability, accuracy, or usability.

#### Why This Is Important:

* Protects NASA and its contractors from legal claims resulting from software misuse, integration issues, or unexpected behaviors.
* Enhances legal compliance with U.S. export control laws.

## 3.4 Software Rights and Licensing

Sharing NASA software requires validating that ownership and licensing rights are clearly defined to avoid licensing conflicts.

#### Steps for Determining Software Rights:

1. **Verify Development Context**:
   * If the software was developed entirely by NASA civil servants, and it does not include third-party components (e.g., open-source or commercial software), it is typically NASA property and can be shared internally.
   * If contractors contributed, or if any non-NASA software is integrated, consult with your Legal Office.
2. **Confirm Licensing Rights and Permissions**:
   * **For Proprietary and Commercial Software**: Confirm NASA has proper usage or redistribution rights through [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software).
   * **For Open Source**: Ensure the software meets the requirements of the specific open-source license. Document how these obligations are being fulfilled.
3. **Address Additional Legal Considerations**:
   * Ensure proprietary rights, warranties, licensing terms, and other agreements have been documented.
   * Secure appropriate permissions or approvals if portions of the software are owned by third parties.
4. **Avoid License Conflicts**:  
   Cross-check compatibility between open-source, proprietary, and NASA standards to ensure there are no contradictions. Address any discrepancies before publishing within NASA's internal software catalog.

#### Relevant Policies:

* [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software)
* [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights)

## 3.5 Avoiding Software Licensing Conflicts

To prevent issues related to software-sharing rights:

* Ensure the software has a **Government Purpose License** or equivalent rights giving NASA permission to share it internally.
* In cases where licensing is unclear, obtain clarification and guidance from:
  + NASA’s Office of the General Counsel or your Center’s legal team.
  + The Office of the Chief Information Officer (OCIO) when Class F software is involved.

### **Key Responsibilities Checklist**

To simplify compliance, the Civil Servant Technical POC should ensure:

✔ A **complete contributor list** is maintained, including third-party contributors.  
✔ A **standard disclaimer** is added to all software documentation.  
✔ Any **rights, licenses, and legal constraints** are fully reviewed and documented.  
✔ Compliance with **U.S. export controls** is validated.  
✔ **Collaboration with the Center Legal Office** for software developed with external partners or contractors.

This improved guidance ensures a clear and consistent process for safeguarding NASA’s software, reducing liability risks, and fostering a culture of compliance and accountability.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire)      * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

This requirement applies to all NASA Centers and spans all software classifications. Small projects must follow the same compliance requirements as larger projects but often need a simplified and practical approach due to limited resources.

#### Challenges for Small Projects

* **Fewer Dedicated Resources**: Small teams may not have legal or administrative specialists available to assist with licensing or legal disclaimers.
* **Time Constraints**: Limited schedules may push compliance tasks to the end of the project, which can lead to oversights.
* **Agility vs. Formality**: Small projects often operate within agile or informal workflows, which may not naturally align with NASA’s formal compliance requirements.

## 4.1 Guidance for Small Projects

Here's a tailored, lightweight approach to ensure compliance while minimizing administrative burdens on small projects.

### 4.1.1 Steps for Small Projects

#### 4.1.1.1  Maintain a Minimalist Contributor List

An accurate contributor list is essential for determining software ownership and managing intellectual property (IP) rights. Small projects can adopt a simple, streamlined approach:

**Actions**:

* + Document contributor information in a basic format like a spreadsheet, version control system log (e.g., in Git or GitHub), or a plain text file in the software repository.
  + Include the following fields for each contributor:
    1. **Name**: Full name of the contributor.
    2. **Affiliation/Employer**: Whether they are a NASA civil servant, contractor, or an external collaborator.
    3. **Role**: The nature of their work—e.g., development, design, testing, documentation.
    4. **Source**: Indicate if the contribution involves third-party software (commercial or open source).

**Quick Tip**: If you’re using Git, you can use the **`git log` command** to generate a record of code contributions and package it as part of your documentation.

**Free Tool Suggestions**:

* + Excel/Google Sheets for manual tracking.
  + Built-in GitHub/GitLab contribution tracking features.

**Frequency**: Update the contributor list after each development milestone or when new contributors are added.

**Benefits for Small Projects**:

* + Ensures compliance without additional overhead.
  + Helps trace contribution origins quickly if IP or licensing questions arise later.

#### 4.1.1.2  Include a Pre-Written Disclaimer in Documentation

Small projects can comply with the disclaimer requirement by embedding a pre-written statement into the **README** file and/or source code comments.

**Actions**:

1. 1. **Copy-paste the Standard Disclaimer**:  
      Add the following text to the **README** file:  

      Standard Disclaimer

      "This software may be subject to U.S. export control restrictions, and it is provided 'as is' without any warranty, express or implied. The recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors."
   2. **Place the Disclaimer in Two Locations**:
      * In the root **README** file or similar documentation format.
      * As a comment block in the main source code file of the project.

**Template File Placement for Small Projects**:

* + [README.md](http://README.md) (or equivalent documentation file).
  + Licensing.txt (if you maintain one).
  + At the top of the main file in your code repository.

**If You’re Unsure**:

Contact your **Center’s Legal Office** for guidance on export control or indemnification specifics, especially if the software involves sensitive technology or third-party tools.

**Benefits for Small Projects**:

* + Embedding a ready-made statement saves time.
  + Reduces the risk of legal exposure by clearly protecting NASA.

#### 4.1.1.3  Verify Software Ownership and Licensing Early

Avoid last-minute issues with software sharing rights by reviewing ownership and licensing details early in the project lifecycle.

**Simplified Checks for Small Teams**:

1. 1. **Ownership Assessment**:
      * If the entire software was developed by NASA civil servants and contains no external components, it is likely NASA property and may be shareable internally.
      * If external contributors (e.g., contractors or collaborators) are involved, verify contract terms or agreements to ensure NASA retains rights for reuse or distribution.
   2. **Check Open Source or Third-Party Software**:
      * Use a lightweight inventory to identify all third-party or open-source components used in your software.
      * Confirm that any open-source components are compatible with NASA's internal software-sharing policies. Ensure compliance with specific licensing terms (e.g., GNU, MIT, Apache).
   3. **Work with Legal for Mixed Contributions**:
      * If your software integrates commercial solutions, proprietary code, or third-party components, consult your Center Legal Office to verify NASA’s rights before sharing.
      * Ensure you have a valid Government Purpose License Agreement (GPLA) or another appropriate license for any redistribution or reuse.

**Quick Tip**:

* + Use tools like FOSSology or Black Duck to scan and analyze third-party and open-source licenses efficiently.

**Benefits for Small Projects**:

* + Reduces the risk of accidentally violating licensing agreements.
  + Keeps projects on track by clarifying ownership before sharing or reuse.

#### 4.1.1.4  Document and Retain Project Artifacts for Reuse

Maintaining organized artifacts ensures your software is easily reusable by others at NASA.

**Minimum Artifacts to Retain**:

* + **Contributor List** (from step 1).
  + **README File**: Include software purpose, usage instructions, and the disclaimer.
  + **Licensing Documentation**: Copy any relevant licensing terms for third-party components.

**Where to Store Artifacts**:

* + **GitHub Enterprise/GitLab Repository**: Store documentation alongside the source code.
  + **Centralized NASA Repository**: If your Center maintains a software catalog or repository, upload artifacts there following local policies.

**Benefits for Small Projects**:

* + Streamlines future sharing/reuse without rework.
  + Facilitates easy access for collaborators.

### 4.1.2  Small Project Checklist

Use this checklist to keep your small project compliant:

#### **Contributor List**

✔ Maintain a list of all contributors (name, affiliation, role).  
✔ Track third-party component contributors, licenses, and source.

#### **Documentation**

✔ Add the standard disclaimer to the README and source code comments.  
✔ Confirm all disclaimers are visible and clear.

#### **Legal and Licensing**

✔ Verify software ownership (e.g., NASA Civil Servants-only vs. mixed contributions).  
✔ Consult Center Legal Office for open source or commercial software rights.  
✔ Ensure proprietary, usage, warranty, and licensing rights have been addressed.

#### **Artifacts for Sharing**

✔ Retain updated documentation (README, contributor list, licensing details).  
✔ Store artifacts in a version-controlled, easily accessible repository.

## 4.2  Scenario Example for Small Software Team

**Project**: An internal analysis tool developed by a small team.  
**Steps Followed**:

1. The team documents contributors in `contributors.txt` with simple fields: names, roles, affiliations.
2. They add a disclaimer to their `README.md` file and embed it in the main `.py` script.
3. They use open-source Python libraries (e.g., NumPy), track their licenses in `LICENSES.txt`, and verify compliance with MIT terms.
4. All files (source code, README, contributor list, and license details) are pushed to a GitHub Enterprise repository shared internally.
5. They perform a final legal review to confirm ownership of any shared outputs.

## 4.3 Key Takeaways for Small Projects

* Adopt simple tools (e.g., Git logs, spreadsheets) to track contributors and document software ownership.
* Always include the pre-written disclaimer in public-facing project documentation.
* Confirm legal rights early, especially when integrating external components into NASA software.
* Provide basic project artifacts (README, contributor list, licenses) to ensure future reusability.

With these streamlined actions, small projects can meet compliance without overloading limited resources.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
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

Below are lessons from NASA's **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** that directly or indirectly highlight the importance of tracking contributors, compliance with legal disclaimers, and managing software licensing.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Noncompliance with Export Control Laws

* **Lesson Number**: 1863
* **Title**: *Failure to Identify and Document Export-Controlled Technology*
* **Summary**:  
  A Lesson Learned from past NASA projects involved a failure to properly identify and label export-controlled technology within software documentation. A lack of clarity on export control regulations and insufficient disclaimers led to inadvertent distribution of restricted technology to unauthorized entities, resulting in legal and reputational risks for the agency.
* **Relevance to the Requirement**:  
  This demonstrates the critical role of including appropriate disclaimers in shared software to inform users of export control restrictions. Software products subject to such restrictions must communicate the limitations clearly to avoid accidental violations.
* **Key Takeaways**:
  + Proper legal disclaimers mitigate the risk of unauthorized use or sharing of export-controlled technology.
  + Legal offices should be consulted to ensure all software is compliant with export control laws before sharing.

#### 2. Lack of Disclaimer for Distributed Software

* **Lesson Number**: 1421
* **Title**: *Liability from “As-Is” Distributed Software Without Proper Disclaimers*
* **Summary**:  
  A NASA team learned that software distributed without explicit "as-is" disclaimers raised liability concerns when end-users claimed damages due to software defects. In one incident, the software was reused for a critical operational context for which it was not originally designed. Failure to include disclaimers harmed NASA’s reputation and could have resulted in legal claims against the agency.
* **Relevance to the Requirement**:  
  An "as-is" warranty disclaimer (ensuring no liability for performance or defects) is essential in all NASA software to protect the agency from claims while making it clear that the software is not guaranteed for a specific purpose.
* **Key Takeaways**:
  + Always include a disclaimer indicating that the software is distributed "as-is" without warranty, to lower liability risks.
  + Disclaimers must be visible in the README file or source code comments.

#### 3. Incomplete Contributor Records Led to Licensing Confusion

* **Lesson Number**: 0912
* **Title**: *Failure to Track Contributors Created Licensing and Ownership Issues*
* **Summary**:  
  A NASA software product intended for sharing was delayed due to incomplete records of contributors. The project team was uncertain whether certain contributors were civil servants, contractors, or external collaborators. This ambiguity complicated the determination of intellectual property rights and compliance with licensing obligations. As a result, the software could not be immediately shared or reused until legal and IP investigations were complete, causing significant delays.
* **Relevance to the Requirement**:  
  Maintaining a complete and accurate contributor list is critical for ownership and licensing clarity. If owner/contributor roles aren’t properly tracked, there’s a risk of uncertainty about who owns what portion of the code, leading to delays or potential litigation.
* **Key Takeaways**:
  + A regularly updated contributor list is essential to document the intellectual property (IP) chain of the software.
  + Knowing the contributors helps validate ownership and ensures proper credit and compliance with usage rights.

#### 4. Software Licensing Noncompliance

* **Lesson Number**: 1175
* **Title**: *Improper Integration of Third-Party Software Due to Licensing Confusion*
* **Summary**:  
  On several NASA projects, teams unknowingly reused third-party open-source software under licenses that did not permit redistribution within government systems or with other agencies. Failure to track the specific licensing restrictions or confirm proper usage rights resulted in the need to rewrite portions of the software to ensure compliance, causing delays and additional costs.
* **Relevance to the Requirement**:  
  Part of ensuring compliance when sharing software is maintaining visibility into any open-source or commercial software included in the software package. The contributor list must also identify external dependencies and licensing terms to confirm appropriate redistribution rights.
* **Key Takeaways**:
  + Ensure open-source and third-party software licenses are documented in the contributor list or README file.
  + Work with legal authorities early to confirm licenses align with NASA’s use and sharing policies.

#### 5. Failure to Communicate Software Limitations

* **Lesson Number**: 0886
* **Title**: *Lack of Proper Documentation Led to Misuse of Shared Software*
* **Summary**:  
  Software originally developed for scientific analysis tools was shared across NASA Centers but lacked adequate documentation outlining its limitations or intended scope of use. Another team integrated the software into a mission-critical system without realizing it was developed "as-is" and not validated for safety-critical functionality. This led to mission delays when issues arose during testing, requiring significant rework.
* **Relevance to the Requirement**:  
  This highlights the need to include explicit disclaimers in software documentation to clarify that the software is shared without warranty or guarantees of suitability for specific applications.
* **Key Takeaways**:
  + Clearly communicate limitations and intended use via disclaimers and documentation to avoid misuse.
  + Including disclaimers protects the distributing team and ensures shared software is not improperly integrated into critical systems without further validation.

#### 6. Regular Audits of Licenses and Legal Statements are Critical

* **Lesson Number**: 1647
* **Title**: *Unverified Software Created Reuse Failures*
* **Summary**:  
  A NASA Center hosting an internal reuse catalog was found to include software listings with incomplete or outdated licensing information and disclaimers. This created confusion and risks when other projects attempted to reuse the software. A later audit identified licenses that were incompatible with NASA policies, leading to the software being removed from the repository.
* **Relevance to the Requirement**:  
  Regular verification of software documentation, including contributor lists, disclaimers, and licensing rights, ensures the software can be reused without legal or operational complications.
* **Key Takeaways**:
  + Conduct periodic reviews of contributor records, license terms, and disclaimers for listed software.
  + Always ensure software listed in reuse catalogs is up to date and compliant with NASA requirements.

#### 7. Mismanagement of Minor Third-Party Contributions

* **Lesson Number**: 1276
* **Title**: *Untracked Third-Party Contributions Introduced Licensing Risks*
* **Summary**:  
  Minor contributions to software from external contractors or other collaborators went untracked during the software development process. When it came time to share the software internally, uncertainty about the ownership of small contributions delayed approval.
* **Relevance to the Requirement**:  
  Contributions by contractors, even minor ones, can introduce restrictions on sharing unless properly documented and accounted for. A robust contributor list helps identify external contributions and ensures proper approvals are in place.
* **Key Takeaways**:
  + Maintain a thorough record of all contributions, no matter how small, especially when external parties are involved.
  + Contact your Center’s Legal Office to clarify ownership and redistribution rights when contractors or collaborators are part of development.

### 6.1.2  Conclusion

The lessons above emphasize several key themes that align with the requirement:

1. **The importance of tracking contributors**: Regularly updated contributor lists prevent ownership disputes, simplify licensing compliance, and reduce approval delays.
2. **The necessity of disclaimers and indemnifications**: Clear software disclaimers protect NASA’s reputation, avoid liability, and minimize misuse.
3. **The importance of legal and licensing checks**: Ensuring rights to third-party and open-source components avoids costly rework and risk of noncompliance.

By integrating these lessons learned into small or large project workflows, NASA teams can minimize legal risks, ensure clarity in ownership, and enable successful sharing and reuse of software across the agency.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Coordination with Export Control Office](https://software.gsfc.nasa.gov/lesson-details/168/). **Lesson Number #**: The recommendation states: "Coordinate early in the project or release cycle with Export Control and Patent Counsel, via direct real-time communication."

# 7. Software Assurance

**SWE-217 - List of All Contributors and Disclaimer Notice**

2.1.5.15 The Center Director, or designee, (e.g., the Civil Servant Technical Point of Contact (POC) for the software product) shall perform the following actions:

a. Keep a list of all contributors to the software product.

b. Ensure that the software product contains appropriate disclaimer and indemnification provisions (e.g., in a “README” file) stating that the software may be subject to U.S. export control restrictions, and it is provided “as is” without any warranty, express or implied, and that the recipient waives any claims against, and indemnifies and holds harmless, NASA and its contractors and subcontractors.

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

The purpose of this requirement is to:

* Maintain a clear record of contributors to the software product for accountability, traceability, and compliance with NASA's intellectual property management policies.
* Ensure that software distributions include appropriate legal disclaimers and indemnification provisions to protect NASA, its contractors, and subcontractors from liability and to communicate terms of use, especially for software subject to export control laws.

Software Assurance (SA) personnel are responsible for verifying that software documentation includes these elements and ensuring the processes to maintain contributors' lists and enforce export control and legal disclaimers are followed.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Verify and Maintain Contributor Records

1. **Ensure a Complete List of Contributors**
   * Confirm that a list of contributors to the software product is compiled and maintained by the Civil Servant Technical POC or other designee.
   * Contributors' details should include, at a minimum:
     + Full name.
     + Role or area of contribution (e.g., coding, testing, documentation).
     + Affiliation, including contractor status, if applicable.
     + Contribution dates (e.g., start and end for specific work).
2. **Ensure Updates to the Contributor List**
   * Verify that the contributors' list is updated whenever new contributors join or leave the project. Consistent updates help maintain compliance and ensure traceability.
   * Check that the contributors' list is included in the software repository or tracked in a separate, clearly referenced document located in the project’s configuration management or version control system.
3. **Enable Traceability**
   * Ensure the contributor list is auditable and traceable to software artifacts, enabling the identification of development and assurance responsibilities.

#### 7.4.2.2  Verify the Inclusion of Required Disclaimers and Indemnification Provisions

1. **Verify the Disclaimer Language**
   * Confirm that the software product includes appropriate disclaimer and indemnification provisions in a visible and easily accessible location. Common places include:
     + A **README** file in the root directory of the software package.
     + An accompanying user manual or usage guide.
     + A prominent section of the software’s webpage or distribution notes (for web-based sharing).
   * The disclaimer provisions should include the following language:
     + A statement addressing **export control compliance**, such as:  
       "This software may be subject to U.S. export control laws and regulations. Recipients are responsible for obtaining all necessary licenses or other approvals for export."
     + A statement on the **"as-is" nature** of the software, such as:  
       "This software is provided 'as is,' without any warranty, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose."
     + An **indemnification provision**, such as:  
       "The recipient waives any claims against, and agrees to indemnify and hold harmless, NASA and its contractors and subcontractors from any claims, liabilities, damages, or losses arising out of its use of the software."
2. **Verify Correct Placement**
   * Confirm that the README file or equivalent document containing the disclaimers is included in every version of the distributed software (e.g., in source code repositories, build distributions, and any shared versions of the software).
3. **Compliance with Export Control Requirements**
   * Ensure that the disclaimer makes it clear that the software may be governed by U.S. export control laws and regulations (e.g., EAR or ITAR), and recipients are obligated to comply with those laws.
   * Confirm the Civil Servant Technical POC has addressed export control requirements in collaboration with NASA’s Export Control Office.

#### 7.4.2.3  Audit Compliance with These Requirements

1. **Validate Contributor List Maintenance**
   * During audits or reviews, verify that the software project has a complete, up-to-date, and accurate list of all contributors.
   * Ensure the list has been consistently updated at each major milestone, such as during code baseline releases or major revisions.
   * Confirm that the list can be traced back to the project’s version control system or related management tools.
2. **Review Documentation for Disclaimers**
   * Check the README file or equivalent document in the software package to verify it includes:
     + The proper "as-is" language, indemnification statements, and export control disclaimers.
     + Placement in the root directory or a similarly accessible location.
     + Consistent inclusion across different versions/releases of the software.
3. **Confirm Traceability**
   * Ensure that the record of contributors and the incorporated disclaimers are traceable in the project’s documentation repository, such as within software configuration management plans or distribution logs.

#### 7.4.2.4  Provide Feedback or Corrective Actions

1. **Identify and Address Gaps**
   * If the contributor list or disclaimers are incomplete or missing, document the gaps and provide these findings to the Civil Servant Technical POC or other responsible personnel.
   * Work with the project team to resolve these issues prior to software release or updates to the reuse catalog.
2. **Monitor Implementation of Fixes**
   * Track corrective actions through to completion and verify that updates to contributors' lists and disclaimer provisions are implemented properly.
3. **Report to Leadership**
   * Include findings related to contributor tracking and disclaimer compliance in software assurance reports submitted to the Center Director or designee.

#### 7.4.2.5. Promote Awareness and Process Improvements

1. **Educate Teams on Requirements**
   * Ensure that the Software Development and Software Assurance teams understand:
     + The need for maintaining up-to-date contributor records.
     + The importance of including legally required disclaimers and indemnification language in software products.
     + Export control requirements that govern the distribution of certain software products.
2. **Standardize Procedures**
   * Promote the use of standardized templates for README files or disclaimer text to ensure all projects properly address this requirement.
3. **Recommend Automation**
   * Recommend the use of automated tools and scripts to track contributor records within the version control system and ensure disclaimers are automatically included in distributed software packages.

### 7.4.3  Expected Outcomes

By implementing the above guidance, the following outcomes are achieved:

1. **Comprehensive Contributor Tracking**:
   * All contributors to a software product are traceable, providing accountability and clarity for intellectual property, licensing, and assurance reviews.
2. **Clear Disclaimer Compliance**:
   * Every shared software product includes appropriate disclaimers and indemnification provisions to protect NASA and its contractors.
3. **Reduced Legal and Export Risks**:
   * Export control disclaimers and licenses reduce risks of non-compliance with U.S. export regulations and mitigate liability concerns.
4. **Standardized Processes**:
   * Teams adopt consistent practices for tracking contributors and including required disclaimers, ensuring periodic conformance to standards.

### 7.4.4  Conclusion

Software Assurance (SA) personnel must verify that software projects maintain up-to-date contributor lists and include the proper disclaimers and indemnification provisions (e.g., in README files). This ensures compliance with legal, export control, and NASA-specific requirements, reducing risks associated with software sharing and reuse. Regular audits, process improvements, and team education are key activities for ensuring consistent adherence to these requirements.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-215 - Software License Rights](/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights) |
