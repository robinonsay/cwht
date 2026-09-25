# SWE-033 - Acquisition vs. Development Assessment

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695412. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment

SWE-033 - Acquisition vs. Development Assessment

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695412)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695412&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. The Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

3.1.2 The project manager shall assess options for software acquisition versus development.

## 1.1 Notes

The assessment can include risk, cost, and benefits criteria for each of the options listed below:

a. Acquire an off-the-shelf software product that satisfies the requirement.

b. Develop a software product or obtain the software service internally.

c. Develop the software product or obtain the software service through contract.

d. Enhance an existing software product or service.

e. Reuse an existing software product or service.

f. Source code available external to NASA.

See the NASA Software Engineering Handbook for additional detail.

## 1.2 History

Click here to view the history of this requirement: SWE-033 History

SWE-033 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.5.2 The project shall assess options for software acquisition versus development. |
| Difference between A and B | No Change |
| B | 3.12.2 The project manager shall assess options for software acquisition versus development. |
| Difference between B and C | No Change |
| C | 3.1.2 The project manager shall assess options for software acquisition versus development. |
| Difference between C and D | No Change |
| D | 3.1.2 The project manager shall assess options for software acquisition versus development. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

When making any decision, it is important to assess the options available to obtain the greatest value and benefit.  Software development is no different.  Choices need to be assessed to identify the best use of available resources (budget, time, personnel, etc.) to address a defined and scoped need while providing the greatest benefit with the least risk to the project.

Requiring the project manager to assess options for software acquisition versus development ensures that critical trade-offs between cost, schedule, functionality, risk, and long-term sustainability are carefully evaluated. This decision directly impacts the **success, reliability, and adaptability** of the software and the mission it supports. By mandating this structured decision-making process, projects can pursue solutions that best meet their unique requirements while minimizing risks and realizing maximum value.

This requirement is essential because the decision to either acquire (purchase or license) software or develop custom software has significant implications for the project's **cost, timeline, functionality, risk, and long-term sustainability.** A thorough assessment of these options ensures that the selected approach aligns with the **project's goals, budget, operational requirements, and risk tolerance.** Below is a detailed rationale addressing why this requirement matters:

## 2.1. Optimizing Cost-Effectiveness

* **Why It Matters:**
  + Acquiring existing software (e.g., Commercial Off-The-Shelf [COTS], Government Off-The-Shelf [GOTS], or Open Source Software [OSS]) can reduce upfront development costs, as the software already exists and is ready for integration or minor adaptation.
  + Custom software development, while potentially more expensive, allows the creation of software tailored to specific mission needs, avoiding unnecessary features or licensing fees.
* **Rationale:**
  + By assessing both options, project managers can make cost-conscious decisions while balancing upfront expenses, licensing/subscription costs, and long-term maintenance costs. This ensures that project resources are allocated efficiently and economically.

## 2.2 Meeting Functional Needs Without Compromise

* **Why It Matters:**
  + Acquired software typically comes with predefined functionalities, which may only partially meet the requirements. It might lack critical capabilities or include unnecessary features, thus requiring modifications.
  + Custom software, on the other hand, offers the ability to define every feature and functionality to satisfy the unique demands of the system or mission, ensuring no gaps in operational capability.
* **Rationale:**
  + Assessing both options ensures that the selected approach delivers all **mission- or safety-critical functions,** satisfying operational needs without compromises or workarounds.

## 2.3 Managing Project Timeline and Schedule Risks

* **Why It Matters:**
  + Acquiring ready-made software can significantly reduce development time and expedite project schedules. However, it may require significant time for **integration, testing**, and customizing functionality, particularly in complex aerospace systems.
  + Developing software in-house provides control over the development process but can introduce schedule risks due to design iteration, unforeseen technical challenges, or resource constraints.
* **Rationale:**
  + An assessment helps project managers choose the approach that aligns best with the project’s deadlines and ensures readiness for key milestones, such as **certification deadlines, mission deployment, or crew availability.**

## 2.4 Managing Risk (Technical, Legal, and Operational)

* **Why It Matters:**
  + Acquiring software involves risks such as:
    - Dependence on external vendors for updates, patches, and technical support.
    - Potential cybersecurity vulnerabilities, particularly with third-party or open-source software.
    - Licensing risks, including compliance with commercial licenses, intellectual property concerns, or future restrictions by vendors.
  + Developing software carries risks associated with **technical feasibility, resource allocation, or scalability** but offers greater control over quality, security, and risk management.
* **Rationale:**
  + A thorough assessment allows the project to minimize risks by weighing the trade-offs between external dependencies and in-house control, ensuring that cybersecurity, operational resilience, and compliance are addressed.

## 2.5 Supporting Long-Term Sustainability and Maintainability

* **Why It Matters:**
  + Acquired software often comes with licensing renewal costs, potential vendor lock-in, and dependencies on external parties for continued updates, which can complicate long-term use and adaptability.
  + Developing software in-house ensures full ownership and control, allowing for easier adaptation to evolving mission requirements and integration with future systems. However, it also requires ongoing investment in maintenance, skilled personnel, and infrastructure.
* **Rationale:**
  + By assessing acquisition versus development, the project can prioritize a sustainable solution that aligns with the software's expected lifespan and anticipated future requirements.

## 2.6 Navigating Certification and Regulatory Requirements

* **Why It Matters:**
  + Software used in aerospace systems often needs to comply with stringent regulations (e.g., **DO-178C**, **NASA NPR 7150.2D**, **FAA**, or other mission-critical software standards). Acquired software might not meet these certification requirements out of the box, requiring additional validation, documentation, and testing.
  + Custom software development enables alignment with regulatory and certification standards from the ground up, ensuring compliance is integrated into the software lifecycle.
* **Rationale:**
  + Assessing these factors upfront ensures that the chosen software path avoids delays or additional costs associated with bringing software into compliance after acquisition or development.

## 2.7 Enabling Scalability and Future Adaptations

* **Why It Matters:**
  + Acquired software is often less flexible when adapting to new mission requirements, hardware, or operational conditions. Features may be updated or discontinued based on vendor decisions rather than specific project needs.
  + Custom software, while initially more resource-intensive, is designed with scalability and adaptability in mind, allowing easy upgrades or feature additions in response to future needs.
* **Rationale:**
  + Evaluating both options ensures that the chosen approach provides the flexibility to accommodate future mission changes, emerging technologies, or long-term operational goals.

## 2.8 Maintaining Alignment with the Mission’s Criticality

* **Why It Matters:**
  + Mission-critical software (e.g., onboard hazard detection, automated abort handling, life support) must operate under **all conditions without fail.**
  + Acquired software may introduce risks (e.g., untested functionality, unexpected limitations) that are unacceptable for high-assurance systems, while in-house development allows for tighter control, validation, and safety assurance.
* **Rationale:**
  + The assessment ensures that the approach chosen—whether acquisition or development—can meet the reliability and safety requirements for the mission’s criticality level (**DO-178C DAL-A/B/C**).

## 2.9 Encouraging Innovative and Strategic Decision-Making

