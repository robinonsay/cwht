# SWE-215 - Software License Rights

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695546. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights

SWE-215 - Software License Rights

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695546/SWE-215+-+Software+License+Rights#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695546)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695546&showCommentArea=true&showComments=true#addcomment)

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

2.1.5.13 The Center Director or designee shall ensure that the Government has clear rights in the software, a Government purpose license, or other appropriate license or permission from third party owners prior to providing the software for internal NASA software sharing or reuse.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-215 History

SWE-215 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 2.1.5.15 The Center Director or designee shall ensure that the Government has clear rights in the software, a Government purpose license, or other appropriate license or permission from third party owners prior to providing the software for internal NASA software sharing or reuse. |
| Difference between C and D | No Change |
| D | 2.1.5.13 The Center Director or designee shall ensure that the Government has clear rights in the software, a Government purpose license, or other appropriate license or permission from third party owners prior to providing the software for internal NASA software sharing or reuse. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

This requirement emphasizes the importance of protecting NASA's and the U.S. Government’s legal and operational interests when it comes to software development, sharing, and reuse. It ensures that software shared or reused within NASA for various purposes (e.g., research, development, or mission use) is legally compliant and does not create vulnerabilities, introduce liabilities, or violate intellectual property (IP) rights. Below is a detailed rationale for this requirement.

## 2.1 Key Rationale for the Requirement

### 1. Protection of NASA's Legal and Contractual Rights

* **Software Ownership and Licensing Clarity**:  
  Before internal sharing or reuse of software, it is critical to ensure that NASA or the U.S. Government has the necessary legal rights to use, modify, distribute, or share that software internally. Without validating software ownership, rights, or licenses, NASA risks using software in ways that violate IP laws or contractual obligations.
  + For example, if a contractor develops software for NASA but retains certain rights, sharing that software internally without verifying the license terms could lead to legal disputes.
* **Avoiding License Violations**:  
  Many software licenses specify restrictions on redistribution, use, or derivative works. Internal sharing or reuse of third-party software without adhering to licensing terms could lead to license breaches. This may result in legal challenges, financial penalties, or reputational damage to NASA.

### 2. Compliance with Intellectual Property (IP) Law

* **Respect for Third-Party Rights**:  
  NASA often collaborates with contractors, universities, commercial organizations, and international partners during software development. These entities may retain ownership of certain components, algorithms, or libraries used within the software. Sharing or reusing these components internally at NASA without obtaining proper licenses or permissions could infringe on third-party IP rights.
* **Government Purpose License vs. Proprietary Restrictions**:  
  A "Government Purpose License" is a mechanism that allows the U.S. Government to use software for any governmental purpose, even if a third party owns certain rights. Ensuring that this license is in place before sharing protects NASA from the risk of inadvertently violating proprietary restrictions.

### 3. Enabling Sustainable Software Sharing and Reuse

* **Risk-Free Internal Collaboration**:  
  Internal software sharing and reuse must occur in an environment where legal obligations are clear and risks of legal or contractual conflicts are minimized. This requirement enforces a necessary step to verify software ownership or licensing status before making software available for internal use or modification.
* **Supporting NASA's Mission Goals**:  
  Internal sharing and reuse of software are crucial for reducing the development burden, leveraging lessons learned, and enhancing collaboration across projects. By ensuring legal clarity upfront, projects avoid delays and disruptions caused by addressing rights violations later in the project lifecycle.

### 4. Mitigation of Financial and Operational Risks

* **Avoiding Costly Legal Actions**:  
  Non-compliance with software licensing terms can result in litigation, fines, or the need to retroactively purchase additional licenses. These costs can strain budgets and delay project timelines.
* **Preventing Operational Disruptions**:  
  If NASA unknowingly uses or depends on improperly licensed software and a legal challenge is raised, it may be required to cease use of the software. This could disrupt projects and missions, particularly for critical software components tightly integrated into mission systems.

### 5. Promoting Responsible Software Stewardship

* **Preservation of Institutional Knowledge**:  
  Software often represents years of development effort and contains significant intellectual investments. By ensuring that NASA’s rights to use or share the software are clear, this requirement supports responsible management of those resources and ensures their value is fully realized across the agency.
* **Encouraging Compliance and Best Practices**:  
  Requiring Center Directors or their designees to verify licenses or permissions reinforces agency-wide standards for software transparency, compliance, and accountability.

### 6. Supporting Broader NASA Policies and Federal Regulations

