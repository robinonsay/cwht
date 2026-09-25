# SWE-006 - Center Software Inventory

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695396. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695396/SWE-006+-+Center+Software+Inventory

SWE-006 - Center Software Inventory

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695396/SWE-006+-+Center+Software+Inventory#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695396)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695396&showCommentArea=true&showComments=true#addcomment)

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

2.1.5.6 Center Director, or designee, shall maintain a reliable list of their Center’s programs and projects containing Class A, B, C, and D software. The list should include: 

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

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-006 History

SWE-006 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 1.2.5 To support compliance with NASA policy and facilitate the application of resources to mitigate risk, the NASA Headquarters' Chief Engineer, in coordination with the Chief, Safety and Mission Assurance, shall maintain a reliable list of the Agency's programs and projects containing software. |
| Difference between A and B | Shifted responsibility  for maintaining list of programs and projects to each Centers and based it on class. Removed effort to support compliance with NASA policies and risk mitigation. |
| B | 2.1.3.8 Center Directors, or designees, shall maintain a reliable list of their Center's programs and projects containing Class A, B, C, and D software. The list should include:  a. Project/program name and Work Breakdown Structure (WBS) number.  b. Software name(s) and WBS number(s).  c. Software size estimate (report in Kilo/Thousand Source Lines of Code (KSLOCs)).  d. Phase of development or operations.  e. Safety-Critical Software (Yes or No).  f. Software Class or list of the software classes being development on the project.  g. For each Computer Software Configuration Item (CSCI)/Major System containing Class A, B, or C software, provide:  (1) The name of the software development organization.  (2) Title or brief description of the CSCI/Major System.  (3) The estimated total KSLOC the CSCI/Major System represents.  (4) The primary programming languages used.  (5) Primary life cycle methodology being used on the software project.  (6) Name of responsible software assurance organization(s). |
| Difference between B and C | No Change |
| C | 2.1.5.8 Center Director, or designee, shall maintain a reliable list of their Center’s programs and projects containing Class A, B, C, and D software. The list should include:  a. Project/program name and Work Breakdown Structure (WBS) number.  b. Software name(s) and WBS number(s).  c. Software size estimate (report in Kilo/Thousand Source Lines of Code (KSLOCs)).  d. The phase of development or operations.  e. Software Class or list of the software classes being used on the project.  f. Software safety-critical status.  g. For each Computer Software Configuration Item (CSCI)/Major System containing Class A, B, or C software, provide:  (1) The name of the software development organization.  (2) Title or brief description of the CSCI/Major System.  (3) The estimated total KSLOCs, the CSCI/Major System, represents.  (4) The primary programming languages used.  (5) The life-cycle methodology on the software project.  (6) Name of responsible software assurance organization(s). |
| Difference between C and D | No Change |
| D | 2.1.5.6 Center Director, or designee, shall maintain a reliable list of their Center’s programs and projects containing Class A, B, C, and D software. The list should include:   a. Project/program name and Work Breakdown Structure (WBS) number. b. Software name(s) and WBS number(s). c. Software size estimate (report in Kilo/Thousand Source Lines of Code (KSLOCs)). d. The phase of development or operations. e. Software Class or list of the software classes being used on the project. f. Software safety-critical status. g. For each Computer Software Configuration Item (CSCI)/Major System containing Class A, B, or C software, provide:  (1) The name of the software development organization. (2) Title or brief description of the CSCI/Major System. (3) The estimated total KSLOCs, the CSCI/Major System, represents. (4) The primary programming languages used. (5) The life cycle methodology on the software project. (6) Name of responsible software assurance organization(s). |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

NASA Centers are required to maintain an accurate and up-to-date inventory of software projects to support strategic decision-making processes at both the Center and Agency levels. This Software Inventory serves as a foundational tool for ensuring transparency, facilitating oversight, supporting governance, and providing the necessary data to address external and internal inquiries related to software development, classification, and safety assurance. Below is a detailed rationale that outlines the specific uses and benefits of maintaining this inventory.

## 2.1 Key Rationale for the Requirement

### 1. Supports Oversight and Governance of Software Engineering Practices