* **Why It Matters:**
  + By assessing both acquisition and development options, the project may discover creative hybrid approaches, such as:
    - Acquiring an existing platform and customizing it for specific mission capabilities.
    - Using open-source software as a baseline and building missing functionalities in-house.
    - Leveraging vendor expertise while maintaining control over safety-critical components through co-development.
  + Such innovative strategies can help projects achieve optimal outcomes in terms of cost, schedule, and functionality.
* **Rationale:**
  + This requirement serves as a structured approach to apply critical thinking and innovation to software decision-making, rather than defaulting to either acquisition or development without due consideration.

## 2.10 Accountability and Justification

* **Why It Matters:**
  + The decision between acquisition and development is a defining project milestone with long-term effects on budgets, schedules, and risks. Documenting a formal assessment ensures:
    - Accountability for decision-making.
    - A clear record of how the final decision aligns with mission objectives, constraints, and risks.
    - Justification for leadership, stakeholders, and auditors to understand why one option was chosen over the other.
* **Rationale:**
  + This formal assessment ensures transparency and provides a way to justify the decision process, especially in high-stakes environments like aerospace where project outcomes carry significant consequences.

# 3. Guidance

## 3.1 Acquisition Versus Development Options

When assessing solutions for software acquisition versus development, there are five possible options:

* Acquire an off-the-shelf software product that satisfies the requirement.
* Develop a software product or obtain a software service internally.
* Develop the software product or obtain the software service through the contract.
* Enhance an existing software product or service.
* Reuse an existing software product or service.

Each option has its benefits, costs, and risks which should be identified through trade studies (for off-the-shelf products), internal assessments (for existing products), and cost-benefit analyses. Checklists of questions to ask when assessing acquisition versus development can be found in [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) in this handbook.

## 3.2 Risks in Make Versus Buy Decisions

Risks are considered in software to make/buy and acquisition decisions.  The project needs to ensure that software products used in the design or support of human space flight components or systems include a level of rigor in risk mitigation as a software management requirement, regardless of software classification.  The level of documentation needed for risk identification and tracking is defined by the Center processes.

## 3.3 Reuse of Existing Software Products

The team should assess existing software products, whether off-the-shelf or in-house, to identify how well they meet the need of the current project and whether they are suitable for the intended environment. The following information should be weighed against the defined need, architecture, environment, requirements, safety classification, budget, etc. of the current project:

* Features/functionality/capabilities.
* Documentation.
* Test results.
* Performance record.
* Safety record.
* Licensing, maintenance, integration, and support costs.
* Any other relevant information.

The project responsible for procuring off-the-shelf software is responsible for documenting, prior to procurement, a plan for verifying and validating the off-the-shelf software to the same level of confidence that would be needed for an equivalent class of software if obtained through a "development" process. For more detail, see [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software).

See also [6.3 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SWEHBVD/pages/102695560/6.3+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS), [PAT-025 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SITE/pages/116294244/PAT-025+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS), 

## 3.4 Developing Software

For development, whether internal or external, consider the following information:

* Personnel skill sets, experience, availability.
* The cost is associated with training, tools, post-development maintenance, and support.
* Company reputation, track record, history, etc. (for contracted development).
* Overall life cycle cost, including the cost of integration with existing software components.
* Intellectual property rights.
* Cost and availability of the workforce should follow-on work be required.
* Insight into development processes.
* Schedule associated with procurement (sole source, competitive, task order, etc.) for procured software or a contracted development.
* Life cycle supportability risks.
* The complexity of effort and extent of modifications required.

## 3.5 Making the Decision

Identify risks associated with each assessed option, including:

* Technical risks.
* Supplier risks, including track record and support risks.
* Cost and schedule risks.

The team should document the results of the analysis as well as the raw data that was collected and evaluated to arrive at the final solution.

Involve the right stakeholders in the assessment process to benefit from their experience and consider all key information.  Consider the following, as applicable:

* Technical personnel.
* Management.
* Contracts.
* Procurement.
* End users.
* Customers.
* Technical Authority.

See [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) in this Handbook for additional guidance on this topic. The references in this topic may also provide additional guidance on assessing acquisition versus development options. See also [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation), [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions)

Additionally, Center procedures addressing decision analysis and resolution may be helpful in planning and carrying out the assessment and selection process.

The Agency Software Manager can be used as a resource for this confirmation.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions)        * [6.3 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SWEHBVD/pages/102695560/6.3+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-025 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SITE/pages/116294244/PAT-025+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting)      * [Decision Making](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Decision+Making) |

# 4. Small Projects

While assessing all available options is important for any software development project, it may be even more important for projects with limited budgets, personnel, or both. Small projects need to evaluate their available resources against the possible solutions to find the best fit with the least risk.

The use of existing trade studies and market analyses may reduce the cost and time of assessing available options.

## 4.1 Key Considerations for Small Projects

* **Keep it Simple:** Avoid overthinking for small projects—prioritize options that achieve objectives cost-effectively and quickly.
* **Don't Overscope:** Custom software development can introduce complexity; acquisition may be better suited for small, well-defined needs.
* **Revisit Assumptions:** If project requirements change, reassess acquisition vs. development.

By following this structured approach, you can make an informed and balanced decision to meet the requirement of assessing software acquisition versus development for small-scale projects.

Good guidance for small projects on this requirement typically involves a structured decision-making process tailored to the scale and complexity of the project. Here's how you can approach it:

### 4.1.1 Clearly Define the Requirements

* Start by understanding and documenting the specific functional, technical, and business requirements of your project.
* Ensure requirements are as clear and concise as possible to make comparison easier.

### 4.1.2 **Assess Feasibility of Acquisition vs. Development**

* **Software Acquisition:** Evaluate if there is existing Commercial-Off-The-Shelf (COTS) software or open-source software that meets your needs with minimal customization.
* **Software Development:** Evaluate whether building custom software is necessary to meet unique or highly specific requirements.

### 4.1.3 **Perform Cost Analysis**

* **Acquisition Costs:** Factor in the cost of purchasing the software, licensing fees, installation, configuration, training, and long-term maintenance or renewal.
* **Development Costs:** Consider the cost of man-hours, tools, infrastructure, testing, debugging, maintenance, and updates.

### 4.1.4 **Assess Timeline**

* Determine which option would allow you to meet project deadlines. Prebuilt software may allow faster implementation, whereas custom development could take more time.

### 4.1.5 Evaluate Risks

* **Acquisition Risks:** Risks include vendor lock-in, limited customization, compatibility issues, and dependency on vendor support.
* **Development Risks:** Risks include resource availability, technical challenges, scope creep, budget overruns, and testing bottlenecks.

### 4.1.6 Assess Long-term Scalability and Flexibility

* Determine whether the acquired software or custom-built solution can scale with future needs or adapt to changing project requirements.

### 4.1.7 Check Compatibility with Existing Systems

* Evaluate how well either option integrates with your organization’s or project's existing technologies and processes.

### 4.1.8 **Consider Expertise and Resources**

* **Acquisition:** Determine whether your team is trained or if additional training is needed for the acquired software.
* **Development:** Assess whether your team has sufficient technical expertise, or if external consultants may be required.