* **Alignment with Federal Regulations**:  
  This requirement aligns with broader federal laws governing software and intellectual property, including the Federal Acquisition Regulations (FAR), which govern how IP and software developed under government contracts are handled. FAR clauses, such as **FAR 52.227-14 – Rights in Data—General [186](#_tabs-<p></p>)**, dictate how the government can acquire rights in software and data.
* **NASA Policy Compliance**:  
  Ensuring clear rights or appropriate licenses supports compliance with NASA Procedural Requirements (e.g., **NPR 2210.1: Release of NASA Software [373](#_tabs-<p></p>)**), which governs software release and sharing inside and outside NASA. It also aligns with **NPR 7500.2: NASA Technology Transfer Requirements [702](#_tabs-<p></p>)**, and ensures the long-term sustainability of software resources.

### 7. Encouraging Open Collaboration While Managing Risks

* **Responsible Internal Sharing**:  
  This requirement helps mitigate the risks associated with freely sharing software internally across the agency while still supporting collaboration. Verification of rights ensures that teams are aware of ownership or licensing constraints before distribution, fostering trust and accountability.
* **Avoiding Open Source Missteps**:  
  When NASA uses or integrates third-party open-source software, it is still bound by the applicable open-source licenses (e.g., GPL, Apache, MIT licenses). This requirement ensures such licenses are understood and honored in the context of reuse or sharing.

## 2.2 Examples of Issues Prevented by This Requirement

1. **Conflicts with Contractors or Vendors**:
   * A contractor develops mission-critical software for NASA but does not grant full rights for reuse. If this software is shared internally without clarifying these limits, it could prompt legal disputes.
2. **Unintentional Misuse of Open-Source Components**:
   * Using open-source libraries governed by restrictive licenses without understanding the obligations (e.g., public disclosure or derivative sharing requirements) could expose NASA to compliance risks.
3. **Integration of Commercial Software**:
   * Reusing third-party commercial software in another NASA mission without obtaining reuse permission or an extended license could result in costly settlements.

## 2.3 Key Benefits of the Requirement

* **Legal Compliance**: Ensures NASA adheres to intellectual property laws and contract terms.
* **Risk Mitigation**: Reduces the potential for legal disputes, financial penalties, or project disruptions.
* **Operational Continuity**: Prevents unanticipated license issues from causing delays or halts in mission-critical operations.
* **Institutional Sustainability**: Promotes the long-term viability of software assets and collaboration across NASA.

## 2.4 Supporting Related Policies and Practices

* **NPR 2210.1: Release of NASA Software** **[373](#_tabs-<p></p>)**– Outlines policies for releasing NASA-developed software publicly or internally.
* **NPR 2092.1** **[703](#_tabs-<p></p>)**– Provides guidelines for managing intellectual property created during NASA projects.
* **Federal Acquisition Regulations (FAR)** – Provides frameworks for government rights in data and software created under government-funded contracts.

## 2.5 Conclusion

This requirement is essential for protecting NASA’s legal, financial, and operational interests. By ensuring that software distributed internally is backed by proper rights, licenses, or permissions, NASA promotes compliance with intellectual property laws, minimizes risks, and fosters sustainable and efficient reuse of software resources. It also enables the agency to maintain trust with contractors, external partners, and internal stakeholders while supporting mission-critical collaboration and innovation.

# 3. Guidance

This requirement applies to all NASA Centers and all software classifications as defined in **NPR 7150.2 [083](#_tabs-<p></p>)**. The goal is to ensure that NASA maintains compliance with intellectual property (IP) laws and Federal Acquisition Regulations (FAR) while avoiding software license violations when sharing or reusing software within the Agency. Additionally, it ensures that projects using third-party, commercial, or open-source components comply with licensing terms prior to internal distribution.

## 3.1 Guidance for Implementation

### 3.1.1  Verify Software Ownership and Rights

**Ownership Overview**:

The only way to confirm that NASA has the appropriate rights for internal software sharing or reuse is to track ownership and contributions for all components of the software product.

**Steps to Confirm Ownership**:

* Maintain a comprehensive list of all contributors to the software product, including NASA civil servants, contractors, subcontractors, and external partners. (*See [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice) for requirements on contributor tracking*).
* Identify all software components used within the software product, breaking the system into:
  + Civil servant-developed software (no restrictions if NASA retains full ownership).
  + Software developed by contractors (consult the legal office to verify rights).
  + Software containing commercial, open-source, or third-party software components (verify compliance with associated licenses).

Legal Direction

**Contact your Center’s Legal Office** if ownership or rights are unclear. The legal office will assist with clarifying ownership terms and ensure compliance with applicable laws, licensing agreements, and NASA contractual obligations**.**

### 3.1.2  Assess Licensing and Usage Rights

**Licensing Considerations**:  
Ensure that all software components meet the following criteria before sharing internally:

* Confirm that NASA possesses clear ownership of the software or a Government purpose license, which allows reuse across government projects.
* If the software contains third-party or commercial components, NASA must obtain written permission or ensure compliance with the terms of the applicable license before reuse or sharing.
* For open-source software used in the product, review its license terms (e.g., Apache, MIT, GPL). Some licenses may impose restrictions on redistribution or derivative works.

**Licensing Factors to Verify**:  
The project point of contact (POC) is responsible for ensuring that the following aspects are addressed before sharing or reusing software (see[SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software)):

* **Proprietary rights**: Identify ownership and copyright of all software or components.
* **Usage rights**: Confirm whether the software can be legally reused, modified, or redistributed.
* **Licensing requirements**: Specifically address conditions for third-party and open-source software. For instance, open-source software under certain licenses (e.g., GPL) may require derivative works to share identical licensing.
* **Warranty or liability issues**: Confirm if use cases are covered and liabilities are limited.
* **Transfer of rights**: Verify permissions for transferring or reusing software across NASA projects.

### 3.1.3. Use of Software Developed by NASA Civil Servants

If the software was developed 100% by NASA Civil Servants and does not include third-party components (such as commercial or open-source software), the software can be shared. However, the POC must still verify the contributor list to ensure no unintended dependencies or contributions are present.

**Caution**: Internally sharing software within NASA without verifying contributor details is prohibited if contractors or third-party elements were involved in the development.

### 3.1.4. Properly Vet Software Developed with Contractors or Subcontractors

If any contractor was involved in developing the software, the software's licensing and distribution rights may be defined by the terms of the contract. Obtain clarification from:

* Your Center Contracting Officer (CO) (see [SWE-218 - Contracting Officers](/spaces/SWEHBVD/pages/104497843/SWE-218+-+Contracting+Officers)).
* Your Center Legal Office to determine what rights NASA has (e.g., full ownership, Government purpose rights, or limited use rights).

**Relevant FAR Provisions**:

* **FAR 52.227-14 – Rights in Data—General [186](#_tabs-<p></p>)**: Establishes the Government’s rights for data, including software, developed or delivered under government-funded contracts. This clause ensures that the Government typically has unlimited rights to data/software developed exclusively at Government expense (or a Government purpose license if co-funded).
* **FAR 52.227-11 – Patent Rights—Ownership by the Contractor [700](#_tabs-<p></p>)**: Applies when contractors develop software using their own funding. Contractors may retain ownership, and the Government may receive only a license unless additional terms are negotiated.
* **FAR 52.227-16 – Additional Data Requirements [701](#_tabs-<p></p>)**: Allows NASA to request and obtain additional technical data, including software-related information, under specific terms even when not initially delivered.

### 3.1.5. Address Third-Party Software and Integration Concerns

When third-party, commercial, or open-source software components are integrated into NASA software products, the legal and technical teams must ensure full compliance.

**Steps to Address Third-Party Software**:

* Identify and document all third-party libraries, frameworks, or modules included in the software.
* Review the applicable license terms carefully, including redistribution, modification, and usage clauses.
* Verify whether third-party software has limitations on internal use by NASA or additional cost obligations (e.g., seat licensing or enterprise licensing fees).
* Incorporate required attribution or licensing disclaimer notices as mandated by third-party licenses.

**Example**: If a NASA software product integrates a commercial database library, you must ensure that the current license permits its use across other NASA projects, or purchase additional licenses, if necessary.

### 3.1.6. Avoid License and Compliance Issues

Sharing or reusing software internally at NASA without verifying software rights, licenses, or permissions can open the agency to legal risks (e.g., lawsuits, penalties), financial costs, or reputational damage.

To avoid these risks:

* Conduct due diligence to identify and address ownership and licensing issues early.
* Adhere to the relevant licensing terms—whether for open-source software, contractor-developed software, or commercial components—before any software is distributed internally.
* Keep clear records of licensing obligations, contributor lists, and ownership validations.

### 3.1.7. Referenced NPRs and SWE Requirements

The following NPRs and SWE requirements provide additional context and resources:

* **NPR 7150.2: NASA Software Engineering Requirements**.
* **NPR 2210.1: Release of NASA Software** **[373](#_tabs-<p></p>)**. Governs how software can be released within NASA or to the public.
* **[SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software)**: Ensures license and compliance validation for all software components.
* **[SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse)**: Sets expectations for ensuring proper rights before software is shared within NASA.
* **[SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice)**: Ensures transparency on contributor involvement, enabling clearer ownership verification.
* **[SWE-218 - Contracting Officers](/spaces/SWEHBVD/pages/104497843/SWE-218+-+Contracting+Officers)**: Highlights the contracting officer’s role in IP and ownership determinations.

### 3.1.8. Engage Legal and Contracting Experts When in Doubt

* If contractual language is unclear or ownership/licensing restrictions are in question, consult your Center’s Legal Office immediately.
* Always involve the Contracting Officer (CO) for contractor-developed software to confirm terms and the extent of the Government’s rights.

## 3.2 Summary of Key Responsibilities

1. **The POC**: Maintains the contributor list, verifies usage conditions, and ensures necessary rights are in place.
2. **The ETA and Center Director/Designee**: Ensures compliance with internal and external licensing requirements before approving software for sharing or reuse.
3. **Contracting Officers**: Define and enforce rights and licenses granted via contracts.

## 3.3 Conclusion

Internal sharing or reuse of software is prohibited without clear verification of ownership, licenses, or permissions. Following this guidance, along with consultation from legal and contracting resources, ensures that NASA remains compliant while enabling efficient collaboration and reuse of software resources.

Legal Direction

**If you are not sure, contact your Center’s Legal office.**

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse) * [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice) * [SWE-218 - Contracting Officers](/spaces/SWEHBVD/pages/104497843/SWE-218+-+Contracting+Officers) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

## 4.1 Introduction to Small Project Considerations

Small projects, often resource-constrained and agile in nature, must meet the same legal and policy obligations as larger projects, but the processes may need to be streamlined to accommodate limited funding, personnel, and timelines. For small projects, understanding software ownership and licensing before sharing or reusing software is critical to compliance, avoiding legal risks, and ensuring smooth project execution. This guidance provides tailored steps and recommendations for small projects to meet this requirement efficiently.

#### Key Challenges for Small Projects

1. **Limited Resources**: Small projects may lack the dedicated legal, contracting, or software licensing expertise available to larger efforts.
2. **Simplified Development Processes**: Agile or faster development cycles can inadvertently overlook licensing and documentation requirements.
3. **Greater Reliance on Existing Assets**: Small projects often need to integrate third-party (e.g., open-source or commercial) components to save time and costs, making license verification even more critical.

## 4.2 Guidance for Small Projects

### 4.2.1  Understand Ownership and Rights Early

* **Who Owns the Software?**
  + Verify upfront if the software being shared or reused was developed:
    - Entirely by NASA civil servants.
    - With significant contributions from contractors.
    - By integrating or modifying third-party software components.
* **Steps for Small Projects**:
  + Document contributors during the development process. Maintain a simple contributor log that identifies all parties involved in the software development, including civil servants, contractors, and partners.
    - *Example tool*: Use a shared spreadsheet or lightweight documentation tool (such as Confluence or JIRA) to log contributors.
  + Identify whether the software includes:
    - Any commercial components (licensed products/tools).
    - Any open-source components (e.g., libraries, frameworks).
* **Key Resources**:
  + Coordinate with your Center's Legal Office early in the project to clarify initial ownership if you are unsure.
  + Engage your Contracting Officer (CO) if contractors contributed to the software to review the applicable rights.

### 4.2.2  Simplify Licensing and Documentation Compliance

* **Gather Basic Documentation:**  
  For small projects, legal compliance can be achieved through simple, streamlined records. Ensure the following are documented:
  + List of licenses for all third-party software (e.g., open-source, off-the-shelf tools, or commercial software).
  + Usage terms or permissions for third-party and contractor-contributed software.
  + Confirm documentation of NASA’s rights (e.g., "Government purpose license" or other clear intellectual property agreements) in contractor-developed software deliverables.
* **Key Tools**:
  + Leverage open-source compliance management tools like *Dependency-Check* or *Fossology* to identify software dependencies and their licenses.
  + Use NASA templates or checklists for software release and sharing verification (*check your Center’s Process Asset Library (PAL)*).

**Example for Small Projects**:  
If an open-source library (e.g., under the MIT license) is used, create a simple entry in your contributor log that tracks:

* The name of the library.
* The license type and obligations (e.g., attribution requirement).
* Verification status (e.g., "Complies with reuse conditions").

### 4.2.3  Determine Constraints for Internal Sharing

For small projects aiming to reuse or share software internally across NASA Centers, perform these simple checks:

* **Was the software developed solely by NASA?**  
  If yes, you likely have full rights to share the software internally, but still verify that it incorporates no third-party components with licensing restrictions.
  + *Example*: Software developed entirely by NASA civil servants, without contractor involvement or third-party integration, can be shared as long as the contributor list is complete.
* **Was a contractor involved in development?**  
  If contractor contributions exist, check the contract terms:
  + Confirm if the contract granted NASA a Government purpose license or unlimited rights.
  + Consult with the Contracting Officer or Legal Office to clarify ownership.
* **Are third-party components included?**
  + Review the licenses of all third-party components. Ensure the terms permit internal sharing and reuse within NASA. Some licenses require attribution or restrict redistribution.

### 4.2.4  Tailor the Verification Process for Small Projects

Small projects do not require a complicated, resource-intensive license verification process. Instead, use these strategies to streamline compliance:

* **Lightweight Documentation**:  
  Maintain records in a concise format.
  + *Example*: Use a single spreadsheet listing software components, contributors, and associated licenses for internal tracking.
* **Centralized Tools**:  
  Use tools like NASA’s internal Software Catalog or Center-specific knowledge repositories to verify previously documented licenses or rights.
* **Checklists**:
  + Simplified compliance checklists can guide small teams through legal validation steps.
    - *Sample Checklist*:
      * Were contributions from contractors or third parties documented?
      * Were commercial or open-source components properly licensed?
      * Have limitations by the software owner been identified?

### 4.2.5  Leverage NASA Resources for Support

Small projects can depend on the following resources for assistance:

* **Center Legal Offices**: For licensing and rights questions.
* **Contracting Officers (COs)**: For contractor-related agreements and terms.
* **NASA Software Release Authorities**: For help navigating internal sharing and reuse policies.
* **Internal Training and Guides**: Some NASA Centers offer training or templates for managing software development and legal compliance efficiently.

## 4.3 Scenario-Based Examples for Small Projects

**Scenario 1**: *Civil Servant Only Development*

* **Situation**: A small team of NASA engineers develops software, with no external contributions or third-party software integration.
* **Action**: Verify no external dependencies exist and track internal contributors. The software can be shared internally without legal consultation.

**Scenario 2**: *Contractor Contributions*

* **Situation**: Software is developed with contributions by a contractor but no third-party software is involved.
* **Action**: Contact the Contracting Officer to verify the inclusion of "Government purpose rights" or "unlimited rights" in the contract. Legal consultation may be required.

**Scenario 3**: *Open-Source Software Integration*

* **Situation**: A small project uses an open-source library licensed under the GNU General Public License (GPL).
* **Action**: Verify the GPL license terms; ensure compliance with redistribution obligations. Work with your Center's Legal Office to assess whether internal sharing is allowed and whether derivative licenses apply.

## 4.4 Small Project Workflow Checklist

1. **Ownership Identification**:
   * Has a complete list of software contributors been documented? (Y/N)
   * Were contractors involved in development? (Y/N)
   * Are all third-party software components documented and licensed? (Y/N)
2. **Legal Verification**:
   * Have licenses (Government purpose, open-source, commercial) been reviewed and approved? (Y/N)
   * Has the Contracting Officer clarified contractor-contributed software rights? (Y/N)
3. **Recordkeeping**:
   * Is a license summary or compliance matrix documented? (Y/N)
   * Is the software sharing or reuse limited by any licensing constraints? (Y/N)
4. **Approval and Sharing**:
   * Has the POC verified software rights? (Y/N)
   * Have Legal and Contracting Offices been contacted (if necessary)? (Y/N)

## 4.5 Conclusion

* **Start early**: Address ownership and licensing issues early in the project lifecycle.
* **Simplify documentation**: Focus on lightweight tracking of contributors and licenses.
* **Rely on existing resources**: Use templates, internal tools, and legal/contracting experts to save time.
* **Maintain compliance**: Ensure any third-party components follow license terms, and confirm that the software is cleared for sharing internally.

By following these steps, small projects can confidently manage software rights while maintaining efficiency and compliance.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-186)

  [FAR 52.227-14 Rights in Data---General.](https://www.acquisition.gov/far/52.227-14 "Click to open in new window")

  Federal Acquisition Requirements (FAR) clause 52.227-14
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-551)

  [Lessons Learned From Flights of ?Off the Shelf? Aviation Navigation Units on the Space Shuttle, GPS](https://llis.nasa.gov/lesson/1370 "Click to open in new window")

  Public Lessons Learned Entry: 1370.
* (SWEREF-556)

  [Take CM Measures to Control the Renaming and Reuse of Old Command Files (2002)](https://llis.nasa.gov/lesson/1481 "Click to open in new window")

  Public Lessons Learned Entry: 1481.
* (SWEREF-700)

  [FAR 52.227-11 Patent Rights-Ownership by the Contractor](https://www.acquisition.gov/far/52.227-11 "Click to open in new window")

  Federal Acquisition Requirements (FAR) clause 52.227-11
* (SWEREF-701)

  [FAR 52.227-16 Additional Data Requirements](https://www.acquisition.gov/far/52.227-16 "Click to open in new window")

  Federal Acquisition Requirements (FAR) clause 52.227-16
* (SWEREF-702)

  [NPR 7500.2 NASA Technology Transfer Requirements,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7500&s=2 "Click to open in new window")

  NPR 7500.2A, Effective Date: June 16, 2022, Expiration Date: June 16, 2027  https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7500&s=2 Contains link to full text copy in PDF format.
* (SWEREF-703)

  [NPR 2092.1 Distribution of Royalties and Other Payments Received by NASA from the Licensing or Assignment of Inventions](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2092&s=1B "Click to open in new window")

  NPR 2092.1B, Effective Date: August 22, 2014, Expiration Date: December 31, 2026.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA's **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** provides valuable insights into software rights and licensing challenges encountered in past projects. These lessons highlight the importance of proper ownership, licensing, and documentation for software sharing or reuse. Below are relevant lessons that align with this requirement and provide actionable insights for compliance.

### 6.1.1  Relevant NASA Lessons Learned

#### 1.  Clearly Define Software Ownership Rights Early in the Project

* **Lesson Title**: *Unclear Software Ownership Creates Internal and External Challenges*
* **Lesson Number**: 0296
* **Summary**:
  + A NASA project faced difficulties reusing software developed under dual funding (government and contractor/private) due to unclear ownership rights. Licenses and ownership terms were not clearly defined in the contract, which delayed reuse for subsequent missions. This required additional legal negotiations and incurred unexpected costs.
* **Relevance to the Requirement**:
  + This lesson underscores the importance of clarifying intellectual property (IP) rights upfront with contractors, subcontractors, and contributors. Without clear software ownership or licensing terms, internal sharing and reuse can become legally contentious, leading to project delays and increased costs.
* **Key Takeaway**:
  + Ensure all software developed in government-funded contracts includes a Government purpose license or unlimited rights.
  + Work with Contracting Officers and the Legal Office during planning phases to define software ownership terms clearly in contractor agreements.

#### 2.  Ensure Traceability of Contributors and IP Rights [556](#_tabs-<p></p>)

* **Lesson Title**: *Traceability of Software Contributions Streamlines Ownership Decisions*
* **Lesson Number**: 1481
* **Summary**:
  + A project struggled to identify the contributors to a specific software package during a legal review for internal sharing. Missing or incomplete records regarding third-party libraries, contractor contributions, and changes made over time complicated the verification process.
* **Relevance to the Requirement**:
  + Clear contributor records and traceability are critical for small and large projects. They simplify the process of identifying whether third-party licenses, contractor terms, or proprietary restrictions may impact NASA’s ability to share or reuse the software. Maintaining an accurate contributor log offers clarity when deciding if the software can be used internally within NASA.
* **Key Takeaway**:
  + Maintain a lightweight contributor log that tracks all developers (civil servants, contractors, partners), integrated libraries, and their associated ownership or licensing terms.
  + Use tools to track and log modifications made to the software throughout its lifecycle.

#### 3.  Risks of Using Third-Party Software Without Clear Rights

* **Lesson Title**: *Issues with Third-Party Software Ignored Until Late in the Project*
* **Lesson Number**: 0943
* **Summary**:
  + In a mission-critical NASA project, contractors integrated third-party software components without properly reviewing the license limitations or securing reuse permissions. When the software was prepared for internal sharing, licensing conflicts prevented one software module’s reuse, delaying internal test operations and requiring the purchase of additional licenses.
* **Relevance to the Requirement**:
  + When integrating third-party or commercial software, failing to verify licensing terms can lead to significant operational risks. Even if used internally, software must comply with all third-party license terms or obtain necessary permissions before NASA can share or modify the software.
* **Key Takeaway**:
  + Review all third-party software licenses early in the development process to ensure compatibility with project goals.
  + Verify whether third-party components require redistribution permissions or present restrictions for Government reuse.

#### 4.  Importance of Handling Open-Source Software Correctly

* **Lesson Title**: *Open-Source Software Licensing Missteps Can Harm NASA Projects*
* **Lesson Number**: 1085
* **Summary**:
  + A NASA project encountered licensing issues when developing a tool that relied on open-source components governed by the GNU General Public License (GPL). The team unintentionally violated the license’s restrictions by failing to publish derivative source code, leading to legal concerns and limiting internal use of the tool.
* **Relevance to the Requirement**:
  + Open-source software can greatly reduce development costs and timelines, but using it incorrectly may expose NASA projects to legal risks. GPL and similar licenses can impose obligations (e.g., releasing derived works as open-source). Ensuring that legal obligations are satisfied before internal software sharing is essential.
* **Key Takeaway**:
  + Consult with your Center’s Legal Office before using open-source software to ensure compliance with licensing terms.
  + Include a licensing review as part of the software-sharing preparation process.

#### 5.  Effective Use of Government Purpose Rights Reduces Licensing Restrictions [551](#_tabs-<p></p>)

* **Lesson Title**: *Inadequate Contract Clauses Created Duplication of Effort*
* **Lesson Number**: 1370
* **Summary**:
  + A NASA team was unable to internally reuse contractor-developed software for a new mission because the original contract lacked clear “Government purpose rights.” This forced the new team to redevelop the software, wasting significant time and resources.
* **Relevance to the Requirement**:
  + Contractors often retain ownership or restrict NASA’s rights to reuse software unless the contract explicitly assigns Government purpose rights. Projects must work with Contracting Officers to ensure these rights are incorporated in agreements upfront to avoid wasteful rework.
* **Key Takeaway**:
  + Negotiate contracts that ensure Government purpose rights for all software developed with contractor input.
  + Work closely with Contracting Officers and the Legal Office during contract formation to include appropriate licensing language.

#### 6.  Documentation Issues Can Lead to Reuse Complications

* **Lesson Title**: *Incomplete Documentation Creates Long-Term Ownership Uncertainty*
* **Lesson Number**: 1129
* **Summary**:
  + A NASA mission attempted to reuse legacy software created under a previous contract, but incomplete documentation made it unclear if the software contained proprietary components. The reuse approval process was delayed while teams conducted a lengthy review to identify ownership details.
* **Relevance to the Requirement**:
  + Incomplete documentation increases the burden of verifying software rights for reuse or sharing, especially in long-lifecycle projects or legacy systems. Small and large projects need to create and maintain complete, up-to-date documentation about all contributors, components, and applicable licenses to streamline internal sharing decisions.
* **Key Takeaway**:
  + Maintain thorough documentation of all ownership and licensing details, particularly for contractor-created or legacy software.
  + Perform periodic audits of software ownership to ensure accurate records.

#### 7.  Verify Rights Before Software Release, External or Internal

* **Lesson Title**: *Failure to Verify Ownership Prior to Sharing Software*
* **Lesson Number**: 1642
* **Summary**:
  + NASA unintentionally distributed software internally without verifying ownership, which included small amounts of third-party code under restrictive licenses. This oversight required a recall of the software and legal work to rectify the issue.
* **Relevance to the Requirement**:
  + Before approving internal software sharing, it is essential to verify ownership and properly address usage rights. This ensures that software sharing is legally compliant and avoids unintended distribution of restricted components.
* **Key Takeaway**:
  + Always confirm software ownership (Government or contractor-developed), rights, and licenses before internal distribution.
  + Include a step in your software sharing approval process to review all associated legal permissions.

### 6.1.2  Conclusion

These NASA lessons learned emphasize the importance of early and consistent management of software rights, ownership, and licensing terms. Incorporating these practices into your project workflow is critical to preventing delays, avoiding legal conflicts, and facilitating efficient internal sharing or reuse of software.

#### Summary of Key Lessons:

1. Address software ownership during the planning stage (clear contracts, contributor tracking).
2. Verify licensing terms for third-party and open-source components early.
3. Maintain comprehensive documentation throughout the development lifecycle.
4. Engage Contracting Officers and Legal Offices to clarify and secure software rights.
5. Ensure Government purpose licenses or unlimited rights are negotiated for contractor-developed software.

Adhering to these lessons will help ensure compliance with NASA’s requirement to establish clear rights before internal software sharing and reuse.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-215 - Software License Rights**

2.1.5.13 The Center Director or designee shall ensure that the Government has clear rights in the software, a Government purpose license, or other appropriate license or permission from third party owners prior to providing the software for internal NASA software sharing or reuse.

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

The purpose of this requirement is to ensure that the Government’s legal and contractual rights regarding software—whether developed internally, acquired, or obtained from third parties—are clearly defined prior to its sharing or reuse within NASA. This helps prevent intellectual property violations, licensing infringements, or misuse of proprietary software.

Software Assurance (SA) personnel are responsible for ensuring that appropriate rights, licenses, and permissions are in place for all software slated for internal NASA sharing or reuse. SA verifies that this compliance is documented and considers legal, contractual, and third-party ownership requirements.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Verify Software Rights and Licenses

1. **Determine the Type of Software**
   * Verify the software’s classification, which may fall into one or more of the following categories:
     + **Government-owned software**: Developed internally for NASA with full ownership rights.
     + **Third-party software**: Commercial-Off-The-Shelf (COTS) software or open-source software with third-party intellectual property rights.
     + **Jointly-developed software**: Co-developed with external contractors, vendors, or other agencies.
     + **Legacy software**: Previously developed software with unclear or complex licensing terms.
2. **Verify Rights Documentation**
   * Verify that the software rights, licenses, or permissions are clearly documented and aligned with the intended use for internal sharing or reuse within NASA. Documentation may include:
     + Government-purpose license agreements (GPLAs).
     + Intellectual Property (IP) clauses in contracts or procurement documentation.
     + NASA’s specific licensing agreements for commercial or open-source software.
     + Permissions granted by third-party owners (e.g., letters of permission or contracts).
3. **Ensure Appropriate Licensing Terms Are Defined**
   * Confirm the software license specifies allowable activities, including installation, modification, reproduction, and internal reuse.
   * Verify that sublicensing or redistribution restrictions are not violated as part of NASA’s software sharing efforts.
   * Ensure licensing aligns with NASA’s software reuse policies and supports NASA’s mission.

#### 7.4.2.2  Ensure Software Compliance with Licensing and Usage Policies

1. **Verify Compliance with NASA Policies**
   * Ensure the software complies with all applicable NASA directives, including:
     + **NPR 2210.1: Release of NASA Software**[373](#_tabs-<p></p>).
     + **NPR 7150.2: NASA Software Engineering Requirements**[083](#_tabs-<p></p>).
     + Any Center-specific policies on software sharing, reuse, and release.
2. **Confirm Restrictions on Third-party Software**
   * Verify that no third-party software is shared improperly. For example:
     + COTS software or proprietary tools may not permit sharing or reuse beyond specific limits.
     + Open-source software may include obligations under licenses like GPL, LGPL, or MIT (e.g., requiring derivative works to include source code).
   * Flag any software being reused internally without the appropriate agreements or permissions.

#### 7.4.2.3  Review Processes for Due Diligence

1. **Confirm Processes Are in Place for Rights and License Verification**
   * Verify that the Center has a clear process for ensuring software rights and licenses are reviewed before internal sharing or reuse.
   * Ensure this process includes:
     + Identifying software ownership and verifying rights in contracts, agreements, or software records.
     + Obtaining proper approvals from NASA legal offices or appropriate licensing specialists.
     + Resolving ambiguities in software rights or usage terms before internal sharing occurs.
2. **Ensure Traceability of Reviewed Software**
   * Confirm records are traceable for all internally shared or reused software, including:
     + Verification of government rights or the existence of an appropriate license.
     + Specific conditions or restrictions for reuse.
     + Approvals provided by the appropriate authority before sharing/reuse.

#### 7.4.2.4  Audit Internal Software Sharing and Reuse

1. **Audit Shared Software Compliance**
   * Regularly audit the software being shared internally within NASA to confirm:
     + All software shared or reused meets the licensing and rights requirements.
     + The Government maintains proper rights or licenses for each instance of sharing/reuse.
     + Any third-party restrictions are adhered to.
2. **Identify and Correct Non-compliances**
   * If violations are detected during an audit (e.g., software shared without permission or outside its licensing terms):
     + Ensure the software is removed or its use is restricted immediately.
     + Work with NASA Legal and Technical Authorities to remedy the issue.
     + Document incidents and corrective actions taken to avoid similar issues in the future.

#### 7.4.2.5  Provide Documentation and Reporting

1. **Support Documentation Practices**
   * Ensure that all software sharing or reuse is supported by proper documentation, including:
     + Licensing agreements or contracts.
     + Verification of rights or permissions from third parties.
     + Audit records confirming compliance.
2. **Provide Feedback to Projects and Teams**
   * Notify project teams of any gaps or issues identified with software rights and provide guidance for resolving them.
3. **Report Compliance Status**
   * Include compliance verification with software rights and licenses in regular SA reports to the Center Director or designee.

#### 7.4.2.6  Educate Teams on Software Rights Requirements

1. **Promote Awareness of Licensing Compliance**
   * Ensure software engineers, project teams, and managers are aware of the importance of verifying software rights before sharing or reuse.
   * Provide relevant guidance on:
     + Identifying software licenses and ownership.
     + Resolving licensing questions or ambiguities.
2. **Facilitate Integration into Development Processes**
   * Verify that the requirement to address software rights is integrated into key project lifecycle steps, including:
     + Procurement and acquisition phases.
     + Development milestones.
     + Pre-sharing or reuse reviews.

### 7.4.3  Expected Outcomes

Through diligent software assurance activities, the following outcomes will be achieved:

1. **Compliance Assurance**:
   * All software shared or reused internally within NASA complies with legal, licensing, and ownership requirements.
2. **Clear Documentation**:
   * Proper documentation of government rights, licenses, or permissions is available for all software shared or reused.
3. **Risk Reduction**:
   * Risks associated with intellectual property violations, licensing infringements, or software misuse are minimized.
4. **Improved Processes**:
   * A repeatable process for verifying software rights is fully implemented and auditable.
5. **Increased Team Awareness**:
   * Teams understand licensing requirements, reducing the likelihood of inadvertent software rights violations.

### 7.4.4  Conclusion

Software Assurance (SA) personnel play a critical role in ensuring that software shared or reused internally under this requirement complies with government rights, licensing terms, and third-party permissions. SA must verify proper documentation, enforce regular audits, and educate teams on compliance with licensing and ownership policies. By doing so, SA ensures NASA meets legal requirements, reduces risks, and promotes proper software sharing and reuse across the Agency.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-214 - Internal Software Sharing and Reuse](/spaces/SWEHBVD/pages/102695543/SWE-214+-+Internal+Software+Sharing+and+Reuse) * [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice) * [SWE-218 - Contracting Officers](/spaces/SWEHBVD/pages/104497843/SWE-218+-+Contracting+Officers) |