The Center Software Inventory enables NASA to track the Software Classification and safety-critical status of software across all projects, ensuring proper governance and compliance with Agency standards, such as **NPR 7150.2** [083](#_tabs-<p></p>) and **NASA-STD-8739.8** [278](#_tabs-<p></p>)).

* **Engineering and S&MA Technical Authorities:** The Inventory provides critical classification data (e.g., Class A, B, C, D) to help Technical Authorities assess the rigor of processes applied to projects based on their software classification and safety-criticality.
* **Internal and External Inquiries:** The Inventory equips the Office of the Chief Engineer (OCE) and Safety and Mission Assurance (S&MA) personnel with accurate data to address audits, evaluations, and requests from oversight organizations such as the NASA Inspector General (OIG), Government Accountability Office (GAO), or congressional stakeholders.

### 2. Ensures Alignment Between Center Capabilities and Responsibilities

The Inventory data helps the OCE determine whether each Center’s software engineering capabilities are appropriately aligned with the responsibilities assigned to them. It provides insights into whether Centers have:

* Adequate staffing, resources, and expertise to handle the complexity and scale of their software projects.
* The ability to meet the required safety and reliability standards for mission-critical software.  
  This assessment ensures that Centers are equipped to support NASA’s overall mission goals without compromising on software quality or safety.

### 3. Facilitates Agency-Wide Strategic Decision-Making

The Inventory provides an accurate and comprehensive profile of critical software projects (Class A, B, C, and D) across NASA, enabling informed, data-driven decisions at the Agency level.

* **Mission Planning:** Detailed software data, such as development phase, KSLOC estimates, programming languages, and life cycle methodologies, help NASA plan future missions and allocate resources effectively.
* **Risk Assessment:** Inventory information aids in determining trends associated with software risks, safety-criticality, and process challenges that may require Agency-level interventions.
* **Resource Prioritization:** Centers and the Agency can identify high-priority, high-risk projects and adjust staffing, funding, or assurance activities accordingly.

### 4. Enhances Software Safety and Assurance Activities

Center **S&MA personnel** use the Software Inventory to proactively identify projects that contain safety-critical software and verify they have undergone appropriate safety and assurance assessments.

* **Safety-Critical Projects:** The inventory highlights systems that require additional scrutiny for ensuring fault tolerance, hazard mitigation, and failure prediction.
* **Assurance Coverage:** It ensures that software assurance activities (e.g., verification and validation, safety audits, and process assessments) are applied to all safety-critical systems, reducing risks to personnel, missions, and assets.

### 5. Provides Accurate and Timely Data for Decision-Making

The Inventory offers comprehensive, current software-related data in real time, supporting both Center-level and Agency-level decisions.

* **Engineering and Projects Oversight:** Up-to-date information on software lifecycle phases, development organizations, methodology, programming languages, and estimated size (KSLOC) allows curated decision-making for project management and engineering process improvement.
* **Audits and Reviews:** Accurate Software Inventory data ensures smooth collaboration during audits, reviews, and questions from internal stakeholders (NASA leadership) and external entities (e.g., OIG, GAO).
* **Lessons Learned:** Standardized data tracking enables cross-Center sharing of insights, helping the Agency to refine best practices in software development, assurance, and risk management.

### 6. Strengthens NASA’s Capability to Maintain Software Excellence

By cataloging software details—including safety-related data, classifications, and responsible organizations—the Inventory reinforces NASA’s ability to track and improve its software engineering performance, enabling continuous improvement and alignment with mission-critical needs.

## 2.2 Conclusion

The Center Software Inventory is essential for enabling transparency, enhancing decision-making, strengthening oversight, supporting safety assurance, managing resources, and improving alignment with Agency-wide software engineering standards. By maintaining detailed and accurate data on software projects—including classification, development status, size, and responsible organizations—NASA ensures the successful execution of its missions while proactively managing risks, resources, and compliance. This requirement provides the structured framework necessary to consistently monitor and manage software systems across the Agency, securing the safety and efficiency of NASA’s programs and projects.

# 3. Guidance

The guidance for this requirement applies to Software Classes A through E (see [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)).  Inventory information for Software Classes F is captured separately and maintained by the NASA Chief Information Officer.

## 3.1 Purpose

Each NASA Center is responsible for maintaining a current and comprehensive inventory of software development activities, including those in development, operations, and maintenance at their Center. This inventory ensures that the Agency has accurate, real-time data for oversight, assessment, and decision-making processes. Centers must maintain the inventory in a format and system of their choice but be able to provide an electronic version of the data to the Office of the Chief Engineer (OCE) upon request.

**Periodic Updates Required:**

The OCE periodically requests updates to the inventory of software projects under Center purview. This guidance outlines the specific information to be provided for software activities involving Class A, B, C, and D software, in alignment with **NPR 7150.2** [083](#_tabs-<p></p>) and **NASA-STD-8739.8** [278](#_tabs-<p></p>).

## 3.2 Detailed Guidance on Data Elements to Include in the Center Software Inventory

1. **Project/Program Name and Work Breakdown Structure (WBS) Number**
   * Record both the project/program name and corresponding WBS number.
   * The WBS number should reflect the charge code used for the project, enabling traceability to budgets and resource allocations.
2. **Software Name(s) and WBS Number(s)**
   * Include the name of the software components and their WBS numbers if the project has multiple software components associated with different tasks or charge codes.
   * The software name may align with the project name if only one major software element is involved.
3. **Software Size Estimate** *(report in Kilo/Thousand Source Lines of Code – KSLOCs)*
   * Provide an **estimated KSLOC** until actual lines of code can be measured.
   * Once the source code is available:
     + Use a standardized code counting tool to measure actual Source Lines of Code (SLOC).
     + For auto-generated code (auto-coding or model-based development), use an appropriate code conversion method to estimate equivalent SLOCs.
4. **Phase of Development or Operations**
   1. Indicate the software’s current phase within the development lifecycle as defined in **NPR 7120.5 [082](#_tabs-<p></p>)**. Examples include:
      1. Formulation
      2. Implementation
      3. Integration and Test
      4. Operations
      5. Sustainment or Maintenance
5. **Safety-Critical Software Status (Yes/No)**
   * Use the software safety-critical determination process defined in **NASA-STD-8739.8** to classify software components as safety-critical or not.
     + Note: Multiple software components within a project may have different safety-critical designations based on their functionality and potential impact on mission safety.
6. **Software Class (or List of Classes) Used on the Project**
   * Determine the Software Classification for each component using the guidelines in Topic [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality).
     + Classes range from Class A (human-rated, highest criticality) to Class D (non-critical, exploratory and low rigor).
   * If a project involves multiple components with different classifications, provide the classifications for each relevant software element.

## 3.3 Additional Information for Software Containing Class A, B, or C Components

For Computer Software Configuration Items (CSCIs) or major systems with Class A, B, or C software, include the following additional information:

1. **Name of the Software Development Organization**
   * Identify the organization(s) responsible for developing the software component (e.g., internal NASA team, contractor, or collaboration with external partners).
2. **Title or Brief Description of the CSCI/Major System**
   * Provide a clear name or description of each software component and its purpose within the project.
3. **Estimated Total KSLOC Represented by the CSCI/Major System**
   * Continue to report SLOC estimates until the source code is available, at which point actual counts should be provided using a code counting tool or equivalent standards for auto-generated code.
4. **Primary Programming Languages Used for Development**
   * Specify the programming languages used in the software development (e.g., C, C++, Python, Java, LabVIEW, or others) for each CSCI or major system.
5. **Primary Life Cycle Methodology**
   * Indicate the life cycle development methodology used for the software project (e.g., Waterfall, Agile, Iterative/Incremental, Spiral, or Hybrid Models).
   * This information enables alignment of processes with the software’s scale and criticality.
6. **Name of Responsible Software Assurance Organization**
   * Specify which software assurance organization(s) is responsible for verifying and validating software quality, compliance, and reliability for each software component.
   * This assurance coverage ensures adherence to **NASA-STD-8739.8** and **NPR 8715.3**[267](#_tabs-<p></p>).

## 3.4 Additional Notes for Maintaining the Software Inventory

* **Flexibility in Inventory Maintenance:**  
  Centers may use local systems or databases of their choice to maintain the software inventory. However, these systems must be capable of generating electronic data files (e.g., spreadsheets, databases) for submission to the OCE upon request.
* **Periodic Review and Updates:**  
  Ensure the inventory is updated regularly to reflect project changes, such as the transition of software into new development phases, reclassification, or adjustments in resource requirements.
* **Consistency Across the Agency:**  
  Adhere to standardized definitions and methods for classifying software, calculating SLOCs, and assessing safety-criticality to ensure uniformity across Centers, facilitating Agency-wide analysis and strategic planning.
* **Ensure Cross-Component Details:**  
  For projects containing multiple software components, outline the details separately for each software element, ensuring clarity on their classifications, unique characteristics, and safety assessments.
* **Compliance with NPR 7150.2 and NASA-STD-8739.8:**  
  The inventory process must align with Agency standards to ensure compliance with software engineering requirements and safety-criticality determinations.

## 3.5 Importance of This Guidance

The above inventory maintenance process ensures that NASA Centers:

* **Fulfill technical authority expectations** by maintaining transparency on all ongoing software-related activities.
* **Provide real-time and reliable data** needed for strategic decision-making at both Center and Agency levels.
* **Enable efficient resource allocation, oversight, and assurance activities** by ensuring high-risk software systems receive adequate attention. By maintaining an accurate and thorough inventory of software activities, Centers contribute to NASA’s overarching commitment to mission success, safety, and software excellence.

See also Topic [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects),

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)        * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small projects, while typically less complex and resource-intensive than larger initiatives, are still required to be documented in the Center's software inventory to ensure visibility, traceability, and compliance with NASA’s software engineering policies. The scope of the inventory data for small projects may be tailored based on the project’s complexity, size, classification, and criticality. This guidance outlines a simplified approach to fulfilling the inventory requirement for small projects while ensuring alignment with **NPR 7150.2** [083](#_tabs-<p></p>) and associated standards.

## 4.1 Guidance for Small Projects

When adding small projects to the software inventory, the following steps can be taken to reduce the administrative burden while still satisfying the core requirement:

### 4.1.1  Simplified Project and Software Data

* **Project/Program Name and WBS**:
  + Record the project name and its unique Work Breakdown Structure (WBS) number, which is often the primary charge code for the project.
  + If the software component doesn’t have its own WBS, use the project’s primary WBS.
* **Software Name(s)**:
  + If the project contains only one software element, the project and software name may be the same.
  + For software components not requiring custom names, a generic placeholder (e.g., "Flight Control System Module") is sufficient.
* **Estimated Size (KSLOC)**:
  + Small projects can rely on order-of-magnitude size estimates rather than detailed source line-of-code counts during the early development phases.
  + Use a simple estimate (e.g., "Less than 10 KSLOC") to avoid unnecessary counting for small or exploratory efforts.
* **Development or Operations Phase**:
  + Indicate the current development phase (e.g., Formulation, Implementation, or Sustainment) as defined in **NPR 7120.5**[082](#_tabs-<p></p>), without requiring precise sub-phase distinctions for small projects.

### 4.1.2  Streamlined Safety and Classification Reporting

* **Safety-Criticality**:
  + Perform a basic evaluation of safety-criticality using the process outlined in **NASA-STD-8739.8**[278](#_tabs-<p></p>), ensuring the evaluation is limited to core safety implications (i.e., failure modes linked to risk). For small projects, simply report "Yes" or "No" based on this evaluation.
  + Small projects are less likely to be safety-critical unless they are directly linked to safety-critical systems (e.g., flight hardware).
* **Software Classification**:
  + Assess software classification using Topic [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality). For small projects, briefly document the rationale for the classification:
    - **Class D or C:** Most small, exploratory, or prototype-like software will be Class D (low-priority mission contribution) or Class C (useful but non-essential to success).
    - **Class A or B:** Small projects are unlikely to fall under high-risk classifications unless associated with mission-critical systems (e.g., controls or human-rated systems).

### 4.1.3  Simplified Data for Class A, B, or C Software Projects

If a small project contains Class A, B, or C software, include the following aspects in a simplified version:

* **Development Organization**:
  + Identify the entity (e.g., NASA internal team or external contractor) responsible for developing the software.
* **High-Level Description**:
  + Offer a brief description of the software’s purpose (e.g., "Navigation Module for Small Payload").
* **Estimated KSLOC for CSCI**:
  + Provide an approximate KSLOC count or a simple range estimate (e.g., "1-5 KSLOC") to avoid precision counting in small projects.
* **Programming Languages**:
  + List the primary programming languages or tools used (e.g., Python, C, MATLAB, LabVIEW).
* **Life Cycle Methodology**:
  + State the chosen development approach (e.g., Agile, Waterfall, or Hybrid). For small projects, this can be a broad designation without extensive explanation of the process.
* **Software Assurance Assignment**:
  + Identify the organization responsible for software assurance, ensuring that basic assurance activities match the project’s scale and safety-critical determination.

### 4.1.4  Use of Existing Tools/Spreadsheets

* Small projects can maintain inventory records in simple formats (e.g., Excel sheets, Google Sheets) or existing lightweight tools, without requiring dedicated inventory management software.
* Standard templates and tools provided by the Center’s software engineering office or S&MA office can be adapted for small projects with reduced fields.

### 4.1.5  Proportional Effort Based on Size and Complexity

Small projects should follow a tailored approach to the inventory requirement:

* Minimize excessive reporting: Focus only on fields relevant to the project’s scale and criticality.
* Use ranges or approximations for size, lifecycle phase, and classification where precise data isn’t immediately available.
* Avoid duplicative work: Rely on existing documents (e.g., project charters or safety assessments) to populate inventory fields.

### 4.1.6  Example Inventory Entry for a Small Project

Below is a sample inventory entry for a small project based on this guidance:

| Field | Example Value |
| --- | --- |
| Project/Program Name | CubeSat Thermal Control |
| WBS Number | 12345 |
| Software Name(s) | CubeSat Thermal Control Software |
| Estimated KSLOC | <5 KSLOC |
| Current Phase | Implementation |
| Safety-Critical (Yes/No) | No |
| Software Classification | Class D |
| **For Class A/B/C Software** |  |
| Development Organization | NASA Internal Development Team |
| Description of CSCI/Major System | CubeSat Thermal Monitor |
| Estimated KSLOC for CSCI | ~3 KSLOC |
| Programming Languages | C++, Python |
| Life Cycle Methodology | Agile |
| Software Assurance Organization | Center S&MA Office |

## 4.2 Conclusion

This small project guidance streamlines compliance with the software inventory requirement by balancing the need for accurate reporting with the reduced complexity and scale of smaller efforts. By tailoring reporting to the project’s size and criticality, Centers can reduce administrative burdens while maintaining essential oversight, safety assurance, and compliance with Agency standards.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-267)

  [NASA General Safety Program Requirements (Updated w/Change 3)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8715&s=3D "Click to open in new window")

  NASA Procedural Requirements, NPR8715.3D, Effective Date: August 01, 2017, Expiration Date: August 01, 2022
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-290) OCE Software Survey Instructions and Templates (on SPAN) This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook. 2010 Software Inventory instructions, version 7 (available from the OCE).

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

To strengthen understanding and ensure effective implementation of the requirement mandating Centers to maintain an accurate and up-to-date software inventory, lessons from past NASA experiences offer critical insights. These lessons, derived from the NASA **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** and historical mission reviews, demonstrate the importance of accurate software tracking, inventory management, and oversight.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Jet Propulsion Laboratory (JPL) Flight Software Engineering Lessons [572](#_tabs-<p></p>)

* **Lesson Learned ID: 2218**
* **Key Issue:**  
  Tracking and managing the development of flight software posed significant challenges across JPL spacecraft projects, leading to cost overruns, schedule delays, and potential risks due to insufficient oversight and incomplete verification.
* **Relevance to Current Requirement:**  
  Maintaining an accurate software inventory with detailed metadata such as classification, size (KSLOC), development phase, and safety-criticality status allows Centers to monitor software progress systematically and identify high-risk projects early in the process.

#### 2. Mars Climate Orbiter Loss Due to Navigation Error [529](#_tabs-<p></p>)

* **Lesson Learned ID: 0938**
* **Key Issue:**  
  The Mars Climate Orbiter mission failed due to mismatched units in the navigation software, which went undetected prior to launch due to inadequate oversight of software activities across development teams.
* **Applicable Lessons:**
  + A comprehensive inventory of software projects helps track which components or subsystems are contributing to mission-critical systems, ensuring proper verification and validation (V&V) practices are applied, especially for safety-critical and/or high-rigor software classes.
  + Establishing standard reporting formats for inventory data (e.g., project phase, responsible organization) minimizes the risks of oversight flaws.

#### 3. James Webb Space Telescope (JWST) Software Development Challenges

* **Lesson Learned ID: 4646**
* **Key Issue:**  
  The JWST faced significant delays caused in part by the complexities in managing multiple interconnected software systems. Inadequate communication and manual tracking of software development tasks led to slow identification and resolution of integration issues.
* **Relevance to the Requirement:**
  + Properly maintaining a centralized inventory of all ongoing software development activities, including lifecycle phase and responsible organizations, ensures better visibility into potential dependencies and integration issues across projects.
  + For large-scale projects, an accurate software inventory reduces communication gaps between multiple teams and facilitates early issue tracking.

#### 4. Software Safety Oversight for NASA Space Flight Programs

* **Lesson Learned ID: 1861**
* **Key Issue:**  
  Insufficient tracking of software safety-related data and classification resulted in a failure to identify critical software risks on certain programs, such as software faults that could lead to catastrophic failures.
* **Relevance to the Requirement:**
  + Adding safety-critical status and software classification (per **NASA-STD-8739.8**[083](#_tabs-<p></p>)requirements) into the inventory ensures safety-critical systems are flagged early for robust assurance activities.
  + Eliminating ambiguity in the inventory promotes consistent safety analyses across all Centers.

#### 5. Mars Polar Lander (MPL) Failure Due to Premature Shutdown of Descent Engines [683](#_tabs-<p></p>)

* **Lesson Learned ID: 1778**
* **Key Issue:**  
  The failure resulted from inadequate testing of a software component, which was linked to incomplete tracking of software verification activities during development.
* **Relevance to Current Requirement:**
  + By maintaining an updated list of software’s phase in development or operation, Centers can monitor the V&V progress of software components and identify whether appropriate testing has been applied at each stage of the lifecycle.
  + Detailed inventory records would facilitate proactive oversight and prevent similar gaps in testing.

#### 6. Columbia Accident Investigation Board Report - Lack of Oversight

* **Lesson Related to Software Oversight Failures during Development**
* **Key Insight:**  
  The Columbia accident highlighted deficiencies in capturing and tracking potential risks associated with various systems, including software, compounded by inadequate reporting and documentation of ongoing development activities.
* **Relevance to Current Requirement:**
  + Maintaining a database of software projects with clear links to their safety statuses and responsible assurance organizations ensures that all safety-critical activities are well-documented and properly monitored.
  + Centralized, reliable inventory data would have allowed leadership to detect and respond to gaps in software development or testing with greater urgency.

#### 7. ISS Joint Integrated Simulation Software Discrepancies

* **Key Issue:**  
  Software discrepancies in training simulations for the International Space Station (ISS) resulted from poorly documented development status updates. Certain software components were not adequately tracked, leading to delays in addressing compatibility issues before system integration.
* **Relevance to the Requirement:**
  + A fully updated inventory of software names, WBS numbers, and their development status would have allowed teams to identify discrepancies earlier in the lifecycle and address risks before integration challenges arose.
  + Tracking responsible development and assurance organizations in the inventory further ensures accountability for addressing technical issues.

#### 8. Space Shuttle Block II Engine Controller Software Development Oversight

* **Lesson Learned ID: 2686**
* **Key Issue:**  
  Software engineering shortfalls in defining development processes and managing software inventories for complex systems led to late identification of risks, miscommunications, and delays in delivering the software.
* **Relevance to Current Requirement:**
  + Properly structured inventories that include life cycle methodologies (e.g., Agile, Waterfall) and the name of the responsible development organizations ensure clearer communication of expectations, workflows, and progress.
  + Such data improves collaboration among engineering teams while giving leadership visibility into potential bottlenecks.

### 6.1.2  Summary of Applicability to the Requirement

The Lessons Learned from these events collectively emphasize the necessity of:

1. Maintaining accurate and centralized software inventories to ensure visibility into all active projects.
2. Including detailed metadata fields, such as safety-critical status, software classifications, lifecycle phase, and responsible organizations, to mitigate risks arising from oversight gaps, miscommunications, and insufficient testing.
3. Tracking software projects across complex missions to identify and address risks early in the development lifecycle.

### 6.1.3  Recommendations for Implementing the Lessons Learned:

* Ensure inventory data is maintained in a real-time accessible system that can support updates and ad hoc queries.
* Include fields directly relevant to historical Lessons Learned, such as:
  + Development phase monitoring (to identify risks in early stages).
  + Safety-criticality and classification status (to flag high-priority systems).
  + Responsible organizations for assurance and development (to ensure accountability).
* Leverage trends observed in the inventory to inform decisions on resource allocation, risk analysis, and process improvements at both Center and Agency levels.

By learning from past challenges and applying these insights, NASA can enhance the reliability of its software inventory systems and reduce risks tied to its software-intensive missions.

## 6.2 Other Lessons Learned

 As part of its 2003 audit report on IV&V software, the Inspector General (IG) included this recommendation: "The NASA Chief Engineer, in coordination with the Associate Administrator for Safety and Mission Assurance, should establish a process that provides the NASA IV&V Facility, on a recurring basis, a complete and accurate list of the Agency's programs and projects governed by either NASA Procedures and Guidelines **NPR 7120.5A** [082](#_tabs-<p></p>) or NASA Technical Standard **NASA-STD-8719.13A** [271](#_tabs-<p></p>)."

# 7. Software Assurance

**SWE-006 - Center Software Inventory**

2.1.5.6 Center Director, or designee, shall maintain a reliable list of their Center’s programs and projects containing Class A, B, C, and D software. The list should include:

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

The purpose of this requirement is to ensure the Center maintains an accurate and up-to-date inventory of its programs and projects that involve software of Classes A, B, C, and D. This provides critical visibility into software-related efforts and helps NASA effectively manage software risks, compliance, and quality across the organization.

Software Assurance (SA) personnel play an essential role in verifying that this list is complete, accurate, and reliable. SA is also responsible for examining how this list is maintained and ensuring that it supports compliance with software assurance requirements identified in **NPR 7150.2** [083](#_tabs-<p></p>), **NASA-STD-8739.8** [278](#_tabs-<p></p>), and other directives.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Ensure the List’s Completeness and Accuracy

1. **Review and Verify the List**
   * Verify that the list includes all projects and programs involving Class A, B, C, and D software that are currently under development or operational at the Center.
   * Ensure the information specified in the requirement (items a through g) is complete, up-to-date, and accurate for each entry.
2. **Confirm Information Accuracy**
   * Review source documentation (e.g., project plans, Software Requirements Specifications (SRSs), and design documents) to validate:
     + Project/program names and WBS numbers.
     + Names and estimates of software items (e.g., KSLOCs, programming languages).
     + Software classification and safety-critical status (confirmed through classification reviews).
     + Life cycle methodology, responsible software assurance organizations, and development organizations.
3. **Audit Periodically**
   * Perform periodic audits or reviews of the list to ensure it reflects the latest project statuses (e.g., phase of development, changes to software size estimates, or updates to methodology) using data pulled from assurance audits, metrics, or project reporting.
4. **Coordinate Updates**
   * Collaborate with software engineering, development, and assurance teams to ensure that any changes to project or software attributes are promptly reflected in the list.

#### 7.4.2.2  Support and Monitor the Maintenance Process

1. **Assist in Establishing a Maintenance Process**
   * Collaborate with the Center Director (or designee) to develop procedures for maintaining the list, including:
     + How the list will be reviewed and updated.
     + Who is responsible for contributing and validating information.
     + How updates will be tracked and controlled.
2. **Ensure Traceability**
   * Confirm that data in the list is traceable and aligns with approved project and software engineering documentation, such as:
     + Software Development/Management Plans.
     + Assessed KSLOC values and class determination documents.
     + Safety-critical analysis results.
3. **Advocate for Version Control**
   * Recommend maintaining a version-controlled repository or database for the software list to ensure the historical tracking of changes and updates over time.

#### 7.4.2.3  Verify Compliance with Required Data Fields

SA personnel should ensure that all the required information specified in the directive is included in the list. The fields to be validated are as follows:

1. **General Project/Program Data**:
   1. Ensure the list includes:
      1. Project/program name.
      2. Work Breakdown Structure (WBS) number.
   2. Include the names and WBS identifiers of all software under the project or program.
   3. Verify that the software size estimates are reported in KSLOCs. Confirm any estimates using size estimation models provided by the development team.
   4. Confirm that the current phase of development or operations (e.g., requirements definition, design, implementation, testing, operations/maintenance) is indicated.
2. **Software Classification and Safety-Critical Indicator**:
   1. Ensure the Software Class (A, B, C, or D) is listed for each software component. If multiple classifications exist within a project, ensure all are reflected.
   2. Confirm whether the software is designated as safety-critical.
3. **Details for Each CSCI/Major System Containing Class A, B, or C Software**:
   1. For each Computer Software Configuration Item (CSCI) or Major System:
      1. Verify the name of the software development organization and confirm its correctness.
      2. Ensure that each CSCI/Major System includes a title or brief description.
      3. Confirm the estimated total KSLOCs per CSCI/Major System.
      4. Validate that all primary programming languages are specified.
      5. Confirm that the life cycle methodology (“waterfall,” “agile,” “spiral,” etc.) being used for the CSCI/Major System is listed.
      6. Ensure that the name(s) of the responsible software assurance organization(s) are identified.

#### 7.4.2.4. Monitor Software Assurance Oversight Responsibilities

* **Support Consistency**:
  + Ensure the Center’s software assurance organization is accurately identified in the CSCI-level data (g.6) and confirm its documented role in performing SA tasks (e.g., audits, peer reviews, risk analysis).
* **Assess Safety-Critical Designation (f)**:
  + Verify that the assignment of “safety-critical” status is based on safety analyses, hazard reports, and criticality assessments in alignment with **NASA-STD-8739.8**.

#### 7.4.2.5  Communicate Findings and Drive Continuous Improvement

1. **Report Discrepancies or Inconsistencies**:
   * Highlight projects with incomplete, outdated, or incorrect data and coordinate with relevant teams to correct the information.
2. **Use Metrics for Oversight**:
   * Leverage software assurance metrics (e.g., audits completed, classification errors found, or trends in software sizing) to monitor the health of the list.
3. **Recommend Process Improvements**:
   * Propose updates to the maintenance process if recurring issues (e.g., delayed updates, missing fields, inconsistent methods for estimating KSLOCs) are identified.

### 7.4.3  Expected Outcomes

By ensuring the development and maintenance of a reliable and comprehensive software list, the following objectives will be achieved:

1. **Complete Inventory**:
   * The list will provide an accurate, centralized view of all projects containing Class A, B, C, and D software at the Center.
2. **Compliance**:
   * The data in the list will satisfy the requirements of NASA directives, particularly with mandatory fields defined in this requirement.
3. **Improved Oversight**:
   * The list will serve as a key resource for managing software engineering discipline, tracking compliance, and maintaining a high level of software assurance.
4. **Risk Mitigation**:
   * Accurate classification, size estimation, and proper tracking will help identify and mitigate risks tied to large, critical, or safety-sensitive software.

### 7.4.4  Summary

**Software Assurance (SA) personnel** are responsible for verifying that the Center maintains an accurate and reliable list of its programs and projects containing Class A, B, C, and D software. This includes ensuring all required fields are complete, data is traceable and consistent, and updates are made in a timely manner. Through regular reviews and proactive monitoring, SA personnel play a key role in maintaining compliance, improving transparency, and supporting NASA’s commitment to software quality and safety.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)        * [7.02 - Classification and Safety-Criticality](/spaces/SWEHBVD/pages/102695612/7.02+-+Classification+and+Safety-Criticality) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) |