### 4.1.9 **Include Stakeholders in Decision-Making**

* Involve technical team members, end-users, or relevant stakeholders in the evaluation process to ensure all perspectives are considered.

### 4.1.10 **Use Decision Criteria to Compare Options**

Create a weighted scorecard or decision matrix to compare acquisition vs. development based on factors such as:

* Cost
* Timeline
* Functionality
* Scalability
* Risk
* Maintenance effort

### 4.1.11 **Document the Process**

* Document your analysis and rationale for selecting acquisition or development. This promotes transparency and can be helpful if your decision is reviewed later.

### 4.1.12 **Pilot/Test If Necessary**

* If uncertain, consider a small-scale trial of the software acquisition option, or prototype a portion of the custom development to evaluate feasibility.

### 4.1.13 **Consider Hybrid Approaches**

* For small projects, a hybrid approach might work—for example, customizing an existing software platform slightly to meet your needs, rather than starting development from scratch.

## 4.2 Example Framework for Decision

| Criteria | Acquisition (Prebuilt) | Development (Custom) |
| --- | --- | --- |
| Cost | $5,000 licensing | $20,000 dev costs |
| Timeline | 1 month setup | 6 months build |
| Functionality | 80% match to needs | 100% tailored |
| Risk | Medium (vendor lock-in) | High (scope/budget risks) |
| Scalability | Limited customization | Unlimited flexibility |
| Maintenance Effort | Low | High |

You can adjust this based on your specific needs.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-067) Trade Study Checklist,
   NASA Marshall Space Flight Center (MSFC), 2008.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-068) Trade Study Template,  NASA Marshall Space Flight Center (MSFC), 2009. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-078) SED Decision Analysis and Resolution,  580-SP-038-002, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2005. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-551)

  [Lessons Learned From Flights of ?Off the Shelf? Aviation Navigation Units on the Space Shuttle, GPS](https://llis.nasa.gov/lesson/1370 "Click to open in new window")

  Public Lessons Learned Entry: 1370.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 Lessons Learned

A documented lesson from the NASA Lessons Learned database notes the following topics that should be kept in mind when assessing software acquisitions versus development. While many of these lessons seem hardware-oriented, some of these lessons can also be applied to software [551](#_tabs-<p></p>):

* **Lessons Learned From Flights of "Off the Shelf" Aviation Navigation Units on the Space Shuttle, GPS (Talk to those that have used the product before.) Lesson Number 1370:** "Outside consultants, who do not have a stake in the choice of a particular unit, should be used. Such consultants have "hands-on experience" ... and can be an important information source concerning their design, integration, and use. Consultants who have participated in previous integrations will know problems that other users have encountered. Consultants and other users can also provide valuable insight into the rationale and requirements that governed the original design of the unit. This information is invaluable ... for identifying technical, cost, and schedule risks associated with a particular ... unit ...."

* **Lessons Learned From Flights of "Off the Shelf" Aviation Navigation Units on the Space Shuttle, GPS ("Plug And Play" versus development.) Lesson Number 1370:** "The fact that a unit is in mass production and is a proven product does not mean that its integration to a different vehicle will be a simple, problem-free 'plug and play' project. A difference in the application (such as aviation versus space flight) will result in the manifestation of firmware issues that may not have appeared in the original application. Unique data interfaces used by manned and some unmanned spacecraft avionics may require modification of the unit. Power supply changes and radiation hardening may also have to be performed." While this lesson describes hardware acquisitions, software acquisitions should also keep this lesson in mind because projects have differences that can affect the suitability of the software for a particular application.

* **Lessons Learned From Flights of "Off the Shelf" Aviation Navigation Units on the Space Shuttle, GPS (Pay attention to "Technical Risk.") Lesson Number 1370:**  "Project management may focus mainly on risk to cost and schedule, with little attention paid to technical risk. GPS project management kept Shuttle Program management well aware of the nature of a 'success-oriented' approach and that cost and schedule could be impacted. Analysis at the start of a project should be conducted to determine the risk to cost and schedule based on the technology level, the maturity of the technology, and the difference between the planned application and the application for which the box was designed originally. Software complexity should also be examined. Failure to account for technical risk can lead to cost and schedule problems."

"An additional risk in using 'off the shelf' units concerns the availability of the vendor. Can a user continue to use and maintain a product if the vendor goes out of business or stops producing and supporting the product?"

* **Lessons Learned From Flights of "Off the Shelf" Aviation Navigation Units on the Space Shuttle, GPS (Provide guidelines for COTS and "Faster-Better-Cheaper" implementation).****Lesson Number 1370:** "A key lesson from unmanned spacecraft failures and DoD software programs is that one must understand how to properly use commercial off the shelf (COTS) products and apply 'faster-better-cheaper' principles."

"Some projects have failed since management was not given guidance concerning how to implement a faster-better-cheaper approach. 'Faster' and 'cheaper' are easily understood, but 'better' is difficult to define. This has also led to inconsistent application of faster-better-cheaper principles from one project to another."

"A COTS policy is needed to help prevent cost, schedule, and technical difficulties from imperiling projects that use COTS. Criteria for determining whether a COTS approach can be taken must be determined. Of prime importance is defining the level of insight needed into vendor software, software maintenance, and certification processes."

"Problems in COTS projects can arise when requirements are levied on the product that the vendor did not originally intend for the unit to meet. Using COTS may mean either compromising requirements on the COTS unit or the integrated system. Whether or not new requirements have to be applied to the unit is a critical decision. Unfortunately, new requirements may not be recognized until the COTS product experiences difficulties in the testing and integration phases of the project."

"The Shuttle Program created COTS/MOTS (modified off the shelf) software guidelines for varying levels of application criticality. This recommended policy defines what considerations should be made before deciding to procure a COTS/MOTS product. The following should be examined based on the criticality (impact of failure on the safety of flight or mission success) of the application and product in question:

* **"Certification Plan** – How much of the vendors' in-house certification can be relied upon? For critical applications, additional testing will be needed if access to test results, source code, and requirements documents are not allowed. Can the unit be certified to a level commensurate with the criticality of the application?
* **"Vendor Support** – This should cover the certification process and the system life cycle. The level of support should be defined based on the criticality of the system.
* **"Product Reliability** – Vendor development and certification processes for both hardware and software should be examined.
* **"Trade Studies** – Define 'must meet,' 'highly desirable' and 'nice to have' requirements. The ability of the unit to meet those requirements, and at what cost, will be a major deciding factor in the COTS decision. Identify loss of operational and upgrade flexibility as well as technical risks and cost associated with the product. Examine the impact of the product on the integrated system, including hardware and software interface changes. Compare the proposed COTS products to a custom-developed product. Assess the life expectancy of the product and its track record in the marketplace.
* **"Risk Mitigation** – Identify areas that increase risk, such as lack of support if the vendor goes out of business or the product is no longer produced. Ensuring vendor support over the product life cycle can mitigate risk, along with gaining access to source code, design requirements, verification plans, and test results. Off-line simulations of the product should also be considered. Can access be obtained to vendor information on product issues discovered by other users?

"Trade studies and risk identification must be performed before committing to the use of a particular unit and integration architecture."

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Software Systems Engineering should be involved on projects](https://software.gsfc.nasa.gov/lesson-details/33/). **Lesson Number 33**: The recommendation states: "Projects are strongly encouraged to consider including the software systems engineering role when performing project planning."
* [Ensure heritage software meets all requirements before reuse](https://software.gsfc.nasa.gov/lesson-details/57/). **Lesson Number 57**: The recommendation states: "Ensure heritage software meets all requirements before reuse, or evaluate the impact on areas where the heritage and reused requirements differ."
* [When inheriting FSW from a previous mission, evaluate the differences between the missions' requirements and/or design](https://software.gsfc.nasa.gov/lesson-details/71/). **Lesson Number 71**: The recommendation states: "When inheriting FSW from a previous mission, evaluate the differences between the missions' requirements and/or design."
* [Leverage projects to create benefits that go beyond the project](https://software.gsfc.nasa.gov/lesson-details/73/). **Lesson Number 73**: The recommendation states: "Leverage projects to create benefits that go beyond the project."
* [Use Common Ground Systems over mission life-cycles](https://software.gsfc.nasa.gov/lesson-details/103/). **Lesson Number 103**: The recommendation states: "Use Common Ground Systems over mission life-cycles as much as possible."
* [Primary Instruments should have a Programmable Processor](https://software.gsfc.nasa.gov/lesson-details/105/). **Lesson Number 105**: The recommendation states: "Primary Instruments should have a Programmable Processor."
* [Select one Command & Control System for use over the mission life cycle](https://software.gsfc.nasa.gov/lesson-details/107/). **Lesson Number 107**: The recommendation states: "Select one Command & Control System for use over the mission life cycle."
* [Ensure that the impacts of design decisions are clearly communicated](https://software.gsfc.nasa.gov/lesson-details/109/). **Lesson Number 109**: The recommendation states: "When Flight Software provides inputs to design decisions, ensure that the impacts of design decisions are clearly communicated."
* [Select data analysis platform for all Instrument Team Facilities](https://software.gsfc.nasa.gov/lesson-details/114/). **Lesson Number 114**: The recommendation states: "Select the data analysis platform for all Instrument Team Facilities (ITFs) early in the life cycle."
* [Consider innovative and "outside-the-box" approaches to risks and challenges](https://software.gsfc.nasa.gov/lesson-details/153/). **Lesson Number 153**: The recommendation states: "Consider innovative and "outside-the-box" approaches to risks and challenges."
* [AWS pricing model and discount programs](https://software.gsfc.nasa.gov/lesson-details/175/). **Lesson Number 175**: The recommendation states: "Invest time to consult with subject matter experts familiar with AWS products and discount programs during AWS migration planning stages so costing estimates are as accurate as possible."
* [AWS services availability](https://software.gsfc.nasa.gov/lesson-details/176/). **Lesson Number 176**: The recommendation states: "Ensure that AWS services of interest are available in the AWS region you selected."
* [When using OTS software, consult early on with people familiar with the software](https://software.gsfc.nasa.gov/lesson-details/281/). **Lesson Number 281**: The recommendation states: "When using off-the-shelf (OTS) software, discuss design decisions related to this software with SMEs (and if possible with the OTS developers) early on, to catch any design problems as soon as possible."
* [AWS Availability Zone - System Availability](https://software.gsfc.nasa.gov/lesson-details/294/). **Lesson Number 294**: The recommendation states: "Although the Availability Zone (AZ) is a highly available system, some services in the AZ or the entire AZ may not be available at all times (e.g. not 100% uptime). If high system availability is a requirement, design a system that can withstand an AZ outage by spreading resources across two or more AZs."
* [Near Space Network (NSN) Cloud transition challenges](https://software.gsfc.nasa.gov/lesson-details/300/). **Lesson Number 300**: The recommendation states: "When considering a transition to Cloud platform/services, keep these in mind: A delivered cloud service capability may not be as robust as needed for operations. Don't take on a Cloud instance if you don't have to; use the Cloud as a giant Network-attached storage and just pay data egress. Hire a Cloud expert even before inheriting the Cloud Concepts. Write requirements for the Cloud up front; everything should have a requirement, no matter if it needs to be built or already works; never let your management agree to accepting an operational component of the ground segment without having agreed upon requirements. A proper communication between the Project leadership and the Ground Segment Manager and PDLs is crucial. Near Space Network (NSN) services have “hidden” fees, so make sure you have a good understanding of all cost implications upfront."
* [Include File Manager, Memory Manager, and EEPROM write-enable routines early](https://software.gsfc.nasa.gov/lesson-details/303/). **Lesson Number 303**: The recommendation states: "When including reused software in the system consider adding File Manager, Memory Manager, and EEPROM write enable routines early, even in the first build, to allow the features to be used by the development and test teams.  These features can be beneficial by allowing tests to be simpler and testing to be more complete/final.  They can also be used in diagnostics, as well as in cleanup activities."
* [Have a cloud expert on the team when migrating to the cloud](https://software.gsfc.nasa.gov/lesson-details/307/). **Lesson Number 307**: The recommendation states: "When migrating operational software to the cloud, have on the team at least one cloud expert with experience in the applicable environment."
* [Rewrite outdated software before moving it to the cloud](https://software.gsfc.nasa.gov/lesson-details/308/). **Lesson Number 308**: The recommendation states: "Don’t try to move outdated software to the cloud. If you plan to keep working on it, rewrite it."
* [Use of a Mature and Proven Information Technology (IT) for Operation Centers](https://software.gsfc.nasa.gov/lesson-details/312/). **Lesson Number 312**: The recommendation states: "Projects should prefer proven IT infrastructure over starting from scratch."
* [Perform software prototyping early to increase confidence in selections](https://software.gsfc.nasa.gov/lesson-details/315/). **Lesson Number 315**: The recommendation states: "Identify and pursue early prototyping efforts in order to understand the design space and options, better prior to closing trade studies."
* [Consider weighing software sustainability over heritage](https://software.gsfc.nasa.gov/lesson-details/316/). **Lesson Number 316**: The recommendation states: "Determine how important software sustainability (especially to the length of 10-15 years) is for the project and consider prioritizing it over heritage."
* [During initial design, explore available ground systems tools from other NASA Centers to include in design trade studies](https://software.gsfc.nasa.gov/lesson-details/317/). **Lesson Number 317**: The recommendation states: "Seek demos from other NASA centers during ground software initial trade studies, in-person when possible."
* [Heritage analysis should consider all aspects of the flight software](https://software.gsfc.nasa.gov/lesson-details/337/). **Lesson Number 337**: The recommendation states: "Heritage analysis should consider operating system selection as well as framework and application software when developing a Basis of Estimate (BOE) and schedule."

# 7. Software Assurance

**SWE-033 - Acquisition vs. Development Assessment**

3.1.2 The project manager shall assess options for software acquisition versus development.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the options for software acquisition versus development have been evaluated.

2. Confirm the flow down of applicable software engineering, software assurance, and software safety requirements on all acquisition activities. (NPR 7150.2 and NASA-STD-8739.8).

3. Assess any risks with acquisition versus development decision(s).

## 7.2 Products

* **Risk Assessment Report**: Identifying and comparing risks from a software assurance perspective for acquisition versus development.
* **Compliance Evaluation**: Document adherence of each option to software assurance standards and procedures.
* **Verification Plan**: Recommendations for verifying and validating assurance practices for the chosen option.
* **Traceability Report**: Documentation showing requirement traceability through assurance-related activities (e.g., testing, risk management, security).
* **Decision Rationale**: Report documenting the assurance-based rationale for selecting acquisition or development.

7.3 Metrics

The following categories list relevant metrics that align with software assurance objectives when assessing the acquisition versus development decision.

### **7.3.1.** Risk and Quality Metrics

These metrics help evaluate potential risks and the inherent quality of both options:

1. **Defect Density**

   * **Definition**: Number of defects per unit size of the software (e.g., per 1,000 lines of code or function points).
   * **Purpose**: To measure the quality of the software by identifying potential issues in the code through vendor-supplied reports or testing of internally developed software.
   * **Comparison Use**:
     + Acquisition: Request defect reports or software assurance metrics from the vendor.
     + Development: Evaluate the historical defect density of the development team or conduct early testing of prototypes.
2. **Open Defects or Bug Backlog**

   * **Definition**: Number of unresolved, documented issues at the time of evaluation.
   * **Purpose**: To assess the current stability and readiness of the existing (acquired) software compared to development efforts.
   * **Comparison Use**:
     + Acquisition: Vendor-provided status of unresolved defects.
     + Development: Number of unresolved defects during internal testing stages.
3. **Mean Time Between Failures (MTBF)**

   * **Definition**: The average time between software system failures.
   * **Purpose**: Measures system reliability.
   * **Comparison Use**:
     + Acquisition: Use failure reports and historical data from vendor proofs of reliability.
     + Development: Collect this metric via testing of prototypes or similar software from the same team.
4. **Mean Time to Recovery (MTTR)**

   * **Definition**: The average time it takes to recover or restore the software after a failure.
   * **Purpose**: Indicates how quickly an option can resume normal operations, essential for critical systems.
   * **Comparison Use**:
     + Acquisition: Assess the vendor’s incident response and patch delivery timelines for maintenance.
     + Development: Evaluate the in-house team's ability to provide patches or fixes.
5. **Software Fault Tolerance Testing Results**

   * **Definition**: Results from fault injection testing to assess how well the software handles unexpected conditions or failures.
   * **Purpose**: To measure fault tolerance of the system.
   * **Comparison Use**:
     + Acquisition: Perform fault testing on the vendor's software or request test results.
     + Development: Execute fault testing on interim development builds.

### **7.3.2 Security Metrics**

Security is a critical software assurance attribute that directly impacts whether software can be trusted for sensitive or critical use.

1. **Number of Known Vulnerabilities**

   * **Definition**: Count of disclosed vulnerabilities in the software (e.g., from vulnerability databases, vendor reports, or scans).
   * **Purpose**: Indicates overall software security posture.
   * **Comparison Use**:
     + Acquisition: Request vulnerability scans or reports from the vendor.
     + Development: Perform in-house vulnerability scans as part of the development lifecycle.
2. **Time to Patch Vulnerabilities**

   * **Definition**: The average time it takes to identify, develop, and deploy a patch for a known vulnerability.
   * **Purpose**: Measures how quickly issues in security are resolved.
   * **Comparison Use**:
     + Acquisition: Review vendor’s historical patch delivery timelines.
     + Development: Evaluate the internal team’s track record for addressing security issues in code.
3. **Percentage of Code Passing Static Analysis Checks**

   * **Definition**: Percentage of code that passes automated static analysis checks without generating critical security warnings (e.g., using tools like Fortify, SonarQube, or Coverity).
   * **Purpose**: Evaluate code quality against secure coding standards.
   * **Comparison Use**:
     + Acquisition: If the vendor provides source code, perform static analysis.
     + Development: Run static code analysis during development phases.
4. **Compliance with Security Standards**

   * **Definition**: Level of adherence to relevant security frameworks or certifications (e.g., OWASP Top 10, NIST, SOC 2, ISO/IEC 27001).
   * **Purpose**: Ensures the software meets recognized security assurance benchmarks.
   * **Comparison Use**:
     + Acquisition: Request compliance documentation for the vendor software.
     + Development: Assess adherence to required security standards during development.

### 7.3.3 Maintainability Metrics

These metrics help evaluate the ease of maintaining and evolving the software.

1. **Cyclomatic Complexity**

   * **Definition**: A metric to measure the complexity of a program’s control flow.
   * **Purpose**: High complexity values indicate more challenging and error-prone future maintenance.
   * **Comparison Use**:
     + Acquisition: Evaluate control flow complexity if the source code is provided.
     + Development: Assess code complexity during development.
2. **Documentation Quality Score**

   * **Definition**: Subjective or objective assessment of the quality and completeness of documentation (e.g., user manuals, API documentation).
   * **Purpose**: Assesses whether the acquired software or custom-developed system will be well-documented, making future updates and debugging easier.
   * **Comparison Use**:
     + Acquisition: Evaluate vendor-supplied documentation.
     + Development: Plan for internal documentation tracking.
3. **Maintenance Effort Estimation**

   * **Definition**: Estimated effort (in person-hours or cost) needed to maintain the software over its lifecycle.
   * **Purpose**: Understand whether acquisition or development will create more maintenance burden.
   * **Comparison Use**:
     + Acquisition: Use information on vendor support services and expected customization needs.
     + Development: Estimate internal maintenance costs based on project scope and design.

### 7.3.4 Performance and Scalability Metrics

Evaluate how well the software performs and grows with demand.

1. **Execution Time or Response Time**

   * **Definition**: Time taken by the software to execute or respond to a specific operation/workload.
   * **Purpose**: Measures how quickly the software will perform under normal conditions.
   * **Comparison Use**:
     + Acquisition: Use vendor-provided benchmarks or test reports.
     + Development: Collect performance results through testing prototypes.
2. **Scalability Testing Results**

   * **Definition**: How well the software scales in terms of users, data, or transactions.
   * **Purpose**: To measure the ability of the software to handle increased demand.
   * **Comparison Use**:
     + Acquisition: Assess scalability test results from the vendor.
     + Development: Conduct scalability testing on early builds and assess the resource allocation needed.

### 7.3.5 Lifecycle and Long-Term Sustainability Metrics

Evaluate the long-term viability of the software.

1. **Vendor Dependence Score**

   * **Definition**: Assessment of how dependent you will be on the vendor for updates, maintenance, and support.
   * **Purpose**: Indicates risk of vendor lock-in for acquired software.
   * **Comparison Use**:
     + Acquisition: Evaluate vendor's update policies, support guarantees, and end-of-life policies.
     + Development: Assess whether you have the internal expertise to sustain custom development.
2. **Cost of Ownership**

   * **Definition**: Total cost incurred, including licensing, development, integration, and maintenance, over the software lifecycle.
   * **Purpose**: Compare the lifetime costs of both options relative to their assurance quality.
   * **Comparison Use**:
     + Acquisition: Total cost of licensing, support, and ongoing vendor updates.
     + Development: Total cost of development, including assurance practices, testing, and maintenance.

### **7.3.6 Summary Table of Metrics**

| **Metric** | **Acquisition** | **Development** |
| --- | --- | --- |
| Defect Density | Vendor reports | Internal testing |
| Known Vulnerabilities | Vendor documents or scans | Vulnerability scans |
| Mean Time Between Failures (MTBF) | Vendor data | Internal test data |
| Time to Patch Vulnerabilities | Vendor patch timelines | Development schedule |
| Cyclomatic Complexity | Source code analysis (if allowed) | Static analysis during development |
| Scalability Testing Results | Vendor performance tests | Internal testing |
| Cost of Ownership | License + vendor support | Development cost + maintenance cost |

  

By selecting appropriate metrics, the project team can assess both acquisition and development options objectively, ensuring the final decision meets software assurance requirements for quality, reliability, security, and maintainability.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

Good software assurance guidance for this requirement ensures that software quality, reliability, and safety are thoroughly considered during the acquisition-development decision process. For software assurance specifically, the emphasis is on evaluating software risks, compliance, and how both options (acquisition or development) align with software assurance objectives such as safety, security, maintainability, and performance.

### 7.4.1 Structured Approach

Here’s a structured approach to providing **software assurance guidance** for this requirement:

#### 1. **Ensure Requirements Are Well Defined**

* Verify that the functional, non-functional, and regulatory requirements for the software are clear and complete. Software assurance focuses on ensuring that these requirements address key areas such as:
  + Safety-critical functions
  + Cybersecurity and data privacy
  + System reliability
  + Maintainability and scalability
* These parameters are essential when assessing whether acquisition or development is the better choice.

#### 2. **Identify Software Risks**

Evaluate risks related to acquisition versus development from a software assurance perspective:

* **Acquisition Risks**:
  + Vendor may not meet quality standards (e.g., unreliable or insecure prebuilt software).
  + Lack of accountability and transparency in the vendor’s software assurance practices.
  + Compatibility or integration issues with your existing systems.
  + Inability to verify the vendor’s quality assurance (QA) processes.
  + Difficulty in obtaining code-level assurance if the source code is inaccessible.
* **Development Risks**:
  + Custom development risks include insufficient testing, inexperienced development teams, lack of adherence to accepted software assurance standards, and failure to meet required software quality attributes.
  + Increased complexity and longer timelines may lead to inconsistent implementation of assurance practices.

#### 3. **Evaluate Compliance and Standards**

* Assess compliance with organizational, industry, and regulatory software assurance standards for both acquisition and development options.
* **Key Considerations**:
  + Does the vendor follow recognized standards (e.g., ISO/IEC 25010 for software quality, IEEE 12207 for software lifecycle processes)?
  + Will custom-developed software be required to meet specific assurance-related standards (e.g., NASA-STD-8739.8, DO-178C for airborne software, etc.)?

#### 4. **Review Quality Assurance Processes**

* **For Acquisition**:
  + Request evidence of the vendor’s software assurance practices, such as documentation of testing, quality management, bug fixes, and validation.
  + Confirm security features, including secure coding practices, vulnerability scans, and penetration test results.
  + Assess the frequency and process for delivering updates and patches to ensure ongoing reliability and security.
* **For Development**:
  + Ensure your development team has formalized software assurance processes, including appropriate use of verification and validation (V&V) activities, unit testing, and integration testing.
  + Verify the skills and tools available to manage key software assurance activities, such as static code analysis, dynamic testing, and fault injection testing.

#### 5. **Assess Lifecycle Support**

* Evaluate the ability to sustain and maintain the software over the lifecycle:
  + **Acquisition**: Verify that the vendor will provide adequate lifecycle support, including regular updates, security patches, and bug fixes. Confirm the vendor’s end-of-life policies.
  + **Development**: Assess whether your organization has the infrastructure and resources to maintain custom-developed software, including issue tracking, testing, patch management, and updates.

#### 6. **Consider Security and Data Privacy**

* Ensure that security and data privacy are part of the decision criteria:
  + **Acquisition**: Assess the vendor’s ability to provide secure software (e.g., encryption, authentication, secure APIs). Examine certifications related to application security (e.g., SOC 2, FIPS 140-2).
  + **Development**: Confirm your internal team’s ability to incorporate secure coding practices, conduct threat modeling, and perform vulnerability assessments throughout the development lifecycle.

#### 7. **Perform Independent Verification and Validation (IV&V)**

* For both acquisition and development options:
  + Identify how IV&V roles can be integrated to verify the adequacy of software assurance processes.
  + If possible, perform an independent review of the vendor’s COTS solution to ensure it meets your reliability and assurance goals before a final decision.

#### 8. **Maintain Traceability**

* Ensure traceability of software assurance requirements through both options:
  + For acquisition: Verify that the vendor can provide traceability between your requirements and their existing solution, including architecture, design, and testing processes.
  + For development: Confirm that your team will establish traceability throughout the software lifecycle, from initial requirements to code and test cases.

#### 9. **Cost-Benefit Analysis from an Assurance Perspective**

* Incorporate software assurance-specific factors into the cost-benefit analysis:
  + How does the acquisition or development option address assurance requirements for safety, security, quality, and performance?
  + What are the costs associated with addressing assurance gaps (e.g., securing a prebuilt solution versus implementing robust assurance practices in custom development)?

#### 10. **Address Configuration Management**

* Determine how software configuration management will be maintained:
  + For acquisition: Verify how updates, patches, and versioning will be handled by the vendor and the mechanisms for applying changes.
  + For development: Ensure that proper configuration management tools and processes are in place for tracking changes throughout development and deployment.

#### 11. **Monitor and Measure Software Assurance Metrics**

* Before making a final decision, compare acquisition versus development options based on measurable software assurance metrics, such as:
  + Defect density (quality)
  + Number of open vulnerabilities (security)
  + Mean time to failure (reliability)
  + Time to restore (maintainability)

#### 12. **Sustainability and Vendor Lock-in**

* Evaluate how either option impacts long-term sustainability and ongoing assurance:
  + Acquisition: Assess risks related to vendor lock-in and the ability to ensure assurance if the vendor ceases operations.
  + Development: Consider the sustainability of in-house expertise and the cost of continuously evolving software assurance practices.

---

### 7.4.2 Deliverables for Software Assurance on This Requirement

1. **Risk Assessment Report**: Identifying and comparing risks from a software assurance perspective for acquisition versus development.
2. **Compliance Evaluation**: Document adherence of each option to software assurance standards and procedures.
3. **Verification Plan**: Recommendations for verifying and validating assurance practices for the chosen option.
4. **Traceability Report**: Documentation showing requirement traceability through assurance-related activities (e.g., testing, risk management, security).
5. **Decision Rationale**: Report documenting the assurance-based rationale for selecting acquisition or development.

### 7.4.3 Key Considerations

* For **small projects**, software assurance criteria should be scaled appropriately. Keep the focus on critical assurance risks that have the greatest potential to impact the project's success (e.g., security, reliability, maintainability).
* Software assurance professionals should work closely with project managers to ensure assurance concerns are factored into every stage of the assessment and decision-making process.

By integrating software assurance considerations into the evaluation of acquisition versus development, you ensure the chosen option meets quality, reliability, and safety requirements while effectively managing costs, risks, and lifecycle support.

Planning the software assurance on any project requires an understanding of the project’s function, needs, and risk posture as well as Software Class and criticality. Software Assurance needs to work with the software development team to assure that the software development processes are planned well and are based on the project and software criteria, as appropriate.

Software Assurance also needs to assure any acquisition process is adequate and complete and that criteria are set up to eventually assure the delivery of needed software products and reports.  Once these criteria are established, software assurance can create their plans and assure the appropriate SA needs are provided, e.g. sufficient personnel to perform the SA activities, any needed training on the project development processes and functionality, needed tools, and access to project data, products and activities.

When the software project is in the process of determining whether to “make or buy” their software, the software assurance should review the process used to make the decision. Although the process is often not followed with strict formality, these basic steps below should be considered:

* Use Guidelines for Decision Analysis
* Establish Evaluation Criteria
* Identify Alternative Solutions
* Select Evaluation Methods
* Evaluate Alternatives
* Select Solutions
* Document Solution and Rationale

Software assurance should evaluate the alternatives identified and investigated review the rationale used to make the selection. SA should document any risks identified with the choice. Some risk areas to consider include:

Will long-term maintenance support the products? Will the provider support requested changes to the product? Would update costs be reasonable? Does the product have a government-approved license? Is the source code available? Is the provider a stable company (that will be around for future support)? Is any new technology being proposed/used? Will there be any security risks?

Open Source licenses need to be reviewed by the Center Chief of Patent/Intellectual Property Counsel before being accepted into software development projects.

The Software assurance organization supports acquisition in determining whether all the appropriate SA support activities are included in the solicitations, contract, or task order, and in evaluating whether the proposed SA support activities have realistic cost estimates. The software assurance organization should also be supporting any acquisitions by making sure that all the requirements are flowed down to the contractor. These include at a minimum, NPR-7150.2 [083](#_tabs-<p></p>) , NASA-STD–8739.8 [278](#_tabs-<p></p>)  , any Center level requirements, as well as the requirements for the project, including metrics and other deliverables needed for insight/oversight.

All solicitations should be checked to see if there is software included. Often, the software is included in the products such as tools, facilities, cameras, test equipment, instruments, etc. Failure to assure COTS and embedded software in purchased software has led to failures or serious losses.

Any risks or issues with decision or rationale are brought to the attention of management.

The Agency Software Manager can be used as a resource for this confirmation.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions)        * [6.3 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SWEHBVD/pages/102695560/6.3+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-025 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SITE/pages/116294244/PAT-025+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) |

# 8. Objective Evidence

Objective evidence is critical for demonstrating compliance with software assurance standards and supporting an informed decision between acquisition and development. Good objective evidence provides tangible, verifiable, and documented data that substantiate the analysis and evaluation of each option.

When assessing compliance with this requirement it's important to collect objective evidence that demonstrates thorough and documented evaluation. Objective evidence should include documentation, analysis, and decision-making artifacts that clearly show the assessment process.

## 8.1 Examples of Good Objective Evidence:

1. **Documented Evaluation Criteria**:

   * A document outlining criteria for assessment, such as cost, time to deployment, scalability, maintainability, security, support, and alignment with project goals.
2. **Make-versus-Buy Analysis**:

   * A formal report or spreadsheet showing the comparative analysis of software acquisition (buying) versus in-house development, including:
     + Cost estimates (initial, operational, and maintenance costs).
     + Resource availability (e.g., skilled staff, infrastructure).
     + Time estimates for deployment.
     + Risk assessment for both options.
     + Long-term impacts like vendor dependency or customizability.
3. **Stakeholder Input and Meeting Minutes**:

   * Recorded minutes or notes from meetings where stakeholders (e.g., technical leads, procurement teams, and project sponsors) discussed the pros and cons of acquisition versus development.
4. **Vendor Research and Evaluation**:

   * Evidence of market research for available software solutions, such as:
     + Vendor comparison charts.
     + Product demonstrations or trial evaluations.
     + Requests for information (RFIs) or proposals (RFPs) sent to vendors.
     + Vendor responses and evaluations.
5. **Prototyping or Feasibility Study**:

   * Results from a feasibility study or prototypes/pilots that compare software acquisition solutions with internal development.
6. **Risk Assessment Report**:

   * A document identifying and quantifying potential risks for both acquisition and development options, such as:
     + Uncertain vendor support.
     + Intellectual property conflicts.
     + Technical integration challenges.
7. **Cost–Benefit Analysis**:

   * Documented cost–benefit analysis, including total cost of ownership (TCO), return on investment (ROI), and break-even point for acquisition vs. development.
8. **Decision Matrix or Trade Study**:

   * A decision matrix or trade-off analysis scoring the software acquisition and development options against predefined criteria. The matrix should include clear justifications for the scores.
9. **Project Plan Updates**:

   * Evidence that the selected option (acquisition or development) was incorporated into subsequent project documentation, like the project management plan, software development plan, or procurement plan.
10. **Approval Records**:

    * Formal approval document (e.g., signed decision memo) showing that the decision to acquire or develop software was reviewed and approved by the appropriate authority (e.g., project sponsor, steering committee).
11. **Regulatory or Contractual Compliance Analysis**:

    * Evidence showing how the acquisition or development approach complies with relevant regulations, standards, or contractual obligations.

### Key Points for Evidence:

* The evidence must be clear, specific, and traceable to the decision-making process.
* It should demonstrate that the project manager conducted a balanced and objective assessment.
* It must show that the assessment was documented and communicated to relevant stakeholders.
* If a decision-making tool (e.g., decision matrix, cost analysis tool) was used, it should include source data, assumptions, and rationale.

By having these types of evidence, you can objectively demonstrate compliance with the requirement to assess options for software acquisition versus development.

Definition of objective evidence

Objective evidence is an unbiased, documented fact showing that an activity was confirmed or performed by the software assurance/safety person(s). The evidence for confirmation of the activity can take any number of different forms, depending on the activity in the task. Examples are:

* Observations, findings, issues, risks found by the SA/safety person and may be expressed in an audit or checklist record, email, memo or entry into a tracking system (e.g. Risk Log).
* Meeting minutes with attendance lists or SA meeting notes or assessments of the activities and recorded in the project repository.
* Status report, email or memo containing statements that confirmation has been performed with date (a checklist of confirmations could be used to record when each confirmation has been done!).
* Signatures on SA reviewed or witnessed products or activities, or
* Status report, email or memo containing a short summary of information gained by performing the activity. Some examples of using a “short summary” as objective evidence of a confirmation are:
  + To confirm that: “IV&V Program Execution exists”, the summary might be: IV&V Plan is in draft state. It is expected to be complete by (some date).
  + To confirm that: “Traceability between software requirements and hazards with SW contributions exists”, the summary might be x% of the hazards with software contributions are traced to the requirements.
* The specific products listed in the Introduction of 8.16 are also objective evidence as well as the examples listed above.

Below are examples of quality objective evidence for **software assurance** related to this requirement:

## 8.2 Objective Evidence for Software Acquisition Option

#### 8.2.1 Vendor Documentation

* Software quality reports (defects, error rates, performance metrics).
* Test results demonstrating the reliability, security, scalability, and compliance with standards (e.g., ISO/IEC 25010, OWASP Top 10, etc.).
* Certification documentation (e.g., ISO/IEC 27001 for security, SOC 2 compliance).
* Statements of applicability for regulatory standards (e.g., for safety-critical systems, data privacy law compliance).
* Detailed system architecture and design documentation for COTS (Commercial off-the-shelf) software.
* Maintenance agreements and upgrade policies (e.g., frequency of patches, vendor support capabilities).

#### 8.2.2 Security Assessment Reports

* Results of vulnerability assessments, penetration tests, or security audits conducted by the vendor or third-party assessors.
* Signed verification of encryption protocols (if data protection is needed).
* Records of secure coding practices followed by the vendor.

#### 8.2.3 Compatibility and Integration Reports

* Integration test results showing compatibility with existing systems or environments.
* API documentation and integration guides.
* Assessments or certifications verifying compatibility with legacy systems or required platforms.

#### 8.2.4 Known Issue Logs

* Vendor-provided defect or issue logs showing current unresolved issues with their software.
* Bug fix timetables and evidence of ongoing issue resolution.

#### 8.2.5 Performance Specifications

* Load, performance, and stress testing results provided by the vendor (e.g., scalability testing under simulated environments).
* Benchmarks for operational efficiency (e.g., resource usage metrics, response time).

#### 8.2.6 Software Assurance Process Reports

* Documentation showing quality assurance measures applied by the vendor during development (V&V processes, configuration management, regression testing, etc.).
* Change management and version control documentation for the vendor's product lifecycle.

#### 8.2.7 User Feedback and Case Studies

* Customer testimonials or third-party reviews of the software's quality, reliability, and ease of maintenance based on real-world usage.
* Case studies demonstrating successful deployment and long-term use by similar industries or organizations.

#### 8.2.8 Licensing and Support Agreements

* SLA (Service Level Agreement) that guarantees software assurance support (e.g., bug fixes, updates, response time).
* Evidence of long-term sustainability (e.g., vendor’s commitment to upgrading software over time).

## 8.3 Objective Evidence for Software Development Option

### 8.3.1 Requirements Traceability Matrix (RTM)

* Traceability matrix linking functional and non-functional requirements directly to design, implementation, test plans, and verification activities.
* Ensures that every requirement has been addressed, validated, and tested.

### 8.3.2 Testing Results

* Results from unit tests, integration tests, system tests, and acceptance tests.
* Defect logs and corrective action records from testing phases.
* Regression testing results to demonstrate the stability of new features or bug fixes.

### 8.3.3 Software Security Analysis

* Static and dynamic code analysis results conducted during the development lifecycle.
* Security findings from threat modeling sessions and vulnerability assessments.
* Documentation of secure coding practices (peer reviews, automated scans, adherence to coding standards).

### 8.3.4 Verification and Validation (V&V) Records

* V&V plans, procedures, and results showing independent verification of software behavior against requirements.
* Evidence of simulation or emulation testing for critical systems.

### 8.3.5 Architecture and Design Documentation

* Completed and reviewed software architecture diagrams, system design documentation, and module specifications.
* Records of software assurance considerations embedded in the design phase, such as fault tolerance requirements or security-by-design principles.

### 8.3.6 Configuration Management Evidence

* Logs from configuration management systems, showing tracking of code versions, change records, and approval workflows.
* Documentation demonstrating strict adherence to version control policies (e.g., Git logs, change control forms).

### 8.3.7 Code Quality Reports

* Results of code quality assessments using tools such as SonarQube, Coverity, or Fortify.
* Metrics such as cyclomatic complexity, maintainability index, or technical debt analysis.

### 8.3.8 Cost-Estimation and Effort Logs

* Detailed records of estimated development costs, timelines, and resources versus actual costs and durations during prototype phases.
* Logs showing team training efforts, onboarding, or capability-building activities needed to support the project.

### 8.3.9 Risk Analysis Reports

* Risk identification and mitigation plans specific to the software assurance objectives (e.g., reliability, safety).
* Documentation of risks encountered during early development phases and how they were addressed.
* Fault tree analysis or failure mode and effects analysis (FMEA) documentation.

### 8.3.10 Peer Reviews and Code Inspections

* Meeting minutes and reports from peer code reviews and design inspections involving developers and software assurance personnel.
* Results and corrective actions from reviews conducted at key development milestones.

### 8.3.11 Scalability Testing Results

* Benchmark tests of the custom-built solution under simulated workloads to verify scalability.
* Documentation of how the system adapts to increasing user demand or data input.

### 8.3.12 Compliance Checklist

* Checklist verifying compliance with applicable standards and organizational policies (e.g., NASA-STD-8739.8, ISO/IEC 25010).
* Supporting evidence that required assurance objectives (safety, security, quality) have been validated.

## 8.4 Common Evidence for Both Acquisition and Development

#### **Cost-Benefit Analysis**

* Detailed cost comparison documents showing acquisition and development costs (licensing costs, support costs, development effort, resource allocation, long-term maintenance).

#### **Decision Matrix**

* Weighted decision matrix comparing acquisition versus development options based on assurance criteria, such as risk likelihood, defect probability, security readiness, lifecycle support, and long-term viability.

#### **Independent Verification and Validation (IV&V) Reports**

* Results of independent reviews verifying that either chosen software (acquired or developed) meets quality and assurance expectations.
* IV&V audits focused on assurance attributes such as reliability, maintainability, and security.

## 8.5 Checklist **of Objective Evidence for Compliance**

| **Category** | **Example Evidence** | **Acquisition** | **Development** |
| --- | --- | --- | --- |
| Requirements Traceability | RTM | ✓ | ✓ |
| Security Reports | Vulnerability assessments, penetration tests | ✓ | ✓ |
| Testing Reports | Unit, integration, system, and acceptance tests | ✓ | ✓ |
| Quality Metrics | Defect density, cyclomatic complexity, MTBF | ✓ | ✓ |
| Architecture Documentation | Architecture and design diagrams | ✓ | ✓ |
| Configuration Management Logs | Version control logs, change approvals | ✓ | ✓ |
| Cost Analysis | Detailed cost-benefit analysis | ✓ | ✓ |
| Performance Benchmarks | Load and stress testing results | ✓ | ✓ |
| Vendor/Team Process Documentation | QA and V&V process adherence | ✓ | ✓ |
